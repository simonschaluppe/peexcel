from __future__ import annotations
from pathlib import Path
from typing import Iterator

from pexl.schema.current import SCHEMA_META
from .selection import VariableSelection
from .view import ProjectView
from .scenario import Scenario

class Project:
    """
    Top-level representation of a PEExcel project or export file.

    A Project contains an ordered collection of Scenario objects.

    For standard project exports, each Scenario corresponds to one
    scenario/variant column in the PEExcel IN/OUT sheets. Its identity is
    the exact Excel column header (`Scenario.column_name`), which must be
    unique within the Project.

    For single-scenario timestep exports (`IN.STAGE`, `OUT.Live`, `SIM2`),
    STAGE and Live are treated as source placeholders for one Scenario.
    The Scenario name is derived from the export file name and the SIM2
    data is attached as timestep data.

    Passing `file_source` loads the project immediately. Omitting it creates
    an empty Project.

    Parameters
    ----------
    file_source : str | Path | None
        PEExcel project/export file to load. If None, create an empty Project.
    unknown : {"ignore", "raise"}
        How unknown schema variables encountered during import are handled.

    Examples
    --------
    Load a project:

    >>> project = Project("project.xlsx")

    Create an empty project:

    >>> project = Project()

    Access scenarios:

    >>> project[0]
    >>> project["Aspern Seestadt | BT2 KON FW"]

    Iterate over scenarios:

    >>> for scenario in project:
    ...     print(scenario)

    """

    def __init__(
        self,
        file_source: str | Path | None = None,
        *,
        unknown: str = "ignore"
    ):
        self.file_source = None
        self.scenarios: list[Scenario] = []
        self._scenario_dict: dict[str, Scenario] = {}

        self.warnings: list[str] = []
        self.meta = SCHEMA_META
        self.variables = VariableSelection.all()

        if file_source is not None:
            loaded = self.from_excel(file_source, unknown=unknown)
            self.__dict__.update(loaded.__dict__)

    def add_scenario(
        self,
        scenario: Scenario,
        overwrite: bool = False,
    ) -> None:
        """
        Add a scenario using its Excel column_name as unique key.
        """
        key = scenario.column_name

        if key in self._scenario_dict:
            if not overwrite:
                raise ValueError(
                    f"Duplicate scenario column: {key!r}"
                )

            old = self._scenario_dict[key]
            index = self.scenarios.index(old)
            self.scenarios[index] = scenario

        else:
            self.scenarios.append(scenario)

        self._scenario_dict[key] = scenario

    def get_or_create_scenario(
        self,
        column_name: str,
    ) -> Scenario:
        scenario = self._scenario_dict.get(column_name)

        if scenario is None:
            scenario = Scenario(column_name)
            self.add_scenario(scenario)

        return scenario

    def __getitem__(
        self,
        key: str | int,
    ) -> Scenario:
        if isinstance(key, str):
            return self._scenario_dict[key]

        if isinstance(key, int):
            return self.scenarios[key]

        raise TypeError(
            f"Unsupported scenario key type: {type(key)}"
        )

    def __iter__(self) -> Iterator[Scenario]:
        return iter(self.scenarios)

    def __len__(self) -> int:
        return len(self.scenarios)

    def get(
        self,
        column_name: str,
        default=None,
    ):
        """
        Get a scenario by exact Excel column name.
        """
        return self._scenario_dict.get(
            column_name,
            default,
        )

    def column_names(self) -> list[str]:
        """
        Unique Excel scenario-column identifiers.
        """
        return [
            scenario.column_name
            for scenario in self.scenarios
        ]

    def scenario_names(self) -> list[object]:
        """
        Human-readable project_scenario_name values.

        These are NOT required to be unique.
        """
        return [
            scenario.name
            for scenario in self.scenarios
        ]

    def project_names(self) -> list[object]:
        """
        Unique project_name values in first-occurrence order.
        """
        result = []

        for scenario in self.scenarios:
            value = scenario.project_name

            if value is None:
                continue

            if value not in result:
                result.append(value)

        return result
    

    @classmethod
    def from_excel(
        cls,
        path: str | Path,
        *,
        unknown: str = "ignore", #"raise"
    ) -> "Project":
        from pexl.io.excel import read_project

        return read_project(
            path,
            unknown=unknown,
        )
    
    @classmethod
    def from_files(
        cls,
        paths,
        *,
        unknown: str = "ignore",
    ) -> "Project":
        """
        Load multiple PEExcel files into one Project.

        All scenarios from all source files are combined in file order.
        Scenario column names must be unique across the files.
        """
        project = cls()

        for path in paths:
            source = cls.from_excel(path, unknown=unknown)

            for scenario in source.scenarios:
                if scenario.column_name in project._scenario_dict:
                    raise ValueError(
                        f"Duplicate scenario: {scenario.column_name!r}"
                    )

                project.scenarios.append(scenario)
                project._scenario_dict[scenario.column_name] = scenario

            project.warnings.extend(
                f"{Path(path).name}: {warning}"
                for warning in source.warnings
            )

        return project

    @property
    def view(self):
        from .view import ProjectView
        return ProjectView(self)

    def select(self, **filters):
        return self.view.select(**filters)

    def where(self, **variable_values):
        return self.view.where(**variable_values)


    @property
    def inn(self) -> ProjectView:
        from .view import ProjectView
        from .selection import VariableSelection

        return ProjectView(
            self,
            variables=VariableSelection.all().for_source("IN"),
        )


    @property
    def out(self) -> ProjectView:
        from .view import ProjectView
        from .selection import VariableSelection

        return ProjectView(
            self,
            variables=VariableSelection.all().for_source("OUT"),
        )


    def to_excel(
        self,
        path: str | Path,
        include_derived: bool = True,
        include_default: bool = False,
        include_meta: bool = True,
    ) -> Path:
        from pexl.io.excel import write_project_excel

        return write_project_excel(
            project=self,
            path=path,
            include_derived=include_derived,
            include_default=include_default,
            include_meta=include_meta,
        )

    def __repr__(self) -> str:
        src = (
            f" source={self.file_source!r}"
            if self.file_source
            else ""
        )

        return (
            f"<Project "
            f"scenarios={len(self.scenarios)} "
            f"warnings={len(self.warnings)}"
            f"{src}>"
        )