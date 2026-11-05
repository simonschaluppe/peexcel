"""Resolve current/legacy embodied-emission definitions before materialization.

Current components and totals form one family. A present zero is a current
result; partial current results never borrow legacy values. Legacy detail has
coarser categories, retained as such rather than mapped to individual new parts.
No project values are modified and no Excel formula is evaluated here.
"""
from dataclasses import replace
from collections import Counter
import logging

logger = logging.getLogger(__name__)

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


def _read(row, key):
    return row.get(key)


def _present(value):
    return value is not None and not pd.isna(value)


def resolve(spec, frame):
    """Return resolved spec, row overrides and per-scenario source provenance.

    Unused family columns in mixed *detail* reports are structural zeros. 
    """
    if getattr(spec, 'chart_name', None) not in REPORTS:
        return spec, {}, {}
    from pexl.schema.current import CHARTS, ATTR_NAME_MAP, SCHEMA_META
    current_components = tuple(s.var_name for s in CHARTS['gwp_ee_detail'].series
                               if s.role != 'Balance Variable')
    current_totals = tuple(k for k in ATTR_NAME_MAP if k.startswith('GWP_ee_total'))
    needed = set(current_components + current_totals + LEGACY_CONSTRUCTION + LEGACY_TES)
    needed.update(series.var_name for series in spec.series)
    needed.update(('legacy_GWP_ee_lc_construction', 'legacy_GWP_ee_lc_tga',
                   'legacy_GWP_lc_total', 'legacy_GWP_lc_OE_total',
                   'GWP_ee_lc_mob', 'GWP_lc_OE_total'))
    rows = frame.loc[:, frame.columns.intersection(list(needed))].to_dict(orient='index')
    families = {identity: ('current' if any(_present(_read(row, k))
                for k in (*current_components, *current_totals)) else 'legacy')
                for identity, row in rows.items()}
    if spec.chart_name == 'gwp_ee_fossil_biogenic' and 'legacy' in families.values():
        raise ValueError('Legacy data have no equivalent complete fossil/biogenic TES lifecycle totals; '
                         'use gwp_ee or gwp_ee_detail instead of inferring a split')

    detail = spec.chart_name == 'gwp_ee_detail'
    if detail and 'legacy' in families.values():
        legacy_series = tuple(SeriesSpec(
            var_name=key, label_de='Legacy: ' + (getattr(SCHEMA_META, ATTR_NAME_MAP[key]).label_de or key),
            label_en='Legacy: ' + (getattr(getattr(SCHEMA_META, ATTR_NAME_MAP[key]), "label_en", None) or key),
            role='Baulich', order=i,
            color='#9fd3a2' if key in LEGACY_CONSTRUCTION else '#e9b44c')
            for i, key in enumerate((*LEGACY_CONSTRUCTION, *LEGACY_TES)))
        active = tuple(s for s in spec.series
                       if s.role == 'Balance Variable' or 'current' in families.values())
        spec = replace(spec, series=active + legacy_series)
    if 'legacy' in families.values():
        spec = replace(spec, title=spec.title + ' [Legacy-Fallback enthalten]',
                       title_de=(spec.title_de or spec.title) + ' [Legacy-Fallback enthalten]',
                       title_en=(spec.title_en or spec.title) + ' [legacy fallback included]')

    overrides, provenance = {}, {}
    missing_fields = Counter()
    for identity, scenario in rows.items():
        family = families[identity]
        row, sources = {}, {}

        def required(key):
            value = _read(scenario, key)
            if not _present(value):
                value = float("nan")
                missing_fields[(family, key)] += 1
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
        overrides[identity] = row
        provenance[identity] = dict(family=family, fields=sources)
    for (family, key), count in missing_fields.items():
        logger.warning('missing %s GWP field %r in %d scenario(s); partial current results cannot be mixed with legacy results',
                       family, key, count)
    return spec, overrides, provenance
