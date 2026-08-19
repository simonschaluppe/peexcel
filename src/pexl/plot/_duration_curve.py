from __future__ import annotations

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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

TOP_HOURS_LABEL = LocalizedText(
    de="Höchste",
    en="Top",
)

SEASONS = (
    (LocalizedText(de="❄️ Winter", en="❄️ Winter"), (12, 1, 2)),
    (LocalizedText(de="Frühling", en="Spring"), (3, 4, 5)),
    (LocalizedText(de="☀️ Sommer", en="☀️ Summer"), (6, 7, 8)),
    (LocalizedText(de="Herbst", en="Autumn"), (9, 10, 11)),
)


# Helpers ----------------------------------------------------------------------


def _sorted_values(series) -> np.ndarray:
    """Return numeric values sorted from highest to lowest."""
    values = (
        pd.to_numeric(series, errors="coerce")
        .dropna()
        .to_numpy()
    )

    return np.sort(values)[::-1]


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


def _plot_curves(
    ax,
    data: pd.DataFrame,
    *,
    x: str,
    colors=None,
    annotate_max: bool = False,
    unit: str | None = None,
):
    """
    Plot all duration curves onto one axis.

    Returns the sorted values and assigned colors for reuse by the inset.
    """
    curves = {}

    for name, series in data.items():
        values = _sorted_values(series)

        if len(values) == 0:
            continue

        xx = _duration_x(len(values), x)

        color = colors.get(name) if colors else None

        line, = ax.plot(
            xx,
            values,
            label=name,
            color=color,
        )

        curves[name] = {
            "values": values,
            "color": line.get_color(),
        }

        if annotate_max:
            ax.annotate(
                f"Max. {name}\n{values[0]:.1f} {unit or ''}",
                xy=(0, values[0]),
                xytext=(250, values[0]),
                color=line.get_color(),
                fontsize=8,
                va="bottom",
                ha="left",
            )

    return curves


def _add_peak_inset(
    ax,
    curves,
    *,
    peak_hours: int,
    language: Language,
):
    """Add a common inset showing the highest N hours."""

    if not peak_hours or not curves:
        return None

    ax_peak = ax.inset_axes(
        [0.53, 0.25, 0.44, 0.42]
    )

    peak_values = []

    for curve in curves.values():
        values = curve["values"]
        color = curve["color"]

        n = min(peak_hours, len(values))

        if n == 0:
            continue

        ax_peak.plot(
            np.arange(n),
            values[:n],
            color=color,
            linewidth=1,
        )

        peak_values.extend(values[:n])

    if not peak_values:
        return ax_peak

    ymin = min(peak_values)
    ymax = max(peak_values)

    padding = (ymax - ymin) * 0.08 or 1

    ax_peak.set_xlim(
        0,
        peak_hours,
    )

    ax_peak.set_ylim(
        ymin - padding,
        ymax + padding,
    )

    # 24 h grid/ticks, including zero
    ax_peak.set_xticks(
        np.arange(
            0,
            peak_hours + 1,
            24,
        )
    )

    ax_peak.set_title(
        f"{TOP_HOURS_LABEL.get(language)} {peak_hours} h",
        fontsize=8,
    )

    ax_peak.tick_params(
        labelsize=7,
    )

    ax_peak.grid(
        alpha=0.2,
    )

    return ax_peak


def _format_duration_axis(
    ax,
    *,
    x: str,
    unit: str | None,
    language: Language,
    zero_line: bool,
):
    """Apply common duration-curve axis formatting."""

    ax.set_xlabel(
        XLABEL.get(language)
        if x == "hours"
        else DURATION_LABEL.get(language)
    )

    if unit:
        ax.set_ylabel(unit)

    if x == "hours":
        # Duration curve starts exactly at hour 0.
        ax.set_xlim(left=0)

    if zero_line:
        # Neutral zero line, not Matplotlib's default blue.
        ax.axhline(
            0,
            color="0.35",
            linewidth=0.8,
        )


