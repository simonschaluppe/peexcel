import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from .utils import normalize_data


def duration_curve(
    data,
    *,
    unit=None,
    x="hours",
    figsize=None,
    ax=None,
    zero_line=True,
    legend=True,
    zoom_hours=None,
    colors=None
):
    """
    Plot duration curves for one or more time series.

    Values are sorted independently from highest to lowest.

    Parameters
    ----------
    data : Series | DataFrame | Mapping | Sequence[Series]
        Time series to plot.
    unit : str | None
        Y-axis unit.
    x : {"hours", "percent"}
        X-axis representation.
    figsize : tuple | None
        Figure size.
    ax : matplotlib.axes.Axes | None
        Existing axes. Cannot be used together with zoom_hours.
    zero_line : bool
        Draw a horizontal zero line.
    legend : bool
        Show legend.
    zoom_hours : int | None
        If given, add a second panel showing only the first N hours
        with an automatically adjusted y-axis.

    Returns
    -------
    fig, ax
        Without zoom_hours.

    fig, (ax, ax_zoom)
        With zoom_hours.
    """
    data = normalize_data(data)

    if zoom_hours is not None:
        if ax is not None:
            raise ValueError("ax cannot be used together with zoom_hours")

        if x != "hours":
            raise ValueError("zoom_hours requires x='hours'")

        if figsize is None:
            figsize = (10, 4)

        fig, (ax, ax_zoom) = plt.subplots(
            1,
            2,
            figsize=figsize,
            gridspec_kw={"width_ratios": [2, 1]},
        )
    else:
        ax_zoom = None

        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        else:
            fig = ax.figure

    zoom_values = []

    for name, series in data.items():
        color = colors.get(name) if colors else None
        values = pd.to_numeric(series, errors="coerce").dropna()
        values = np.sort(values.to_numpy())[::-1]

        if x == "hours":
            xx = np.arange(1, len(values) + 1)
        elif x == "percent":
            xx = np.linspace(0, 100, len(values))
        else:
            raise ValueError("x must be 'hours' or 'percent'")

        line, = ax.plot(xx, values, label=name, color=color)

        if ax_zoom is not None:
            n = min(zoom_hours, len(values))

            if ax_zoom is not None:
                ax_zoom.plot(
                    xx[:zoom_hours],
                    values[:zoom_hours],
                    color=line.get_color(),
                    label=name,
                )

            zoom_values.extend(values[:n])

    ax.set_xlabel("Hours" if x == "hours" else "Duration [%]")

    if unit:
        ax.set_ylabel(unit)

    if zero_line:
        ax.axhline(0, linewidth=0.8)

    if legend and len(data.columns) > 1:
        ax.legend()

    if ax_zoom is not None:
        ax_zoom.set_xlabel("Hours")

        if unit:
            ax_zoom.set_ylabel(unit)

        if zero_line:
            ax_zoom.axhline(0, linewidth=0.8)

        if zoom_values:
            ymin = np.nanmin(zoom_values)
            ymax = np.nanmax(zoom_values)

            if ymin == ymax:
                padding = abs(ymin) * 0.05 or 1
            else:
                padding = (ymax - ymin) * 0.05

            ax_zoom.set_ylim(
                ymin - padding,
                ymax + padding,
            )

        ax_zoom.set_xlim(1, zoom_hours)
        ax_zoom.set_title(f"Highest {zoom_hours} h")

        return fig, (ax, ax_zoom)

    return fig, ax