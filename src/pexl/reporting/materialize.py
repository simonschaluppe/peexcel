from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import pandas as pd


def _field(obj: object, name: str, default=None):
    """Read a field from either a generated dict or dataclass-like object."""
    if isinstance(obj, Mapping):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _chart_registry():
    """Return the active generated chart registry from ``pexl.schema.current``."""
    from pexl.schema import current

    charts = getattr(current, "CHARTS", None)
    if charts is None:
        raise ImportError(
            "The active schema does not export CHARTS. "
            "Ensure pexl.schema.current also imports the generated reports module."
        )
    return charts


def chart_names() -> tuple[str, ...]:
    """Return chart names from the active generated reporting schema."""
    return tuple(_chart_registry())


def materialize(view, chart_name: str) -> dict[str, Any]:
    """Materialize one generated chart definition for the scenarios in a ProjectView.

    The returned dictionary is renderer-neutral. It contains chart metadata,
    ordered series metadata, and a DataFrame with one row per selected scenario.
    """
    from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META

    charts = _chart_registry()
    try:
        spec = charts[chart_name]
    except KeyError as exc:
        raise KeyError(
            f"Unknown chart {chart_name!r}. Available: {', '.join(charts)}"
        ) from exc

    raw_series = list(_field(spec, "series", ()) or ())
    raw_series.sort(key=lambda s: _field(s, "order", 0) or 0)

    series: list[dict[str, Any]] = []
    for item in raw_series:
        var_name = _field(item, "var_name")
        if not var_name:
            raise ValueError(f"Chart {chart_name!r} contains a series without var_name")

        attr_name = ATTR_NAME_MAP.get(var_name)
        if attr_name is None:
            raise KeyError(
                f"Chart {chart_name!r} references unknown variable {var_name!r}"
            )

        variable_meta = getattr(SCHEMA_META, attr_name)
        series.append(
            {
                "var_name": var_name,
                "label": _field(item, "label_de") or variable_meta.label_de or var_name,
                "role": _field(item, "role"),
                "order": _field(item, "order", 0) or 0,
                "color": _field(item, "color"),
                "pattern": _field(item, "pattern"),
                "unit": variable_meta.unit,
            }
        )

    rows = []
    for scenario in view.scenarios:
        row = {"Variant": scenario.column_name}
        for item in series:
            attr_name = ATTR_NAME_MAP[item["var_name"]]
            row[item["var_name"]] = getattr(scenario.v, attr_name)
        rows.append(row)

    frame = pd.DataFrame(rows, columns=["Variant", *[s["var_name"] for s in series]])
    units = {s["unit"] for s in series if s["unit"] not in (None, "")}

    return {
        "chart_name": _field(spec, "chart_name", chart_name) or chart_name,
        "tab_name": _field(spec, "tab_name"),
        "title": _field(spec, "title", chart_name) or chart_name,
        "chart_type": _field(spec, "chart_type"),
        "unit": next(iter(units)) if len(units) == 1 else None,
        "series": series,
        "frame": frame,
    }