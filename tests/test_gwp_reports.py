"""Current/legacy GWP boundaries and downstream data must agree."""
from copy import deepcopy
from pathlib import Path
import sys

import pandas as pd
import pytest

from pexl import Project, reporting
from pexl.plot import reports
from pexl.schema.current import CHARTS, ATTR_NAME_MAP
from pexl.reporting.gwp import LEGACY_CONSTRUCTION, LEGACY_TES

ROOT = Path(__file__).resolve().parents[1]
CURRENT = tuple(s.var_name for s in CHARTS['gwp_ee_detail'].series) + tuple(
    k for k in ATTR_NAME_MAP if k.startswith('GWP_ee_total'))


@pytest.fixture(scope='module')
def source_project():
    return Project.from_excel(ROOT / 'data/exports/examples/Bsp_San_6G.xlsx')


@pytest.fixture
def current(source_project):
    return deepcopy(source_project)


def as_legacy(project):
    result = Project()
    for original in project:
        scenario = deepcopy(original)
        scenario.column_name += ' legacy'
        for key in CURRENT:
            setattr(scenario.v, ATTR_NAME_MAP[key], None)
        result.add_scenario(scenario)
    return result


def test_schema_regeneration_matches_registry():
    from pexl.schema.report_codegen import generate_report_module_text
    folder = ROOT / 'data/schemas/1.13.1_dev'
    text = generate_report_module_text(pd.read_csv(folder/'CHART_types.csv', sep=';'),
                                      pd.read_csv(folder/'CHART_metadata.csv', sep=';'),
                                      version='1_13_1_dev')
    namespace = {}
    exec(text, namespace)
    assert namespace['CHARTS'] == CHARTS
    assert len(CHARTS['gwp_ee_detail'].series) == 36  # 35 parts, one net marker


def test_current_totals_precede_legacy_and_keep_mobility(current):
    s = current[0]
    assert s.v.GWP_ee_total_construction != s.v.legacy_GWP_ee_lc_construction
    r = reporting.gwp_ee(current)
    assert r['frame']['GWP_ee_total_construction'][0] == s.v.GWP_ee_total_construction
    assert 'GWP_ee_total' not in r['frame']  # do not add a subtotal again
    parts = [x['var_name'] for x in r['series'] if x['role'] != 'Balance Variable']
    assert r['frame'][parts].sum(axis=1)[0] == pytest.approx(s.v.GWP_lc_total)
    assert s.v.GWP_lc_EE_total == pytest.approx(s.v.GWP_ee_total+s.v.GWP_ee_lc_mob)
    assert r['sources'][s.column_name]['family'] == 'current'


def test_current_zero_is_not_missing(current):
    for key in CURRENT:
        setattr(current[0].v, ATTR_NAME_MAP[key], 0.)
    r = reporting.gwp_ee(current)
    assert r['frame']['GWP_ee_total_construction'][0] == 0
    assert r['sources'][current[0].column_name]['family'] == 'current'


def test_partial_current_does_not_borrow_legacy(current, caplog):
    current[0].v.GWP_ee_total_TES = None
    report = reporting.gwp_ee(current)
    assert pd.isna(report['frame']['GWP_ee_total_TES'][0])
    assert 'partial current' in caplog.text


def test_detail_and_fossil_biogenic_do_not_double_count(current):
    for make in [reporting.gwp_ee_detail, reporting.gwp_ee_fossil_biogenic]:
        r = make(current)
        parts = [s['var_name'] for s in r['series'] if s['role'] != 'Balance Variable']
        assert r['frame'][parts].sum(axis=1)[0] == pytest.approx(current[0].v.GWP_ee_total)
        fig = reports.render(r)
        assert any(v < 0 for t in fig.data if t.type == 'bar' for v in t.y)
        assert not fig.layout.shapes  # no district thresholds on embodied-only data
        assert len([t for t in fig.data if t.type == 'scatter']) == 1


def test_legacy_fallback_is_coarse_and_nonmutating(current):
    project = as_legacy(current)
    s = project[0]
    before = deepcopy(s.as_dict())
    r = reporting.gwp_ee(project)
    assert r['frame']['GWP_ee_total_construction'][0] == s.v.legacy_GWP_ee_lc_construction
    assert r['frame']['GWP_lc_total'][0] == s.v.legacy_GWP_lc_total
    assert r['sources'][s.column_name]['fields']['GWP_ee_total_TES'] == 'legacy_GWP_ee_lc_tga'
    detail = reporting.gwp_ee_detail(project)
    assert {x['var_name'] for x in detail['series']} == set(LEGACY_CONSTRUCTION+LEGACY_TES) | {'GWP_ee_total'}
    assert 'Legacy' in detail['title']
    assert detail['frame']['GWP_ee_total'][0] == pytest.approx(s.v.legacy_GWP_ee_lc_construction+s.v.legacy_GWP_ee_lc_tga)
    assert s.as_dict() == before
    with pytest.raises(ValueError, match='fossil/biogenic'):
        reporting.gwp_ee_fossil_biogenic(project)


def test_mixed_detail_has_only_structural_zeroes(current, caplog):
    old = as_legacy(current)[0]
    current.add_scenario(old)
    r = reporting.gwp_ee_detail(current)
    assert r['frame'].loc[0, list(LEGACY_CONSTRUCTION+LEGACY_TES)].eq(0).all()
    assert r['frame'].loc[1, 'GWP_ee_wall'] == 0
    assert r['frame'].loc[1, 'legacy_GWP_ee_lc_walls'] == old.v.legacy_GWP_ee_lc_walls
    old.v.legacy_GWP_ee_lc_walls = None
    report = reporting.gwp_ee_detail(current)
    assert pd.isna(report['frame'].loc[1, 'legacy_GWP_ee_lc_walls'])
    assert 'missing legacy' in caplog.text


def test_browser_payload_uses_resolved_legacy_values(current, monkeypatch):
    sys.path.insert(0, str(ROOT/'scripts'))
    import assessment_explained as viewer
    # Unrelated scenario-analysis panels need not be built to check report binding.
    monkeypatch.setattr(viewer, '_analysis_templates', lambda *args: {})
    project = as_legacy(current)
    payload = viewer.browser_data(project)
    r = reporting.gwp_ee(project)
    for series in r['series']:
        key = series['var_name']
        assert payload['scenarios'][0]['values'][payload['columns'][key]] == r['frame'].iloc[0][key]
    assert payload['scenarios'][0]['report_sources']['thg']['family'] == 'legacy'
    assert sum('meta' in t for t in payload['templates']['thg']['data']) == 5
