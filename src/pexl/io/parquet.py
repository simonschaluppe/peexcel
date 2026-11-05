"""Bounded-memory annual Excel-to-Parquet conversion for recorded batch runs."""
from collections import Counter, defaultdict
from datetime import date, datetime, time as datetime_time
import hashlib
import json
import logging
import math
from pathlib import Path
from time import perf_counter
from uuid import uuid4

import openpyxl
import pyarrow as pa
import pyarrow.parquet as pq

logger = logging.getLogger(__name__)
SHEETS = ("IN", "OUT")
ID_COLUMNS = ("batch", "scenario_name", "source_file")

def _sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _discover_sources(directory: Path):
    manifest_path = directory / "batch.json"
    if not manifest_path.is_file():
        raise FileNotFoundError(f"Batch-Manifest fehlt: {manifest_path}")

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("failed"):
        logger.warning("Batch enthält fehlgeschlagene Szenarien; exportiere abgeschlossene Chunks")

    chunks = manifest.get("chunks", [])
    if not chunks:
        raise ValueError("Das Batch-Manifest enthält keine Chunks.")

    by_file = {chunk["annual"]: chunk for chunk in chunks}
    if len(by_file) != len(chunks):
        raise ValueError("Doppelte annual-Dateinamen im Manifest.")

    paths = []
    for filename in by_file:
        path = directory / filename
        if path.parent.resolve() != directory.resolve() or not path.is_file():
            raise ValueError(f"Ungültige oder fehlende Quelldatei: {filename}")
        paths.append(path)
    extra = {p.name for p in directory.glob("annual-*.xlsx")} - set(by_file)
    if extra:
        logger.warning("Ignoriere %d annual-Dateien außerhalb des Manifests", len(extra))

    all_names = [name for chunk in chunks for name in chunk["scenarios"]]
    if not all_names or len(all_names) != len(set(all_names)):
        raise ValueError("Szenarionamen im Batch sind leer oder nicht eindeutig.")

    selected = manifest.get("selected", {}).get("data", [])
    if selected and len(selected) != len(all_names):
        logger.warning("Teilbestand: %d von %d geplanten Szenarien", len(all_names), len(selected))
    return manifest, paths, by_file, len(all_names)


def _read_annual(path: Path, scenario_names: list[str]) -> dict[str, dict]:
    """Liest IN/OUT als {sheet: {var_name: [Werte pro Szenario]}}.

    Der Rückgabewert umfasst nur ein einzelnes Quelldokument im Speicher.
    """
    workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
    try:
        result = {}
        for sheet_name in SHEETS:
            if sheet_name not in workbook.sheetnames:
                raise ValueError(f"{path.name}: Tabellenblatt {sheet_name} fehlt")

            rows = iter(workbook[sheet_name].iter_rows())
            try:
                header = [cell.value for cell in next(rows)]
            except StopIteration as exc:
                raise ValueError(f"{path.name}/{sheet_name}: leeres Blatt") from exc

            while header and header[-1] is None:
                header.pop()
            if len(header) != len(set(header)) or "var_name" not in header:
                raise ValueError(f"{path.name}/{sheet_name}: ungültige oder doppelte Spaltennamen")

            missing = [name for name in scenario_names if name not in header]
            if missing:
                raise ValueError(f"{path.name}/{sheet_name}: Szenariospalten fehlen: {missing[:5]}")
            scenario_indices = [header.index(name) for name in scenario_names]
            if scenario_indices != sorted(scenario_indices):
                raise ValueError(f"{path.name}/{sheet_name}: Szenarioreihenfolge weicht vom Manifest ab")

            key_index = header.index("var_name")
            variables = {}
            for row in rows:
                key = row[key_index].value
                if key is None and all(cell.value is None for cell in row):
                    continue  # leere Abschlusszeilen
                if not isinstance(key, str) or not key:
                    raise ValueError(f"{path.name}/{sheet_name}: leere/ungültige var_name-Zeile")
                if key in variables or key in ID_COLUMNS:
                    raise ValueError(f"{path.name}/{sheet_name}: doppelte/reservierte Variable {key!r}")

                values = []
                for column_index in scenario_indices:
                    cell = row[column_index]
                    if cell.data_type == "e":
                        logger.warning("%s/%s/%s: Excel-Fehler %s als Text erhalten", path.name, sheet_name, key, cell.value)
                    value = cell.value
                    if isinstance(value, (int, float)) and not isinstance(value, bool):
                        if not math.isfinite(value):
                            raise ValueError(f"{path.name}/{sheet_name}/{key}: nichtendlicher Wert")
                    values.append(value)
                variables[key] = values

            result[sheet_name] = variables
        return result
    finally:
        workbook.close()


