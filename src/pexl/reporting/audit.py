"""Audit tables from existing annual values; no simulation or certification.

The report, not the importer, owns these variable requirements. Missing optional
values remain visible. The import/export balance is mandatory and checked.
All functions accept the same DataFrame/model sources as reporting.variables.
"""
from __future__ import annotations

import math
import numbers

import pandas as pd

from ._data import annual_frame

_USES = ('residential', 'office', 'schoolsec', 'schoolprim', 'retailfood', 'retailother', 'other')
_DIRECTIONS = ('north', 'east', 'south', 'west', 'horizontal')
_BALANCE = ('PEI_import', 'PEI_export', 'PEI_saldo_project', 'PEI_saldo_target', 'PEI_importExport_balance')

# Ordered report requirements. Names/units are resolved only when a table is used.
TABLES = {
    'project': ('project_name', 'location_name', 'location_address', 'location_postcode'),
    'geometry': ('plot_area', 'GFA_total', 'NFA_total', 'FSI', 'renovation_share'),
    'model': ('tool_version', 'input_version_number', 'project_scenario_name', 'weather_name'),
    'balance': _BALANCE,
    'pv': ('PV_kWp', 'PV_total', 'PV_profile_name', 'PV_simplified_name', 'PV_mode', 'PV_roof_share', 'hull_roof_m2', 'PV_efficiency'),
    'flexibility': ('FLEX_PV_is_used', 'FLEX_is_used', 'FLEX_signal_name', 'FLEX_grid_maxpower_Wm2', 'FLEX_is_used_for_plugloads', 'FLEX_is_used_for_HVAC_min', 'FLEX_is_used_for_ev_min', 'flex_heat_dT', 'FLEX_choice_heat_system', 'flex_cool_dT', 'FLEX_choice_cool_system', 'flex_dhw_use', 'DHW_Tmax', 'Batt_is_used', 'Batt_cap_kWh', 'Batt_is_gridcharged', 'ev_bidirectional_use', 'PEI_sub_flex'),
    'opaque': ('hull_ext_wall_wo_window_m2', 'hull_transmittance_walls', 'hull_roof_m2', 'hull_transmittance_roof', 'hull_fundament_m2', 'hull_transmittance_fundament'),
    'windows': tuple(f'hull_windows_{d}_m2' for d in _DIRECTIONS) + tuple(f'hull_transmittance_windows_{d}' for d in _DIRECTIONS) + tuple(f'window_total_transmittance_{d}' for d in _DIRECTIONS),
    'hull': ('illuminance_efficiency_glazing_ratio', 'hull_transmittance_heatbridge', 'vent_air_tightness', 'heat_capacity_effective_m2'),
    'shading': tuple(f'window_irradiation_factor_{season}_{d}' for season in ('winter', 'summer') for d in _DIRECTIONS),
    'mobile_shading': tuple(f'{prefix}_{u}' for u in _USES for prefix in ('fc', 'illuminance_min')),
    'heating': ('preset_recorded_heating_system', 'heat_cop_1el', 'heat_cop_2th', 'heat_cop_3el', 'heat_cop_4th', 'heat_th2_carrier_type', 'heat_th4_carrier_type'),
    'cooling': ('preset_recorded_cooling_system', 'cool_cop_1el', 'cool_cop_2th', 'cool_cop_3el', 'cool_th2_carrier_type') + tuple(f'cool_share_{u}' for u in _USES),
    'dhw': tuple(f'DHW_{suffix}' for suffix in ('carriertype_1', '1_efficiency', 'efficiency_distribution_1', 'losses_1', '1_el_aux', 'carriertype_2', '2_efficiency', 'efficiency_distribution_2', 'losses_2', '2_el_aux')),
    'dhw_storage': ('DHW_storage_liter_pPerson', 'DHW_storage_env_temp_default', 'DHW_Tmin', 'DHW_Tmax', 'DHW_storage_1_liter', 'DHW_storage_2_liter'),
    'ventilation': tuple(f'{prefix}_{u}' for u in _USES for prefix in ('vent_ach_max', 'vent_share_mechanical', 'vent_heat_recovery_winter', 'vent_heat_recovery_summer')),
    'demand': ('Tsetheat_min', 'Tsetcool_max') + tuple(f'plugloads_{u}' for u in _USES) + tuple(f'DHW_demand_{u}_kWhm2' for u in _USES),
}
TABLES['heating'] += tuple(f'{prefix}_{s}' for s in ('1el', '2th', '3el', '4th') for prefix in ('QH_distr_loss', 'QH_aux_el_to_th'))
TABLES['cooling'] += tuple(f'{prefix}_{s}' for s in ('1el', '2th', '3el') for prefix in ('QC_distr_losses', 'QC_aux'))


def select_scenario(source, scenario=None):
    """Return exactly one annual row; never guess or substring-match a name."""
    frame = annual_frame(source)
    if scenario is not None:
        if scenario not in frame.index:
            raise ValueError(f'Unknown scenario {scenario!r}. Available: {list(frame.index)!r}')
        frame = frame.loc[[scenario]].copy()
    if len(frame) != 1:
        raise ValueError('Audit requires exactly one explicitly selected scenario')
    return frame


def _finite(value):
    return isinstance(value, numbers.Real) and not isinstance(value, bool) and math.isfinite(value)


