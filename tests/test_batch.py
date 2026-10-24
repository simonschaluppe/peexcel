"""Batch orchestration uses real Project serialization with a deterministic Excel boundary."""
import json
from types import SimpleNamespace

import pandas as pd
import pytest

from pexl import Project
from pexl import batch
from pexl.io.excel import read_project
from pexl.io.excel_com import PEExcelAdapter
from pexl.io._project_tables import load_scenario_values


class FakeExcel:
    calls = []
    failure = None
    captured = []
    configurations = []
    closed = False
    rows = pd.DataFrame({
        'Scenario Name': ['Demo | A', 'Demo | B', 'Demo | C', 'Demo | D'],
        'Base Scenario': ['Default', 'Default', 'Other', 'Other'],
        'Simulieren?': [False] * 4,
        'Preset': ['one', 'two', 'three', 'four'],
    })

    def __init__(self, path):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        type(self).closed = True

    def read_scenarios(self):
        return self.rows.copy()

    def configure_scenarios(self, frame, *, replace):
        self.configurations.append((frame.copy(), replace))
        self.active = frame

    def run_scenario(self, row, reload):
        self.calls.append((row, reload))
        if self.failure == row:
            raise RuntimeError('VBA returned False')
        self.last = row

    def capture_scenario(self, project, name, *, timeseries):
        self.captured.append(name)
        scenario = project.get_or_create_scenario(name)
        load_scenario_values(scenario, pd.DataFrame({
            'var_name': ['project_name', 'project_scenario_name', 'QH'],
            'Live': ['Demo', name.split(' | ')[-1], 10 + self.last],
        }), 'Live', unknown='raise')
        if timeseries:
            scenario.set_timeseries(pd.DataFrame({'Ta': [1., 2.], 'E_grid': [3., 4.]}))
        return scenario


@pytest.fixture
def setup(monkeypatch, tmp_path):
    for key, value in dict(calls=[], failure=None, captured=[], configurations=[], closed=False).items():
        monkeypatch.setattr(FakeExcel, key, value)
    monkeypatch.setattr(batch, 'PEExcelAdapter', FakeExcel)
    workbook = tmp_path / 'model.xlsb'
    workbook.write_bytes(b'workbook contract fixture')
    return {'workbook': workbook, 'output_dir': tmp_path / 'results', 'batch_size': 2}


def test_chunked_results_roundtrip_and_resume_without_rerunning(setup):
    result = batch.run_batch(**setup, base_reload='first_only', export_timeseries=True)
    assert result.status == 'completed' and result.completed == FakeExcel.rows['Scenario Name'].tolist()
    assert FakeExcel.calls == [(0, True), (1, False), (2, True), (3, False)]
    annual = [p for p in result.exported_files if p.suffix == '.xlsx']
    assert len(annual) == 2 and len(result.exported_files) == 6
    assert [s.to_var_dict()['QH'] for p in annual for s in read_project(p)] == [10, 11, 12, 13]
    assert pd.read_csv(next(p for p in result.exported_files if p.suffix == '.csv')).E_grid.tolist() == [3., 4.]
    again = batch.run_batch(**setup, base_reload='first_only', export_timeseries=True, resume=True)
    assert again.skipped == result.completed and len(FakeExcel.calls) == 4
    assert FakeExcel.closed


def test_failure_flushes_successes_resume_reloads_first_pending(setup, monkeypatch):
    monkeypatch.setattr(FakeExcel, 'failure', 1)
    first = batch.run_batch(**setup, base_reload='first_only')
    assert first.completed == ['Demo | A']
    assert first.status == 'failed' and 'Demo | B' in first.failed
    assert FakeExcel.captured == ['Demo | A']
    monkeypatch.setattr(FakeExcel, 'failure', None)
    resumed = batch.run_batch(**setup, base_reload='first_only', resume=True)
    assert resumed.skipped == ['Demo | A']
    assert FakeExcel.calls[2] == (1, True)
    assert len(resumed.completed) == 4


@pytest.mark.parametrize('kind', ['csv', 'xlsx', 'frame'])
def test_external_definitions_filter_and_exact_row_position(setup, tmp_path, kind):
    frame = FakeExcel.rows.copy()
    source = frame
    if kind != 'frame':
        source = tmp_path / f'scenarios.{kind}'
        if kind == 'csv':
            frame.to_csv(source, index=False, sep=';')
        else:
            frame.to_excel(source, index=False, sheet_name='Scenarios')
    result = batch.run_batch(**setup, scenarios=source, scenario_filter={'Base Scenario': 'Other'})
    assert result.completed == ['Demo | C', 'Demo | D']
    assert FakeExcel.calls == [(2, True), (3, True)]
    assert FakeExcel.configurations[0][1] is True


