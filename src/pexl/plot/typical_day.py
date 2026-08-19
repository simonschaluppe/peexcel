from __future__ import annotations

import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from pexl.i18n import Language, LocalizedText
from .utils import normalize_data


BALANCE_LABEL = LocalizedText(de="Saldo", en="Balance")
HOUR_LABEL = LocalizedText(de="Stunde", en="Hour")
SEASON_TITLE = LocalizedText(
    de="Stündliche Verteilung nach Jahreszeit",
    en="Hourly distribution by season",
)

SEASONS = (
    (LocalizedText(de="Winter", en="Winter"), (12, 1, 2)),
    (LocalizedText(de="Frühling", en="Spring"), (3, 4, 5)),
    (LocalizedText(de="Sommer", en="Summer"), (6, 7, 8)),
    (LocalizedText(de="Herbst", en="Autumn"), (9, 10, 11)),
)


def _numeric_frame(data) -> pd.DataFrame:
    """Normalize supported input types and convert values to numeric."""
    df = normalize_data(data).copy()

    for column in df.columns:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

    return df


def _prepare_balance(
    positive,
    negative,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series]:
    """Prepare positive, negative and resulting balance series."""

    positive = _numeric_frame(positive).abs()
    negative = -_numeric_frame(negative).abs()

    positive, negative = positive.align(
        negative,
        join="inner",
        axis=0,
    )

    balance = (
        positive.sum(axis=1)
        + negative.sum(axis=1)
    )

    balance.name = "balance"

    return positive, negative, balance


def typical_day_balance(
    positive,
    negative,
    *,
    day: str | pd.Timestamp,
    language: Language = "de",
    title: str | None = None,
    ylabel: str | None = None,
) -> go.Figure:
    """
    Plot positive flows, negative flows and their balance for one day.

    positive / negative can be Series, DataFrames, mappings, etc.
    """

    positive, negative, balance = _prepare_balance(
        positive,
        negative,
    )

    if not isinstance(balance.index, pd.DatetimeIndex):
        raise TypeError("Data must have a DatetimeIndex.")

    day = pd.Timestamp(day).normalize()

    mask = (
        (balance.index >= day)
        & (balance.index < day + pd.Timedelta(days=1))
    )

    positive = positive.loc[mask]
    negative = negative.loc[mask]
    balance = balance.loc[mask]

    if balance.empty:
        raise ValueError(
            f"No timeseries data found for {day.date()}"
        )

    hours = balance.index.hour

    fig = go.Figure()

    for column in positive.columns:
        fig.add_bar(
            x=hours,
            y=positive[column],
            name=str(column),
        )

    for column in negative.columns:
        fig.add_bar(
            x=hours,
            y=negative[column],
            name=str(column),
        )

    fig.add_scatter(
        x=hours,
        y=balance,
        name=BALANCE_LABEL.get(language),
        mode="lines+markers",
        line={"width": 2},
        marker={"size": 5},
    )

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
        xaxis_title=HOUR_LABEL.get(language),
        yaxis_title=ylabel,
        legend={
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "left",
            "x": 0,
        },
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

def seasonal_hourly_boxplot(
    data,
    *,
    language: Language = "de",
    title: str | None = None,
    ylabel: str | None = None,
    shade_sign: bool = True,
) -> go.Figure:
    """
    Show the hourly distribution of one time series by season.

    Each box contains all values occurring at the respective hour
    during that season.
    """

    df = _numeric_frame(data)

    if df.shape[1] != 1:
        raise ValueError(
            "seasonal_hourly_boxplot requires exactly one series."
        )

    series = df.iloc[:, 0].dropna()

    if not isinstance(series.index, pd.DatetimeIndex):
        raise TypeError("Data must have a DatetimeIndex.")

    data = pd.DataFrame(
        {
            "value": series,
            "hour": series.index.hour,
            "month": series.index.month,
        },
        index=series.index,
    )

    fig = make_subplots(
        rows=1,
        cols=4,
        shared_yaxes=True,
        subplot_titles=[
            label.get(language)
            for label, _ in SEASONS
        ],
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
                y=season_data["value"],
                name=season.get(language),
                boxpoints=False,
                showlegend=False,
                width=0.8,
                line={"width": 0.5},
            ),
            row=1,
            col=col,
        )

        fig.update_xaxes(
            title_text=HOUR_LABEL.get(language),
            tickmode="array",
            tickvals=list(range(24)),
            ticktext=list(range(24)),
            row=1,
            col=col,
        )

    # Shared limits for the background regions.
    ymin = min(series.min(), 0)
    ymax = max(series.max(), 0)

    for col in range(1, 5):

        if shade_sign:
            if ymax > 0:
                fig.add_hrect(
                    y0=0,
                    y1=ymax,
                    fillcolor="lightgreen",
                    opacity=0.12,
                    line_width=0,
                    layer="below",
                    row=1,
                    col=col,
                )

            if ymin < 0:
                fig.add_hrect(
                    y0=ymin,
                    y1=0,
                    fillcolor="lightcoral",
                    opacity=0.12,
                    line_width=0,
                    layer="below",
                    row=1,
                    col=col,
                )

        fig.add_hline(
            y=0,
            line_color="red",
            line_width=1.2,
            row=1,
            col=col,
        )

    fig.update_yaxes(
        title_text=ylabel,
        row=1,
        col=1,
    )

    fig.update_layout(
        title=title or SEASON_TITLE.get(language),
        template="plotly_white",
        boxgap=0.1,
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