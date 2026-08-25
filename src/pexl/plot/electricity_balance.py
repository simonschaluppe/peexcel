from __future__ import annotations

from collections.abc import Sequence

import pandas as pd
import plotly.graph_objects as go

from pexl.plot.styles import color_for



VAR_LABELS = {
    "E_plug": "Nutzer*innenstrom",
    "Eaux": "Allgemeinstrom",
    "Elight": "Beleuchtung",
    "E_plugAuxLight": "Nutzer- und Allgemeinstrom",
    
    "E_plug": "Nutzer*innenstrom",
    "Ev_min": "Lüften",

    "Eh_min": "Heizen Mindestbedarf",
    "Eh_flex_1el_final": "Heizen Flex 1",
    "Eh_flex_3el_final": "Heizen Flex 3",

    "Ec_min": "Kühlen Mindestbedarf",
    "Ec_flex_1el_final": "Kühlen Flex 1",
    "Ec_flex_3el_final": "Kühlen Flex 3",

    "Edhw_min": "Warmwasser Mindestbedarf",
    "Edhw1_flex_final": "Warmwasser Flex 1",
    "Edhw2_flex_final": "Warmwasser Flex 2",

    "Eev_min": "E-Cars",

    "PV_to_user": "PV Direktdeckung Nutzer",
    "PV_total_direct_use": "PV Direktdeckung HKLS",
    "PV_total_flex_use": "flexible Nutzung von PV-Üerschüssen",
    "PV_to_Egrid": "PV Netzeinspeisung",
    "Batt_to_user": "Batterie",
    "Batt_to_HVAC_min": "Batterie",
    "Batt_to_Eev_min": "Batterie",
    "VRGrid_total_min_use": "Netzdienlicher Bezug",
    "Eev_to_user": "Vehicle-to-Building",
    "Eev_to_HVAC": "Vehicle-to-Building",
    "E_grid": "Netzbezug",
}


def electricity_balance(
    data: pd.DataFrame,
    *,
    positive: Sequence[str],
    negative: Sequence[str],
    x: str | None = None,
    title: str | None = None,
    x_title: str | None = None,
    y_title: str | None = None,
    labels: dict[str, str] | None = None,
    colors: dict[str, str] | None = None,
    omit_empty: bool = False
) -> go.Figure:
    """
    Plot a stacked positive/negative electricity balance.

    The dataframe must already contain the desired temporal aggregation.
    The function performs no grouping, resampling or unit conversion.

    Parameters
    ----------
    data:
        Prepared dataframe.

    positive:
        var_names plotted above zero.

    negative:
        var_names plotted below zero.

    x:
        Column used for the x-axis. If None, use the dataframe index.

    title:
        Figure title.

    x_title, y_title:
        Axis titles.

    labels:
        Optional display-label overrides keyed by var_name.

    colors:
        Optional color overrides keyed by var_name.
    """
    positive = list(positive)
    negative = list(negative)

    _require_columns(data, positive + negative)

    if x is None:
        x_values = data.index
    else:
        _require_columns(data, [x])
        x_values = data[x]

    label_map = VAR_LABELS | (labels or {})
    color_overrides = colors or {}  

    fig = go.Figure()

    for var_name in positive:
        if omit_empty:
            values = data[var_name].abs()

            if values.fillna(0).eq(0).all():
                continue

        _add_balance_bar(
            fig,
            x=x_values,
            values=data[var_name].abs(),
            var_name=var_name,
            label=label_map.get(var_name, var_name),
            color=color_overrides.get(
                var_name,
                color_for(var_name),
            ),
        )

    for var_name in negative:
        if omit_empty:
            values = data[var_name].abs()
            if values.fillna(0).eq(0).all():
                continue

        _add_balance_bar(
            fig,
            x=x_values,
            values=-data[var_name].abs(),
            var_name=var_name,
            label=label_map.get(var_name, var_name),
            color=color_overrides.get(
                var_name,
                color_for(var_name),
            ),
        )

    fig.add_hline(
        y=0,
        line_width=1,
    )

    fig.update_layout(
        title=title,
        barmode="relative",
        xaxis_title=x_title,
        yaxis_title=y_title,
        legend_title=None,
        hovermode="x unified",
    )

    return fig


def _add_balance_bar(
    fig: go.Figure,
    *,
    x,
    values: pd.Series,
    var_name: str,
    label: str,
    color: str | None,
) -> None:
    kwargs = {}
    if color is not None:
        kwargs["marker_color"] = color
    fig.add_bar(
        x=x,
        y=values,
        name=label,
        legendgroup=var_name,
        customdata=values.abs(),
        hovertemplate=(
            f"{label}: %{{customdata:.2f}}"
            "<extra></extra>"
        ),
        **kwargs
    )



def _require_columns(
    data: pd.DataFrame,
    columns: Sequence[str],
) -> None:
    missing = [
        column
        for column in columns
        if column not in data.columns
    ]

    if missing:
        raise KeyError(
            f"Missing electricity balance columns: {missing}"
        )

    from collections.abc import Sequence

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def electricity_balance_facets(
    data: pd.DataFrame,
    *,
    positive: Sequence[str],
    negative: Sequence[str],
    facet: str,
    facet_order: Sequence[str] | None = None,
    facet_labels: dict[str, str] | None = None,
    x: str | None = None,
    title: str | None = None,
    x_title: str | None = None,
    y_title: str | None = None,
    labels: dict[str, str] | None = None,
    colors: dict[str, str] | None = None,
    omit_empty: bool = False
) -> go.Figure:

    facets = (
        list(facet_order)
        if facet_order is not None
        else list(data[facet].drop_duplicates())
    )

    facet_labels = facet_labels or {}

    fig = make_subplots(
        rows=1,
        cols=len(facets),
        shared_yaxes=True,
        subplot_titles=[
            facet_labels.get(value, value)
            for value in facets
        ],
        horizontal_spacing=0.02,
    )

    shown_legend = set()
    for col, facet_value in enumerate(facets, start=1):
        subset = data.loc[data[facet] == facet_value]

        part = electricity_balance(
            subset,
            x=x,
            positive=positive,
            negative=negative,
            labels=labels,
            colors=colors,
            omit_empty=omit_empty
        )

        for trace in part.data:
            trace.showlegend = trace.name not in shown_legend

            if trace.showlegend:
                shown_legend.add(trace.name)

            fig.add_trace(trace, row=1, col=col)

        fig.add_hline(
            y=0,
            row=1,
            col=col,
            line_width=1,
        )

    fig.update_layout(
        title=title,
        barmode="relative",
        legend_title=None,
        hovermode="x unified",
    )

    fig.update_xaxes(title_text=x_title)
    fig.update_yaxes(title_text=y_title, col=1)

    return fig