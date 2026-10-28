"""Internal PEExcel table mapping, independent of workbook file handling.

Rows are schema variables; scenario identities are column headers. These
serialization tables are distinct from the scenario-row analysis views.
"""
from __future__ import annotations

from dataclasses import fields
from typing import TYPE_CHECKING, Literal

import pandas as pd

from pexl.schema.schema_codegen import VariableMetaRow
from ..schema.current import ATTR_NAME_MAP, SCHEMA_META

if TYPE_CHECKING:
    from ..model.project import Project
    from ..model.scenario import Scenario


LEGACY_RESERVED_IN_COLUMN_HEADER_NAMES = [
    "Icon", "Name", "Einheit", "Kommentar", "Type", "var_name", "ka", "Formel",
]

LEGACY_RESERVED_OUT_COLUMN_HEADER_NAMES = [
    "ID", "Kategorie", "Type", "Name", "Icon", "Bereich", "var_cat", "var_name",
    "Einheit", "Formel", "Label", "Kommentar",
]

PROJECT_NAME_VAR = "project_name"
PROJECT_SCENARIO_NAME_VAR = "project_scenario_name"


def _unique(items: list[str]) -> list[str]:
    seen = set()
    out = []
    for item in items:
        if item not in seen:
            seen.add(item)
            out.append(item)
    return out


VARIABLE_META_COLUMN_NAMES = [f.name for f in fields(VariableMetaRow)]

DEFAULT_IN_EXPORT_BASE_COLUMNS = VARIABLE_META_COLUMN_NAMES.copy()
DEFAULT_OUT_EXPORT_BASE_COLUMNS = VARIABLE_META_COLUMN_NAMES.copy()

RESERVED_IN_COLUMN_HEADER_NAMES = _unique(
    LEGACY_RESERVED_IN_COLUMN_HEADER_NAMES + VARIABLE_META_COLUMN_NAMES
)
RESERVED_OUT_COLUMN_HEADER_NAMES = _unique(
    LEGACY_RESERVED_OUT_COLUMN_HEADER_NAMES + VARIABLE_META_COLUMN_NAMES
)

RESERVED_IN_COLUMN_HEADER_SET = set(RESERVED_IN_COLUMN_HEADER_NAMES)
RESERVED_OUT_COLUMN_HEADER_SET = set(RESERVED_OUT_COLUMN_HEADER_NAMES)


def _parse_scenario_column_convention(column_name: str) -> tuple[str, str]:
    """
    Parse the conventional PEExcel scenario-column naming scheme.

    This is validation only. The actual Excel column header remains the
    authoritative Scenario.column_name.
    """
    column_name = str(column_name).strip()
    if not column_name:
        raise ValueError("Empty scenario column name.")

    if " | " in column_name:
        project_name, scenario_name = column_name.split(" | ", 1)
        project_name = project_name.strip()
        scenario_name = scenario_name.strip()
    else:
        project_name = column_name
        scenario_name = column_name

    if not project_name or not scenario_name:
        raise ValueError(f"Invalid scenario column convention: {column_name!r}")

    return project_name, scenario_name


def _clean_text(value) -> str | None:
    if value is None or pd.isna(value):
        return None
    value = str(value).strip()
    return value or None


def _validate_scenario_column_convention(project: Project, scenario) -> None:
    """
    Compare the structural Excel column name with semantic scenario values.

    Mismatches are warnings only. The Excel column header remains identity.
    """
    try:
        column_project_name, column_scenario_name = _parse_scenario_column_convention(
            scenario.column_name
        )
    except ValueError as exc:
        project.warnings.append(str(exc))
        return

    project_attr = ATTR_NAME_MAP.get(PROJECT_NAME_VAR)
    scenario_attr = ATTR_NAME_MAP.get(PROJECT_SCENARIO_NAME_VAR)

    value_project_name = (
        _clean_text(getattr(scenario.v, project_attr, None)) if project_attr else None
    )
    value_scenario_name = (
        _clean_text(getattr(scenario.v, scenario_attr, None)) if scenario_attr else None
    )

    if value_project_name is not None and value_project_name != column_project_name:
        project.warnings.append(
            f"Column {scenario.column_name!r}: conventional project name "
            f"{column_project_name!r} does not match "
            f"{PROJECT_NAME_VAR}={value_project_name!r}"
        )

    if value_scenario_name is not None and value_scenario_name != column_scenario_name:
        project.warnings.append(
            f"Column {scenario.column_name!r}: conventional scenario name "
            f"{column_scenario_name!r} does not match "
            f"{PROJECT_SCENARIO_NAME_VAR}={value_scenario_name!r}"
        )


def _handle_unknown_var_name(
    *,
    var_name: str,
    column_name: str,
    unknown: str,
) -> None:
    if unknown == "ignore":
        return
    if unknown == "raise":
        raise KeyError(f"Unknown schema var_name {var_name!r} in {column_name!r}")
    raise ValueError(f"Unsupported unknown policy: {unknown!r}")


def _get_first_scenario(project: Project):
    return project.scenarios[0] if project.scenarios else None