def _value_kind(value):
    if value is None:
        return None
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        return "int"
    if isinstance(value, float):
        return "float"
    if isinstance(value, (date, datetime, datetime_time)):
        return "text"  # später ISO-Text
    return "text"


def _arrow_type(kinds: set[str]) -> pa.DataType:
    if not kinds or "text" in kinds:
        return pa.string()
    if kinds == {"bool"}:
        return pa.bool_()
    if kinds == {"int"}:
        return pa.int64()
    return pa.float64()


def _inspect_types(paths, chunks, verify_hashes=False):
    variable_order = {}
    kind_sets = {sheet: defaultdict(set) for sheet in SHEETS}
    sentinels = Counter()
    start = perf_counter()

    for index, path in enumerate(paths, start=1):
        chunk = chunks[path.name]
        if verify_hashes:
            actual = _sha256(path)
            expected = chunk["files"][path.name]
            if actual != expected:
                raise ValueError(f"SHA256-Abweichung: {path.name}")

        tables = _read_annual(path, chunk["scenarios"])
        for sheet, variables in tables.items():
            names = list(variables)
            if sheet in variable_order and names != variable_order[sheet]:
                raise ValueError(f"{path.name}/{sheet}: abweichende Variablenliste/Reihenfolge")
            variable_order.setdefault(sheet, names)
            for name, values in variables.items():
                for value in values:
                    kind = _value_kind(value)
                    if kind is not None:
                        kind_sets[sheet][name].add(kind)
                    if (isinstance(value, (int, float)) and not isinstance(value, bool)
                            and -2146826300 <= value <= -2146826200):
                        sentinels[(sheet, name)] += 1

        if index % 50 == 0 or index == len(paths):
            logger.info("Schema geprüft: %d/%d Dateien", index, len(paths))

    logger.info("Schema-Passage abgeschlossen (%.1f s)", perf_counter() - start)
    return variable_order, kind_sets, sentinels


def _convert_value(value, dtype: pa.DataType):
    if value is None:
        return None
    if pa.types.is_string(dtype):
        if isinstance(value, (date, datetime, datetime_time)):
            return value.isoformat()
        return value if isinstance(value, str) else str(value)
    if pa.types.is_boolean(dtype):
        return bool(value)
    if pa.types.is_integer(dtype):
        return int(value)
    if pa.types.is_floating(dtype):
        return float(value)
    raise TypeError(f"Nicht unterstützter Arrow-Typ: {dtype}")


