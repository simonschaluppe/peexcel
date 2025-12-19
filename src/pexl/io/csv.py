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
    }
