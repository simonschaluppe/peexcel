import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from .utils import normalize_data

def _hour_day_matrix(series: pd.Series) -> pd.DataFrame:
    if not isinstance(series, pd.Series):
        raise TypeError("Expected pd.Series")

    series = series.copy()
    if not isinstance(series.index, pd.DatetimeIndex):
        series.index = pd.to_datetime(series.index, format="mixed")

    series.index = series.index.round("h")

    df = series.rename("value").to_frame()
    df["date"] = df.index.normalize()
    df["hour"] = df.index.hour

    return df.pivot(index="date", columns="hour", values="value").reindex(columns=range(24))


def _set_month_axis(ax, dates):
    dates = pd.DatetimeIndex(dates)
    periods = dates.to_period("M")

    centers = []
    labels = []
    boundaries = [-0.5]

    for month in periods.unique():
        idx = np.flatnonzero(periods == month)
        centers.append((idx[0] + idx[-1]) / 2)
        labels.append(month.strftime("%b"))
        boundaries.append(idx[-1] + 0.5)

    # Labels in month centers
    ax.set_xticks(centers)
    ax.set_xticklabels(labels)

    # Tick marks / separators between months
    ax.set_xticks(boundaries, minor=True)
    ax.tick_params(axis="x", which="major", length=0)
    ax.tick_params(axis="x", which="minor", length=5)


def _heatmap_ax(series, ax, *, title=None, ylabel="Hour of the day",
                vmin=None, vmax=None, cmap="magma"):
    matrix = _hour_day_matrix(series)

    image = ax.imshow(
        matrix.T,
        aspect="auto",
        origin="lower",
        vmin=vmin,
        vmax=vmax,
        cmap=cmap,
    )

    _set_month_axis(ax, matrix.index)

    ax.set_yticks([0, 6, 12, 18, 23])
    ax.set_ylabel(ylabel)

    if title is not None:
        ax.set_title(title)

    return image


def heatmap(
    data,
    *,
    unit=None,
    figsize=None,
    layout="vertical",
    sharex=None,
    sharey=None,
    center=None,
    vmin=None,
    vmax=None,
    cmap="magma",
):
    data = normalize_data(data)
    if sharex is None:
        sharex = layout == "vertical"
    if sharey is None:
        sharey = layout == "horizontal"
    if center is not None and vmin is None and vmax is None:
        values = data.to_numpy(dtype=float)
        limit = np.nanmax(np.abs(values - center))
        vmin = center - limit
        vmax = center + limit
    if isinstance(data, pd.Series):
        if figsize is None:
            figsize = (12, 4)

        fig, ax = plt.subplots(figsize=figsize)

        if center is not None and vmin is None and vmax is None:
            limit = np.nanmax(np.abs(data.to_numpy() - center))
            vmin = center - limit
            vmax = center + limit

        image = _heatmap_ax(
            data,
            ax,
            title=data.name,
            vmin=vmin,
            vmax=vmax,
            cmap=cmap,
        )

        cbar = fig.colorbar(image, ax=ax)
        if unit:
            cbar.set_label(unit)

        fig.tight_layout()
        return fig, ax

    if not isinstance(data, pd.DataFrame):
        raise TypeError("Expected pd.Series or pd.DataFrame")

    n = len(data.columns)

    if center is not None and vmin is None and vmax is None:
        limit = np.nanmax(np.abs(data.to_numpy() - center))
        vmin = center - limit
        vmax = center + limit

    if layout == "horizontal":
        if figsize is None:
            figsize = (6 * n, 4)
        fig, axes = plt.subplots(1, n, figsize=figsize, squeeze=False)
        axes = axes[0]
    else:
        if figsize is None:
            figsize = (12, 3 * n)
        fig, axes = plt.subplots(n, 1, figsize=figsize, squeeze=False)
        axes = axes[:, 0]

    for ax, column in zip(axes, data.columns):
        image = _heatmap_ax(
            data[column],
            ax,
            title=str(column),
            vmin=vmin,
            vmax=vmax,
            cmap=cmap,
        )

    cbar = fig.colorbar(image, ax=axes.tolist())
    if unit:
        cbar.set_label(unit)

    return fig, axes