def table(source, name, *, scenario=None):
    """Return Parameter/Wert/Einheit plus raw var_name for traceability.

    Raw values and schema units are preserved, including dimensionless COPs.
    Missing data is NaN, never zero. ``attrs['missing']`` lists missing fields.
    Balance values must be finite and agree to 0.05 kWhPE/(m²NGF a).
    """
    from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META
    selected = select_scenario(source, scenario)
    names = TABLES[name]
    row = selected.iloc[0]
    if name == 'balance':
        missing = [n for n in names if not _finite(row.get(n))]
        if missing:
            raise ValueError(f'Incomplete primary-energy balance: {missing}')
        if not math.isclose(row.PEI_export - row.PEI_import, row.PEI_saldo_project, abs_tol=.05):
            raise ValueError('Inconsistent primary-energy balance: export - import != project')
        if not math.isclose(row.PEI_saldo_project - row.PEI_saldo_target, row.PEI_importExport_balance, abs_tol=.05):
            raise ValueError('Inconsistent primary-energy balance: project - target != difference')
    records = []
    for var in names:
        meta = getattr(SCHEMA_META, ATTR_NAME_MAP.get(var, ''), None)
        records.append({'Parameter': getattr(meta, 'label_de', None) or var,
                        'Wert': row.get(var, float('nan')),
                        'Einheit': getattr(meta, 'unit', None) or '', 'var_name': var})
    if name == 'pv':
        yield_specific, area, power = (row.get(n) for n in ('PV_total', 'NFA_total', 'PV_kWp'))
        annual = yield_specific * area if all(_finite(v) for v in (yield_specific, area)) and area > 0 else float('nan')
        records[2:2] = [
            {'Parameter': 'Jahresertrag (aus PV_total × NFA_total)', 'Wert': annual / 1000,
             'Einheit': 'MWh/a', 'var_name': 'PV_total * NFA_total / 1000'},
            {'Parameter': 'Spezifischer PV-Ertrag', 'Wert': annual / power if _finite(power) and power > 0 else float('nan'),
             'Einheit': 'kWh/(kWp a)', 'var_name': 'PV_total * NFA_total / PV_kWp'},
        ]
    result = pd.DataFrame(records)
    result.attrs['missing'] = [r['var_name'] for r in records if pd.isna(r['Wert']) or (isinstance(r['Wert'], numbers.Real) and not math.isfinite(r['Wert']))]
    result.attrs['scenario'] = selected.index[0]
    return result


def chart(source, name, *, scenario=None):
    """Use existing schema reports; add only the audit-specific use/flex plots."""
    import plotly.graph_objects as go
    from .materialize import materialize
    from pexl.plot.reports import render
    selected = select_scenario(source, scenario)
    row = selected.iloc[0]
    if name == 'usage':
        names = [f'NFA_{u}' for u in _USES]
        values = [row.get(n) for n in names]
        if not all(_finite(v) and v >= 0 for v in values) or sum(values) <= 0:
            raise ValueError('Usage chart requires non-negative NFA values for all uses')
        labels = ['Wohnen', 'Büro und Gewerbe', 'Bildung sekundär', 'Kindergarten und Volksschule', 'Lebensmittelhandel', 'Handel Sonstige', 'Sonstige Nutzung']
        fig = go.Figure(go.Pie(labels=labels, values=values, textinfo='percent', sort=False))
        fig.update_layout(title='Nutzungsmix nach Nettogrundfläche', height=420)
        return fig
    if name == 'flexibility':
        groups = {'Flexible Direktdeckung': ['VRGrid_to_plugloads', 'VRGrid_to_Eh_min', 'VRGrid_to_Ec_min', 'VRGrid_to_Edhw_min', 'VRGrid_to_Ev_min', 'VRGrid_to_Eev_min'],
                  'Flexible Speicherung': ['VRGrid_to_Eh_flex', 'VRGrid_to_Ec_flex', 'VRGrid_to_Edhw_flex', 'VRGrid_to_Batt', 'VRGrid_to_Eev_flex']}
        from ._data import variable_label
        fig = go.Figure()
        for group, names in groups.items():
            for var in names:
                if not _finite(row.get(var)):
                    raise ValueError(f'Incomplete flexibility chart: {var}')
                fig.add_bar(y=[group], x=[row[var]], name=variable_label(var, 'de').split(' [')[0], orientation='h')
        fig.update_layout(barmode='stack', title='Flexible Deckung im Quartier', xaxis_title='kWh/(m²NGF a)', height=650, legend=dict(orientation='h', y=-.25))
        return fig
    return render(materialize(selected, name, language='de'))


def data_notes(source, *, scenario=None):
    """Visible model/schema provenance; no implicit migration or certification."""
    from pexl.schema.current import SCHEMA_VERSION
    row = select_scenario(source, scenario).iloc[0]
    version = str(row.get('tool_version', 'unbekannt'))
    notes = [f'PEQ-Nachweistool: {version}; Reporting-Schema: {SCHEMA_VERSION}.']
    if version.replace('.', '_').replace('-', '_') != SCHEMA_VERSION:
        notes.append('Achtung: Toolversion und Reporting-Schema weichen ab. Zuordnung und Ergebnisse fachlich prüfen; keine automatische Migration.')
    notes.append('Ausgewiesene Werte sind gespeicherte Modellergebnisse. Eine rechnerische Zielerreichung ersetzt keine Plausibilitätsprüfung oder Deklarationsfreigabe.')
    return notes
