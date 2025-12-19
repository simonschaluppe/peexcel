from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

import json
import pandas as pd

from pexl.io.csv import read_dataset_dir, normalize_table


DEFAULT_COMPARE_COLS: dict[str, list[str]] = {
    "IN": ["ka", "Type", "Einheit", "Formel", "Name"],
    "OUT": ["Kategorie", "Bereich", "var_cat", "Einheit", "Label", "Formel", "Name"],
}


@dataclass(frozen=True)
class SchemaDiffOptions:
    key_col: str = "var_name"
    compare_cols: dict[str, list[str]] | None = None
    max_value_changes: int = 200  # cap for report size


def diff_schema_dirs(
    old_dir: str | Path,
    new_dir: str | Path,
    *,
    options: SchemaDiffOptions | None = None,
) -> dict[str, Any]:
    """
    Diff two schema dataset directories that contain IN.csv and OUT.csv.
    Returns a JSON-serializable report dict.
    """
    options = options or SchemaDiffOptions()
    compare_cols = options.compare_cols or DEFAULT_COMPARE_COLS

    old_dir = Path(old_dir)
    new_dir = Path(new_dir)

    old_tables = read_dataset_dir(old_dir)
    new_tables = read_dataset_dir(new_dir)

    report: dict[str, Any] = {
        "meta": {
            "old_dir": str(old_dir),
            "new_dir": str(new_dir),
            "key_col": options.key_col,
        },
        "tables": {},
        "audit": _diff_audit(old_dir, new_dir),
    }

    for table_name in ("IN", "OUT"):
        old_df = old_tables[table_name]
        new_df = new_tables[table_name]

        report["tables"][table_name] = _diff_table(
            old_df,
            new_df,
            table_name=table_name,
            key_col=options.key_col,
            compare_cols=compare_cols.get(table_name, []),
            max_value_changes=options.max_value_changes,
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

    value_changes = _diff_values_by_key(
        old_norm,
        new_norm,
        key_col=key_col,
        keys=common_keys,
        cols=cols_to_compare,
        max_changes=max_value_changes,
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
        },
    }


def _diff_values_by_key(
    old_df: pd.DataFrame,
    new_df: pd.DataFrame,
    *,
    key_col: str,
    keys: list[str],
    cols: list[str],
    max_changes: int,
) -> dict[str, Any]:
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

            if old_val != new_val:
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


def schema_diff_to_markdown(report: dict, *, format: Literal["table", "items"] = "table") -> str:
    """
    Render a schema diff report (from diff_schema_dirs) to Markdown.

    format="table": value changes rendered as a Markdown table (current behavior)
    format="items": value changes rendered as grouped bullet items (better for long var_name/formulas)
    """
    meta = report.get("meta", {})
    header = "\n".join(
        [
            "# Schema Diff",
            "",
            f"- **Old:** `{meta.get('old_dir')}`",
            f"- **New:** `{meta.get('new_dir')}`",
            f"- **Key:** `{meta.get('key_col')}`",
        ]
    )

    tables_md = "\n\n".join(
        _render_table_section(tname, t, value_format=format)
        for tname, t in (report.get("tables", {}) or {}).items()
    )

    audit = report.get("audit", {}) or {}
    audit_md = _render_audit_section(audit) if audit.get("present") else ""

    return "\n\n".join(s for s in (header, tables_md, audit_md) if s.strip())


def _render_table_section(tname: str, t: dict, *, value_format: Literal["table", "items"]) -> str:
    cols = t.get("columns", {}) or {}
    rows = t.get("rows", {}) or {}
    ch = t.get("changes", {}) or {}

    columns_md = "\n".join(
        [
            "### Columns",
            f"- Added: {cols.get('added', [])}",
            f"- Removed: {cols.get('removed', [])}",
            f"- Common count: {cols.get('common_count')}",
        ]
    )

    row_lines = [
        "### Rows",
        f"- Old count: {rows.get('old_count')}",
        f"- New count: {rows.get('new_count')}",
        f"- var_name added: {rows.get('var_name_added', [])}",
        f"- var_name removed: {rows.get('var_name_removed', [])}",
    ]
    if rows.get("duplicate_keys_old"):
        row_lines.append(f"- ⚠ Duplicates (old): {rows['duplicate_keys_old']}")
    if rows.get("duplicate_keys_new"):
        row_lines.append(f"- ⚠ Duplicates (new): {rows['duplicate_keys_new']}")
    rows_md = "\n".join(row_lines)

    value_md = _render_value_changes(ch, value_format=value_format)

    return "\n\n".join([f"## {tname}", columns_md, rows_md, value_md])


def _render_value_changes(ch: dict, *, value_format: Literal["table", "items"]) -> str:
    compared = ch.get("compared_columns", [])
    count = ch.get("value_change_count")
    truncated = ch.get("truncated")
    changes = ch.get("value_changes", []) or []

    header_lines = [
        "### Value changes",
        f"- Compared columns: {compared}",
        f"- Change count: {count}",
    ]
    if truncated:
        header_lines.append("- ⚠ Output truncated")

    header = "\n".join(header_lines)

    if not changes:
        return "\n\n".join([header, "_No value changes._"])

    if value_format == "table":
        return "\n\n".join([header, _render_changes_table(changes)])
    if value_format == "items":
        return "\n\n".join([header, _render_changes_items(changes)])

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
    return s