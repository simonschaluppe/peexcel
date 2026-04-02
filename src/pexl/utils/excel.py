from __future__ import annotations

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


class Scenario:
    def __init__(self, name: str):
        self.name = name
        self.v = ExcelNamedVariables()
        self.meta = SCHEMA_META
        # TODO: attach timestep data container here, e.g. self.sim = None

    def __repr__(self) -> str:
        return f"<Scenario {self.name!r}>"


class District:
    def __init__(self, file_source: str | Path | None = None):
        self.scenarios: list[Scenario] = []
        self._scenario_dict: dict[str, Scenario] = {}
        self.file_source = str(file_source) if file_source is not None else None
        self.default_scenario: str | None = None

    def add_scenario(self, scenario: Scenario) -> None:
        if scenario.name in self._scenario_dict:
            raise ValueError(f"Duplicate scenario name: {scenario.name!r}")
        self.scenarios.append(scenario)
        self._scenario_dict[scenario.name] = scenario
        if self.default_scenario is None:
            self.default_scenario = scenario.name

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
        src = f" source={self.file_source!r}" if self.file_source else ""
        return f"<District scenarios={len(self.scenarios)}{src}>"


def _read_tables(file_path: str | Path) -> tuple[pd.DataFrame, pd.DataFrame]:
    df_in = pd.read_excel(file_path, sheet_name="IN")
    df_out = pd.read_excel(file_path, sheet_name="OUT")
    return df_in, df_out


def _get_input_scenario_names(df_in: pd.DataFrame) -> list[str]:
    return [
        str(c)
        for c in df_in.columns
        if c not in RESERVED_IN_COLUMN_HEADER_NAMES
    ]


def _apply_sheet_to_scenario(
    scenario: Scenario,
    df: pd.DataFrame,
    scenario_column: str,
    *,
    unknown: str = "raise",
    context: str = "",
) -> None:
    if scenario_column not in df.columns:
        return

    for _, row in df.iterrows():
        var_name = row.get("var_name")
        if pd.isna(var_name) or not var_name:
            continue

        var_name = str(var_name)
        attr_name = ATTR_NAME_MAP.get(var_name)

        if attr_name is None:
            if unknown == "raise":
                raise KeyError(f"Unknown schema var_name {var_name!r} in {context}")
            if unknown == "ignore":
                continue
            raise ValueError(f"Unsupported unknown policy: {unknown!r}")

        setattr(scenario.v, attr_name, row[scenario_column])


def read_project(
    file_path: str | Path,
    *,
    unknown: str = "raise",
) -> District:
    file_path = Path(file_path)
    district = District(file_source=file_path)

    df_in, df_out = _read_tables(file_path)
    scenario_names = _get_input_scenario_names(df_in)

    for sname in scenario_names:
        scenario = Scenario(sname)
        district.add_scenario(scenario)

        _apply_sheet_to_scenario(
            scenario,
            df_in,
            sname,
            unknown=unknown,
            context=f"IN[{sname}]",
        )
        _apply_sheet_to_scenario(
            scenario,
            df_out,
            sname,
            unknown=unknown,
            context=f"OUT[{sname}]",
        )

        # TODO: integrate timestep/simulation data loading for this scenario here

    return district