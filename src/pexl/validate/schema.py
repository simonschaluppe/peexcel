from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Literal

import json
import re
import pandas as pd
from openpyxl.formula import Tokenizer
from openpyxl.formula.tokenizer import TokenizerError

from pexl.io.csv_io import read_dataset_dir, normalize_table


TABLE_KEYS: dict[str, str] = {
    "IN": "var_name",
    "OUT": "var_name",
    "SIM": "var_name",
    "CHART_types": "chart_name",
}

# Excel schema columns that contain formulas; compare independently of the
# general metadata/value-change report and its output cap.
FORMULA_COLUMNS: dict[str, str] = {
    "IN": "Formel",
    "OUT": "Formel",
    "SIM": "Formula",
}

DEFAULT_COMPARE_COLS: dict[str, list[str]] = {
    "IN": ["ka", "Type", "Einheit", "Formel", "Name"],
    "OUT": ["Kategorie", "Bereich", "var_cat", "Einheit", "Label", "Formel", "Name"],
    "SIM": ["Column Name", "Formula"],
    "CHART_types": ["tab_name", "title", "chart_type"],
}

@dataclass(frozen=True)
class SchemaDiffOptions:
    key_col: str = "var_name"
    compare_cols: dict[str, list[str]] | None = None
    max_value_changes: int = 200  # cap for report size


def _diff_table_structure(
    old_df: pd.DataFrame,
    new_df: pd.DataFrame,
) -> dict[str, Any]:

    old_cols = set(old_df.columns)
    new_cols = set(new_df.columns)

    return {
        "status": "common",
        "detail": "structural",
        "columns": {
            "added": sorted(new_cols - old_cols),
            "removed": sorted(old_cols - new_cols),
            "common_count": len(old_cols & new_cols),
        },
        "rows": {
            "old_count": len(old_df),
            "new_count": len(new_df),
        },
    }


def _describe_new_table(
    df: pd.DataFrame,
    *,
    status: str,
) -> dict[str, Any]:

    return {
        "status": status,
        "detail": "structural",
        "columns": list(df.columns),
        "rows": {
            "count": len(df),
        },
    }

def diff_schema_dirs(
    old_dir: str | Path,
    new_dir: str | Path,
    *,
    options: SchemaDiffOptions | None = None,
) -> dict[str, Any]:

    options = options or SchemaDiffOptions()
    compare_cols = options.compare_cols or DEFAULT_COMPARE_COLS

    old_dir = Path(old_dir)
    new_dir = Path(new_dir)

    old_tables = read_dataset_dir(old_dir, strict=False) #might not have new structures
    new_tables = read_dataset_dir(new_dir, strict=False) # might not have old structures

    old_names = set(old_tables)
    new_names = set(new_tables)

    added_tables = sorted(new_names - old_names)
    removed_tables = sorted(old_names - new_names)
    common_tables = sorted(old_names & new_names)

    warnings: list[str] = []

    if added_tables:
        warnings.append(
            f"Tables added to schema: {added_tables}"
        )

    if removed_tables:
        warnings.append(
            f"Tables removed from schema: {removed_tables}"
        )

    report: dict[str, Any] = {
        "meta": {
            "old_dir": str(old_dir),
            "new_dir": str(new_dir),
        },
        "files": {
            "old_count": len(old_names),
            "new_count": len(new_names),
            "added": added_tables,
            "removed": removed_tables,
            "common": common_tables,
        },
        "warnings": warnings,
        "tables": {},
        "audit": _diff_audit(old_dir, new_dir),
    }

    # Detailed diff where both versions contain the table
    # and we know its semantic key.
    for table_name in common_tables:

        key_col = TABLE_KEYS.get(table_name)

        if key_col is None:
            report["tables"][table_name] = _diff_table_structure(
                old_tables[table_name],
                new_tables[table_name],
            )
            continue

        report["tables"][table_name] = _diff_table(
            old_tables[table_name],
            new_tables[table_name],
            table_name=table_name,
            key_col=key_col,
            compare_cols=compare_cols.get(table_name, []),
            max_value_changes=options.max_value_changes,
        )

    # Still describe newly added/removed tables.
    for table_name in added_tables:
        report["tables"][table_name] = _describe_new_table(
            new_tables[table_name],
            status="added",
        )

    for table_name in removed_tables:
        report["tables"][table_name] = _describe_new_table(
            old_tables[table_name],
            status="removed",
        )

    return report


