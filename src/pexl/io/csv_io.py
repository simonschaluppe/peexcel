# pexl/io/csv.py
from pathlib import Path
import pandas as pd


REQUIRED_FILES = ("IN.csv", "OUT.csv")
DEFAULT_TABLES = (
    "IN",
    "OUT",
    "SIM",
    "CHART_metadata",
    "CHART_types",
)

def _read_csv(path: Path) -> pd.DataFrame:
    """
    Read a CSV with strict, predictable settings.
    Everything is read as string; empty cells stay empty strings.
    """
    return pd.read_csv(
        path,
        dtype=str,
        keep_default_na=False,
        delimiter=";"
    )


def read_dataset_dir(
    root: str | Path,
    *,
    strict: bool = True,
) -> dict[str, pd.DataFrame]:

    root = Path(root)

    if strict:
        missing = [
            name
            for name in DEFAULT_TABLES
            if not (root / f"{name}.csv").exists()
        ]

        if missing:
            raise FileNotFoundError(
                f"Missing dataset tables in {root}: {missing}"
            )

        table_names = DEFAULT_TABLES

    else:
        table_names = tuple(
            path.stem
            for path in sorted(root.glob("*.csv"))
        )

        if not table_names:
            raise FileNotFoundError(
                f"No CSV tables found in {root}"
            )

    return {
        name: pd.read_csv(
            root / f"{name}.csv",
            sep=";",
            encoding="utf-8-sig",
        )
        for name in table_names
    }

def normalize_table(
    df: pd.DataFrame,
    *,
    key_cols: list[str],
) -> pd.DataFrame:
    """
    Normalize a table for stable diffs:
    - strip whitespace from all cells
    - stable sort by key columns
    - reset index
    """
    if not key_cols:
        raise ValueError("key_cols must be provided")

    missing = [c for c in key_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Missing key columns: {missing}")

    out = df.copy()

    # strip whitespace everywhere
    for col in out.columns:
        out[col] = out[col].astype(str).str.strip()

    # stable sort
    out = out.sort_values(by=key_cols, kind="stable")

    return out.reset_index(drop=True)

def normalize_dataset(
    tables: dict[str, pd.DataFrame],
    *,
    key_cols: dict[str, list[str]],
) -> dict[str, pd.DataFrame]:
    """
    Normalize all tables in a dataset.
    key_cols: e.g. {"IN": ["var_name"], "OUT": ["var_name"]}
    """
    out: dict[str, pd.DataFrame] = {}
    for name, df in tables.items():
        if name in key_cols:
            out[name] = normalize_table(df, key_cols=key_cols[name])
        else:
            out[name] = df.copy()
    return out
