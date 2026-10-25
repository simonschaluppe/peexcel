"""Batch orchestration uses real Project serialization with a deterministic Excel boundary."""
import json
from types import SimpleNamespace

import pandas as pd
import pytest

from pexl import Project
from pexl import batch
from pexl.io.excel import read_project
from pexl.io.excel_com import PEExcelAdapter, _ScenarioFailure, _ExcelFailure
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

    def __init__(self, path, *, reuse_existing=True):
        pass

    def __enter__(self):
        return self

    def __exit__(self, *args):
        type(self).closed = True

    def _validate_scenarios(self, definitions, *, timeseries=False):
        pass

    def _recover(self, exc):
        return isinstance(exc, _ScenarioFailure)

    def read_scenarios(self):
        return self.rows.copy()

    def configure_scenarios(self, frame, *, replace):
        self.configurations.append((frame.copy(), replace))
        self.active = frame

    def run_scenario(self, row, reload):
        self.calls.append((row, reload))
        if self.failure == row:
            raise _ScenarioFailure('VBA returned False')
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


def test_progress_tracks_capture_resume_and_committed_completion(setup, monkeypatch):
    events = []

    def progress(done, total, name):
        events.append((done, total, name))
        if done == total:
            checkpoint = json.loads((setup['output_dir'] / 'batch.json').read_text())
            assert sum(len(chunk['scenarios']) for chunk in checkpoint['chunks']) == total
            assert all((setup['output_dir'] / chunk['annual']).is_file()
                       for chunk in checkpoint['chunks'])

    monkeypatch.setattr(FakeExcel, 'failure', 1)
    first = batch.run_batch(**setup, progress_callback=progress)
    assert first.status == 'failed'
    assert events == [(0, 4, ''), (1, 4, 'Demo | A'), (2, 4, 'Demo | C'), (3, 4, 'Demo | D')]
    events.clear()
    monkeypatch.setattr(FakeExcel, 'failure', None)
    batch.run_batch(**setup, resume=True, progress_callback=progress)
    assert events == [(3, 4, ''), (4, 4, 'Demo | B')]
    events.clear()
    calls = len(FakeExcel.calls)
    batch.run_batch(**setup, resume=True, progress_callback=progress)
    assert events == [(4, 4, '')]
    assert len(FakeExcel.calls) == calls


def test_progress_error_saves_capture_and_releases_session(setup):
    def progress(done, total, name):
        if done:
            raise RuntimeError('display failed')

    with pytest.raises(RuntimeError, match='display failed'):
        batch.run_batch(**setup, progress_callback=progress)
    assert FakeExcel.closed
    assert not (setup['output_dir'] / '.batch.lock').exists()
    resumed = batch.run_batch(**setup, resume=True)
    assert resumed.skipped == ['Demo | A']
    assert len(resumed.completed) == 4
    assert len(FakeExcel.calls) == 4


def test_failure_flushes_successes_resume_reloads_first_pending(setup, monkeypatch):
    monkeypatch.setattr(FakeExcel, 'failure', 1)
    first = batch.run_batch(**setup, base_reload='first_only')
    assert first.completed == ['Demo | A', 'Demo | C', 'Demo | D']
    assert first.status == 'failed' and 'Demo | B' in first.failed
    assert FakeExcel.captured == ['Demo | A', 'Demo | C', 'Demo | D']
    monkeypatch.setattr(FakeExcel, 'failure', None)
    resumed = batch.run_batch(**setup, base_reload='first_only', resume=True)
    assert resumed.skipped == ['Demo | A', 'Demo | C', 'Demo | D']
    assert FakeExcel.calls[4] == (1, True)
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



