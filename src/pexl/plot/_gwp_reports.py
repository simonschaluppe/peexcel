"""Lifecycle and embodied greenhouse-gas figures."""
from textwrap import wrap

import plotly.graph_objects as go

from pexl.i18n import chart_text

from ._report_helpers import _difference_bracket, _marker, _number, _role, _series_for_role, _values


_GWP_AXIS = (
    "Kumulierte THG-Emissionen 2025 - 2075<br>"
    "[kg<sub>CO2eq</sub>/m<sup>2</sup><sub>BGF</sub>]"
)
_GWP_BANDS = (
    {"name": "ghg budget", "y0": 0, "y1": 320, "color": "#93B9C6"},
    {"name": "L2", "y0": 70, "y1": 195, "color": "#93B9C6"},
    {"name": "L1", "y0": 0, "y1": 70, "color": "#73A8BB"},
)


def gwp_overview(report: dict, *, budget: float | None, annotate: bool) -> go.Figure:
    """Draw one signed lifecycle stack and a net marker per variant."""
    fig = go.Figure()
    variants = report["frame"]["Variant"].tolist()
    language = report["language"]
    totals = []
    for series in report["series"]:
        values = _values(report, series)
        trace = dict(name=series["label"], x=variants, y=values,
                     meta={"var_name": series["var_name"], "role": series["role"]})
        if _role(series) == "balance variable":
            totals.append(values)
            fig.add_scatter(
                **trace, mode="markers+text",
                marker=dict(symbol="diamond", size=8, color=series.get("color") or "#3BACBE"),
                text=[_number(value, language=language) for value in values],
                textposition="middle right",
            )
        else:
            fig.add_bar(
                **trace, marker=_marker(series, replace_pattern=True), width=0.6,
                hovertemplate=f"<b>{series['label']}</b><br>"
                              f"{chart_text('value', language)}: %{{y:.1f}}<extra></extra>",
            )

    fig.update_layout(
        barmode="relative", plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
        yaxis=_gwp_axis(report), margin=dict(l=50, r=150, t=50, b=50),
        xaxis=dict(type="category", categoryorder="array", categoryarray=variants, showgrid=False),
    )
    budget = _GWP_BANDS[0]["y1"] if budget is None else budget
    _add_budget_reference(fig, report, budget)
    if annotate:
        for values in totals:
            _annotate_gwp_budget(fig, report, values, budget)
    return fig


def _gwp_axis(report):
    return dict(title=report.get("unit") or _GWP_AXIS, autorange=True,
                gridcolor="gray", griddash="dot", zerolinecolor="gray", zerolinewidth=2)


def _add_budget_reference(fig, report, budget):
    language = report["language"]
    unit = report.get("unit") or "kg CO₂e/m² BGF"
    for index, band in enumerate(_GWP_BANDS):
        fig.add_hrect(
            y0=band["y0"], y1=budget if index == 0 else band["y1"],
            fillcolor=band["color"], opacity=0.4, layer="below", line_width=0,
            name=chart_text(band["name"], language), showlegend=True,
            visible=True if index == 0 else "legendonly",
        )
    fig.add_hline(y=budget, line_color="#ba3030", line_width=2, line_dash="dash")
    fig.add_annotation(
        x=1, xref="paper", y=budget, yref="y", xanchor="right", yanchor="top", yshift=-6,
        text=f"<b>{chart_text('reference_budget', language)}: {_number(budget, language=language)} {unit}</b>",
        showarrow=False, font=dict(color="#ba3030", size=12),
        bgcolor="rgba(255,255,255,0.95)", borderpad=3,
    )


def _annotate_gwp_budget(fig, report, totals, budget):
    language = report["language"]
    unit = report.get("unit") or "kg CO₂e/m² BGF"
    for index, total in enumerate(totals):
        remaining = budget - total
        if remaining >= 0.05:
            status, color = "budget_below", "#237a45"
        elif remaining <= -0.05:
            status, color = "budget_above", "#ba3030"
        else:
            status, color = "budget_met", "#59636e"
        label = chart_text(status, language)
        if status != "budget_met":
            distance = _number(abs(remaining), language=language)
            label = f"{label}<br><b>{distance} {unit}</b>"

        _difference_bracket(fig, index, total, budget, color)
        fig.add_annotation(
            x=index, y=max(total, budget), xref="x", yref="y", yshift=8, yanchor="bottom",
            text=label, showarrow=False, font=dict(color=color, size=11),
            bgcolor="rgba(255,255,255,0.95)", borderpad=3,
        )


def embodied_gwp(report: dict) -> go.Figure:
    """Render supplied embodied-only contributions and an explicit net marker.

    No operational/mobility values, lifecycle benchmark bands or hidden totals
    are inferred. Negative biogenic values retain their sign.
    """
    fig = go.Figure()
    variants = report['frame']['Variant'].tolist()
    for series in report['series']:
        values = _values(report, series)
        common = dict(name='<br>'.join(wrap(series['label'], width=38)), x=variants,
                      y=values, meta={'var_name': series['var_name'], 'role': series['role']})
        if _role(series) == 'balance variable':
            fig.add_scatter(**common, mode='markers', marker=dict(symbol='diamond', size=10, color='#333333'))
        else:
            fig.add_bar(**common, marker=_marker(series),
                        hovertemplate=f"{series['label']}: %{{y:.2f}}<extra></extra>")
    fig.update_layout(yaxis_title=report.get('unit'),
                      barmode='relative', autosize=True,
                      margin=dict(l=65, r=20, t=70, b=120))
    return fig


def four_column_gwp(report: dict) -> go.Figure:
    """Render the four-column embodied/operational GWP breakdown."""
    fig = go.Figure()
    variants = report["frame"]["Variant"].tolist()

    labels = list(dict.fromkeys(s['role'] for s in report['series']
                               if _role(s) != 'balance variable'))
    if len(labels) != 4:
        raise ValueError('Four-column report requires exactly four explicit component roles')

    display_labels = [chart_text(role, report['language']) for role in labels]
    x_axis = [
        [variant for variant in variants for _ in range(4)],
        display_labels * len(variants),
    ]

    for column_index, role in enumerate(labels):
        for series in _series_for_role(report, role):
            values = []

            for value in _values(report, series):
                row = [0, 0, 0, 0]
                row[column_index] = value
                values.extend(row)

            fig.add_trace(
                go.Bar(
                    name=series["label"],
                    x=x_axis,
                    y=values,
                    marker=_marker(series, replace_pattern=True),
                    width=0.6,
                    hovertemplate=(
                        f"<b>{series['label']}</b><br>"
                        f"{chart_text('value', report['language'])}: %{{y:.1f}}<extra></extra>"
                    ),
                )
            )

    for series in _series_for_role(report, "Balance Variable"):
        values = _values(report, series)

        fig.add_trace(
            go.Scatter(
                name=series["label"],
                x=[variants, [display_labels[-1]] * len(variants)],
                y=values,
                mode="markers+text",
                marker={
                    "symbol": "diamond",
                    "color": series.get("color") or "#7B8E1D",
                    "size": 8,
                },
                text=[f"  {value:.1f}" for value in values],
                textposition="middle right",
            )
        )

    fig.update_layout(
        barmode="relative",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=_gwp_axis(report),
        xaxis={
            "type": "multicategory",
            "tickangle": 90,
            "dividercolor": "gray",
            "dividerwidth": 2,
            "showgrid": False,
        },
        margin={"l": 50, "r": 180, "t": 50, "b": 50},
    )

    return fig
