from __future__ import annotations

from typing import TYPE_CHECKING, Iterable, Iterator

from pexl.schema.current import (
    ATTR_NAME_MAP,
    SCHEMA_META,
    VariableMeta,
    TIMESERIES_ATTR_NAME_MAP,
    TIMESERIES_META,
    TimeseriesMeta,
)

if TYPE_CHECKING:
    from .project import Project
    from .scenario import Scenario

def _resolve_attr_name(
    name: str | VariableMeta,
) -> str:
    if isinstance(name, VariableMeta):
        return name.attr_name

    if name in ATTR_NAME_MAP:
        return ATTR_NAME_MAP[name]

    if name in ATTR_NAME_MAP.values():
        return name

    raise KeyError(f"Unknown variable: {name!r}")


class VariableSelection:
    """
    Ordered, value-free selection of schema variables.

    A VariableSelection only describes WHICH variables are selected.
    It does not contain scenarios or runtime values.

    Canonical schema order is preserved when selections are created
    from `all()` and subsequently filtered.
    """

    def __init__(self, variables: Iterable[VariableMeta]):
        self._vars = tuple(variables)

    @classmethod
    def all(cls) -> "VariableSelection":
        """
        Return all variables in canonical schema order.
        """
        return cls(
            getattr(SCHEMA_META, attr_name)
            for attr_name in ATTR_NAME_MAP.values()
        )

    def for_source(self, source: str) -> "VariableSelection":
        """
        Restrict selection to IN or OUT variables.

        Variables with source='BOTH' are included in either selection.
        """
        if source not in ("IN", "OUT"):
            raise ValueError(
                f"source must be 'IN' or 'OUT', got {source!r}"
            )

        return VariableSelection(
            meta
            for meta in self._vars
            if meta.source in (source, "BOTH")
        )
    
    def select(
        self,
        *names: str | VariableMeta,
        **filters,
    ) -> VariableSelection:
        """
        Select variables explicitly by name or filter by VariableMeta fields.

        Explicit names may be canonical Excel var_names or Python attr_names.
        Their requested order is preserved.

        Examples
        --------
        selection.select(
            "PV_own_consumption",
            "EUI_self_sufficiency",
        )

        selection.select(
            domain="primary_energy_balance",
            measure="demand",
        )
        """
        if names and filters:
            raise ValueError(
                "Use either explicit variable names or metadata filters, not both."
            )

        if names:
            selected = {meta.attr_name: meta for meta in self._vars}
            result = []

            for name in names:
                attr_name = _resolve_attr_name(name)

                if attr_name not in selected:
                    raise KeyError(
                        f"Variable {name!r} is not part of this selection"
                    )

                result.append(selected[attr_name])

            return VariableSelection(result)

        valid_fields = VariableMeta.__dataclass_fields__

        unknown = [
            field
            for field in filters
            if field not in valid_fields
        ]
        if unknown:
            raise KeyError(
                f"Unknown VariableMeta field(s): {unknown}"
            )

        return VariableSelection(
            meta
            for meta in self._vars
            if all(
                getattr(meta, field) == value
                for field, value in filters.items()
            )
        )

    def by(
        self,
        *,
        source: str | None = None,
        domain: str | None = None,
        measure: str | None = None,
        spatial_scope: str | None = None,
        temporal_scope: str | None = None,
        entity_group: str | None = None,
        entity_key: str | None = None,
        ka: int | None = None,
    ) -> "VariableSelection":
        """
        Convenience wrapper for common semantic metadata filters.
        """
        selection = self

        if source is not None:
            selection = selection.for_source(source)

        filters = {
            "domain": domain,
            "measure": measure,
            "spatial_scope": spatial_scope,
            "temporal_scope": temporal_scope,
            "entity_group": entity_group,
            "entity_key": entity_key,
            "ka": ka,
        }

        return selection.select(
            **{
                key: value
                for key, value in filters.items()
                if value is not None
            }
        )

    def unique(self, field: str) -> list[object]:
        """
        Return distinct non-empty metadata values.

        Order follows first occurrence in canonical schema order.
        """
        if field not in VariableMeta.__dataclass_fields__:
            raise KeyError(
                f"Unknown VariableMeta field: {field!r}"
            )

        result = []

        for meta in self._vars:
            value = getattr(meta, field)

            if value in (None, ""):
                continue

            if value not in result:
                result.append(value)

        return result

    def get(self, var_name: str) -> VariableMeta | None:
        """
        Return metadata for a selected variable by canonical var_name.
        """
        for meta in self._vars:
            if meta.var_name == var_name:
                return meta

        return None

    @property
    def metas(self) -> tuple[VariableMeta, ...]:
        return self._vars

    @property
    def var_names(self) -> list[str]:
        return [meta.var_name for meta in self._vars]

    @property
    def attr_names(self) -> list[str]:
        return [meta.attr_name for meta in self._vars]

    def domains(self) -> list[object]:
        return self.unique("domain")

    def measures(self) -> list[object]:
        return self.unique("measure")

    def entity_groups(self) -> list[object]:
        return self.unique("entity_group")

    def entity_keys(self) -> list[object]:
        return self.unique("entity_key")

    def __iter__(self) -> Iterator[VariableMeta]:
        return iter(self._vars)

    def __len__(self) -> int:
        return len(self._vars)

    def __bool__(self) -> bool:
        return bool(self._vars)
    
    def __getitem__(self, key):
        if isinstance(key, slice):
            return VariableSelection(self._vars[key])
        return self._vars[key]

    def __contains__(self, item) -> bool:
        return item in self._vars

    def __repr__(self) -> str:
        return f"<VariableSelection n={len(self._vars)}>"

