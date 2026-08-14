from __future__ import annotations

from pexl.schema.current import (
    ExcelNamedVariables,
    SCHEMA_META,
    ATTR_NAME_MAP,
)

class Scenario:
    """
    Represents one PEExcel scenario/variant column.

    Structural identity
    -------------------
    column_name:
        Exact Excel column header. Unique within a Project.

    Scenario metadata
    -----------------
    project_name:
        Backed by v.project_name.

    name:
        Human-readable scenario/variant name.
        Backed by v.project_scenario_name.

    """

    def __init__(self, column_name: str):
        if not column_name:
            raise ValueError("Scenario column_name must not be empty")

        self.column_name = str(column_name)

        self.v = ExcelNamedVariables()
        self.meta = SCHEMA_META

        # TODO:
        # self.sim = None

    @property
    def project_name(self):
        return self.v.project_name

    @property
    def name(self):
        return self.v.project_scenario_name
    
    @property
    def view(self):
        from .view import ScenarioView
        return ScenarioView(self)
    
    def select(self, **filters):
        return self.view.select(**filters)

    @property
    def inn(self):
        from .view import ScenarioView
        from .selection import VariableSelection

        return ScenarioView(
            self,
            VariableSelection.all().for_source("IN"),
        )


    @property
    def out(self):
        from .view import ScenarioView
        from .selection import VariableSelection

        return ScenarioView(
            self,
            VariableSelection.all().for_source("OUT"),
        )

    def as_dict(self) -> dict:
        """
        Flat dict of runtime values keyed by Python attribute name.
        """
        return vars(self.v)

    def to_var_dict(self) -> dict[str, object]:
        """
        Flat dict keyed by canonical Excel var_name.
        """
        return {
            var_name: getattr(self.v, attr_name)
            for var_name, attr_name in ATTR_NAME_MAP.items()
        }

    def __repr__(self) -> str:
        return (
            f"<Scenario "
            f"column={self.column_name!r} "
            f"project={self.project_name!r} "
            f"name={self.name!r}>"
        )