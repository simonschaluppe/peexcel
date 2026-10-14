"""PEExcel workbook IO. Table-to-model conversion lives in _project_tables."""
from __future__ import annotations

from datetime import datetime, UTC
from pathlib import Path

import pandas as pd

from ..model.project import Project
# Retain existing module-level constants for callers importing them from excel.
from ._project_tables import (
    DEFAULT_IN_EXPORT_BASE_COLUMNS,
    DEFAULT_OUT_EXPORT_BASE_COLUMNS,
    LEGACY_RESERVED_IN_COLUMN_HEADER_NAMES,
    LEGACY_RESERVED_OUT_COLUMN_HEADER_NAMES,
    PROJECT_NAME_VAR,
    PROJECT_SCENARIO_NAME_VAR,
    RESERVED_IN_COLUMN_HEADER_NAMES,
    RESERVED_OUT_COLUMN_HEADER_NAMES,
    RESERVED_IN_COLUMN_HEADER_SET,
    RESERVED_OUT_COLUMN_HEADER_SET,
    VARIABLE_META_COLUMN_NAMES,
    _unique,
    _validate_scenario_column_convention,
    build_project_table,
    load_scenario_values,
    scenario_columns,
)


def read_project(
    file_path: str | Path,
    *,
    unknown: str = "raise",
) -> Project:
    """
    Read a PEExcel project/export workbook.

    Supported formats:

    1. Single-scenario timestep export
       - SIM2 sheet exists
       - IN contains exactly one scenario column: STAGE
       - scenario name is derived from the file name
       - IN/STAGE, OUT/Live and SIM2 belong to that scenario

    2. Standard annual project export
       - no SIM2
       - IN and OUT contain one or more scenario columns
       - Excel scenario column headers remain authoritative identities

    3. Future multi-scenario timestep export
       - TSD_index sheet exists
       - not implemented yet
    """
    file_path = Path(file_path)
    project = Project()
    project.file_source = file_path

    with pd.ExcelFile(file_path) as xls:
        sheets = set(xls.sheet_names)

        if "TSD_index" in sheets:
            raise NotImplementedError(
                "Multi-scenario timestep exports with TSD_index are not yet supported."
            )

        if "IN" not in sheets or "OUT" not in sheets:
            raise ValueError("PEExcel project must contain sheets 'IN' and 'OUT'.")

        df_in = pd.read_excel(xls, sheet_name="IN")
        df_out = pd.read_excel(xls, sheet_name="OUT")

        in_columns = scenario_columns(df_in, source="IN")
        out_columns = scenario_columns(df_out, source="OUT")

        # ------------------------------------------------------------------
        # Case 1: single-scenario timestep export
        # ------------------------------------------------------------------
        if "SIM2" in sheets:
            if in_columns != ["STAGE"]:
                raise ValueError(
                    "SIM2 export expected exactly one IN scenario column named 'STAGE', "
                    f"found: {in_columns}"
                )

            scenario_name = file_path.stem
            scenario = project.get_or_create_scenario(scenario_name)
            load_scenario_values(scenario, df_in, "STAGE", unknown=unknown)

            if "Live" in df_out.columns:
                load_scenario_values(scenario, df_out, "Live", unknown=unknown)
            elif len(out_columns) == 1:
                project.warnings.append(
                    f"SIM2 export has no OUT column 'Live'; using {out_columns[0]!r}."
                )
                load_scenario_values(scenario, df_out, out_columns[0], unknown=unknown)
            else:
                project.warnings.append(
                    "SIM2 export has no unambiguous OUT scenario column."
                )

            df_sim = pd.read_excel(xls, sheet_name="SIM2")

            if "date" in df_sim.columns:
                df_sim["date"] = pd.to_datetime(
                    df_sim["date"],
                    format="mixed",
                ).dt.round("h")
                df_sim = df_sim.set_index("date",drop=False)

            scenario.set_timeseries(df_sim)
            return project

        # ------------------------------------------------------------------
        # Case 2: standard annual project export
        # ------------------------------------------------------------------
        all_columns = _unique(in_columns + out_columns)

        for column_name in all_columns:
            if not column_name.strip():
                message = "Empty scenario column name."
                if unknown == "ignore":
                    project.warnings.append(message)
                    continue
                raise ValueError(message)

            scenario = project.get_or_create_scenario(column_name)

            load_scenario_values(scenario, df_in, column_name, unknown=unknown)
            load_scenario_values(scenario, df_out, column_name, unknown=unknown)

            _validate_scenario_column_convention(project, scenario)

        return project



def build_project_in_dataframe(
    project: Project,
    include_derived: bool = True,
    base_columns: list[str] | None = None,
    strict: bool = False,
) -> pd.DataFrame:
    """Build an IN export table: variable rows and scenario columns.

    Retained as the public entry point; values and identities come from Project.
    For analysis with scenario rows, use ProjectView.to_frame() instead.
    """
    return build_project_table(
        project, source="IN", include_derived=include_derived,
        base_columns=base_columns, strict=strict,
    )


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
                    ("project_name_count", len(project.project_names())),
                    ("scenario_count", len(project.scenarios)),
                    ("created_by", "pexl"),
                    ("created_at_utc", datetime.now(UTC).isoformat()),
                    ("include_derived", include_derived),
                ],
                columns=["key", "value"],
            )
            df_meta.to_excel(writer, sheet_name="META", index=False)

    return path
