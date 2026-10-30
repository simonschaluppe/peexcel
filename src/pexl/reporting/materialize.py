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


def materialize(source, chart_name: str, *, language="de", unit=None) -> dict[str, Any]:
    """Materialize a chart for a Project, Scenario, ProjectView, or ScenarioView."""
    from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META, SCHEMA_VERSION
    from pexl.i18n import PRIMARY_ENERGY_LABELS, chart_text
    from pexl.model.project import Project
    from pexl.model.scenario import Scenario
    from pexl.model.view import ProjectView, ScenarioView

    if language not in ("de", "en"):
        raise ValueError("language must be 'de' or 'en'")

    if isinstance(source, Scenario):
        scenarios = (source,)
    elif isinstance(source, ScenarioView):
        scenarios = (source.scenario,)
    elif isinstance(source, (Project, ProjectView)):
        scenarios = tuple(source.scenarios)
    else:
        raise TypeError(
            "source must be a Project, Scenario, ProjectView, or ScenarioView"
        )

    charts = _chart_registry()
    try:
        spec = charts[chart_name]
    except KeyError as exc:
        raise KeyError(
            f"Unknown chart {chart_name!r}. Available: {', '.join(charts)}"
        ) from exc

    from .gwp import resolve
    spec, overrides, provenance = resolve(spec, scenarios)
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

    rows = []
    for scenario in scenarios:
        version = getattr(scenario.v, 'tool_version', None)
        if version is not None and str(version).replace('.', '_').replace('-', '_') != SCHEMA_VERSION:
            raise ValueError(f'{scenario.column_name}: model version {version!r} does not match active schema {SCHEMA_VERSION!r}')
        row = {"Variant": scenario.column_name}
        for item in series:
            attr_name = ATTR_NAME_MAP[item["var_name"]]
            row[item["var_name"]] = overrides.get(scenario.column_name, {}).get(
                item["var_name"], getattr(scenario.v, attr_name))
        rows.append(row)

    frame = pd.DataFrame(rows, columns=["Variant", *[s["var_name"] for s in series]])
    if chart_name == "primary_energy_balance":
        legacy_density = {
            scenario.column_name: scenario.legacy.get("PEI_cf_density")
            for scenario in scenarios
        }
        density = pd.to_numeric(
            frame["Variant"].map(legacy_density),
            errors="raise",
        )

        for column, fallback in {
            "PEI_cf_density_pos": density.clip(lower=0),
            "PEI_cf_density_neg": (-density).clip(lower=0),
        }.items():
            if column in frame:
                frame[column] = frame[column].fillna(fallback)
                
    units = {s["unit"] for s in series if s["unit"] not in (None, "")}

    report = {
        "chart_name": _field(spec, "chart_name", chart_name) or chart_name,
        "tab_name": _field(spec, "tab_name"),
        "title": _field(spec, "title", chart_name) or chart_name,
        "chart_type": _field(spec, "chart_type"),
        "unit": next(iter(units)) if len(units) == 1 else None,
        "series": series,
        "frame": frame,
        "language": language,
        "value_mode": "magnitude" if _field(spec, "chart_type") == "stacked_bar_comparison" else "signed",
    }
    if provenance:
        report['sources'] = provenance
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
