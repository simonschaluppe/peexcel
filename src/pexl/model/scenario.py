from __future__ import annotations
from dataclasses import fields

from pexl.schema.current import ExcelNamedVariables, VariableMeta, SCHEMA_META, ATTR_NAME_MAP


class ScenarioView:
    """
    Read-only query interface over a Scenario's schema-defined variables.

    A ScenarioView exposes a filtered view of a Scenario's variables together
    with their metadata. It is intended for generic downstream use cases such as:
    - grouping variables by metadata fields
    - selecting subsets of variables
    - plotting and tabular exports
    - scenario-to-scenario comparison

    Parameters
    ----------
    scenario:
        The Scenario instance to read from.
    source:
        Optional source filter:
        - None   -> include all variables
        - "IN"   -> include variables from IN and BOTH
        - "OUT"  -> include variables from OUT and BOTH
    filters:
        -
    """

    def __init__(self, scenario: "Scenario", source: str | None = None, filters=None):
        self._s = scenario
        self._source = source
        self._filters = filters or {}

    def _iter_items(self):
        """
        Yield (meta, value) pairs in canonical schema order.
        """
        for var_name, attr_name in ATTR_NAME_MAP.items():
            meta = getattr(self._s.meta, attr_name)

            if self._source is not None and meta.source not in (self._source, "BOTH"):
                continue

            # metadata filters
            ok = True
            for k, v in self._filters.items():
                if getattr(meta, k, None) != v:
                    ok = False
                    break
            if not ok:
                continue

            value = getattr(self._s.v, attr_name)
            yield meta, value

    def __getattr__(self, attr_name):
        for meta, value in self._iter_items():
            if meta.attr_name == attr_name:
                return value
        raise AttributeError(f"{attr_name} not in this ScenarioView")

    def unique(self, field: str) -> list[str]:
        vals = {
            getattr(meta, field)
            for meta, _ in self._iter_items()
            if getattr(meta, field, None) not in (None, "")
        }
        return sorted(vals)
    
    def domains(self) -> list[str]:
        return self.unique("domain")

    def entity_groups(self) -> list[str]:
        return self.unique("entity_group")

    def entity_keys(self) -> list[str]:
        return self.unique("entity_key")

    def measures(self) -> list[str]:
        return self.unique("measure")

    def by(
        self,
        *,
        domain: str | None = None,
        entity_group: str | None = None,
        entity_key: str | None = None,
        measure: str | None = None,
    ) -> "ScenarioView":
        """
        Return a new ScenarioView filtered by semantic metadata fields.

        This is the primary method for refining a view. All provided filters are
        combined with logical AND and matched by exact equality against the
        metadata (`VariableMeta`) of each variable.

        Parameters
        ----------
        domain: 
            High-level semantic family of the variable (e.g. "GFA", "NFA_to_GFA").
        entity_group: 
            Repeating entity group:
            usage, hull, component, mobility, heating, cooling, dhw, energy_carrier

        entity_key:
            Specific member within an entity group (e.g. "residential", "office").
        measure:
            Type of quantity (e.g. "area", "ratio").

        Returns
        -------
        ScenarioView
            A new filtered view that can be further refined or materialized.

        Examples
        --------
        `scenario.out.by(entity_group="usage")`

        `scenario.inn.by(entity_group="usage", entity_key="residential")`

        `scenario.inn.by(domain="GFA", measure="area")`

        Notes
        -----
        - Filters are applied cumulatively and can be chained.
        - Only exact matches are supported.
        - This method does not materialize data; use `items_dict()` or
        `to_var_dict()` to extract values.
        """
        filters = dict(self._filters)

        if domain is not None:
            filters["domain"] = domain
        if entity_group is not None:
            filters["entity_group"] = entity_group
        if entity_key is not None:
            filters["entity_key"] = entity_key
        if measure is not None:
            filters["measure"] = measure

        return ScenarioView(self._s, source=self._source, filters=filters)

    def items(self):
        """
        Public iterator over (meta, value) pairs.

        Returns
        -------
        iterator
            Iterator yielding `(VariableMeta, value)` tuples.
        """
        return self._iter_items()


    def items_dict(self) -> dict:
        return {meta: value for meta, value in self._iter_items()}

    def to_var_dict(self) -> dict[str, object]:
        return {meta.var_name: value for meta, value in self._iter_items()}

    def metas(self):
        return [meta for meta, _ in self._iter_items()]

    def values(self):
        return [value for _, value in self._iter_items()]

    def __repr__(self) -> str:
        count = sum(1 for _ in self._iter_items())
        parts = [f"ScenarioView({self._s.name!r}", f"n={count}"]
        if self._source:
            parts.append(f"source={self._source}")
        if self._filters:
            filt = ", ".join(f"{k}={v!r}" for k, v in self._filters.items())
            parts.append(f"filters={{ {filt} }}")
        return "<" + ", ".join(parts) + ")>"
    

class Scenario:
    """
    Represents a single scenario within a district.
    Parent district is implied via scenario.v.project_name -> District name

    Attributes
    ----------
    name:
        Scenario name.
    v:
        Container holding all schema variables as Python attributes.
    meta:
        Shared schema metadata object for all variables.

    Notes
    -----
    Variable values and metadata can be accessed via dot-notation:
        scenario.v.QH
        scenario.meta.QH.unit

    This is the primary interface when the caller already knows
    the variable they want.

    The properties `view`, `inn`, and `out` provide generic access for
    downstream tooling that needs to inspect variables systematically.
    """

    def __init__(self, name: str):
        self.name = name
        self.v = ExcelNamedVariables()
        self.meta = SCHEMA_META
        # TODO: attach timestep data container here, e.g. self.sim = None

    def __repr__(self) -> str:
        return f"<Scenario {self.name!r}>"

    def as_dict(self) -> dict:
        """
        Flat dict of all v.* values keyed by Python attribute name.

        Returns
        -------
        dict
            Mapping `{attr_name: value}` from the runtime values container.
        """
        return vars(self.v)

    def to_var_dict(self) -> dict[str, object]:
        """
        Export all scenario values keyed by canonical Excel var_name.

        Returns
        -------
        dict[str, object]
            Mapping `{var_name: value}` for the full scenario.
        """
        out: dict[str, object] = {}

        for var_name, attr_name in ATTR_NAME_MAP.items():
            out[var_name] = getattr(self.v, attr_name)

        return out

    @property
    def view(self) -> ScenarioView:
        """
        Return an unfiltered ScenarioView over all schema variables.
        """
        return ScenarioView(self)

    @property
    def out(self) -> ScenarioView:
        """
        Return a ScenarioView restricted to output variables.
        """
        return ScenarioView(self, source="OUT")

    @property
    def inn(self) -> ScenarioView:
        """
        Return a ScenarioView restricted to input variables.
        """
        return ScenarioView(self, source="IN")