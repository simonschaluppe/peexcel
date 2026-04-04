from __future__ import annotations

from pathlib import Path


import pandas as pd

from ..model.project import Project
from ..schema.current import ATTR_NAME_MAP


RESERVED_IN_COLUMN_HEADER_NAMES = [
    "Icon",
    "Name",
    "Einheit",
    "Kommentar",
    "Type",
    "var_name",
    "ka",
    "Formel",
]

RESERVED_OUT_COLUMN_HEADER_NAMES = [
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


def read_project(
    file_path: str | Path,
    *,
    unknown: str = "raise",
) -> Project:
    """
    Read a project workbook with sheets IN and OUT.

    Expected column layout:
    - "District" -> base scenario named "Base"
    - "District | Scenario" -> named scenario inside the district
    """
    file_path = Path(file_path)
    project = Project(file_source=file_path)

    # Read both sheets
    df_in = pd.read_excel(file_path, sheet_name="IN")
    df_out = pd.read_excel(file_path, sheet_name="OUT")

    # Collect all non-reserved data columns from both sheets
    in_columns = [
        str(c) for c in df_in.columns
        if c not in RESERVED_IN_COLUMN_HEADER_NAMES
    ]
    out_columns = [
        str(c) for c in df_out.columns
        if c not in RESERVED_OUT_COLUMN_HEADER_NAMES
    ]

    # Keep original order, but avoid duplicates
    all_columns: list[str] = []
    for column_name in in_columns + out_columns:
        if column_name not in all_columns:
            all_columns.append(column_name)

    # Process each project/scenario column
    for column_name in all_columns:
        # Decode column name:
        #   "District" -> district="District", scenario="Base"
        #   "District | Scenario" -> district="District", scenario="Scenario"
        if " | " in column_name:
            district_name, scenario_name = column_name.split(" | ", 1)
            district_name = district_name.strip()
            scenario_name = scenario_name.strip()
            if not district_name or not scenario_name:
                if unknown == "ignore":
                    project.warnings.append(f"Skipping invalid scenario column format: {column_name!r}")
                    continue
                else:
                    raise ValueError(f"Invalid scenario column format: {column_name!r}")
        else:
            district_name = column_name.strip()
            scenario_name = district_name
            if not district_name:
                if unknown == "ignore":
                    project.warnings.append(f"Skipping invalid scenario column format: {column_name!r}")
                    continue
                else:
                    raise ValueError(f"Invalid district column format: {column_name!r}")

        # Get or create the district 
        district = project.get_or_create_district(district_name)

        # Get or create the scenario (can be passed twice: once by input and once by output sheet, but potentially also only once)
        scenario = district.get_or_create_scenario(scenario_name)

        # Copy IN values into the scenario
        for df in [df_in, df_out]:
            if column_name in df.columns:
                for _, row in df.iterrows():
                    var_name = row.get("var_name")
                    if not var_name or pd.isna(var_name):
                        continue

                    var_name = str(var_name)
                    attr_name = ATTR_NAME_MAP.get(var_name)

                    if attr_name is None:
                        if unknown == "raise":
                            raise KeyError(f"Unknown schema var_name {var_name!r} in {column_name}")
                        if unknown == "ignore":
                            continue
                        raise ValueError(f"Unsupported unknown policy: {unknown!r}")

                    setattr(scenario.v, attr_name, row[column_name])

        # Check whether the values stored inside the scenario agree with the column name
        value_project_name = getattr(scenario.v, ATTR_NAME_MAP.get(PROJECT_NAME_VAR), None)
        value_scenario_name = getattr(scenario.v, ATTR_NAME_MAP.get(PROJECT_SCENARIO_NAME_VAR), None) 

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

        # TODO: integrate timestep/simulation data loading for this scenario here

    return project