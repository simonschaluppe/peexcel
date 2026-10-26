from __future__ import annotations

import math

import pandas as pd
import plotly.graph_objects as go


_GWP_AXIS = (
    "Kumulierte THG-Emissionen 2025 - 2075<br>"
    "[kg<sub>CO2eq</sub>/m<sup>2</sup><sub>BGF</sub>]"
)

_GWP_BANDS = (
    {"name": "L3", "y0": 195, "y1": 320, "color": "#CFDCE0"},
    {"name": "L2", "y0": 70, "y1": 195, "color": "#93B9C6"},
    {"name": "L1", "y0": 0, "y1": 70, "color": "#73A8BB"},
)


def darken_color(hex_color: str, factor: float = 0.7) -> str:
    """Return a darker hex color for Plotly pattern foregrounds."""
    value = (hex_color or "").strip().lstrip("#")

    if len(value) == 3:
        value = "".join(c * 2 for c in value)

    if len(value) != 6:
        return "#000000"

    try:
        r, g, b = (int(value[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return "#000000"

    r, g, b = (max(0, int(v * factor)) for v in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def _scenario_plot_frame(view, names):
    from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META
    names = list(dict.fromkeys(n for n in names if n))
    frame = view.select(*names).to_frame().reset_index()
    labels = {n: f"{getattr(SCHEMA_META, ATTR_NAME_MAP[n]).label_de or n} "
                 f"[{getattr(SCHEMA_META, ATTR_NAME_MAP[n]).unit or '-'}]" for n in names}
    labels['column_name'] = 'Szenario'
    return frame, labels


def scenario_scatter(view, x, y, *, color=None, symbol=None, size=None, hover_data=()):
    """Scatter of stored scenario values with schema-derived labels and units."""
    import plotly.express as px
    frame, labels = _scenario_plot_frame(view, [x, y, color, symbol, size, *hover_data])
    return px.scatter(frame, x=x, y=y, color=color, symbol=symbol, size=size,
                      hover_name='column_name', hover_data=list(hover_data), labels=labels)


def scenario_distribution(view, variable, *, by, color=None, kind='box'):
    """Unweighted distribution of simulated variants (not a stock estimate)."""
    import plotly.express as px
    if kind not in ('box', 'violin'):
        raise ValueError("kind must be 'box' or 'violin'")
    frame, labels = _scenario_plot_frame(view, [variable, by, color])
    return getattr(px, kind)(frame, x=by, y=variable, color=color, labels=labels,
                             hover_name='column_name', points=False)


def report_balance_scatter(view, chart_name, x, *, color=None):
    """Scatter the displayed Deckung-minus-Bedarf balance of an existing report.

    This uses the same absolute series totals as the paired-bar renderer. It is
    a report balance, not an additional simulated energy-flow variable.
    """
    import plotly.express as px
    from pexl import reporting
    report = reporting.materialize(view, chart_name)
    if report['chart_type'] != 'stacked_bar_comparison':
        raise ValueError('Balance scatter requires a Bedarf/Deckung report')
    frame, labels = _scenario_plot_frame(view, [x, color])
    frame['report_balance'] = [s-d for s, d in zip(
        _role_total(report, 'Deckung', absolute=True),
        _role_total(report, 'Bedarf', absolute=True))]
    labels['report_balance'] = f"{report['title']}: Deckung − Bedarf [{report.get('unit') or '-'}]"
    return px.scatter(frame, x=x, y='report_balance', color=color,
                      hover_name='column_name', labels=labels)


def _marker(series: dict, *, replace_pattern: bool = False) -> dict:
    """Build a Plotly marker dictionary from materialized series metadata."""
    color = series.get("color") or "#cccccc"
    pattern = series.get("pattern") or ""
    marker = {"color": color}

    if color.lower() == "#ffffff":
        marker["line"] = {"color": "gray", "width": 1}

    if pattern:
        marker["pattern"] = {
            "shape": pattern,
            "fgcolor": darken_color(color),
            "bgcolor": color,
            **({"fillmode": "replace"} if replace_pattern else {}),
        }

    return marker


def _role(series: dict) -> str:
    """Return the normalized semantic role of a materialized series."""
    return str(series.get("role") or "").strip().casefold()


def _series_for_role(report: dict, role: str) -> list[dict]:
    """Return report series matching one semantic chart role."""
    role = role.strip().casefold()
    return [series for series in report["series"] if _role(series) == role]


def _values(report: dict, series: dict, *, absolute: bool = False) -> list[float]:
    """Return numeric values for one materialized report series."""
    values = pd.to_numeric(
        report["frame"][series["var_name"]],
        errors="coerce",
    ).fillna(0.0)

    if absolute:
        values = values.abs()

    return values.tolist()


def _empty_chart(report: dict, message: str) -> go.Figure:
    """Return an empty Plotly figure with an explanatory annotation."""
    fig = go.Figure()
    fig.add_annotation(
        text=message,
        x=0.5,
        y=0.5,
        xref="paper",
        yref="paper",
        showarrow=False,
    )
    fig.update_layout(
        title=report.get("title") or report.get("chart_name"),
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis={"visible": False},
        yaxis={"visible": False},
    )
    return fig


def render(report: dict, *, annotate: bool = False, budget: float | None = None) -> go.Figure:
    """Render one materialized PEExcel report as a Plotly figure.

    Supported chart types are the canonical values generated by the active
    PEExcel reporting schema.

    ``annotate`` labels the displayed Deckung-minus-Bedarf difference in PE
    charts (not the separately exported PEI_balance). In a two-column GWP
    chart, ``budget`` adds a reference line in the report's unit; ``annotate``
    additionally labels its distance to the existing balance series. Overlays
    always describe the full report, even when legend entries are hidden.
    Defaults preserve the existing figures. No assessment values are changed.
    """
    chart_type = str(report.get("chart_type") or "").strip()
    if budget is not None:
        if chart_type != "build_gwp_chart":
            raise ValueError("budget is supported only for two-column GWP charts")
        if not math.isfinite(budget):
            raise ValueError("budget must be finite")

    if not report.get("series"):
        return _empty_chart(
            report,
            f"Keine Serien für Diagramm '{report.get('chart_name')}'.",
        )

    if chart_type == "stacked_bar_comparison":
        fig = _stacked_bar_comparison(report)
        if annotate and report.get("chart_name") == "primary_energy_balance":
            _annotate_pe(fig, report)
        return fig

    if chart_type == "build_gwp_chart":
        fig = _gwp(report)
        if budget is not None:
            _annotate_gwp_budget(fig, report, budget, annotate=annotate)
        return fig

    if chart_type == "build_four_column_gwp_chart":
        return _gwp_four_column(report)

    if chart_type == "build_multi_grid_chart":
        return _multi_grid(report)

    raise ValueError(
        f"Unsupported Plotly chart type {chart_type!r} "
        f"for chart {report.get('chart_name')!r}"
    )


def _number(value: float, *, signed: bool = False) -> str:
    # Avoid a misleading negative zero in rounded labels.
    value = 0.0 if abs(value) < 0.05 else value
    return format(value, "+.1f" if signed else ".1f").replace(".", ",")


def _role_total(report: dict, role: str, *, absolute: bool = False) -> list[float]:
    totals = [0.0] * len(report["frame"])
    for series in _series_for_role(report, role):
        totals = [a + b for a, b in zip(totals, _values(report, series, absolute=absolute))]
    return totals


def _difference_bracket(fig: go.Figure, x: float, start: float, end: float, color: str) -> None:
    """Draw a difference at a numeric position on the multicategory axis."""
    for x0, x1, y0, y1 in (
        (x, x, start, end),
        (x - 0.12, x + 0.12, start, start),
        (x - 0.12, x + 0.12, end, end),
    ):
        fig.add_shape(type="line", xref="x", yref="y", x0=x0, x1=x1,
                      y0=y0, y1=y1, line={"color": color, "width": 2.5})


def _annotate_pe(fig: go.Figure, report: dict) -> None:
    demand = _role_total(report, "Bedarf", absolute=True)
    supply = _role_total(report, "Deckung", absolute=True)
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
            text=f"Deckung − Bedarf<br><b>{_number(delta, signed=True)}</b><br>{report.get('unit') or ''}",
            showarrow=False, yanchor="bottom", font={"color": color, "size": 12},
            bgcolor="rgba(255,255,255,0.9)", borderpad=3,
        )
    fig.update_yaxes(range=[0, scale * 1.38])


def _annotate_gwp_budget(fig: go.Figure, report: dict, budget: float, *, annotate: bool) -> None:
    unit = report.get("unit") or "kg CO₂e/m² BGF"
    fig.add_hline(y=budget, line_color="#ba3030", line_width=2, line_dash="dash")
    fig.add_annotation(
        x=1, xref="paper", y=budget, yref="y", xanchor="right", yanchor="top", yshift=-6,
        text=f"<b>Referenzbudget: {_number(budget)} {unit}</b>",
        showarrow=False, font={"color": "#ba3030", "size": 12},
        bgcolor="rgba(255,255,255,0.95)", borderpad=3,
    )
    if not annotate:
        return
    for series in _series_for_role(report, "Balance Variable"):
        for i, total in enumerate(_values(report, series)):
            remaining = budget - total
            color = "#237a45" if remaining >= 0.05 else "#ba3030" if remaining <= -0.05 else "#59636e"
            status = "unterschritten um" if remaining >= 0.05 else "überschritten um" if remaining <= -0.05 else "erreicht"
            distance = f"{_number(abs(remaining))} {unit}" if abs(remaining) >= 0.05 else ""
            x = 2 * i + 0.5
            _difference_bracket(fig, x, total, budget, color)
            fig.add_annotation(
                x=x, y=max(total, budget), xref="x", yref="y", yshift=8, yanchor="bottom",
                text=f"Budget {status}<br><b>{distance}</b>" if distance else "Budget erreicht",
                showarrow=False,
                font={"color": color, "size": 11}, bgcolor="rgba(255,255,255,0.95)", borderpad=3,
            )


def _stacked_bar_comparison(report: dict) -> go.Figure:
    """Render Bedarf and Deckung as paired stacked bars for each scenario."""
    fig = go.Figure()
    variants = report["frame"]["Variant"].tolist()

    groups = (
        ("Bedarf", _series_for_role(report, "Bedarf")),
        ("Deckung", _series_for_role(report, "Deckung")),
    )

    for group_name, series_list in groups:
        x = [variants, [group_name] * len(variants)]

        for series in series_list:
            values = _values(report, series, absolute=True)

            fig.add_trace(
                go.Bar(
                    name=series["label"],
                    x=x,
                    y=values,
                    marker=_marker(series),
                    text=values,
                    texttemplate="<b>%{y:.1f}</b>",
                    textposition="inside",
                    insidetextanchor="middle",
                    legendgroup=group_name,
                    legendgrouptitle_text=group_name,
                    hovertemplate=(
                        f"<b>{series['label']}</b><br>"
                        "Wert: %{y:.1f}<extra></extra>"
                    ),
                )
            )

    fig.update_layout(
        title=report["title"],
        barmode="stack",
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
        legend={
            "orientation": "v",
            "yanchor": "top",
            "y": 1,
            "xanchor": "left",
            "x": 1.02,
        },
        margin={"t": 50, "l": 50, "r": 150, "b": 50},
    )

    return fig


def _add_gwp_bands(fig: go.Figure, variants: list[str]) -> None:
    """Add the L1-L3 GWP reference bands used by the PEExcel charts."""
    if not variants:
        return

    for band in _GWP_BANDS:
        fig.add_hrect(
            y0=band["y0"],
            y1=band["y1"],
            fillcolor=band["color"],
            opacity=0.4,
            layer="below",
            line_width=0,
        )

        fig.add_trace(
            go.Bar(
                x=[[variants[0]], ["EE"]],
                y=[None],
                name=band["name"],
                marker={"color": band["color"]},
                showlegend=True,
            )
        )


def _gwp(report: dict) -> go.Figure:
    """Render the two-column embodied/operational GWP chart."""
    fig = go.Figure()
    variants = report["frame"]["Variant"].tolist()

    x_axis = [
        [variant for variant in variants for _ in (0, 1)],
        ["EE", "OE"] * len(variants),
    ]

    _add_gwp_bands(fig, variants)

    def add_group(role: str, is_oe: bool) -> None:
        for series in _series_for_role(report, role):
            values = []

            for value in _values(report, series):
                values.extend([0, value] if is_oe else [value, 0])

            fig.add_trace(
                go.Bar(
                    name=series["label"],
                    x=x_axis,
                    y=values,
                    marker=_marker(series, replace_pattern=True),
                    width=0.6,
                    hovertemplate=(
                        f"<b>{series['label']}</b><br>"
                        "Wert: %{y:.1f}<extra></extra>"
                    ),
                )
            )

    add_group("Baulich", False)
    add_group("Betrieblich", True)

    for series in _series_for_role(report, "Balance Variable"):
        values = _values(report, series)

        fig.add_trace(
            go.Scatter(
                name=series["label"],
                x=[variants, ["EE"] * len(variants)],
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
        title=report["title"],
        barmode="relative",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        legend={
            "orientation": "v",
            "yanchor": "top",
            "y": 1,
            "xanchor": "left",
            "x": 1.02,
        },
        yaxis={
            "title": report.get("unit") or _GWP_AXIS,
            "autorange": True,
            "gridcolor": "gray",
            "griddash": "dot",
            "zerolinecolor": "gray",
            "zerolinewidth": 2,
        },
        xaxis={
            "type": "multicategory",
            "tickangle": 0,
            "dividercolor": "gray",
            "dividerwidth": 2,
            "showgrid": False,
        },
        margin={"l": 50, "r": 150, "t": 50, "b": 50},
    )

    return fig


def _gwp_four_column(report: dict) -> go.Figure:
    """Render the four-column embodied/operational GWP breakdown."""
    fig = go.Figure()
    variants = report["frame"]["Variant"].tolist()

    labels = [
        "Baulich",
        "Baulich kompensation",
        "Betrieblich",
        "Betrieblich kompensation",
    ]

    x_axis = [
        [variant for variant in variants for _ in range(4)],
        labels * len(variants),
    ]

    _add_gwp_bands(fig, variants)

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
                        "Wert: %{y:.1f}<extra></extra>"
                    ),
                )
            )

    for series in _series_for_role(report, "Balance Variable"):
        values = _values(report, series)

        fig.add_trace(
            go.Scatter(
                name=series["label"],
                x=[variants, [labels[-1]] * len(variants)],
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
        title=report["title"],
        barmode="relative",
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        legend={
            "orientation": "v",
            "yanchor": "top",
            "y": 1,
            "xanchor": "left",
            "x": 1.02,
        },
        yaxis={
            "title": report.get("unit") or _GWP_AXIS,
            "autorange": True,
            "gridcolor": "gray",
            "griddash": "dot",
            "zerolinecolor": "gray",
            "zerolinewidth": 2,
        },
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


def _multi_grid(report: dict) -> go.Figure:
    """Render a placeholder until multi-grid report metadata is defined."""
    return _empty_chart(
        report,
        "Multi-grid rendering is not implemented yet.",
    )

def chart(data, chart_name: str, *, annotate: bool = False, budget: float | None = None) -> go.Figure:
    """Materialize a chart; optional overlays follow :func:`render`."""
    from pexl.reporting import materialize
    return render(materialize(data, chart_name), annotate=annotate, budget=budget)
