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
from functools import cached_property

import pandas as pd

from ._project_tables import load_scenario_values


class PEExcelAdapter:
    """One PEExcel session; resolve each table only when an operation needs it.

    This internal IO boundary keeps COM objects out of workflow APIs. It can
    capture the current model without configuring or executing a batch.
    """
    def __init__(self, workbook):
        self.path = Path(workbook).resolve()
        self.app = self.book = None
        self.own_app = self.own_book = False
        self._restore = None
        self._initialized = False
        self._controls = {"Simulieren?"}

    def __enter__(self):
        try:
            import pythoncom
            import win32com.client as win32
        except ImportError as exc:
            raise RuntimeError("Live PEExcel access requires Windows, Excel and pywin32 (included in peexcel[batch])") from exc

        pythoncom.CoInitialize()
        self._initialized = True
        try:
            try:
                app = win32.GetActiveObject("Excel.Application")
                self.book = next((b for b in app.Workbooks
                                  if Path(b.FullName).resolve() == self.path), None)
            except pythoncom.com_error:
                self.book = None
            if self.book is not None:
                self.app = app
            else:
                self.app = win32.DispatchEx("Excel.Application")
                self.own_app = True
                self.book = self.app.Workbooks.Open(str(self.path), UpdateLinks=0, ReadOnly=False)
                self.own_book = True
            return self
        except BaseException:
            self.__exit__(None, None, None)
            raise

    @cached_property
    def scen(self):
        return self.book.Worksheets("SCEN").ListObjects("Scenarios")

    @cached_property
    def inputs(self):
        return self._table("IN")

    @cached_property
    def outputs(self):
        return self._table("OUT")

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
        return pd.DataFrame(list(values), columns=headers)

    def read_scenarios(self):
        """Read the workbook's scenario definitions as an ordinary DataFrame."""
        return self._frame(self.scen)

    def configure_scenarios(self, definitions, *, replace=False):
        """Save formulas, then optionally load a temporary CSV/XLSX configuration."""
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
        self._restore = (self.scen.ListRows.Count,
                         original.Formula if original is not None else None,
                         replace)
        if replace:
            self._resize(len(definitions))
            # Only supplied columns are writable; absent columns retain no stale values.
            self.scen.DataBodyRange.ClearContents()
            for column in definitions.columns:
                values = tuple((None if pd.isna(v) else v,) for v in definitions[column])
                self.scen.ListColumns(column).DataBodyRange.Value = values
        else:
            self._control_formulas = {
                name: self.scen.ListColumns(name).DataBodyRange.Formula
                for name in self._controls
            }
        for column in self._controls - {"Simulieren?", "Skip base reload?"}:
            self.scen.ListColumns(column).DataBodyRange.Value = False

    def _resize(self, count):
        self.scen.Resize(self.scen.HeaderRowRange.Resize(count + 1, self.scen.ListColumns.Count))

    def run_scenario(self, row, reload_base):
        """Select one SCEN row and execute the existing VBA scenario operation."""
        # One bulk write, including false for every unselected row.
        self.scen.ListColumns("Simulieren?").DataBodyRange.Value = tuple(
            (i == row,) for i in range(self.scen.ListRows.Count))
        if "Skip base reload?" in self._controls:
            self.scen.ListColumns("Skip base reload?").DataBodyRange.Value = not reload_base
        macro = "'" + self.book.Name.replace("'", "''") + "'!RunScenariosAutomated"
        success = self.app.Run(macro, bool(reload_base))
        if success is not True and success != -1:
            raise RuntimeError("RunScenariosAutomated returned failure")

    def capture_scenario(self, project, name, *, timeseries=False):
        """Capture current live values into Project, independently of SCEN execution."""
        frames = [(self._live_frame(self.inputs, "STAGE"), "STAGE"),
                  (self._live_frame(self.outputs, "Live"), "Live")]
        scenario = project.get_or_create_scenario(name)
        for frame, column in frames:
            load_scenario_values(scenario, frame, column, unknown="raise")
        if timeseries:
            data = self._frame(self._table("SIM"))
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
            data[name] = [row[0] for row in values] if isinstance(values, tuple) else [values]
        frame = pd.DataFrame(data)
        if frame.empty:
            raise ValueError(f"Empty {value_column} result column")
        return frame

    def __exit__(self, exc_type, exc, tb):
        try:
            if self._restore is not None:
                count, formulas, replaced = self._restore
                if replaced:
                    # Clear temporary rows before shrinking, so no data is left below SCEN.
                    self.scen.DataBodyRange.ClearContents()
                    self._resize(count)
                    if formulas is not None:
                        self.scen.DataBodyRange.Formula = formulas
                elif hasattr(self, "_control_formulas"):
                    for name, values in self._control_formulas.items():
                        self.scen.ListColumns(name).DataBodyRange.Formula = values
        finally:
            try:
                if self.own_book and self.book is not None:
                    self.book.Close(SaveChanges=False)
            finally:
                try:
                    if self.own_app and self.app is not None:
                        self.app.Quit()
                finally:
                    for name in ("scen", "inputs", "outputs", "_control_formulas"):
                        self.__dict__.pop(name, None)
                    self._restore = None
                    self.book = self.app = None
                    if self._initialized:
                        import pythoncom
                        pythoncom.CoUninitialize()
                        self._initialized = False