def _diff_table(
    old_df: pd.DataFrame,
    new_df: pd.DataFrame,
    *,
    table_name: str,
    key_col: str,
    compare_cols: list[str],
    max_value_changes: int,
) -> dict[str, Any]:
    # Normalize for stable diffs (strip + stable sort by key)
    # If key_col missing, fail loudly: schema exports must contain var_name.
    old_norm = normalize_table(old_df, key_cols=[key_col])
    new_norm = normalize_table(new_df, key_cols=[key_col])

    # Basic column diffs
    old_cols = list(old_norm.columns)
    new_cols = list(new_norm.columns)
    old_set = set(old_cols)
    new_set = set(new_cols)

    added_cols = sorted(new_set - old_set)
    removed_cols = sorted(old_set - new_set)
    common_cols = [c for c in old_cols if c in new_set]  # preserve old ordering

    # Row/key stats
    old_keys = old_norm[key_col].tolist()
    new_keys = new_norm[key_col].tolist()

    old_key_set = set(old_keys)
    new_key_set = set(new_keys)

    added_keys = sorted(new_key_set - old_key_set)
    removed_keys = sorted(old_key_set - new_key_set)

    # Duplicates (should not happen in canonical schema)
    old_dupes = _find_duplicates(old_norm, key_col)
    new_dupes = _find_duplicates(new_norm, key_col)

    # Compare values for keys present in both
    common_keys = sorted(old_key_set & new_key_set)

    # Determine which columns to compare
    # Only compare columns that exist in BOTH frames.
    if compare_cols:
        cols_to_compare = [c for c in compare_cols if c in old_set and c in new_set]
    else:
        # fallback: compare all common columns except key
        cols_to_compare = [c for c in common_cols if c != key_col]

    # Classify formula changes independently of the generic diff cap.
    # Local relative A1-reference movements are retained as relocations,
    # but do not count as actual formula changes.
    formula_diff = _diff_formulas_by_key(
        old_norm,
        new_norm,
        key_col=key_col,
        keys=common_keys,
        formula_col=FORMULA_COLUMNS.get(table_name),
    )

    # Suppress local-reference-only differences from the generic diff too.
    # This keeps schema_evolution.ipynb's value_changes free of noise.
    formula_col = formula_diff["column"]
    ignored_changes = {
        (str(item[key_col]), formula_col)
        for item in formula_diff["relocations"]
    }
    value_changes = _diff_values_by_key(
        old_norm,
        new_norm,
        key_col=key_col,
        keys=common_keys,
        cols=cols_to_compare,
        max_changes=max_value_changes,
        ignored_changes=ignored_changes,
    )

    return {
        "columns": {
            "added": added_cols,
            "removed": removed_cols,
            "common_count": len(common_cols),
        },
        "rows": {
            "old_count": len(old_norm),
            "new_count": len(new_norm),
            "var_name_added": added_keys,
            "var_name_removed": removed_keys,
            "duplicate_keys_old": old_dupes,
            "duplicate_keys_new": new_dupes,
        },
        "changes": {
            "compared_columns": cols_to_compare,
            "value_change_count": value_changes["change_count"],
            "value_changes": value_changes["changes"],
            "truncated": value_changes["truncated"],
            "formula_column": formula_diff["column"],
            "formula_status": formula_diff["status"],
            "formula_missing_in": formula_diff["missing_in"],
            "formula_change_count": formula_diff["count"],
            "formula_changes": formula_diff["changes"],
            "formula_relocation_count": len(formula_diff["relocations"]),
            "formula_relocations": formula_diff["relocations"],
        },
    }


