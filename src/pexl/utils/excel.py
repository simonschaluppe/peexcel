from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterator

import pandas as pd

from ..schemas.current import ExcelNamedVariables, SCHEMA_META, ATTR_NAME_MAP


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

@dataclass
class Usage:
    key: str
    area: float #m2 NFA
    room_height: float
    # add more usage-scoped variables over time
    dhw_occupancy: float | None = None
    plugloads_scale: float | None = None
    cool_share: float | None = None
    vent_scale: float | None = None
    vent_share_mechanical: float | None = None


class Scenario:
    """
    Represents a single scenario within a district.

    A scenario contains:
    - `name`: Name of the Scenario
    - `v`: all excel "var_name" variable values (inputs + results)
    - `meta`: static metadata for each variable (units, names, etc.)

    Values are accessed via dot-notation:
        scenario.v.QH
        scenario.meta.QH.unit

    Scenarios are created from Excel columns and belong to exactly one District.
    Scenario is indirectly linked to district via scenario.v.project_name -> District name
    """
    def __init__(self, name: str):
        self.name = name
        self.v = ExcelNamedVariables()
        self.meta = SCHEMA_META
        # TODO: attach timestep data container here, e.g. self.sim = None

    def __repr__(self) -> str:
        return f"<Scenario {self.name!r}>"

    def as_dict(self) -> dict:
        """Flat dict of all v.* values"""
        return vars(self.v)

    @staticmethod
    def _get(d, key, default=0):
        val = d.get(key)
        return default if val is None else val

    @property
    def usage_keys(self) -> list[str]:
        return [
            "residential",
            "office",
            "schoolprim",
            "schoolsec",
            "retailfood",
            "retailother",
            "other",
        ]
    
    @property
    def usages(self) -> list[Usage]:
        d = self.as_dict()
        avg_h = self._get(d, "rh_avg", 3.0)

        usages = []

        for k in self.usage_keys:
            area = self._get(d, f"NFA_{k}")
            if area <= 0:
                continue

            usages.append(
                Usage(
                    key=k,
                    area=area,
                    room_height=self._get(d, f"rh_{k}", avg_h),
                    dhw_occupancy=d.get(f"DHW_occupancy_{k}"),
                    plugloads_scale=d.get(f"Plugloads_scale_{k}"),
                    cool_share = d.get(f"cool_share_{k}"),
                    vent_scale=d.get(f"vent_scale_{k}"),
                    vent_share_mechanical = d.get(f"vent_share_mechanical_{k}"),
                )
            )
        return usages
    
class District:
    """
    Container for multiple scenarios belonging to the same district.

    A district groups scenarios that share most base inputs (IN sheet),
    but may differ in outputs (OUT sheet) and some inputs).

    Access patterns:
        district["Base"]        -> scenario by name
        district[0]             -> scenario by index
        for scenario in district: ...  -> iterate scenarios

    Attributes:
        name: name of the district (derived from column names)
        scenarios: ordered list of Scenario objects
        default_scenario: name of the first added scenario (typically "Base")
    """  
    def __init__(self, name: str):
        self.name = name
        self.scenarios: list[Scenario] = []
        self._scenario_dict: dict[str, Scenario] = {}
        self.default_scenario: str | None = None

    def add_scenario(self, scenario: Scenario) -> None:
        if scenario.name in self._scenario_dict:
            raise ValueError(
                f"Duplicate scenario name in district {self.name!r}: {scenario.name!r}"
            )
        self.scenarios.append(scenario)
        self._scenario_dict[scenario.name] = scenario
        if self.default_scenario is None:
            self.default_scenario = scenario.name

    def get_or_create_scenario(self, scenario_name):    
        scenario = self.get(scenario_name)
        if scenario is None:
            scenario = Scenario(scenario_name)
            self.add_scenario(scenario)
        return scenario

    def __getitem__(self, key: str | int) -> Scenario:
        if isinstance(key, str):
            return self._scenario_dict[key]
        if isinstance(key, int):
            return self.scenarios[key]
        raise TypeError(f"Unsupported scenario key type: {type(key)}")

    def __iter__(self) -> Iterator[Scenario]:
        return iter(self.scenarios)

    def __len__(self) -> int:
        return len(self.scenarios)

    def get(self, name: str, default=None):
        return self._scenario_dict.get(name, default)

    def names(self) -> list[str]:
        return [s.name for s in self.scenarios]

    def __repr__(self) -> str:
        return f"<District {self.name!r} scenarios={len(self.scenarios)}>"


class Project:
    """
    Top-level representation of a Project Excel file.

    A project consists of (1 to many) districts, each containing multiple scenarios.

    The project does NOT expose scenarios directly — they are always accessed
    through their district:

        project["District A"]["Base"]

    Attributes:
        file_source: path to the source Excel file
        districts: list of District objects
        warnings: list of import warnings (e.g. mismatches between column names
                  and values inside the Excel data)

    Access patterns:
        project["District A"]   -> district by name
        project[0]              -> district by index
        for d in project: ...   -> iterate districts
    """
    def __init__(self, file_source: str | Path | None = None):
        self.file_source = str(file_source) if file_source is not None else None
        self.districts: list[District] = []
        self._district_dict: dict[str, District] = {}
        self.warnings: list[str] = []

    def add_district(self, district: District) -> None:
        if district.name in self._district_dict:
            raise ValueError(f"Duplicate district name: {district.name!r}")
        self.districts.append(district)
        self._district_dict[district.name] = district

    def get_or_create_district(self, district_name: str) -> District:
        district = self._district_dict.get(district_name)
        if district is None:
            district = District(district_name)
            self.add_district(district)
        return district

    def __getitem__(self, key: str | int) -> District:
        if isinstance(key, str):
            return self._district_dict[key]
        if isinstance(key, int):
            return self.districts[key]
        raise TypeError(f"Unsupported district key type: {type(key)}")

    def __iter__(self) -> Iterator[District]:
        return iter(self.districts)

    def __len__(self) -> int:
        return len(self.districts)

    def get(self, name: str, default=None):
        return self._district_dict.get(name, default)

    def names(self) -> list[str]:
        return [d.name for d in self.districts]

    def __repr__(self) -> str:
        src = f" source={self.file_source!r}" if self.file_source else ""
        return f"<Project districts={len(self.districts)} warnings={len(self.warnings)}{src}>"


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
                    if not var_name: # skip
                        continue
                    if pd.isna(var_name):
                        project.warnings.append(f"{district_name} | {scenario_name} > pd.isna({var_name=}) = True")
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