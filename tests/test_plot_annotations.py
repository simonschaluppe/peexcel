"""Optional assessment overlays leave the existing report and traces intact."""
from copy import deepcopy

import pandas as pd
import pytest

from pexl.plot.reports import render, chart


def report(kind="pe"):
    pe = kind == "pe"
    return {
        "chart_name": "primary_energy_balance" if pe else "gwp_ee",
        "chart_type": "stacked_bar_comparison" if pe else "build_gwp_chart",
        "title": "Beispiel", "unit": "kWhPE/m²NGFa" if pe else "kg CO₂e/m² BGF",
        "frame": pd.DataFrame({"Variant": ["A", "B", "C"],
                               "need": [100, 100, 100], "supply": [120, 80, 100],
                               "ee": [200, 200, 200], "oe": [-20, 200, 120],
                               "total": [180, 400, 320]}),
        "series": [
            {"var_name": name, "label": name, "role": role, "color": "#123456"}
            for name, role in ([('need', 'Bedarf'), ('supply', 'Deckung')] if pe else
                               [('ee', 'Baulich'), ('oe', 'Betrieblich'), ('total', 'Balance Variable')])
        ],
    }


def test_pe_difference_signs_positions_and_defaults():
    data = report()
    before = deepcopy(data)
    plain = render(data, annotate=False)
    annotated = render(data)
    assert annotated.to_json() == render(data, annotate=True).to_json()
    assert [t.to_plotly_json() for t in plain.data] == [t.to_plotly_json() for t in annotated.data]
    assert not plain.layout.shapes and not plain.layout.annotations
    assert [a.x for a in annotated.layout.annotations] == [0.5, 2.5, 4.5]
    assert [a.font.color for a in annotated.layout.annotations] == ['#237a45', '#ba3030', '#59636e']
    assert all(s.y0 == 100 for s in annotated.layout.shapes[::3])
    assert [s.y1 for s in annotated.layout.shapes[::3]] == [120, 80, 100]
    assert '+20,0' in annotated.layout.annotations[0].text
    assert '−' in annotated.layout.annotations[0].text
    pd.testing.assert_frame_equal(data['frame'], before['frame'])
    assert data['series'] == before['series']


def test_budget_uses_signed_net_total_and_preserves_bands():
    data = report('gwp')
    plain = render(data, annotate=False)
    annotated = render(data)
    assert len(plain.layout.annotations) == 1  # reference label only
    assert [band.visible for band in plain.layout.shapes[:3]] == [True, 'legendonly', 'legendonly']
    assert plain.layout.shapes[0].y1 == plain.layout.shapes[3].y0 == plain.layout.shapes[3].y1 == 320
    assert [t.to_plotly_json() for t in plain.data] == [t.to_plotly_json() for t in annotated.data]
    assert len(annotated.data) == 3
    assert all(list(t.x) == ['A', 'B', 'C'] for t in annotated.data)
    assert list(annotated.data[1].y) == [-20, 200, 120]
    assert list(annotated.data[2].y) == [180, 400, 320]
    assert annotated.layout.barmode == 'relative'
    assert 'unterschritten' in annotated.layout.annotations[1].text
    assert '140,0' in annotated.layout.annotations[1].text
    assert 'überschritten' in annotated.layout.annotations[2].text
    assert '80,0' in annotated.layout.annotations[2].text
    assert annotated.layout.annotations[3].text == 'Budget erreicht'
    assert annotated.layout.shapes[4].y0 == 180
    assert [a.x for a in annotated.layout.annotations[1:]] == [0, 1, 2]
    assert [a.y for a in annotated.layout.annotations[1:]] == [320, 400, 320]
    assert all(not a.showarrow and a.yanchor == 'bottom' and a.yshift > 0
               for a in annotated.layout.annotations[1:])


def test_all_gwp_entry_points_share_defaults_and_custom_budget(monkeypatch):
    import pexl.reporting
    data = report('gwp')
    monkeypatch.setattr(pexl.reporting, 'materialize', lambda *args, **kwargs: data)
    for options in ({}, {'budget': 250, 'legend_position': 'right'}, {'annotate': False}):
        expected = render(data, **options).to_json()
        assert chart(None, 'gwp_ee', **options).to_json() == expected
        assert pexl.reporting.gwp_ee_plot(None, **options).to_json() == expected

    custom = render(data, budget=250)
    assert custom.layout.shapes[0].y1 == custom.layout.shapes[3].y0 == 250
    assert custom.layout.shapes[4].y1 == 250
    assert '250,0' in custom.layout.annotations[0].text
    assert '70,0' in custom.layout.annotations[1].text


def test_invalid_budget_is_explicit():
    with pytest.raises(ValueError, match='GWP overview'):
        render(report(), budget=320)
    with pytest.raises(ValueError, match='finite'):
        render(report('gwp'), budget=float('nan'))
