from __future__ import annotations

from collections.abc import Mapping
from typing import Any

import logging

import pandas as pd

logger = logging.getLogger(__name__)


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


def materialize(source, chart_name: str, *, language="de", unit=None) -> dict[str, Any]:
    """Prepare a named annual report from a DataFrame or model object.

    Parameters
    ----------
    source : pandas.DataFrame, Project, Scenario, ProjectView or ScenarioView
        Annual values with canonical ``var_name`` columns. DataFrames may carry
        ``batch`` and ``scenario_name`` columns, a ``column_name`` column, or a
        unique index. Only the report's dependencies are interpreted; additional
        columns are allowed. Input values and row order are preserved.
    chart_name : str
        Name returned by :func:`chart_names`.
    language : {"de", "en"}
        Language of titles and series labels, with German/canonical fallbacks.
    unit : str, optional
        Compatible Wh/kWh/MWh unit including the same reference quantity.

    Returns
    -------
    dict
        Editable ``frame``, ``series``, title, unit and renderer metadata.
        Missing columns are logged and represented by NaN, never by zero.
        Renderers can reject incomplete numerical reports. Model-version
        differences produce a warning; this function performs no migration.
    """
    from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META, SCHEMA_VERSION
    from pexl.i18n import PRIMARY_ENERGY_LABELS, chart_text
    from ._data import annual_frame, display_names

    chart_text("value", language)
    values = annual_frame(source)
    if "tool_version" in values:
        versions = values["tool_version"].dropna().astype(str).unique()
        older = [v for v in versions if v.replace(".", "_").replace("-", "_") != SCHEMA_VERSION]
        if older:
            logger.warning("Report %s uses schema %s; source versions %s need interpretation with care",
                           chart_name, SCHEMA_VERSION, older)

    charts = _chart_registry()
    try:
        spec = charts[chart_name]
    except KeyError as exc:
        raise KeyError(
            f"Unknown chart {chart_name!r}. Available: {', '.join(charts)}"
        ) from exc

    from .gwp import resolve
    spec, overrides, provenance = resolve(spec, values)
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
                "label": (PRIMARY_ENERGY_LABELS[var_name].get(language)
                          if var_name in PRIMARY_ENERGY_LABELS else
                          _field(item, f"label_{language}") or
                          getattr(variable_meta, f"label_{language}", None) or
                          _field(item, "label_de") or variable_meta.label_de or var_name),
                "role": _field(item, "role"),
                "order": _field(item, "order", 0) or 0,
                "color": _field(item, "color"),
                "pattern": _field(item, "pattern"),
                "unit": variable_meta.unit,
            }
        )

    names = list(dict.fromkeys(item["var_name"] for item in series))
    missing = [name for name in names if name not in values]
    if missing:
        logger.warning("Report %s: missing columns represented as NaN: %s", chart_name, missing)
    frame = values.reindex(columns=names).copy()
    for identity, resolved in overrides.items():
        for name, value in resolved.items():
            frame.at[identity, name] = value
    if chart_name == "primary_energy_balance":
        density = pd.to_numeric(values.get("PEI_cf_density", pd.Series(index=values.index, dtype=float)), errors="coerce")
        for column, fallback in {
            "PEI_cf_density_pos": density.clip(lower=0),
            "PEI_cf_density_neg": (-density).clip(lower=0),
        }.items():
            if column in frame:
                frame[column] = frame[column].fillna(fallback)
    frame.insert(0, "Variant", display_names(values))
    # Report renderers and existing consumers expect a positional frame.
    frame = frame.reset_index(drop=True)

    units = {s["unit"] for s in series if s["unit"] not in (None, "")}

    report = {
        "chart_name": _field(spec, "chart_name", chart_name) or chart_name,
        "tab_name": _field(spec, "tab_name"),
        "title": (_field(spec, f"title_{language}") or _field(spec, "title_de")
                  or _field(spec, "title", chart_name) or chart_name),
        "chart_type": _field(spec, "chart_type"),
        "unit": next(iter(units)) if len(units) == 1 else None,
        "series": series,
        "frame": frame,
        "language": language,
        "value_mode": "magnitude" if _field(spec, "chart_type") == "stacked_bar_comparison" else "signed",
    }
    if provenance:
        report['sources'] = dict(zip(display_names(values), (provenance[key] for key in values.index)))
        # District overview components use the boundary of the lifecycle total.
        # Embodied-only reports retain their separate A-unit metadata.
        if chart_name in ('gwp_ee', 'district_gwp_ee'):
            report['unit'] = getattr(SCHEMA_META, ATTR_NAME_MAP['GWP_lc_total']).unit
    if chart_name == 'primary_energy_balance':
        report['title'] = chart_text('primary_energy', language)
    return convert_unit(report, unit) if unit is not None else report


def convert_unit(report, unit):
    """Copy a report, converting Wh/kWh/MWh prefixes with identical reference units.

    No implicit area, time or primary-energy conversion. For those operations
    prepare explicit values and metadata first. Every series must share a unit.
    """
    from copy import deepcopy
    import re
    source = report.get('unit')
    pattern = r'^(MWh|kWh|Wh)(.*)$'
    old, new = re.match(pattern, source or ''), re.match(pattern, unit or '')
    if not old or not new or old.group(2) != new.group(2):
        raise ValueError(f'Incompatible units: {source!r} -> {unit!r}; reference must remain unchanged')
    result = deepcopy(report)
    scales = {'Wh': 1, 'kWh': 1000, 'MWh': 1000000}
    factor = scales[old.group(1)] / scales[new.group(1)]
    converted = set()
    for series in result['series']:
        if series.get('unit') != source:
            raise ValueError('All report series must have the same explicit unit')
        key = series['var_name']
        if key not in converted:
            result['frame'][key] = pd.to_numeric(result['frame'][key], errors='raise') * factor
            converted.add(key)
        series['unit'] = unit
    result['unit'] = unit
    return result
