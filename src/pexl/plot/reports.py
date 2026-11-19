"""Render materialized annual PEExcel reports as Plotly figures."""
from __future__ import annotations

import math

import plotly.graph_objects as go

from pexl.i18n import chart_text

from ._energy_reports import energy_balance
from ._gwp_reports import embodied_gwp, four_column_gwp, gwp_overview
from ._report_helpers import darken_color  # Historical import from this module.


# Report-wide presentation defaults. Chart-specific geometry lives with its drawer.
_DEFAULT_ANNOTATIONS = {"primary_energy_balance", "gwp_ee"}
_DEFAULT_LEGEND_POSITION = "below"
_LEGENDS = {
    "below": dict(orientation="h", x=0, xanchor="left", y=-0.18, yanchor="top"),
    "right": dict(orientation="v", x=1.02, xanchor="left", y=1, yanchor="top"),
}
_ENERGY = "stacked_bar_comparison"
_GWP = "build_gwp_chart"


def render(
    report: dict,
    *,
    annotate: bool | None = None,
    budget: float | None = None,
    language: str | None = None,
    legend_position: str | None = None,
) -> go.Figure:
    """Draw an annual report without modifying it.

    By default, primary energy labels displayed supply minus demand, and the
    GWP overview labels the distance from the lifecycle total to its budget.
    Set ``annotate=False`` to hide these per-variant labels and brackets.
    ``budget`` overrides the GWP overview reference in the report's unit.
    Set ``legend_position="right"`` to place the legend beside the chart.
    """
    language = language or report.get("language", "de")
    chart_text("value", language)
    report = {**report, "language": language}
    name = report.get("chart_name")
    chart_type = str(report.get("chart_type") or "").strip()
    annotate = name in _DEFAULT_ANNOTATIONS if annotate is None else annotate
    if legend_position is None:
        legend_position = _DEFAULT_LEGEND_POSITION

    if report.get("value_mode", "magnitude") not in ("magnitude", "signed"):
        raise ValueError("value_mode must be 'magnitude' or 'signed'")
    if legend_position not in _LEGENDS:
        raise ValueError("legend_position must be 'below' or 'right'")
    if budget is not None:
        if chart_type != _GWP:
            raise ValueError("budget is supported only by the GWP overview")
        if not math.isfinite(budget):
            raise ValueError("budget must be finite")

    if not report.get("series"):
        fig = _empty_chart(f"Keine Serien für Diagramm '{name}'.")
    elif chart_type == _ENERGY:
        fig = energy_balance(report, annotate=annotate and name == "primary_energy_balance")
    elif chart_type == _GWP:
        fig = gwp_overview(report, budget=budget, annotate=annotate)
    elif chart_type == "build_four_column_gwp_chart":
        fig = four_column_gwp(report)
    elif chart_type == "embodied_gwp":
        fig = embodied_gwp(report)
    elif chart_type == "build_multi_grid_chart":
        fig = _empty_chart("Multi-grid rendering is not implemented yet.")
    else:
        raise ValueError(f"Unsupported Plotly chart type {chart_type!r} for chart {name!r}")

    fig.update_layout(
        title=report.get("title") or name,
        legend=_LEGENDS[legend_position],
        margin_autoexpand=True,
        separators=",." if language == "de" else ".,",
    )
    return fig


def chart(
    data,
    chart_name: str,
    *,
    annotate: bool | None = None,
    budget: float | None = None,
    language="de",
    unit=None,
    legend_position: str | None = None,
) -> go.Figure:
    """Materialize and render a chart."""
    from pexl.reporting import materialize

    report = materialize(
        data, chart_name, language=language, unit=unit
    )
    return render(
        report,
        annotate=annotate,
        budget=budget,
        legend_position=legend_position,
    )


def _empty_chart(message: str) -> go.Figure:
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
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        xaxis={"visible": False},
        yaxis={"visible": False},
    )
    return fig


# Historical adapters also used through pexl.plot.plotly.
def _role_total(report: dict, role: str, *, absolute: bool = False) -> list[float]:
    from pexl.reporting.analysis import role_total

    return role_total(report, role, absolute=absolute).tolist()


def _scenario_plot_frame(view, names):
    from pexl.reporting import variables
    from pexl.reporting._data import display_names
    data = variables(view, *dict.fromkeys(n for n in names if n))
    frame = data["frame"]
    frame["column_name"] = display_names(frame)
    return frame.reset_index(drop=True), data["labels"]


def scenario_scatter(view, x, y, *, color=None, symbol=None, size=None, hover_data=()):
    """Compatibility entry point; prepare labels then call plot.scatter."""
    from .scenarios import scatter
    frame, labels = _scenario_plot_frame(view, [x, y, color, symbol, size, *hover_data])
    return scatter(frame, x, y, color=color, symbol=symbol, size=size,
                   hover_name="column_name", hover_data=hover_data, labels=labels)


def scenario_distribution(view, variable, *, by, color=None, kind='box'):
    """Compatibility entry point for schema-labelled box and violin plots."""
    from .scenarios import distribution
    frame, labels = _scenario_plot_frame(view, [variable, by, color])
    return distribution(frame, variable, by=by, color=color, kind=kind,
                        hover_name="column_name", labels=labels)


def report_balance_scatter(view, chart_name, x, *, color=None):
    """Compatibility entry point using the shared reporting balance calculation."""
    from pexl.reporting import balance
    from pexl.reporting._data import display_names
    from .scenarios import scatter
    data = balance(view, chart_name, include=tuple(n for n in (x, color) if n))
    # Preserve the historical column name used by the static browser generator.
    data["frame"] = data["frame"].rename(columns={"balance": "report_balance"})
    data["labels"]["report_balance"] = data["labels"].pop("balance")
    data["frame"]["column_name"] = display_names(data["frame"])
    return scatter(**data, x=x, y="report_balance", color=color, hover_name="column_name")