# A single, unqualified relative A1 reference (e.g. N83, AB105).
# References with '$' and sheet-qualified ranges are deliberately NOT masked.
_LOCAL_A1_REF = re.compile(r"[A-Z]{1,3}[1-9][0-9]*", re.IGNORECASE)


def _formula_signature(formula: str) -> str | None:
    """Mask only unqualified *relative* A1 coordinates in a formula.

    Formula cells in schema CSVs can lack the leading '='. It is added only
    for tokenization; the original presence of '=' is retained in the signature.

    Examples:
      N83 * N105                   -> <REF> * <REF>
      SUMME(N112:N115) * N111      -> SUMME(<REF>:<REF>) * <REF>
      IN!N83                       -> IN!N83            (cross-sheet: literal)
      SUMME(IN!N83:N90)            -> unchanged         (cross-sheet range)
      $N$83                        -> $N$83             (absolute: literal)
      Table[Column N83]            -> unchanged         (structured reference)
      "N83"                        -> unchanged         (string constant)

    This is deliberately pattern-based, not semantic dependency analysis:
    changing a local reference to another local reference is suppressed even
    if the referenced variable is different. If tokenization fails, return
    None, which conservatively makes the diff report the change.
    """
    raw = str(formula).strip()
    if not raw:
        return raw

    has_equal = raw.startswith("=")
    try:
        tokens = Tokenizer(raw if has_equal else "=" + raw).items
    except (TokenizerError, ValueError, IndexError):
        return None

    parts: list[str] = []
    for token in tokens:
        value = token.value
        if token.type == "OPERAND" and token.subtype == "RANGE":
            # Tokenizer keeps sheet-qualified ranges, including the second
            # endpoint of Sheet!N83:N90, as ONE operand. Preserve them.
            # A local range is a colon-separated chain of bare A1 refs.
            cells = value.split(":")
            if all(_LOCAL_A1_REF.fullmatch(cell) for cell in cells):
                value = ":".join("<REF>" for _ in cells)
        parts.append(value)
    return ("=" if has_equal else "") + "".join(parts)


def _is_local_reference_only_change(old: str, new: str) -> bool:
    """True when all modifications are to local relative A1 coordinates."""
    if old == new:
        return False
    old_sig = _formula_signature(old)
    new_sig = _formula_signature(new)
    return old_sig is not None and old_sig == new_sig


def _diff_formulas_by_key(
    old_df: pd.DataFrame,
    new_df: pd.DataFrame,
    *,
    key_col: str,
    keys: list[str],
    formula_col: str | None,
) -> dict[str, Any]:
    """Separate substantive changes from local-reference-only changes."""
    empty = {
        "column": formula_col,
        "status": "not_applicable" if formula_col is None else "unavailable",
        "missing_in": [],
        "count": 0,
        "changes": [],
        "relocations": [],
    }
    if formula_col is None:
        return empty

    missing_in = [
        version for version, df in (("old", old_df), ("new", new_df))
        if formula_col not in df.columns
    ]
    if missing_in:
        return {**empty, "missing_in": missing_in}

    old_idx = old_df.set_index(key_col)
    new_idx = new_df.set_index(key_col)
    changes: list[dict[str, str]] = []
    relocations: list[dict[str, str]] = []

    for key in keys:
        old_val = str(old_idx.at[key, formula_col])
        new_val = str(new_idx.at[key, formula_col])
        if old_val == new_val:
            continue

        change = {
            key_col: key,
            "column": formula_col,
            "old": old_val,
            "new": new_val,
        }
        if _is_local_reference_only_change(old_val, new_val):
            relocations.append(change)
        else:
            changes.append(change)

    return {
        "column": formula_col,
        "status": "compared",
        "missing_in": [],
        "count": len(changes),
        "changes": changes,
        "relocations": relocations,
    }


