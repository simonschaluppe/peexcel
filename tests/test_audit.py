from pathlib import Path

import nbformat
import pandas as pd
import pytest

from pexl import Project
from pexl.reporting import audit
from pexl.reporting.document import render_notebook
from pexl.schema.current import ATTR_NAME_MAP


def balance_frame():
    return pd.DataFrame({'PEI_import': [30., 12.], 'PEI_export': [20., 20.],
                         'PEI_saldo_project': [-10., 8.], 'PEI_saldo_target': [-15., 3.],
                         'PEI_importExport_balance': [5., 5.]}, index=['A', 'B'])


def test_exact_selection_and_balance_consistency():
    frame = balance_frame()
    before = frame.copy(deep=True)
    assert audit.table(frame, 'balance', scenario='B').Wert.tolist() == [12., 20., 8., 3., 5.]
    pd.testing.assert_frame_equal(frame, before)
    with pytest.raises(ValueError, match='exactly one'):
        audit.table(frame, 'balance')
    with pytest.raises(ValueError, match='Unknown scenario'):
        audit.select_scenario(frame, 'AW Holz')
    frame.loc['A','PEI_saldo_project'] = 99
    with pytest.raises(ValueError, match='Inconsistent'):
        audit.table(frame, 'balance', scenario='A')


@pytest.mark.parametrize('bad', [None, float('nan'), float('inf'), '30'])
def test_missing_balance_never_becomes_success(bad):
    frame = balance_frame().astype(object)
    frame.loc['A','PEI_import'] = bad
    with pytest.raises(ValueError, match='Incomplete'):
        audit.table(frame, 'balance', scenario='A')


def test_optional_missing_and_schema_requirements():
    assert all(n in ATTR_NAME_MAP for names in audit.TABLES.values() for n in names)
    result = audit.table(balance_frame(), 'pv', scenario='A')
    assert result.Wert.isna().all()
    assert 'PV_kWp' in result.attrs['missing']


def test_pv_units_and_zero_capacity():
    frame = pd.DataFrame({'PV_total':[20.], 'NFA_total':[1000.], 'PV_kWp':[25.]}, index=['A'])
    result = audit.table(frame, 'pv').set_index('var_name')
    assert result.loc['PV_total * NFA_total / 1000','Wert'] == 20
    assert result.loc['PV_total * NFA_total / PV_kWp','Wert'] == 800
    frame['PV_kWp'] = 0
    assert pd.isna(audit.table(frame,'pv').set_index('var_name').loc['PV_total * NFA_total / PV_kWp','Wert'])


def test_project_scenario_view_and_dataframe_agree():
    project = Project()
    for name,row in balance_frame().iterrows():
        scenario = project.get_or_create_scenario(name)
        for key,value in row.items():
            setattr(scenario.v, ATTR_NAME_MAP[key], value)
    expected = audit.table(project, 'balance', scenario='B')
    for source in [project['B'], project.view, project.view.to_frame()]:
        actual = audit.table(source, 'balance', scenario=None if source is project['B'] else 'B')
        pd.testing.assert_frame_equal(actual, expected)


def test_invalid_formats_do_not_execute(tmp_path):
    path = tmp_path/'bad.ipynb'
    nbformat.write(nbformat.v4.new_notebook(),path)
    with pytest.raises(ValueError, match='formats'):
        render_notebook(path, formats=['pdf'])


def test_real_typologies_if_available():
    path = Path(__file__).resolve().parents[1] / 'data/Excel Files/THG Bilanzierung/Klimagemeinschaften_typen.xlsx'
    if not path.is_file():
        pytest.skip('Private example workbook is not checked into the repository')
    project = Project(path)
    assert len(project) > 0
    assert 'Hol_PHniv' in [s.column_name for s in project]
    for scenario in project:
        for name in audit.TABLES:
            result = audit.table(scenario, name)
            assert result.attrs['scenario'] == scenario.column_name
        for name in ['usage','primary_energy_balance','final_energy_balance','heat_balance','flexibility']:
            figure = audit.chart(scenario,name)
            assert figure.data


def test_export_control_cells_and_saved_text(tmp_path):
    # Full small integration: real Quarto, no charts/Chrome needed.
    import shutil
    if not shutil.which('quarto'):
        pytest.skip('Quarto integration requires the external executable')
    nb = nbformat.v4.new_notebook(cells=[
        nbformat.v4.new_markdown_cell('# Mein Audit\n\nEigener gespeicherter Text.'),
        nbformat.v4.new_code_cell("raise RuntimeError('must not execute')", metadata={'tags':['audit-control']}),
        nbformat.v4.new_code_cell("from IPython.display import display, Markdown; display(Markdown('Frisches Ergebnis'))")])
    path = tmp_path/'auditbericht.ipynb'
    nbformat.write(nb,path)
    before = path.read_bytes()
    result = render_notebook(path)
    assert path.read_bytes() == before
    assert 'Eigener gespeicherter Text' in result['html'].read_text(encoding='utf-8')
    assert 'Frisches Ergebnis' in result['html'].read_text(encoding='utf-8')
    from zipfile import ZipFile
    with ZipFile(result['docx']) as z:
        xml = z.read('word/document.xml').decode()
    assert 'Eigener gespeicherter Text' in xml and 'Frisches Ergebnis' in xml


def test_html_plotly_is_offline(tmp_path):
    import shutil
    from html.parser import HTMLParser
    if not shutil.which('quarto'):
        pytest.skip('Quarto integration requires the external executable')
    nb = nbformat.v4.new_notebook(cells=[nbformat.v4.new_code_cell('',outputs=[
        nbformat.v4.new_output('display_data', data={
            'application/vnd.plotly.v1+json': {'data':[{'type':'bar','x':['A'],'y':[3]}],
                                            'layout':{'title':{'text':'Offline chart'}}}})])])
    path = tmp_path/'plot.ipynb'
    nbformat.write(nb,path)
    result = render_notebook(path,formats=('html',),execute=False)
    html = result['html'].read_text(encoding='utf-8')
    assert 'Plotly.newPlot' in html and 'PEXL-PLOT-' not in html
    class Resources(HTMLParser):
        external = []
        def handle_starttag(self, tag, attrs):
            if tag in ('script','img','link'):
                attributes = dict(attrs)
                url = attributes.get('src',attributes.get('href',''))
                if url.startswith(('http://','https://')):
                    self.external.append(url)
    parsed = Resources()
    parsed.feed(html)
    assert not parsed.external
