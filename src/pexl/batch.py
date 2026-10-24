"""Python orchestration of PEExcel's single-scenario VBA contract.

Annual chunks are ordinary Project Excel exports. Only a small resume manifest
is batch-specific; no Excel automation objects escape this module.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
from time import sleep
from typing import Mapping

import pandas as pd

from pexl.io.excel import read_project, write_project_excel
from pexl.io._project_tables import RESERVED_IN_COLUMN_HEADER_SET, RESERVED_OUT_COLUMN_HEADER_SET
from pexl.io.excel_com import PEExcelAdapter
from pexl.model.project import Project
from pexl.schema.current import SCHEMA_VERSION


@dataclass
class BatchResult:
    """Completed includes verified resumed scenarios; failed maps names to errors."""
    completed: list[str] = field(default_factory=list)
    failed: dict[str, str] = field(default_factory=dict)
    exported_files: list[Path] = field(default_factory=list)
    skipped: list[str] = field(default_factory=list)
    status: str = "completed"


def _sha(path):
    digest = hashlib.sha256()
    with Path(path).open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _read_definitions(source):
    if isinstance(source, pd.DataFrame):
        return source.copy()
    path = Path(source)
    if path.suffix.lower() == ".csv":
        return pd.read_csv(path, sep=None, engine="python")
    with pd.ExcelFile(path) as book:
        sheet = next((s for s in ("Scenarios", "SCEN") if s in book.sheet_names), None)
        if sheet is None and len(book.sheet_names) != 1:
            raise ValueError("Scenario workbook needs a Scenarios or SCEN sheet, or exactly one sheet")
        return pd.read_excel(book, sheet_name=sheet or book.sheet_names[0])


def _validate_definitions(frame, available):
    if frame.empty or frame.columns.has_duplicates:
        raise ValueError("Scenario definitions must be non-empty with unique columns")
    required = {"Scenario Name", "Base Scenario"}
    if not required.issubset(frame):
        raise ValueError(f"Scenario definitions require columns {sorted(required)}")
    unknown = set(frame.columns) - set(available)
    if unknown:
        raise ValueError(f"Unknown Scenarios columns: {sorted(unknown)}")
    names = frame["Scenario Name"]
    if names.map(lambda x: not isinstance(x, str) or not x.strip()).any() or names.duplicated().any():
        raise ValueError("Scenario Name must contain unique non-empty strings")
    reserved = RESERVED_IN_COLUMN_HEADER_SET | RESERVED_OUT_COLUMN_HEADER_SET
    if set(names) & reserved:
        raise ValueError("Scenario Name collides with an export metadata column")
    if frame["Base Scenario"].map(lambda x: not isinstance(x, str) or not x.strip()).any():
        raise ValueError("Every scenario needs a non-empty Base Scenario")


def _atomic_json(path, value):
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    _replace(temporary, path)


def _replace(temporary, target):
    # Windows indexers/virus scanners can briefly hold an otherwise closed file.
    for attempt in range(4):
        try:
            return temporary.replace(target)
        except PermissionError:
            if attempt == 3:
                raise
            sleep(0.05 * (2 ** attempt))


def run_batch(
    workbook: str | Path,
    *,
    scenarios: str | Path | pd.DataFrame | None = None,
    scenario_filter: Mapping[str, object] | None = None,
    batch_size: int = 25,
    base_reload: str = "always",
    export_annual: bool = True,
    export_timeseries: bool = False,
    output_dir: str | Path = "results/batch",
    resume: bool = False,
) -> BatchResult:
    """Run selected SCEN rows one at a time and capture results immediately.

    ``scenarios`` optionally supplies a CSV, Excel sheet or DataFrame with SCEN
    headers. Its configuration temporarily replaces SCEN and is restored on exit.
    ``scenario_filter`` applies exact equality to columns, preserving row order.

    ``batch_size`` is the maximum number of scenarios per annual output file,
    not the number selected in Excel. ``first_only`` reloads at session start
    and whenever Base Scenario changes; use it only for complete independent
    preset definitions. ``always`` prevents input carry-over and is the default.

    Resume verifies workbook/configuration/schema/options and hashes of all
    committed files. It re-runs any interrupted, uncommitted chunk. Do not edit
    the workbook, definitions or result directory concurrently. The first error
    stops execution, returning ``status='failed'``; earlier successes are saved.
    Setup/export errors and KeyboardInterrupt propagate. No workbook is saved.
    """
    if isinstance(batch_size, bool) or not isinstance(batch_size, int) or not 1 <= batch_size <= 1000:
        raise ValueError("batch_size must be an integer from 1 to 1000")
    if base_reload not in {"always", "first_only"}:
        raise ValueError("base_reload must be 'always' or 'first_only'")
    if not export_annual and not export_timeseries:
        raise ValueError("Enable at least one result export")
    if resume and not export_annual:
        raise ValueError("resume requires annual Project exports")
    workbook = Path(workbook).resolve(strict=True)
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    # Exclusive creation avoids two writers sharing checkpoint names.
    lock = output_dir / ".batch.lock"
    with lock.open("x", encoding="utf-8") as stream:
        stream.write("Batch in progress; after a hard crash remove only after Excel has stopped.\n")
    try:
        return _run(workbook, scenarios, scenario_filter, batch_size, base_reload,
                    export_annual, export_timeseries, output_dir, resume)
    finally:
        lock.unlink()


def _run(workbook, scenarios, filters, batch_size, base_reload, annual, timeseries, directory, resume):
    result = BatchResult()
    manifest_path = directory / "batch.json"
    if not resume and (manifest_path.exists() or list(directory.glob("annual-*.xlsx"))
                       or list(directory.glob("sim-*.csv"))):
        raise FileExistsError("Batch outputs already exist; use resume=True or a new output directory")
    with PEExcelAdapter(workbook) as excel:
        native = excel.read_scenarios()
        if "Simulieren?" not in native:
            raise ValueError("Scenarios requires the Simulieren? column")
        definitions = native if scenarios is None else _read_definitions(scenarios)
        _validate_definitions(definitions, native.columns)
        selected = definitions.copy()
        for column, value in (filters or {}).items():
            if column not in selected:
                raise ValueError(f"Unknown scenario_filter column: {column}")
            selected = selected.loc[selected[column].eq(value)]
        if selected.empty:
            raise ValueError("No scenarios match scenario_filter")
        # Runtime fields are not inputs; the saved workbook hash still guards
        # workbook changes. All preset/configuration columns remain fingerprinted.
        controls = [c for c in selected if c in {
            "Simulieren?", "Zeitpunkt", "Skip base reload?",
            "SAVE as Scenario in Inputs?", "Export as single project file incl. Timeseries?",
        } or "status" in c.casefold()]
        identity = {
            "version": 1, "workbook": str(workbook), "sha256": _sha(workbook),
            "schema": SCHEMA_VERSION, "batch_size": batch_size, "base_reload": base_reload,
            "annual": annual, "timeseries": timeseries,
            "definitions": selected.drop(columns=controls).to_json(orient="split", date_format="iso"),
        }
        manifest = {"identity": identity, "chunks": [], "failed": {}}
        if resume and manifest_path.exists():
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            if manifest.get("identity") != identity:
                raise ValueError("Resume inputs/options differ from batch.json; use a new directory")
            for chunk in manifest["chunks"]:
                if chunk["annual"] not in chunk["files"]:
                    raise ValueError("Checkpoint annual file has no recorded hash")
                for name, digest in chunk["files"].items():
                    if Path(name).name != name:
                        raise ValueError("Invalid checkpoint filename")
                    path = directory / name
                    if not path.is_file() or _sha(path) != digest:
                        raise ValueError(f"Missing or changed checkpoint: {name}")
                    result.exported_files.append(path)
                loaded = read_project(directory / chunk["annual"], unknown="raise")
                if loaded.column_names() != chunk["scenarios"]:
                    raise ValueError("Checkpoint scenario identities differ")
                result.completed.extend(chunk["scenarios"])
            if result.completed != selected["Scenario Name"].tolist()[:len(result.completed)]:
                raise ValueError("Completed scenarios are not a prefix of this batch")
            result.skipped = result.completed.copy()
        elif resume and (list(directory.glob("annual-*.xlsx")) or list(directory.glob("sim-*.csv"))):
            raise ValueError("Cannot resume files without batch.json")
        pending = selected.iloc[len(result.completed):]
        if pending.empty:
            return result
        manifest["failed"] = {}
        _atomic_json(manifest_path, manifest)
        excel.configure_scenarios(definitions, replace=scenarios is not None)
        chunk_project = Project()
        files = {}

        def flush():
            nonlocal chunk_project, files
            if not len(chunk_project):
                return
            filename = None
            if annual:
                filename = f"annual-{len(manifest['chunks']) + 1:05d}.xlsx"
                target = directory / filename
                temporary = target.with_name(target.stem + ".tmp.xlsx")
                write_project_excel(chunk_project, temporary, include_out=True)
                _replace(temporary, target)
                files[filename] = _sha(target)
            names = chunk_project.column_names()
            manifest["chunks"].append({"scenarios": names, "annual": filename, "files": files})
            _atomic_json(manifest_path, manifest)
            result.completed.extend(names)
            result.exported_files.extend(directory / name for name in files)
            chunk_project, files = Project(), {}

        last_base = None
        # iloc positions remain the actual SCEN row positions, even after filtering.
        positions = {name: i for i, name in enumerate(definitions["Scenario Name"])}
        try:
            for _, row in pending.iterrows():
                name, base = row["Scenario Name"], row["Base Scenario"]
                one = Project()
                try:
                    excel.run_scenario(positions[name], base_reload == "always" or last_base != base)
                    scenario = excel.capture_scenario(one, name, timeseries=timeseries)
                except Exception as exc:
                    result.failed[name] = f"{type(exc).__name__}: {exc}"
                    result.status = "failed"
                    manifest["failed"] = result.failed
                    break
                if timeseries:
                    filename = f"sim-{positions[name] + 1:05d}.csv"
                    target = directory / filename
                    temporary = target.with_suffix(".tmp.csv")
                    scenario.timeseries.to_frame().to_csv(temporary, index=False)
                    _replace(temporary, target)
                    files[filename] = _sha(target)
                    # Keep memory bounded even for 5,000 hourly simulations.
                    scenario.set_timeseries(pd.DataFrame())
                chunk_project.add_scenario(scenario)
                last_base = base
                if len(chunk_project) >= batch_size:
                    flush()
        except KeyboardInterrupt:
            flush()
            raise
        flush()
        _atomic_json(manifest_path, manifest)
    return result