def test_default_logging_is_scoped_persistent_and_before_blocking_call(setup, monkeypatch, capsys):
    import logging
    root = (logging.getLogger().level, logging.getLogger().handlers.copy())
    previous = (batch.logger.level, batch.logger.handlers.copy(), batch.logger.propagate)
    original = FakeExcel.run_scenario
    def check(self, row, reload):
        text = (setup['output_dir'] / 'batch.log').read_text(encoding='utf-8')
        assert f'RUN [{row + 1:03d}/4]' in text
        original(self, row, reload)
    monkeypatch.setattr(FakeExcel, 'run_scenario', check)
    batch.run_batch(**setup)
    text = capsys.readouterr().err
    assert 'Checkpoint saved' in text and 'Summary: 4 completed' in text
    assert 'missing, nonnumeric or nonfinite PEI_balance' in text
    assert (logging.getLogger().level, logging.getLogger().handlers) == root
    assert (batch.logger.level, batch.logger.handlers, batch.logger.propagate) == previous
    batch.run_batch(**setup, resume=True)
    text = (setup['output_dir'] / 'batch.log').read_text(encoding='utf-8')
    assert text.count('Summary:') == 2


def test_retry_csv_preserves_selected_original_values_and_order(setup, monkeypatch):
    rows = FakeExcel.rows.copy()
    rows['Presets_geometry_table'] = ['001', 'NA', 'a;b,"c"', 'Zeile\nü']
    rows['Custom 1'] = ['x=1', '', 'x=2', 'x=3']
    monkeypatch.setattr(FakeExcel, 'rows', rows)
    monkeypatch.setattr(FakeExcel, 'failure', 1)
    result = batch.run_batch(**setup, scenarios=rows)
    retry = batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')
    assert retry.columns.tolist() == rows.columns.tolist()
    assert retry['Scenario Name'].tolist() == ['Demo | B']
    assert retry['Presets_geometry_table'].tolist() == ['NA']
    assert retry['Custom 1'].tolist() == ['']
    assert result.completed == ['Demo | A', 'Demo | C', 'Demo | D']
    monkeypatch.setattr(FakeExcel, 'failure', None)
    retried = batch.run_batch(setup['workbook'], scenarios=setup['output_dir'] / 'remaining_scenarios.csv',
                             output_dir=setup['output_dir'] / 'retry')
    assert retried.completed == ['Demo | B']
    assert batch._read_definitions(setup['output_dir'] / 'retry' / 'remaining_scenarios.csv').empty


def test_csv_literal_identifiers_roundtrip(tmp_path):
    frame = pd.DataFrame({'Scenario Name': ['001', 'NA'], 'Base Scenario': ['Default'] * 2,
                          'Presets_geometry_table': ['0002', 'a,b;"ü"\nnext'], 'Custom 1': ['', 'n=1.50']})
    batch._write_remaining(tmp_path, frame, [])
    pd.testing.assert_frame_equal(batch._read_definitions(tmp_path / 'remaining_scenarios.csv'), frame)


def test_inspect_reconciles_stale_csv_without_excel_or_original_source(setup, monkeypatch):
    monkeypatch.setattr(FakeExcel, 'failure', 1)
    batch.run_batch(**setup)
    FakeExcel.rows.to_csv(setup['output_dir'] / 'remaining_scenarios.csv', index=False)
    monkeypatch.setattr(FakeExcel, '__enter__', lambda self: pytest.fail('inspection opened Excel'))
    pending = batch.inspect_batch(setup['workbook'], output_dir=setup['output_dir'])
    assert pending['Scenario Name'].tolist() == ['Demo | B']
    assert batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')['Scenario Name'].tolist() == ['Demo | B']


def test_inspect_fresh_validates_without_configuring_or_running(setup):
    selected = batch.inspect_batch(setup['workbook'], scenario_filter={'Base Scenario': 'Other'})
    assert selected['Scenario Name'].tolist() == ['Demo | C', 'Demo | D']
    assert not FakeExcel.calls and not FakeExcel.configurations


