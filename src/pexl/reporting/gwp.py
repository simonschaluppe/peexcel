"""Resolve current/legacy embodied-emission definitions before materialization.

Current components and totals form one family. A present zero is a current
result; partial current results never borrow legacy values. Legacy detail has
coarser categories, retained as such rather than mapped to individual new parts.
No project values are modified and no Excel formula is evaluated here.
"""
from dataclasses import replace

import pandas as pd

from .spec import SeriesSpec


REPORTS = frozenset(('gwp_ee', 'gwp_ee_detail', 'district_gwp_ee', 'gwp_ee_fossil_biogenic'))
LEGACY_CONSTRUCTION = (
    'legacy_GWP_ee_lc_walls', 'legacy_GWP_ee_lc_windows',
    'legacy_GWP_ee_lc_roof', 'legacy_GWP_ee_lc_ground',
    'legacy_GWP_ee_lc_ceil', 'legacy_GWP_ee_lc_general',
    'legacy_GWP_ee_lc_other', 'legacy_GWP_ee_lc_direct',
)
LEGACY_TES = (
    'legacy_GWP_ee_lc_pv', 'legacy_GWP_ee_lc_boreholes',
    'legacy_GWP_ee_lc_ventilation', 'legacy_GWP_ee_lc_solarthermal',
    'legacy_GWP_ee_lc_battery', 'legacy_GWP_ee_lc_storage',
    'legacy_GWP_ee_lc_tga_general', 'legacy_GWP_ee_lc_tga_other',
)


def _read(scenario, key):
    from pexl.schema.current import ATTR_NAME_MAP
    value = getattr(scenario.v, ATTR_NAME_MAP.get(key, key), None)
    if value is None or pd.isna(value):
        value = getattr(scenario, 'legacy', {}).get(key)
    return value


def _present(value):
    return value is not None and not pd.isna(value)


def resolve(spec, scenarios):
    """Return resolved spec, row overrides and per-scenario source provenance.

    Unused family columns in mixed *detail* reports are structural zeros. 
    """
    if getattr(spec, 'chart_name', None) not in REPORTS:
        return spec, {}, {}
    from pexl.schema.current import CHARTS, ATTR_NAME_MAP, SCHEMA_META
    current_components = tuple(s.var_name for s in CHARTS['gwp_ee_detail'].series
                               if s.role != 'Balance Variable')
    current_totals = tuple(k for k in ATTR_NAME_MAP if k.startswith('GWP_ee_total'))
    families = {s.column_name: ('current' if any(_present(_read(s, k))
                for k in (*current_components, *current_totals)) else 'legacy')
                for s in scenarios}
    if spec.chart_name == 'gwp_ee_fossil_biogenic' and 'legacy' in families.values():
        raise ValueError('Legacy data have no equivalent complete fossil/biogenic TES lifecycle totals; '
                         'use gwp_ee or gwp_ee_detail instead of inferring a split')

    detail = spec.chart_name == 'gwp_ee_detail'
    if detail and 'legacy' in families.values():
        legacy_series = tuple(SeriesSpec(
            var_name=key, label_de='Legacy: ' + (getattr(SCHEMA_META, ATTR_NAME_MAP[key]).label_de or key),
            role='Baulich', order=i,
            color='#9fd3a2' if key in LEGACY_CONSTRUCTION else '#e9b44c')
            for i, key in enumerate((*LEGACY_CONSTRUCTION, *LEGACY_TES)))
        active = tuple(s for s in spec.series
                       if s.role == 'Balance Variable' or 'current' in families.values())
        spec = replace(spec, series=active + legacy_series)
    if 'legacy' in families.values():
        spec = replace(spec, title=spec.title + ' [Legacy-Fallback enthalten]')

    overrides, provenance = {}, {}
    for scenario in scenarios:
        family = families[scenario.column_name]
        row, sources = {}, {}

        def required(key):
            value = _read(scenario, key)
            if not _present(value):
                value = float("nan")
                print(f'{scenario.column_name}: missing {family} GWP field {key!r}; partial current results cannot be mixed with legacy results')
            return value

        for series in spec.series:
            key = series.var_name
            if detail and ((family == 'current' and key.startswith('legacy_'))
                           or (family == 'legacy' and key in current_components)):
                row[key], sources[key] = 0.0, 'not applicable: other detail family'
                continue
            source = key
            if family == 'legacy':
                source = {
                    'GWP_ee_total_construction': 'legacy_GWP_ee_lc_construction',
                    'GWP_ee_total_TES': 'legacy_GWP_ee_lc_tga',
                    'GWP_lc_total': 'legacy_GWP_lc_total',
                }.get(key, key)
                if key == 'GWP_lc_OE_total' and _present(_read(scenario, 'legacy_GWP_lc_OE_total')):
                    source = 'legacy_GWP_lc_OE_total'
                if key == 'GWP_ee_total':
                    parts = ('legacy_GWP_ee_lc_construction', 'legacy_GWP_ee_lc_tga')
                    row[key] = sum(required(k) for k in parts)
                    sources[key] = 'sum(' + ', '.join(parts) + ')'
                    continue
                if key == 'GWP_lc_total' and not _present(_read(scenario, source)):
                    parts = ('legacy_GWP_ee_lc_construction', 'legacy_GWP_ee_lc_tga',
                             'GWP_ee_lc_mob', 'GWP_lc_OE_total')
                    oe = 'legacy_GWP_lc_OE_total' if _present(_read(scenario, 'legacy_GWP_lc_OE_total')) else parts[-1]
                    parts = (*parts[:-1], oe)
                    row[key] = sum(required(k) for k in parts)
                    sources[key] = 'sum(' + ', '.join(parts) + ')'
                    continue
            row[key], sources[key] = required(source), source
        overrides[scenario.column_name] = row
        provenance[scenario.column_name] = dict(family=family, fields=sources)
    return spec, overrides, provenance
