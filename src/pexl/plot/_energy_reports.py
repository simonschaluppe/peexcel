"""Demand and supply stacks for annual energy balances."""
from textwrap import wrap

import plotly.graph_objects as go

from pexl.i18n import chart_text
from pexl.reporting.analysis import role_total

from ._report_helpers import _difference_bracket, _marker, _number, _series_for_role, _values


def energy_balance(report: dict, *, annotate: bool = False) -> go.Figure:
    """Render Bedarf and Deckung as paired stacked bars for each scenario."""
    fig = go.Figure()
    variants = report["frame"]["Variant"].tolist()

    groups = (
        ("Bedarf", _series_for_role(report, "Bedarf")),
        ("Deckung", _series_for_role(report, "Deckung")),
    )

    for group_name, series_list in groups:
        group_name = chart_text('demand' if group_name == 'Bedarf' else 'supply', report['language'])
        x = [variants, [group_name] * len(variants)]

        for series in series_list:
            values = _values(report, series, absolute=report.get("value_mode", "magnitude") == "magnitude")

            fig.add_trace(
                go.Bar(
                    name='<br>'.join(wrap(series["label"], width=38)),
                    x=x,
                    y=values,
                    meta={"var_name": series["var_name"], "role": series["role"]},
                    marker=_marker(series),
                    text=values,
                    texttemplate="<b>%{y:.1f}</b>",
                    textposition="inside",
                    insidetextanchor="middle",
                    legendgroup=group_name,
                    legendgrouptitle_text=group_name,
                    hovertemplate=(
                        f"<b>{series['label']}</b><br>"
                        f"{chart_text('value', report['language'])}: %{{y:.1f}}<extra></extra>"
                    ),
                )
            )

    fig.update_layout(
        barmode="relative" if report.get('value_mode') == 'signed' else "stack",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis_title=report.get("unit") or "",
        xaxis={
            "tickangle": 0,
            "dividerwidth": 2,
            "dividercolor": "gray",
            "showgrid": False,
        },
        yaxis={
            "gridcolor": "gray",
            "griddash": "dot",
        },
        autosize=True, margin={"t": 65, "l": 55, "r": 20, "b": 100},
    )

    if annotate:
        _annotate_pe(fig, report)
    return fig


def _annotate_pe(fig: go.Figure, report: dict) -> None:
    absolute = report.get("value_mode", "magnitude") == "magnitude"
    demand = role_total(report, "Bedarf", absolute=absolute).tolist()
    supply = role_total(report, "Deckung", absolute=absolute).tolist()
    if not demand:
        return
    scale = max(*demand, *supply, 1.0)
    for i, (needed, provided) in enumerate(zip(demand, supply)):
        delta = provided - needed
        color = "#237a45" if delta >= 0.05 else "#ba3030" if delta <= -0.05 else "#59636e"
        x = 2 * i + 0.5
        _difference_bracket(fig, x, needed, provided, color)
        fig.add_annotation(
            x=x, y=max(needed, provided) + 0.045 * scale, xref="x", yref="y",
            text=f"{chart_text('difference', report['language'])}<br><b>{_number(delta, signed=True, language=report['language'])}</b><br>{report.get('unit') or ''}",
            showarrow=False, yanchor="bottom", font={"color": color, "size": 12},
            bgcolor="rgba(255,255,255,0.9)", borderpad=3,
        )
    fig.update_yaxes(range=[min(0, *demand, *supply) - (0.05 * scale if min(*demand, *supply) < 0 else 0), scale * 1.38])