class ScenarioSelection:
    """
    Ordered subset of scenarios belonging to one Project.

    Scenario identity is `Scenario.column_name`.

    `.where(...)` filters scenarios by values of schema variables.
    """

    def __init__(
        self,
        project: "Project",
        scenarios=None,
    ):
        self._project = project

        project_scenarios = tuple(project.scenarios)

        if scenarios is None:
            selected = project_scenarios

        else:
            selected = tuple(scenarios)

            project_ids = {
                id(scenario)
                for scenario in project_scenarios
            }

            invalid = [
                scenario.column_name
                for scenario in selected
                if id(scenario) not in project_ids
            ]

            if invalid:
                raise ValueError(
                    "ScenarioSelection contains scenarios "
                    f"not belonging to this project: {invalid}"
                )

        self._scenarios = selected

    @property
    def project(self):
        return self._project

    @property
    def scenarios(self):
        return self._scenarios

    @property
    def column_names(self) -> list[str]:
        return [
            scenario.column_name
            for scenario in self._scenarios
        ]

    def where(self, **variable_values):
        """
        Filter by schema-variable values.

        Example
        -------
        scenarios.where(
            project_name="Forsthausgasse",
            preset_recorded_heating_system="Wärmepumpe",
        )
        """
        resolved = {
            _resolve_attr_name(name): expected
            for name, expected in variable_values.items()
        }

        def matches(scenario):
            return all(
                getattr(
                    scenario.v,
                    attr_name,
                ) == expected
                for attr_name, expected in resolved.items()
            )

        return ScenarioSelection(
            self._project,
            (
                scenario
                for scenario in self._scenarios
                if matches(scenario)
            ),
        )

    def by_columns(
        self,
        *column_names: str,
    ):
        """
        Restrict by exact Excel scenario-column names.
        """
        requested = set(column_names)

        existing = {
            scenario.column_name
            for scenario in self._scenarios
        }

        missing = requested - existing

        if missing:
            raise KeyError(
                f"Unknown scenario column(s): {sorted(missing)}"
            )

        return ScenarioSelection(
            self._project,
            (
                scenario
                for scenario in self._scenarios
                if scenario.column_name in requested
            ),
        )
    
    def unique(
        self,
        variable: str,
        *,
        drop_none: bool = True,
    ) -> list[object]:
        """
        Return distinct values of one schema variable across
        the selected scenarios.

        Order follows first occurrence in project scenario order.
        """
        attr_name = _resolve_attr_name(variable)

        result = []

        for scenario in self._scenarios:
            value = getattr(scenario.v, attr_name)

            if drop_none and value is None:
                continue

            if value not in result:
                result.append(value)

        return result

    def __iter__(self):
        return iter(self._scenarios)

    def __len__(self) -> int:
        return len(self._scenarios)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return ScenarioSelection(
                self._project,
                self._scenarios[key],
            )
        return self._scenarios[key]

    def __contains__(self, item) -> bool:
        return item in self._scenarios

    def __repr__(self):
        return (
            f"<ScenarioSelection "
            f"n={len(self._scenarios)}>"
        )

