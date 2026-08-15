from __future__ import annotations

from pathlib import Path
from typing import Any, Iterable

import pandas as pd


CSV_SEP = ";"


def clean_cell(value: Any) -> Any:
    """Normalize spreadsheet/CSV cells for code generation."""
    if pd.isna(value):
        return None
    if isinstance(value, str):
        value = value.strip()
        return value if value else None
    return value


def optional_int(value: Any) -> int | None:
    """Parse an optional integer-like spreadsheet value."""
    value = clean_cell(value)
    if value is None:
        return None
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return None


def as_python_literal(value: Any) -> str:
    """Return a safe Python source literal for a normalized cell value."""
    value = clean_cell(value)
    return "None" if value is None else repr(value)


def require_columns(
    df: pd.DataFrame,
    required: Iterable[str],
    *,
    table_name: str,
) -> None:
    """Raise a clear error if a schema/report table misses required columns."""
    required = tuple(required)
    missing = [name for name in required if name not in df.columns]
    if missing:
        raise ValueError(
            f"{table_name} is missing required columns: {missing}. "
            f"Available columns: {list(df.columns)}"
        )


def read_csv_table(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    return pd.read_csv(path, sep=CSV_SEP, encoding="utf-8-sig")


def write_generated_module(path: str | Path, code: str) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(code, encoding="utf-8")
    return path
