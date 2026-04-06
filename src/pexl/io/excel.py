from __future__ import annotations

from dataclasses import fields
from datetime import datetime, UTC
from pathlib import Path

import pandas as pd

from pexl.schema.schema_codegen import VariableMetaRow

from ..model.project import Project
from ..schema.current import ATTR_NAME_MAP


LEGACY_RESERVED_IN_COLUMN_HEADER_NAMES = [
    "Icon",
    "Name",
    "Einheit",
    "Kommentar",
    "Type",
    "var_name",
    "ka",
    "Formel",
]

LEGACY_RESERVED_OUT_COLUMN_HEADER_NAMES = [
    "ID",
    "Kategorie",
    "Type",
    "Name",
    "Icon",
    "Bereich",
    "var_cat",
    "var_name",
    "Einheit",
    "Formel",
    "Label",
    "Kommentar",
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


def _parse_scenario_column(column_name: str) -> tuple[str, str]:
    column_name = str(column_name).strip()
    if not column_name:
        raise ValueError("Empty scenario column name.")

    if " | " in column_name:
        district_name, scenario_name = column_name.split(" | ", 1)
        district_name = district_name.strip()
        scenario_name = scenario_name.strip()
    else:
        district_name = column_name
        scenario_name = column_name

    if not district_name or not scenario_name:
        raise ValueError(f"Invalid scenario column format: {column_name!r}")

    return district_name, scenario_name


def _handle_unknown_var_name(
    *,
    project: Project,
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
    for district in project.districts:
        for scenario in district.scenarios:
            return scenario
    return None


def _iter_scenario_columns(project: Project):
    seen = set()

    for district in project.districts:
        for scenario in district.scenarios:
            col_name = f"{district.name} | {scenario.name}"
            if col_name in seen:
                raise ValueError(f"Duplicate scenario export column name: {col_name!r}")
            seen.add(col_name)
            yield district, scenario, col_name


def read_project(
    file_path: str | Path,
    *,
    unknown: str = "raise",
) -> Project:
    """
    Read a project workbook with sheets IN and OUT.

    Parameters:
    - unknown: when encountering schema-unknown variables: "raise", "ignore"

    Expected column layout:
    - "District" -> district/scenario with same name
    - "District | Scenario" -> named scenario inside the district
    """
    file_path = Path(file_path)
    project = Project(file_source=file_path)

    df_in = pd.read_excel(file_path, sheet_name="IN")
    df_out = pd.read_excel(file_path, sheet_name="OUT")

    in_columns = [str(c) for c in df_in.columns if c not in RESERVED_IN_COLUMN_HEADER_SET]
    out_columns = [str(c) for c in df_out.columns if c not in RESERVED_OUT_COLUMN_HEADER_SET]
    all_columns = _unique(in_columns + out_columns)

    for column_name in all_columns:
        try:
            district_name, scenario_name = _parse_scenario_column(column_name)
        except ValueError as exc:
            if unknown == "ignore":
                project.warnings.append(str(exc))
                continue
            raise

        district = project.get_or_create_district(district_name)
        scenario = district.get_or_create_scenario(scenario_name)

        for df in (df_in, df_out):
            if column_name not in df.columns:
                continue

            for _, row in df.iterrows():
                var_name = row.get("var_name")
                if pd.isna(var_name) or not str(var_name).strip():
                    continue

                var_name = str(var_name)
                attr_name = ATTR_NAME_MAP.get(var_name)
                if attr_name is None:
                    _handle_unknown_var_name(
                        project=project,
                        var_name=var_name,
                        column_name=column_name,
                        unknown=unknown,
                    )
                    continue

                setattr(scenario.v, attr_name, row[column_name])

        project_attr = ATTR_NAME_MAP.get(PROJECT_NAME_VAR)
        scenario_attr = ATTR_NAME_MAP.get(PROJECT_SCENARIO_NAME_VAR)

        value_project_name = getattr(scenario.v, project_attr, None) if project_attr else None
        value_scenario_name = getattr(scenario.v, scenario_attr, None) if scenario_attr else None

        if value_project_name is not None and pd.notna(value_project_name):
            value_project_name = str(value_project_name).strip()
            if value_project_name and value_project_name != district_name:
                project.warnings.append(
                    f"Column {column_name!r}: district name {district_name!r} "
                    f"does not match {PROJECT_NAME_VAR}={value_project_name!r}"
                )

        if value_scenario_name is not None and pd.notna(value_scenario_name):
            value_scenario_name = str(value_scenario_name).strip()
            if value_scenario_name and value_scenario_name != scenario_name:
                project.warnings.append(
                    f"Column {column_name!r}: scenario name {scenario_name!r} "
                    f"does not match {PROJECT_SCENARIO_NAME_VAR}={value_scenario_name!r}"
                )

    return project


def build_project_in_dataframe(
    project: Project,
    include_derived: bool = True,
    base_columns: list[str] | None = None,
    strict: bool = False,
) -> pd.DataFrame:
    """
    Build an Excel-style IN sheet:
    - one row per schema item, in canonical order
    - one scenario column per scenario: "district | scenario"
    """
    if base_columns is None:
        base_columns = DEFAULT_IN_EXPORT_BASE_COLUMNS.copy()

    if "var_name" not in base_columns:
        raise ValueError("base_columns must include 'var_name'.")

    first_scenario = _get_first_scenario(project)
    if first_scenario is None:
        return pd.DataFrame(columns=base_columns)

    rows = []
    exported_var_names = []

    first_var_names = [meta.var_name for meta, _ in first_scenario.inn.items()]
    first_var_name_set = set(first_var_names)

    for meta, _ in first_scenario.inn.items():
        if not include_derived and getattr(meta, "ka", None) == 0:
            continue

        rows.append({col: getattr(meta, col, None) for col in base_columns})
        exported_var_names.append(meta.var_name)

    df = pd.DataFrame(rows, columns=base_columns)

    if df["var_name"].isna().any():
        raise ValueError("Export contains empty var_name values.")
    if (df["var_name"].astype(str).str.strip() == "").any():
        raise ValueError("Export contains blank var_name values.")
    if df["var_name"].duplicated().any():
        dups = df.loc[df["var_name"].duplicated(), "var_name"].tolist()
        raise ValueError(f"Duplicate var_name values in schema: {dups}")

    exported_var_name_set = set(exported_var_names)

    for district, scenario, col_name in _iter_scenario_columns(project):
        values = scenario.inn.to_var_dict()
        values[PROJECT_NAME_VAR] = district.name
        values[PROJECT_SCENARIO_NAME_VAR] = scenario.name

        if strict and set(values) != first_var_name_set:
            missing = sorted(first_var_name_set - set(values))
            extra = sorted(set(values) - first_var_name_set)
            raise ValueError(
                f"Scenario {col_name!r} has mismatching IN items. "
                f"Missing: {missing[:10]} Extra: {extra[:10]}"
            )

        values = {k: v for k, v in values.items() if k in exported_var_name_set}
        df[col_name] = df["var_name"].map(values)

    return df


def write_project_excel(
    project: Project,
    path: str | Path,
    include_derived: bool = True,
    include_default: bool = False,
    include_meta: bool = True,
    base_columns: list[str] | None = None,
    strict: bool = False,
) -> Path:
    path = Path(path)

    if base_columns is None:
        base_columns = DEFAULT_IN_EXPORT_BASE_COLUMNS.copy()

    if not include_default and "default" in base_columns:
        base_columns = [c for c in base_columns if c != "default"]

    df_in = build_project_in_dataframe(
        project=project,
        include_derived=include_derived,
        base_columns=base_columns,
        strict=strict,
    )

    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        df_in.to_excel(writer, sheet_name="IN", index=False)

        if include_meta:
            df_meta = pd.DataFrame(
                [
                    ("export_type", "python_project_excel"),
                    ("file_source", project.file_source or ""),
                    ("district_count", len(project.districts)),
                    ("scenario_count", sum(len(d.scenarios) for d in project.districts)),
                    ("created_by", "pexl"),
                    ("created_at_utc", datetime.now(UTC).isoformat()),
                    ("include_derived", include_derived),
                ],
                columns=["key", "value"],
            )
            df_meta.to_excel(writer, sheet_name="META", index=False)

    return path