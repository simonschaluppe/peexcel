# pexl/io/csv.py
from pathlib import Path
import pandas as pd


REQUIRED_FILES = ("IN.csv", "OUT.csv")


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


def read_dataset_dir(root: str | Path) -> dict[str, pd.DataFrame]:
    """
    Read a dataset directory containing IN.csv and OUT.csv.

    Returns:
        {
            "IN": DataFrame,
            "OUT": DataFrame,
            "SIM": DataFrame,
        }
    """
    root = Path(root)

    if not root.exists():
        raise FileNotFoundError(f"Dataset dir does not exist: {root}")

    missing = [f for f in REQUIRED_FILES if not (root / f).exists()]
    if missing:
        raise FileNotFoundError(
            f"Missing required files in {root}: {missing}"
        )

    return {
        "IN": _read_csv(root / "IN.csv"),
        "OUT": _read_csv(root / "OUT.csv"),
        "SIM": _read_csv(root / "SIM.csv"),
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
