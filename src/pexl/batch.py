"""Python orchestration of PEExcel's single-scenario VBA contract.

Annual chunks are ordinary Project Excel exports. Only a small resume manifest
is batch-specific; no Excel automation objects escape this module.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from collections.abc import Callable
from contextlib import contextmanager
from contextvars import ContextVar
from copy import copy, deepcopy
import logging
import math
import re
import sys
from importlib.metadata import PackageNotFoundError, version
from datetime import date, datetime
import hashlib
import json
from pathlib import Path
from time import sleep, monotonic
from typing import Mapping

import pandas as pd

from pexl.io.excel import read_project, write_project_excel
from pexl.io._project_tables import RESERVED_IN_COLUMN_HEADER_SET, RESERVED_OUT_COLUMN_HEADER_SET
from pexl.io.excel_com import PEExcelAdapter, _ScenarioFailure, _ExcelFailure
from pexl.model.project import Project
from pexl.schema.current import SCHEMA_VERSION, SCHEMA_META


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
        return pd.read_csv(path, sep=None, engine="python", dtype=str, keep_default_na=False, encoding="utf-8-sig")
    with pd.ExcelFile(path) as book:
        sheet = next((s for s in ("Scenarios", "SCEN") if s in book.sheet_names), None)
        if sheet is None and len(book.sheet_names) != 1:
            raise ValueError("Scenario workbook needs a Scenarios or SCEN sheet, or exactly one sheet")
        return pd.read_excel(book, sheet_name=sheet or book.sheet_names[0], dtype=object, keep_default_na=False)


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
    if names.map(lambda x: not isinstance(x, str) or not x.strip()).any() or names.str.strip().duplicated().any():
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
    overwrite: bool = False,
    progress_callback: Callable[[int, int, str], None] | None = None,
) -> BatchResult:
    """Run selected PEExcel scenarios sequentially and capture their results.

    Each scenario is selected alone, passed to ``RunScenariosAutomated`` and
    captured before the next scenario runs. Annual results use the existing
    Project Excel format. Optional SIM time series are written as CSV files.

    Parameters
    ----------
    workbook : str or Path
        PEExcel workbook to use. Requires Windows, Excel and the
        ``peexcel[batch]`` extra.
    scenarios : str, Path, DataFrame or None, default None
        Optional scenario definitions from a CSV, Excel file or DataFrame.
        Each definition temporarily replaces only the first existing SCEN row;
        the table size stays fixed and original contents are restored when the
        session ends. Required columns are ``Scenario Name``
        and ``Base Scenario``; other columns must match SCEN headers. If None,
        use the existing SCEN table.
    scenario_filter : Mapping[str, object] or None, default None
        Select rows whose values exactly match every supplied column/value pair.
        Scenario order is preserved. With no filter, run all definitions.
    batch_size : int, default 25
        Maximum scenarios per annual Project export file; this does not control
        how many scenarios are selected or run in Excel at once.
    base_reload : {"always", "first_only"}, default "always"
        Controls the ``reloadBase`` Boolean passed to VBA.

        ``"always"`` reloads the base before every scenario, preventing inputs
        from carrying over between runs.

        ``"first_only"`` reloads before the first pending scenario and whenever
        ``Base Scenario`` changes. After resuming, the first pending scenario
        also reloads its base. Use this only when presets fully define independent
        scenarios; omitted inputs may otherwise carry over from the previous run.

        Any other value raises ``ValueError``.
    export_annual : bool, default True
        Write annual IN and OUT results as Project Excel files.
    export_timeseries : bool, default False
        Capture the SIM table and write one CSV per scenario.
    output_dir : str or Path, default "results/batch"
        Directory for result files, ``batch.json``, ``batch.log``, the portable
        ``remaining_scenarios.csv`` and the exclusive run lock.
    resume : bool, default False
        Resume from verified annual chunks in ``batch.json``. Workbook contents,
        selected definitions, schema, options and recorded file hashes must match.
        Resume requires ``export_annual=True``.
    overwrite : bool, default False
        Start fresh by deleting generated batch outputs in output_dir, including
        checkpoints, logs and retry CSV. Other files and subdirectories are kept.
        Cannot be combined with resume=True; an existing run lock is respected.
    progress_callback : callable or None, default None
        Optional ``callback(completed, total, scenario_name)`` called initially
        with the verified resumed count and an empty scenario name, then after
        each successfully captured scenario. Counts include resumed scenarios.
        Updates occur between synchronous Excel calls. Intermediate counts may
        include an unsaved chunk; the final successful update follows export.
        Callback exceptions propagate after captured results are saved.

    Returns
    -------
    BatchResult
        ``completed`` lists newly completed and resumed scenarios;
        ``skipped`` lists scenarios loaded from earlier verified chunks;
        ``failed`` maps unsuccessful scenarios to their errors;
        ``exported_files`` lists result files; and ``status`` is ``"completed"``
        or ``"failed"``.

    Raises
    ------
    ValueError
        If options, scenario definitions, filters or resume state are invalid.
    FileExistsError
        If the output directory already contains batch results without resume,
        or another run holds its lock.
    KeyboardInterrupt
        Propagated after any fully captured scenarios are saved when possible.
    Exception
        Setup, structural capture and export errors propagate after finalization.
        Explicit VBA failures are skipped if Excel remains healthy. Unrecoverable
        COM failures stop the run and are reported in ``BatchResult.failed``.

    Notes
    -----
    Progress is logged automatically, independently of the callback. A matching
    open workbook is reused and left open. Otherwise an owned session is created.
    Save input changes before running: the checkpoint fingerprints the disk file,
    not unsaved Excel edits.
    The workbook is not saved. Excel runs synchronously, and the workbook,
    definitions and output directory must not be edited concurrently. A hard
    process interruption may leave a stale ``.batch.lock``; remove it only after
    confirming Excel is no longer running the batch. After a hard crash, reconcile
    the retry CSV with ``inspect_batch(workbook, output_dir=...)`` before using it
    as standalone input; JSON and CSV cannot be replaced atomically together.
    """
    if isinstance(batch_size, bool) or not isinstance(batch_size, int) or not 1 <= batch_size <= 1000:
        raise ValueError("batch_size must be an integer from 1 to 1000")
    if base_reload not in {"always", "first_only"}:
        raise ValueError("base_reload must be 'always' or 'first_only'")
    if not export_annual and not export_timeseries:
        raise ValueError("Enable at least one result export")
    if overwrite and resume:
        raise ValueError("overwrite=True cannot be combined with resume=True")
    if resume and not export_annual:
        raise ValueError("resume requires annual Project exports")
    if progress_callback is not None and not callable(progress_callback):
        raise TypeError("progress_callback must be callable or None")
    workbook = Path(workbook).resolve(strict=True)
    output_dir = Path(output_dir).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)
    with _batch_lock(output_dir):
        if overwrite:
            # Preserve input when a retry CSV inside this directory is the source.
            if isinstance(scenarios, (str, Path)):
                scenarios = _read_definitions(scenarios)
            targets = [p for p in output_dir.iterdir() if p.name in {
                "batch.json", "batch.tmp", "batch.log", "remaining_scenarios.csv",
                "remaining_scenarios.tmp.csv",
            } or re.fullmatch(r"(?:annual-\d{5,}(?:\.tmp)?\.xlsx|sim-\d{5,}(?:\.tmp)?\.csv)", p.name)]
            for target in targets:
                if target.resolve().parent != output_dir or target.resolve() == workbook or not target.is_file():
                    raise ValueError(f"Refusing to overwrite unexpected batch output: {target}")
            for target in targets:
                target.unlink()
        with _batch_logging(output_dir):
            if overwrite:
                logger.info("Overwrite enabled: starting a fresh batch")
            return _run(workbook, scenarios, scenario_filter, batch_size, base_reload,
                        export_annual, export_timeseries, output_dir, resume, progress_callback)


logger = logging.getLogger(__name__)
_scenario_logging = ContextVar("pexl_scenario_logging", default=False)


class _BatchFormatter(logging.Formatter):
    def __init__(self, *, color=False):
        super().__init__("%(asctime)s %(levelname)-7s %(message)s", "%Y-%m-%d %H:%M:%S")
        self.color = color

    def format(self, record):
        record = copy(record)
        if _scenario_logging.get():
            record.msg = "    " + record.getMessage().replace("\n", "\n    ")
            record.args = ()
        text = super().format(record)
        if self.color:
            color = "32" if record.name == "pexl.io.excel_com" else "35"
            return f"\033[{color}m{text}\033[0m"
        return text


@contextmanager
def _batch_lock(directory):
    lock = directory / ".batch.lock"
    with lock.open("x", encoding="utf-8") as stream:
        stream.write("Batch in progress; after a hard crash remove only after Excel has stopped.\n")
    try:
        yield
    finally:
        active_error = sys.exc_info()[0] is not None
        try:
            lock.unlink()
        except OSError:
            if not active_error:
                raise
            logger.exception("Could not release batch lock")


@contextmanager
def _batch_logging(directory):
    # Scope changes to these two loggers; never configure the root logger.
    targets = [logger, logging.getLogger("pexl.io.excel_com")]
    previous = [(log.level, log.propagate) for log in targets]
    handlers = []
    try:
        handlers.append(logging.StreamHandler(sys.stderr))
        handlers.append(logging.FileHandler(directory / "batch.log", mode="a", encoding="utf-8"))
        handlers[0].setFormatter(_BatchFormatter(color=getattr(sys.stderr, "isatty", lambda: False)()))
        handlers[1].setFormatter(_BatchFormatter())
        for log in targets:
            log.setLevel(logging.INFO)
            log.propagate = False
            for handler in handlers:
                log.addHandler(handler)
        yield
    finally:
        for log, (level, propagate) in zip(targets, previous):
            for handler in handlers:
                log.removeHandler(handler)
            log.setLevel(level)
            log.propagate = propagate
        for handler in handlers:
            handler.close()


def _select(definitions, available, filters):
    _validate_definitions(definitions, available)
    selected = definitions.copy(deep=True)
    for column, value in (filters or {}).items():
        if column not in selected:
            raise ValueError(f"Unknown scenario_filter column: {column}")
        selected = selected.loc[selected[column].eq(value)]
    if selected.empty:
        raise ValueError("No scenarios match scenario_filter")
    return selected


def _definition_identity(selected):
    controls = [c for c in selected if c in {
        "Simulieren?", "Zeitpunkt", "Skip base reload?",
        "SAVE as Scenario in Inputs?", "Export as single project file incl. Timeseries?",
    } or "status" in c.casefold()]
    return selected.drop(columns=controls).to_json(orient="split", date_format="iso")


def _snapshot(selected):
    snapshot = selected.astype(object).where(pd.notna(selected), None).to_dict(orient="split")
    snapshot["data"] = [[value.isoformat() if isinstance(value, (date, datetime)) else value
                         for value in row] for row in snapshot["data"]]
    return snapshot


def _from_snapshot(snapshot):
    # No pandas inference: literal identifiers such as '001' must remain strings.
    return pd.DataFrame(snapshot["data"], columns=snapshot["columns"], index=snapshot["index"])


def _remaining(selected, completed):
    return selected.loc[~selected["Scenario Name"].isin(completed)].copy()


def _write_remaining(directory, selected, completed):
    remaining = _remaining(selected, completed)
    target = directory / "remaining_scenarios.csv"
    temporary = target.with_suffix(".tmp.csv")
    logger.info("Saving remaining_scenarios.csv (%d scenarios)...", len(remaining))
    remaining.to_csv(temporary, index=False, encoding="utf-8-sig")
    _replace(temporary, target)
    logger.info("Saved remaining_scenarios.csv (%d scenarios)", len(remaining))
    return remaining


def _verify_manifest(manifest, directory, selected):
    if manifest.get("version", 1) not in (1, 2):
        raise ValueError("Unsupported batch.json version")
    result = BatchResult()
    for chunk in manifest["chunks"]:
        if chunk["annual"] is not None and chunk["annual"] not in chunk["files"]:
            raise ValueError("Checkpoint annual file has no recorded hash")
        if not chunk["files"]:
            raise ValueError("Checkpoint has no result files")
        for name, digest in chunk["files"].items():
            if Path(name).name != name or name in {".", ".."}:
                raise ValueError("Invalid checkpoint filename")
            path = directory / name
            if not path.is_file() or _sha(path) != digest:
                raise ValueError(f"Missing or changed checkpoint: {name}")
            result.exported_files.append(path)
        if chunk["annual"] is not None:
            loaded = read_project(directory / chunk["annual"], unknown="raise")
            if loaded.column_names() != chunk["scenarios"]:
                raise ValueError("Checkpoint scenario identities differ")
        result.completed.extend(chunk["scenarios"])
    names = selected["Scenario Name"].tolist()
    if len(set(result.completed)) != len(result.completed) or not set(result.completed).issubset(names):
        raise ValueError("Checkpoint has duplicate or unknown completed scenarios")
    if not set(manifest.get("failed", {})).issubset(names):
        raise ValueError("Checkpoint has unknown failed scenarios")
    result.skipped = result.completed.copy()
    result.failed = {n: e for n, e in manifest.get("failed", {}).items() if n not in result.completed}
    return result


def inspect_batch(
    workbook: str | Path,
    *,
    scenarios: str | Path | pd.DataFrame | None = None,
    scenario_filter: Mapping[str, object] | None = None,
    output_dir: str | Path | None = None,
) -> pd.DataFrame:
    """Validate SCEN definitions or reconcile a stopped batch without simulation.

    Parameters
    ----------
    workbook : str or Path
        PEExcel workbook. Fresh inspection reuses a matching open workbook.
    scenarios : str, Path, DataFrame or None
        Definitions in the same format as ``run_batch``. With a v2 checkpoint,
        None uses its original snapshot, so a lost source CSV is not required.
    scenario_filter : Mapping or None
        Exact column/value selection, as in ``run_batch``.
    output_dir : str, Path or None
        Existing stopped batch directory. Verify inputs and exports under its
        exclusive lock, refresh ``remaining_scenarios.csv`` and return remaining
        rows. This mode does not open Excel. A stale lock must first be checked
        and removed manually after confirming the old simulation has stopped.

    Returns
    -------
    pandas.DataFrame
        Selected (or remaining) original SCEN rows, without added status columns.

    Raises
    ------
    ValueError
        Definitions, workbook identity or checkpoint verification are invalid.
    FileExistsError
        The batch directory is locked.
    """
    workbook = Path(workbook).resolve(strict=True)
    if output_dir is None:
        with PEExcelAdapter(workbook, reuse_existing=True) as excel:
            native = excel.read_scenarios()
            definitions = native if scenarios is None else _read_definitions(scenarios)
            selected = _select(definitions, native.columns, scenario_filter)
            excel._validate_scenarios(selected)
            return selected
    directory = Path(output_dir).resolve(strict=True)
    with _batch_lock(directory), _batch_logging(directory):
        manifest = json.loads((directory / "batch.json").read_text(encoding="utf-8"))
        identity = manifest["identity"]
        if identity["sha256"] != _sha(workbook) or identity["schema"] != SCHEMA_VERSION:
            raise ValueError("Workbook/schema differ from batch.json")
        if scenarios is None:
            if "selected" not in manifest:
                raise ValueError("Legacy checkpoint inspection requires the original scenarios input")
            definitions = _from_snapshot(manifest["selected"])
        else:
            definitions = _read_definitions(scenarios)
        selected = _select(definitions, definitions.columns, scenario_filter)
        if _definition_identity(selected) != identity["definitions"]:
            raise ValueError("Scenario definitions differ from batch.json")
        result = _verify_manifest(manifest, directory, selected)
        if "selected" in manifest:
            selected = _from_snapshot(manifest["selected"])
        return _write_remaining(directory, selected, result.completed)


def _plausibility(scenario):
    value = scenario.to_var_dict().get("PEI_saldo_project")
    try:
        valid = not isinstance(value, bool) and value is not None and math.isfinite(float(value))
    except (TypeError, ValueError):
        valid = False
    if valid:
        logger.info("Results plausible: PEI_saldo_project=%.2f %s", float(value), SCHEMA_META.PEI_saldo_project.unit)
    else:
        logger.warning("%s: missing, nonnumeric or nonfinite PEI_saldo_project: %r", scenario.column_name, value)


def _run(workbook, scenarios, filters, batch_size, base_reload, annual, timeseries, directory, resume,
         progress_callback=None):
    result = BatchResult()
    manifest_path = directory / "batch.json"
    if not resume and (manifest_path.exists() or list(directory.glob("annual-*.xlsx"))
                       or list(directory.glob("sim-*.csv"))):
        raise FileExistsError("Batch outputs already exist; use resume=True, overwrite=True or a new output directory")
    if resume and not manifest_path.exists() and (list(directory.glob("annual-*.xlsx")) or list(directory.glob("sim-*.csv"))):
        raise ValueError("Cannot resume files without batch.json")
    started = monotonic()
    selected = None
    manifest = None
    chunk_project = Project()
    files = {}
    durations = []
    positions = {}
    scenario_seconds = {}
    phase = "setup"
    current = None
    excel = PEExcelAdapter(workbook, reuse_existing=True)

    def checkpoint():
        nonlocal manifest
        candidate = deepcopy(manifest)
        candidate["failed"] = result.failed.copy()
        logger.info("Saving checkpoint...")
        _atomic_json(manifest_path, candidate)
        manifest = candidate
        logger.info("Checkpoint saved")

    def export_series():
        if not timeseries:
            return
        for scenario in chunk_project:
            filename = f"sim-{positions[scenario.column_name] + 1:05d}.csv"
            if filename in files:
                continue
            target = directory / filename
            temporary = target.with_suffix(".tmp.csv")
            logger.info("Exporting %s...", filename)
            scenario.timeseries.to_frame().to_csv(temporary, index=False)
            _replace(temporary, target)
            files[filename] = _sha(target)
            scenario.set_timeseries(pd.DataFrame())

    def flush():
        nonlocal chunk_project, files, manifest
        if not len(chunk_project):
            return
        logger.info("Flushing %d captured scenarios...", len(chunk_project))
        export_series()
        chunk_files = files.copy()
        filename = None
        if annual:
            filename = f"annual-{len(manifest['chunks']) + 1:05d}.xlsx"
            target = directory / filename
            temporary = target.with_name(target.stem + ".tmp.xlsx")
            logger.info("Exporting %s...", filename)
            write_project_excel(chunk_project, temporary, include_out=True)
            _replace(temporary, target)
            chunk_files[filename] = _sha(target)
        names = chunk_project.column_names()
        candidate = deepcopy(manifest)
        candidate["chunks"].append({"scenarios": names, "annual": filename, "files": chunk_files,
                                    "seconds": {n: scenario_seconds[n] for n in names}})
        candidate["failed"] = {n: e for n, e in result.failed.items() if n not in names}
        logger.info("Saving checkpoint...")
        _atomic_json(manifest_path, candidate)
        # Commit memory only AFTER the durable checkpoint; a failed flush is retryable.
        manifest = candidate
        result.failed = candidate["failed"].copy()
        result.completed.extend(names)
        result.exported_files.extend(directory / name for name in chunk_files)
        chunk_project, files = Project(), {}
        logger.info("Checkpoint saved (%d committed)", len(result.completed))
        _write_remaining(directory, selected, result.completed)

    try:
        if resume and manifest_path.exists():
            saved = json.loads(manifest_path.read_text(encoding="utf-8"))
            if "selected" in saved:
                selected = _from_snapshot(saved["selected"])
                expected = {"version": 1, "workbook": str(workbook), "sha256": _sha(workbook),
                            "schema": SCHEMA_VERSION, "batch_size": batch_size, "base_reload": base_reload,
                            "annual": annual, "timeseries": timeseries,
                            "definitions": _definition_identity(selected)}
                if saved.get("identity") != expected:
                    raise ValueError("Resume inputs/options differ from batch.json; use a new directory")
                if scenarios is not None:
                    supplied = _select(_read_definitions(scenarios), selected.columns, filters)
                    if _definition_identity(supplied) != expected["definitions"]:
                        raise ValueError("Resume scenario definitions differ from batch.json")
                result = _verify_manifest(saved, directory, selected)
                _write_remaining(directory, selected, result.completed)
        elif scenarios is not None:
            supplied = _read_definitions(scenarios)
            selected = _select(supplied, supplied.columns, filters)
            _write_remaining(directory, selected, [])
        excel.__enter__()
        logger.info("Reading scenario definitions...")
        native = excel.read_scenarios()
        if "Simulieren?" not in native:
            raise ValueError("Scenarios requires the Simulieren? column")
        definitions = native if scenarios is None else _read_definitions(scenarios)
        selected = _select(definitions, native.columns, filters)
        identity = {
            "version": 1, "workbook": str(workbook), "sha256": _sha(workbook),
            "schema": SCHEMA_VERSION, "batch_size": batch_size, "base_reload": base_reload,
            "annual": annual, "timeseries": timeseries,
            "definitions": _definition_identity(selected),
        }
        if resume and manifest_path.exists():
            saved = json.loads(manifest_path.read_text(encoding="utf-8"))
            if saved.get("identity") != identity:
                raise ValueError("Resume inputs/options differ from batch.json; use a new directory")
            result = _verify_manifest(saved, directory, selected)
            manifest = saved
            if "selected" in saved:
                selected = _from_snapshot(saved["selected"])
        else:
            manifest = {"identity": identity, "chunks": [], "failed": {}}
        manifest["version"] = 2
        manifest.setdefault("selected", _snapshot(selected))
        try:
            package_version = version("peexcel")
        except PackageNotFoundError:
            package_version = "source checkout"
        manifest.setdefault("runtime", {"python": sys.version.split()[0], "peexcel": package_version,
                                        "excel": getattr(excel, "version", None)})
        checkpoint()
        _write_remaining(directory, selected, result.completed)
        pending = _remaining(selected, result.completed)
        logger.info("Batch: %d scenarios, %d completed (resume)", len(selected), len(result.completed))
        if progress_callback is not None:
            progress_callback(len(result.completed), len(selected), "")
        configuration = definitions
        replace = scenarios is not None
        if not pending.empty:
            logger.info("Validating workbook references and result schema...")
            excel._validate_scenarios(selected, timeseries=timeseries)
            if not replace:
                logger.info("Configuring scenarios...")
                excel.configure_scenarios(configuration, replace=False)
        positions = {name: i for i, name in enumerate(configuration["Scenario Name"])}
        indices = {name: i + 1 for i, name in enumerate(selected["Scenario Name"])}
        last_base = None
        for name, base in zip(pending["Scenario Name"], pending["Base Scenario"]):
            current = name
            scenario_started = monotonic()
            logger.info("RUN [%03d/%d] %s (batch elapsed %.1fs)", indices[name], len(selected), name, monotonic() - started)
            log_token = _scenario_logging.set(True)
            try:
                phase = "simulation"
                try:
                    if replace:
                        phase = "configuration"
                        excel.configure_scenarios(configuration.iloc[[positions[name]]], replace=True)
                    phase = "simulation"
                    excel.run_scenario(0 if replace else positions[name], base_reload == "always" or last_base != base)
                    phase = "capture"
                    capture_started = monotonic()
                    scenario = excel.capture_scenario(Project(), name, timeseries=timeseries)
                    logger.info("Results captured (%.1fs)", monotonic() - capture_started)
                except (_ScenarioFailure, _ExcelFailure) as exc:
                    result.failed[name] = f"{phase}: {type(exc).__name__}: {exc}"
                    logger.error("%s: %s", name, result.failed[name])
                    checkpoint()
                    _write_remaining(directory, selected, result.completed)
                    last_base = None
                    if not excel._recover(exc):
                        logger.error("Excel connection/state could not be recovered; stopping")
                        break
                    if not replace:
                        logger.info("Configuring scenarios after recovery...")
                        excel.configure_scenarios(configuration, replace=False)
                    continue
                scenario_seconds[name] = monotonic() - scenario_started
                _plausibility(scenario)
                phase = "export"
                chunk_project.add_scenario(scenario)
                export_series()
                last_base = base
                durations.append(scenario_seconds[name])
                completed_count = len(result.completed) + len(chunk_project)
                if len(chunk_project) >= batch_size or name == pending.iloc[-1]["Scenario Name"]:
                    flush()
                logger.debug("Captured (%.1fs); %d captured, %d committed", durations[-1], completed_count, len(result.completed))
                phase = "callback"
                if progress_callback is not None:
                    progress_callback(completed_count, len(selected), name)
                current = None
            finally:
                _scenario_logging.reset(log_token)
        phase = "export"
        flush()
    except BaseException as exc:
        if manifest is not None and current is not None and current not in result.completed:
            result.failed[current] = f"{phase}: {type(exc).__name__}: {exc}"
        logger.error("Batch stopped during %s: %s: %s", phase, type(exc).__name__, exc)
        raise
    finally:
        original_error = sys.exc_info()
        cleanup_errors = []
        # Each step is independent: a flush failure must not suppress retry CSV or cleanup.
        if manifest is not None:
            for label, action in [("flush", flush), ("checkpoint", checkpoint),
                                  ("retry CSV", lambda: _write_remaining(directory, selected, result.completed))]:
                try:
                    action()
                except BaseException as exc:
                    cleanup_errors.append(exc)
                    logger.error("Final %s failed: %s", label, exc)
        try:
            excel.__exit__(*original_error)
        except BaseException as exc:
            cleanup_errors.append(exc)
            logger.error("Excel cleanup failed: %s", exc)
        count = len(selected) if selected is not None else 0
        outstanding = count - len(result.completed)
        logger.info("Summary: %d completed, %d failed, %d pending; %.1fs elapsed; mean successful scenario %.1fs",
                    len(result.completed), len(result.failed), max(0, outstanding - len(result.failed)),
                    monotonic() - started, sum(durations) / len(durations) if durations else 0)
        logger.info("Exported files: %s", ", ".join(str(p) for p in result.exported_files) or "none")
        logger.info("Log: %s", directory / "batch.log")
        if manifest is not None and outstanding:
            logger.warning("Incomplete batch: %d scenarios require retry; reconcile batch.json before using CSV after a hard crash", outstanding)
        if cleanup_errors and original_error[0] is None:
            raise cleanup_errors[0]
    result.status = "failed" if result.failed or len(result.completed) != len(selected) else "completed"
    return result
