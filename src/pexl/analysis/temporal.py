from __future__ import annotations

import pandas as pd
import numpy as np

from pexl.i18n import LocalizedText


SEASONS = (
    ("winter", LocalizedText(de="Winter", en="Winter"), (12, 1, 2)),
    ("spring", LocalizedText(de="Frühling", en="Spring"), (3, 4, 5)),
    ("summer", LocalizedText(de="Sommer", en="Summer"), (6, 7, 8)),
    ("autumn", LocalizedText(de="Herbst", en="Autumn"), (9, 10, 11)),
)

SEASON_BY_MONTH = {
    month: season
    for season, _, months in SEASONS
    for month in months
}

def add_season(
    df: pd.DataFrame,
    *,
    month_col: str = "Monat_nr",
    season_col: str = "season",
) -> pd.DataFrame:
    df = df.copy()
    df[season_col] = df[month_col].map(SEASON_BY_MONTH)
    return df

def numeric_frame(frame, columns):
    missing = set(columns) - set(frame.columns)
    if missing:
        raise ValueError(f'Missing exported channels: {sorted(missing)}')
    values = frame[list(columns)].apply(pd.to_numeric, errors='raise')
    if not np.isfinite(values.to_numpy(dtype=float)).all():
        raise ValueError('Missing or non-finite result values; zero substitution is not permitted')
    return values


def hourly_frame(scenario):
    """Copy and validate exported hourly timestamps and calendar metadata."""
    frame = scenario.timeseries.to_frame().copy()
    index = pd.DatetimeIndex(pd.to_datetime(frame['date']))
    if index.hasnans or index.has_duplicates or not index.is_monotonic_increasing:
        raise ValueError('Invalid hourly time axis')
    if len(index) < 2 or not (index.to_series().diff().dropna() == pd.Timedelta(hours=1)).all():
        raise ValueError('Expected a continuous one-hour timestep')
    frame.index = index
    if not (frame['Monat_nr'].to_numpy() == index.month).all():
        raise ValueError('Month metadata differs from timestamps')
    if not (frame['hour_of_the_day'].to_numpy() == index.hour).all():
        raise ValueError('Hour metadata differs from timestamps')
    return frame


def channel_inventory(frame, groups):
    """Inspect explicitly selected channels; absent channels are not zero series.

    Column names are stable identifiers, independent of presentation language.
    ``sum`` is the sum in the input unit, not an inferred energy integral.
    """
    rows = []
    for group, columns in groups.items():
        for column in columns:
            present = column in frame
            values = numeric_frame(frame, [column])[column] if present else None
            rows.append(dict(group=group, channel=column, present=present,
                             nonzero_count=int(values.ne(0).sum()) if present else None,
                             sum=float(values.sum()) if present else None))
    return pd.DataFrame(rows, columns=['group', 'channel', 'present', 'nonzero_count', 'sum'])


def seasonal_hourly_mean(frame, columns):
    """Mean of selected values by season/hour, without unit conversion.

    Requires a continuous hourly DatetimeIndex. Returns a new frame with
    ``season`` and ``hour_of_the_day`` plus the selected columns.
    """
    index = frame.index
    if (not isinstance(index, pd.DatetimeIndex) or index.hasnans
            or len(index) < 2 or index.has_duplicates
            or not (index.to_series().diff().dropna() == pd.Timedelta(hours=1)).all()):
        raise ValueError('Expected a continuous one-hour DatetimeIndex')
    values = numeric_frame(frame, columns).copy()
    values['season'] = index.month.map(SEASON_BY_MONTH)
    values['hour_of_the_day'] = index.hour
    return values.groupby(['season', 'hour_of_the_day'], observed=True)[list(columns)].mean().reset_index()
