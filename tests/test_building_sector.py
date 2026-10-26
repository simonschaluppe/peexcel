"""Technical acceptance; scientific anomalies are recorded, not repaired."""
import importlib.util
import json
import math
from pathlib import Path
import sys

import pandas as pd
import pytest

from pexl import Project, reporting
from pexl.model.scenario import Scenario
from pexl.plot import plotly
from pexl.analysis.targets import target

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from assessment_explained import browser_data, context_values, CONTEXT, build
from build_building_sector_results import check_roundtrip, inspect_sources, digest


@pytest.fixture(scope='module')
def sample():
    return Project.from_excel(ROOT / 'data/exports/typologies/building_sector/annual-00001.xlsx', unknown='raise')


def test_roundtrip_checks_all_values_and_identities(sample, tmp_path):
    path = sample.to_excel(tmp_path / 'sample.xlsx', include_out=True)
    restored = Project.from_excel(path, unknown='raise')
    assert check_roundtrip(sample, restored) > 20000
    restored[0].v.PV_roof_share = 0.99
    with pytest.raises(ValueError, match='PV_roof_share'):
        check_roundtrip(sample, restored)


def test_payload_is_compact_and_uses_recorded_inputs(sample):
    payload = browser_data(sample)
    assert len(payload['scenarios']) == 25
    assert len(payload['templates']) == 2
    assert len(payload['analysis']) == 5
    for figure in payload['analysis'].values():
        assert sorted(i for t in figure['data'] for i in t['meta']['ids']) == list(range(len(sample)))
    assert all('plots' not in s for s in payload['scenarios'])
    assert payload['scenarios'][0]['filters']['pv'] == '30 %'
    assert payload['scenarios'][0]['filters']['geometry'] == sample[0].v.preset_recorded_geometry
    assert json.dumps(payload, allow_nan=False)
    for key, chart in [('pe', 'primary_energy_balance'), ('thg', 'gwp_ee')]:
        report = reporting.materialize(sample.view, chart)
        for series in report['series']:
            column = payload['columns'][series['var_name']]
            assert [s['values'][column] for s in payload['scenarios']] == report['frame'][series['var_name']].tolist()


@pytest.mark.parametrize('bgf,gf,renovation', [(100,1000,0),(2000,1000,50),(10000,1000,100)])
def test_context_preserves_original_and_uses_schema(sample, bgf, gf, renovation):
    original = {k: getattr(sample[0].v, k) for k in CONTEXT}
    before = original.copy()
    adjusted = context_values(original, bgf=bgf, gf=gf, renovation=renovation)
    c = -min(original['cfd_fPE']*(original['cfd_A']/(bgf/gf+original['cfd_dx'])-original['cfd_EUI']),original['cfd_cutoff'])
    assert adjusted['context_factor_density'] == pytest.approx(c)
    assert adjusted['PEI_cf_density_pos'] + adjusted['PEI_cf_density_neg'] == pytest.approx(c)
    assert adjusted['PEI_cf_renovation'] == original['cfr_budget']*renovation/100
    assert original == before
    assert context_values(original) == original
    assert adjusted['GFA_total'] == original['GFA_total']
    assert adjusted['PEI_balance'] - original['PEI_balance'] == pytest.approx(
        c-original['context_factor_density']+adjusted['PEI_cf_renovation']-original['PEI_cf_renovation'])


@pytest.mark.parametrize('kwargs',[dict(bgf=0,gf=10),dict(bgf=10),dict(renovation=-1),dict(renovation=101),dict(renovation=math.inf)])
def test_invalid_context(sample, kwargs):
    with pytest.raises(ValueError):
        context_values({k:getattr(sample[0].v,k) for k in CONTEXT}, **kwargs)


def test_zero_cutoff_matches_excel_min():
    assert target(0.1, cutoff=0) == 0
    assert target(0.1, cutoff=None) > 0


def test_gwp_compatibility_uses_exported_totals(sample):
    r = reporting.materialize(sample.view, 'gwp_ee')
    assert {s['var_name'] for s in r['series']} == {'GWP_lc_EE_total','GWP_lc_OE_total','GWP_lc_total'}
    assert (r['frame'].GWP_lc_EE_total+r['frame'].GWP_lc_OE_total-r['frame'].GWP_lc_total).abs().max() < 1e-8
    assert len(plotly.render(r).data) == 6


def test_generic_plots_use_schema_and_scenario_identity(sample):
    fig = plotly.scenario_scatter(sample.view, 'PEI_virtual_demand','PEI_virtual_supply', color='preset_recorded_heating_system', size='GFA_total')
    assert sum(len(t.x) for t in fig.data) == len(sample)
    assert 'NGF' in fig.layout.xaxis.title.text
    assert plotly.scenario_distribution(sample.view,'QH',by='preset_recorded_hulls').data
    report = reporting.materialize(sample.view, 'final_energy_balance')
    figure = plotly.report_balance_scatter(sample.view, 'final_energy_balance', 'FSI')
    expected = [s-d for s,d in zip(plotly._role_total(report, 'Deckung', absolute=True), plotly._role_total(report, 'Bedarf', absolute=True))]
    assert list(figure.data[0].y) == pytest.approx(list(expected))
    with pytest.raises(ValueError):
        plotly.scenario_distribution(sample.view,'QH',by='preset_recorded_hulls',kind='pie')


def test_single_file_manifest_and_corruption(tmp_path, sample):
    path=sample.to_excel(tmp_path/'annual-00001.xlsx',include_out=True)
    names=sample.column_names()
    pd.DataFrame({'Scenario Name':names}).to_csv(tmp_path/'scenarios_5400_SCEN.csv',sep=';',index=False)
    manifest={'identity':{'definitions':json.dumps({'columns':['Scenario Name'],'data':[[n] for n in names]}),'schema':'1_13_1_dev','base_reload':'first_only'},
              'chunks':[{'annual':path.name,'scenarios':names,'files':{path.name:digest(path)}}], 'failed':{}}
    (tmp_path/'batch.json').write_text(json.dumps(manifest),encoding='utf-8')
    paths,audit=inspect_sources(tmp_path,expected=25)
    assert audit['scenarios']==25 and paths==[path]
    manifest['chunks'][0]['files'][path.name]='wrong'
    (tmp_path/'batch.json').write_text(json.dumps(manifest),encoding='utf-8')
    with pytest.raises(ValueError,match='hash mismatch'):
        inspect_sources(tmp_path,expected=25)


def test_browser_context_matches_python_if_benchmark_available(sample):
    path=ROOT/'notebooks/local_exports/building_sector/browser/browser-performance.json'
    if not path.exists():
        pytest.skip('Run quickcheck_browser.cjs for cross-language acceptance')
    result=json.loads(path.read_text())['results'][0]['contextSample']
    data=browser_data(sample)
    expected=context_values({k:getattr(sample[0].v,k) for k in CONTEXT},bgf=2000,gf=1000,renovation=50)
    for key in CONTEXT:
        assert result[data['columns'][key]] == pytest.approx(expected[key])
