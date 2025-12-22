# src/pexl/io/converter.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal, Mapping

import json
import shutil

import pandas as pd


Mode = Literal["schema", "raw"]


@dataclass(frozen=True)
class ConvertResult:
    out_dir: Path
    written: dict[str, Path]
    audit_path: Path | None


def xlsx_to_dataset_dir(
    xlsx_path: str | Path,
    out_dir: str | Path,
    *,
    sheets: Mapping[str, str] | None = None,
    mode: Mode = "schema",
    delimiter: str = ";",
    encoding: str = "utf-8",
    replace_files: bool = False,
) -> ConvertResult:
    """
    Convert an exported workbook into a dataset directory.

    Modes:
      - mode="schema" (recommended contract):
          * writes IN.csv and OUT.csv filtered to rows with non-empty var_name (if present)
          * strips whitespace in all cells
          * writes AUDIT.json containing exclusions + counts
      - mode="raw":
          * writes IN.csv and OUT.csv as-is (only fillna(""))

    Notes:
      - This function does not perform semantic schema validation. It only converts.
      - Your CSV reader can auto-detect delimiters; writing ';' keeps Excel-friendly output.
    """
    xlsx_path = Path(xlsx_path)
    out_dir = Path(out_dir)

    if sheets is None:
        sheets = {"IN": "IN", "OUT": "OUT", "SIM": "SIM2"}

    _prepare_out_dir(out_dir, replace_files=replace_files)

    written: dict[str, Path] = {}
    audit: dict[str, object] | None = None

    if mode == "schema":
        audit = {
            "mode": "schema",
            "source_xlsx": str(xlsx_path),
            "tables": {},
        }
    elif mode != "raw":
        raise ValueError(f"Invalid mode={mode!r}. Use 'schema' or 'raw'.")

    for table_name, sheet_name in sheets.items():
        df = pd.read_excel(xlsx_path, sheet_name=sheet_name, dtype=str).fillna("")

        if mode == "schema":
            df, table_audit = _clean_for_schema_contract(df)
            audit["tables"][table_name] = table_audit  # type: ignore[index]

        csv_path = out_dir / f"{table_name}.csv"
        df.to_csv(csv_path, index=False, sep=delimiter, encoding=encoding)
        written[table_name] = csv_path

    audit_path: Path | None = None
    if audit is not None:
        audit_path = out_dir / "AUDIT.json"
        audit_path.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding="utf-8")

    return ConvertResult(out_dir=out_dir, written=written, audit_path=audit_path)


def _prepare_out_dir(out_dir: Path, *, replace_files: bool = False) -> None:
    if out_dir.exists():
        if not replace_files:
            raise FileExistsError(
                f"Output directory exists: {out_dir}\n"
                "Choose a new directory or use replace_files=True."
            )
    else:
        out_dir.mkdir(parents=True)


def _strip_all_cells(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for c in out.columns:
        out[c] = out[c].astype(str).str.strip()
    return out


def _clean_for_schema_contract(df: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, object]]:
    """
    Contract cleaning:
      - strip whitespace across all cells
      - if var_name exists: keep only rows where var_name != ""
      - record excluded rows in audit with minimal identifying info

    We intentionally do NOT filter by ka here; ka quality checks belong in validate/schema.py.
    """
    original_rows = len(df)
    df = _strip_all_cells(df)

    audit: dict[str, object] = {
        "original_rows": original_rows,
        "kept_rows": None,
        "excluded_rows": {},
    }

    if "var_name" in df.columns:
        empty_mask = df["var_name"] == ""
        excluded = df.loc[empty_mask].copy()
        kept = df.loc[~empty_mask].copy()

        audit["excluded_rows"] = {
            "empty_var_name_count": int(empty_mask.sum()),
            # keep a small sample so audit stays readable
            "empty_var_name_sample": _audit_sample_rows(excluded),
        }
        df = kept
    else:
        # If there's no var_name column, we cannot apply the contract filter.
        audit["excluded_rows"] = {
            "empty_var_name_count": None,
            "empty_var_name_sample": [],
            "note": "No 'var_name' column present; no row filtering applied.",
        }

    audit["kept_rows"] = len(df)
    return df.reset_index(drop=True), audit


def _audit_sample_rows(df: pd.DataFrame, *, max_rows: int = 20) -> list[dict[str, str]]:
    """
    Provide a compact sample of excluded rows for debugging in Excel.
    Includes common identifying columns if present + row number within the export.
    """
    if df.empty:
        return []

    # Candidate columns to help you locate the row back in Excel
    preferred_cols = [
        "Name",
        "Kategorie",
        "Bereich",
        "var_cat",
        "Type",
        "Einheit",
        "ka",
        "Formel",
        "Kommentar",
        "ID",
    ]
    cols = [c for c in preferred_cols if c in df.columns]
    sample = df.head(max_rows)

    # Include 1-based row number from the exported sheet (header is row 1)
    # Data starts at row 2 in your export workbook, so +2.
    out: list[dict[str, str]] = []
    for idx, row in sample.iterrows():
        item: dict[str, str] = {"export_row": str(int(idx) + 2)}
        for c in cols:
            item[c] = str(row.get(c, ""))
        out.append(item)
    return out