def _resolve_timeseries_attr_name(
    name: str | TimeseriesMeta,
) -> str:
    """
    Resolve a SIM var_name, generated Python attr_name, or TimeseriesMeta
    to its generated attr_name.
    """
    if isinstance(name, TimeseriesMeta):
        return name.attr_name

    if name in TIMESERIES_ATTR_NAME_MAP:
        return TIMESERIES_ATTR_NAME_MAP[name]

    if name in TIMESERIES_ATTR_NAME_MAP.values():
        return name

    raise KeyError(f"Unknown timeseries variable: {name!r}")


class TimeseriesSelection:
    '''
    Ordered, value-free selection of SIM/timeseries variables.

    Contains TimeseriesMeta objects only; no hourly runtime values.
    '''

    def __init__(self, variables: Iterable[TimeseriesMeta]):
        self._vars = tuple(variables)

    @classmethod
    def all(cls) -> "TimeseriesSelection":
        return cls(
            getattr(TIMESERIES_META, attr_name)
            for attr_name in TIMESERIES_ATTR_NAME_MAP.values()
        )

    def select(
        self,
        *names: str | TimeseriesMeta,
        **filters,
    ) -> "TimeseriesSelection":
        """
        Select explicit SIM variables or filter by TimeseriesMeta fields.

        Examples
        --------
        selection.select("Ta", "Irr_horizontal")

        selection.select(
            pexl.timeseries.Ta,
            pexl.timeseries.Irr_horizontal,
        )

        selection.select(
            domain="🌦️ Wetter",
            measure="Temperatur",
        )
        """
        if names and filters:
            raise ValueError(
                "Use either explicit timeseries names or metadata filters, not both."
            )

        if names:
            selected = {
                meta.attr_name: meta
                for meta in self._vars
            }

            result = []

            for name in names:
                attr_name = _resolve_timeseries_attr_name(name)

                if attr_name not in selected:
                    raise KeyError(
                        f"Timeseries variable {name!r} "
                        "is not part of this selection"
                    )

                result.append(selected[attr_name])

            return TimeseriesSelection(result)

        valid_fields = TimeseriesMeta.__dataclass_fields__

        unknown = [
            field
            for field in filters
            if field not in valid_fields
        ]

        if unknown:
            raise KeyError(
                f"Unknown TimeseriesMeta field(s): {unknown}"
            )

        return TimeseriesSelection(
            meta
            for meta in self._vars
            if all(
                getattr(meta, field) == value
                for field, value in filters.items()
            )
        )

    def unique(self, field: str) -> list[object]:
        if field not in TimeseriesMeta.__dataclass_fields__:
            raise KeyError(
                f"Unknown TimeseriesMeta field: {field!r}"
            )

        result = []

        for meta in self._vars:
            value = getattr(meta, field)

            if value in (None, ""):
                continue

            if value not in result:
                result.append(value)

        return result

    def get(
        self,
        var_name: str,
    ) -> TimeseriesMeta | None:
        for meta in self._vars:
            if meta.var_name == var_name:
                return meta

        return None

    @property
    def metas(self) -> tuple[TimeseriesMeta, ...]:
        return self._vars

    @property
    def var_names(self) -> list[str]:
        return [
            meta.var_name
            for meta in self._vars
        ]

    @property
    def attr_names(self) -> list[str]:
        return [
            meta.attr_name
            for meta in self._vars
        ]

    def domains(self) -> list[object]:
        return self.unique("domain")

    def measures(self) -> list[object]:
        return self.unique("measure")

    def __iter__(self) -> Iterator[TimeseriesMeta]:
        return iter(self._vars)

    def __len__(self) -> int:
        return len(self._vars)

    def __bool__(self) -> bool:
        return bool(self._vars)

    def __getitem__(self, key):
        if isinstance(key, slice):
            return TimeseriesSelection(
                self._vars[key]
            )

        return self._vars[key]

    def __contains__(self, item) -> bool:
        return item in self._vars

    def __repr__(self) -> str:
        return (
            f"<TimeseriesSelection "
            f"n={len(self._vars)}>"
        )
