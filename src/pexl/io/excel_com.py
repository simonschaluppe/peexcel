"""General Windows COM adapter for a live PEExcel workbook.

No COM dependency is imported until a session is opened. Caller-owned workbooks
are never saved or closed. Owned workbooks close without saving.

Connection ownership and table access are shared infrastructure. Scenario-table
configuration, scenario execution and live-result capture are the first concrete
operations. Batch ordering, checkpoints and exports belong to pexl.batch, not
this adapter. Future PEExcel operations can reuse this session without requiring
SCEN or introducing another Excel connection layer.
"""
from __future__ import annotations

from pathlib import Path
from datetime import datetime
from functools import cached_property
import logging
import sys
from time import sleep
from typing import Callable, TypeVar

from pexl.model.project import Project
from pexl.model.scenario import Scenario

import pandas as pd

from ._project_tables import load_scenario_values


logger = logging.getLogger(__name__)
_T = TypeVar("_T")


class _ScenarioFailure(RuntimeError):
    """VBA explicitly returned failure; no uncertain invocation is repeated."""


class _ExcelFailure(RuntimeError):
    """COM operation failed; execution may be uncertain for non-idempotent calls."""

    def __init__(self, operation: str, hresult: int, *, uncertain: bool):
        super().__init__(f"{operation}: COM HRESULT 0x{hresult:08X}" + (" (execution uncertain)" if uncertain else ""))
        self.hresult = hresult
        self.uncertain = uncertain


