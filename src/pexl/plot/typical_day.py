from __future__ import annotations

from collections.abc import Sequence

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from pexl.i18n import Language, LocalizedText
from pexl.schema.current import (
    TIMESERIES_ATTR_NAME_MAP,
    TIMESERIES_META,
    TimeseriesMeta,
)


TimeseriesRef = str | TimeseriesMeta


BALANCE_LABEL = LocalizedText(
    de="Saldo",
    en="Balance",
)

HOUR_LABEL = LocalizedText(
    de="Stunde",
    en="Hour",
)

ENERGY_LABEL = LocalizedText(
    de="Energie",
    en="Energy",
)

SEASON_TITLE = LocalizedText(
    de="Stündliche Verteilung nach Jahreszeit",
    en="Hourly distribution by season",
)

SEASONS = (
    (
        LocalizedText(de="Winter", en="Winter"),
        (12, 1, 2),
    ),
    (
        LocalizedText(de="Frühling", en="Spring"),
        (3, 4, 5),
    ),
    (
        LocalizedText(de="Sommer", en="Summer"),
        (6, 7, 8),
    ),
    (
        LocalizedText(de="Herbst", en="Autumn"),
        (9, 10, 11),
    ),
)


def _resolve_meta(variable: TimeseriesRef) -> TimeseriesMeta:
    """Resolve var_name, attr_name or TimeseriesMeta."""

    if isinstance(variable, TimeseriesMeta):
        return variable

    if variable in TIMESERIES_ATTR_NAME_MAP:
        attr_name = TIMESERIES_ATTR_NAME_MAP[variable]

    elif variable in TIMESERIES_ATTR_NAME_MAP.values():
        attr_name = variable

    else:
        raise KeyError(f"Unknown timeseries variable: {variable!r}")

    return getattr(TIMESERIES_META, attr_name)


def _variable_label(
    variable: TimeseriesMeta,
    language: Language,
) -> str:
    """
    German: public label_de.
    English: canonical var_name.
    """

    if language == "de":
        return variable.attr_name or variable.var_name

    return variable.var_name


def _resolve_variables(
    variables: Sequence[TimeseriesRef],
) -> tuple[TimeseriesMeta, ...]:

    return tuple(
        _resolve_meta(variable)
        for variable in variables
    )


def _common_unit(
    variables: Sequence[TimeseriesMeta],
) -> str:

    units = {
        variable.unit
        for variable in variables
        if variable.unit
    }

    if len(units) == 1:
        return units.pop()

    return ""


def _prepare_balance(
    df: pd.DataFrame,
    *,
    positive: Sequence[TimeseriesRef],
    negative: Sequence[TimeseriesRef],
) -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.Series,
    tuple[TimeseriesMeta, ...],
    tuple[TimeseriesMeta, ...],
]:
    """Prepare positive, negative and balance series."""

    positive_meta = _resolve_variables(positive)
    negative_meta = _resolve_variables(negative)

    positive_names = [
        meta.var_name
        for meta in positive_meta
    ]

    negative_names = [
        meta.var_name
        for meta in negative_meta
    ]

    missing = [
        name
        for name in positive_names + negative_names
        if name not in df.columns
    ]

    if missing:
        raise KeyError(
            f"Timeseries columns missing from DataFrame: {missing}"
        )

    positive_plot = df[positive_names].abs()

    negative_plot = -df[negative_names].abs()

    balance = (
        positive_plot.sum(axis=1)
        + negative_plot.sum(axis=1)
    )

    return (
        positive_plot,
        negative_plot,
        balance,
        positive_meta,
        negative_meta,
    )