def _diff_values_by_key(
    old_df: pd.DataFrame,
    new_df: pd.DataFrame,
    *,
    key_col: str,
    keys: list[str],
    cols: list[str],
    max_changes: int,
    ignored_changes: set[tuple[str, str]] | None = None,
) -> dict[str, Any]:
    ignored_changes = ignored_changes or set()
    # Index by key for fast lookups (assumes canonical schema => unique)
    old_idx = old_df.set_index(key_col, drop=False)
    new_idx = new_df.set_index(key_col, drop=False)
    
    changes: list[dict[str, str]] = []
    change_count = 0
    truncated = False

    for k in keys:
        old_row = old_idx.loc[k]
        new_row = new_idx.loc[k]

        for c in cols:
            old_val = str(old_row.get(c, ""))
            new_val = str(new_row.get(c, ""))

            if old_val != new_val and (str(k), c) not in ignored_changes:
                change_count += 1
                if len(changes) < max_changes:
                    changes.append(
                        {
                            key_col: k,
                            "column": c,
                            "old": old_val,
                            "new": new_val,
                        }
                    )
                else:
                    truncated = True

    return {
        "change_count": change_count,
        "changes": changes,
        "truncated": truncated,
    }



def _find_duplicates(df: pd.DataFrame, key_col: str) -> list[str]:
    dupes = df[key_col][df[key_col].duplicated()].unique().tolist()
    return sorted([str(x) for x in dupes])


def _read_audit(path: Path) -> dict[str, Any] | None:
    audit_path = path / "AUDIT.json"
    if not audit_path.exists():
        return None
    try:
        return json.loads(audit_path.read_text(encoding="utf-8"))
    except Exception:
        # keep diff robust; schema diff should still work even if audit is malformed
        return {"_error": f"Failed to parse {audit_path}"}


def _diff_audit(old_dir: Path, new_dir: Path) -> dict[str, Any]:
    old_audit = _read_audit(old_dir)
    new_audit = _read_audit(new_dir)

    if old_audit is None and new_audit is None:
        return {"present": False}

    # Extract the key signal: empty var_name exclusions per table (from converter)
    def extract_empty_counts(a: dict[str, Any] | None) -> dict[str, Any]:
        if not a or "tables" not in a:
            return {}
        out: dict[str, Any] = {}
        for tname, tinfo in (a.get("tables") or {}).items():
            ex = (tinfo or {}).get("excluded_rows") or {}
            out[tname] = {
                "empty_var_name_count": ex.get("empty_var_name_count"),
            }
        return out

    return {
        "present": True,
        "old": extract_empty_counts(old_audit),
        "new": extract_empty_counts(new_audit),
        "raw_old_present": old_audit is not None,
        "raw_new_present": new_audit is not None,
    }


def schema_diff_to_markdown(report: dict, *, value_format: Literal["table", "items", "None"] = "table") -> str:
    """
    Render a schema diff report (from diff_schema_dirs) to Markdown.

    format="table": value changes rendered as a Markdown table (current behavior)
    format="items": other value changes rendered as grouped bullet items.

    Formula changes are always displayed in a side-by-side version table,
    independent of value_format and without truncation.
    """
    meta = report.get("meta", {})
    header = "\n".join(
        [
            "# Schema Diff",
            "",
            f"- **Old:** `{meta.get('old_dir')}`",
            f"- **New:** `{meta.get('new_dir')}`",
        ]
    )

    files_md = _render_files_section(report)

    tables_md = "\n\n".join(
        _render_table_section(
            tname,
            t,
            value_format=value_format,
            old_version=Path(str(meta.get("old_dir", "old"))).name,
            new_version=Path(str(meta.get("new_dir", "new"))).name,
        )
        for tname, t in (report.get("tables", {}) or {}).items()
    )

    audit = report.get("audit", {}) or {}
    audit_md = _render_audit_section(audit) if audit.get("present") else ""

    return "\n\n".join(
        s
        for s in (
            header,
            files_md,
            tables_md,
            audit_md,
        )
        if s.strip()
    )