@pytest.mark.parametrize('failure_point', ['annual', 'manifest', 'timeseries'])
def test_export_failure_never_commits_or_loses_retry_rows(setup, monkeypatch, failure_point):
    if failure_point == 'annual':
        monkeypatch.setattr(batch, 'write_project_excel', lambda *a, **k: (_ for _ in ()).throw(OSError('disk full')))
    elif failure_point == 'manifest':
        original = batch._atomic_json
        def fail(path, value):
            if value['chunks']:
                raise OSError('disk full')
            original(path, value)
        monkeypatch.setattr(batch, '_atomic_json', fail)
    else:
        original = batch._replace
        def fail(source, target):
            if target.name.startswith('sim-'):
                raise OSError('disk full')
            return original(source, target)
        monkeypatch.setattr(batch, '_replace', fail)
    with pytest.raises(OSError, match='disk full'):
        batch.run_batch(**setup, export_timeseries=failure_point == 'timeseries')
    manifest = json.loads((setup['output_dir'] / 'batch.json').read_text())
    assert not manifest['chunks']
    assert batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')['Scenario Name'].tolist() == FakeExcel.rows['Scenario Name'].tolist()
    assert FakeExcel.closed and not (setup['output_dir'] / '.batch.lock').exists()


def test_failed_checkpoint_retry_does_not_duplicate_chunk(setup, monkeypatch):
    original = batch._atomic_json
    attempts = []
    def fail_once(path, value):
        if value['chunks']:
            attempts.append(len(value['chunks']))
            if len(attempts) == 1:
                raise OSError('transient checkpoint failure')
        original(path, value)
    monkeypatch.setattr(batch, '_atomic_json', fail_once)
    with pytest.raises(OSError, match='transient checkpoint'):
        batch.run_batch(**setup)
    saved = json.loads((setup['output_dir'] / 'batch.json').read_text())
    assert len(saved['chunks']) == 1
    assert saved['chunks'][0]['scenarios'] == ['Demo | A', 'Demo | B']
    assert not saved['failed']
    resumed = batch.run_batch(**setup, resume=True)
    assert resumed.completed == FakeExcel.rows['Scenario Name'].tolist()
    assert len(FakeExcel.calls) == 4


def test_transient_timeseries_export_flushes_captured_result(setup, monkeypatch):
    original = batch._replace
    attempts = []
    def fail_once(source, target):
        if target.name.startswith('sim-'):
            attempts.append(target)
            if len(attempts) == 1:
                raise OSError('temporary export failure')
        original(source, target)
    monkeypatch.setattr(batch, '_replace', fail_once)
    with pytest.raises(OSError, match='temporary export'):
        batch.run_batch(**setup, export_timeseries=True)
    saved = json.loads((setup['output_dir'] / 'batch.json').read_text())
    assert saved['chunks'][0]['scenarios'] == ['Demo | A']
    assert len(saved['chunks'][0]['files']) == 2
    assert batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')['Scenario Name'].tolist() == ['Demo | B', 'Demo | C', 'Demo | D']


