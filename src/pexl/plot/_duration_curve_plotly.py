from __future__ import annotations

import numpy as np
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

from pexl.i18n import Language, LocalizedText
from .utils import normalize_data


XLABEL = LocalizedText(
    de="Stunden",
    en="Hours",
)

DURATION_LABEL = LocalizedText(
    de="Dauer [%]",
    en="Duration [%]",
)

RANK_LABEL = LocalizedText(
    de="Rang",
    en="Rank",
)

TIME_LABEL = LocalizedText(
    de="Zeitpunkt",
    en="Time",
)

SEASONS = (
    (LocalizedText(de="❄️ Winter", en="❄️ Winter"), (12, 1, 2)),
    (LocalizedText(de="Frühling", en="Spring"), (3, 4, 5)),
    (LocalizedText(de="☀️ Sommer", en="☀️ Summer"), (6, 7, 8)),
    (LocalizedText(de="Herbst", en="Autumn"), (9, 10, 11)),
)


# Helpers ----------------------------------------------------------------------


def _sorted_series(series) -> pd.Series:
    """Return numeric values sorted from highest to lowest."""
    values = pd.to_numeric(
        series,
        errors="coerce",
    ).dropna()

    return values.sort_values(
        ascending=False
    )


def _duration_x(
    n: int,
    x: str,
) -> np.ndarray:
    """Create the duration-curve x axis."""

    if x == "hours":
        return np.arange(n)

    if x == "percent":
        return np.linspace(0, 100, n)

    raise ValueError("x must be 'hours' or 'percent'")


def _customdata(
    series: pd.Series,
) -> np.ndarray:
    """Return original source index for hover display."""

    if isinstance(series.index, pd.DatetimeIndex):
        return series.index.strftime(
            "%Y-%m-%d %H:%M"
        ).to_numpy()

    return series.index.astype(str).to_numpy()


def _hovertemplate(
    *,
    x: str,
    language: Language,
) -> str:
    """Create common duration-curve hover text."""

    x_label = (
        RANK_LABEL.get(language)
        if x == "hours"
        else DURATION_LABEL.get(language)
    )

    return (
        "%{fullData.name}<br>"
        f"{x_label}: %{{x:.0f}}"
        + (" h<br>" if x == "hours" else " %<br>")
        + "%{y:.2f}<br>"
        + f"{TIME_LABEL.get(language)}: %{{customdata}}"
        + "<extra></extra>"
    )


def _add_duration_trace(
    fig,
    series,
    *,
    name,
    x,
    color,
    language,
    row=None,
    col=None,
    showlegend=True,
):
    """Add one duration curve to a Plotly figure."""

    sorted_series = _sorted_series(series)

    if sorted_series.empty:
        return

    xx = _duration_x(
        len(sorted_series),
        x,
    )

    trace = go.Scatter(
        x=xx,
        y=sorted_series.to_numpy(),
        mode="lines",
        name=str(name),
        showlegend=showlegend,
        customdata=_customdata(sorted_series),
        line=(
            {"color": color}
            if color is not None
            else None
        ),
        hovertemplate=_hovertemplate(
            x=x,
            language=language,
        ),
    )

    if row is None:
        fig.add_trace(trace)
    else:
        fig.add_trace(
            trace,
            row=row,
            col=col,
        )


def _format_xaxis(
    fig,
    *,
    x,
    language,
    row=None,
    col=None,
):
    """Apply common x-axis formatting."""

    title = (
        XLABEL.get(language)
        if x == "hours"
        else DURATION_LABEL.get(language)
    )

    kwargs = {
        "title_text": title,
        "rangemode": "tozero",
    }

    if row is None:
        fig.update_xaxes(**kwargs)
    else:
        fig.update_xaxes(
            **kwargs,
            row=row,
            col=col,
        )


# Duration curve ---------------------------------------------------------------


def duration_curve_interactive(
    data,
    *,
    ylabel=None,
    title=None,
    x="hours",
    zero_line=True,
    legend=True,
    colors=None,
    language: Language = "de",
) -> go.Figure:
    """
    Plot interactive duration curves.

    Parameters
    ----------
    data : Series | DataFrame | Mapping | Sequence[Series]
        One or more time series.
    ylabel : str | None
        Complete y-axis label, including unit if desired.
    title : str | None
        Figure title.
    x : {"hours", "percent"}
        X-axis representation.
    zero_line : bool
        Draw horizontal zero line.
    legend : bool
        Show legend.
    colors : Mapping | None
        Optional mapping of series name -> color.
    language : {"de", "en"}
        Plot language.

    Returns
    -------
    plotly.graph_objects.Figure
    """
    data = normalize_data(data)

    if x not in {"hours", "percent"}:
        raise ValueError(
            "x must be 'hours' or 'percent'"
        )

    fig = go.Figure()

    for name, series in data.items():
        _add_duration_trace(
            fig,
            series,
            name=name,
            x=x,
            color=(
                colors.get(name)
                if colors
                else None
            ),
            language=language,
            showlegend=legend,
        )

    if zero_line:
        fig.add_hline(
            y=0,
            line_width=1,
            line_color="gray",
        )

    _format_xaxis(
        fig,
        x=x,
        language=language,
    )

    fig.update_layout(
        title=title,
        template="plotly_white",
        yaxis_title=ylabel,
        showlegend=legend,
        hovermode="closest",
    )

    return fig


# Seasonal duration curves -----------------------------------------------------


def seasonal_duration_curves_interactive(
    data,
    *,
    ylabel=None,
    title=None,
    x="hours",
    zero_line=True,
    legend=True,
    colors=None,
    language: Language = "de",
    height=450,
    width=1400,
) -> go.Figure:
    """
    Plot interactive seasonal duration curves side by side.

    Data must have a DatetimeIndex so that values can be assigned
    to winter, spring, summer and autumn.
    """
    data = normalize_data(data)

    if not isinstance(
        data.index,
        pd.DatetimeIndex,
    ):
        raise TypeError(
            "seasonal_duration_curves requires "
            "data with a DatetimeIndex"
        )

    if x not in {"hours", "percent"}:
        raise ValueError(
            "x must be 'hours' or 'percent'"
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

    for col, (_, months) in enumerate(
        SEASONS,
        start=1,
    ):
        season_data = data[
            data.index.month.isin(months)
        ]

        for name, series in season_data.items():
            _add_duration_trace(
                fig,
                series,
                name=name,
                x=x,
                color=(
                    colors.get(name)
                    if colors
                    else None
                ),
                language=language,
                row=1,
                col=col,
                # Same series appears in all four panels.
                showlegend=legend and col == 1,
            )

        if zero_line:
            fig.add_hline(
                y=0,
                line_width=1,
                line_color="gray",
                row=1,
                col=col,
            )

        _format_xaxis(
            fig,
            x=x,
            language=language,
            row=1,
            col=col,
        )

    fig.update_yaxes(
        title_text=ylabel,
        row=1,
        col=1,
    )

    fig.update_layout(
        title=title,
        template="plotly_white",
        height=height,
        width=width,
        showlegend=legend,
        hovermode="closest",
    )

    return fig