@pytest.mark.parametrize('change', ['workbook', 'definitions', 'chunk', 'options'])
def test_resume_rejects_changed_inputs_or_exports(setup, monkeypatch, change):
    result = batch.run_batch(**setup)
    if change == 'workbook':
        setup['workbook'].write_bytes(b'changed')
    elif change == 'definitions':
        rows = FakeExcel.rows.copy()
        rows.loc[0, 'Preset'] = 'changed'
        monkeypatch.setattr(FakeExcel, 'rows', rows)
    elif change == 'chunk':
        result.exported_files[0].write_bytes(b'corrupt')
    else:
        setup['batch_size'] = 3
    with pytest.raises(ValueError):
        batch.run_batch(**setup, resume=True)
    assert len(FakeExcel.calls) == 4


def test_validation_and_lock_prevent_excel_mutations(setup):
    with pytest.raises(ValueError, match='No scenarios'):
        batch.run_batch(**setup, scenario_filter={'Base Scenario': 'absent'})
    assert not FakeExcel.configurations
    frame = FakeExcel.rows.copy()
    frame.loc[1, 'Scenario Name'] = frame.loc[0, 'Scenario Name']
    with pytest.raises(ValueError, match='unique'):
        batch.run_batch(**setup, scenarios=frame)
    lock = setup['output_dir'] / '.batch.lock'
    lock.touch()
    with pytest.raises(FileExistsError):
        batch.run_batch(**setup)
    assert lock.exists() and not FakeExcel.calls


def test_no_overwrite_or_resume_without_annual(setup):
    batch.run_batch(**setup)
    with pytest.raises(FileExistsError):
        batch.run_batch(**setup)
    with pytest.raises(ValueError, match='annual'):
        batch.run_batch(**setup, resume=True, export_annual=False, export_timeseries=True)


def test_keyboard_interrupt_commits_captured_prefix(setup, monkeypatch):
    original = FakeExcel.run_scenario
    def interrupt(self, row, reload):
        if row == 1:
            raise KeyboardInterrupt()
        original(self, row, reload)
    monkeypatch.setattr(FakeExcel, 'run_scenario', interrupt)
    with pytest.raises(KeyboardInterrupt):
        batch.run_batch(**setup)
    saved = json.loads((setup['output_dir'] / 'batch.json').read_text())
    assert saved['chunks'][0]['scenarios'] == ['Demo | A']
    assert not (setup['output_dir'] / '.batch.lock').exists()


def table(name, headers, rows):
    return SimpleNamespace(Name=name, HeaderRowRange=SimpleNamespace(Value=(tuple(headers),)),
                           DataBodyRange=SimpleNamespace(Value=tuple(map(tuple, rows))),
                           ListColumns=lambda column: SimpleNamespace(DataBodyRange=SimpleNamespace(
                               Value=tuple((row[headers.index(column)],) for row in rows))))


def test_adapter_bulk_selection_boolean_macro_and_live_capture():
    adapter = PEExcelAdapter('dummy.xlsb')
    selection = SimpleNamespace(Value=None)
    adapter.scen = SimpleNamespace(ListRows=SimpleNamespace(Count=3), ListColumns=lambda name: SimpleNamespace(DataBodyRange=selection))
    adapter.book = SimpleNamespace(Name="model's.xlsb")
    calls = []
    def macro(*args):
        calls.append(args)
        assert selection.Value == ((False,), (True,), (False,))
        return True
    adapter.app = SimpleNamespace(Run=macro)
    adapter.inputs = table('IN', ['var_name', 'STAGE'], [['project_name', 'Demo']])
    adapter.outputs = table('OUT', ['var_name', 'Live'], [['QH', 42]])
    adapter.run_scenario(1, False)
    project = Project()
    adapter.capture_scenario(project, 'Demo | A')
    assert calls == [("'model''s.xlsb'!RunScenariosAutomated", False)]
    assert project[0].to_var_dict()['QH'] == 42
    assert project[0].project_name == 'Demo'
    adapter.app.Run = lambda *args: False
    with pytest.raises(RuntimeError):
        adapter.run_scenario(1, True)
    adapter.outputs = table('OUT', ['var_name', 'Wrong'], [['QH', 99]])
    with pytest.raises(ValueError, match='Live'):
        adapter.capture_scenario(project, 'Demo | B')
    assert len(project) == 1