def typical_day_balance(
    df: pd.DataFrame,
    *,
    positive: Sequence[TimeseriesRef],
    negative: Sequence[TimeseriesRef],
    day: str | pd.Timestamp,
    language: Language = "de",
    title: str | None = None,
) -> go.Figure:
    """Plot production, demand and balance for one day."""

    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError(
            "DataFrame index must be a DatetimeIndex."
        )

    day = pd.Timestamp(day).normalize()

    data = df.loc[
        (df.index >= day)
        & (df.index < day + pd.Timedelta(days=1))
    ]

    if data.empty:
        raise ValueError(
            f"No timeseries data found for {day.date()}"
        )

    (
        positive_plot,
        negative_plot,
        balance,
        positive_meta,
        negative_meta,
    ) = _prepare_balance(
        data,
        positive=positive,
        negative=negative,
    )

    fig = go.Figure()

    # Use hour 0–23 instead of full timestamps.
    hours = data.index.hour

    for meta in positive_meta:
        fig.add_bar(
            x=hours,
            y=positive_plot[meta.var_name],
            name=_variable_label(meta, language),
            hovertemplate=(
                "%{x}:00<br>"
                "%{y:.2f}"
                "<extra>%{fullData.name}</extra>"
            ),
        )

    for meta in negative_meta:
        fig.add_bar(
            x=hours,
            y=negative_plot[meta.var_name],
            name=_variable_label(meta, language),
            hovertemplate=(
                "%{x}:00<br>"
                "%{y:.2f}"
                "<extra>%{fullData.name}</extra>"
            ),
        )

    fig.add_scatter(
        x=hours,
        y=balance,
        name=BALANCE_LABEL.get(language),
        mode="lines+markers",
        line={"width": 2},
        marker={"size": 5},
        hovertemplate=(
            "%{x}:00<br>"
            "%{y:.2f}"
            "<extra>%{fullData.name}</extra>"
        ),
    )

    unit = _common_unit(
        positive_meta + negative_meta
    )

    y_title = ENERGY_LABEL.get(language)

    if unit:
        y_title += f" [{unit}]"

    fig.add_hline(
        y=0,
        line_width=1,
    )

    fig.update_layout(
        title=title or str(day.date()),
        template="plotly_white",
        barmode="relative",
        bargap=0.08,
        hovermode="x unified",
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "left",
            "x": 0,
        },
        xaxis_title=HOUR_LABEL.get(language),
        yaxis_title=y_title,
    )

    fig.update_xaxes(
        tickmode="array",
        tickvals=list(range(24)),
        ticktext=[
            f"{hour:02d}"
            for hour in range(24)
        ],
        range=[-0.5, 23.5],
    )

    return fig


def seasonal_hourly_balance_boxplot(
    df: pd.DataFrame,
    *,
    positive: Sequence[TimeseriesRef],
    negative: Sequence[TimeseriesRef],
    language: Language = "de",
    title: str | None = None,
) -> go.Figure:
    """
    Plot hourly balance distributions for each season.

    Each box represents the distribution of the balance at one
    hour of day across all days in the respective season.
    """

    if not isinstance(df.index, pd.DatetimeIndex):
        raise TypeError(
            "DataFrame index must be a DatetimeIndex."
        )

    (
        _,
        _,
        balance,
        positive_meta,
        negative_meta,
    ) = _prepare_balance(
        df,
        positive=positive,
        negative=negative,
    )

    data = pd.DataFrame(
        {
            "balance": balance,
            "hour": df.index.hour,
            "month": df.index.month,
        },
        index=df.index,
    )

    season_labels = [
        label.get(language)
        for label, _ in SEASONS
    ]

    fig = make_subplots(
        rows=1,
        cols=4,
        shared_yaxes=True,
        subplot_titles=season_labels,
        horizontal_spacing=0.035,
    )

    for col, (season, months) in enumerate(
        SEASONS,
        start=1,
    ):
        season_data = data[
            data["month"].isin(months)
        ]

        fig.add_trace(
            go.Box(
                x=season_data["hour"],
                y=season_data["balance"],
                name=season.get(language),
                boxpoints=False,
                showlegend=False,
                hovertemplate=(
                    f"{HOUR_LABEL.get(language)} "
                    "%{x}<br>"
                    "Median: %{median:.2f}<br>"
                    "Q1: %{q1:.2f}<br>"
                    "Q3: %{q3:.2f}"
                    "<extra></extra>"
                ),
            ),
            row=1,
            col=col,
        )

        fig.update_xaxes(
            title_text=HOUR_LABEL.get(language),
            tickmode="array",
            tickvals=list(range(24)),
            ticktext=[
                str(hour)
                for hour in range(24)
            ],
            row=1,
            col=col,
        )

    unit = _common_unit(
        positive_meta + negative_meta
    )

    y_title = BALANCE_LABEL.get(language)

    if unit:
        y_title += f" [{unit}]"

    fig.update_yaxes(
        title_text=y_title,
        row=1,
        col=1,
        zeroline=True,
        zerolinewidth=1,
    )

    fig.update_layout(
        title=title or SEASON_TITLE.get(language),
        template="plotly_white",
        height=450,
        width=1400,
        margin={
            "l": 70,
            "r": 30,
            "t": 90,
            "b": 60,
        },
    )

    return fig