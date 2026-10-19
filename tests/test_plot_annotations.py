"""Optional assessment overlays leave the existing report and traces intact."""
from copy import deepcopy

import pandas as pd
import pytest

from pexl.plot.plotly import render, chart


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
    plain = render(data)
    annotated = render(data, annotate=True)
    assert plain.to_json() == render(data, annotate=False).to_json()
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
    plain = render(data)
    line = render(data, budget=320)
    annotated = render(data, budget=320, annotate=True)
    assert len(plain.layout.shapes) == 3
    assert len(line.layout.shapes) == 4
    assert line.layout.shapes[-1].y0 == line.layout.shapes[-1].y1 == 320
    assert [t.to_plotly_json() for t in plain.data] == [t.to_plotly_json() for t in annotated.data]
    assert 'unterschritten' in annotated.layout.annotations[1].text
    assert '140,0' in annotated.layout.annotations[1].text
    assert 'überschritten' in annotated.layout.annotations[2].text
    assert '80,0' in annotated.layout.annotations[2].text
    assert annotated.layout.annotations[3].text == 'Budget erreicht'
    assert annotated.layout.shapes[4].y0 == 180
    assert [a.y for a in annotated.layout.annotations[1:]] == [320, 400, 320]
    assert all(not a.showarrow and a.yanchor == 'bottom' and a.yshift > 0
               for a in annotated.layout.annotations[1:])


def test_chart_forwards_options(monkeypatch):
    import pexl.reporting
    data = report('gwp')
    monkeypatch.setattr(pexl.reporting, 'materialize', lambda *args: data)
    assert chart(None, 'gwp_ee', annotate=True, budget=320).to_json() == render(data, annotate=True, budget=320).to_json()


def test_invalid_budget_is_explicit():
    with pytest.raises(ValueError, match='two-column'):
        render(report(), budget=320)
    with pytest.raises(ValueError, match='finite'):
        render(report('gwp'), budget=float('nan'))
