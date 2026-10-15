"""Real-export reconciliation and safeguards for configured publication."""
import sys
from pathlib import Path

import pandas as pd
import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import website_examples as examples


@pytest.fixture(scope='module')
def reports():
    return examples.annual_reports()


def test_exported_balances_reconcile(reports):
    checks = examples.balance_checks(reports)
    closed = checks[checks.Diagramm != 'primary_energy_balance']
    assert closed.Differenz.abs().max() < 1e-6
    assert checks[checks.Diagramm == 'primary_energy_balance'].Differenz.gt(0).all()
    final = reports['final_energy_balance']
    assert not {'PV_to_Egrid','Eev_ext_charge'} & {s['var_name'] for s in final['series']}
    assert next(s for s in final['series'] if s['var_name']=='EUIdhwdirect_el')['role']=='Bedarf'


def test_ghg_retains_credits_and_export_total(reports):
    from pexl.plot.plotly import render
    report = reports['gwp_ee']
    figure = render(report)
    assert any(any(v is not None and v < 0 for v in trace.y) for trace in figure.data)
    total = next(t for t in figure.data if t.name == 'THG-Gesamtbilanz')
    assert list(total.y) == list(report['frame']['GWP_lc_total'])


def test_no_missing_value_or_channel_fallback():
    with pytest.raises(ValueError,match='Missing exported'):
        examples.numeric_frame(pd.DataFrame({'a':[1]}),['b'])
    with pytest.raises(ValueError,match='non-finite'):
        examples.numeric_frame(pd.DataFrame({'a':[float('nan')]}),['a'])


def test_exact_config_selection(tmp_path):
    config = examples.configuration()
    assert config['dynamic_example']['scenario'] == 'Aspern PVCheck _ F7'
    entry = dict(config['examples'][0],scenario='not present')
    with pytest.raises(ValueError,match='Expected exactly'):
        examples.load_entry(entry)
    config['examples'][1]['id'] = config['examples'][0]['id']
    path = tmp_path/'examples.yml'
    path.write_text(yaml.safe_dump(config),encoding='utf-8')
    with pytest.raises(ValueError,match='unique'):
        examples.configuration(path)


def test_aspern_profiles_and_channel_inventory():
    scenario = examples.load_entry(examples.configuration()['dynamic_example']).scenarios[0]
    frame = examples.hourly_frame(scenario)
    assert len(frame) == 8760
    inventory = examples.flow_inventory(scenario).set_index('Kanal')
    assert not inventory.loc['E_plugAuxLight','Exportiert']
    assert pd.isna(inventory.loc['E_plugAuxLight','Summe Exportwerte'])
    figures = examples.dynamic_figures(scenario)
    seasons = figures['f7_seasons']
    winter_grid = frame.loc[frame.index.month.isin([12,1,2])].groupby('hour_of_the_day')['E_grid'].mean()
    trace = next(t for t in seasons.data if t.name == examples.FLOW_LABELS['E_grid'])
    assert list(trace.y) == pytest.approx(winter_grid.tolist())
    hourly = figures['f7_hourly']
    assert len(hourly.data[0].x) == 8760
    assert hourly.layout.updatemenus[0].buttons[2].label == 'Gesamtjahr'
    original = scenario.timeseries.to_frame()
    try:
        scenario.set_timeseries(original.iloc[[0,2,3]])
        with pytest.raises(ValueError,match='continuous'):
            examples.hourly_frame(scenario)
    finally:
        scenario.set_timeseries(original)