def export_annual_batch(source_dir, output_dir, *, batch_id=None,
                        files_per_row_group=8, compression="zstd", verify_hashes=False):
    """Consolidate recorded annual IN/OUT chunks into scenarios.parquet.

    Parameters
    ----------
    source_dir : path-like
        Typology run containing batch.json and annual-*.xlsx. Only manifest
        chunks are read, in manifest order. Cached Excel values are required.
    output_dir : path-like
        Destination directory. A successful conversion atomically replaces
        scenarios.parquet. Existing results remain readable if conversion fails.
    batch_id : str, optional
        Stable run identifier, defaulting to source_dir.name. Use distinct IDs
        for runs that should be compared together.
    files_per_row_group : int
        Number of source chunks buffered for each Parquet row group (default 8).
    compression : str
        PyArrow Parquet compression codec, default zstd.
    verify_hashes : bool
        Optionally compare source SHA256 hashes with the batch manifest.

    Returns
    -------
    pathlib.Path
        Completed scenarios.parquet, directly readable with pandas.read_parquet.
        Rows represent scenarios, columns retain raw canonical variable names.
        Identity columns are batch, scenario_name and source_file. Embedded
        ``pexl.batch`` JSON metadata records provenance and schema information.

    Notes
    -----
    Two streaming Excel passes determine column types and write bounded groups.
    Mixed text/numeric columns become strings with a warning. COM error numbers
    are preserved with a warning. Failed or unfinished runs export their recorded
    completed chunks with a warning. Missing files, ambiguous identities and
    incompatible column layouts raise because they prevent a faithful export.
    Progress is logged through this module's logger; configure logging in the
    calling application. No handlers are installed by the library.
    """
    if not isinstance(files_per_row_group, int) or files_per_row_group < 1:
        raise ValueError("files_per_row_group must be a positive integer")
    directory, output = Path(source_dir).resolve(), Path(output_dir).resolve()
    manifest_bytes = (directory / "batch.json").read_bytes()
    manifest, paths, chunks, expected = _discover_sources(directory)
    snapshots = {p: (p.stat().st_size, p.stat().st_mtime_ns) for p in paths}
    started = perf_counter()
    logger.info("Konvertiere %d Dateien / %d Szenarien aus %s", len(paths), expected, directory)
    order, kinds, sentinels = _inspect_types(paths, chunks, verify_hashes)
    fields = [pa.field(name, pa.string()) for name in ID_COLUMNS]
    for sheet in SHEETS:
        for name in order[sheet]:
            observed = kinds[sheet][name]
            if len(observed) > 1 and ("text" in observed or "bool" in observed):
                logger.warning("Gemischte Typen für %s/%s: %s", sheet, name, sorted(observed))
            fields.append(pa.field(name, _arrow_type(observed)))
    if len({field.name for field in fields}) != len(fields):
        raise ValueError("IN/OUT contain duplicate variable names; a combined column would be ambiguous")
    if sentinels:
        logger.warning("%d numerische Excel-Fehlercodes als Quellwerte erhalten", sum(sentinels.values()))
    run_id = str(batch_id or directory.name)
    metadata = dict(batch=run_id, source_directory=str(directory),
                    schema=manifest.get("identity", {}).get("schema"),
                    manifest_sha256=hashlib.sha256(manifest_bytes).hexdigest(),
                    scenario_count=expected, source_file_count=len(paths),
                    failed=manifest.get("failed", {}),
                    planned_count=len(manifest.get("selected", {}).get("data", [])),
                    hashes_verified=verify_hashes,
                    variables=order)
    schema = pa.schema(fields, metadata={b"pexl.batch": json.dumps(metadata).encode("utf8")})
    output.mkdir(parents=True, exist_ok=True)
    target = output / "scenarios.parquet"
    pending = output / f".{uuid4().hex}.pending.parquet"
    try:
        buffer = []
        with pq.ParquetWriter(pending, schema, compression=compression) as writer:
            for index, path in enumerate(paths, 1):
                names = chunks[path.name]["scenarios"]
                tables = _read_annual(path, names)
                data = {"batch": [run_id] * len(names), "scenario_name": names,
                        "source_file": [path.name] * len(names)}
                for sheet in SHEETS:
                    if list(tables[sheet]) != order[sheet]:
                        raise ValueError(f"Source layout changed during conversion: {path.name}/{sheet}")
                    for name, values in tables[sheet].items():
                        data[name] = [_convert_value(value, schema.field(name).type) for value in values]
                buffer.append(pa.Table.from_pydict(data, schema=schema))
                if index % files_per_row_group == 0 or index == len(paths):
                    writer.write_table(pa.concat_tables(buffer))
                    buffer.clear()
                    logger.info("Parquet geschrieben: %d/%d Dateien", index, len(paths))
        if pq.ParquetFile(pending).metadata.num_rows != expected:
            raise ValueError("Converted scenario count differs from manifest")
        if manifest_bytes != (directory / "batch.json").read_bytes() or any(
            snapshots[p] != (p.stat().st_size, p.stat().st_mtime_ns) for p in paths
        ):
            raise ValueError("Source run changed during conversion; retry after the batch has finished")
        pending.replace(target)
    except Exception:
        logger.exception("Parquet-Konvertierung fehlgeschlagen: %s", directory)
        try:
            pending.unlink(missing_ok=True)
        except OSError:
            logger.warning("Temporäre Datei konnte nicht entfernt werden: %s", pending)
        raise
    logger.info("Parquet fertig: %s (%.1f s)", target, perf_counter() - started)
    return target