def _render_files_section(report: dict) -> str:
    files = report.get("files", {})
    warnings = report.get("warnings", [])

    lines = [
        "## Dataset files",
        "",
        f"- Old file count: {files.get('old_count')}",
        f"- New file count: {files.get('new_count')}",
        f"- Added: {files.get('added', [])}",
        f"- Removed: {files.get('removed', [])}",
    ]

    if warnings:
        lines += [
            "",
            "### Warnings",
            *[f"- ⚠ {warning}" for warning in warnings],
        ]

    return "\n".join(lines)

def _render_table_section(
    tname: str,
    t: dict,
    *,
    value_format: Literal["table", "items", "None"],
    old_version: str,
    new_version: str,
) -> str:
    
    if t.get("detail") == "structural":
        status = t.get("status", "common")
        rows = t.get("rows", {})
        columns = t.get("columns", {})

        return "\n".join(
            [
                f"## {tname}",
                "",
                f"- Status: **{status}**",
                f"- Rows: {rows}",
                f"- Columns: {columns}",
            ]
        )
    cols = t.get("columns", {}) or {}
    rows = t.get("rows", {}) or {}
    ch = t.get("changes", {}) or {}

    column_lines = ["### Columns", f"- Common: {cols.get('common_count', 0)}"]
    if cols.get("added"):
        column_lines.append(f"- Added: {', '.join(cols['added'])}")
    if cols.get("removed"):
        column_lines.append(f"- Removed: {', '.join(cols['removed'])}")
    columns_md = "\n".join(column_lines)

    row_lines = [
        "### Rows",
        f"- Count: {rows.get('old_count', 0)} → {rows.get('new_count', 0)}",
    ]
    if rows.get("var_name_added"):
        row_lines.extend([
            "- Added variables:",
            *(f"  - `{name}`" for name in rows["var_name_added"]),
        ])
    if rows.get("var_name_removed"):
        row_lines.extend([
            "- Removed variables:",
            *(f"  - `{name}`" for name in rows["var_name_removed"]),
        ])
    if rows.get("duplicate_keys_old"):
        row_lines.append(f"- ⚠ Duplicates (old): {rows['duplicate_keys_old']}")
    if rows.get("duplicate_keys_new"):
        row_lines.append(f"- ⚠ Duplicates (new): {rows['duplicate_keys_new']}")
    rows_md = "\n".join(row_lines)

    formula_md = _render_formula_changes(ch, old_version=old_version, new_version=new_version)
    value_md = _render_value_changes(ch, value_format=value_format)

    return "\n\n".join(
        part for part in (f"## {tname}", columns_md, rows_md, formula_md, value_md)
        if part
    )

def _render_formula_changes(
    ch: dict, *, old_version: str, new_version: str
) -> str:
    """Render substantive formula edits as a side-by-side version table.

    Raw export formulas may omit their initial '='. Restore it for display
    only; keep the underlying diff data exactly as exported.
    """
    status = ch.get("formula_status", "not_applicable")
    if status == "not_applicable":
        return ""

    lines = [
        "### Formula changes",
        f"- Changed: {ch.get('formula_change_count', 0)}",
        f"- Local relative-reference changes suppressed: {ch.get('formula_relocation_count', 0)}",
    ]
    if status == "unavailable":
        missing = ", ".join(ch.get("formula_missing_in", []))
        lines.append(f"- ⚠ Comparison unavailable (`{ch.get('formula_column')}` missing in: {missing})")
        return "\n".join(lines)

    changes = ch.get("formula_changes", [])
    if not changes:
        return "\n".join(lines + ["", "_No formula changes._"])

    lines += [
        "",
        f"| var_name | { _md_escape(old_version) } | { _md_escape(new_version) } |",
        "|---|---|---|",
    ]
    for change in changes:
        lines.append(
            f"| {_md_escape(change.get('var_name', ''))} | "
            f"{_md_formula(change.get('old', ''))} | "
            f"{_md_formula(change.get('new', ''))} |"
        )
    return "\n".join(lines)