class PEExcelAdapter:
    """One PEExcel session; resolve each table only when an operation needs it.

    This internal IO boundary keeps COM objects out of workflow APIs. It can
    capture the current model without configuring or executing a batch.
    """
    def __init__(self, workbook: str | Path, *, reuse_existing: bool = True) -> None:
        """Create a lazy session for a saved workbook.

        ``reuse_existing=True`` preserves attachment to a caller-owned workbook.
        False requires an owned session and rejects an already-open/read-only
        workbook. Neither mode saves the workbook or changes macro security.
        """
        self.path = Path(workbook).resolve()
        self.reuse_existing = reuse_existing
        self.pid: int | None = None
        self.version: str | None = None
        self._process_handle = None
        self._reconnections = 0
        self._uncertain = False
        self.app = self.book = None
        self.own_app = self.own_book = False
        self._restore = None
        self._initialized = False
        self._controls = {"Simulieren?"}

    def _call(self, operation: str, action: Callable[[], _T], *, safe: bool = True) -> _T:
        """Retry only known transient rejection of explicitly idempotent work.

        This bounds retries, not the duration of a synchronous COM call. No
        implicit reconnection occurs during a read: live results must never be
        replaced by values from a reopened workbook.
        """
        for attempt in range(4):
            try:
                return action()
            except BaseException as exc:
                code = getattr(exc, "hresult", None)
                if code is None:
                    if not safe:
                        self._uncertain = True
                    raise
                code &= 0xFFFFFFFF
                if safe and code in {0x80010001, 0x8001010A, 0x800AC472} and attempt < 3:
                    logger.warning("Excel COM rejected %s; retry %d/3", operation, attempt + 1)
                    sleep(0.25 * 2 ** attempt)
                    continue
                self._uncertain |= not safe
                raise _ExcelFailure(operation, code, uncertain=not safe) from exc
        raise AssertionError("unreachable")

    def __enter__(self) -> PEExcelAdapter:
        """Connect on this thread without requiring any model-specific table."""
        try:
            import pythoncom
            import win32com.client as win32
        except ImportError as exc:
            raise RuntimeError("Live PEExcel access requires Windows, Excel and pywin32 (included in peexcel[batch])") from exc
        logger.info("Connecting to Excel...")
        pythoncom.CoInitialize()
        self._initialized = True
        try:
            app = None
            try:
                app = win32.GetActiveObject("Excel.Application")
            except pythoncom.com_error as exc:
                # MK_E_UNAVAILABLE means no running object; other errors must not
                # trigger a second instance while the first is inaccessible.
                if (getattr(exc, "hresult", 0) & 0xFFFFFFFF) != 0x800401E3:
                    raise
            if app is not None:
                self.book = self._call("find open workbook", lambda: next(
                    (b for b in app.Workbooks if Path(b.FullName).resolve() == self.path), None))
            if self.book is not None:
                if not self.reuse_existing:
                    self.book = None
                    raise ValueError("Batch workbook is already open; save and close it before running")
                self.app = app
                logger.info("Reusing open workbook %s; caller-owned Excel will remain open", self.path)
            else:
                self.app = self._call("create Excel instance", lambda: win32.DispatchEx("Excel.Application"), safe=False)
                self.own_app = True
                self._track_process()
                logger.info("Opening workbook %s...", self.path)
                self.book = self._call("open workbook", lambda: self.app.Workbooks.Open(
                    str(self.path), UpdateLinks=0, ReadOnly=False), safe=False)
                self.own_book = True
                if self.book.ReadOnly:
                    raise ValueError("Workbook opened read-only; another Excel instance may own it")
            try:
                self.version = str(self._call("read Excel version", lambda: self.app.Version))
            except Exception as exc:
                logger.warning("Excel version unavailable: %s", exc)
            logger.info("Excel connected (PID %s)", self.pid if self.pid else "unavailable / attached")
            return self
        except BaseException:
            self.__exit__(*sys.exc_info())
            raise

    def _track_process(self) -> None:
        # A process handle guards against PID reuse during reconnection checks.
        try:
            import win32api
            import win32process
            _, self.pid = win32process.GetWindowThreadProcessId(self.app.Hwnd)
            self._process_handle = win32api.OpenProcess(0x00100000, False, self.pid)
        except Exception as exc:
            logger.warning("Cannot track owned Excel process; automatic reconnection disabled: %s", exc)

    def _recover(self, failure: Exception) -> bool:
        """Continue only with proven idle state or a confirmed dead owned process.

        The failed macro is never replayed. The caller must reapply configuration
        and reload the base before a subsequent independent operation.
        """
        if isinstance(failure, _ScenarioFailure) or (
            isinstance(failure, _ExcelFailure) and not failure.uncertain
            and failure.hresult in {0x80010001, 0x8001010A, 0x800AC472}
        ):
            try:
                return self._call("check Excel readiness", lambda: self.app.Ready) is True
            except Exception as exc:
                logger.error("Excel health check failed: %s", exc)
                return False
        if not self.own_app or self._process_handle is None or self._reconnections >= 1:
            return False
        import win32event
        if win32event.WaitForSingleObject(self._process_handle, 0) != win32event.WAIT_OBJECT_0:
            # Even a responding Excel cannot prove that an uncertain macro ended.
            return False
        logger.warning("Owned Excel PID %s exited; reconnecting once...", self.pid)
        self._reconnections += 1
        self.book = self.app = None
        self._restore = None
        self.__exit__(None, None, None)
        self.own_app = self.own_book = False
        self._uncertain = False
        try:
            self.__enter__()
            return True
        except Exception as exc:
            logger.error("Excel reconnection failed: %s", exc)
            return False

    @cached_property
    def scen(self):
        return self._call("resolve SCEN", lambda: self.book.Worksheets("SCEN").ListObjects("Scenarios"))

    @cached_property
    def inputs(self):
        return self._call("resolve IN", lambda: self._table("IN"))

    @cached_property
    def outputs(self):
        return self._call("resolve OUT", lambda: self._table("OUT"))

    def _table(self, name):
        for sheet in self.book.Worksheets:
            for table in sheet.ListObjects:
                if table.Name.casefold() == name.casefold():
                    return table
        raise ValueError(f"Workbook has no structured table {name!r}")

    @staticmethod
    def _frame(table):
        headers = list(table.HeaderRowRange.Value[0])
        if any(not isinstance(h, str) or not h.strip() for h in headers) or len(set(headers)) != len(headers):
            raise ValueError(f"Invalid or duplicate headers in {table.Name}")
        values = table.DataBodyRange.Value if table.DataBodyRange is not None else []
        # Excel dates are wall-clock values. COM's timezone wrapper can break
        # pandas conversion/CSV export; remove it before pandas infers a dtype.
        rows = [tuple(value.replace(tzinfo=None) if isinstance(value, datetime) else value
                      for value in row) for row in values]
        return pd.DataFrame(rows, columns=headers)

    def read_scenarios(self) -> pd.DataFrame:
        """Read the workbook's scenario definitions as an ordinary DataFrame."""
        return self._call("read SCEN", lambda: self._frame(self.scen))

    def _validate_scenarios(self, definitions: pd.DataFrame, *, timeseries: bool = False) -> None:
        """Validate references against live tables, without writing to Excel."""
        def validate():
            headers = {str(h).strip().casefold() for h in self.inputs.HeaderRowRange.Value[0]}
            missing = {v for v in definitions["Base Scenario"] if v.strip().casefold() not in headers}
            if missing:
                raise ValueError(f"Unknown Base Scenario columns in IN: {sorted(missing)}")
            custom_options = None
            for column in definitions:
                values = {str(v).strip() for v in definitions[column] if pd.notna(v) and str(v).strip()}
                if not values:
                    continue
                if column.startswith("Presets_"):
                    # RunScenariosAutomated resolves dropdown_name values to
                    # columns RIGHT of PRESETS>, not the column IDs themselves.
                    frame = self._frame(self._table(column))
                    if "PRESETS>" not in frame or "var_name" not in frame:
                        raise ValueError(f"{column} needs PRESETS> and var_name")
                    dropdown = frame.loc[frame["var_name"].eq("dropdown_name")]
                    if dropdown.empty:
                        raise ValueError(f"{column} has no dropdown_name row")
                    offset = frame.columns.get_loc("PRESETS>") + 1
                    options = {str(v).strip().casefold() for v in dropdown.iloc[0, offset:] if pd.notna(v)}
                    missing = {v for v in values if v.casefold() not in options}
                    if missing:
                        raise ValueError(f"Unknown preset dropdown names in {column}: {sorted(missing)}")
                elif column.startswith("Custom "):
                    if custom_options is None:
                        custom = self._frame(self._table("presets"))
                        if "Preset Name" not in custom:
                            raise ValueError("presets table needs Preset Name")
                        custom_options = {str(v).strip() for v in custom["Preset Name"] if pd.notna(v)}
                    missing = values - custom_options  # VBA uses vbBinaryCompare.
                    if missing:
                        raise ValueError(f"Unknown custom presets in {column}: {sorted(missing)}")
            # Existing strict loader detects incompatible result schemas before
            # an expensive run; validation never starts a macro.
            for table, value in ((self.inputs, "STAGE"), (self.outputs, "Live")):
                load_scenario_values(Scenario("validation"), self._live_frame(table, value), value, unknown="raise")
            if timeseries:
                self._frame(self._table("SIM"))
        self._call("validate workbook", validate)

    def configure_scenarios(self, definitions: pd.DataFrame, *, replace: bool = False) -> None:
        """Save formulas, then optionally load a temporary CSV/XLSX configuration."""
        logger.info("Configuring SCEN (%d rows)...", len(definitions))
        self._call("configure SCEN", lambda: self._configure_scenarios(definitions, replace=replace), safe=False)

    def _configure_scenarios(self, definitions, *, replace):
        if self.scen.ShowTotals:
            raise ValueError("Scenarios must not have a totals row")
        self._controls = set(self.scen.HeaderRowRange.Value[0]) & {
            "Simulieren?", "Skip base reload?", "SAVE as Scenario in Inputs?",
            "Export as single project file incl. Timeseries?",
        }
        if replace and len(definitions) > self.scen.ListRows.Count:
            extra = self.scen.HeaderRowRange.Offset(self.scen.ListRows.Count + 1, 0).Resize(
                len(definitions) - self.scen.ListRows.Count, self.scen.ListColumns.Count)
            if any(value is not None and value != "" for row in extra.Formula for value in row):
                raise ValueError("Cannot expand Scenarios over occupied cells below the table")
        original = self.scen.DataBodyRange
        if self._restore is None:
            self._restore = (self.scen.ListRows.Count,
                             original.Formula if original is not None else None,
                             replace)
        if replace:
            self._resize(len(definitions))
            # Only supplied columns are writable; absent columns retain no stale values.
            self.scen.DataBodyRange.ClearContents()
            for column in definitions.columns:
                values = tuple((None if pd.isna(v) else v,) for v in definitions[column])
                self._call(f"write {column}", lambda: setattr(self.scen.ListColumns(column).DataBodyRange, "Value", values))
        elif not hasattr(self, "_control_formulas"):
            self._control_formulas = {
                name: self.scen.ListColumns(name).DataBodyRange.Formula
                for name in self._controls
            }
        for column in self._controls - {"Simulieren?", "Skip base reload?"}:
            self.scen.ListColumns(column).DataBodyRange.Value = False

    def _resize(self, count):
        self.scen.Resize(self.scen.HeaderRowRange.Resize(count + 1, self.scen.ListColumns.Count))

    def run_scenario(self, row: int, reload_base: bool) -> None:
        """Select one SCEN row and execute the existing VBA scenario operation."""
        def select():
            self.scen.ListColumns("Simulieren?").DataBodyRange.Value = tuple(
                (i == row,) for i in range(self.scen.ListRows.Count))
            if "Skip base reload?" in self._controls:
                self.scen.ListColumns("Skip base reload?").DataBodyRange.Value = not reload_base
        self._call("select scenario", select)
        macro = self._call("resolve macro", lambda: "'" + self.book.Name.replace("'", "''") + "'!RunScenariosAutomated")
        logger.info("Starting VBA simulation (row %d, reload_base=%s)...", row + 1, reload_base)
        try:
            success = self._call("RunScenariosAutomated", lambda: self.app.Run(macro, bool(reload_base)), safe=False)
        except _ExcelFailure as exc:
            info = getattr(exc.__cause__, "excepinfo", None)
            # The existing VBA contract raises this exact error AFTER CleanExit.
            # Other automation errors do not establish whether simulation ended.
            if (exc.hresult == 0x80020009 and info and len(info) == 6
                    and info[1] == "RunScenariosAutomated"
                    and isinstance(info[5], int) and info[5] & 0xFFFFFFFF == 0x800408FB):
                self._uncertain = False
                raise _ScenarioFailure(str(info[2])) from exc
            raise
        if success is not True and success != -1:
            raise _ScenarioFailure("RunScenariosAutomated returned failure")

    def capture_scenario(self, project: Project, name: str, *, timeseries: bool = False) -> Scenario:
        """Capture current live values into Project, independently of SCEN execution."""
        frames = self._call("capture live IN/OUT", lambda: [
            (self._live_frame(self.inputs, "STAGE"), "STAGE"),
            (self._live_frame(self.outputs, "Live"), "Live")])
        scenario = project.get_or_create_scenario(name)
        for frame, column in frames:
            load_scenario_values(scenario, frame, column, unknown="raise")
        if timeseries:
            data = self._call("capture SIM", lambda: self._frame(self._table("SIM")))
            if data.empty:
                raise ValueError("SIM has no time series rows")
            scenario.set_timeseries(data)
        return scenario

    @staticmethod
    def _live_frame(table, value_column):
        # Read two complete columns, not thousands of saved scenario columns.
        headers = table.HeaderRowRange.Value[0]
        if "var_name" not in headers or value_column not in headers or table.DataBodyRange is None:
            raise ValueError(f"Missing or empty var_name/{value_column} result columns")
        data = {}
        for name in ("var_name", value_column):
            values = table.ListColumns(name).DataBodyRange.Value
            cells = [row[0] for row in values] if isinstance(values, tuple) else [values]
            data[name] = [value.replace(tzinfo=None) if isinstance(value, datetime) else value
                          for value in cells]
        frame = pd.DataFrame(data)
        if frame.empty:
            raise ValueError(f"Empty {value_column} result column")
        return frame

    def __exit__(self, exc_type, exc, tb) -> None:
        """Restore configuration and close only owned resources, preserving errors."""
        errors = []
        logger.info("Cleaning up Excel...")

        def attempt(label, action):
            try:
                self._call(label, action)
            except BaseException as error:
                errors.append(error)
                logger.error("%s failed (owned PID %s): %s", label, self.pid, error)

        def restore():
            if self._restore is not None:
                count, formulas, replaced = self._restore
                if replaced:
                    self.scen.DataBodyRange.ClearContents()
                    self._resize(count)
                    if formulas is not None:
                        self.scen.DataBodyRange.Formula = formulas
                elif hasattr(self, "_control_formulas"):
                    for name, values in self._control_formulas.items():
                        self.scen.ListColumns(name).DataBodyRange.Formula = values

        # An uncertain macro may still be running: never mutate its state or
        # call Close/Quit and risk another synchronous block. Report the PID.
        if self._uncertain and self.app is not None:
            logger.warning("Excel execution state uncertain; inspect PID %s manually; workbook not restored/closed", self.pid)
        else:
            attempt("restore SCEN", restore)
            if self.own_book and self.book is not None:
                attempt("close owned workbook", lambda: self.book.Close(SaveChanges=False))
            if self.own_app and self.app is not None:
                attempt("quit owned Excel", self.app.Quit)
        for name in ("scen", "inputs", "outputs", "_control_formulas"):
            self.__dict__.pop(name, None)
        self._restore = None
        self.book = self.app = None
        if self._process_handle is not None:
            attempt("release process handle", self._process_handle.Close)
            self._process_handle = None
        if self._initialized:
            import pythoncom
            attempt("uninitialize COM", pythoncom.CoUninitialize)
            self._initialized = False
        if errors:
            if exc_type is None:
                raise errors[0]
        elif not self._uncertain:
            logger.info("Excel cleanup completed")