# Standard duration curve ------------------------------------------------------


def duration_curve(
    data,
    *,
    unit=None,
    x="hours",
    annotate_max=True,
    peak_hours=72,
    figsize=None,
    ax=None,
    zero_line=True,
    legend=True,
    colors=None,
    language: Language = "de",
):
    """
    Plot duration curves for one or more time series.

    Values are sorted independently from highest to lowest.

    Parameters
    ----------
    data : Series | DataFrame | Mapping | Sequence[Series]
        Time series to plot.
    unit : str | None
        Y-axis label/unit.
    x : {"hours", "percent"}
        X-axis representation.
    annotate_max : bool
        Annotate the maximum value of each curve.
    peak_hours : int | None
        Show an inset containing the highest N hours.
        Only available for x="hours".
    figsize : tuple | None
        Figure size.
    ax : matplotlib.axes.Axes | None
        Existing axes.
    zero_line : bool
        Draw a neutral horizontal zero line.
    legend : bool
        Show legend.
    colors : Mapping | None
        Optional mapping of series name -> color.
    language : {"de", "en"}
        Plot language.

    Returns
    -------
    fig, ax
    """
    data = normalize_data(data)

    if x not in {"hours", "percent"}:
        raise ValueError("x must be 'hours' or 'percent'")

    if peak_hours and x != "hours":
        raise ValueError(
            "peak_hours requires x='hours'"
        )

    if ax is None:
        fig, ax = plt.subplots(
            figsize=figsize,
        )
    else:
        fig = ax.figure

    curves = _plot_curves(
        ax,
        data,
        x=x,
        colors=colors,
        annotate_max=annotate_max,
        unit=unit,
    )

    _format_duration_axis(
        ax,
        x=x,
        unit=unit,
        language=language,
        zero_line=zero_line,
    )

    if peak_hours:
        _add_peak_inset(
            ax,
            curves,
            peak_hours=peak_hours,
            language=language,
        )

    if legend and len(data.columns) > 1:
        ax.legend()

    return fig, ax


# Seasonal duration curves -----------------------------------------------------


def seasonal_duration_curves(
    data,
    *,
    unit=None,
    x="hours",
    annotate_max=True,
    peak_hours=72,
    figsize=(14, 4),
    zero_line=True,
    legend=False,
    colors=None,
    language: Language = "de",
):
    """
    Plot duration curves for winter, spring, summer and autumn.

    Data must have a DatetimeIndex.
    """
    data = normalize_data(data)

    if not isinstance(data.index, pd.DatetimeIndex):
        raise TypeError(
            "seasonal_duration_curves requires "
            "data with a DatetimeIndex"
        )

    if x not in {"hours", "percent"}:
        raise ValueError("x must be 'hours' or 'percent'")

    if peak_hours and x != "hours":
        raise ValueError(
            "peak_hours requires x='hours'"
        )

    fig, axes = plt.subplots(
        1,
        4,
        figsize=figsize,
        sharey=True,
    )

    for ax, (season_label, months) in zip(
        axes,
        SEASONS,
    ):
        season_data = data[
            data.index.month.isin(months)
        ]

        curves = _plot_curves(
            ax,
            season_data,
            x=x,
            colors=colors,
            annotate_max=annotate_max,
            unit=unit,
        )

        _format_duration_axis(
            ax,
            x=x,
            unit=None,  # shared y label below
            language=language,
            zero_line=zero_line,
        )

        if peak_hours:
            _add_peak_inset(
                ax,
                curves,
                peak_hours=peak_hours,
                language=language,
            )

        ax.set_title(
            season_label.get(language)
        )

    if unit:
        axes[0].set_ylabel(unit)

    if legend and len(data.columns) > 1:
        axes[0].legend()

    fig.tight_layout()

    return fig, axes