def _md_formula(value: str) -> str:
    """Add the Excel '=' prefix and format formula safely in a Markdown table."""
    formula = str(value).strip()
    if not formula:
        return "—"
    if not formula.startswith("="):
        formula = "=" + formula
    formula = formula.replace("|", r"\|").replace("\r", "").replace("\n", r"\n")
    # A longer code fence allows backticks within formula text.
    fence = "`" * (max((len(m.group()) for m in re.finditer(r"`+", formula)), default=0) + 1)
    return f"{fence}{formula}{fence}"


def _render_value_changes(ch: dict, *, value_format: Literal["table", "items", "None"]) -> str:
    # Keep formula entries in the JSON value_changes for existing consumers,
    # but avoid displaying them twice in the Markdown report.
    formula_col = (
        ch.get("formula_column") if ch.get("formula_status") == "compared"
        else None
    )
    formula_in_generic_diff = formula_col in ch.get("compared_columns", [])
    other_count = ch.get("value_change_count", 0) - (
        ch.get("formula_change_count", 0) if formula_in_generic_diff else 0
    )
    changes = [
        c for c in (ch.get("value_changes", []) or [])
        if c.get("column") != formula_col
    ]
    if other_count == 0 and not ch.get("truncated"):
        return ""

    header_lines = [
        "### Other value changes",
        f"- Compared columns: {[c for c in ch.get('compared_columns', []) if c != formula_col]}",
        f"- Change count: {other_count}",
    ]
    if ch.get("truncated"):
        header_lines.append("- ⚠ Output truncated")

    header = "\n".join(header_lines)

    if not changes:
        note = (
            "_No other value changes shown (output truncated)._"
            if other_count > 0 and ch.get("truncated")
            else "_No other value changes._"
        )
        return "\n\n".join([header, note])

    if value_format == "table":
        return "\n\n".join([header, _render_changes_table(changes)])
    elif value_format == "items":
        return "\n\n".join([header, _render_changes_items(changes)])
    elif value_format == "None": 
        return "\n\n"
    else:
        raise ValueError(f"Unknown value_format={value_format!r}")


def _render_changes_table(changes: list[dict]) -> str:
    lines = ["| var_name | column | old | new |", "|---|---|---|---|"]
    for c in changes:
        lines.append(
            f"| {c.get('var_name')} | {c.get('column')} | "
            f"{_md_escape(c.get('old',''))} | {_md_escape(c.get('new',''))} |"
        )
    return "\n".join(lines)


def _render_changes_items(changes: list[dict]) -> str:
    grouped: dict[str, list[dict]] = {}
    for c in changes:
        grouped.setdefault(str(c.get("var_name", "")), []).append(c)

    blocks: list[str] = []
    for var_name in sorted(grouped.keys()):
        blocks.append(f"- **{var_name}**")
        for d in grouped[var_name]:
            blocks.append(
                f"  - `{d.get('column')}`: `{_md_escape(d.get('old',''))}` → `{_md_escape(d.get('new',''))}`"
            )
    return "\n".join(blocks)


def _render_audit_section(audit: dict) -> str:
    return "\n".join(
        [
            "## Audit summary",
            "",
            f"- Raw audit present (old): {audit.get('raw_old_present')}",
            f"- Raw audit present (new): {audit.get('raw_new_present')}",
            "",
            "### Empty var_name exclusions (converter)",
            "",
            "**Old:**",
            f"```json\n{audit.get('old', {})}\n```",
            "**New:**",
            f"```json\n{audit.get('new', {})}\n```",
        ]
    )


def _md_escape(val: str) -> str:
    # minimal escaping for Markdown tables and inline code
    s = str(val)
    s = s.replace("|", "\\|")
    s = s.replace("\n", "\\n")
    s = s.replace("\r", "")
    s = s.replace("*", " * ")
    return s