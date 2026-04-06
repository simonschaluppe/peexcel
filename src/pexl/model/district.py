   
from typing import Iterator
from .scenario import Scenario


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

    def add_scenario(self, scenario: Scenario, overwrite=False) -> None:
        if scenario.name in self._scenario_dict:
            if not overwrite:
                raise ValueError(
                f"Duplicate scenario name in district {self.name!r}: {scenario.name!r}"
            )
        else:
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