def test_resume_ignores_workbook_execution_timestamp(setup, monkeypatch):
    rows = FakeExcel.rows.assign(Zeitpunkt=0)
    monkeypatch.setattr(FakeExcel, 'rows', rows)
    batch.run_batch(**setup)
    monkeypatch.setattr(FakeExcel, 'rows', rows.assign(Zeitpunkt=46310.5))
    result = batch.run_batch(**setup, resume=True)
    assert len(result.skipped) == 4 and len(FakeExcel.calls) == 4


def test_adapter_controls_and_sim_capture_restore_native_flags():
    adapter = PEExcelAdapter('dummy.xlsb')
    flags = {name: SimpleNamespace(Formula=((True,), (False,)), Value=None)
             for name in ('Simulieren?', 'Skip base reload?', 'SAVE as Scenario in Inputs?',
                          'Export as single project file incl. Timeseries?')}
    adapter.scen = SimpleNamespace(
        ShowTotals=False, HeaderRowRange=SimpleNamespace(Value=(tuple(flags),)),
        DataBodyRange=SimpleNamespace(Formula=(('original',),)),
        ListRows=SimpleNamespace(Count=2), ListColumns=lambda n: SimpleNamespace(DataBodyRange=flags[n]))
    adapter.configure_scenarios(pd.DataFrame(), replace=False)
    assert flags['SAVE as Scenario in Inputs?'].Value is False
    assert flags['Export as single project file incl. Timeseries?'].Value is False
    adapter.book = SimpleNamespace(Name='test.xlsb')
    adapter.app = SimpleNamespace(Run=lambda *args: True)
    adapter.run_scenario(0, True)
    assert flags['Skip base reload?'].Value is False
    adapter.inputs = table('IN', ['var_name', 'STAGE'], [['project_name', 'Demo']])
    adapter.outputs = table('OUT', ['var_name', 'Live'], [['QH', 42]])
    adapter._table = lambda name: table('sim', ['Ta', 'E_grid'], [[1, 2], [3, 4]])
    scenario = adapter.capture_scenario(Project(), 'Demo', timeseries=True)
    assert scenario.timeseries.to_frame().E_grid.tolist() == [2, 4]
    adapter.__exit__(None, None, None)
    assert all(f.Formula == ((True,), (False,)) for f in flags.values())


def test_external_configuration_bulk_writes_and_restores_formulas():
    from unittest.mock import MagicMock
    adapter = PEExcelAdapter('dummy.xlsb')
    scen = MagicMock()
    adapter.scen = scen
    scen.ShowTotals = False
    scen.ListRows.Count = 1
    scen.ListColumns.Count = 3
    scen.HeaderRowRange.Value = (('Scenario Name', 'Base Scenario', 'Simulieren?'),)
    original = (('old', '=SomeBase', False),)
    scen.DataBodyRange.Formula = original
    scen.HeaderRowRange.Offset.return_value.Resize.return_value.Formula = ((None, None, None),)
    columns = {name: MagicMock() for name in scen.HeaderRowRange.Value[0]}
    scen.ListColumns.side_effect = columns.__getitem__
    definitions = pd.DataFrame({'Scenario Name': ['A', 'B'], 'Base Scenario': ['Default', 'Default']})
    adapter.configure_scenarios(definitions, replace=True)
    assert columns['Scenario Name'].DataBodyRange.Value == (('A',), ('B',))
    assert columns['Base Scenario'].DataBodyRange.Value == (('Default',), ('Default',))
    assert scen.DataBodyRange.ClearContents.call_count == 1
    adapter.__exit__(RuntimeError, RuntimeError('calculation failed'), None)
    assert scen.DataBodyRange.Formula == original
    assert scen.DataBodyRange.ClearContents.call_count == 2
    assert scen.HeaderRowRange.Resize.call_args.args == (2, 3)
    # The same extension must fail before mutation if it would overwrite other data.
    adapter = PEExcelAdapter('dummy.xlsb')
    adapter.scen = scen
    scen.HeaderRowRange.Offset.return_value.Resize.return_value.Formula = (('keep', None, None),)
    with pytest.raises(ValueError, match='occupied'):
        adapter.configure_scenarios(definitions, replace=True)
    assert scen.DataBodyRange.ClearContents.call_count == 2