def test_interruption_survives_flush_csv_and_cleanup_errors(setup, monkeypatch):
    original = FakeExcel.run_scenario
    def interrupt(self, row, reload):
        if row == 1:
            raise KeyboardInterrupt('user stop')
        original(self, row, reload)
    monkeypatch.setattr(FakeExcel, 'run_scenario', interrupt)
    monkeypatch.setattr(batch, 'write_project_excel', lambda *a, **k: (_ for _ in ()).throw(OSError('export failed')))
    monkeypatch.setattr(FakeExcel, '__exit__', lambda *a: (_ for _ in ()).throw(RuntimeError('cleanup failed')))
    with pytest.raises(KeyboardInterrupt, match='user stop'):
        batch.run_batch(**setup)
    assert len(batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')) == 4
    assert not (setup['output_dir'] / '.batch.lock').exists()


def test_uncertain_macro_is_not_repeated_and_remaining_is_saved(setup, monkeypatch):
    def fail(self, row, reload):
        self.calls.append((row, reload))
        raise _ExcelFailure('macro', 0x80010108, uncertain=True)
    monkeypatch.setattr(FakeExcel, 'run_scenario', fail)
    result = batch.run_batch(**setup)
    assert result.status == 'failed' and len(FakeExcel.calls) == 1
    assert len(batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')) == 4


def test_legacy_manifest_upgrade_and_unknown_version_rejection(setup):
    batch.run_batch(**setup)
    path = setup['output_dir'] / 'batch.json'
    manifest = json.loads(path.read_text())
    for key in ('version', 'selected', 'runtime'):
        manifest.pop(key)
    path.write_text(json.dumps(manifest))
    batch.run_batch(**setup, resume=True)
    manifest = json.loads(path.read_text())
    assert manifest['version'] == 2 and 'selected' in manifest
    manifest['version'] = 99
    path.write_text(json.dumps(manifest))
    before = path.read_bytes()
    with pytest.raises(ValueError, match='version'):
        batch.run_batch(**setup, resume=True)
    assert path.read_bytes() == before


def test_adapter_retries_rejection_but_never_macro(monkeypatch):
    import pexl.io.excel_com as com
    monkeypatch.setattr(com, 'sleep', lambda _: None)
    class Rejected(Exception):
        hresult = -2147418111  # RPC_E_CALL_REJECTED
    attempts = []
    def flaky():
        attempts.append(1)
        if len(attempts) < 3:
            raise Rejected()
        return 42
    adapter = PEExcelAdapter('dummy.xlsb')
    assert adapter._call('read', flaky) == 42 and len(attempts) == 3
    attempts.clear()
    with pytest.raises(_ExcelFailure) as exc:
        adapter._call('macro', flaky, safe=False)
    assert exc.value.uncertain and len(attempts) == 1
    assert adapter._uncertain


def test_adapter_cleanup_preserves_primary_error_and_attempts_owned_close():
    adapter = PEExcelAdapter('dummy.xlsb')
    adapter._restore = (1, None, True)
    adapter.scen = SimpleNamespace(DataBodyRange=SimpleNamespace(ClearContents=lambda: (_ for _ in ()).throw(ValueError('restore failed'))))
    calls = []
    adapter.own_app = adapter.own_book = True
    adapter.book = SimpleNamespace(Close=lambda **k: calls.append('close'))
    adapter.app = SimpleNamespace(Quit=lambda: calls.append('quit'))
    adapter.__exit__(KeyboardInterrupt, KeyboardInterrupt(), None)
    assert calls == ['close', 'quit']


def test_adapter_uncertain_cleanup_does_not_touch_running_excel():
    adapter = PEExcelAdapter('dummy.xlsb')
    adapter.own_app = adapter.own_book = True
    adapter._uncertain = True
    adapter.book = SimpleNamespace(Close=lambda **k: pytest.fail('closed uncertain macro'))
    adapter.app = SimpleNamespace(Quit=lambda: pytest.fail('quit uncertain macro'))
    adapter.__exit__(None, None, None)


def test_adapter_reconnects_only_after_owned_process_exit(monkeypatch):
    import sys
    from types import ModuleType
    adapter = PEExcelAdapter('dummy.xlsb')
    adapter.own_app = True
    adapter.pid = 123
    adapter._process_handle = SimpleNamespace(Close=lambda: None)
    adapter.scen = object()
    event = ModuleType('win32event')
    event.WAIT_OBJECT_0 = 0
    event.WaitForSingleObject = lambda *args: 258
    monkeypatch.setitem(sys.modules, 'win32event', event)
    calls = []
    monkeypatch.setattr(PEExcelAdapter, '__enter__', lambda self: calls.append('open'))
    error = _ExcelFailure('macro', 0x80010108, uncertain=True)
    assert not adapter._recover(error) and not calls
    event.WaitForSingleObject = lambda *args: 0
    assert adapter._recover(error) and calls == ['open']
    assert 'scen' not in adapter.__dict__
    assert not adapter._recover(error)


def test_retry_csv_failure_does_not_hide_callback_error(setup, monkeypatch):
    original = batch._write_remaining
    def fail_on_cleanup(directory, selected, completed):
        if FakeExcel.calls:
            raise OSError('CSV unavailable')
        return original(directory, selected, completed)
    monkeypatch.setattr(batch, '_write_remaining', fail_on_cleanup)
    def callback(done, total, name):
        if done:
            raise RuntimeError('original callback failure')
    with pytest.raises(RuntimeError, match='original callback'):
        batch.run_batch(**setup, progress_callback=callback)
    assert not (setup['output_dir'] / '.batch.lock').exists()
    saved = json.loads((setup['output_dir'] / 'batch.json').read_text())
    assert saved['chunks'][0]['scenarios'] == ['Demo | A']



def test_adapter_validation_uses_dropdown_labels_and_custom_names():
    adapter = PEExcelAdapter('dummy.xlsb')
    adapter.inputs = table('IN', ['var_name', 'STAGE', 'Default'], [['project_name', 'Demo', 'Demo']])
    adapter.outputs = table('OUT', ['var_name', 'Live'], [['QH', 42]])
    tables = {
        'Presets_geometry_table': table('Presets_geometry_table', ['var_name', 'PRESETS>', 'G001'],
                                       [['dropdown_name', None, 'Two storey']]),
        'presets': table('presets', ['Preset Name'], [['Custom renovation']]),
    }
    adapter._table = tables.__getitem__
    rows = pd.DataFrame({'Scenario Name': ['A'], 'Base Scenario': ['Default'],
                         'Presets_geometry_table': [' two STOREY '], 'Custom 1': ['Custom renovation']})
    adapter._validate_scenarios(rows)
    with pytest.raises(ValueError, match='dropdown'):
        adapter._validate_scenarios(rows.assign(Presets_geometry_table='G001'))
    with pytest.raises(ValueError, match='custom'):
        adapter._validate_scenarios(rows.assign(**{'Custom 1': 'custom renovation'}))
    with pytest.raises(ValueError, match='Base Scenario'):
        adapter._validate_scenarios(rows.assign(**{'Base Scenario': 'not there'}))


def test_known_vba_cleanup_error_is_scenario_failure_only():
    class VBAError(Exception):
        hresult = -2147352567  # DISP_E_EXCEPTION
        excepinfo = (0, 'RunScenariosAutomated', 'Preset application failed', None, 0, -2147219205)
    adapter = PEExcelAdapter('dummy.xlsb')
    selection = SimpleNamespace(Value=None)
    adapter.scen = SimpleNamespace(ListRows=SimpleNamespace(Count=1),
                                   ListColumns=lambda name: SimpleNamespace(DataBodyRange=selection))
    adapter.book = SimpleNamespace(Name='model.xlsb')
    def fail(*args):
        raise VBAError()
    adapter.app = SimpleNamespace(Run=fail, Ready=True)
    with pytest.raises(_ScenarioFailure, match='Preset application failed'):
        adapter.run_scenario(0, True)
    assert not adapter._uncertain
    assert adapter._recover(_ScenarioFailure())
    VBAError.excepinfo = (0, 'OtherMacro', 'Unknown failure', None, 0, -2147219205)
    with pytest.raises(_ExcelFailure):
        adapter.run_scenario(0, True)
    assert adapter._uncertain


def test_interrupt_during_nonrepeatable_call_marks_state_uncertain():
    adapter = PEExcelAdapter('dummy.xlsb')
    with pytest.raises(KeyboardInterrupt):
        adapter._call('macro', lambda: (_ for _ in ()).throw(KeyboardInterrupt()), safe=False)
    assert adapter._uncertain


def test_failed_scenario_forces_reload_with_unchanged_base(setup, monkeypatch):
    monkeypatch.setattr(FakeExcel, 'failure', 2)
    result = batch.run_batch(**setup, base_reload='first_only')
    assert result.completed == ['Demo | A', 'Demo | B', 'Demo | D']
    assert FakeExcel.calls == [(0, True), (1, False), (2, True), (3, True)]


def test_retry_snapshot_retains_full_float_precision(tmp_path):
    original = pd.DataFrame({'Scenario Name': ['A'], 'Base Scenario': ['Default'],
                             'Zeitpunkt': [46310.586805555555], 'Custom 1': ['NA']})
    snapshot = batch._snapshot(original)
    path = tmp_path / 'batch.json'
    batch._atomic_json(path, snapshot)
    restored = batch._from_snapshot(json.loads(path.read_text()))
    pd.testing.assert_frame_equal(restored, original)


def test_standalone_script_logs_without_callback(setup):
    import subprocess
    import sys
    code = (
        'import sys; from pathlib import Path; from tests.test_batch import FakeExcel; '
        'from pexl import batch; batch.PEExcelAdapter=FakeExcel; '
        'r=batch.run_batch(Path(sys.argv[1]),output_dir=Path(sys.argv[2])); '
        'assert len(r.completed)==4'
    )
    completed = subprocess.run([sys.executable, '-c', code, str(setup['workbook']), str(setup['output_dir'])],
                               capture_output=True, text=True, timeout=60)
    assert completed.returncode == 0, completed.stderr
    assert 'RUN [001/4]' in completed.stderr and 'Summary: 4 completed' in completed.stderr


def test_notebook_typology_inspection_pilot_and_resume(setup, monkeypatch):
    import nbformat
    rows = FakeExcel.rows.copy()
    rows['Scenario Name'] = [f'EFH_1G|type{i}' for i in range(4)]
    rows['Base Scenario'] = 'Default'
    monkeypatch.setattr(FakeExcel, 'rows', rows)
    namespace = {'display': lambda value: None}
    for cell in nbformat.read('notebooks/howto_batch_simulate.ipynb', 4).cells:
        if cell.cell_type != 'code':
            continue
        exec(compile(cell.source, 'howto_batch_simulate.ipynb', 'exec'), namespace)
        if 'RUN_EXCEL = False' in cell.source:
            namespace.update(RUN_EXCEL=True, RUN_INSPECTION=True, RUN_RESUME=True,
                             workbook=setup['workbook'], output_dir=setup['output_dir'])
    assert namespace['result'].skipped == rows['Scenario Name'].tolist()[:3]
    assert len(FakeExcel.calls) == 3



def test_safe_com_retry_is_bounded(monkeypatch):
    import pexl.io.excel_com as com
    monkeypatch.setattr(com, 'sleep', lambda _: None)
    class Busy(Exception):
        hresult = -2147417846  # RPC_E_SERVERCALL_RETRYLATER
    calls = []
    def busy():
        calls.append(1)
        raise Busy()
    adapter = PEExcelAdapter('dummy.xlsb')
    with pytest.raises(_ExcelFailure):
        adapter._call('read', busy)
    assert len(calls) == 4 and not adapter._uncertain


def test_owned_session_rejects_existing_workbook_without_closing_it(monkeypatch, tmp_path):
    import sys
    from types import ModuleType
    from unittest.mock import MagicMock
    path = tmp_path / 'model.xlsb'
    book = MagicMock(FullName=str(path))
    app = SimpleNamespace(Workbooks=[book])
    pythoncom = ModuleType('pythoncom')
    pythoncom.CoInitialize = MagicMock()
    pythoncom.CoUninitialize = MagicMock()
    pythoncom.com_error = type('ComError', (Exception,), {})
    client = ModuleType('win32com.client')
    client.GetActiveObject = lambda name: app
    client.DispatchEx = lambda name: pytest.fail('created duplicate instance')
    win32com = ModuleType('win32com')
    win32com.client = client
    for name, module in [('pythoncom', pythoncom), ('win32com', win32com), ('win32com.client', client)]:
        monkeypatch.setitem(sys.modules, name, module)
    with pytest.raises(ValueError, match='already open'):
        with PEExcelAdapter(path, reuse_existing=False):
            pytest.fail('accepted caller-owned book')
    book.Close.assert_not_called()
    pythoncom.CoUninitialize.assert_called_once()


def test_setup_failure_with_external_definitions_leaves_retry_input(setup, monkeypatch):
    monkeypatch.setattr(FakeExcel, '__enter__', lambda self: (_ for _ in ()).throw(RuntimeError('Excel unavailable')))
    with pytest.raises(RuntimeError, match='Excel unavailable'):
        batch.run_batch(**setup, scenarios=FakeExcel.rows)
    assert len(batch._read_definitions(setup['output_dir'] / 'remaining_scenarios.csv')) == 4


def test_inspection_refuses_corrupt_export_and_retains_retry_csv(setup):
    result = batch.run_batch(**setup)
    csv = setup['output_dir'] / 'remaining_scenarios.csv'
    before = csv.read_bytes()
    result.exported_files[0].write_bytes(b'corrupt')
    with pytest.raises(ValueError, match='changed checkpoint'):
        batch.inspect_batch(setup['workbook'], output_dir=setup['output_dir'])
    assert csv.read_bytes() == before


def test_live_default_typology_pilot_when_explicitly_enabled(tmp_path):
    import os
    from pathlib import Path
    workbook = os.environ.get('PEEXCEL_LIVE_WORKBOOK')
    scenario_name = os.environ.get('PEEXCEL_LIVE_SCENARIO')
    if not workbook or not scenario_name:
        pytest.skip('Set PEEXCEL_LIVE_WORKBOOK and PEEXCEL_LIVE_SCENARIO for an explicit Excel pilot')
    rows = batch.inspect_batch(Path(workbook), scenario_filter={
        'Scenario Name': scenario_name, 'Base Scenario': 'Default'})
    result = batch.run_batch(Path(workbook), scenarios=rows, batch_size=1, output_dir=tmp_path / 'live')
    assert result.completed == [scenario_name] and not result.failed
    again = batch.run_batch(Path(workbook), scenarios=rows, batch_size=1,
                           output_dir=tmp_path / 'live', resume=True)
    assert again.skipped == [scenario_name]



def test_com_uninitialize_failure_does_not_mask_interrupt(monkeypatch):
    import sys
    from types import ModuleType
    pythoncom = ModuleType('pythoncom')
    pythoncom.CoUninitialize = lambda: (_ for _ in ()).throw(RuntimeError('uninitialize failed'))
    monkeypatch.setitem(sys.modules, 'pythoncom', pythoncom)
    adapter = PEExcelAdapter('dummy.xlsb')
    adapter._initialized = True
    adapter.__exit__(KeyboardInterrupt, KeyboardInterrupt(), None)
    assert not adapter._initialized



def test_existing_scenario_subset_does_not_replace_table(setup):
    selected = batch.inspect_batch(setup['workbook']).iloc[[1, 3]]
    result = batch.run_batch(**setup, scenarios=selected)
    assert result.completed == ['Demo | B', 'Demo | D']
    assert FakeExcel.calls == [(1, True), (3, True)]
    assert FakeExcel.configurations[0][1] is False
    pd.testing.assert_frame_equal(FakeExcel.configurations[0][0], FakeExcel.rows)



def test_overwrite_restarts_batch_but_keeps_other_files(setup):
    batch.run_batch(**setup, export_timeseries=True)
    directory = setup['output_dir']
    (directory / 'run.py').write_text('# keep')
    (directory / 'notes.csv').write_text('keep')
    result = batch.run_batch(**setup, scenarios=FakeExcel.rows.head(1), overwrite=True)
    assert result.completed == ['Demo | A']
    assert len(FakeExcel.calls) == 5
    assert not list(directory.glob('sim-*.csv'))
    assert len(list(directory.glob('annual-*.xlsx'))) == 1
    assert (directory / 'run.py').read_text() == '# keep'
    assert (directory / 'notes.csv').read_text() == 'keep'


def test_overwrite_rejects_resume_and_respects_lock(setup):
    with pytest.raises(ValueError, match='cannot be combined'):
        batch.run_batch(**setup, resume=True, overwrite=True)
    setup['output_dir'].mkdir()
    (setup['output_dir'] / '.batch.lock').touch()
    sentinel = setup['output_dir'] / 'batch.json'
    sentinel.write_text('keep')
    with pytest.raises(FileExistsError):
        batch.run_batch(**setup, overwrite=True)
    assert sentinel.read_text() == 'keep'
