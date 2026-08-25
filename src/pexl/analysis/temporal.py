from __future__ import annotations

import pandas as pd

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