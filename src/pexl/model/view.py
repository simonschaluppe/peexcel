from __future__ import annotations

from typing import TYPE_CHECKING, Iterator

import pandas as pd

from .selection import VariableSelection, ScenarioSelection

if TYPE_CHECKING:
    from pexl.schema.current import VariableMeta
    from .project import Project
    from .scenario import Scenario


class _BaseView:
    """
    Internal common view over:

        scenarios x variables

    The variable dimension is represented by VariableSelection.
    Subclasses define how the scenario dimension is represented.
    """

    def __init__(
        self,
        scenarios,
        variables: VariableSelection | None = None,
    ):
        self._scenarios = tuple(scenarios)
        self._variables = (
            variables
            if variables is not None
            else VariableSelection.all()
        )

    

    @property
    def shape(self) -> tuple[int, int]:
        """
        (number of scenarios, number of variables)
        """
        return (
            len(self._scenarios),
            len(self._variables),
        )

    def _with_variables(
        self,
        variables: VariableSelection,
    ):
        """
        Return the same view type with a different variable selection.
        """
        raise NotImplementedError

    def select(self, **filters):
        """
        Refine the variable dimension using VariableMeta fields.
        """
        return self._with_variables(
            self._variables.select(**filters)
        )

    def items(
        self,
    ) -> Iterator[tuple["Scenario", "VariableMeta", object]]:
        """
        Iterate over:

            scenario, metadata, value
        """
        for scenario in self._scenarios:
            for meta in self._variables:
                yield (
                    scenario,
                    meta,
                    getattr(
                        scenario.v,
                        meta.attr_name,
                    ),
                )

    def values(self) -> list[list[object]]:
        """
        Scenario-major value matrix.

        Rows:
            scenarios

        Columns:
            variables
        """
        return [
            [
                getattr(
                    scenario.v,
                    meta.attr_name,
                )
                for meta in self._variables
            ]
            for scenario in self._scenarios
        ]

    def unique(self, field: str) -> list[object]:
        """
        Return distinct non-empty values of a VariableMeta field
        across the selected variables.
        """
        return self._variables.unique(field)

    def domains(self) -> list[object]:
        return self.unique("domain")

    def measures(self) -> list[object]:
        return self.unique("measure")

    def entity_groups(self) -> list[object]:
        return self.unique("entity_group")

    def entity_keys(self) -> list[object]:
        return self.unique("entity_key")

class ScenarioView(_BaseView):
    """
    Read-only semantic view over one Scenario.

    ScenarioView is a shallow one-scenario specialization
    of the common view machinery.

    `.select(...)` refines the variable dimension.
    """

    def __init__(
        self,
        scenario: "Scenario",
        variables: VariableSelection | None = None,
    ):
        self._scenario = scenario

        super().__init__(
            scenarios=(scenario,),
            variables=variables,
        )

    @property
    def scenario(self) -> "Scenario":
        return self._scenario

    def _with_variables(
        self,
        variables: VariableSelection,
    ) -> "ScenarioView":
        return ScenarioView(
            scenario=self._scenario,
            variables=variables,
        )

    def items(
        self,
    ) -> Iterator[tuple["VariableMeta", object]]:
        """
        Iterate over:

            metadata, value
        """
        for meta in self._variables:
            yield (
                meta,
                getattr(
                    self._scenario.v,
                    meta.attr_name,
                ),
            )

    def items_dict(self) -> dict:
        return {
            meta: value
            for meta, value in self.items()
        }

    def to_var_dict(self) -> dict[str, object]:
        """
        Return selected values keyed by canonical Excel var_name.
        """
        return {
            meta.var_name: value
            for meta, value in self.items()
        }

    def values(self) -> list[object]:
        """
        Return selected values in canonical variable order.
        """
        return [
            getattr(
                self._scenario.v,
                meta.attr_name,
            )
            for meta in self._variables
        ]

    def __getattr__(self, attr_name: str):
        """
        Direct access to selected variables remains possible:

            scenario.out.QH
        """
        for meta in self._variables:
            if meta.attr_name == attr_name:
                return getattr(
                    self._scenario.v,
                    attr_name,
                )

        raise AttributeError(
            f"{attr_name!r} is not part of this ScenarioView"
        )


    def __repr__(self) -> str:
        return (
            f"<ScenarioView "
            f"scenario={self._scenario.column_name!r} "
            f"variables={len(self._variables)}>"
        )
    
    def _repr_html_(self) -> str:
        import pandas as pd

        df = pd.DataFrame(
            [
                {
                    "var_name": meta.var_name,
                    "label": meta.label_de,
                    "unit": meta.unit,
                    "value": value,
                }
                for meta, value in self.items()
            ]
        )

        header = self.__repr__()

        return header + df.to_html(
            index=False,
            max_rows=30,
        )


class ProjectView(_BaseView):
    """
    Read-only semantic view over a Project.

    Represents the intersection of:

        ScenarioSelection x VariableSelection

    `.select(...)` refines the variable dimension.
    `.where(...)` refines the scenario dimension.
    """

    def __init__(
        self,
        project: "Project",
        scenarios: ScenarioSelection | None = None,
        variables: VariableSelection | None = None,
    ):
        self._project = project

        self._scenario_selection = (
            scenarios
            if scenarios is not None
            else ScenarioSelection(project)
        )

        super().__init__(
            scenarios=self._scenario_selection,
            variables=variables,
        )

    @property
    def project(self) -> "Project":
        return self._project


    @property
    def variables(self) -> VariableSelection:
        return self._variables

    @property
    def scenarios(self) -> ScenarioSelection:
        return self._scenario_selection

    def _with_variables(
        self,
        variables: VariableSelection,
    ) -> "ProjectView":
        return ProjectView(
            project=self._project,
            scenarios=self._scenario_selection,
            variables=variables,
        )

    def where(
        self,
        **variable_values,
    ) -> "ProjectView":
        """
        Refine the scenario dimension according to schema-variable values.

        Examples
        --------
        project.out.where(
            project_name="Forsthausgasse"
        )

        project.out.where(
            preset_recorded_heating_system="Wärmepumpe"
        )
        """
        return ProjectView(
            project=self._project,
            scenarios=self._scenario_selection.where(
                **variable_values
            ),
            variables=self._variables,
        )

    def to_records(self) -> list[dict[str, object]]:
        """
        Return one record per scenario.

        `column_name` is included as the unique structural scenario
        identifier. Selected variables use canonical Excel var_names.

        Example
        -------
        [
            {
                "column_name": "Forsthausgasse | BT2 KON FW",
                "PEI_el_plugloads": 12.4,
                "PEI_el_hvac": 5.8,
            },
            ...
        ]
        """

        return [
            {
                "column_name": scenario.column_name,
                **{
                    meta.var_name: getattr(
                        scenario.v,
                        meta.attr_name,
                    )
                    for meta in self._variables
                },
            }
            for scenario in self._scenario_selection
        ]
    
    def to_frame(self) -> pd.DataFrame:
        return pd.DataFrame(self.to_records()).set_index("column_name")

    def __iter__(self):
        return self.items()

    def __repr__(self) -> str:
        return (
            f"<ProjectView "
            f"scenarios={len(self._scenario_selection)} "
            f"variables={len(self._variables)}>"
        )
    
    def _repr_html_(self) -> str:
        header = self.__repr__()

        return header + self.to_frame().to_html(
            max_rows=20,
            max_cols=12,
    )