from __future__ import annotations

from collections.abc import Iterable

import pandas as pd

from pexl.schema.current import (
    TIMESERIES_ATTR_NAME_MAP,
    TIMESERIES_META,
)

from .selection import TimeseriesSelection


_VAR_NAME_BY_ATTR = {
    attr_name: var_name
    for var_name, attr_name in TIMESERIES_ATTR_NAME_MAP.items()
}


class ScenarioTimeseries:
    """
    Timeseries data belonging to one PEExcel Scenario.

    The underlying data is a pandas DataFrame whose columns use
    canonical SIM var_name values.

    Examples
    --------
    scenario.timeseries.Ta

    scenario.timeseries["Ta"]

    scenario.timeseries.select(
        "Ta",
        "Irr_horizontal",
    )

    scenario.timeseries.select(
        domain="Wetter",
    )
    """

    def __init__(
        self,
        data: pd.DataFrame | None = None,
    ):
        self._data = (
            data.copy()
            if data is not None
            else pd.DataFrame()
        )

        self.meta = TIMESERIES_META

        available = set(self._data.columns)

        self._variables = TimeseriesSelection(
            meta
            for meta in TimeseriesSelection.all()
            if meta.var_name in available
        )

    @classmethod
    def empty(cls) -> "ScenarioTimeseries":
        return cls()

    @property
    def available(self) -> bool:
        return not self._data.empty

    @property
    def variables(self) -> TimeseriesSelection:
        """
        Timeseries variables actually present in this dataset.
        """
        return self._variables

    @property
    def shape(self) -> tuple[int, int]:
        return self._data.shape

    @property
    def columns(self) -> list[str]:
        return list(self._data.columns)

    @property
    def unknown_columns(self) -> list[str]:
        """
        DataFrame columns not present in the generated SIM schema.
        """
        known = set(TIMESERIES_ATTR_NAME_MAP)

        return [
            column
            for column in self._data.columns
            if column not in known
        ]

    def select(
        self,
        *names: str,
        **filters,
    ) -> pd.DataFrame:
        """
        Select timeseries columns.

        Either give explicit SIM variable names:

            timeseries.select(
                "Ta",
                "Irr_horizontal",
            )

        or filter by TimeseriesMeta fields:

            timeseries.select(
                domain="Wetter",
                measure="Temperatur",
            )

        Returns
        -------
        pandas.DataFrame
        """
        selection = self._variables.select(
            *names,
            **filters,
        )

        return self._data.loc[
            :,
            selection.var_names,
        ].copy()

    def to_frame(
        self,
        *,
        copy: bool = True,
    ) -> pd.DataFrame:
        """
        Return the complete timeseries DataFrame.
        """
        if copy:
            return self._data.copy()

        return self._data

    def domains(self) -> list[object]:
        return self._variables.domains()

    def measures(self) -> list[object]:
        return self._variables.measures()

    def __getitem__(
        self,
        key: str | Iterable[str],
    ):
        """
        Pandas-style access.

        timeseries["Ta"]
            -> Series

        timeseries[["Ta", "Irr_horizontal"]]
            -> DataFrame
        """
        if isinstance(key, str):
            var_name = self._resolve_var_name(key)
            return self._data[var_name]

        var_names = [
            self._resolve_var_name(name)
            for name in key
        ]

        return self._data[var_names]

    def __getattr__(self, attr_name: str):
        """
        Attribute access to generated SIM variables.

        Example
        -------
        scenario.timeseries.Ta
        """
        var_name = _VAR_NAME_BY_ATTR.get(attr_name)

        if var_name is not None:
            if var_name not in self._data.columns:
                raise AttributeError(
                    f"Timeseries variable {var_name!r} "
                    "exists in the schema but is not loaded "
                    "for this scenario."
                )

            return self._data[var_name]

        raise AttributeError(
            f"{attr_name!r} is not a timeseries variable"
        )

    def __dir__(self):
        """
        Include generated SIM attr_names in interactive completion.
        """
        available_attrs = {
            TIMESERIES_ATTR_NAME_MAP[var_name]
            for var_name in self._data.columns
            if var_name in TIMESERIES_ATTR_NAME_MAP
        }

        return sorted(
            set(super().__dir__())
            | available_attrs
        )

    def __len__(self) -> int:
        return len(self._data)

    def __repr__(self) -> str:
        return (
            f"<ScenarioTimeseries "
            f"rows={len(self._data)} "
            f"variables={len(self._variables)}>"
        )

    def _repr_html_(self) -> str:
        header = (
            "<b>ScenarioTimeseries</b>"
            f"<br>{len(self._data)} rows × "
            f"{len(self._variables)} schema variables"
        )

        if self._data.empty:
            return header + "<br><i>No timeseries data loaded.</i>"

        return (
            header
            + self._data.to_html(
                max_rows=10,
                max_cols=12,
            )
        )

    @staticmethod
    def _resolve_var_name(name: str) -> str:
        """
        Accept canonical var_name or generated attr_name.
        """
        if name in TIMESERIES_ATTR_NAME_MAP:
            return name

        if name in _VAR_NAME_BY_ATTR:
            return _VAR_NAME_BY_ATTR[name]

        raise KeyError(
            f"Unknown timeseries variable: {name!r}"
        )