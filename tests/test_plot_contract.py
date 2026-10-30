"""Reference contracts: custom data and project reports share native renderers."""
from copy import deepcopy
from pathlib import Path

import pandas as pd
import pytest

from pexl import Project, reporting
from pexl.plot import electricity_balance, electricity_balance_facets
from pexl.plot import reports
from pexl.analysis.temporal import seasonal_hourly_mean, channel_inventory


@pytest.fixture(scope='module')
def project():
    return Project.from_excel(Path(__file__).resolve().parents[1] / 'data/exports/examples/Bsp_San_6G.xlsx')


def test_named_report_project_view_and_compatibility(project):
    a = reporting.primary_energy_balance(project)
    b = reporting.materialize(project.view, 'primary_energy_balance')
    pd.testing.assert_frame_equal(a['frame'], b['frame'])
    assert a['series'] == b['series']
    assert reports.render(a, annotate=True).to_json() == reports.chart(project, 'primary_energy_balance').to_json()
    from pexl.plot.plotly import render
    assert render is reports.render


def test_unit_conversion_and_language_preserve_values(project):
    original = reporting.primary_energy_balance(project)
    before = deepcopy(original)
    converted = reporting.convert_unit(original, original['unit'].replace('kWh', 'MWh', 1))
    for series in original['series']:
        key = series['var_name']
        assert converted['frame'][key].iloc[0] == pytest.approx(original['frame'][key].iloc[0] / 1000)
    pd.testing.assert_frame_equal(original['frame'], before['frame'])
    assert original['series'] == before['series']
    english = reporting.primary_energy_balance(project, language='en')
    pd.testing.assert_frame_equal(original['frame'], english['frame'])
    assert english['series'][0]['label'] == 'Plug loads'
    fig = reports.render(english, annotate=True)
    assert 'Supply' in fig.layout.annotations[0].text
    assert 'Demand' in fig.data[0].x[1]
    assert [list(t.y) for t in reports.render(original).data] == [list(t.y) for t in fig.data]
    with pytest.raises(ValueError, match='reference'):
        reporting.convert_unit(original, 'MWh')


def test_report_missing_values_do_not_become_zero(project):
    report = reporting.primary_energy_balance(project)
    report['frame'].loc[0, report['series'][0]['var_name']] = float('nan')
    with pytest.raises(ValueError, match='non-finite'):
        reports.render(report)


def test_custom_columns_signed_values_and_input_immutability():
    frame = pd.DataFrame({'my_generation': [3., -2.], 'my_demand': [-1., -4.]})
    before = frame.copy(deep=True)
    fig = electricity_balance(frame, positive=['my_generation'], negative=['my_demand'], value_mode='signed')
    assert list(fig.data[0].y) == [3, -2]
    assert list(fig.data[1].y) == [-1, -4]
    assert list(fig.data[1].customdata) == [-1, -4]
    scaled = electricity_balance(frame * 2, positive=['my_generation'], negative=['my_demand'], value_mode='signed')
    assert list(scaled.data[0].y) == [6, -4]
    pd.testing.assert_frame_equal(frame, before)
    frame.loc[0, 'my_demand'] = float('nan')
    with pytest.raises(ValueError, match='non-finite'):
        electricity_balance(frame, positive=['my_generation'], negative=['my_demand'])


def test_native_time_controls_and_wrapping_facets():
    index = pd.date_range('2025-01-01', periods=48, freq='h')
    frame = pd.DataFrame({'custom': range(48)}, index=index)
    fig = electricity_balance(frame, positive=['custom'], negative=[], language='en',
                              ranges={'Day 1': [index[0], index[24]]},
                              initial_range=[index[0], index[24]], rangeslider=True)
    assert fig.layout.xaxis.rangeslider.visible
    assert fig.layout.updatemenus[0].buttons[-1].label == 'Full period'
    assert fig.layout.updatemenus[0].active == 0
    assert len(fig.data[0].x) == 48
    means = seasonal_hourly_mean(frame, ['custom'])
    assert means['custom'].tolist() == pytest.approx(list(range(12, 36)))
    data = pd.DataFrame({'season': ['a', 'b', 'c', 'd'], 'custom': [1, 2, 3, 4]})
    facets = electricity_balance_facets(data, positive=['custom'], negative=[], facet='season')
    assert facets.layout.xaxis.domain == facets.layout.xaxis3.domain
    assert facets.layout.yaxis.domain != facets.layout.yaxis3.domain
    inventory = channel_inventory(frame, {'mine': ['custom', 'absent']})
    assert inventory['present'].tolist() == [True, False]
    assert pd.isna(inventory.iloc[1]['sum'])