def test_atomic_manifest_retries_transient_windows_lock_and_keeps_old_file(tmp_path, monkeypatch):
    from pathlib import Path
    original = Path.replace
    target = tmp_path / 'batch.json'
    target.write_text('old')
    attempts = []
    def flaky(path, destination):
        attempts.append(path)
        if len(attempts) < 3:
            assert target.read_text() == 'old'
            raise PermissionError('temporarily locked')
        return original(path, destination)
    monkeypatch.setattr(Path, 'replace', flaky)
    monkeypatch.setattr(batch, 'sleep', lambda _: None)
    batch._atomic_json(target, {'new': True})
    assert len(attempts) == 3 and json.loads(target.read_text()) == {'new': True}


def test_adapter_restores_external_formulas_and_does_not_save_or_close_user_book():
    adapter = PEExcelAdapter('dummy.xlsb')
    body = SimpleNamespace(Formula=None, ClearContents=lambda: None)
    adapter.scen = SimpleNamespace(DataBodyRange=body)
    resized = []
    adapter._resize = resized.append
    adapter._restore = (2, (('=A1',), ('original',)), True)
    adapter.book = SimpleNamespace(Close=lambda **kwargs: pytest.fail('closed user workbook'))
    adapter.app = SimpleNamespace(Quit=lambda: pytest.fail('quit user Excel'))
    adapter.__exit__(RuntimeError, RuntimeError('failed run'), None)
    assert resized == [2] and body.Formula == (('=A1',), ('original',))


@pytest.mark.parametrize('notebook', ['notebooks/howto_batch_simulate.ipynb', 'website/tutorial_batch.ipynb'])
def test_notebooks_execute_public_batch_api_with_fake_excel(setup, notebook):
    from pathlib import Path
    import nbformat
    source = Path(__file__).resolve().parents[1] / notebook
    namespace = {'display': lambda value: None}
    for cell in nbformat.read(source, 4).cells:
        if cell.cell_type == 'code':
            assert 'win32com' not in cell.source and 'ListObjects' not in cell.source
            exec(compile(cell.source, notebook, 'exec'), namespace)
            if 'RUN_EXCEL = False' in cell.source:
                namespace.update(RUN_EXCEL=True, workbook=setup['workbook'],
                                 output_dir=setup['output_dir'], scenario_source=FakeExcel.rows.copy())
    assert namespace['result'].completed == ['Demo | A', 'Demo | B']
    assert namespace['summary']['QH'].tolist() == [10, 11]


def test_general_adapter_connects_without_accessing_scenario_tables(monkeypatch, tmp_path):
    import sys
    from types import ModuleType
    from unittest.mock import MagicMock
    path = tmp_path / 'model.xlsb'
    book = MagicMock()
    book.FullName = str(path)
    book.Worksheets.side_effect = AssertionError('Opening a session must not require SCEN')
    app = SimpleNamespace(Workbooks=[book])
    pythoncom = ModuleType('pythoncom')
    pythoncom.CoInitialize = MagicMock()
    pythoncom.CoUninitialize = MagicMock()
    pythoncom.com_error = type('ComError', (Exception,), {})
    client = ModuleType('win32com.client')
    client.GetActiveObject = lambda name: app
    client.DispatchEx = lambda name: pytest.fail('Existing workbook should be reused')
    win32com = ModuleType('win32com')
    win32com.client = client
    for name, module in [('pythoncom', pythoncom), ('win32com', win32com), ('win32com.client', client)]:
        monkeypatch.setitem(sys.modules, name, module)
    with PEExcelAdapter(path) as adapter:
        assert adapter.book is book
        assert 'scen' not in adapter.__dict__
        assert 'inputs' not in adapter.__dict__
    book.Worksheets.assert_not_called()
    book.Close.assert_not_called()
    pythoncom.CoUninitialize.assert_called_once()


def test_live_capture_does_not_require_scenario_configuration():
    adapter = PEExcelAdapter('model.xlsb')
    tables = {
        'IN': table('IN', ['var_name', 'STAGE'], [['project_name', 'Current']]),
        'OUT': table('OUT', ['var_name', 'Live'], [['QH', 17]]),
    }
    requested = []
    def lookup(name):
        requested.append(name)
        return tables[name]
    adapter._table = lookup
    scenario = adapter.capture_scenario(Project(), 'Current | Snapshot')
    assert scenario.to_var_dict()['QH'] == 17
    assert requested == ['IN', 'OUT']
    assert 'scen' not in adapter.__dict__ and adapter._restore is None