def _iter_scenario_columns(project: Project):
    """Yield scenarios with their authoritative Excel column names."""
    seen = set()

    for scenario in project.scenarios:
        col_name = scenario.column_name
        if col_name in seen:
            raise ValueError(f"Duplicate scenario export column name: {col_name!r}")
        seen.add(col_name)
        yield scenario, col_name


def _iter_schema_metas_for_source(source: str):
    """
    Yield schema metadata in canonical order for IN or OUT.

    Workbook serialization stays independent from ScenarioView/ProjectView.
    """
    if source not in ("IN", "OUT"):
        raise ValueError(f"source must be 'IN' or 'OUT', got {source!r}")

    for attr_name in ATTR_NAME_MAP.values():
        meta = getattr(SCHEMA_META, attr_name)
        if meta.source in (source, "BOTH"):
            yield meta


def scenario_columns(frame: pd.DataFrame, *, source: Literal["IN", "OUT"]) -> list[str]:
    """Return non-metadata column headers in workbook order."""
    if source not in ("IN", "OUT"):
        raise ValueError(f"source must be 'IN' or 'OUT', got {source!r}")
    reserved = (RESERVED_IN_COLUMN_HEADER_SET if source == "IN"
                else RESERVED_OUT_COLUMN_HEADER_SET)
    return [str(column) for column in frame.columns if column not in reserved]


def load_scenario_values(
    scenario: Scenario,
    df: pd.DataFrame,
    column_name: str,
    *,
    unknown: str,
) -> None:
    """Copy one workbook column into existing scenario values, without coercion."""
    if unknown not in ("ignore", "raise"):
        raise ValueError(f"Unsupported unknown policy: {unknown!r}")
    if column_name not in df.columns:
        return

    # Reading Series pairs avoids constructing a Series for every cell column.
    # This matters for annual projects with thousands of scenario columns.
    for var_name, value in zip(df["var_name"], df[column_name]):
        if pd.isna(var_name) or not str(var_name).strip():
            continue

        var_name = str(var_name)
        attr_name = ATTR_NAME_MAP.get(var_name)

        if attr_name is None:
            _handle_unknown_var_name(
                var_name=var_name,
                column_name=column_name,
                unknown=unknown,
            )
            if var_name in scenario.legacy:
                previous = scenario.legacy[var_name]
                if not pd.isna(previous) and not pd.isna(value) and previous != value:
                    raise ValueError(f"Conflicting legacy values for {var_name!r} in {column_name!r}")
                if pd.isna(value):
                    continue
            scenario.legacy[var_name] = value
            continue

        setattr(scenario.v, attr_name, value)


def build_project_table(
    project: Project,
    *,
    source: Literal["IN", "OUT"],
    include_derived: bool = True,
    base_columns: list[str] | None = None,
    strict: bool = False,
) -> pd.DataFrame:
    """
    Build an Excel-style IN or OUT table without file IO.

    - one row per selected schema item, in canonical schema order
    - one column per Scenario
    - scenario column names come directly from Scenario.column_name

    project_name and project_scenario_name are exported from Scenario.v like
    all other schema variables; they are not reconstructed from Python objects.
    """
    if source not in ("IN", "OUT"):
        raise ValueError(f"source must be 'IN' or 'OUT', got {source!r}")

    if base_columns is None:
        base_columns = (DEFAULT_IN_EXPORT_BASE_COLUMNS if source == "IN"
                        else DEFAULT_OUT_EXPORT_BASE_COLUMNS).copy()

    if "var_name" not in base_columns:
        raise ValueError("base_columns must include 'var_name'.")

    first_scenario = _get_first_scenario(project)
    if first_scenario is None:
        return pd.DataFrame(columns=base_columns)

    metas = list(_iter_schema_metas_for_source(source))
    if source == "IN" and not include_derived:
        metas = [meta for meta in metas if getattr(meta, "ka", None) != 0]

    rows = [
        {col: getattr(meta, col, None) for col in base_columns}
        for meta in metas
    ]
    df = pd.DataFrame(rows, columns=base_columns)

    if df["var_name"].isna().any():
        raise ValueError("Export contains empty var_name values.")
    if df["var_name"].astype(str).str.strip().eq("").any():
        raise ValueError("Export contains blank var_name values.")
    if df["var_name"].duplicated().any():
        dups = df.loc[df["var_name"].duplicated(), "var_name"].tolist()
        raise ValueError(f"Duplicate var_name values in schema: {dups}")

    scenario_data = {}
    for scenario, col_name in _iter_scenario_columns(project):
        if strict:
            missing_attrs = [
                meta.attr_name
                for meta in metas
                if not hasattr(scenario.v, meta.attr_name)
            ]
            if missing_attrs:
                raise ValueError(
                    f"Scenario {col_name!r} is missing schema attributes: "
                    f"{missing_attrs[:10]}"
                )

        scenario_data[col_name] = [getattr(scenario.v, meta.attr_name) for meta in metas]

    return pd.concat([df, pd.DataFrame(scenario_data, index=df.index)], axis=1)


