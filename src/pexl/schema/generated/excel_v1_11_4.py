"""Auto-generated schema bindings. Do not edit manually!"""

from __future__ import annotations
from dataclasses import dataclass

SCHEMA_VERSION = 'v1_11_4'

@dataclass(frozen=True)
class VariableMeta:
    var_name: str
    attr_name: str
    icon: str | None = None
    label_de: str | None = None
    unit: str | None = None
    comment: str | None = None
    source: str | None = None
    ka: int | None = None
    domain: str | None = None
    measure: str | None = None
    spatial_scope: str | None = None
    temporal_scope: str | None = None
    entity_group: str | None = None
    entity_key: str | None = None

    def __repr__(self) -> str:
        parts = []

        if self.icon:
            parts.append(self.icon)

        parts.append(self.var_name)

        if self.unit:
            parts.append(f"[{self.unit}]")

        if self.source:
            parts.append(f"@{self.source}")

        return "<VarMeta " + " ".join(parts) + ">"


class ExcelNamedVariables:
    def __init__(self):
        self.scenario_version: object | None = None
        self.input_version_number: object | None = None
        self.input_version_date: object | None = None
        self.cfd_fPE: object | None = None
        self.cfd_A: object | None = None
        self.cfd_dx: object | None = None
        self.cfd_EUI: object | None = None
        self.cfd_cutoff: object | None = None
        self.cfm_budget_residential: object | None = None
        self.cfm_budget_office: object | None = None
        self.cfm_budget_school: object | None = None
        self.cfm_budget_retail: object | None = None
        self.cfr_budget: object | None = None
        self.project_name: object | None = None
        self.project_url: object | None = None
        self.location_address: object | None = None
        self.municipality_name: object | None = None
        self.project_creation_date: object | None = None
        self.project_description: object | None = None
        self.project_scenario_name: object | None = None
        self.location_postcode: object | None = None
        self.mobility_mode: object | None = None
        self.weather_name: object | None = None
        self.weather_index: object | None = None
        self.GFA_residential: object | None = None
        self.GFA_office: object | None = None
        self.GFA_schoolsec: object | None = None
        self.GFA_schoolprim: object | None = None
        self.GFA_retailfood: object | None = None
        self.GFA_retailother: object | None = None
        self.GFA_other: object | None = None
        self.GFA_total: object | None = None
        self.NFA_to_GFA_ratio_residential: object | None = None
        self.NFA_to_GFA_ratio_office: object | None = None
        self.NFA_to_GFA_ratio_schoolsec: object | None = None
        self.NFA_to_GFA_ratio_schoolprim: object | None = None
        self.NFA_to_GFA_ratio_retailfood: object | None = None
        self.NFA_to_GFA_ratio_retailother: object | None = None
        self.NFA_to_GFA_ratio_other: object | None = None
        self.NFA_to_GFA_ratio: object | None = None
        self.NFA_residential: object | None = None
        self.NFA_office: object | None = None
        self.NFA_schoolsec: object | None = None
        self.NFA_schoolprim: object | None = None
        self.NFA_retailfood: object | None = None
        self.NFA_retailother: object | None = None
        self.NFA_other: object | None = None
        self.NFA_total: object | None = None
        self.per_NFA: object | None = None
        self.plot_area: object | None = None
        self.FSI: object | None = None
        self.renovation_ratio_residential: object | None = None
        self.renovation_ratio_office: object | None = None
        self.renovation_ratio_schoolsec: object | None = None
        self.renovation_ratio_schoolprim: object | None = None
        self.renovation_ratio_retailfood: object | None = None
        self.renovation_ratio_retailother: object | None = None
        self.renovation_ratio_other: object | None = None
        self.renovation_share: object | None = None
        self.building_count: object | None = None
        self.storey_count_avg: object | None = None
        self.rh_residential: object | None = None
        self.rh_office: object | None = None
        self.rh_schoolsec: object | None = None
        self.rh_schoolprim: object | None = None
        self.rh_retailfood: object | None = None
        self.rh_retailother: object | None = None
        self.rh_other: object | None = None
        self.rh_avg: object | None = None
        self.NFV_total: object | None = None
        self.NFV_u: object | None = None
        self.NFV_c: object | None = None
        self.rh_ceiling: object | None = None
        self.GFV: object | None = None
        self.hull_ext_wall_wo_window_m2: object | None = None
        self.hull_roof_m2: object | None = None
        self.hull_fundament_m2: object | None = None
        self.hull_windows_north_m2: object | None = None
        self.hull_windows_east_m2: object | None = None
        self.hull_windows_south_m2: object | None = None
        self.hull_windows_west_m2: object | None = None
        self.hull_windows_horizontal_m2: object | None = None
        self.hull_window_m2: object | None = None
        self.hull_fenestration_rate: object | None = None
        self.hull_m2: object | None = None
        self.lc: object | None = None
        self.hull_transmittance_walls: object | None = None
        self.hull_transmittance_roof: object | None = None
        self.hull_transmittance_fundament: object | None = None
        self.hull_transmittance_windows_north: object | None = None
        self.hull_transmittance_windows_east: object | None = None
        self.hull_transmittance_windows_south: object | None = None
        self.hull_transmittance_windows_west: object | None = None
        self.hull_transmittance_windows_horizontal: object | None = None
        self.hull_transmittance_heatbridge: object | None = None
        self.transmittance_walls_Wm2NFA: object | None = None
        self.transmittance_roof_Wm2NFA: object | None = None
        self.transmittance_fundament_Wm2NFA: object | None = None
        self.transmittance_windows_Wm2NFA: object | None = None
        self.transmittance_heatbridge_Wm2NFA: object | None = None
        self.transmittance_MW: object | None = None
        self.transmittance_Wm2: object | None = None
        self.heat_capacity_effective_m: object | None = None  # var_name: heat_capacity_effective_m²
        self.heat_cap_eff_uncooled_m2: object | None = None
        self.heat_cap_eff_cooled_m2: object | None = None
        self.window_total_transmittance_north: object | None = None
        self.window_total_transmittance_east: object | None = None
        self.window_total_transmittance_south: object | None = None
        self.window_total_transmittance_west: object | None = None
        self.window_total_transmittance_horizontal: object | None = None
        self.window_irradiation_factor_winter_north: object | None = None
        self.window_irradiation_factor_winter_east: object | None = None
        self.window_irradiation_factor_winter_south: object | None = None
        self.window_irradiation_factor_winter_west: object | None = None
        self.window_irradiation_factor_winter_horizontal: object | None = None
        self.window_irradiation_factor_summer_north: object | None = None
        self.window_irradiation_factor_summer_east: object | None = None
        self.window_irradiation_factor_summer_south: object | None = None
        self.window_irradiation_factor_summer_west: object | None = None
        self.window_irradiation_factor_summer_horizontal: object | None = None
        self.irradiation_opaque_surcharge: object | None = None
        self.fc_residential: object | None = None
        self.fc_office: object | None = None
        self.fc_schoolsec: object | None = None
        self.fc_schoolprim: object | None = None
        self.fc_retailfood: object | None = None
        self.fc_retailother: object | None = None
        self.fc_other: object | None = None
        self.fc_u: object | None = None
        self.fc_c: object | None = None
        self.illuminance_min_residential: object | None = None
        self.illuminance_min_office: object | None = None
        self.illuminance_min_schoolsec: object | None = None
        self.illuminance_min_schoolprim: object | None = None
        self.illuminance_min_retailfood: object | None = None
        self.illuminance_min_retailother: object | None = None
        self.illuminance_min_other: object | None = None
        self.QS_max_shading_u: object | None = None
        self.QS_max_shading_c: object | None = None
        self.illuminance_efficiency_dirt: object | None = None
        self.illuminance_efficiency_glazing_ratio: object | None = None
        self.mob_shading_factor_u: object | None = None
        self.mob_shading_factor_c: object | None = None
        self.vent_air_tightness: object | None = None
        self.vent_tightness_ratio_blowerdoor_to_real: object | None = None
        self.vent_infiltration_ACH: object | None = None
        self.vent_share_mechanical_residential: object | None = None
        self.vent_share_mechanical_office: object | None = None
        self.vent_share_mechanical_schoolsec: object | None = None
        self.vent_share_mechanical_schoolprim: object | None = None
        self.vent_share_mechanical_retailfood: object | None = None
        self.vent_share_mechanical_retailother: object | None = None
        self.vent_share_mechanical_other: object | None = None
        self.NFA_windowvent: object | None = None
        self.NFV_windowvent: object | None = None
        self.NFA_mechvent: object | None = None
        self.NFV_mechvent: object | None = None
        self.vent_night_residential: object | None = None
        self.vent_night_office: object | None = None
        self.vent_night_schoolsec: object | None = None
        self.vent_night_schoolprim: object | None = None
        self.vent_night_retailfood: object | None = None
        self.vent_night_retailother: object | None = None
        self.vent_night_other: object | None = None
        self.ACH_night_m: object | None = None  # var_name: ACH_night_m³
        self.vent_ach_max_residential: object | None = None
        self.vent_ach_max_office: object | None = None
        self.vent_ach_max_schoolsec: object | None = None
        self.vent_ach_max_schoolprim: object | None = None
        self.vent_ach_max_retailfood: object | None = None
        self.vent_ach_max_retailother: object | None = None
        self.vent_ach_max_other: object | None = None
        self.vent_scale_residential: object | None = None
        self.vent_scale_office: object | None = None
        self.vent_scale_school_sec: object | None = None
        self.vent_scale_school_prim: object | None = None
        self.vent_scale_supermarket: object | None = None
        self.vent_scale_retail: object | None = None
        self.vent_scale_other: object | None = None
        self.Ev_scale_residential: object | None = None
        self.Ev_scale_office: object | None = None
        self.Ev_scale_school_sec: object | None = None
        self.Ev_scale_school_prim: object | None = None
        self.Ev_scale_retail_food: object | None = None
        self.Ev_scale_retail_other: object | None = None
        self.Ev_scale_other: object | None = None
        self.vent_heat_recovery_winter_residential: object | None = None
        self.vent_heat_recovery_winter_office: object | None = None
        self.vent_heat_recovery_winter_schoolsec: object | None = None
        self.vent_heat_recovery_winter_schoolprim: object | None = None
        self.vent_heat_recovery_winter_retailfood: object | None = None
        self.vent_heat_recovery_winter_retailother: object | None = None
        self.vent_heat_recovery_winter_other: object | None = None
        self.vent_heat_recovery_summer_residential: object | None = None
        self.vent_heat_recovery_summer_office: object | None = None
        self.vent_heat_recovery_summer_schoolsec: object | None = None
        self.vent_heat_recovery_summer_schoolprim: object | None = None
        self.vent_heat_recovery_summer_retailfood: object | None = None
        self.vent_heat_recovery_summer_retailother: object | None = None
        self.vent_heat_recovery_summer_other: object | None = None
        self.Vent_share_window_uncooled: object | None = None
        self.Vent_share_window_cooled: object | None = None
        self.Vent_share_mech_uncooled: object | None = None
        self.Vent_share_mech_cooled: object | None = None
        self.test_NFV_shares: object | None = None
        self.usage_concurrency_winter_residential: object | None = None
        self.usage_concurrency_winter_office: object | None = None
        self.usage_concurrency_winter_schoolsec: object | None = None
        self.usage_concurrency_winter_schoolprim: object | None = None
        self.usage_concurrency_winter_retailfood: object | None = None
        self.usage_concurrency_winter_retailother: object | None = None
        self.usage_concurrency_winter_other: object | None = None
        self.usage_concurrency_summer_residential: object | None = None
        self.usage_concurrency_summer_office: object | None = None
        self.usage_concurrency_summer_schoolsec: object | None = None
        self.usage_concurrency_summer_schoolprim: object | None = None
        self.usage_concurrency_summer_retailfood: object | None = None
        self.usage_concurrency_summer_retailother: object | None = None
        self.usage_concurrency_summer_other: object | None = None
        self.DHW_demand_residential_kWhm2: object | None = None
        self.DHW_demand_office_kWhm2: object | None = None
        self.DHW_demand_schoolsec_kWhm2: object | None = None
        self.DHW_demand_schoolprim_kWhm2: object | None = None
        self.DHW_demand_retailfood_kWhm2: object | None = None
        self.DHW_demand_retailother_kWhm2: object | None = None
        self.DHW_demand_other_kWhm2: object | None = None
        self.aux_el_demand_residential_kWhm2: object | None = None
        self.aux_el_demand_office_kWhm2: object | None = None
        self.aux_el_demand_schoolsec_kWhm2: object | None = None
        self.aux_el_demand_schoolprim_kWhm2: object | None = None
        self.aux_el_demand_retailfood_kWhm2: object | None = None
        self.aux_el_demand_retailother_kWhm2: object | None = None
        self.aux_el_demand_other_kWhm2: object | None = None
        self.Plugloads_scale_residential: object | None = None
        self.Plugloads_scale_office: object | None = None
        self.Plugloads_scale_schoolsec: object | None = None
        self.Plugloads_scale_schoolprim: object | None = None
        self.Plugloads_scale_retailfood: object | None = None
        self.Plugloads_scale_retailother: object | None = None
        self.Plugloads_scale_other: object | None = None
        self.density_NFApPers_residential: object | None = None
        self.density_NFApPers_office: object | None = None
        self.density_NFApPers_schoolsec: object | None = None
        self.density_NFApPers_retail: object | None = None
        self.density_NFApPers_schoolprim: object | None = None
        self.density_NFApPers_retail_other: object | None = None
        self.mob_simultaneity_edu: object | None = None
        self.mob_simultaneity_retail: object | None = None
        self.mob_simultaneity_office: object | None = None
        self.mob_motorization_perNFA_residential: object | None = None
        self.mob_motorization_perNFA_work: object | None = None
        self.mob_motorization_perNFA_retail: object | None = None
        self.Plight_max_office: object | None = None
        self.Plight_max_schoolsec: object | None = None
        self.Plight_max_schoolprim: object | None = None
        self.Plight_min_office: object | None = None
        self.Plight_min_schoolsec: object | None = None
        self.Plight_min_schoolprim: object | None = None
        self.lighting_factor_office: object | None = None
        self.lighting_factor_schoolsec: object | None = None
        self.lighting_factor_schoolprim: object | None = None
        self.lighting_factor_retailfood: object | None = None
        self.lighting_factor_retailother: object | None = None
        self.lighting_factor_other: object | None = None
        self.Daylightcoefficient_office: object | None = None
        self.Daylightcoefficient_schoolsec: object | None = None
        self.Daylightcoefficient_schoolprim: object | None = None
        self.daylightcontr_office: object | None = None
        self.daylightcontr_schoolsec: object | None = None
        self.daylightcontr_schoolprim: object | None = None
        self.heating_month1: object | None = None
        self.heating_month2: object | None = None
        self.heating_month3: object | None = None
        self.heating_month4: object | None = None
        self.heating_month5: object | None = None
        self.heating_month6: object | None = None
        self.heating_month7: object | None = None
        self.heating_month8: object | None = None
        self.heating_month9: object | None = None
        self.heating_month10: object | None = None
        self.heating_month11: object | None = None
        self.heating_month12: object | None = None
        self.QHmax_room_m: object | None = None  # var_name: QHmax_room_m²
        self.QHmax_room_MW: object | None = None
        self.QHmax_1el_m2: object | None = None
        self.QHmax_2th_m2: object | None = None
        self.QHmax_3el_m2: object | None = None
        self.QHmax_4th_m2: object | None = None
        self.QH_distr_loss_1el: object | None = None
        self.QH_distr_loss_2th: object | None = None
        self.QH_distr_loss_3el: object | None = None
        self.QH_distr_loss_4th: object | None = None
        self.heat_cop_1el: object | None = None
        self.heat_cop_2th: object | None = None
        self.heat_cop_3el: object | None = None
        self.heat_cop_4th: object | None = None
        self.QH_generation_eff_1el: object | None = None
        self.QH_generation_eff_2th: object | None = None
        self.QH_generation_eff_3el: object | None = None
        self.QH_generation_eff_4th: object | None = None
        self.QH_aux_wasteheat: object | None = None
        self.QH_aux_el_to_th_1el: object | None = None
        self.QH_aux_el_to_th_2th: object | None = None
        self.QH_aux_el_to_th_3el: object | None = None
        self.QH_aux_el_to_th_4th: object | None = None
        self.heat_th2_carrier_type: object | None = None
        self.heat_th4_carrier_type: object | None = None
        self.Tsetheat_min: object | None = None
        self.cooling_month1: object | None = None
        self.cooling_month2: object | None = None
        self.cooling_month3: object | None = None
        self.cooling_month4: object | None = None
        self.cooling_month5: object | None = None
        self.cooling_month6: object | None = None
        self.cooling_month7: object | None = None
        self.cooling_month8: object | None = None
        self.cooling_month9: object | None = None
        self.cooling_month10: object | None = None
        self.cooling_month11: object | None = None
        self.cooling_month12: object | None = None
        self.cool_share_residential: object | None = None
        self.cool_share_office: object | None = None
        self.cool_share_schoolsec: object | None = None
        self.cool_share_schoolprim: object | None = None
        self.cool_share_retailfood: object | None = None
        self.cool_share_retailother: object | None = None
        self.cool_share_other: object | None = None
        self.NFA_cooled: object | None = None
        self.NFAfrac_c: object | None = None
        self.NFAfrac_u: object | None = None
        self.QCmax_room_m2: object | None = None
        self.QCmax_room_MW: object | None = None
        self.QCmax_freecooling: object | None = None
        self.QCmax_1el: object | None = None
        self.QCmax_2th: object | None = None
        self.QCmax_3el: object | None = None
        self.QC_distr_losses_1el: object | None = None
        self.QC_distr_losses_2th: object | None = None
        self.QC_distr_losses_3el: object | None = None
        self.cool_cop_1el: object | None = None
        self.cool_cop_2th: object | None = None
        self.cool_cop_3el: object | None = None
        self.QC_to_EC_1: object | None = None
        self.QC_generation_eff_2th: object | None = None
        self.QC_to_EC_3: object | None = None
        self.QC_aux_fc: object | None = None
        self.QC_aux_1el: object | None = None
        self.QC_aux_2th: object | None = None
        self.QC_aux_3el: object | None = None
        self.cool_th2_carrier_type: object | None = None
        self.Tsetcool_max: object | None = None
        self.DHW_Tmin: object | None = None
        self.DHW_Tmax_input: object | None = None
        self.DHW_Tmax: object | None = None
        self.DHW_1_share_residential: object | None = None
        self.DHW_1_share_office: object | None = None
        self.DHW_1_share_schoolsec: object | None = None
        self.DHW_1_share_schoolprim: object | None = None
        self.DHW_1_share_retailfood: object | None = None
        self.DHW_1_share_retailother: object | None = None
        self.DHW_1_share_other: object | None = None
        self.DHW_storage_1_liter: object | None = None
        self.DHW_storage_2_liter: object | None = None
        self.DHW_1_is_used: object | None = None
        self.DHW_2_is_used: object | None = None
        self.DHW_thermal_power_1_kW: object | None = None
        self.DHW_losses_1: object | None = None
        self.DHW_losses_2: object | None = None
        self.DHW_efficiency_distribution_1: object | None = None
        self.DHW_efficiency_distribution_2: object | None = None
        self.DHW_1_incl_distribution_factor: object | None = None
        self.DHW_2_incl_distribution_factor: object | None = None
        self.DHW_carriertype_1: object | None = None
        self.DHW_1_is_electric: object | None = None
        self.DHW_carriertype_2: object | None = None
        self.DHW_2_is_electric: object | None = None
        self.DHW_1_efficiency: object | None = None
        self.DHW_2_efficiency: object | None = None
        self.DHW_conversion_1: object | None = None
        self.DHW_conversion_2: object | None = None
        self.DHW_1_el_aux: object | None = None
        self.DHW_2_el_aux: object | None = None
        self.DHW_occupancy_residential: object | None = None
        self.DHW_occupancy_office: object | None = None
        self.DHW_occupancy_schoolsec: object | None = None
        self.DHW_occupancy_schoolprim: object | None = None
        self.DHW_occupancy_retailfood: object | None = None
        self.DHW_occupancy_retailother: object | None = None
        self.DHW_occupancy_other: object | None = None
        self.DHW_concurrency_residential: object | None = None
        self.DHW_concurrency_office: object | None = None
        self.DHW_concurrency_schoolsec: object | None = None
        self.DHW_concurrency_schoolprim: object | None = None
        self.DHW_concurrency_retailfood: object | None = None
        self.DHW_concurrency_retailother: object | None = None
        self.DHW_concurrency_other: object | None = None
        self.DHW_storage_liter_pPerson: object | None = None
        self.DHW_thermal_power_pPerson: object | None = None
        self.DHW_thermal_power_Wpl: object | None = None
        self.DHW_storage_env_temp_default: object | None = None
        self.PV_is_used: object | None = None
        self.PV_profile_name: object | None = None
        self.PV_id: object | None = None
        self.PV_scale: object | None = None
        self.PV_efficiency: object | None = None
        self.PV_m2_per_kWp: object | None = None
        self.PV_kWp: object | None = None
        self.PV_module_area: object | None = None
        self.FLEX_PV_is_used: object | None = None
        self.FLEX_is_used: object | None = None
        self.FLEX_signal_name: object | None = None
        self.FLEX_signal_ID: object | None = None
        self.FLEX_grid_maxpower_Wm2: object | None = None
        self.FLEX_is_used_for_plugloads: object | None = None
        self.FLEX_is_used_for_HVAC_min: object | None = None
        self.FLEX_is_used_for_ev_min: object | None = None
        self.flex_heat_dT: object | None = None
        self.Tsetheat_flex: object | None = None
        self.FLEX_choice_heat_system: object | None = None
        self.FLEX_heat1_use: object | None = None
        self.FLEX_heat3_use: object | None = None
        self.flex_cool_dT: object | None = None
        self.Tsetcool_flex: object | None = None
        self.FLEX_choice_cool_system: object | None = None
        self.FLEX_cool1_use: object | None = None
        self.FLEX_cool3_use: object | None = None
        self.Batt_is_used: object | None = None
        self.Batt_cap_kWh: object | None = None
        self.Batt_cap_Wh_per_NFA: object | None = None
        self.Batt_c_rate: object | None = None
        self.Batt_max_power_specific: object | None = None
        self.Batt_eff_factor_charge: object | None = None
        self.Batt_eff_factor_discharge: object | None = None
        self.Batt_self_discharge_rate: object | None = None
        self.Batt_auto_discharge_factor: object | None = None
        self.Batt_SOC_init: object | None = None
        self.Batt_is_used_for_plugloads: object | None = None
        self.Batt_is_used_for_HVACminimum: object | None = None
        self.Batt_is_used_for_EV: object | None = None
        self.Batt_is_gridcharged: object | None = None
        self.flex_dhw_use: object | None = None
        self.flex_Signals_selected_column: object | None = None
        self.Batt_is_not_used_during_signals: object | None = None
        self.mobility_is_included: object | None = None
        self.mobility_region: object | None = None
        self.mobshare_residential: object | None = None
        self.mobshare_office: object | None = None
        self.mobshare_school: object | None = None
        self.mobshare_retail: object | None = None
        self.pkm_pedestrian: object | None = None
        self.pkm_bike: object | None = None
        self.pkm_mofa: object | None = None
        self.pkm_car_driver: object | None = None
        self.pkm_car_passenger: object | None = None
        self.pkm_bus: object | None = None
        self.pkm_tram_metro: object | None = None
        self.pkm_train: object | None = None
        self.pkm_distancebus: object | None = None
        self.mobility_vehicle_count: object | None = None
        self.EV_share: object | None = None
        self.EV_demand_kWhpkm: object | None = None
        self.EV_battsize_kWh: object | None = None
        self.EV_storage_total_kWh: object | None = None
        self.EV_self_discharge_per_week: object | None = None
        self.EV_selfdischarge_per_h: object | None = None
        self.EV_soc_minimum: object | None = None
        self.EV_charging_efficiency: object | None = None
        self.EV_charging_losses_surcharge_factor: object | None = None
        self.EV_max_charging_power_ratio: object | None = None
        self.EV_soc_min_work: object | None = None
        self.EV_soc_min_retail: object | None = None
        self.moped_factor: object | None = None
        self.EV_share_constant_charging: object | None = None
        self.mob_pkm_factor: object | None = None
        self.EV_experimental_calculation: object | None = None
        self.EV_mileage_residential: object | None = None
        self.EV_mileage_work: object | None = None
        self.EV_mileage_retail: object | None = None
        self.EV_soc_min_ext: object | None = None
        self.EV_soc_min_discharge: object | None = None
        self.fossile_demand_kWhpkm: object | None = None
        self.EV_count_residential: object | None = None
        self.EV_count_work: object | None = None
        self.EV_count_retail: object | None = None
        self.ev_bidirectional_use: object | None = None
        self.GWP_walls_name: object | None = None
        self.GWP_windows_name: object | None = None
        self.GWP_roof_name: object | None = None
        self.GWP_ground_name: object | None = None
        self.GPW_ceilings_name: object | None = None
        self.COMP_name_terrace: object | None = None
        self.COMP_name_basement_ceiling: object | None = None
        self.COMP_name_fundament: object | None = None
        self.COMP_name_ceil_to_air: object | None = None
        self.COMP_name_wall_earth_contacted: object | None = None
        self.COMP_name_internal_wall_load: object | None = None
        self.COMP_name_internal_wall_nonload: object | None = None
        self.COMP_name_ceiling_topfloor: object | None = None
        self.COMP_name_wall_ec_unheated: object | None = None
        self.COMP_name_basement_floor_unheated: object | None = None
        self.COMP_name_columns: object | None = None
        self.COMP_name_internal_wall_unheated: object | None = None
        self.COMP_name_unheated_horizontal: object | None = None
        self.COMP_name_balconies: object | None = None
        self.COMP_name_windowframe: object | None = None
        self.COMP_name_windowglazing: object | None = None
        self.COMP_name_other: object | None = None
        self.GWP_general_name: object | None = None
        self.GWP_other_name: object | None = None
        self.GWP_ref_area_walls: object | None = None
        self.GWP_ref_area_windows: object | None = None
        self.GWP_ref_area_roof: object | None = None
        self.GWP_ref_area_fundament: object | None = None
        self.GWP_ref_area_ceilings: object | None = None
        self.COMP_area_terrace: object | None = None
        self.COMP_area_basement_ceiling: object | None = None
        self.COMP_area_fundament: object | None = None
        self.COMP_area_ceil_to_air: object | None = None
        self.COMP_area_wall_earth_contacted: object | None = None
        self.COMP_area_internal_wall_load: object | None = None
        self.COMP_area_internal_wall_nonload: object | None = None
        self.COMP_area_ceiling_topfloor: object | None = None
        self.COMP_area_wall_ec_unheated: object | None = None
        self.COMP_area_basement_floor_unheated: object | None = None
        self.COMP_area_columns: object | None = None
        self.COMP_area_internal_wall_unheated: object | None = None
        self.COMP_area_unheated_horizontal: object | None = None
        self.COMP_area_balconies: object | None = None
        self.COMP_area_windowframe: object | None = None
        self.COMP_area_windowglazing: object | None = None
        self.GWP_refratio_walls: object | None = None
        self.GWP_refratio_windows: object | None = None
        self.GWP_refratio_roof: object | None = None
        self.GWP_refratio_fundament: object | None = None
        self.GWP_refratio_ceilings: object | None = None
        self.GWP_pv_name: object | None = None
        self.GWP_refratio_pv: object | None = None
        self.GWP_boreholes_name: object | None = None
        self.borehole_count: object | None = None
        self.GWP_ventilation_name: object | None = None
        self.GWP_solarthermal_name: object | None = None
        self.GWP_battery_name: object | None = None
        self.GWP_storage_name: object | None = None
        self.GWP_tga_general_name: object | None = None
        self.GWP_tga_other_name: object | None = None
        self.GWP_refratio_boreholes: object | None = None
        self.GWP_direct_fossile: object | None = None
        self.GWP_direct_biogenic: object | None = None
        self.GWP_direct_biogenic_share: object | None = None
        self.GWP_direct_life: object | None = None
        self.GWP_miv_count_ev: object | None = None
        self.GWP_miv_count_fossile: object | None = None
        self.GWP_mobility_construction_fossil: object | None = None
        self.GWP_mobility_construction_ev: object | None = None
        self.GHG_LCA_timeframe_years: object | None = None
        self.GWP_mobility_moped_gpPKm: object | None = None
        self.GWP_mobility_car_gpPKm: object | None = None
        self.year_rcp0: object | None = None
        self.year_rcp1: object | None = None
        self.year_rcp2: object | None = None
        self.year_rcp3: object | None = None
        self.grid_rcp1: object | None = None
        self.grid_rcp2: object | None = None
        self.grid_rcp3: object | None = None
        self.rcp1_renewable: object | None = None
        self.rcp2_renewable: object | None = None
        self.rcp3_renewable: object | None = None
        self.rcp1_dh: object | None = None
        self.rcp2_dh: object | None = None
        self.rcp3_dh: object | None = None
        self.rcp1_fossil: object | None = None
        self.rcp2_fossil: object | None = None
        self.rcp3_fossil: object | None = None
        self.GWP_rcpi_grid: object | None = None
        self.GWP_rcpi_grid_substition: object | None = None
        self.GWP_rcpi_district_heating: object | None = None
        self.GWP_rcpi_fossil: object | None = None
        self.GWP_rcpi_natural_gas: object | None = None
        self.GWP_rcpi_biomass: object | None = None
        self.GWP_rcpi_mob_fossile: object | None = None
        self.GWP_rcpi_renewable: object | None = None
        self.fPE_grid_profile: object | None = None
        self.district_heating_conversion_profile: object | None = None
        self.fGHG_grid_profile: object | None = None
        self.fPE_grid_column: object | None = None
        self.fGHG_grid_column: object | None = None
        self.heat_th2_is_dh: object | None = None
        self.heat_th4_is_dh: object | None = None
        self.cool_th2_is_dh: object | None = None
        self.dhw1_is_dh: object | None = None
        self.dhw2_is_dh: object | None = None
        self.heat_th2_is_ng: object | None = None
        self.heat_th4_is_ng: object | None = None
        self.cool_th2_is_ng: object | None = None
        self.dhw1_is_ng: object | None = None
        self.dhw2_is_ng: object | None = None
        self.heat_th2_is_bio: object | None = None
        self.heat_th4_is_bio: object | None = None
        self.cool_th2_is_bio: object | None = None
        self.dhw1_is_bio: object | None = None
        self.dhw2_is_bio: object | None = None
        self.heat_th2_is_other: object | None = None
        self.heat_th4_is_other: object | None = None
        self.cool_th2_is_other: object | None = None
        self.dhw1_is_other: object | None = None
        self.dhw2_is_other: object | None = None
        self.fPE_flex_factor: object | None = None
        self.pe_conversion_factor_gasoline: object | None = None
        self.StatPAX_residential: object | None = None
        self.StatPAX_office: object | None = None
        self.StatPAX_schoolsec: object | None = None
        self.StatPAX_schoolprim: object | None = None
        self.StatPAX_retail: object | None = None
        self.StatPAX_retailother: object | None = None
        self.e_kWhm2a: object | None = None
        self.EV_charging_stations: object | None = None
        self.EV_charging_station_power: object | None = None
        self.Ta_annual_avg: object | None = None
        self.Ta_avg_heating_period: object | None = None
        self.Ta_avg_cooling_period: object | None = None
        self.UED_plugloads: object | None = None
        self.UED_lighting: object | None = None
        self.UED_auxiliary: object | None = None
        self.UED_heating: object | None = None
        self.UED_cooling: object | None = None
        self.UED_dhw: object | None = None
        self.UED_ventilation: object | None = None
        self.UED_mim_electric: object | None = None
        self.UED_mim_fossile: object | None = None
        self.QT: object | None = None
        self.QV: object | None = None
        self.QVn: object | None = None
        self.QS: object | None = None
        self.QI: object | None = None
        self.QH: object | None = None
        self.QC: object | None = None
        self.QV_heatrecovery: object | None = None
        self.QT_winter: object | None = None
        self.QV_winter: object | None = None
        self.QVn_winter: object | None = None
        self.QS_winter: object | None = None
        self.QI_winter: object | None = None
        self.QH_winter: object | None = None
        self.QC_winter: object | None = None
        self.test_heat_balance_winter: object | None = None
        self.QT_wall_winter: object | None = None
        self.QT_roof_winter: object | None = None
        self.QT_ground_winter: object | None = None
        self.QT_window_winter: object | None = None
        self.QT_psi_winter: object | None = None
        self.QV_inf_winter: object | None = None
        self.QV_window_winter: object | None = None
        self.QV_mechvent_winter: object | None = None
        self.QV_heatrecovery_winter: object | None = None
        self.QH_min_winter: object | None = None
        self.QH_flex_winter: object | None = None
        self.QC_min_winter: object | None = None
        self.QC_flex_winter: object | None = None
        self.QH_flexshare_winter: object | None = None
        self.QC_flexshare_winter: object | None = None
        self.QT_summer: object | None = None
        self.QV_summer: object | None = None
        self.QVn_summer: object | None = None
        self.QS_summer: object | None = None
        self.QI_summer: object | None = None
        self.QH_summer: object | None = None
        self.QC_summer: object | None = None
        self.test_heat_balance_summer: object | None = None
        self.QT_wall_summer: object | None = None
        self.QT_roof_summer: object | None = None
        self.QT_ground_summer: object | None = None
        self.QT_window_summer: object | None = None
        self.QT_psi_summer: object | None = None
        self.QV_inf_summer: object | None = None
        self.QV_window_summer: object | None = None
        self.QV_mechvent_summer: object | None = None
        self.QV_heatrecovery_summer: object | None = None
        self.QH_min_summer: object | None = None
        self.QH_flex_summer: object | None = None
        self.QC_min_summer: object | None = None
        self.QC_flex_summer: object | None = None
        self.QH_flexshare_summer: object | None = None
        self.QC_flexshare_summer: object | None = None
        self.test_heat_balance: object | None = None
        self.QT_u: object | None = None
        self.QV_u: object | None = None
        self.QVn_u: object | None = None
        self.QS_u: object | None = None
        self.QI_u: object | None = None
        self.QH_u: object | None = None
        self.QT_wall_u: object | None = None
        self.QT_roof_u: object | None = None
        self.QT_ground_u: object | None = None
        self.QT_window_u: object | None = None
        self.QT_psi_u: object | None = None
        self.QV_inf_u: object | None = None
        self.QV_window_u: object | None = None
        self.QV_mechvent_u: object | None = None
        self.QV_heatrecovery_u: object | None = None
        self.QH_min_u: object | None = None
        self.QH_flex_u: object | None = None
        self.QH_flexanteil_u: object | None = None
        self.QT_c: object | None = None
        self.QV_c: object | None = None
        self.QVn_c: object | None = None
        self.QS_c: object | None = None
        self.QI_c: object | None = None
        self.QH_c: object | None = None
        self.QC_c: object | None = None
        self.QT_wall_c: object | None = None
        self.QT_roof_c: object | None = None
        self.QT_ground_c: object | None = None
        self.QT_window_c: object | None = None
        self.QT_psi_c: object | None = None
        self.QV_inf_c: object | None = None
        self.QV_window_c: object | None = None
        self.QV_mechvent_c: object | None = None
        self.QV_heatrecovery_c: object | None = None
        self.QH_min_c: object | None = None
        self.QH_flex_c: object | None = None
        self.QC_min_c: object | None = None
        self.QC_flex_c: object | None = None
        self.QC_flexanteil: object | None = None
        self.QH_flexanteil_c: object | None = None
        self.Tu_avg_winter: object | None = None
        self.Tc_avg_winter: object | None = None
        self.Tu_avg_summer: object | None = None
        self.Tc_avg_summer: object | None = None
        self.dTu_winter: object | None = None
        self.dTc_winter: object | None = None
        self.dTu_summer: object | None = None
        self.dTc_summer: object | None = None
        self.EUI_plugAuxLight: object | None = None
        self.EUI_plugloads: object | None = None
        self.EUI_auxiliary: object | None = None
        self.EUI_lighting: object | None = None
        self.EUIh_el: object | None = None
        self.EUIh_el_aux: object | None = None
        self.EUIc_el: object | None = None
        self.EUIc_el_aux: object | None = None
        self.EUIdhw_el: object | None = None
        self.EUIv_el: object | None = None
        self.EUIdhwdirect_el: object | None = None
        self.Batt_total_charge_input: object | None = None
        self.EUIev_el: object | None = None
        self.EUI_el_total: object | None = None
        self.PV_total: object | None = None
        self.PV_to_plugloads: object | None = None
        self.PV_to_Eh_min: object | None = None
        self.PV_to_Ec_min: object | None = None
        self.PV_to_Edhw_min: object | None = None
        self.PV_to_Ev_min: object | None = None
        self.PV_to_Eev_min: object | None = None
        self.PV_total_direct: object | None = None
        self.PV_to_Eh_flex: object | None = None
        self.PV_to_Ec_flex: object | None = None
        self.PV_to_Edhw: object | None = None
        self.PV_to_Edhw_direct: object | None = None
        self.PV_to_Batt: object | None = None
        self.PV_to_Eev_flex: object | None = None
        self.PV_total_flex: object | None = None
        self.PV_to_Egrid: object | None = None
        self.Batt_to_plugloads: object | None = None
        self.Batt_to_HVAC: object | None = None
        self.Batt_to_Eh_min: object | None = None
        self.Batt_to_Ec_min: object | None = None
        self.Batt_to_Edhw_min: object | None = None
        self.Batt_to_Ev_min: object | None = None
        self.Batt_to_Eev_min: object | None = None
        self.Batt_charging_losses: object | None = None
        self.VRGrid_to_plugloads: object | None = None
        self.VRGrid_to_Eh_min: object | None = None
        self.VRGrid_to_Ec_min: object | None = None
        self.VRGrid_to_Edhw_min: object | None = None
        self.VRGrid_to_Ev_min: object | None = None
        self.VRGrid_to_Eev_min: object | None = None
        self.VRGrid_to_min: object | None = None
        self.VRGrid_to_Eh_flex: object | None = None
        self.VRGrid_to_Ec_flex: object | None = None
        self.VRGrid_to_Edhw_flex: object | None = None
        self.VRGrid_to_Batt: object | None = None
        self.VRGrid_to_Eev_flex: object | None = None
        self.VRGrid_to_flex: object | None = None
        self.VRGrid_to_building: object | None = None
        self.Eev_to_plugloads: object | None = None
        self.Eev_to_HVAC: object | None = None
        self.Eev_to_Eh_min: object | None = None
        self.Eev_to_Ec_min: object | None = None
        self.Eev_to_Edhw_min: object | None = None
        self.Eev_to_Ev_min: object | None = None
        self.Eev_discharge_loss: object | None = None
        self.Eev_to_district: object | None = None
        self.Grid_to_plugloads: object | None = None
        self.Grid_to_Eh_min: object | None = None
        self.Grid_to_Ec_min: object | None = None
        self.Grid_to_Edhw_min: object | None = None
        self.Grid_to_Ev_min: object | None = None
        self.Grid_to_building_min: object | None = None
        self.Grid_to_Eev_min: object | None = None
        self.Grid_to_min: object | None = None
        self.Eev_ext_charge: object | None = None
        self.EUIh_district_heating: object | None = None
        self.EUIdhw_district_heating: object | None = None
        self.EUI_district_heating: object | None = None
        self.EUIh_natural_gas: object | None = None
        self.EUIdhw_natural_gas: object | None = None
        self.EUI_natural_gas: object | None = None
        self.EUIh_biomass: object | None = None
        self.EUIdhw_biomass: object | None = None
        self.EUI_biomass: object | None = None
        self.EUIh_other: object | None = None
        self.EUIc_other: object | None = None
        self.EUIdhw_other: object | None = None
        self.EUI_other: object | None = None
        self.EUI_mob_fossil: object | None = None
        self.EUIh_2th: object | None = None
        self.EUIh_4th: object | None = None
        self.EUIc_2th: object | None = None
        self.EUIdhw_1th: object | None = None
        self.EUIdhw_2th: object | None = None
        self.Grid_total_flexandnotflex: object | None = None
        self.context_factor_density: object | None = None
        self.context_factor_mobility: object | None = None
        self.context_factor_renovation: object | None = None
        self.PEI_demand: object | None = None
        self.PEI_el_plugloads: object | None = None
        self.PEI_el_hvac: object | None = None
        self.PEI_district_heating: object | None = None
        self.PEI_natural_gas: object | None = None
        self.PEI_biomass: object | None = None
        self.PEI_other: object | None = None
        self.PEI_mob_total: object | None = None
        self.PEI_mob_fossile: object | None = None
        self.PEI_mob_el: object | None = None
        self.PEI_storage_losses: object | None = None
        self.PEI_cf_density: object | None = None
        self.PEI_cf_mobility: object | None = None
        self.PEI_cf_renovation: object | None = None
        self.PEI_sub_PV: object | None = None
        self.PEI_sub_flex: object | None = None
        self.PEI_balance: object | None = None
        self.PEI_grid_import: object | None = None
        self.PEI_flex_import: object | None = None
        self.PEI_evExtCharge_import: object | None = None
        self.PEI_import: object | None = None
        self.PEI_pv_export: object | None = None
        self.PEI_evOtherTravel_export: object | None = None
        self.PEI_export: object | None = None
        self.PEI_saldo_project: object | None = None
        self.PEI_saldo_target: object | None = None
        self.PEI_importExport_balance: object | None = None
        self.fPE_grid: object | None = None
        self.fPE_eff: object | None = None
        self.GWP_ee_walls_fossile: object | None = None
        self.GWP_ee_walls_biogenic: object | None = None
        self.GWP_life_walls: object | None = None
        self.GWP_ee_lc_walls_fossil: object | None = None
        self.GWP_ee_lc_walls_biogenic: object | None = None
        self.GWP_ee_lc_walls: object | None = None
        self.GWP_ee_windows_fossile: object | None = None
        self.GWP_ee_windows_bigenic: object | None = None
        self.GWP_life_windows: object | None = None
        self.GWP_ee_lc_windows_fossile: object | None = None
        self.GWP_ee_lc_windows_biogenic: object | None = None
        self.GWP_ee_lc_windows: object | None = None
        self.GWP_ee_roof_fossile: object | None = None
        self.GWP_ee_roof_biogenic: object | None = None
        self.GWP_life_roof: object | None = None
        self.GWP_ee_lc_roof_fossile: object | None = None
        self.GWP_ee_lc_roof_biogenic: object | None = None
        self.GWP_ee_lc_roof: object | None = None
        self.GWP_ee_ground_fossile: object | None = None
        self.GWP_ee_ground_biogenic: object | None = None
        self.GWP_life_ground: object | None = None
        self.GWP_ee_lc_ground_fossile: object | None = None
        self.GWP_ee_lc_ground_biogenic: object | None = None
        self.GWP_ee_lc_ground: object | None = None
        self.GWP_ee_ceilings_fossile: object | None = None
        self.GWP_ee_ceilings_biogenic: object | None = None
        self.GWP_life_ceilings: object | None = None
        self.GWP_ee_lc_ceilings_fossile: object | None = None
        self.GWP_ee_lc_ceilings_biogenic: object | None = None
        self.GWP_ee_lc_ceil: object | None = None
        self.GWP_ee_general_fossile: object | None = None
        self.GWP_ee_general_bigonenic: object | None = None
        self.GWP_life_general: object | None = None
        self.GWP_ee_lc_general_fossile: object | None = None
        self.GWP_ee_lc_general_biogenic: object | None = None
        self.GWP_ee_general: object | None = None
        self.GWP_ee_other_fossile: object | None = None
        self.GWP_ee_other_biogenic: object | None = None
        self.GWP_life_other: object | None = None
        self.GWP_ee_lc_other_fossile: object | None = None
        self.GWP_ee_lc_other_biogenic: object | None = None
        self.GWP_ee_lc_other: object | None = None
        self.GWP_ee_direct_fossile: object | None = None
        self.GWP_ee_direct_biogenic: object | None = None
        self.GWP_life_direct: object | None = None
        self.GWP_ee_lc_direct_fossile: object | None = None
        self.GWP_ee_lc_direct_biogenic: object | None = None
        self.GWP_ee_lc_direct: object | None = None
        self.GWP_ee_con_build: object | None = None
        self.GWP_ee_rep_build: object | None = None
        self.GWP_ee_lc_fossil: object | None = None
        self.GWP_ee_lc_biogenic: object | None = None
        self.GWP_ee_lc_construction: object | None = None
        self.GWP_ee_tga_pv_fossile: object | None = None
        self.GWP_ee_tga_pv_biogenic: object | None = None
        self.GWP_life_tga_pv: object | None = None
        self.GWP_ee_lc_pv: object | None = None
        self.GWP_ee_tga_boreholes_fossile: object | None = None
        self.GWP_ee_tga_boreholes_biogenic: object | None = None
        self.GWP_life_tga_boreholes: object | None = None
        self.GWP_ee_lc_boreholes: object | None = None
        self.GWP_ee_tga_ventilation_fossile: object | None = None
        self.GWP_ee_tga_ventilation_biogenic: object | None = None
        self.GWP_life_tga_ventilation: object | None = None
        self.GWP_ee_lc_ventilation: object | None = None
        self.GWP_ee_tga_solarthermal_fossile: object | None = None
        self.GWP_ee_tga_solarthermal_biogenic: object | None = None
        self.GWP_life_solarthermal: object | None = None
        self.GWP_ee_lc_solarthermal: object | None = None
        self.GWP_ee_tga_battery_fossile: object | None = None
        self.GWP_ee_tga_battery_biogenic: object | None = None
        self.GWP_life_battery: object | None = None
        self.GWP_ee_lc_battery: object | None = None
        self.GWP_ee_tga_storage_fossile: object | None = None
        self.GWP_ee_tga_storage_biogenic: object | None = None
        self.GWP_life_storage: object | None = None
        self.GWP_ee_lc_storage: object | None = None
        self.GWP_ee_tga_general_fossile: object | None = None
        self.GWP_ee_tga_general_biogenic: object | None = None
        self.GWP_life_tga_general: object | None = None
        self.GWP_ee_lc_tga_general: object | None = None
        self.GWP_ee_tga_other_fossile: object | None = None
        self.GWP_ee_tga_other_biogenic: object | None = None
        self.GWP_life_tga_other: object | None = None
        self.GWP_ee_lc_tga_other: object | None = None
        self.GWP_ee_con_tga: object | None = None
        self.GWP_ee_rep_tga: object | None = None
        self.GWP_ee_lc_tga: object | None = None
        self.GWP_ee_mob_fossile: object | None = None
        self.GWP_ee_mob_ev: object | None = None
        self.GWP_ee_lc_mob: object | None = None
        self.GWP_oe_battery_charge: object | None = None
        self.GWP_emInt_grid_avg: object | None = None
        self.GWP_emInt_grid: object | None = None
        self.GWP_emInt_flex: object | None = None
        self.GWP_emInt_batt_charge: object | None = None
        self.GWP_emInt_ev_charge: object | None = None
        self.GWP_emInt_PV_feedin: object | None = None
        self.GWP_oe_grid_build: object | None = None
        self.GWP_oe_flex_build: object | None = None
        self.GWP_oe_district_heating: object | None = None
        self.GWP_oe_natural_gas: object | None = None
        self.GWP_oe_biomass: object | None = None
        self.GWP_oe_other: object | None = None
        self.GWP_oe_grid_feedin: object | None = None
        self.GWP_oe_building: object | None = None
        self.GWP_oe_mob_ev: object | None = None
        self.GWP_oe_mob_ev_export: object | None = None
        self.GWP_oe_mob_fossile: object | None = None
        self.GWP_oe_mob: object | None = None
        self.GWP_oe: object | None = None
        self.GWP_oe_lc_grid_build: object | None = None
        self.GWP_oe_lc_flex_build: object | None = None
        self.GWP_oe_lc_district_heating: object | None = None
        self.GWP_oe_lc_natural_gas: object | None = None
        self.GWP_oe_lc_biomass: object | None = None
        self.GWP_oe_lc_other: object | None = None
        self.GWP_oe_lc_grid_feedin: object | None = None
        self.GWP_oe_lc_building: object | None = None
        self.GWP_oe_lc_emission: object | None = None
        self.GWP_oe_lc_emission_savings: object | None = None
        self.GWP_oe_lc_mob_ev: object | None = None
        self.GWP_oe_lc_mob_export: object | None = None
        self.GWP_oe_lc_mob_fossile: object | None = None
        self.GWP_oe_lc_mob: object | None = None
        self.GWP_lc_total: object | None = None
        self.GWP_lc_OE_total: object | None = None
        self.GWP_lc_EE_total: object | None = None
        self.cost_E_grid: object | None = None
        self.cost_VRGrid_flex: object | None = None
        self.cost_PV_to_Egrid: object | None = None
        self.cost_total: object | None = None
        self.flex_signal_ratio: object | None = None
        self.flex_signal_ratio_winter: object | None = None
        self.flex_signal_ratio_summer: object | None = None
        self.flex_GSRU: object | None = None
        self.flex_GSRI: object | None = None
        self.flex_GSR: object | None = None
        self.PV_own_consumption_direct: object | None = None
        self.PV_own_consumption_flex: object | None = None
        self.PV_own_consumption: object | None = None
        self.EUI_self_sufficiency: object | None = None
        self.Batt_total_charge: object | None = None
        self.Batt_total_discharge: object | None = None
        self.Batt_charge_losses: object | None = None
        self.Batt_discharge_losses: object | None = None
        self.Batt_RTE: object | None = None
        self.Batt_FEC: object | None = None
        self.StatPAX: object | None = None
        self.mob_annual_milage_district: object | None = None
        self.mob_annual_mileage_PAX: object | None = None
        self.UED_mob_el_target: object | None = None
        self.EUI_mob_fossile: object | None = None
        self.EV_FEC: object | None = None
        self.UED_mob_el_total: object | None = None
        self.UED_mob_el_other: object | None = None
        self.EUIev_el_total: object | None = None
        self.Edhw_th: object | None = None
        self.Edhw_el: object | None = None
        self.Edhw_aux_el: object | None = None
        self.Edhw_1_th: object | None = None
        self.Edhw_1_el: object | None = None
        self.Edhw_1_aux_el: object | None = None
        self.Edhw_2_th: object | None = None
        self.Edhw_2_el: object | None = None
        self.Edhw_2_aux_el: object | None = None

class Meta:
    def __init__(self):
        self.scenario_version = VariableMeta(
            var_name='scenario_version', 
            attr_name='scenario_version', 
            icon='🔧', 
            label_de='Tool Version', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='tool', 
            measure='version', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.input_version_number = VariableMeta(
            var_name='input_version_number', 
            attr_name='input_version_number', 
            icon='🔧', 
            label_de='Inputdatenstruktur Version', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='tool', 
            measure='input version', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.input_version_date = VariableMeta(
            var_name='input_version_date', 
            attr_name='input_version_date', 
            icon=None, 
            label_de='Inputdatenstruktur Datum', 
            unit='date', 
            comment=None, 
            source='IN', 
            ka=None, 
            domain='tool', 
            measure='input version date', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cfd_fPE = VariableMeta(
            var_name='cfd_fPE', 
            attr_name='cfd_fPE', 
            icon='🔧', 
            label_de='Primärenergiefaktor', 
            unit='kWhPE/kWhEE', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='fPE', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cfd_A = VariableMeta(
            var_name='cfd_A', 
            attr_name='cfd_A', 
            icon='🔧', 
            label_de='Ausnutzungsfaktor Erneuerbare', 
            unit='kWhEE/m²GF', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='A', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cfd_dx = VariableMeta(
            var_name='cfd_dx', 
            attr_name='cfd_dx', 
            icon='🔧', 
            label_de='Skalierungsfaktor', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='dx', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cfd_EUI = VariableMeta(
            var_name='cfd_EUI', 
            attr_name='cfd_EUI', 
            icon='🔧', 
            label_de='Energieintensität Bedarf', 
            unit='kWhEE/m²NGFa', 
            comment='Energy End Use Intensity', 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='EUI', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cfd_cutoff = VariableMeta(
            var_name='cfd_cutoff', 
            attr_name='cfd_cutoff', 
            icon='🔧', 
            label_de='Maximum', 
            unit='kWhPE/m²NGFa', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='cutoff', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cfm_budget_residential = VariableMeta(
            var_name='cfm_budget_residential', 
            attr_name='cfm_budget_residential', 
            icon='🔧', 
            label_de='Mobilitätsbudget Wohnen', 
            unit='kWhPE/m²NGFa', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='context factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key=None
        )
        self.cfm_budget_office = VariableMeta(
            var_name='cfm_budget_office', 
            attr_name='cfm_budget_office', 
            icon='🔧', 
            label_de='Mobilitätsbudget Büro', 
            unit='kWhPE/m²NGFa', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='context factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key=None
        )
        self.cfm_budget_school = VariableMeta(
            var_name='cfm_budget_school', 
            attr_name='cfm_budget_school', 
            icon='🔧', 
            label_de='Mobilitätsbudget Ausbildung', 
            unit='kWhPE/m²NGFa', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='context factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key=None
        )
        self.cfm_budget_retail = VariableMeta(
            var_name='cfm_budget_retail', 
            attr_name='cfm_budget_retail', 
            icon='🔧', 
            label_de='Mobilitätsbudget Handel + Sonstige', 
            unit='kWhPE/m²NGFa', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='context factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key=None
        )
        self.cfr_budget = VariableMeta(
            var_name='cfr_budget', 
            attr_name='cfr_budget', 
            icon='🔧', 
            label_de='Kontextfaktor Sanierung', 
            unit='kWhPE/m²NGFa', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='context factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_name = VariableMeta(
            var_name='project_name', 
            attr_name='project_name', 
            icon='📝', 
            label_de='Projektname', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='name', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_url = VariableMeta(
            var_name='project_url', 
            attr_name='project_url', 
            icon='📝', 
            label_de='ProjektURL', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='url', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.location_address = VariableMeta(
            var_name='location_address', 
            attr_name='location_address', 
            icon='📝', 
            label_de='Adresse', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='address', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.municipality_name = VariableMeta(
            var_name='municipality_name', 
            attr_name='municipality_name', 
            icon='📝', 
            label_de='Gemeinde', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='municipality', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_creation_date = VariableMeta(
            var_name='project_creation_date', 
            attr_name='project_creation_date', 
            icon='📝', 
            label_de='Erstellungsdatum', 
            unit='date', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='created', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_description = VariableMeta(
            var_name='project_description', 
            attr_name='project_description', 
            icon='📝', 
            label_de='Projektbeschreibung', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='description', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_scenario_name = VariableMeta(
            var_name='project_scenario_name', 
            attr_name='project_scenario_name', 
            icon='📝', 
            label_de='Variante / Scenario', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='scenario_name', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.location_postcode = VariableMeta(
            var_name='location_postcode', 
            attr_name='location_postcode', 
            icon='📝', 
            label_de='Postleitzahl', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='project', 
            measure='postcode', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mobility_mode = VariableMeta(
            var_name='mobility_mode', 
            attr_name='mobility_mode', 
            icon='📝', 
            label_de='Mobilitätsverfahren', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='declaration', 
            measure='mobility_mode', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.weather_name = VariableMeta(
            var_name='weather_name', 
            attr_name='weather_name', 
            icon='🌦️', 
            label_de='Wetterdatensatz Name', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='weather', 
            measure='name', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.weather_index = VariableMeta(
            var_name='weather_index', 
            attr_name='weather_index', 
            icon='🌦️', 
            label_de='Wetterdatensatz Nummer', 
            unit='int', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='weather', 
            measure='index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GFA_residential = VariableMeta(
            var_name='GFA_residential', 
            attr_name='GFA_residential', 
            icon='🏙️', 
            label_de='BGF Wohnen', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.GFA_office = VariableMeta(
            var_name='GFA_office', 
            attr_name='GFA_office', 
            icon='🏙️', 
            label_de='BGF Büro', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.GFA_schoolsec = VariableMeta(
            var_name='GFA_schoolsec', 
            attr_name='GFA_schoolsec', 
            icon='🏙️', 
            label_de='BGF Bildung sekundär', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.GFA_schoolprim = VariableMeta(
            var_name='GFA_schoolprim', 
            attr_name='GFA_schoolprim', 
            icon='🏙️', 
            label_de='BGF Bildung primär', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.GFA_retailfood = VariableMeta(
            var_name='GFA_retailfood', 
            attr_name='GFA_retailfood', 
            icon='🏙️', 
            label_de='BGF Lebensmittelhandel', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.GFA_retailother = VariableMeta(
            var_name='GFA_retailother', 
            attr_name='GFA_retailother', 
            icon='🏙️', 
            label_de='BGF Handel sonstiger', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.GFA_other = VariableMeta(
            var_name='GFA_other', 
            attr_name='GFA_other', 
            icon='🏙️', 
            label_de='BGF Sonstige', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.GFA_total = VariableMeta(
            var_name='GFA_total', 
            attr_name='GFA_total', 
            icon='🏙️', 
            label_de='BGF Quartier', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='GFA', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFA_to_GFA_ratio_residential = VariableMeta(
            var_name='NFA_to_GFA_ratio_residential', 
            attr_name='NFA_to_GFA_ratio_residential', 
            icon='🏙️', 
            label_de='NGF/BGF Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.NFA_to_GFA_ratio_office = VariableMeta(
            var_name='NFA_to_GFA_ratio_office', 
            attr_name='NFA_to_GFA_ratio_office', 
            icon='🏙️', 
            label_de='NGF/BGF  Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.NFA_to_GFA_ratio_schoolsec = VariableMeta(
            var_name='NFA_to_GFA_ratio_schoolsec', 
            attr_name='NFA_to_GFA_ratio_schoolsec', 
            icon='🏙️', 
            label_de='NGF/BGF Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.NFA_to_GFA_ratio_schoolprim = VariableMeta(
            var_name='NFA_to_GFA_ratio_schoolprim', 
            attr_name='NFA_to_GFA_ratio_schoolprim', 
            icon='🏙️', 
            label_de='NGF/BGF Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.NFA_to_GFA_ratio_retailfood = VariableMeta(
            var_name='NFA_to_GFA_ratio_retailfood', 
            attr_name='NFA_to_GFA_ratio_retailfood', 
            icon='🏙️', 
            label_de='NGF/BGF Lebensmittelhandel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.NFA_to_GFA_ratio_retailother = VariableMeta(
            var_name='NFA_to_GFA_ratio_retailother', 
            attr_name='NFA_to_GFA_ratio_retailother', 
            icon='🏙️', 
            label_de='NGF/BGF Handel sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.NFA_to_GFA_ratio_other = VariableMeta(
            var_name='NFA_to_GFA_ratio_other', 
            attr_name='NFA_to_GFA_ratio_other', 
            icon='🏙️', 
            label_de='NGF/BGF Sonstige', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.NFA_to_GFA_ratio = VariableMeta(
            var_name='NFA_to_GFA_ratio', 
            attr_name='NFA_to_GFA_ratio', 
            icon='🏙️', 
            label_de='NGF/BGF Quartier', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='NFA_to_GFA', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFA_residential = VariableMeta(
            var_name='NFA_residential', 
            attr_name='NFA_residential', 
            icon='🏙️', 
            label_de='NGF Wohnen', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.NFA_office = VariableMeta(
            var_name='NFA_office', 
            attr_name='NFA_office', 
            icon='🏙️', 
            label_de='NGF Büro', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.NFA_schoolsec = VariableMeta(
            var_name='NFA_schoolsec', 
            attr_name='NFA_schoolsec', 
            icon='🏙️', 
            label_de='NGF Bildung sekundär', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.NFA_schoolprim = VariableMeta(
            var_name='NFA_schoolprim', 
            attr_name='NFA_schoolprim', 
            icon='🏙️', 
            label_de='NGF Bildung primär', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.NFA_retailfood = VariableMeta(
            var_name='NFA_retailfood', 
            attr_name='NFA_retailfood', 
            icon='🏙️', 
            label_de='NGF Handel Lebensmittel', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.NFA_retailother = VariableMeta(
            var_name='NFA_retailother', 
            attr_name='NFA_retailother', 
            icon='🏙️', 
            label_de='NGF Handel sonstiger', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.NFA_other = VariableMeta(
            var_name='NFA_other', 
            attr_name='NFA_other', 
            icon='🏙️', 
            label_de='NGF Sonstige', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.NFA_total = VariableMeta(
            var_name='NFA_total', 
            attr_name='NFA_total', 
            icon='🏙️', 
            label_de='NGF Quartier', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.per_NFA = VariableMeta(
            var_name='per_NFA', 
            attr_name='per_NFA', 
            icon='🏙️', 
            label_de='Pro NGF ( Kehrwert NGF)', 
            unit='1/m²NGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='usage', 
            measure='area_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.plot_area = VariableMeta(
            var_name='plot_area', 
            attr_name='plot_area', 
            icon='🏙️', 
            label_de='Bebaubare Grundstücksfläche', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='area', 
            spatial_scope='plot', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FSI = VariableMeta(
            var_name='FSI', 
            attr_name='FSI', 
            icon='🏙️', 
            label_de='Geschoßflächenzahl', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='district', 
            measure='floor_space_index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.renovation_ratio_residential = VariableMeta(
            var_name='renovation_ratio_residential', 
            attr_name='renovation_ratio_residential', 
            icon='🏙️', 
            label_de='Sanierung Anteil Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.renovation_ratio_office = VariableMeta(
            var_name='renovation_ratio_office', 
            attr_name='renovation_ratio_office', 
            icon='🏙️', 
            label_de='Sanierung Anteil Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.renovation_ratio_schoolsec = VariableMeta(
            var_name='renovation_ratio_schoolsec', 
            attr_name='renovation_ratio_schoolsec', 
            icon='🏙️', 
            label_de='Sanierung Anteil Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.renovation_ratio_schoolprim = VariableMeta(
            var_name='renovation_ratio_schoolprim', 
            attr_name='renovation_ratio_schoolprim', 
            icon='🏙️', 
            label_de='Sanierung Anteil Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.renovation_ratio_retailfood = VariableMeta(
            var_name='renovation_ratio_retailfood', 
            attr_name='renovation_ratio_retailfood', 
            icon='🏙️', 
            label_de='Sanierung Anteil Lebensmittelhandel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.renovation_ratio_retailother = VariableMeta(
            var_name='renovation_ratio_retailother', 
            attr_name='renovation_ratio_retailother', 
            icon='🏙️', 
            label_de='Sanierung Anteil Handel Sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.renovation_ratio_other = VariableMeta(
            var_name='renovation_ratio_other', 
            attr_name='renovation_ratio_other', 
            icon='🏙️', 
            label_de='Sanierung Anteil Sonstige', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.renovation_share = VariableMeta(
            var_name='renovation_share', 
            attr_name='renovation_share', 
            icon='🏙️', 
            label_de='Sanierungsanteil im Quartier', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='district', 
            measure='renovation', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.building_count = VariableMeta(
            var_name='building_count', 
            attr_name='building_count', 
            icon='🏙️', 
            label_de='Anzahl Baukörper', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='district', 
            measure='buildings', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.storey_count_avg = VariableMeta(
            var_name='storey_count_avg', 
            attr_name='storey_count_avg', 
            icon='🏙️', 
            label_de='Anzahl Geschoße', 
            unit='-', 
            comment='Average', 
            source='IN', 
            ka=1, 
            domain='district', 
            measure='storeys', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.rh_residential = VariableMeta(
            var_name='rh_residential', 
            attr_name='rh_residential', 
            icon='↕️', 
            label_de='Raumhöhe Wohnen', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.rh_office = VariableMeta(
            var_name='rh_office', 
            attr_name='rh_office', 
            icon='↕️', 
            label_de='Raumhöhe Büro', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.rh_schoolsec = VariableMeta(
            var_name='rh_schoolsec', 
            attr_name='rh_schoolsec', 
            icon='↕️', 
            label_de='Raumhöhe sekundäre Bildungseinrichtung/ Universität', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.rh_schoolprim = VariableMeta(
            var_name='rh_schoolprim', 
            attr_name='rh_schoolprim', 
            icon='↕️', 
            label_de='Raumhöhe primäre Bildundseinrichtung/ Kindergarten', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.rh_retailfood = VariableMeta(
            var_name='rh_retailfood', 
            attr_name='rh_retailfood', 
            icon='↕️', 
            label_de='Raumhöhe Lebensmittelhandel', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.rh_retailother = VariableMeta(
            var_name='rh_retailother', 
            attr_name='rh_retailother', 
            icon='↕️', 
            label_de='Raumhöhe Handel sonstiger', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.rh_other = VariableMeta(
            var_name='rh_other', 
            attr_name='rh_other', 
            icon='↕️', 
            label_de='Raumhöhe Sonstige Nutzung', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.rh_avg = VariableMeta(
            var_name='rh_avg', 
            attr_name='rh_avg', 
            icon='↕️', 
            label_de='Raumhöhe Quartier', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFV_total = VariableMeta(
            var_name='NFV_total', 
            attr_name='NFV_total', 
            icon='↕️', 
            label_de='Raumvolumen Quartier', 
            unit='m³net', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='volume', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFV_u = VariableMeta(
            var_name='NFV_u', 
            attr_name='NFV_u', 
            icon='↕️', 
            label_de='Raumvolumen ungekühlt', 
            unit='m³net', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='volume', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFV_c = VariableMeta(
            var_name='NFV_c', 
            attr_name='NFV_c', 
            icon='↕️', 
            label_de='Raumvolumen gekühlt', 
            unit='m³net', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='volume', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.rh_ceiling = VariableMeta(
            var_name='rh_ceiling', 
            attr_name='rh_ceiling', 
            icon='↕️', 
            label_de='Höhe Geschoßdecken', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='geometry', 
            measure='height', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GFV = VariableMeta(
            var_name='GFV', 
            attr_name='GFV', 
            icon='↕️', 
            label_de='Raumvolumen Quartier brutto', 
            unit='m³gross', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='volume', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.hull_ext_wall_wo_window_m2 = VariableMeta(
            var_name='hull_ext_wall_wo_window_m2', 
            attr_name='hull_ext_wall_wo_window_m2', 
            icon='🧊', 
            label_de='Hüllfläche Außenwand', 
            unit='m²', 
            comment='exkl. Fenster', 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='wall'
        )
        self.hull_roof_m2 = VariableMeta(
            var_name='hull_roof_m2', 
            attr_name='hull_roof_m2', 
            icon='🧊', 
            label_de='Hüllfläche Dach', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='roof'
        )
        self.hull_fundament_m2 = VariableMeta(
            var_name='hull_fundament_m2', 
            attr_name='hull_fundament_m2', 
            icon='🧊', 
            label_de='Hüllfläche Kellerdecke / Fundament', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.hull_windows_north_m2 = VariableMeta(
            var_name='hull_windows_north_m2', 
            attr_name='hull_windows_north_m2', 
            icon='🧊', 
            label_de='Hüllfläche Fenster Nord', 
            unit='m²', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_north'
        )
        self.hull_windows_east_m2 = VariableMeta(
            var_name='hull_windows_east_m2', 
            attr_name='hull_windows_east_m2', 
            icon='🧊', 
            label_de='Hüllfläche Fenster Ost', 
            unit='m²', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_east'
        )
        self.hull_windows_south_m2 = VariableMeta(
            var_name='hull_windows_south_m2', 
            attr_name='hull_windows_south_m2', 
            icon='🧊', 
            label_de='Hüllfläche Fenster Süd', 
            unit='m²', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_south'
        )
        self.hull_windows_west_m2 = VariableMeta(
            var_name='hull_windows_west_m2', 
            attr_name='hull_windows_west_m2', 
            icon='🧊', 
            label_de='Hüllfläche Fenster West', 
            unit='m²', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_west'
        )
        self.hull_windows_horizontal_m2 = VariableMeta(
            var_name='hull_windows_horizontal_m2', 
            attr_name='hull_windows_horizontal_m2', 
            icon='🧊', 
            label_de='Hüllfläche Fenster Horizontal', 
            unit='m²', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_horizontal'
        )
        self.hull_window_m2 = VariableMeta(
            var_name='hull_window_m2', 
            attr_name='hull_window_m2', 
            icon='🧊', 
            label_de='Hüllfläche Fenster gesamt', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.hull_fenestration_rate = VariableMeta(
            var_name='hull_fenestration_rate', 
            attr_name='hull_fenestration_rate', 
            icon='🧊', 
            label_de='Hüllfläche Fensterflächenanteil', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key=None
        )
        self.hull_m2 = VariableMeta(
            var_name='hull_m2', 
            attr_name='hull_m2', 
            icon='🧊', 
            label_de='Hüllfläche gesamt', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='area', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key=None
        )
        self.lc = VariableMeta(
            var_name='lc', 
            attr_name='lc', 
            icon='🧊', 
            label_de='lc', 
            unit='m', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='geometry', 
            measure='lc', 
            spatial_scope='thermal_hull', 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key=None
        )
        self.hull_transmittance_walls = VariableMeta(
            var_name='hull_transmittance_walls', 
            attr_name='hull_transmittance_walls', 
            icon='🧱', 
            label_de='U-Wert Außenwände', 
            unit='W/m²K', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='wall'
        )
        self.hull_transmittance_roof = VariableMeta(
            var_name='hull_transmittance_roof', 
            attr_name='hull_transmittance_roof', 
            icon='🧱', 
            label_de='U-Wert Dach', 
            unit='W/m²K', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='roof'
        )
        self.hull_transmittance_fundament = VariableMeta(
            var_name='hull_transmittance_fundament', 
            attr_name='hull_transmittance_fundament', 
            icon='🧱', 
            label_de='U-Wert Kellerdecke / Fundament', 
            unit='W/m²K', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.hull_transmittance_windows_north = VariableMeta(
            var_name='hull_transmittance_windows_north', 
            attr_name='hull_transmittance_windows_north', 
            icon='🧱', 
            label_de='U-Wert Fenster Nord', 
            unit='W/m²K', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.hull_transmittance_windows_east = VariableMeta(
            var_name='hull_transmittance_windows_east', 
            attr_name='hull_transmittance_windows_east', 
            icon='🧱', 
            label_de='U-Wert Fenster Ost', 
            unit='W/m²K', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.hull_transmittance_windows_south = VariableMeta(
            var_name='hull_transmittance_windows_south', 
            attr_name='hull_transmittance_windows_south', 
            icon='🧱', 
            label_de='U-Wert Fenster Süd', 
            unit='W/m²K', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.hull_transmittance_windows_west = VariableMeta(
            var_name='hull_transmittance_windows_west', 
            attr_name='hull_transmittance_windows_west', 
            icon='🧱', 
            label_de='U-Wert Fenster West', 
            unit='W/m²K', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.hull_transmittance_windows_horizontal = VariableMeta(
            var_name='hull_transmittance_windows_horizontal', 
            attr_name='hull_transmittance_windows_horizontal', 
            icon='🧱', 
            label_de='U-Wert Fenster Horizontal', 
            unit='W/m²K', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.hull_transmittance_heatbridge = VariableMeta(
            var_name='hull_transmittance_heatbridge', 
            attr_name='hull_transmittance_heatbridge', 
            icon='🧱', 
            label_de='Wärmebrückenzuschlag', 
            unit='ratio', 
            comment='Anteil des Transmissionsleitwerts', 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='transmittance_heatbridge_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.transmittance_walls_Wm2NFA = VariableMeta(
            var_name='transmittance_walls_Wm2NFA', 
            attr_name='transmittance_walls_Wm2NFA', 
            icon='🧱', 
            label_de='Transmissionsleitwert Außenwände', 
            unit='W/m²(NFA)K', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='wall'
        )
        self.transmittance_roof_Wm2NFA = VariableMeta(
            var_name='transmittance_roof_Wm2NFA', 
            attr_name='transmittance_roof_Wm2NFA', 
            icon='🧱', 
            label_de='Transmissionsleitwert Dach', 
            unit='W/m²(NFA)K', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='roof'
        )
        self.transmittance_fundament_Wm2NFA = VariableMeta(
            var_name='transmittance_fundament_Wm2NFA', 
            attr_name='transmittance_fundament_Wm2NFA', 
            icon='🧱', 
            label_de='Transmissionsleitwert Kellerdecke / Fundament', 
            unit='W/m²(NFA)K', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.transmittance_windows_Wm2NFA = VariableMeta(
            var_name='transmittance_windows_Wm2NFA', 
            attr_name='transmittance_windows_Wm2NFA', 
            icon='🧱', 
            label_de='Transmissionsleitwert Fenster', 
            unit='W/m²(NFA)K', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='windows'
        )
        self.transmittance_heatbridge_Wm2NFA = VariableMeta(
            var_name='transmittance_heatbridge_Wm2NFA', 
            attr_name='transmittance_heatbridge_Wm2NFA', 
            icon='🧱', 
            label_de='Transmissionsleitwert Wärmebrücken', 
            unit='W/m²(NFA)K', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance_heatbridge_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.transmittance_MW = VariableMeta(
            var_name='transmittance_MW', 
            attr_name='transmittance_MW', 
            icon='🧱', 
            label_de='Transmissionsleitwert absolut', 
            unit='MW/K', 
            comment='ink. Wärmebrückenzuschlag', 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.transmittance_Wm2 = VariableMeta(
            var_name='transmittance_Wm2', 
            attr_name='transmittance_Wm2', 
            icon='🧱', 
            label_de='Transmissionsleitwert spezifisch', 
            unit='W/m²K', 
            comment='ink. Wärmebrückenzuschlag', 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='transmittance', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.heat_capacity_effective_m = VariableMeta(
            var_name='heat_capacity_effective_m²', 
            attr_name='heat_capacity_effective_m', 
            icon='🧱', 
            label_de='Spezif. wirksame Wärmekapazität', 
            unit='Wh/m²K', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Thermal Hull', 
            measure='heat_capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.heat_cap_eff_uncooled_m2 = VariableMeta(
            var_name='heat_cap_eff_uncooled_m2', 
            attr_name='heat_cap_eff_uncooled_m2', 
            icon='🧱', 
            label_de='Spezif. wirksame Wärmekapazität ungekühlter Bereich', 
            unit='Wh/m²K', 
            comment='Kann separat eingegebn werden', 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='heat_capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.heat_cap_eff_cooled_m2 = VariableMeta(
            var_name='heat_cap_eff_cooled_m2', 
            attr_name='heat_cap_eff_cooled_m2', 
            icon='🧱', 
            label_de='Spezif. wirksame Wärmekapazität gekühlter Bereich', 
            unit='Wh/m²K', 
            comment='Kann separat eingegebn werden', 
            source='IN', 
            ka=0, 
            domain='Thermal Hull', 
            measure='heat_capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.window_total_transmittance_north = VariableMeta(
            var_name='window_total_transmittance_north', 
            attr_name='window_total_transmittance_north', 
            icon='🏢', 
            label_de='g-Wert Fenster Nord', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='solar_gains_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_north'
        )
        self.window_total_transmittance_east = VariableMeta(
            var_name='window_total_transmittance_east', 
            attr_name='window_total_transmittance_east', 
            icon='🏢', 
            label_de='g-Wert Fenster Ost', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='solar_gains_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_east'
        )
        self.window_total_transmittance_south = VariableMeta(
            var_name='window_total_transmittance_south', 
            attr_name='window_total_transmittance_south', 
            icon='🏢', 
            label_de='g-Wert Fenster Süd', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='solar_gains_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_south'
        )
        self.window_total_transmittance_west = VariableMeta(
            var_name='window_total_transmittance_west', 
            attr_name='window_total_transmittance_west', 
            icon='🏢', 
            label_de='g-Wert Fenster West', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='solar_gains_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_west'
        )
        self.window_total_transmittance_horizontal = VariableMeta(
            var_name='window_total_transmittance_horizontal', 
            attr_name='window_total_transmittance_horizontal', 
            icon='🏢', 
            label_de='g-Wert Fenster Horizontal', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='solar_gains_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='hull', 
            entity_key='window_horizontal'
        )
        self.window_irradiation_factor_winter_north = VariableMeta(
            var_name='window_irradiation_factor_winter_north', 
            attr_name='window_irradiation_factor_winter_north', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Fenster Nord', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='window_north'
        )
        self.window_irradiation_factor_winter_east = VariableMeta(
            var_name='window_irradiation_factor_winter_east', 
            attr_name='window_irradiation_factor_winter_east', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Fenster Ost', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='window_east'
        )
        self.window_irradiation_factor_winter_south = VariableMeta(
            var_name='window_irradiation_factor_winter_south', 
            attr_name='window_irradiation_factor_winter_south', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Fenster Süd', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='window_south'
        )
        self.window_irradiation_factor_winter_west = VariableMeta(
            var_name='window_irradiation_factor_winter_west', 
            attr_name='window_irradiation_factor_winter_west', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Fenster West', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='window_west'
        )
        self.window_irradiation_factor_winter_horizontal = VariableMeta(
            var_name='window_irradiation_factor_winter_horizontal', 
            attr_name='window_irradiation_factor_winter_horizontal', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Fenster Horizontal', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='window_horizontal'
        )
        self.window_irradiation_factor_summer_north = VariableMeta(
            var_name='window_irradiation_factor_summer_north', 
            attr_name='window_irradiation_factor_summer_north', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Sommer Nord', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='window_north'
        )
        self.window_irradiation_factor_summer_east = VariableMeta(
            var_name='window_irradiation_factor_summer_east', 
            attr_name='window_irradiation_factor_summer_east', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Sommer Ost', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='window_east'
        )
        self.window_irradiation_factor_summer_south = VariableMeta(
            var_name='window_irradiation_factor_summer_south', 
            attr_name='window_irradiation_factor_summer_south', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Sommer Süd', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='window_south'
        )
        self.window_irradiation_factor_summer_west = VariableMeta(
            var_name='window_irradiation_factor_summer_west', 
            attr_name='window_irradiation_factor_summer_west', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Sommer  West', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='window_west'
        )
        self.window_irradiation_factor_summer_horizontal = VariableMeta(
            var_name='window_irradiation_factor_summer_horizontal', 
            attr_name='window_irradiation_factor_summer_horizontal', 
            icon='🏢', 
            label_de='Einstrahlungsfaktor Sommer  Horizontal', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='window_horizontal'
        )
        self.irradiation_opaque_surcharge = VariableMeta(
            var_name='irradiation_opaque_surcharge', 
            attr_name='irradiation_opaque_surcharge', 
            icon='🏢', 
            label_de='Zuschlag opake Bauteile', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fc_residential = VariableMeta(
            var_name='fc_residential', 
            attr_name='fc_residential', 
            icon='🏢', 
            label_de='Fc-Wert Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.fc_office = VariableMeta(
            var_name='fc_office', 
            attr_name='fc_office', 
            icon='🏢', 
            label_de='Fc-Wert Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.fc_schoolsec = VariableMeta(
            var_name='fc_schoolsec', 
            attr_name='fc_schoolsec', 
            icon='🏢', 
            label_de='Fc-Wert Sekundäre Bildungseinrichtung oder Universität', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.fc_schoolprim = VariableMeta(
            var_name='fc_schoolprim', 
            attr_name='fc_schoolprim', 
            icon='🏢', 
            label_de='Fc-Wert Kindergarten und Volksschule', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.fc_retailfood = VariableMeta(
            var_name='fc_retailfood', 
            attr_name='fc_retailfood', 
            icon='🏢', 
            label_de='Fc-Wert Lebensmittelhandel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.fc_retailother = VariableMeta(
            var_name='fc_retailother', 
            attr_name='fc_retailother', 
            icon='🏢', 
            label_de='Fc-Wert Handel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.fc_other = VariableMeta(
            var_name='fc_other', 
            attr_name='fc_other', 
            icon='🏢', 
            label_de='Fc-Wert Sonstige', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.fc_u = VariableMeta(
            var_name='fc_u', 
            attr_name='fc_u', 
            icon='🏢', 
            label_de='Fc-Wert ungekühlt', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fc_c = VariableMeta(
            var_name='fc_c', 
            attr_name='fc_c', 
            icon='🏢', 
            label_de='Fc-Wert gekühlt', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Solar Gains', 
            measure='shading_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.illuminance_min_residential = VariableMeta(
            var_name='illuminance_min_residential', 
            attr_name='illuminance_min_residential', 
            icon='🏢', 
            label_de='Lux-Wert Wohnen', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.illuminance_min_office = VariableMeta(
            var_name='illuminance_min_office', 
            attr_name='illuminance_min_office', 
            icon='🏢', 
            label_de='Lux-Wert Büro', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.illuminance_min_schoolsec = VariableMeta(
            var_name='illuminance_min_schoolsec', 
            attr_name='illuminance_min_schoolsec', 
            icon='🏢', 
            label_de='Lux-Wert Sekundäre Bildungseinrichtung oder Universität', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.illuminance_min_schoolprim = VariableMeta(
            var_name='illuminance_min_schoolprim', 
            attr_name='illuminance_min_schoolprim', 
            icon='🏢', 
            label_de='Lux-Wert Kindergarten und Volksschule', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.illuminance_min_retailfood = VariableMeta(
            var_name='illuminance_min_retailfood', 
            attr_name='illuminance_min_retailfood', 
            icon='🏢', 
            label_de='Lux-Wert Lebensmittelhandel', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.illuminance_min_retailother = VariableMeta(
            var_name='illuminance_min_retailother', 
            attr_name='illuminance_min_retailother', 
            icon='🏢', 
            label_de='Lux-Wert Handel', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.illuminance_min_other = VariableMeta(
            var_name='illuminance_min_other', 
            attr_name='illuminance_min_other', 
            icon='🏢', 
            label_de='Lux-Wert Sonstige', 
            unit='lux', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='illuminance_min', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.QS_max_shading_u = VariableMeta(
            var_name='QS_max_shading_u', 
            attr_name='QS_max_shading_u', 
            icon='🏢', 
            label_de='Strahlungsschwellenwert Jalousie Ungekühlt', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Solar Gains', 
            measure='max_irradiation', 
            spatial_scope='uncooled', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QS_max_shading_c = VariableMeta(
            var_name='QS_max_shading_c', 
            attr_name='QS_max_shading_c', 
            icon='🏢', 
            label_de='Strahlungsschwellenwert Jalousie Gekühlt', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Solar Gains', 
            measure='max_irradiation', 
            spatial_scope='cooled', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.illuminance_efficiency_dirt = VariableMeta(
            var_name='illuminance_efficiency_dirt', 
            attr_name='illuminance_efficiency_dirt', 
            icon='🏢', 
            label_de='Abminderungsfaktor Verschmutzung', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.illuminance_efficiency_glazing_ratio = VariableMeta(
            var_name='illuminance_efficiency_glazing_ratio', 
            attr_name='illuminance_efficiency_glazing_ratio', 
            icon='🏢', 
            label_de='Abminderungsfaktor Verglasungsanteil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Solar Gains', 
            measure='sgc_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mob_shading_factor_u = VariableMeta(
            var_name='mob_shading_factor_u', 
            attr_name='mob_shading_factor_u', 
            icon='🏢', 
            label_de='Abschattungseffekt Mobiler Sonnenschutz ungekühlt', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Solar Gains', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mob_shading_factor_c = VariableMeta(
            var_name='mob_shading_factor_c', 
            attr_name='mob_shading_factor_c', 
            icon='🏢', 
            label_de='Abschattungseffekt Mobiler Sonnenschutz gekühlt', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Solar Gains', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.vent_air_tightness = VariableMeta(
            var_name='vent_air_tightness', 
            attr_name='vent_air_tightness', 
            icon='💨', 
            label_de='Luftdichtheit n50', 
            unit='1/h', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_tightness', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.vent_tightness_ratio_blowerdoor_to_real = VariableMeta(
            var_name='vent_tightness_ratio_blowerdoor_to_real', 
            attr_name='vent_tightness_ratio_blowerdoor_to_real', 
            icon='💨', 
            label_de='Verhältnis Blower Door / Reale Infiltration', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Ventilation', 
            measure='blowerdoor_to_real', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.vent_infiltration_ACH = VariableMeta(
            var_name='vent_infiltration_ACH', 
            attr_name='vent_infiltration_ACH', 
            icon='💨', 
            label_de='Luftwechsel Infiltration', 
            unit='1/h', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='ach', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.vent_share_mechanical_residential = VariableMeta(
            var_name='vent_share_mechanical_residential', 
            attr_name='vent_share_mechanical_residential', 
            icon='💨', 
            label_de='Mechanische Lüftung Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.vent_share_mechanical_office = VariableMeta(
            var_name='vent_share_mechanical_office', 
            attr_name='vent_share_mechanical_office', 
            icon='💨', 
            label_de='Mechanische Lüftung Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.vent_share_mechanical_schoolsec = VariableMeta(
            var_name='vent_share_mechanical_schoolsec', 
            attr_name='vent_share_mechanical_schoolsec', 
            icon='💨', 
            label_de='Mechanische Lüftung Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.vent_share_mechanical_schoolprim = VariableMeta(
            var_name='vent_share_mechanical_schoolprim', 
            attr_name='vent_share_mechanical_schoolprim', 
            icon='💨', 
            label_de='Mechanische Lüftung Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.vent_share_mechanical_retailfood = VariableMeta(
            var_name='vent_share_mechanical_retailfood', 
            attr_name='vent_share_mechanical_retailfood', 
            icon='💨', 
            label_de='Mechanische Lüftung Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.vent_share_mechanical_retailother = VariableMeta(
            var_name='vent_share_mechanical_retailother', 
            attr_name='vent_share_mechanical_retailother', 
            icon='💨', 
            label_de='Mechanische Lüftung Handel sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.vent_share_mechanical_other = VariableMeta(
            var_name='vent_share_mechanical_other', 
            attr_name='vent_share_mechanical_other', 
            icon='💨', 
            label_de='Mechanische Lüftung Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='mechanical_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.NFA_windowvent = VariableMeta(
            var_name='NFA_windowvent', 
            attr_name='NFA_windowvent', 
            icon='💨', 
            label_de='Fensterlüftung Nettogeschoßfläche', 
            unit='m²NGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFV_windowvent = VariableMeta(
            var_name='NFV_windowvent', 
            attr_name='NFV_windowvent', 
            icon='💨', 
            label_de='Fensterlüftung Raumvolumen', 
            unit='m³netto', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFA_mechvent = VariableMeta(
            var_name='NFA_mechvent', 
            attr_name='NFA_mechvent', 
            icon='💨', 
            label_de='Mechanische Lüftung Nettogeschoßfläche', 
            unit='m²NGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFV_mechvent = VariableMeta(
            var_name='NFV_mechvent', 
            attr_name='NFV_mechvent', 
            icon='💨', 
            label_de='Mechanische Lüftung Raumvolumen', 
            unit='m³netto', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.vent_night_residential = VariableMeta(
            var_name='vent_night_residential', 
            attr_name='vent_night_residential', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Wohnen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.vent_night_office = VariableMeta(
            var_name='vent_night_office', 
            attr_name='vent_night_office', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Büro', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.vent_night_schoolsec = VariableMeta(
            var_name='vent_night_schoolsec', 
            attr_name='vent_night_schoolsec', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Bildung sekundär', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.vent_night_schoolprim = VariableMeta(
            var_name='vent_night_schoolprim', 
            attr_name='vent_night_schoolprim', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Bildung primär', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.vent_night_retailfood = VariableMeta(
            var_name='vent_night_retailfood', 
            attr_name='vent_night_retailfood', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Handel Lebensmittel', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.vent_night_retailother = VariableMeta(
            var_name='vent_night_retailother', 
            attr_name='vent_night_retailother', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Handel sonstiger', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.vent_night_other = VariableMeta(
            var_name='vent_night_other', 
            attr_name='vent_night_other', 
            icon='💨', 
            label_de='Nachtauskühlung Fensterstellung Sonstige Nutzung', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.ACH_night_m = VariableMeta(
            var_name='ACH_night_m³', 
            attr_name='ACH_night_m', 
            icon='💨', 
            label_de='Nachtauskühlung Luftwechsel', 
            unit='m³/h', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.vent_ach_max_residential = VariableMeta(
            var_name='vent_ach_max_residential', 
            attr_name='vent_ach_max_residential', 
            icon='💨', 
            label_de='Luftwechsel Wohnen', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.vent_ach_max_office = VariableMeta(
            var_name='vent_ach_max_office', 
            attr_name='vent_ach_max_office', 
            icon='💨', 
            label_de='Luftwechsel Büro', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.vent_ach_max_schoolsec = VariableMeta(
            var_name='vent_ach_max_schoolsec', 
            attr_name='vent_ach_max_schoolsec', 
            icon='💨', 
            label_de='Luftwechsel Bildung sekundär', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.vent_ach_max_schoolprim = VariableMeta(
            var_name='vent_ach_max_schoolprim', 
            attr_name='vent_ach_max_schoolprim', 
            icon='💨', 
            label_de='Luftwechsel Bildung primär', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.vent_ach_max_retailfood = VariableMeta(
            var_name='vent_ach_max_retailfood', 
            attr_name='vent_ach_max_retailfood', 
            icon='💨', 
            label_de='Luftwechsel Handel Lebensmittel', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.vent_ach_max_retailother = VariableMeta(
            var_name='vent_ach_max_retailother', 
            attr_name='vent_ach_max_retailother', 
            icon='💨', 
            label_de='Luftwechsel Handel sonstiger', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.vent_ach_max_other = VariableMeta(
            var_name='vent_ach_max_other', 
            attr_name='vent_ach_max_other', 
            icon='💨', 
            label_de='Luftwechsel Sonstige Nutzung', 
            unit='1/h', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='air_change', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.vent_scale_residential = VariableMeta(
            var_name='vent_scale_residential', 
            attr_name='vent_scale_residential', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Wohnen', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.vent_scale_office = VariableMeta(
            var_name='vent_scale_office', 
            attr_name='vent_scale_office', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Büro', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.vent_scale_school_sec = VariableMeta(
            var_name='vent_scale_school_sec', 
            attr_name='vent_scale_school_sec', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Bildung sekundär', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.vent_scale_school_prim = VariableMeta(
            var_name='vent_scale_school_prim', 
            attr_name='vent_scale_school_prim', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Bildung primär', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.vent_scale_supermarket = VariableMeta(
            var_name='vent_scale_supermarket', 
            attr_name='vent_scale_supermarket', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Handel Lebensmittel', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.vent_scale_retail = VariableMeta(
            var_name='vent_scale_retail', 
            attr_name='vent_scale_retail', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Handel sonstiger', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.vent_scale_other = VariableMeta(
            var_name='vent_scale_other', 
            attr_name='vent_scale_other', 
            icon='💨', 
            label_de='Skalierung Luftwechsel Sonstige Nutzung', 
            unit='raio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure='air_change_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.Ev_scale_residential = VariableMeta(
            var_name='Ev_scale_residential', 
            attr_name='Ev_scale_residential', 
            icon='💨', 
            label_de='Lüfterstrom mech. Wohnen', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.Ev_scale_office = VariableMeta(
            var_name='Ev_scale_office', 
            attr_name='Ev_scale_office', 
            icon='💨', 
            label_de='Lüfterstrom mech. Büro', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.Ev_scale_school_sec = VariableMeta(
            var_name='Ev_scale_school_sec', 
            attr_name='Ev_scale_school_sec', 
            icon='💨', 
            label_de='Lüfterstrom mech.  Bildung sekundär', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.Ev_scale_school_prim = VariableMeta(
            var_name='Ev_scale_school_prim', 
            attr_name='Ev_scale_school_prim', 
            icon='💨', 
            label_de='Lüfterstrom mech.  Bildung primär', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.Ev_scale_retail_food = VariableMeta(
            var_name='Ev_scale_retail_food', 
            attr_name='Ev_scale_retail_food', 
            icon='💨', 
            label_de='Lüfterstrom mech.  Handel Lebensmittel', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.Ev_scale_retail_other = VariableMeta(
            var_name='Ev_scale_retail_other', 
            attr_name='Ev_scale_retail_other', 
            icon='💨', 
            label_de='Lüfterstrom mech.  Handel sonstiger', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.Ev_scale_other = VariableMeta(
            var_name='Ev_scale_other', 
            attr_name='Ev_scale_other', 
            icon='💨', 
            label_de='Lüfterstrom mech.  Sonstige Nutzung', 
            unit='Anteil', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='el_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.vent_heat_recovery_winter_residential = VariableMeta(
            var_name='vent_heat_recovery_winter_residential', 
            attr_name='vent_heat_recovery_winter_residential', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Wohnen', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.vent_heat_recovery_winter_office = VariableMeta(
            var_name='vent_heat_recovery_winter_office', 
            attr_name='vent_heat_recovery_winter_office', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Büro', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.vent_heat_recovery_winter_schoolsec = VariableMeta(
            var_name='vent_heat_recovery_winter_schoolsec', 
            attr_name='vent_heat_recovery_winter_schoolsec', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Bildung sekundär', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.vent_heat_recovery_winter_schoolprim = VariableMeta(
            var_name='vent_heat_recovery_winter_schoolprim', 
            attr_name='vent_heat_recovery_winter_schoolprim', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Bildung primär', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.vent_heat_recovery_winter_retailfood = VariableMeta(
            var_name='vent_heat_recovery_winter_retailfood', 
            attr_name='vent_heat_recovery_winter_retailfood', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Handel Lebensmittel', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.vent_heat_recovery_winter_retailother = VariableMeta(
            var_name='vent_heat_recovery_winter_retailother', 
            attr_name='vent_heat_recovery_winter_retailother', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Handel sonstiger', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.vent_heat_recovery_winter_other = VariableMeta(
            var_name='vent_heat_recovery_winter_other', 
            attr_name='vent_heat_recovery_winter_other', 
            icon='💨', 
            label_de='Wärmerückgewinnung Winter Sonstige Nutzung', 
            unit='ratio', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.vent_heat_recovery_summer_residential = VariableMeta(
            var_name='vent_heat_recovery_summer_residential', 
            attr_name='vent_heat_recovery_summer_residential', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.vent_heat_recovery_summer_office = VariableMeta(
            var_name='vent_heat_recovery_summer_office', 
            attr_name='vent_heat_recovery_summer_office', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.vent_heat_recovery_summer_schoolsec = VariableMeta(
            var_name='vent_heat_recovery_summer_schoolsec', 
            attr_name='vent_heat_recovery_summer_schoolsec', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.vent_heat_recovery_summer_schoolprim = VariableMeta(
            var_name='vent_heat_recovery_summer_schoolprim', 
            attr_name='vent_heat_recovery_summer_schoolprim', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.vent_heat_recovery_summer_retailfood = VariableMeta(
            var_name='vent_heat_recovery_summer_retailfood', 
            attr_name='vent_heat_recovery_summer_retailfood', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.vent_heat_recovery_summer_retailother = VariableMeta(
            var_name='vent_heat_recovery_summer_retailother', 
            attr_name='vent_heat_recovery_summer_retailother', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Handel sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.vent_heat_recovery_summer_other = VariableMeta(
            var_name='vent_heat_recovery_summer_other', 
            attr_name='vent_heat_recovery_summer_other', 
            icon='💨', 
            label_de='Wärmerückgewinnung Sommer Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Ventilation', 
            measure='heat_recovery_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.Vent_share_window_uncooled = VariableMeta(
            var_name='Vent_share_window_uncooled', 
            attr_name='Vent_share_window_uncooled', 
            icon='💨', 
            label_de='Fensterlüftung Anteil ohne aktive Kühlung', 
            unit=None, 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Vent_share_window_cooled = VariableMeta(
            var_name='Vent_share_window_cooled', 
            attr_name='Vent_share_window_cooled', 
            icon='💨', 
            label_de='Fensterlüftung Anteil mit aktiver Kühlung', 
            unit=None, 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Vent_share_mech_uncooled = VariableMeta(
            var_name='Vent_share_mech_uncooled', 
            attr_name='Vent_share_mech_uncooled', 
            icon='💨', 
            label_de='Quartiersanteil Mechanische Lüftung ohne aktiver Kühlung', 
            unit=None, 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Vent_share_mech_cooled = VariableMeta(
            var_name='Vent_share_mech_cooled', 
            attr_name='Vent_share_mech_cooled', 
            icon='💨', 
            label_de='Quartiersanteil Mechanische Lüftung mit aktiver Kühlung', 
            unit=None, 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.test_NFV_shares = VariableMeta(
            var_name='test_NFV_shares', 
            attr_name='test_NFV_shares', 
            icon='💨', 
            label_de='Test', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Ventilation', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.usage_concurrency_winter_residential = VariableMeta(
            var_name='usage_concurrency_winter_residential', 
            attr_name='usage_concurrency_winter_residential', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.usage_concurrency_winter_office = VariableMeta(
            var_name='usage_concurrency_winter_office', 
            attr_name='usage_concurrency_winter_office', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.usage_concurrency_winter_schoolsec = VariableMeta(
            var_name='usage_concurrency_winter_schoolsec', 
            attr_name='usage_concurrency_winter_schoolsec', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.usage_concurrency_winter_schoolprim = VariableMeta(
            var_name='usage_concurrency_winter_schoolprim', 
            attr_name='usage_concurrency_winter_schoolprim', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.usage_concurrency_winter_retailfood = VariableMeta(
            var_name='usage_concurrency_winter_retailfood', 
            attr_name='usage_concurrency_winter_retailfood', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.usage_concurrency_winter_retailother = VariableMeta(
            var_name='usage_concurrency_winter_retailother', 
            attr_name='usage_concurrency_winter_retailother', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Handel sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.usage_concurrency_winter_other = VariableMeta(
            var_name='usage_concurrency_winter_other', 
            attr_name='usage_concurrency_winter_other', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Winter Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_winter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.usage_concurrency_summer_residential = VariableMeta(
            var_name='usage_concurrency_summer_residential', 
            attr_name='usage_concurrency_summer_residential', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.usage_concurrency_summer_office = VariableMeta(
            var_name='usage_concurrency_summer_office', 
            attr_name='usage_concurrency_summer_office', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.usage_concurrency_summer_schoolsec = VariableMeta(
            var_name='usage_concurrency_summer_schoolsec', 
            attr_name='usage_concurrency_summer_schoolsec', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.usage_concurrency_summer_schoolprim = VariableMeta(
            var_name='usage_concurrency_summer_schoolprim', 
            attr_name='usage_concurrency_summer_schoolprim', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.usage_concurrency_summer_retailfood = VariableMeta(
            var_name='usage_concurrency_summer_retailfood', 
            attr_name='usage_concurrency_summer_retailfood', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.usage_concurrency_summer_retailother = VariableMeta(
            var_name='usage_concurrency_summer_retailother', 
            attr_name='usage_concurrency_summer_retailother', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Handel sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.usage_concurrency_summer_other = VariableMeta(
            var_name='usage_concurrency_summer_other', 
            attr_name='usage_concurrency_summer_other', 
            icon='👤', 
            label_de='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_summer', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.DHW_demand_residential_kWhm2 = VariableMeta(
            var_name='DHW_demand_residential_kWhm2', 
            attr_name='DHW_demand_residential_kWhm2', 
            icon='👤', 
            label_de='WWWB Wohnen', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.DHW_demand_office_kWhm2 = VariableMeta(
            var_name='DHW_demand_office_kWhm2', 
            attr_name='DHW_demand_office_kWhm2', 
            icon='👤', 
            label_de='WWWB Büro', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.DHW_demand_schoolsec_kWhm2 = VariableMeta(
            var_name='DHW_demand_schoolsec_kWhm2', 
            attr_name='DHW_demand_schoolsec_kWhm2', 
            icon='👤', 
            label_de='WWWB Bildung sekundär', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.DHW_demand_schoolprim_kWhm2 = VariableMeta(
            var_name='DHW_demand_schoolprim_kWhm2', 
            attr_name='DHW_demand_schoolprim_kWhm2', 
            icon='👤', 
            label_de='WWWB Bildung primär', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.DHW_demand_retailfood_kWhm2 = VariableMeta(
            var_name='DHW_demand_retailfood_kWhm2', 
            attr_name='DHW_demand_retailfood_kWhm2', 
            icon='👤', 
            label_de='WWWB Handel Lebensmittel', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.DHW_demand_retailother_kWhm2 = VariableMeta(
            var_name='DHW_demand_retailother_kWhm2', 
            attr_name='DHW_demand_retailother_kWhm2', 
            icon='👤', 
            label_de='WWWB Handel sonstiger', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.DHW_demand_other_kWhm2 = VariableMeta(
            var_name='DHW_demand_other_kWhm2', 
            attr_name='DHW_demand_other_kWhm2', 
            icon='👤', 
            label_de='WWWB Sonstige Nutzung', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.aux_el_demand_residential_kWhm2 = VariableMeta(
            var_name='aux_el_demand_residential_kWhm2', 
            attr_name='aux_el_demand_residential_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Wohnen', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.aux_el_demand_office_kWhm2 = VariableMeta(
            var_name='aux_el_demand_office_kWhm2', 
            attr_name='aux_el_demand_office_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Büro', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.aux_el_demand_schoolsec_kWhm2 = VariableMeta(
            var_name='aux_el_demand_schoolsec_kWhm2', 
            attr_name='aux_el_demand_schoolsec_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Bildung sekundär', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.aux_el_demand_schoolprim_kWhm2 = VariableMeta(
            var_name='aux_el_demand_schoolprim_kWhm2', 
            attr_name='aux_el_demand_schoolprim_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Bildung primär', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.aux_el_demand_retailfood_kWhm2 = VariableMeta(
            var_name='aux_el_demand_retailfood_kWhm2', 
            attr_name='aux_el_demand_retailfood_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Handel lebensmittel', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.aux_el_demand_retailother_kWhm2 = VariableMeta(
            var_name='aux_el_demand_retailother_kWhm2', 
            attr_name='aux_el_demand_retailother_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Handel sonstiger', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.aux_el_demand_other_kWhm2 = VariableMeta(
            var_name='aux_el_demand_other_kWhm2', 
            attr_name='aux_el_demand_other_kWhm2', 
            icon='👤', 
            label_de='Allgemeinstrom Sonstige Nutzung', 
            unit='kWh/m²NGFa', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='aux_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.Plugloads_scale_residential = VariableMeta(
            var_name='Plugloads_scale_residential', 
            attr_name='Plugloads_scale_residential', 
            icon='👤', 
            label_de='Nutzerstrom Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.Plugloads_scale_office = VariableMeta(
            var_name='Plugloads_scale_office', 
            attr_name='Plugloads_scale_office', 
            icon='👤', 
            label_de='Nutzerstrom Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.Plugloads_scale_schoolsec = VariableMeta(
            var_name='Plugloads_scale_schoolsec', 
            attr_name='Plugloads_scale_schoolsec', 
            icon='👤', 
            label_de='Nutzerstrom Bildung sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.Plugloads_scale_schoolprim = VariableMeta(
            var_name='Plugloads_scale_schoolprim', 
            attr_name='Plugloads_scale_schoolprim', 
            icon='👤', 
            label_de='Nutzerstrom Bildung primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.Plugloads_scale_retailfood = VariableMeta(
            var_name='Plugloads_scale_retailfood', 
            attr_name='Plugloads_scale_retailfood', 
            icon='👤', 
            label_de='Nutzerstrom Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.Plugloads_scale_retailother = VariableMeta(
            var_name='Plugloads_scale_retailother', 
            attr_name='Plugloads_scale_retailother', 
            icon='👤', 
            label_de='Nutzerstrom Handel sonstiger', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.Plugloads_scale_other = VariableMeta(
            var_name='Plugloads_scale_other', 
            attr_name='Plugloads_scale_other', 
            icon='👤', 
            label_de='Nutzerstrom Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='plugload_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.density_NFApPers_residential = VariableMeta(
            var_name='density_NFApPers_residential', 
            attr_name='density_NFApPers_residential', 
            icon='🚗', 
            label_de='Belegungsdichte Wohnen', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.density_NFApPers_office = VariableMeta(
            var_name='density_NFApPers_office', 
            attr_name='density_NFApPers_office', 
            icon='🚗', 
            label_de='Belegungsdichte Büro', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.density_NFApPers_schoolsec = VariableMeta(
            var_name='density_NFApPers_schoolsec', 
            attr_name='density_NFApPers_schoolsec', 
            icon='🚗', 
            label_de='Belegungsdichte Ausbildung Sekundär', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.density_NFApPers_retail = VariableMeta(
            var_name='density_NFApPers_retail', 
            attr_name='density_NFApPers_retail', 
            icon='🚗', 
            label_de='Belegungsdichte Handel Supermarkt', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.density_NFApPers_schoolprim = VariableMeta(
            var_name='density_NFApPers_schoolprim', 
            attr_name='density_NFApPers_schoolprim', 
            icon='🚗', 
            label_de='Belegungsdichte Ausbildung Primär', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.density_NFApPers_retail_other = VariableMeta(
            var_name='density_NFApPers_retail_other', 
            attr_name='density_NFApPers_retail_other', 
            icon='🚗', 
            label_de='Belegungsdichte Handel Sonstige', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.mob_simultaneity_edu = VariableMeta(
            var_name='mob_simultaneity_edu', 
            attr_name='mob_simultaneity_edu', 
            icon='🚗', 
            label_de='Gleichzeitigkeitsfaktorsfaktor Ausbildung', 
            unit=None, 
            comment='1 statistische Nutzer ist x realer Nutzer zwecks Wege, die ins Quartier führen)', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_mobility', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='education'
        )
        self.mob_simultaneity_retail = VariableMeta(
            var_name='mob_simultaneity_retail', 
            attr_name='mob_simultaneity_retail', 
            icon='🚗', 
            label_de='Gleichzeitigkeitsfaktorsfaktor Einkaufen', 
            unit=None, 
            comment='wieviele Verkaufsflchen werden von mehreren Nutzern aufgesucht?', 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='concurrency_mobility', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='retail'
        )
        self.mob_simultaneity_office = VariableMeta(
            var_name='mob_simultaneity_office', 
            attr_name='mob_simultaneity_office', 
            icon='🚗', 
            label_de='Gleichzetigkeitsfaktor Arbeit', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='concurrency_mobility', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='work'
        )
        self.mob_motorization_perNFA_residential = VariableMeta(
            var_name='mob_motorization_perNFA_residential', 
            attr_name='mob_motorization_perNFA_residential', 
            icon='🚗', 
            label_de='Autos pro Nutzung Wohnen', 
            unit='1/100m²', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='education'
        )
        self.mob_motorization_perNFA_work = VariableMeta(
            var_name='mob_motorization_perNFA_work', 
            attr_name='mob_motorization_perNFA_work', 
            icon='🚗', 
            label_de='Autos pro Nutzung Arbeit', 
            unit='1/100m²', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='retail'
        )
        self.mob_motorization_perNFA_retail = VariableMeta(
            var_name='mob_motorization_perNFA_retail', 
            attr_name='mob_motorization_perNFA_retail', 
            icon='🚗', 
            label_de='Autos pro Nutzung Einkaufen', 
            unit='1/100m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='work'
        )
        self.Plight_max_office = VariableMeta(
            var_name='Plight_max_office', 
            attr_name='Plight_max_office', 
            icon='💡', 
            label_de='Beleuchtung maximal Büro', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_power_max', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.Plight_max_schoolsec = VariableMeta(
            var_name='Plight_max_schoolsec', 
            attr_name='Plight_max_schoolsec', 
            icon='💡', 
            label_de='Beleuchtung maximal Ausbildung Sekundär', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_power_max', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.Plight_max_schoolprim = VariableMeta(
            var_name='Plight_max_schoolprim', 
            attr_name='Plight_max_schoolprim', 
            icon='💡', 
            label_de='Beleuchtung maximal Ausbildung Primär', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_power_max', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.Plight_min_office = VariableMeta(
            var_name='Plight_min_office', 
            attr_name='Plight_min_office', 
            icon='💡', 
            label_de='Beleuchtung minimal Büro', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_power_max', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.Plight_min_schoolsec = VariableMeta(
            var_name='Plight_min_schoolsec', 
            attr_name='Plight_min_schoolsec', 
            icon='💡', 
            label_de='Beleuchtung minimal Ausbildung Sekundär', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_power_max', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.Plight_min_schoolprim = VariableMeta(
            var_name='Plight_min_schoolprim', 
            attr_name='Plight_min_schoolprim', 
            icon='💡', 
            label_de='Beleuchtung minimal Ausbildung Primär', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_power_max', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.lighting_factor_office = VariableMeta(
            var_name='lighting_factor_office', 
            attr_name='lighting_factor_office', 
            icon='💡', 
            label_de='Beleuchtung Skalierung Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.lighting_factor_schoolsec = VariableMeta(
            var_name='lighting_factor_schoolsec', 
            attr_name='lighting_factor_schoolsec', 
            icon='💡', 
            label_de='Beleuchtung Skalierung Ausbildung Sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.lighting_factor_schoolprim = VariableMeta(
            var_name='lighting_factor_schoolprim', 
            attr_name='lighting_factor_schoolprim', 
            icon='💡', 
            label_de='Beleuchtung Skalierung Ausbildung Primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.lighting_factor_retailfood = VariableMeta(
            var_name='lighting_factor_retailfood', 
            attr_name='lighting_factor_retailfood', 
            icon='💡', 
            label_de='Beleuchtung Skalierung Handel Food', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.lighting_factor_retailother = VariableMeta(
            var_name='lighting_factor_retailother', 
            attr_name='lighting_factor_retailother', 
            icon='💡', 
            label_de='Beleuchtung Skalierung handel Non-Food', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.lighting_factor_other = VariableMeta(
            var_name='lighting_factor_other', 
            attr_name='lighting_factor_other', 
            icon='💡', 
            label_de='Beleuchtung Skalierung Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='lighting_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.Daylightcoefficient_office = VariableMeta(
            var_name='Daylightcoefficient_office', 
            attr_name='Daylightcoefficient_office', 
            icon='💡', 
            label_de='Tageslichtkoeffizient Büro', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='daylight_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.Daylightcoefficient_schoolsec = VariableMeta(
            var_name='Daylightcoefficient_schoolsec', 
            attr_name='Daylightcoefficient_schoolsec', 
            icon='💡', 
            label_de='Tageslichtkoeffizient Ausbildung Sekundär', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='daylight_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.Daylightcoefficient_schoolprim = VariableMeta(
            var_name='Daylightcoefficient_schoolprim', 
            attr_name='Daylightcoefficient_schoolprim', 
            icon='💡', 
            label_de='Tageslichtkoeffizient Ausbildung Primär', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Space Use', 
            measure='daylight_coefficient', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.daylightcontr_office = VariableMeta(
            var_name='daylightcontr_office', 
            attr_name='daylightcontr_office', 
            icon='💡', 
            label_de='Anteil Tageslichtgesteuert Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='daylight_control_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.daylightcontr_schoolsec = VariableMeta(
            var_name='daylightcontr_schoolsec', 
            attr_name='daylightcontr_schoolsec', 
            icon='💡', 
            label_de='Anteil Tageslichtgesteuert Ausbildung Sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='daylight_control_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.daylightcontr_schoolprim = VariableMeta(
            var_name='daylightcontr_schoolprim', 
            attr_name='daylightcontr_schoolprim', 
            icon='💡', 
            label_de='Anteil Tageslichtgesteuert Ausbildung Primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Space Use', 
            measure='daylight_control_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.heating_month1 = VariableMeta(
            var_name='heating_month1', 
            attr_name='heating_month1', 
            icon='♨️', 
            label_de='Heizperiode Jänner', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month2 = VariableMeta(
            var_name='heating_month2', 
            attr_name='heating_month2', 
            icon='♨️', 
            label_de='Heizperiode Februar', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month3 = VariableMeta(
            var_name='heating_month3', 
            attr_name='heating_month3', 
            icon='♨️', 
            label_de='Heizperiode März', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month4 = VariableMeta(
            var_name='heating_month4', 
            attr_name='heating_month4', 
            icon='♨️', 
            label_de='Heizperiode April', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month5 = VariableMeta(
            var_name='heating_month5', 
            attr_name='heating_month5', 
            icon='♨️', 
            label_de='Heizperiode Mai', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month6 = VariableMeta(
            var_name='heating_month6', 
            attr_name='heating_month6', 
            icon='♨️', 
            label_de='Heizperiode Juni', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month7 = VariableMeta(
            var_name='heating_month7', 
            attr_name='heating_month7', 
            icon='♨️', 
            label_de='Heizperiode Juli', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month8 = VariableMeta(
            var_name='heating_month8', 
            attr_name='heating_month8', 
            icon='♨️', 
            label_de='Heizperiode August', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month9 = VariableMeta(
            var_name='heating_month9', 
            attr_name='heating_month9', 
            icon='♨️', 
            label_de='Heizperiode September', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month10 = VariableMeta(
            var_name='heating_month10', 
            attr_name='heating_month10', 
            icon='♨️', 
            label_de='Heizperiode Oktober', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month11 = VariableMeta(
            var_name='heating_month11', 
            attr_name='heating_month11', 
            icon='♨️', 
            label_de='Heizperiode November', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.heating_month12 = VariableMeta(
            var_name='heating_month12', 
            attr_name='heating_month12', 
            icon='♨️', 
            label_de='Heizperiode Dezember', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='is_heating_period', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QHmax_room_m = VariableMeta(
            var_name='QHmax_room_m²', 
            attr_name='QHmax_room_m', 
            icon='♨️', 
            label_de='spez. thermische Leistung Abgabesystem', 
            unit='W/m²', 
            comment='raumseitig', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='emission_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QHmax_room_MW = VariableMeta(
            var_name='QHmax_room_MW', 
            attr_name='QHmax_room_MW', 
            icon='♨️', 
            label_de='Thermische Leistung Abgabesystem', 
            unit='MW', 
            comment='raumseitig', 
            source='IN', 
            ka=0, 
            domain='Heating', 
            measure='emission_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QHmax_1el_m2 = VariableMeta(
            var_name='QHmax_1el_m2', 
            attr_name='QHmax_1el_m2', 
            icon='♨️', 
            label_de='Thermische Leistung HZEL1', 
            unit='W/m²', 
            comment='raumseitig, Elektrische Heizung PRIO1', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_1'
        )
        self.QHmax_2th_m2 = VariableMeta(
            var_name='QHmax_2th_m2', 
            attr_name='QHmax_2th_m2', 
            icon='♨️', 
            label_de='Thermische Leistung HZTH2', 
            unit='W/m²', 
            comment='raumseitig, thermische Heizung PRIO 2', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.QHmax_3el_m2 = VariableMeta(
            var_name='QHmax_3el_m2', 
            attr_name='QHmax_3el_m2', 
            icon='♨️', 
            label_de='Thermische Leistung HZEL3', 
            unit='W/m²', 
            comment='raumseitig, Elektrisch, PRIO3', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_3'
        )
        self.QHmax_4th_m2 = VariableMeta(
            var_name='QHmax_4th_m2', 
            attr_name='QHmax_4th_m2', 
            icon='♨️', 
            label_de='Thermische Leistung HZTH4', 
            unit='W/m²', 
            comment='raumseitig, thermisch PRIO4', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.QH_distr_loss_1el = VariableMeta(
            var_name='QH_distr_loss_1el', 
            attr_name='QH_distr_loss_1el', 
            icon='♨️', 
            label_de='Verteilverluste HZEL1', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_1'
        )
        self.QH_distr_loss_2th = VariableMeta(
            var_name='QH_distr_loss_2th', 
            attr_name='QH_distr_loss_2th', 
            icon='♨️', 
            label_de='Verteilverluste HZTH2', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.QH_distr_loss_3el = VariableMeta(
            var_name='QH_distr_loss_3el', 
            attr_name='QH_distr_loss_3el', 
            icon='♨️', 
            label_de='Verteilverluste HZEL3', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_3'
        )
        self.QH_distr_loss_4th = VariableMeta(
            var_name='QH_distr_loss_4th', 
            attr_name='QH_distr_loss_4th', 
            icon='♨️', 
            label_de='Verteilverluste HZTH4', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.heat_cop_1el = VariableMeta(
            var_name='heat_cop_1el', 
            attr_name='heat_cop_1el', 
            icon='♨️', 
            label_de='Wirkungsgrad Erzeugung HZEL1', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_1'
        )
        self.heat_cop_2th = VariableMeta(
            var_name='heat_cop_2th', 
            attr_name='heat_cop_2th', 
            icon='♨️', 
            label_de='Wirkungsgrad Erzeugung HZTH2', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.heat_cop_3el = VariableMeta(
            var_name='heat_cop_3el', 
            attr_name='heat_cop_3el', 
            icon='♨️', 
            label_de='Wirkungsgrad Erzeugung HZEL3', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_3'
        )
        self.heat_cop_4th = VariableMeta(
            var_name='heat_cop_4th', 
            attr_name='heat_cop_4th', 
            icon='♨️', 
            label_de='Wirkungsgrad Erzeugung HZTH4', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.QH_generation_eff_1el = VariableMeta(
            var_name='QH_generation_eff_1el', 
            attr_name='QH_generation_eff_1el', 
            icon='♨️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung HZEL1', 
            unit='ratio', 
            comment='weil schneller als divison durch Wirkugsgrad', 
            source='IN', 
            ka=0, 
            domain='Heating', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_1'
        )
        self.QH_generation_eff_2th = VariableMeta(
            var_name='QH_generation_eff_2th', 
            attr_name='QH_generation_eff_2th', 
            icon='♨️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung HZTH2', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Heating', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.QH_generation_eff_3el = VariableMeta(
            var_name='QH_generation_eff_3el', 
            attr_name='QH_generation_eff_3el', 
            icon='♨️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung HZEL3', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Heating', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_3'
        )
        self.QH_generation_eff_4th = VariableMeta(
            var_name='QH_generation_eff_4th', 
            attr_name='QH_generation_eff_4th', 
            icon='♨️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung HZTH4', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Heating', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.QH_aux_wasteheat = VariableMeta(
            var_name='QH_aux_wasteheat', 
            attr_name='QH_aux_wasteheat', 
            icon='♨️', 
            label_de='Hilfsstromanteil HZAbwärme', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Heating', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QH_aux_el_to_th_1el = VariableMeta(
            var_name='QH_aux_el_to_th_1el', 
            attr_name='QH_aux_el_to_th_1el', 
            icon='♨️', 
            label_de='Hilfsstromanteil HZEL1', 
            unit='ratio', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_1'
        )
        self.QH_aux_el_to_th_2th = VariableMeta(
            var_name='QH_aux_el_to_th_2th', 
            attr_name='QH_aux_el_to_th_2th', 
            icon='♨️', 
            label_de='Hilfsstromanteil HZTH2', 
            unit='ratio', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.QH_aux_el_to_th_3el = VariableMeta(
            var_name='QH_aux_el_to_th_3el', 
            attr_name='QH_aux_el_to_th_3el', 
            icon='♨️', 
            label_de='Hilfsstromanteil HZEL3', 
            unit='ratio', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_3'
        )
        self.QH_aux_el_to_th_4th = VariableMeta(
            var_name='QH_aux_el_to_th_4th', 
            attr_name='QH_aux_el_to_th_4th', 
            icon='♨️', 
            label_de='Hilfsstromanteil HZTH4', 
            unit='ratio', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.heat_th2_carrier_type = VariableMeta(
            var_name='heat_th2_carrier_type', 
            attr_name='heat_th2_carrier_type', 
            icon='♨️', 
            label_de='Energieträger HZTH2', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='carrier_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.heat_th4_carrier_type = VariableMeta(
            var_name='heat_th4_carrier_type', 
            attr_name='heat_th4_carrier_type', 
            icon='♨️', 
            label_de='Energieträger HZTH4', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='carrier_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.Tsetheat_min = VariableMeta(
            var_name='Tsetheat_min', 
            attr_name='Tsetheat_min', 
            icon='♨️', 
            label_de='Heizen Raumtemperatur Minimum', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Heating', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month1 = VariableMeta(
            var_name='cooling_month1', 
            attr_name='cooling_month1', 
            icon='❄️', 
            label_de='Kühlperiode Jänner', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month2 = VariableMeta(
            var_name='cooling_month2', 
            attr_name='cooling_month2', 
            icon='❄️', 
            label_de='Kühlperiode Februar', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month3 = VariableMeta(
            var_name='cooling_month3', 
            attr_name='cooling_month3', 
            icon='❄️', 
            label_de='Kühlperiode März', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month4 = VariableMeta(
            var_name='cooling_month4', 
            attr_name='cooling_month4', 
            icon='❄️', 
            label_de='Kühlperiode April', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month5 = VariableMeta(
            var_name='cooling_month5', 
            attr_name='cooling_month5', 
            icon='❄️', 
            label_de='Kühlperiode Mai', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month6 = VariableMeta(
            var_name='cooling_month6', 
            attr_name='cooling_month6', 
            icon='❄️', 
            label_de='Kühlperiode Juni', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month7 = VariableMeta(
            var_name='cooling_month7', 
            attr_name='cooling_month7', 
            icon='❄️', 
            label_de='Kühlperiode Juli', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month8 = VariableMeta(
            var_name='cooling_month8', 
            attr_name='cooling_month8', 
            icon='❄️', 
            label_de='Kühlperiode August', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month9 = VariableMeta(
            var_name='cooling_month9', 
            attr_name='cooling_month9', 
            icon='❄️', 
            label_de='Kühlperiode September', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month10 = VariableMeta(
            var_name='cooling_month10', 
            attr_name='cooling_month10', 
            icon='❄️', 
            label_de='Kühlperiode Oktober', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month11 = VariableMeta(
            var_name='cooling_month11', 
            attr_name='cooling_month11', 
            icon='❄️', 
            label_de='Kühlperiode November', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cooling_month12 = VariableMeta(
            var_name='cooling_month12', 
            attr_name='cooling_month12', 
            icon='❄️', 
            label_de='Kühlperiode Dezember', 
            unit='Bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='is_cooling_period', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.cool_share_residential = VariableMeta(
            var_name='cool_share_residential', 
            attr_name='cool_share_residential', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.cool_share_office = VariableMeta(
            var_name='cool_share_office', 
            attr_name='cool_share_office', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.cool_share_schoolsec = VariableMeta(
            var_name='cool_share_schoolsec', 
            attr_name='cool_share_schoolsec', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Schule sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.cool_share_schoolprim = VariableMeta(
            var_name='cool_share_schoolprim', 
            attr_name='cool_share_schoolprim', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Schule primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.cool_share_retailfood = VariableMeta(
            var_name='cool_share_retailfood', 
            attr_name='cool_share_retailfood', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.cool_share_retailother = VariableMeta(
            var_name='cool_share_retailother', 
            attr_name='cool_share_retailother', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Handel Sonstige', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.cool_share_other = VariableMeta(
            var_name='cool_share_other', 
            attr_name='cool_share_other', 
            icon='❄️', 
            label_de='Aktive Kühlung Anteil Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.NFA_cooled = VariableMeta(
            var_name='NFA_cooled', 
            attr_name='NFA_cooled', 
            icon='❄️', 
            label_de='Fläche Aktive Kühlung', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='area', 
            spatial_scope='cooled', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFAfrac_c = VariableMeta(
            var_name='NFAfrac_c', 
            attr_name='NFAfrac_c', 
            icon='❄️', 
            label_de='NGF Anteil Aktive Kühlung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='active_cooling_share', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.NFAfrac_u = VariableMeta(
            var_name='NFAfrac_u', 
            attr_name='NFAfrac_u', 
            icon='❄️', 
            label_de='NGF Anteil ohne aktive Kühlung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='passive_cooling_shar', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QCmax_room_m2 = VariableMeta(
            var_name='QCmax_room_m2', 
            attr_name='QCmax_room_m2', 
            icon='❄️', 
            label_de='spez. thermische Leistung Aufnahmesystem', 
            unit='W/m²', 
            comment='raumseitig', 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='emission_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QCmax_room_MW = VariableMeta(
            var_name='QCmax_room_MW', 
            attr_name='QCmax_room_MW', 
            icon='❄️', 
            label_de='Thermische Leistung Aufnahmesystem', 
            unit='MW', 
            comment='raumseitig', 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='emission_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QCmax_freecooling = VariableMeta(
            var_name='QCmax_freecooling', 
            attr_name='QCmax_freecooling', 
            icon='❄️', 
            label_de='Thermische Leistung Freecooling', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key=None
        )
        self.QCmax_1el = VariableMeta(
            var_name='QCmax_1el', 
            attr_name='QCmax_1el', 
            icon='❄️', 
            label_de='Thermische Leistung 1 EL', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_1'
        )
        self.QCmax_2th = VariableMeta(
            var_name='QCmax_2th', 
            attr_name='QCmax_2th', 
            icon='❄️', 
            label_de='Thermische Leistung 2 TH', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.QCmax_3el = VariableMeta(
            var_name='QCmax_3el', 
            attr_name='QCmax_3el', 
            icon='❄️', 
            label_de='Thermische Leistung 3 EL', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_3'
        )
        self.QC_distr_losses_1el = VariableMeta(
            var_name='QC_distr_losses_1el', 
            attr_name='QC_distr_losses_1el', 
            icon='❄️', 
            label_de='Verteilverluste 1 El', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_1'
        )
        self.QC_distr_losses_2th = VariableMeta(
            var_name='QC_distr_losses_2th', 
            attr_name='QC_distr_losses_2th', 
            icon='❄️', 
            label_de='Verteilverluste 2th', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.QC_distr_losses_3el = VariableMeta(
            var_name='QC_distr_losses_3el', 
            attr_name='QC_distr_losses_3el', 
            icon='❄️', 
            label_de='Verteilverluste 3el', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='distribution_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_3'
        )
        self.cool_cop_1el = VariableMeta(
            var_name='cool_cop_1el', 
            attr_name='cool_cop_1el', 
            icon='❄️', 
            label_de='Wirkungsgrad Erzeugung 1 El', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_1'
        )
        self.cool_cop_2th = VariableMeta(
            var_name='cool_cop_2th', 
            attr_name='cool_cop_2th', 
            icon='❄️', 
            label_de='Wirkungsgrad Erzeugung 2 TH', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.cool_cop_3el = VariableMeta(
            var_name='cool_cop_3el', 
            attr_name='cool_cop_3el', 
            icon='❄️', 
            label_de='Wirkungsgrad Erzeugung 3 EL', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_3'
        )
        self.QC_to_EC_1 = VariableMeta(
            var_name='QC_to_EC_1', 
            attr_name='QC_to_EC_1', 
            icon='❄️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung 1 El', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_1'
        )
        self.QC_generation_eff_2th = VariableMeta(
            var_name='QC_generation_eff_2th', 
            attr_name='QC_generation_eff_2th', 
            icon='❄️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung 2 TH', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.QC_to_EC_3 = VariableMeta(
            var_name='QC_to_EC_3', 
            attr_name='QC_to_EC_3', 
            icon='❄️', 
            label_de='Wirkungsgrad-Kehrwert Erzeugung 3 EL', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Cooling', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_3'
        )
        self.QC_aux_fc = VariableMeta(
            var_name='QC_aux_fc', 
            attr_name='QC_aux_fc', 
            icon='❄️', 
            label_de='Hilfsstromanteil Freecooling', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key=None
        )
        self.QC_aux_1el = VariableMeta(
            var_name='QC_aux_1el', 
            attr_name='QC_aux_1el', 
            icon='❄️', 
            label_de='Hilfsstromanteil KLEL1', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_1'
        )
        self.QC_aux_2th = VariableMeta(
            var_name='QC_aux_2th', 
            attr_name='QC_aux_2th', 
            icon='❄️', 
            label_de='Hilfsstromanteil KLTh2', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.QC_aux_3el = VariableMeta(
            var_name='QC_aux_3el', 
            attr_name='QC_aux_3el', 
            icon='❄️', 
            label_de='Hilfsstromanteil KLEL3', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_3'
        )
        self.cool_th2_carrier_type = VariableMeta(
            var_name='cool_th2_carrier_type', 
            attr_name='cool_th2_carrier_type', 
            icon='❄️', 
            label_de='Energieträger System 2 Thermisch', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='carrier_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.Tsetcool_max = VariableMeta(
            var_name='Tsetcool_max', 
            attr_name='Tsetcool_max', 
            icon='❄️', 
            label_de='Kühlen Solltemperatur Maximum', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Cooling', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_Tmin = VariableMeta(
            var_name='DHW_Tmin', 
            attr_name='DHW_Tmin', 
            icon='💧', 
            label_de='Temperatur Minimum', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_Tmax_input = VariableMeta(
            var_name='DHW_Tmax_input', 
            attr_name='DHW_Tmax_input', 
            icon='💧', 
            label_de='Temperatur Maximum Eingabe', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_Tmax = VariableMeta(
            var_name='DHW_Tmax', 
            attr_name='DHW_Tmax', 
            icon='💧', 
            label_de='Temperatur Maximum Effektiv', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_1_share_residential = VariableMeta(
            var_name='DHW_1_share_residential', 
            attr_name='DHW_1_share_residential', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.DHW_1_share_office = VariableMeta(
            var_name='DHW_1_share_office', 
            attr_name='DHW_1_share_office', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.DHW_1_share_schoolsec = VariableMeta(
            var_name='DHW_1_share_schoolsec', 
            attr_name='DHW_1_share_schoolsec', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Schule sekundär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.DHW_1_share_schoolprim = VariableMeta(
            var_name='DHW_1_share_schoolprim', 
            attr_name='DHW_1_share_schoolprim', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Schule primär', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.DHW_1_share_retailfood = VariableMeta(
            var_name='DHW_1_share_retailfood', 
            attr_name='DHW_1_share_retailfood', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Handel Lebensmittel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.DHW_1_share_retailother = VariableMeta(
            var_name='DHW_1_share_retailother', 
            attr_name='DHW_1_share_retailother', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Handel Sonstige', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.DHW_1_share_other = VariableMeta(
            var_name='DHW_1_share_other', 
            attr_name='DHW_1_share_other', 
            icon='💧', 
            label_de='Warmwasser System 1 Anteil Sonstige Nutzung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='system_1_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.DHW_storage_1_liter = VariableMeta(
            var_name='DHW_storage_1_liter', 
            attr_name='DHW_storage_1_liter', 
            icon='💧', 
            label_de='Warmwasser-Speichergröße 1', 
            unit='liter', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_storage_2_liter = VariableMeta(
            var_name='DHW_storage_2_liter', 
            attr_name='DHW_storage_2_liter', 
            icon='💧', 
            label_de='Warmwasser-Speichergröße 2', 
            unit='liter', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_1_is_used = VariableMeta(
            var_name='DHW_1_is_used', 
            attr_name='DHW_1_is_used', 
            icon='💧', 
            label_de='Warmwasser System 1 in Verwendung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='system_used', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_2_is_used = VariableMeta(
            var_name='DHW_2_is_used', 
            attr_name='DHW_2_is_used', 
            icon='💧', 
            label_de='Warmwasser System 2 in Verwendung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='system_used', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_thermal_power_1_kW = VariableMeta(
            var_name='DHW_thermal_power_1_kW', 
            attr_name='DHW_thermal_power_1_kW', 
            icon='💧', 
            label_de='Warmwasser Ladeleistung 1', 
            unit='kW', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_losses_1 = VariableMeta(
            var_name='DHW_losses_1', 
            attr_name='DHW_losses_1', 
            icon='💧', 
            label_de='Warmwasser Verluste: Speicher1', 
            unit='1/h', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='storage_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_losses_2 = VariableMeta(
            var_name='DHW_losses_2', 
            attr_name='DHW_losses_2', 
            icon='💧', 
            label_de='Warmwasser Verluste: Speicher2', 
            unit='1/h', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='storage_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_efficiency_distribution_1 = VariableMeta(
            var_name='DHW_efficiency_distribution_1', 
            attr_name='DHW_efficiency_distribution_1', 
            icon='💧', 
            label_de='Warmwasser Verluste: Wirkungsgrad Verteilsystem 1', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='distribution_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_efficiency_distribution_2 = VariableMeta(
            var_name='DHW_efficiency_distribution_2', 
            attr_name='DHW_efficiency_distribution_2', 
            icon='💧', 
            label_de='Warmwasser Verluste: Wirkungsgrad Verteilsystem 2', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='distribution_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_1_incl_distribution_factor = VariableMeta(
            var_name='DHW_1_incl_distribution_factor', 
            attr_name='DHW_1_incl_distribution_factor', 
            icon='💧', 
            label_de='Warmwasser Verlustaufschlag Verteilsystem 1', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='distribution_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_2_incl_distribution_factor = VariableMeta(
            var_name='DHW_2_incl_distribution_factor', 
            attr_name='DHW_2_incl_distribution_factor', 
            icon='💧', 
            label_de='Warmwasser Verlustaufschlag Verteilsystem 2', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='distribution_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_carriertype_1 = VariableMeta(
            var_name='DHW_carriertype_1', 
            attr_name='DHW_carriertype_1', 
            icon='💧', 
            label_de='Warmwasser System 1 Energieträger', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='carrier_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_1_is_electric = VariableMeta(
            var_name='DHW_1_is_electric', 
            attr_name='DHW_1_is_electric', 
            icon='💧', 
            label_de='Warmwasser System 1 ist elektrisch', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='is_electric', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_carriertype_2 = VariableMeta(
            var_name='DHW_carriertype_2', 
            attr_name='DHW_carriertype_2', 
            icon='💧', 
            label_de='Warmwasser System 2 Energieträger', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='carrier_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_2_is_electric = VariableMeta(
            var_name='DHW_2_is_electric', 
            attr_name='DHW_2_is_electric', 
            icon='💧', 
            label_de='Warmwasser System 2 ist elektrisch', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='is_electric', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_1_efficiency = VariableMeta(
            var_name='DHW_1_efficiency', 
            attr_name='DHW_1_efficiency', 
            icon='💧', 
            label_de='Warmwasser System 1 Wirkungsgrad', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_2_efficiency = VariableMeta(
            var_name='DHW_2_efficiency', 
            attr_name='DHW_2_efficiency', 
            icon='💧', 
            label_de='Warmwasser System 2 Wirkungsgrad', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='generation_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_conversion_1 = VariableMeta(
            var_name='DHW_conversion_1', 
            attr_name='DHW_conversion_1', 
            icon='💧', 
            label_de='Warmwasser System 1 Wirkungsgradkehrwert', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_conversion_2 = VariableMeta(
            var_name='DHW_conversion_2', 
            attr_name='DHW_conversion_2', 
            icon='💧', 
            label_de='Warmwasser System 2 Wirkungsgradkehrwert', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='generation_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_1_el_aux = VariableMeta(
            var_name='DHW_1_el_aux', 
            attr_name='DHW_1_el_aux', 
            icon='💧', 
            label_de='WW-System 1 Hilfsstromanteil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='DHW', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.DHW_2_el_aux = VariableMeta(
            var_name='DHW_2_el_aux', 
            attr_name='DHW_2_el_aux', 
            icon='💧', 
            label_de='WW-System 2 Hilfsstromanteil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='auxiliary_power_ratio', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.DHW_occupancy_residential = VariableMeta(
            var_name='DHW_occupancy_residential', 
            attr_name='DHW_occupancy_residential', 
            icon='💧', 
            label_de='Personenbelegung Wohnen', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.DHW_occupancy_office = VariableMeta(
            var_name='DHW_occupancy_office', 
            attr_name='DHW_occupancy_office', 
            icon='💧', 
            label_de='Personenbelegung Büro', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.DHW_occupancy_schoolsec = VariableMeta(
            var_name='DHW_occupancy_schoolsec', 
            attr_name='DHW_occupancy_schoolsec', 
            icon='💧', 
            label_de='Personenbelegung Bildung sekundär', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.DHW_occupancy_schoolprim = VariableMeta(
            var_name='DHW_occupancy_schoolprim', 
            attr_name='DHW_occupancy_schoolprim', 
            icon='💧', 
            label_de='Personenbelegung Bildung primär', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.DHW_occupancy_retailfood = VariableMeta(
            var_name='DHW_occupancy_retailfood', 
            attr_name='DHW_occupancy_retailfood', 
            icon='💧', 
            label_de='Personenbelegung Handel Lebensmittel', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.DHW_occupancy_retailother = VariableMeta(
            var_name='DHW_occupancy_retailother', 
            attr_name='DHW_occupancy_retailother', 
            icon='💧', 
            label_de='Personenbelegung Handel sonstiger', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.DHW_occupancy_other = VariableMeta(
            var_name='DHW_occupancy_other', 
            attr_name='DHW_occupancy_other', 
            icon='💧', 
            label_de='Personenbelegung Sonstige', 
            unit='m²NF/Pers', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='occupancy', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.DHW_concurrency_residential = VariableMeta(
            var_name='DHW_concurrency_residential', 
            attr_name='DHW_concurrency_residential', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor Wohnen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.DHW_concurrency_office = VariableMeta(
            var_name='DHW_concurrency_office', 
            attr_name='DHW_concurrency_office', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor Büro', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.DHW_concurrency_schoolsec = VariableMeta(
            var_name='DHW_concurrency_schoolsec', 
            attr_name='DHW_concurrency_schoolsec', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor Bildung sekundär', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.DHW_concurrency_schoolprim = VariableMeta(
            var_name='DHW_concurrency_schoolprim', 
            attr_name='DHW_concurrency_schoolprim', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor bildung primär', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.DHW_concurrency_retailfood = VariableMeta(
            var_name='DHW_concurrency_retailfood', 
            attr_name='DHW_concurrency_retailfood', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor Handel Lebensmittel', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.DHW_concurrency_retailother = VariableMeta(
            var_name='DHW_concurrency_retailother', 
            attr_name='DHW_concurrency_retailother', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor handel sonstiger', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.DHW_concurrency_other = VariableMeta(
            var_name='DHW_concurrency_other', 
            attr_name='DHW_concurrency_other', 
            icon='💧', 
            label_de='WW Gleichzeitigkeitsfaktor Sonstige', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='concurrency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='other'
        )
        self.DHW_storage_liter_pPerson = VariableMeta(
            var_name='DHW_storage_liter_pPerson', 
            attr_name='DHW_storage_liter_pPerson', 
            icon='💧', 
            label_de='Warmwasser Speicher pro Person', 
            unit='l/Pers/Tag', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='storage_capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_thermal_power_pPerson = VariableMeta(
            var_name='DHW_thermal_power_pPerson', 
            attr_name='DHW_thermal_power_pPerson', 
            icon='💧', 
            label_de='Warmwasser Ladeleistung Thermisch', 
            unit='W/Pers', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='DHW', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_thermal_power_Wpl = VariableMeta(
            var_name='DHW_thermal_power_Wpl', 
            attr_name='DHW_thermal_power_Wpl', 
            icon='💧', 
            label_de='Warmwasser Ladeleistung Thermisch pro Speicher', 
            unit='W/l', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='DHW', 
            measure='generation_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.DHW_storage_env_temp_default = VariableMeta(
            var_name='DHW_storage_env_temp_default', 
            attr_name='DHW_storage_env_temp_default', 
            icon='💧', 
            label_de='Warmwasser Speicher Umgebungstemperatur', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='DHW', 
            measure='ambient_temperature', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_is_used = VariableMeta(
            var_name='PV_is_used', 
            attr_name='PV_is_used', 
            icon='🌞', 
            label_de='PV Nutzung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='PV', 
            measure='is_used', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_profile_name = VariableMeta(
            var_name='PV_profile_name', 
            attr_name='PV_profile_name', 
            icon='🌞', 
            label_de='PV Profil Name', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='PV', 
            measure='name', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_id = VariableMeta(
            var_name='PV_id', 
            attr_name='PV_id', 
            icon='🌞', 
            label_de='PV Profil ID', 
            unit='int', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='PV', 
            measure='index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_scale = VariableMeta(
            var_name='PV_scale', 
            attr_name='PV_scale', 
            icon='🌞', 
            label_de='PV Skalierungsfaktor Profil', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='PV', 
            measure='pv_scale', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_efficiency = VariableMeta(
            var_name='PV_efficiency', 
            attr_name='PV_efficiency', 
            icon='🌞', 
            label_de='PV Wechselrichter Effizienz', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='PV', 
            measure='efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_m2_per_kWp = VariableMeta(
            var_name='PV_m2_per_kWp', 
            attr_name='PV_m2_per_kWp', 
            icon='🌞', 
            label_de='Spezifische PV Fläche', 
            unit='m²/kWp', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='PV', 
            measure='area', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_kWp = VariableMeta(
            var_name='PV_kWp', 
            attr_name='PV_kWp', 
            icon='🌞', 
            label_de='PV Installierte Leistung', 
            unit='kWp', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='PV', 
            measure='installed_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_module_area = VariableMeta(
            var_name='PV_module_area', 
            attr_name='PV_module_area', 
            icon='🌞', 
            label_de='PV-Modulfläche', 
            unit='m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='PV', 
            measure='area', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_PV_is_used = VariableMeta(
            var_name='FLEX_PV_is_used', 
            attr_name='FLEX_PV_is_used', 
            icon='🔋', 
            label_de='Flex PV Nutzung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='flexible_PV_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_is_used = VariableMeta(
            var_name='FLEX_is_used', 
            attr_name='FLEX_is_used', 
            icon='🔋', 
            label_de='Flex Signal Nutzung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_signal_name = VariableMeta(
            var_name='FLEX_signal_name', 
            attr_name='FLEX_signal_name', 
            icon='🔋', 
            label_de='Flex Signal Name', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='signal_name', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_signal_ID = VariableMeta(
            var_name='FLEX_signal_ID', 
            attr_name='FLEX_signal_ID', 
            icon='🔋', 
            label_de='Flex Signal ID', 
            unit='int', 
            comment='should be obsolete, together with signals in PV Import', 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='signal_index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_grid_maxpower_Wm2 = VariableMeta(
            var_name='FLEX_grid_maxpower_Wm2', 
            attr_name='FLEX_grid_maxpower_Wm2', 
            icon='🔋', 
            label_de='Flex Maximale Leistung', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Flexibility', 
            measure='max_grid_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_is_used_for_plugloads = VariableMeta(
            var_name='FLEX_is_used_for_plugloads', 
            attr_name='FLEX_is_used_for_plugloads', 
            icon='🔋', 
            label_de='Flex Netzbezug deckt Nutzerstrom', 
            unit='bool', 
            comment='muss jetzt nicht mehr automatisch Wahr sein', 
            source='IN', 
            ka=1, 
            domain='Flexibility', 
            measure='plugloads_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_is_used_for_HVAC_min = VariableMeta(
            var_name='FLEX_is_used_for_HVAC_min', 
            attr_name='FLEX_is_used_for_HVAC_min', 
            icon='🔋', 
            label_de='Flex Netzbezug deckt HVAC Minimum', 
            unit='bool', 
            comment='muss jetzt nicht mehr automatisch Wahr sein', 
            source='IN', 
            ka=1, 
            domain='Flexibility', 
            measure='HVAC_min_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_is_used_for_ev_min = VariableMeta(
            var_name='FLEX_is_used_for_ev_min', 
            attr_name='FLEX_is_used_for_ev_min', 
            icon='🔋', 
            label_de='Flex Netzbezug deckt EV Minimum', 
            unit='bool', 
            comment='muss jetzt nicht mehr automatisch Wahr sein', 
            source='IN', 
            ka=1, 
            domain='Flexibility', 
            measure='EV_min_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_heat_dT = VariableMeta(
            var_name='flex_heat_dT', 
            attr_name='flex_heat_dT', 
            icon='♨️', 
            label_de='Flexibles Heizen über Solltemperatur', 
            unit='K', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='max_temperature_increase', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Tsetheat_flex = VariableMeta(
            var_name='Tsetheat_flex', 
            attr_name='Tsetheat_flex', 
            icon='♨️', 
            label_de='Flexibles Heizen Maximale Raumtemperatur', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='maximum_setpoint_temperature', 
            spatial_scope=None, 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_choice_heat_system = VariableMeta(
            var_name='FLEX_choice_heat_system', 
            attr_name='FLEX_choice_heat_system', 
            icon='♨️', 
            label_de='Flexibles Heizsystem', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='heating_system_selection', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_heat1_use = VariableMeta(
            var_name='FLEX_heat1_use', 
            attr_name='FLEX_heat1_use', 
            icon='♨️', 
            label_de='Flexibles Heizen mit Heizsystem 1', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='is_flexible', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_1'
        )
        self.FLEX_heat3_use = VariableMeta(
            var_name='FLEX_heat3_use', 
            attr_name='FLEX_heat3_use', 
            icon='♨️', 
            label_de='Flexibles Heizen mit Heizsystem 3', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='is_flexible', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_3'
        )
        self.flex_cool_dT = VariableMeta(
            var_name='flex_cool_dT', 
            attr_name='flex_cool_dT', 
            icon='❄️', 
            label_de='Flexibles Kühlen unter Solltemperatur', 
            unit='K', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='max_temperature_decrease', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Tsetcool_flex = VariableMeta(
            var_name='Tsetcool_flex', 
            attr_name='Tsetcool_flex', 
            icon='❄️', 
            label_de='Flexibles Kühlen Minimale Raumtemperatur', 
            unit='°C', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='maximum_setpoint_temperature', 
            spatial_scope=None, 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_choice_cool_system = VariableMeta(
            var_name='FLEX_choice_cool_system', 
            attr_name='FLEX_choice_cool_system', 
            icon='❄️', 
            label_de='Flexibles Kühlsystem', 
            unit='text', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Flexibility', 
            measure='cooling_system_selection', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FLEX_cool1_use = VariableMeta(
            var_name='FLEX_cool1_use', 
            attr_name='FLEX_cool1_use', 
            icon='❄️', 
            label_de='Flexibles Kühlen mit Kühlsystem 1', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='is_flexible', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_1'
        )
        self.FLEX_cool3_use = VariableMeta(
            var_name='FLEX_cool3_use', 
            attr_name='FLEX_cool3_use', 
            icon='❄️', 
            label_de='Flexibles Kühlen mit Kühlsystem 3', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='is_flexible', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_3'
        )
        self.Batt_is_used = VariableMeta(
            var_name='Batt_is_used', 
            attr_name='Batt_is_used', 
            icon='🔋', 
            label_de='Batterie Nutzung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='is_used', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_cap_kWh = VariableMeta(
            var_name='Batt_cap_kWh', 
            attr_name='Batt_cap_kWh', 
            icon='🔋', 
            label_de='Batterie Kapazität', 
            unit='kWh', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_cap_Wh_per_NFA = VariableMeta(
            var_name='Batt_cap_Wh_per_NFA', 
            attr_name='Batt_cap_Wh_per_NFA', 
            icon='🔋', 
            label_de='Batterie Kapazität spezifisch', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Battery', 
            measure='capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_c_rate = VariableMeta(
            var_name='Batt_c_rate', 
            attr_name='Batt_c_rate', 
            icon='🔋', 
            label_de='Maximale Be/Entladeleistung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='c_rate', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_max_power_specific = VariableMeta(
            var_name='Batt_max_power_specific', 
            attr_name='Batt_max_power_specific', 
            icon='🔋', 
            label_de='Batterie Leistung spezifisch', 
            unit='W/m²', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Battery', 
            measure='power', 
            spatial_scope='NFA', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_eff_factor_charge = VariableMeta(
            var_name='Batt_eff_factor_charge', 
            attr_name='Batt_eff_factor_charge', 
            icon='🔋', 
            label_de='Wirkungsgrad Ladung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_eff_factor_discharge = VariableMeta(
            var_name='Batt_eff_factor_discharge', 
            attr_name='Batt_eff_factor_discharge', 
            icon='🔋', 
            label_de='Wirkungsgrad Entladung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_self_discharge_rate = VariableMeta(
            var_name='Batt_self_discharge_rate', 
            attr_name='Batt_self_discharge_rate', 
            icon='🔋', 
            label_de='Batterie Selbstentladung', 
            unit='1/week', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='storage_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_auto_discharge_factor = VariableMeta(
            var_name='Batt_auto_discharge_factor', 
            attr_name='Batt_auto_discharge_factor', 
            icon='🔋', 
            label_de='Batterie Selbstentladung pro Stunde', 
            unit='1/h', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Battery', 
            measure='storage_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_SOC_init = VariableMeta(
            var_name='Batt_SOC_init', 
            attr_name='Batt_SOC_init', 
            icon='🔋', 
            label_de='Batterie Initialer SOC', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Battery', 
            measure='SOC_init', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_is_used_for_plugloads = VariableMeta(
            var_name='Batt_is_used_for_plugloads', 
            attr_name='Batt_is_used_for_plugloads', 
            icon='🔋', 
            label_de='Batterie Nutzung für Nutzerstrom', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Battery', 
            measure='plugloads_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_is_used_for_HVACminimum = VariableMeta(
            var_name='Batt_is_used_for_HVACminimum', 
            attr_name='Batt_is_used_for_HVACminimum', 
            icon='🔋', 
            label_de='Batterie Nutzung für HKLS Minimum', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Battery', 
            measure='HVAC_min_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_is_used_for_EV = VariableMeta(
            var_name='Batt_is_used_for_EV', 
            attr_name='Batt_is_used_for_EV', 
            icon='🔋', 
            label_de='Batterie Nutzung für Ecars', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Battery', 
            measure='EV_min_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_is_gridcharged = VariableMeta(
            var_name='Batt_is_gridcharged', 
            attr_name='Batt_is_gridcharged', 
            icon='🔋', 
            label_de='Batterie wird flexibel  durch Netz geladen?', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Battery', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_dhw_use = VariableMeta(
            var_name='flex_dhw_use', 
            attr_name='flex_dhw_use', 
            icon='🔋', 
            label_de='Flexible WW-Speicherbeladung', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Flexibility', 
            measure='dhw_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_Signals_selected_column = VariableMeta(
            var_name='flex_Signals_selected_column', 
            attr_name='flex_Signals_selected_column', 
            icon='🔋', 
            label_de='Flex Signal Table', 
            unit='int', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Flexibility', 
            measure='signal_index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_is_not_used_during_signals = VariableMeta(
            var_name='Batt_is_not_used_during_signals', 
            attr_name='Batt_is_not_used_during_signals', 
            icon='🔋', 
            label_de='Batterie wird während Netzsignal nicht entladen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Flexibility', 
            measure='is_not_discharged_during_signals', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mobility_is_included = VariableMeta(
            var_name='mobility_is_included', 
            attr_name='mobility_is_included', 
            icon='🚗', 
            label_de='MIV simulieren', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='is_used', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mobility_region = VariableMeta(
            var_name='mobility_region', 
            attr_name='mobility_region', 
            icon='🚗', 
            label_de='Mobilitätsregion', 
            unit='str', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='selection', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mobshare_residential = VariableMeta(
            var_name='mobshare_residential', 
            attr_name='mobshare_residential', 
            icon='🚗', 
            label_de='Zielverkehrsanteil Wohnen', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='target_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='residential'
        )
        self.mobshare_office = VariableMeta(
            var_name='mobshare_office', 
            attr_name='mobshare_office', 
            icon='🚗', 
            label_de='Zielverkehrsanteil Büro', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='target_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='work'
        )
        self.mobshare_school = VariableMeta(
            var_name='mobshare_school', 
            attr_name='mobshare_school', 
            icon='🚗', 
            label_de='Zielverkehrsanteil Ausbildung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='target_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='education'
        )
        self.mobshare_retail = VariableMeta(
            var_name='mobshare_retail', 
            attr_name='mobshare_retail', 
            icon='🚗', 
            label_de='Zielverkehrsanteil Handel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='target_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='retail'
        )
        self.pkm_pedestrian = VariableMeta(
            var_name='pkm_pedestrian', 
            attr_name='pkm_pedestrian', 
            icon='🚗', 
            label_de='Pkm Zu Fuß', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_bike = VariableMeta(
            var_name='pkm_bike', 
            attr_name='pkm_bike', 
            icon='🚗', 
            label_de='Pkm Fahrrad', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_mofa = VariableMeta(
            var_name='pkm_mofa', 
            attr_name='pkm_mofa', 
            icon='🚗', 
            label_de='Pkm Moped', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_car_driver = VariableMeta(
            var_name='pkm_car_driver', 
            attr_name='pkm_car_driver', 
            icon='🚗', 
            label_de='Pkm PKW-LenkerIn', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_car_passenger = VariableMeta(
            var_name='pkm_car_passenger', 
            attr_name='pkm_car_passenger', 
            icon='🚗', 
            label_de='Pkm PKW-MitfahrerIn', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_bus = VariableMeta(
            var_name='pkm_bus', 
            attr_name='pkm_bus', 
            icon='🚗', 
            label_de='Pkm Stadt/ Regionalbus', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_tram_metro = VariableMeta(
            var_name='pkm_tram_metro', 
            attr_name='pkm_tram_metro', 
            icon='🚗', 
            label_de='Pkm Straßenbahn/U-Bahn', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_train = VariableMeta(
            var_name='pkm_train', 
            attr_name='pkm_train', 
            icon='🚗', 
            label_de='Pkm Eisenbahn', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.pkm_distancebus = VariableMeta(
            var_name='pkm_distancebus', 
            attr_name='pkm_distancebus', 
            icon='🚗', 
            label_de='Pkm Reisebus', 
            unit='km', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.mobility_vehicle_count = VariableMeta(
            var_name='mobility_vehicle_count', 
            attr_name='mobility_vehicle_count', 
            icon='🚗', 
            label_de='Fahrzeuge', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='vehicles', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_share = VariableMeta(
            var_name='EV_share', 
            attr_name='EV_share', 
            icon='🚗', 
            label_de='Anteil Ecars', 
            unit='ratio', 
            comment='Am Mobilitätsbedarf', 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='ev_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_demand_kWhpkm = VariableMeta(
            var_name='EV_demand_kWhpkm', 
            attr_name='EV_demand_kWhpkm', 
            icon='🚗', 
            label_de='Ecar Energieverbrauch', 
            unit='kWh/km', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_battsize_kWh = VariableMeta(
            var_name='EV_battsize_kWh', 
            attr_name='EV_battsize_kWh', 
            icon='🚗', 
            label_de='Ecar Speicher pro Fahrzeug', 
            unit='kWh/EV', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_storage_total_kWh = VariableMeta(
            var_name='EV_storage_total_kWh', 
            attr_name='EV_storage_total_kWh', 
            icon='🚗', 
            label_de='Ecar Speicher im Quartier', 
            unit='kWh', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='capacity', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_self_discharge_per_week = VariableMeta(
            var_name='EV_self_discharge_per_week', 
            attr_name='EV_self_discharge_per_week', 
            icon='🚗', 
            label_de='Ecar Selbstentladung wöchentlich', 
            unit='1/week', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='storage_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_selfdischarge_per_h = VariableMeta(
            var_name='EV_selfdischarge_per_h', 
            attr_name='EV_selfdischarge_per_h', 
            icon='🚗', 
            label_de='Ecar Selbstentladung stündlich', 
            unit='1/h', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='storage_losses', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_soc_minimum = VariableMeta(
            var_name='EV_soc_minimum', 
            attr_name='EV_soc_minimum', 
            icon='🚗', 
            label_de='Ecar Mindest-Speicherstand', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='residential'
        )
        self.EV_charging_efficiency = VariableMeta(
            var_name='EV_charging_efficiency', 
            attr_name='EV_charging_efficiency', 
            icon='🚗', 
            label_de='Ecar Batterie-Effizienz Beladung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='charging_efficiency', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_charging_losses_surcharge_factor = VariableMeta(
            var_name='EV_charging_losses_surcharge_factor', 
            attr_name='EV_charging_losses_surcharge_factor', 
            icon='🚗', 
            label_de='Ecar Batterie-Effizienz Beladung Kehrwert', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='charging_efficiency_inverse', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_max_charging_power_ratio = VariableMeta(
            var_name='EV_max_charging_power_ratio', 
            attr_name='EV_max_charging_power_ratio', 
            icon='🚗', 
            label_de='Ecar Batterie Maximale Beladungsleistung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='c_rate', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_soc_min_work = VariableMeta(
            var_name='EV_soc_min_work', 
            attr_name='EV_soc_min_work', 
            icon='🚗', 
            label_de='Ecar Mindestspeicherstand Arbeit', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='work'
        )
        self.EV_soc_min_retail = VariableMeta(
            var_name='EV_soc_min_retail', 
            attr_name='EV_soc_min_retail', 
            icon='🚗', 
            label_de='Ecar Mindestspeicherstand Handel', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='retail'
        )
        self.moped_factor = VariableMeta(
            var_name='moped_factor', 
            attr_name='moped_factor', 
            icon='🚗', 
            label_de='Moped im Verhältnis zu Auto', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='moped_to_car', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_share_constant_charging = VariableMeta(
            var_name='EV_share_constant_charging', 
            attr_name='EV_share_constant_charging', 
            icon='🚗', 
            label_de='Anteil Ecars, die konstant vor Ort laden', 
            unit='ratio', 
            comment='Rest konstantes Laden', 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='nonflexible_charging_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mob_pkm_factor = VariableMeta(
            var_name='mob_pkm_factor', 
            attr_name='mob_pkm_factor', 
            icon='🚗', 
            label_de='Reduktionsfaktor JPkm MIV', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='mileage_reduction', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_experimental_calculation = VariableMeta(
            var_name='EV_experimental_calculation', 
            attr_name='EV_experimental_calculation', 
            icon='🚗', 
            label_de='New Calculation Method', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_mileage_residential = VariableMeta(
            var_name='EV_mileage_residential', 
            attr_name='EV_mileage_residential', 
            icon='🚗', 
            label_de='Ecar Pkm Real Wohnen (Insgesamt)', 
            unit='Pkm/a', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='residential'
        )
        self.EV_mileage_work = VariableMeta(
            var_name='EV_mileage_work', 
            attr_name='EV_mileage_work', 
            icon='🚗', 
            label_de='Ecar Pkm Real Arbeiten (Insgesamt)', 
            unit='Pkm/a', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='work'
        )
        self.EV_mileage_retail = VariableMeta(
            var_name='EV_mileage_retail', 
            attr_name='EV_mileage_retail', 
            icon='🚗', 
            label_de='Ecar Pkm Real Einkaufen (Insgesamt)', 
            unit='Pkm/a', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='mileage', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='retail'
        )
        self.EV_soc_min_ext = VariableMeta(
            var_name='EV_soc_min_ext', 
            attr_name='EV_soc_min_ext', 
            icon='🚗', 
            label_de='Ecar Mindest-Speicherstand Extern', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_soc_min_discharge = VariableMeta(
            var_name='EV_soc_min_discharge', 
            attr_name='EV_soc_min_discharge', 
            icon='🚗', 
            label_de='Ecar Mindest-Speicherstand Entladung', 
            unit='ratio', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='minimum_setpoint', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fossile_demand_kWhpkm = VariableMeta(
            var_name='fossile_demand_kWhpkm', 
            attr_name='fossile_demand_kWhpkm', 
            icon='🚗', 
            label_de='Fossiler Energieverbrauch', 
            unit='kWh/km', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='Mobility', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_count_residential = VariableMeta(
            var_name='EV_count_residential', 
            attr_name='EV_count_residential', 
            icon='🚗', 
            label_de='Ecar Anzahl Wohnen', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='ev_count', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='residential'
        )
        self.EV_count_work = VariableMeta(
            var_name='EV_count_work', 
            attr_name='EV_count_work', 
            icon='🚗', 
            label_de='Ecar Anzahl Arbeit', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='ev_count', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='work'
        )
        self.EV_count_retail = VariableMeta(
            var_name='EV_count_retail', 
            attr_name='EV_count_retail', 
            icon='🚗', 
            label_de='Ecar Anzahl Einkaufen', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='Mobility', 
            measure='ev_count', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='mobility', 
            entity_key='retail'
        )
        self.ev_bidirectional_use = VariableMeta(
            var_name='ev_bidirectional_use', 
            attr_name='ev_bidirectional_use', 
            icon='🚗', 
            label_de='Bidirektionales Laden', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Mobility', 
            measure='is_bidirectional', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_walls_name = VariableMeta(
            var_name='GWP_walls_name', 
            attr_name='GWP_walls_name', 
            icon='☁', 
            label_de='Bauweise Außenwand', 
            unit=None, 
            comment='COMP_name_wall', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_windows_name = VariableMeta(
            var_name='GWP_windows_name', 
            attr_name='GWP_windows_name', 
            icon='☁', 
            label_de='Bauweise Fenster', 
            unit=None, 
            comment='COMP_name_windows', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_roof_name = VariableMeta(
            var_name='GWP_roof_name', 
            attr_name='GWP_roof_name', 
            icon='☁', 
            label_de='Bauweise Dach', 
            unit=None, 
            comment='COMP_name_roof', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_ground_name = VariableMeta(
            var_name='GWP_ground_name', 
            attr_name='GWP_ground_name', 
            icon='☁', 
            label_de='Bauweise Erdb. Fußboden beheizt', 
            unit=None, 
            comment='COMP_name_floor', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GPW_ceilings_name = VariableMeta(
            var_name='GPW_ceilings_name', 
            attr_name='GPW_ceilings_name', 
            icon='☁', 
            label_de='Bauweise Geschossdecke', 
            unit=None, 
            comment='COMP_name_ceiling', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_terrace = VariableMeta(
            var_name='COMP_name_terrace', 
            attr_name='COMP_name_terrace', 
            icon=None, 
            label_de='Bauweise Terasse', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_basement_ceiling = VariableMeta(
            var_name='COMP_name_basement_ceiling', 
            attr_name='COMP_name_basement_ceiling', 
            icon=None, 
            label_de='Bauweise Kellerdecke', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_fundament = VariableMeta(
            var_name='COMP_name_fundament', 
            attr_name='COMP_name_fundament', 
            icon=None, 
            label_de='Bauweise Bodenplatte', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_ceil_to_air = VariableMeta(
            var_name='COMP_name_ceil_to_air', 
            attr_name='COMP_name_ceil_to_air', 
            icon=None, 
            label_de='Bauweise Außendecke gg. Außenluft', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_wall_earth_contacted = VariableMeta(
            var_name='COMP_name_wall_earth_contacted', 
            attr_name='COMP_name_wall_earth_contacted', 
            icon=None, 
            label_de='Bauweise Erdb. Wand beheizt', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_internal_wall_load = VariableMeta(
            var_name='COMP_name_internal_wall_load', 
            attr_name='COMP_name_internal_wall_load', 
            icon=None, 
            label_de='Bauweise Innenwand tragend', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_internal_wall_nonload = VariableMeta(
            var_name='COMP_name_internal_wall_nonload', 
            attr_name='COMP_name_internal_wall_nonload', 
            icon=None, 
            label_de='Bauweise Innenwand nicht tragend', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_ceiling_topfloor = VariableMeta(
            var_name='COMP_name_ceiling_topfloor', 
            attr_name='COMP_name_ceiling_topfloor', 
            icon=None, 
            label_de='Bauweise Oberste Geschoßdecke', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_wall_ec_unheated = VariableMeta(
            var_name='COMP_name_wall_ec_unheated', 
            attr_name='COMP_name_wall_ec_unheated', 
            icon=None, 
            label_de='Bauweise Erdb. Wand Keller', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_basement_floor_unheated = VariableMeta(
            var_name='COMP_name_basement_floor_unheated', 
            attr_name='COMP_name_basement_floor_unheated', 
            icon=None, 
            label_de='Bauweise  Erdb. Fußboden unbeheizt', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_columns = VariableMeta(
            var_name='COMP_name_columns', 
            attr_name='COMP_name_columns', 
            icon=None, 
            label_de='Bauweise Stützen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_internal_wall_unheated = VariableMeta(
            var_name='COMP_name_internal_wall_unheated', 
            attr_name='COMP_name_internal_wall_unheated', 
            icon=None, 
            label_de='Bauweise Innenwand unbeheizt', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_unheated_horizontal = VariableMeta(
            var_name='COMP_name_unheated_horizontal', 
            attr_name='COMP_name_unheated_horizontal', 
            icon=None, 
            label_de='Bauweise Zwischendecke unbeheizt / Keller / TG', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_balconies = VariableMeta(
            var_name='COMP_name_balconies', 
            attr_name='COMP_name_balconies', 
            icon=None, 
            label_de='Bauweise Balkone', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_windowframe = VariableMeta(
            var_name='COMP_name_windowframe', 
            attr_name='COMP_name_windowframe', 
            icon=None, 
            label_de='Bauweise Fensterrahmen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_windowglazing = VariableMeta(
            var_name='COMP_name_windowglazing', 
            attr_name='COMP_name_windowglazing', 
            icon=None, 
            label_de='Bauweise Fensterglas', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_name_other = VariableMeta(
            var_name='COMP_name_other', 
            attr_name='COMP_name_other', 
            icon=None, 
            label_de='Bauweise Sonstige', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_general_name = VariableMeta(
            var_name='GWP_general_name', 
            attr_name='GWP_general_name', 
            icon='☁', 
            label_de='Typ Bauliche Maßnahmen Allgemein', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_other_name = VariableMeta(
            var_name='GWP_other_name', 
            attr_name='GWP_other_name', 
            icon='☁', 
            label_de='Typ Andere bauliche Maßnahmen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ref_area_walls = VariableMeta(
            var_name='GWP_ref_area_walls', 
            attr_name='GWP_ref_area_walls', 
            icon='☁', 
            label_de='FU Außenwand', 
            unit='m² FU', 
            comment='COMP_area_wall', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_ref_area_windows = VariableMeta(
            var_name='GWP_ref_area_windows', 
            attr_name='GWP_ref_area_windows', 
            icon='☁', 
            label_de='FU Fenster', 
            unit='m² FU', 
            comment='COMP_area_windows', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_ref_area_roof = VariableMeta(
            var_name='GWP_ref_area_roof', 
            attr_name='GWP_ref_area_roof', 
            icon='☁', 
            label_de='FU Dach', 
            unit='m² FU', 
            comment='COMP_area_roof', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_ref_area_fundament = VariableMeta(
            var_name='GWP_ref_area_fundament', 
            attr_name='GWP_ref_area_fundament', 
            icon='☁', 
            label_de='FU Erdb. Fußboden beheizt', 
            unit='m² FU', 
            comment='COMP_area_floor', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_ref_area_ceilings = VariableMeta(
            var_name='GWP_ref_area_ceilings', 
            attr_name='GWP_ref_area_ceilings', 
            icon='☁', 
            label_de='FU Geschossdecke', 
            unit='m² FU', 
            comment='COMP_area_ceilings', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_terrace = VariableMeta(
            var_name='COMP_area_terrace', 
            attr_name='COMP_area_terrace', 
            icon=None, 
            label_de='FU Terasse', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_basement_ceiling = VariableMeta(
            var_name='COMP_area_basement_ceiling', 
            attr_name='COMP_area_basement_ceiling', 
            icon=None, 
            label_de='FU Kellerdecke', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_fundament = VariableMeta(
            var_name='COMP_area_fundament', 
            attr_name='COMP_area_fundament', 
            icon=None, 
            label_de='FU Bodenplatte', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_ceil_to_air = VariableMeta(
            var_name='COMP_area_ceil_to_air', 
            attr_name='COMP_area_ceil_to_air', 
            icon=None, 
            label_de='FU Außendecke gg. Außenluft', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_wall_earth_contacted = VariableMeta(
            var_name='COMP_area_wall_earth_contacted', 
            attr_name='COMP_area_wall_earth_contacted', 
            icon=None, 
            label_de='FU Erdb. Wand beheizt', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_internal_wall_load = VariableMeta(
            var_name='COMP_area_internal_wall_load', 
            attr_name='COMP_area_internal_wall_load', 
            icon=None, 
            label_de='FU Innenwand tragend', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_internal_wall_nonload = VariableMeta(
            var_name='COMP_area_internal_wall_nonload', 
            attr_name='COMP_area_internal_wall_nonload', 
            icon=None, 
            label_de='FU Innenwand nicht tragend', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_ceiling_topfloor = VariableMeta(
            var_name='COMP_area_ceiling_topfloor', 
            attr_name='COMP_area_ceiling_topfloor', 
            icon=None, 
            label_de='FU Oberste Geschoßdecke', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_wall_ec_unheated = VariableMeta(
            var_name='COMP_area_wall_ec_unheated', 
            attr_name='COMP_area_wall_ec_unheated', 
            icon=None, 
            label_de='FU Erdb. Wand Keller', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_basement_floor_unheated = VariableMeta(
            var_name='COMP_area_basement_floor_unheated', 
            attr_name='COMP_area_basement_floor_unheated', 
            icon=None, 
            label_de='FU Erdb. Fußboden Keller', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_columns = VariableMeta(
            var_name='COMP_area_columns', 
            attr_name='COMP_area_columns', 
            icon=None, 
            label_de='FU Stützen', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_internal_wall_unheated = VariableMeta(
            var_name='COMP_area_internal_wall_unheated', 
            attr_name='COMP_area_internal_wall_unheated', 
            icon=None, 
            label_de='FU Innenwand unbeheizt', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_unheated_horizontal = VariableMeta(
            var_name='COMP_area_unheated_horizontal', 
            attr_name='COMP_area_unheated_horizontal', 
            icon=None, 
            label_de='FU Zwischendecke unbeheizt / Keller / TG', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_balconies = VariableMeta(
            var_name='COMP_area_balconies', 
            attr_name='COMP_area_balconies', 
            icon=None, 
            label_de='FU Balkone', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_windowframe = VariableMeta(
            var_name='COMP_area_windowframe', 
            attr_name='COMP_area_windowframe', 
            icon=None, 
            label_de='FU Fensterrahmen', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.COMP_area_windowglazing = VariableMeta(
            var_name='COMP_area_windowglazing', 
            attr_name='COMP_area_windowglazing', 
            icon=None, 
            label_de='FU Fensterglas', 
            unit='m² FU', 
            comment='functional unit', 
            source='IN', 
            ka=2, 
            domain='Construction', 
            measure='component_fu', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='component', 
            entity_key=None
        )
        self.GWP_refratio_walls = VariableMeta(
            var_name='GWP_refratio_walls', 
            attr_name='GWP_refratio_walls', 
            icon='☁', 
            label_de='Bezug pro BGF (Außenwand)', 
            unit='m²AW/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_refratio_windows = VariableMeta(
            var_name='GWP_refratio_windows', 
            attr_name='GWP_refratio_windows', 
            icon='☁', 
            label_de='Bezug pro BGF (Fenster)', 
            unit='m²Fe/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_refratio_roof = VariableMeta(
            var_name='GWP_refratio_roof', 
            attr_name='GWP_refratio_roof', 
            icon='☁', 
            label_de='Bezug pro BGF (Dach)', 
            unit='m²Dach/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_refratio_fundament = VariableMeta(
            var_name='GWP_refratio_fundament', 
            attr_name='GWP_refratio_fundament', 
            icon='☁', 
            label_de='Bezug pro BGF (Fundament)', 
            unit='m²KB/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_refratio_ceilings = VariableMeta(
            var_name='GWP_refratio_ceilings', 
            attr_name='GWP_refratio_ceilings', 
            icon='☁', 
            label_de='Bezug pro BGF (Zwischengeschoßdecken)', 
            unit='m²Zwd/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_pv_name = VariableMeta(
            var_name='GWP_pv_name', 
            attr_name='GWP_pv_name', 
            icon='☁', 
            label_de='Typ PV-Anlage', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_refratio_pv = VariableMeta(
            var_name='GWP_refratio_pv', 
            attr_name='GWP_refratio_pv', 
            icon='☁', 
            label_de='Bezug pro BGF (PV)', 
            unit='m²PV/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_boreholes_name = VariableMeta(
            var_name='GWP_boreholes_name', 
            attr_name='GWP_boreholes_name', 
            icon='☁', 
            label_de='Typ Erdwärmesonden', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.borehole_count = VariableMeta(
            var_name='borehole_count', 
            attr_name='borehole_count', 
            icon='☁', 
            label_de='Anzahl Erdsonden', 
            unit='Stk Erdsonden', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ventilation_name = VariableMeta(
            var_name='GWP_ventilation_name', 
            attr_name='GWP_ventilation_name', 
            icon='☁', 
            label_de='Typ Komfortlüftung', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_solarthermal_name = VariableMeta(
            var_name='GWP_solarthermal_name', 
            attr_name='GWP_solarthermal_name', 
            icon='☁', 
            label_de='Typ Solarthermie', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_battery_name = VariableMeta(
            var_name='GWP_battery_name', 
            attr_name='GWP_battery_name', 
            icon='☁', 
            label_de='Typ E-Batterie', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_storage_name = VariableMeta(
            var_name='GWP_storage_name', 
            attr_name='GWP_storage_name', 
            icon='☁', 
            label_de='Typ Pufferspeicher', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='lca', 
            measure='component_type', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_tga_general_name = VariableMeta(
            var_name='GWP_tga_general_name', 
            attr_name='GWP_tga_general_name', 
            icon='☁', 
            label_de='Typ  Allgemein', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_tga_other_name = VariableMeta(
            var_name='GWP_tga_other_name', 
            attr_name='GWP_tga_other_name', 
            icon='☁', 
            label_de='Typ  Andere bauliche Maßnahmen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_refratio_boreholes = VariableMeta(
            var_name='GWP_refratio_boreholes', 
            attr_name='GWP_refratio_boreholes', 
            icon='☁', 
            label_de='Bezug pro BGF (Erdsonden)', 
            unit='StkErdsonden/m²BGF', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_direct_fossile = VariableMeta(
            var_name='GWP_direct_fossile', 
            attr_name='GWP_direct_fossile', 
            icon='☁', 
            label_de='Direkteingabe GWP Fossil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_direct_biogenic = VariableMeta(
            var_name='GWP_direct_biogenic', 
            attr_name='GWP_direct_biogenic', 
            icon='☁', 
            label_de='Direkteingabe GWP Biogen', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_direct_biogenic_share = VariableMeta(
            var_name='GWP_direct_biogenic_share', 
            attr_name='GWP_direct_biogenic_share', 
            icon='☁', 
            label_de='Direkteingabe Biogener Anteil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_direct_life = VariableMeta(
            var_name='GWP_direct_life', 
            attr_name='GWP_direct_life', 
            icon='☁', 
            label_de='Direkteingabe Lebensdauer', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_miv_count_ev = VariableMeta(
            var_name='GWP_miv_count_ev', 
            attr_name='GWP_miv_count_ev', 
            icon='☁', 
            label_de='GWP Herstellung E-Cars', 
            unit='Anzahl Fahrzeuge', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='vehicle_count', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_miv_count_fossile = VariableMeta(
            var_name='GWP_miv_count_fossile', 
            attr_name='GWP_miv_count_fossile', 
            icon='☁', 
            label_de='GWP Herstellung Verbrenner', 
            unit='Anzahl Fahrzeuge', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='vehicle_count', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_mobility_construction_fossil = VariableMeta(
            var_name='GWP_mobility_construction_fossil', 
            attr_name='GWP_mobility_construction_fossil', 
            icon='☁', 
            label_de='GWP Verbrenner', 
            unit='t CO2/Fahrzeug', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_mobility_construction_ev = VariableMeta(
            var_name='GWP_mobility_construction_ev', 
            attr_name='GWP_mobility_construction_ev', 
            icon='☁', 
            label_de='GWP E-Car', 
            unit='t CO2/Fahrzeug', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GHG_LCA_timeframe_years = VariableMeta(
            var_name='GHG_LCA_timeframe_years', 
            attr_name='GHG_LCA_timeframe_years', 
            icon='☁', 
            label_de='Betrachtungszeitraum Ökobilanz', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_mobility_moped_gpPKm = VariableMeta(
            var_name='GWP_mobility_moped_gpPKm', 
            attr_name='GWP_mobility_moped_gpPKm', 
            icon='☁', 
            label_de='GWP Mobilität Moped', 
            unit='GWP 100S (gCO2equiv/Pkm)', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_mobility_car_gpPKm = VariableMeta(
            var_name='GWP_mobility_car_gpPKm', 
            attr_name='GWP_mobility_car_gpPKm', 
            icon='☁', 
            label_de='GWP Mobilität PKW', 
            unit='GWP 100S (gCO2equiv/Pkm)', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.year_rcp0 = VariableMeta(
            var_name='year_rcp0', 
            attr_name='year_rcp0', 
            icon='☁', 
            label_de='Bezugsjahr Ausgangssituation', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_year', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.year_rcp1 = VariableMeta(
            var_name='year_rcp1', 
            attr_name='year_rcp1', 
            icon='☁', 
            label_de='Bezugsjahr Stütztstelle 1', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_year', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.year_rcp2 = VariableMeta(
            var_name='year_rcp2', 
            attr_name='year_rcp2', 
            icon='☁', 
            label_de='Bezugsjahr Stütztstelle 2', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_year', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.year_rcp3 = VariableMeta(
            var_name='year_rcp3', 
            attr_name='year_rcp3', 
            icon='☁', 
            label_de='Bezugsjahr Stütztstelle 3', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_year', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.grid_rcp1 = VariableMeta(
            var_name='grid_rcp1', 
            attr_name='grid_rcp1', 
            icon='☁', 
            label_de='Absenkfaktor 1 Netzstrom', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='grid'
        )
        self.grid_rcp2 = VariableMeta(
            var_name='grid_rcp2', 
            attr_name='grid_rcp2', 
            icon='☁', 
            label_de='Absenkfaktor 2 Netzstrom', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='grid'
        )
        self.grid_rcp3 = VariableMeta(
            var_name='grid_rcp3', 
            attr_name='grid_rcp3', 
            icon='☁', 
            label_de='Absenkfaktor 3 Netzstrom', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='grid'
        )
        self.rcp1_renewable = VariableMeta(
            var_name='rcp1_renewable', 
            attr_name='rcp1_renewable', 
            icon='☁', 
            label_de='Absenkfaktor 1 Erneuerbare', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='renewables'
        )
        self.rcp2_renewable = VariableMeta(
            var_name='rcp2_renewable', 
            attr_name='rcp2_renewable', 
            icon='☁', 
            label_de='Absenkfaktor 2 Erneuerbare', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='renewables'
        )
        self.rcp3_renewable = VariableMeta(
            var_name='rcp3_renewable', 
            attr_name='rcp3_renewable', 
            icon='☁', 
            label_de='Absenkfaktor 3 Erneuerbare', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='renewables'
        )
        self.rcp1_dh = VariableMeta(
            var_name='rcp1_dh', 
            attr_name='rcp1_dh', 
            icon='☁', 
            label_de='Absenkfaktor 1 Fernwärme', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='district_heating'
        )
        self.rcp2_dh = VariableMeta(
            var_name='rcp2_dh', 
            attr_name='rcp2_dh', 
            icon='☁', 
            label_de='Absenkfaktor 2 Fernwärme', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='district_heating'
        )
        self.rcp3_dh = VariableMeta(
            var_name='rcp3_dh', 
            attr_name='rcp3_dh', 
            icon='☁', 
            label_de='Absenkfaktor 3 Fernwärme', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='district_heating'
        )
        self.rcp1_fossil = VariableMeta(
            var_name='rcp1_fossil', 
            attr_name='rcp1_fossil', 
            icon='☁', 
            label_de='Absenkfaktor 1 Andere Fossile', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='fossile'
        )
        self.rcp2_fossil = VariableMeta(
            var_name='rcp2_fossil', 
            attr_name='rcp2_fossil', 
            icon='☁', 
            label_de='Absenkfaktor 2 Andere Fossile', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='fossile'
        )
        self.rcp3_fossil = VariableMeta(
            var_name='rcp3_fossil', 
            attr_name='rcp3_fossil', 
            icon='☁', 
            label_de='Absenkfaktor 3 Andere Fossile', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='lca', 
            measure='pathway_reduction_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='fossile'
        )
        self.GWP_rcpi_grid = VariableMeta(
            var_name='GWP_rcpi_grid', 
            attr_name='GWP_rcpi_grid', 
            icon='☁', 
            label_de='Absenkpfad-Integral Netzstrom', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='grid'
        )
        self.GWP_rcpi_grid_substition = VariableMeta(
            var_name='GWP_rcpi_grid_substition', 
            attr_name='GWP_rcpi_grid_substition', 
            icon='☁', 
            label_de='Absenkpfad-Integral Substi', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='renewables'
        )
        self.GWP_rcpi_district_heating = VariableMeta(
            var_name='GWP_rcpi_district_heating', 
            attr_name='GWP_rcpi_district_heating', 
            icon='☁', 
            label_de='Absenkpfad-Integral Fernwärme', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='district_heating'
        )
        self.GWP_rcpi_fossil = VariableMeta(
            var_name='GWP_rcpi_fossil', 
            attr_name='GWP_rcpi_fossil', 
            icon='☁', 
            label_de='Absenkpfad-Integral Fossil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='fossile'
        )
        self.GWP_rcpi_natural_gas = VariableMeta(
            var_name='GWP_rcpi_natural_gas', 
            attr_name='GWP_rcpi_natural_gas', 
            icon='☁', 
            label_de='Absenkpfad-Integral Gas', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='natural_gas'
        )
        self.GWP_rcpi_biomass = VariableMeta(
            var_name='GWP_rcpi_biomass', 
            attr_name='GWP_rcpi_biomass', 
            icon='☁', 
            label_de='Absenkpfad-Integral Biomasse', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='biomass'
        )
        self.GWP_rcpi_mob_fossile = VariableMeta(
            var_name='GWP_rcpi_mob_fossile', 
            attr_name='GWP_rcpi_mob_fossile', 
            icon='☁', 
            label_de='Absenkpfad-Integral MIV Fossil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='fossile'
        )
        self.GWP_rcpi_renewable = VariableMeta(
            var_name='GWP_rcpi_renewable', 
            attr_name='GWP_rcpi_renewable', 
            icon='☁', 
            label_de='Absenkpfad-Integral Erneuerbar', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='lca', 
            measure='pathway_integral', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='energy_carrier', 
            entity_key='renewables'
        )
        self.fPE_grid_profile = VariableMeta(
            var_name='fPE_grid_profile', 
            attr_name='fPE_grid_profile', 
            icon='⚖', 
            label_de='Strom Konversionsprofil PE', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.district_heating_conversion_profile = VariableMeta(
            var_name='district_heating_conversion_profile', 
            attr_name='district_heating_conversion_profile', 
            icon='⚖', 
            label_de='Fernwärme Konversionsprofil', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='assessment', 
            measure='district_heating_index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fGHG_grid_profile = VariableMeta(
            var_name='fGHG_grid_profile', 
            attr_name='fGHG_grid_profile', 
            icon='⚖', 
            label_de='Strom Konversionsprofil THG', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='assessment', 
            measure='grid_name', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fPE_grid_column = VariableMeta(
            var_name='fPE_grid_column', 
            attr_name='fPE_grid_column', 
            icon='⚖', 
            label_de='Strom Konversionsprofil ID PE', 
            unit='int', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='conversion_factor_index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fGHG_grid_column = VariableMeta(
            var_name='fGHG_grid_column', 
            attr_name='fGHG_grid_column', 
            icon='⚖', 
            label_de='Strom Konversionsprofil ID THG', 
            unit='int', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='GHG', 
            measure='conversion_factor_index', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.heat_th2_is_dh = VariableMeta(
            var_name='heat_th2_is_dh', 
            attr_name='heat_th2_is_dh', 
            icon='⚖', 
            label_de='PE Heizen 2 ist Fernwärme', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_district_heating', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.heat_th4_is_dh = VariableMeta(
            var_name='heat_th4_is_dh', 
            attr_name='heat_th4_is_dh', 
            icon='⚖', 
            label_de='PE Heizen 4 ist Fernwärme', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_district_heating', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.cool_th2_is_dh = VariableMeta(
            var_name='cool_th2_is_dh', 
            attr_name='cool_th2_is_dh', 
            icon='⚖', 
            label_de='PE Kühlen 2 ist Fernwärme', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_district_heating', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.dhw1_is_dh = VariableMeta(
            var_name='dhw1_is_dh', 
            attr_name='dhw1_is_dh', 
            icon='⚖', 
            label_de='PE WWWB 1 ist Fernwärme', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_district_heating', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.dhw2_is_dh = VariableMeta(
            var_name='dhw2_is_dh', 
            attr_name='dhw2_is_dh', 
            icon='⚖', 
            label_de='PE WWWB 2 ist Fernwärme', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_district_heating', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.heat_th2_is_ng = VariableMeta(
            var_name='heat_th2_is_ng', 
            attr_name='heat_th2_is_ng', 
            icon='⚖', 
            label_de='PE Heizen 2 ist Erdgas', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_natural_gas', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.heat_th4_is_ng = VariableMeta(
            var_name='heat_th4_is_ng', 
            attr_name='heat_th4_is_ng', 
            icon='⚖', 
            label_de='PE Heizen 4 ist Erdgas', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_natural_gas', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.cool_th2_is_ng = VariableMeta(
            var_name='cool_th2_is_ng', 
            attr_name='cool_th2_is_ng', 
            icon='⚖', 
            label_de='PE Kühlen 2 ist Erdgas', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_natural_gas', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.dhw1_is_ng = VariableMeta(
            var_name='dhw1_is_ng', 
            attr_name='dhw1_is_ng', 
            icon='⚖', 
            label_de='PE WWWB 1 ist Erdgas', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_natural_gas', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.dhw2_is_ng = VariableMeta(
            var_name='dhw2_is_ng', 
            attr_name='dhw2_is_ng', 
            icon='⚖', 
            label_de='PE WWWB 2 ist Erdgas', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_natural_gas', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.heat_th2_is_bio = VariableMeta(
            var_name='heat_th2_is_bio', 
            attr_name='heat_th2_is_bio', 
            icon='⚖', 
            label_de='PE Heizen 2 ist Biomasse', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_biomass', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.heat_th4_is_bio = VariableMeta(
            var_name='heat_th4_is_bio', 
            attr_name='heat_th4_is_bio', 
            icon='⚖', 
            label_de='PE Heizen 4 ist Biomasse', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_biomass', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.cool_th2_is_bio = VariableMeta(
            var_name='cool_th2_is_bio', 
            attr_name='cool_th2_is_bio', 
            icon='⚖', 
            label_de='PE Kühlen 2 ist Biomasse', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_biomass', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.dhw1_is_bio = VariableMeta(
            var_name='dhw1_is_bio', 
            attr_name='dhw1_is_bio', 
            icon='⚖', 
            label_de='PE WWWB 1 ist Biomasse', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_biomass', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.dhw2_is_bio = VariableMeta(
            var_name='dhw2_is_bio', 
            attr_name='dhw2_is_bio', 
            icon='⚖', 
            label_de='PE WWWB 2 ist Biomasse', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_biomass', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.heat_th2_is_other = VariableMeta(
            var_name='heat_th2_is_other', 
            attr_name='heat_th2_is_other', 
            icon='⚖', 
            label_de='PE Heizen 2 ist Sonstige', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_other', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.heat_th4_is_other = VariableMeta(
            var_name='heat_th4_is_other', 
            attr_name='heat_th4_is_other', 
            icon='⚖', 
            label_de='PE Heizen 4 ist Sonstige', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_other', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.cool_th2_is_other = VariableMeta(
            var_name='cool_th2_is_other', 
            attr_name='cool_th2_is_other', 
            icon='⚖', 
            label_de='PE Kühlen 2 ist Sonstige', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_other', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.dhw1_is_other = VariableMeta(
            var_name='dhw1_is_other', 
            attr_name='dhw1_is_other', 
            icon='⚖', 
            label_de='PE WWWB 1 ist Sonstige', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_other', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.dhw2_is_other = VariableMeta(
            var_name='dhw2_is_other', 
            attr_name='dhw2_is_other', 
            icon='⚖', 
            label_de='PE WWWB 2 ist Sonstige', 
            unit='bool', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='primary_energy', 
            measure='is_other', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.fPE_flex_factor = VariableMeta(
            var_name='fPE_flex_factor', 
            attr_name='fPE_flex_factor', 
            icon='⚖', 
            label_de='Flexibler Netzbezug Anteil PE-Faktor', 
            unit=None, 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='primary_energy', 
            measure='flex_share', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.pe_conversion_factor_gasoline = VariableMeta(
            var_name='pe_conversion_factor_gasoline', 
            attr_name='pe_conversion_factor_gasoline', 
            icon='⚖', 
            label_de='PE-Konversionsfaktor Kraftstoff', 
            unit='kWhPE/kWhEE', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='primary_energy', 
            measure='conversion_factor', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.StatPAX_residential = VariableMeta(
            var_name='StatPAX_residential', 
            attr_name='StatPAX_residential', 
            icon='🚗', 
            label_de='Mobilitätsstatistische Nutzer Wohnen', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='mobility', 
            measure='statistical_persons', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='residential'
        )
        self.StatPAX_office = VariableMeta(
            var_name='StatPAX_office', 
            attr_name='StatPAX_office', 
            icon='🚗', 
            label_de='Mobilitätsstatistische Nutzer Büro', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='mobility', 
            measure='statistical_persons', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='office'
        )
        self.StatPAX_schoolsec = VariableMeta(
            var_name='StatPAX_schoolsec', 
            attr_name='StatPAX_schoolsec', 
            icon='🚗', 
            label_de='Mobilitätsstatistische Nutzer Schule sekundär', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='mobility', 
            measure='statistical_persons', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolsec'
        )
        self.StatPAX_schoolprim = VariableMeta(
            var_name='StatPAX_schoolprim', 
            attr_name='StatPAX_schoolprim', 
            icon='🚗', 
            label_de='Mobilitätsstatistische Nutzer Schule primär', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='mobility', 
            measure='statistical_persons', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='schoolprim'
        )
        self.StatPAX_retail = VariableMeta(
            var_name='StatPAX_retail', 
            attr_name='StatPAX_retail', 
            icon='🚗', 
            label_de='Mobilitätsstatistische Nutzer Handel Supermarkt', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='mobility', 
            measure='statistical_persons', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailfood'
        )
        self.StatPAX_retailother = VariableMeta(
            var_name='StatPAX_retailother', 
            attr_name='StatPAX_retailother', 
            icon='🚗', 
            label_de='Mobilitätsstatistische Nutzer Handel Sonstige', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=0, 
            domain='mobility', 
            measure='statistical_persons', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group='usage', 
            entity_key='retailother'
        )
        self.e_kWhm2a = VariableMeta(
            var_name='e_kWhm2a', 
            attr_name='e_kWhm2a', 
            icon='☑', 
            label_de='Test precision kWhm2NFAa', 
            unit='kWh/m²NFA', 
            comment=None, 
            source='IN', 
            ka=1, 
            domain='tool', 
            measure='precision', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_charging_stations = VariableMeta(
            var_name='EV_charging_stations', 
            attr_name='EV_charging_stations', 
            icon='🚗', 
            label_de='Anzahl Ladestationen', 
            unit='-', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='mobility', 
            measure='charging_stations', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_charging_station_power = VariableMeta(
            var_name='EV_charging_station_power', 
            attr_name='EV_charging_station_power', 
            icon='🚗', 
            label_de='Leistung Ladestation', 
            unit='kW', 
            comment=None, 
            source='IN', 
            ka=2, 
            domain='mobility', 
            measure='charging_station_power', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_name = VariableMeta(
            var_name='project_name', 
            attr_name='project_name', 
            icon=None, 
            label_de='Projektname', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.location_address = VariableMeta(
            var_name='location_address', 
            attr_name='location_address', 
            icon=None, 
            label_de='Adresse', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_creation_date = VariableMeta(
            var_name='project_creation_date', 
            attr_name='project_creation_date', 
            icon=None, 
            label_de='Erstellungsdatum', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.project_scenario_name = VariableMeta(
            var_name='project_scenario_name', 
            attr_name='project_scenario_name', 
            icon=None, 
            label_de='Variante / Scenario', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.FSI = VariableMeta(
            var_name='FSI', 
            attr_name='FSI', 
            icon=None, 
            label_de='GFZ', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.renovation_share = VariableMeta(
            var_name='renovation_share', 
            attr_name='renovation_share', 
            icon=None, 
            label_de='Sanierungsanteil', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.rh_avg = VariableMeta(
            var_name='rh_avg', 
            attr_name='rh_avg', 
            icon=None, 
            label_de='Raumhöhe', 
            unit='m Netto', 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.lc = VariableMeta(
            var_name='lc', 
            attr_name='lc', 
            icon=None, 
            label_de='Charakteristische Länge (lc)', 
            unit='m', 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.weather_name = VariableMeta(
            var_name='weather_name', 
            attr_name='weather_name', 
            icon=None, 
            label_de='Wetterdatensatz Name', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.weather_index = VariableMeta(
            var_name='weather_index', 
            attr_name='weather_index', 
            icon=None, 
            label_de='Wetterdatensatz Nummer', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Ta_annual_avg = VariableMeta(
            var_name='Ta_annual_avg', 
            attr_name='Ta_annual_avg', 
            icon=None, 
            label_de='Außentemperatur Jahresmittel', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='weather', 
            measure='Wetter', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Ta_avg_heating_period = VariableMeta(
            var_name='Ta_avg_heating_period', 
            attr_name='Ta_avg_heating_period', 
            icon=None, 
            label_de='Mittelaußentemperatur Heizperiode', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='weather', 
            measure='temperature', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Ta_avg_cooling_period = VariableMeta(
            var_name='Ta_avg_cooling_period', 
            attr_name='Ta_avg_cooling_period', 
            icon=None, 
            label_de='Mittelaußentemperatur Kühlperiode', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='weather', 
            measure='temperature', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.UED_plugloads = VariableMeta(
            var_name='UED_plugloads', 
            attr_name='UED_plugloads', 
            icon='🔌', 
            label_de='Nutzerstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='plugloads', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_lighting = VariableMeta(
            var_name='UED_lighting', 
            attr_name='UED_lighting', 
            icon='💡', 
            label_de='Beleuchtung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='lighting', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_auxiliary = VariableMeta(
            var_name='UED_auxiliary', 
            attr_name='UED_auxiliary', 
            icon='🌃', 
            label_de='Allgemeinstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='aux_el_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_heating = VariableMeta(
            var_name='UED_heating', 
            attr_name='UED_heating', 
            icon='🔥', 
            label_de='Heiwärmebedarf', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_cooling = VariableMeta(
            var_name='UED_cooling', 
            attr_name='UED_cooling', 
            icon='❄', 
            label_de='Külenergiebedarf', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_dhw = VariableMeta(
            var_name='UED_dhw', 
            attr_name='UED_dhw', 
            icon='💧', 
            label_de='WWWB', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='dhw_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_ventilation = VariableMeta(
            var_name='UED_ventilation', 
            attr_name='UED_ventilation', 
            icon='💨', 
            label_de='Lüftungsenergiebedarf', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure='vent_el_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_mim_electric = VariableMeta(
            var_name='UED_mim_electric', 
            attr_name='UED_mim_electric', 
            icon='🚗', 
            label_de='E-Mobilität', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure=None, 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.UED_mim_fossile = VariableMeta(
            var_name='UED_mim_fossile', 
            attr_name='UED_mim_fossile', 
            icon='🚗', 
            label_de='Fossile Mobilität', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='useful_energy', 
            measure=None, 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QT = VariableMeta(
            var_name='QT', 
            attr_name='QT', 
            icon='🧱', 
            label_de='Transmissionswärmeverl.', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV = VariableMeta(
            var_name='QV', 
            attr_name='QV', 
            icon='💨', 
            label_de='Lüftungswärmeverluste', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QVn = VariableMeta(
            var_name='QVn', 
            attr_name='QVn', 
            icon='🌒', 
            label_de='Nachtlüftung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QS = VariableMeta(
            var_name='QS', 
            attr_name='QS', 
            icon='🌞', 
            label_de='Solare Gewinne', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QI = VariableMeta(
            var_name='QI', 
            attr_name='QI', 
            icon='👤', 
            label_de='Innere Wärmen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH = VariableMeta(
            var_name='QH', 
            attr_name='QH', 
            icon='♨', 
            label_de='Heizwärmebedarf', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QC = VariableMeta(
            var_name='QC', 
            attr_name='QC', 
            icon='❄', 
            label_de='Kühlbedarf (KB)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_heatrecovery = VariableMeta(
            var_name='QV_heatrecovery', 
            attr_name='QV_heatrecovery', 
            icon=None, 
            label_de='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_recovery', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_winter = VariableMeta(
            var_name='QT_winter', 
            attr_name='QT_winter', 
            icon=None, 
            label_de='Transmissionswärmeverl.', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_winter = VariableMeta(
            var_name='QV_winter', 
            attr_name='QV_winter', 
            icon=None, 
            label_de='Lüftungswärmeverluste', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QVn_winter = VariableMeta(
            var_name='QVn_winter', 
            attr_name='QVn_winter', 
            icon=None, 
            label_de='Nachtlüftung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QS_winter = VariableMeta(
            var_name='QS_winter', 
            attr_name='QS_winter', 
            icon=None, 
            label_de='Solare Gewinne', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QI_winter = VariableMeta(
            var_name='QI_winter', 
            attr_name='QI_winter', 
            icon=None, 
            label_de='Innere Wärmen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_winter = VariableMeta(
            var_name='QH_winter', 
            attr_name='QH_winter', 
            icon=None, 
            label_de='Heizwärmebedarf', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_winter = VariableMeta(
            var_name='QC_winter', 
            attr_name='QC_winter', 
            icon=None, 
            label_de='Kühlbedarf (KB)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.test_heat_balance_winter = VariableMeta(
            var_name='test_heat_balance_winter', 
            attr_name='test_heat_balance_winter', 
            icon='☑', 
            label_de='Wärmebilanz Heizperiode', 
            unit='False', 
            comment=None, 
            source='OUT', 
            ka=4, 
            domain='heat_balance', 
            measure='test', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.QT_wall_winter = VariableMeta(
            var_name='QT_wall_winter', 
            attr_name='QT_wall_winter', 
            icon=None, 
            label_de='Transmission AW', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='wall'
        )
        self.QT_roof_winter = VariableMeta(
            var_name='QT_roof_winter', 
            attr_name='QT_roof_winter', 
            icon=None, 
            label_de='Transmission Dach', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='roof'
        )
        self.QT_ground_winter = VariableMeta(
            var_name='QT_ground_winter', 
            attr_name='QT_ground_winter', 
            icon=None, 
            label_de='Transmission KD/EFB', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.QT_window_winter = VariableMeta(
            var_name='QT_window_winter', 
            attr_name='QT_window_winter', 
            icon=None, 
            label_de='Transmission Fenster', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key='windows'
        )
        self.QT_psi_winter = VariableMeta(
            var_name='QT_psi_winter', 
            attr_name='QT_psi_winter', 
            icon=None, 
            label_de='Transmission Wärmebrücken', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group='hull', 
            entity_key=None
        )
        self.QV_inf_winter = VariableMeta(
            var_name='QV_inf_winter', 
            attr_name='QV_inf_winter', 
            icon=None, 
            label_de='Infiltration', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_window_winter = VariableMeta(
            var_name='QV_window_winter', 
            attr_name='QV_window_winter', 
            icon=None, 
            label_de='Lüftung Fenster', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_mechvent_winter = VariableMeta(
            var_name='QV_mechvent_winter', 
            attr_name='QV_mechvent_winter', 
            icon=None, 
            label_de='Mechanische Lüftung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_heatrecovery_winter = VariableMeta(
            var_name='QV_heatrecovery_winter', 
            attr_name='QV_heatrecovery_winter', 
            icon=None, 
            label_de='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_recovery', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_min_winter = VariableMeta(
            var_name='QH_min_winter', 
            attr_name='QH_min_winter', 
            icon=None, 
            label_de='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flex_winter = VariableMeta(
            var_name='QH_flex_winter', 
            attr_name='QH_flex_winter', 
            icon=None, 
            label_de='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_min_winter = VariableMeta(
            var_name='QC_min_winter', 
            attr_name='QC_min_winter', 
            icon=None, 
            label_de='Kühlbedarf Statisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_flex_winter = VariableMeta(
            var_name='QC_flex_winter', 
            attr_name='QC_flex_winter', 
            icon=None, 
            label_de='Kühlbedarf Flexibel', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flexshare_winter = VariableMeta(
            var_name='QH_flexshare_winter', 
            attr_name='QH_flexshare_winter', 
            icon=None, 
            label_de='Anteil Flexibler Heizung an Gesamtheizung', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_flexshare_winter = VariableMeta(
            var_name='QC_flexshare_winter', 
            attr_name='QC_flexshare_winter', 
            icon='F', 
            label_de='Anteil Flexibler Kühlung an Gesamtkühlung', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='district', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_summer = VariableMeta(
            var_name='QT_summer', 
            attr_name='QT_summer', 
            icon=None, 
            label_de='Transmissionswärmeverl.', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_summer = VariableMeta(
            var_name='QV_summer', 
            attr_name='QV_summer', 
            icon=None, 
            label_de='Lüftungswärmeverluste', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QVn_summer = VariableMeta(
            var_name='QVn_summer', 
            attr_name='QVn_summer', 
            icon=None, 
            label_de='Nachtlüftung gekühlt', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QS_summer = VariableMeta(
            var_name='QS_summer', 
            attr_name='QS_summer', 
            icon=None, 
            label_de='Solare Gewinne', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QI_summer = VariableMeta(
            var_name='QI_summer', 
            attr_name='QI_summer', 
            icon=None, 
            label_de='Innere Wärmen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_summer = VariableMeta(
            var_name='QH_summer', 
            attr_name='QH_summer', 
            icon=None, 
            label_de='Heizwärmebedarf', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_summer = VariableMeta(
            var_name='QC_summer', 
            attr_name='QC_summer', 
            icon=None, 
            label_de='Kühlbedarf (KB)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.test_heat_balance_summer = VariableMeta(
            var_name='test_heat_balance_summer', 
            attr_name='test_heat_balance_summer', 
            icon='☑', 
            label_de='Wärmebilanz Kühlperiode', 
            unit='False', 
            comment=None, 
            source='OUT', 
            ka=4, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='Test', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_wall_summer = VariableMeta(
            var_name='QT_wall_summer', 
            attr_name='QT_wall_summer', 
            icon=None, 
            label_de='Transmission AW', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='wall'
        )
        self.QT_roof_summer = VariableMeta(
            var_name='QT_roof_summer', 
            attr_name='QT_roof_summer', 
            icon=None, 
            label_de='Transmission Dach', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='roof'
        )
        self.QT_ground_summer = VariableMeta(
            var_name='QT_ground_summer', 
            attr_name='QT_ground_summer', 
            icon=None, 
            label_de='Transmission KD/EFB', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.QT_window_summer = VariableMeta(
            var_name='QT_window_summer', 
            attr_name='QT_window_summer', 
            icon=None, 
            label_de='Transmission Fenster', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key='windows'
        )
        self.QT_psi_summer = VariableMeta(
            var_name='QT_psi_summer', 
            attr_name='QT_psi_summer', 
            icon=None, 
            label_de='Transmission Wärmebrücken', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group='hull', 
            entity_key=None
        )
        self.QV_inf_summer = VariableMeta(
            var_name='QV_inf_summer', 
            attr_name='QV_inf_summer', 
            icon=None, 
            label_de='Infiltration', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_window_summer = VariableMeta(
            var_name='QV_window_summer', 
            attr_name='QV_window_summer', 
            icon=None, 
            label_de='Lüftung Fenster', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_mechvent_summer = VariableMeta(
            var_name='QV_mechvent_summer', 
            attr_name='QV_mechvent_summer', 
            icon=None, 
            label_de='Mechanische Lüftung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_heatrecovery_summer = VariableMeta(
            var_name='QV_heatrecovery_summer', 
            attr_name='QV_heatrecovery_summer', 
            icon=None, 
            label_de='ML Wärmerückgewinnung 2', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_recovery', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_min_summer = VariableMeta(
            var_name='QH_min_summer', 
            attr_name='QH_min_summer', 
            icon=None, 
            label_de='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flex_summer = VariableMeta(
            var_name='QH_flex_summer', 
            attr_name='QH_flex_summer', 
            icon=None, 
            label_de='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_min_summer = VariableMeta(
            var_name='QC_min_summer', 
            attr_name='QC_min_summer', 
            icon=None, 
            label_de='Kühlbedarf Statisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_flex_summer = VariableMeta(
            var_name='QC_flex_summer', 
            attr_name='QC_flex_summer', 
            icon=None, 
            label_de='Kühlbedarf Flexibel', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flexshare_summer = VariableMeta(
            var_name='QH_flexshare_summer', 
            attr_name='QH_flexshare_summer', 
            icon=None, 
            label_de='Anteil Flexibler Heizung an Gesamtheizung', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_flexshare_summer = VariableMeta(
            var_name='QC_flexshare_summer', 
            attr_name='QC_flexshare_summer', 
            icon=None, 
            label_de='Anteil Flexibler Kühlung an Gesamtkühlung', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='district', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.test_heat_balance = VariableMeta(
            var_name='test_heat_balance', 
            attr_name='test_heat_balance', 
            icon='☑', 
            label_de='Wärmebilanz', 
            unit='True', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='Test', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_u = VariableMeta(
            var_name='QT_u', 
            attr_name='QT_u', 
            icon='🧱', 
            label_de='Transmissionswärmeverl.', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_u = VariableMeta(
            var_name='QV_u', 
            attr_name='QV_u', 
            icon='💨', 
            label_de='Lüftungswärmeverluste', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QVn_u = VariableMeta(
            var_name='QVn_u', 
            attr_name='QVn_u', 
            icon='🌒', 
            label_de='Nachtlüftung', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QS_u = VariableMeta(
            var_name='QS_u', 
            attr_name='QS_u', 
            icon='🌞', 
            label_de='Solare Gewinne', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QI_u = VariableMeta(
            var_name='QI_u', 
            attr_name='QI_u', 
            icon='👤', 
            label_de='Innere Wärmen', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_u = VariableMeta(
            var_name='QH_u', 
            attr_name='QH_u', 
            icon='♨', 
            label_de='Heizwärmebedarf', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_wall_u = VariableMeta(
            var_name='QT_wall_u', 
            attr_name='QT_wall_u', 
            icon='🧱', 
            label_de='Transmission AW', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='wall'
        )
        self.QT_roof_u = VariableMeta(
            var_name='QT_roof_u', 
            attr_name='QT_roof_u', 
            icon='🧱', 
            label_de='Transmission Dach', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='roof'
        )
        self.QT_ground_u = VariableMeta(
            var_name='QT_ground_u', 
            attr_name='QT_ground_u', 
            icon='🧱', 
            label_de='Transmission KD/EFB', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.QT_window_u = VariableMeta(
            var_name='QT_window_u', 
            attr_name='QT_window_u', 
            icon='🧱', 
            label_de='Transmission Fenster', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='windows'
        )
        self.QT_psi_u = VariableMeta(
            var_name='QT_psi_u', 
            attr_name='QT_psi_u', 
            icon='🧱', 
            label_de='Transmission Wärmebrücken', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key=None
        )
        self.QV_inf_u = VariableMeta(
            var_name='QV_inf_u', 
            attr_name='QV_inf_u', 
            icon='💨', 
            label_de='Infiltration', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_window_u = VariableMeta(
            var_name='QV_window_u', 
            attr_name='QV_window_u', 
            icon='💨', 
            label_de='Lüftung Fenster', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_mechvent_u = VariableMeta(
            var_name='QV_mechvent_u', 
            attr_name='QV_mechvent_u', 
            icon='💨', 
            label_de='Mechanische Lüftung', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_heatrecovery_u = VariableMeta(
            var_name='QV_heatrecovery_u', 
            attr_name='QV_heatrecovery_u', 
            icon='🔀', 
            label_de='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_recovery', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_min_u = VariableMeta(
            var_name='QH_min_u', 
            attr_name='QH_min_u', 
            icon='♨', 
            label_de='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flex_u = VariableMeta(
            var_name='QH_flex_u', 
            attr_name='QH_flex_u', 
            icon='♨', 
            label_de='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFungekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flexanteil_u = VariableMeta(
            var_name='QH_flexanteil_u', 
            attr_name='QH_flexanteil_u', 
            icon='F', 
            label_de='Flexibilitätsanteil', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='uncooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_c = VariableMeta(
            var_name='QT_c', 
            attr_name='QT_c', 
            icon='🧱', 
            label_de='Transmissionswärmeverl.', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_c = VariableMeta(
            var_name='QV_c', 
            attr_name='QV_c', 
            icon='💨', 
            label_de='Lüftungswärmeverluste', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QVn_c = VariableMeta(
            var_name='QVn_c', 
            attr_name='QVn_c', 
            icon='🌒', 
            label_de='Nachtlüftung gekühlt', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QS_c = VariableMeta(
            var_name='QS_c', 
            attr_name='QS_c', 
            icon='🌞', 
            label_de='Solare Gewinne', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QI_c = VariableMeta(
            var_name='QI_c', 
            attr_name='QI_c', 
            icon='👤', 
            label_de='Innere Wärmen', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_gain', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_c = VariableMeta(
            var_name='QH_c', 
            attr_name='QH_c', 
            icon='♨', 
            label_de='Heizwärmebedarf', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_c = VariableMeta(
            var_name='QC_c', 
            attr_name='QC_c', 
            icon='❄', 
            label_de='Kühlbedarf (KB)', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QT_wall_c = VariableMeta(
            var_name='QT_wall_c', 
            attr_name='QT_wall_c', 
            icon='🧱', 
            label_de='Transmission AW', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='wall'
        )
        self.QT_roof_c = VariableMeta(
            var_name='QT_roof_c', 
            attr_name='QT_roof_c', 
            icon='🧱', 
            label_de='Transmission Dach', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='roof'
        )
        self.QT_ground_c = VariableMeta(
            var_name='QT_ground_c', 
            attr_name='QT_ground_c', 
            icon='🧱', 
            label_de='Transmission KD/EFB', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='fundament'
        )
        self.QT_window_c = VariableMeta(
            var_name='QT_window_c', 
            attr_name='QT_window_c', 
            icon='🧱', 
            label_de='Transmission Fenster', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key='windows'
        )
        self.QT_psi_c = VariableMeta(
            var_name='QT_psi_c', 
            attr_name='QT_psi_c', 
            icon='🧱', 
            label_de='Transmission Wärmebrücken', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group='hull', 
            entity_key=None
        )
        self.QV_inf_c = VariableMeta(
            var_name='QV_inf_c', 
            attr_name='QV_inf_c', 
            icon='💨', 
            label_de='Infiltration', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_window_c = VariableMeta(
            var_name='QV_window_c', 
            attr_name='QV_window_c', 
            icon='💨', 
            label_de='Lüftung Fenster', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_mechvent_c = VariableMeta(
            var_name='QV_mechvent_c', 
            attr_name='QV_mechvent_c', 
            icon='💨', 
            label_de='Mechanische Lüftung', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_loss', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QV_heatrecovery_c = VariableMeta(
            var_name='QV_heatrecovery_c', 
            attr_name='QV_heatrecovery_c', 
            icon='🔀', 
            label_de='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heat_recovery', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_min_c = VariableMeta(
            var_name='QH_min_c', 
            attr_name='QH_min_c', 
            icon='♨', 
            label_de='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flex_c = VariableMeta(
            var_name='QH_flex_c', 
            attr_name='QH_flex_c', 
            icon='♨', 
            label_de='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='heating_demand', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_min_c = VariableMeta(
            var_name='QC_min_c', 
            attr_name='QC_min_c', 
            icon='❄', 
            label_de='Kühlbedarf Statisch', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_flex_c = VariableMeta(
            var_name='QC_flex_c', 
            attr_name='QC_flex_c', 
            icon='❄', 
            label_de='Kühlbedarf Flexibel', 
            unit='kWh/m²NGFgekühlta', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure='cooling_demand', 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QC_flexanteil = VariableMeta(
            var_name='QC_flexanteil', 
            attr_name='QC_flexanteil', 
            icon='F', 
            label_de='Flexibilitätsanteil', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.QH_flexanteil_c = VariableMeta(
            var_name='QH_flexanteil_c', 
            attr_name='QH_flexanteil_c', 
            icon='F', 
            label_de='Flexibilitätsanteil', 
            unit='ratio', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='heat_balance', 
            measure=None, 
            spatial_scope='cooled', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.Tu_avg_winter = VariableMeta(
            var_name='Tu_avg_winter', 
            attr_name='Tu_avg_winter', 
            icon=None, 
            label_de='Mitteltemperatur ungekühlt', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature', 
            spatial_scope='uncooled', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.Tc_avg_winter = VariableMeta(
            var_name='Tc_avg_winter', 
            attr_name='Tc_avg_winter', 
            icon=None, 
            label_de='Mitteltemperatur gekühlt', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature', 
            spatial_scope='cooled', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.Tu_avg_summer = VariableMeta(
            var_name='Tu_avg_summer', 
            attr_name='Tu_avg_summer', 
            icon=None, 
            label_de='Mitteltemperatur ungekühlt', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature', 
            spatial_scope='uncooled', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.Tc_avg_summer = VariableMeta(
            var_name='Tc_avg_summer', 
            attr_name='Tc_avg_summer', 
            icon=None, 
            label_de='Mitteltemperatur gekühlt', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature', 
            spatial_scope='cooled', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.dTu_winter = VariableMeta(
            var_name='dTu_winter', 
            attr_name='dTu_winter', 
            icon=None, 
            label_de='Mittlere Temperaturüberschreitung ungekühlt', 
            unit='K', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature_difference', 
            spatial_scope='uncooled', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.dTc_winter = VariableMeta(
            var_name='dTc_winter', 
            attr_name='dTc_winter', 
            icon=None, 
            label_de='Mittlere Temperaturüberschreitung gekühlt', 
            unit='K', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature_difference', 
            spatial_scope='cooled', 
            temporal_scope='winter', 
            entity_group=None, 
            entity_key=None
        )
        self.dTu_summer = VariableMeta(
            var_name='dTu_summer', 
            attr_name='dTu_summer', 
            icon=None, 
            label_de='Mittlere Temperaturunterschreitung ungekühlt', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature_difference', 
            spatial_scope='uncooled', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.dTc_summer = VariableMeta(
            var_name='dTc_summer', 
            attr_name='dTc_summer', 
            icon=None, 
            label_de='Mittlere Temperaturunterschreitung gekühlt', 
            unit='°C', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='comfort', 
            measure='temperature_difference', 
            spatial_scope='cooled', 
            temporal_scope='summer', 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_plugAuxLight = VariableMeta(
            var_name='EUI_plugAuxLight', 
            attr_name='EUI_plugAuxLight', 
            icon=None, 
            label_de='Nutzerstrom, Beleuchtung und Allgemeinstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='user_electricity', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_plugloads = VariableMeta(
            var_name='EUI_plugloads', 
            attr_name='EUI_plugloads', 
            icon=None, 
            label_de='Nutzerstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='plugloads', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_auxiliary = VariableMeta(
            var_name='EUI_auxiliary', 
            attr_name='EUI_auxiliary', 
            icon=None, 
            label_de='Allgemeinstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='aux_el_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_lighting = VariableMeta(
            var_name='EUI_lighting', 
            attr_name='EUI_lighting', 
            icon=None, 
            label_de='Beleuchtung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='lighting', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_el = VariableMeta(
            var_name='EUIh_el', 
            attr_name='EUIh_el', 
            icon=None, 
            label_de='Heizen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='heating_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_el_aux = VariableMeta(
            var_name='EUIh_el_aux', 
            attr_name='EUIh_el_aux', 
            icon=None, 
            label_de='Heizen Hilfsstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='heating_aux', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIc_el = VariableMeta(
            var_name='EUIc_el', 
            attr_name='EUIc_el', 
            icon=None, 
            label_de='Kühlen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='cooling_demand', 
            spatial_scope='district', 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIc_el_aux = VariableMeta(
            var_name='EUIc_el_aux', 
            attr_name='EUIc_el_aux', 
            icon=None, 
            label_de='Heizen Hilfsstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='cooling_aux', 
            spatial_scope='district', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUIdhw_el = VariableMeta(
            var_name='EUIdhw_el', 
            attr_name='EUIdhw_el', 
            icon=None, 
            label_de='Warmwasser', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUIv_el = VariableMeta(
            var_name='EUIv_el', 
            attr_name='EUIv_el', 
            icon=None, 
            label_de='Lüftung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='vent_el_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUIdhwdirect_el = VariableMeta(
            var_name='EUIdhwdirect_el', 
            attr_name='EUIdhwdirect_el', 
            icon=None, 
            label_de='WW\nE-Stab', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='dhw_demand', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_total_charge_input = VariableMeta(
            var_name='Batt_total_charge_input', 
            attr_name='Batt_total_charge_input', 
            icon=None, 
            label_de='e-Speicher Beladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='battery_charge', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUIev_el = VariableMeta(
            var_name='EUIev_el', 
            attr_name='EUIev_el', 
            icon=None, 
            label_de='EV Quartiersladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='ev_local_charge', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_el_total = VariableMeta(
            var_name='EUI_el_total', 
            attr_name='EUI_el_total', 
            icon='O', 
            label_de='Quartier', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_end_use', 
            measure='total', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_total = VariableMeta(
            var_name='PV_total', 
            attr_name='PV_total', 
            icon='🌞', 
            label_de='PV Ertrag', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.PV_to_plugloads = VariableMeta(
            var_name='PV_to_plugloads', 
            attr_name='PV_to_plugloads', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='user_electricity'
        )
        self.PV_to_Eh_min = VariableMeta(
            var_name='PV_to_Eh_min', 
            attr_name='PV_to_Eh_min', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.PV_to_Ec_min = VariableMeta(
            var_name='PV_to_Ec_min', 
            attr_name='PV_to_Ec_min', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.PV_to_Edhw_min = VariableMeta(
            var_name='PV_to_Edhw_min', 
            attr_name='PV_to_Edhw_min', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.PV_to_Ev_min = VariableMeta(
            var_name='PV_to_Ev_min', 
            attr_name='PV_to_Ev_min', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.PV_to_Eev_min = VariableMeta(
            var_name='PV_to_Eev_min', 
            attr_name='PV_to_Eev_min', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='ev_local_charge'
        )
        self.PV_total_direct = VariableMeta(
            var_name='PV_total_direct', 
            attr_name='PV_total_direct', 
            icon='🌞', 
            label_de='3 static', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key=None
        )
        self.PV_to_Eh_flex = VariableMeta(
            var_name='PV_to_Eh_flex', 
            attr_name='PV_to_Eh_flex', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='user_electricity'
        )
        self.PV_to_Ec_flex = VariableMeta(
            var_name='PV_to_Ec_flex', 
            attr_name='PV_to_Ec_flex', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.PV_to_Edhw = VariableMeta(
            var_name='PV_to_Edhw', 
            attr_name='PV_to_Edhw', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.PV_to_Edhw_direct = VariableMeta(
            var_name='PV_to_Edhw_direct', 
            attr_name='PV_to_Edhw_direct', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.PV_to_Batt = VariableMeta(
            var_name='PV_to_Batt', 
            attr_name='PV_to_Batt', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.PV_to_Eev_flex = VariableMeta(
            var_name='PV_to_Eev_flex', 
            attr_name='PV_to_Eev_flex', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='ev_local_charge'
        )
        self.PV_total_flex = VariableMeta(
            var_name='PV_total_flex', 
            attr_name='PV_total_flex', 
            icon='🌞', 
            label_de='3 flexible', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key=None
        )
        self.PV_to_Egrid = VariableMeta(
            var_name='PV_to_Egrid', 
            attr_name='PV_to_Egrid', 
            icon='🌞', 
            label_de='PV Netzeinspeisung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='PV_use', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_to_plugloads = VariableMeta(
            var_name='Batt_to_plugloads', 
            attr_name='Batt_to_plugloads', 
            icon='🔋', 
            label_de='E-Batterie → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='user_electricity'
        )
        self.Batt_to_HVAC = VariableMeta(
            var_name='Batt_to_HVAC', 
            attr_name='Batt_to_HVAC', 
            icon=None, 
            label_de='E-Batterie → HKLS', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_to_Eh_min = VariableMeta(
            var_name='Batt_to_Eh_min', 
            attr_name='Batt_to_Eh_min', 
            icon='🔋', 
            label_de='E-Batterie', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.Batt_to_Ec_min = VariableMeta(
            var_name='Batt_to_Ec_min', 
            attr_name='Batt_to_Ec_min', 
            icon='🔋', 
            label_de='E-Batterie', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.Batt_to_Edhw_min = VariableMeta(
            var_name='Batt_to_Edhw_min', 
            attr_name='Batt_to_Edhw_min', 
            icon='🔋', 
            label_de='E-Batterie', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.Batt_to_Ev_min = VariableMeta(
            var_name='Batt_to_Ev_min', 
            attr_name='Batt_to_Ev_min', 
            icon='🔋', 
            label_de='E-Batterie', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.Batt_to_Eev_min = VariableMeta(
            var_name='Batt_to_Eev_min', 
            attr_name='Batt_to_Eev_min', 
            icon='🔋', 
            label_de='E-Batterie', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='ev_local_charge'
        )
        self.Batt_charging_losses = VariableMeta(
            var_name='Batt_charging_losses', 
            attr_name='Batt_charging_losses', 
            icon=None, 
            label_de='E-Batterie Verluste', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='battery_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group=None, 
            entity_key=None
        )
        self.VRGrid_to_plugloads = VariableMeta(
            var_name='VRGrid_to_plugloads', 
            attr_name='VRGrid_to_plugloads', 
            icon='🔋', 
            label_de='Flexible Direktdeckung → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='user_electricity'
        )
        self.VRGrid_to_Eh_min = VariableMeta(
            var_name='VRGrid_to_Eh_min', 
            attr_name='VRGrid_to_Eh_min', 
            icon='🔋', 
            label_de='Flexible Direktdeckung → Heizen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.VRGrid_to_Ec_min = VariableMeta(
            var_name='VRGrid_to_Ec_min', 
            attr_name='VRGrid_to_Ec_min', 
            icon='🔋', 
            label_de='Flexible Direktdeckung → Kühlen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.VRGrid_to_Edhw_min = VariableMeta(
            var_name='VRGrid_to_Edhw_min', 
            attr_name='VRGrid_to_Edhw_min', 
            icon='🔋', 
            label_de='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.VRGrid_to_Ev_min = VariableMeta(
            var_name='VRGrid_to_Ev_min', 
            attr_name='VRGrid_to_Ev_min', 
            icon='🔋', 
            label_de='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.VRGrid_to_Eev_min = VariableMeta(
            var_name='VRGrid_to_Eev_min', 
            attr_name='VRGrid_to_Eev_min', 
            icon='🔋', 
            label_de='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='ev_local_charge'
        )
        self.VRGrid_to_min = VariableMeta(
            var_name='VRGrid_to_min', 
            attr_name='VRGrid_to_min', 
            icon='🔋', 
            label_de='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope='district', 
            temporal_scope='flexible', 
            entity_group=None, 
            entity_key=None
        )
        self.VRGrid_to_Eh_flex = VariableMeta(
            var_name='VRGrid_to_Eh_flex', 
            attr_name='VRGrid_to_Eh_flex', 
            icon='🔋', 
            label_de='Flexible Überdeckung → Heizen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.VRGrid_to_Ec_flex = VariableMeta(
            var_name='VRGrid_to_Ec_flex', 
            attr_name='VRGrid_to_Ec_flex', 
            icon='🔋', 
            label_de='Flexible Überdeckung → Kühlen', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.VRGrid_to_Edhw_flex = VariableMeta(
            var_name='VRGrid_to_Edhw_flex', 
            attr_name='VRGrid_to_Edhw_flex', 
            icon='🔋', 
            label_de='Flexible Überdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.VRGrid_to_Batt = VariableMeta(
            var_name='VRGrid_to_Batt', 
            attr_name='VRGrid_to_Batt', 
            icon='🔋', 
            label_de='Flexible Überdeckung → Batterie', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.VRGrid_to_Eev_flex = VariableMeta(
            var_name='VRGrid_to_Eev_flex', 
            attr_name='VRGrid_to_Eev_flex', 
            icon='🔋', 
            label_de='Flexible Überdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group='energy_use', 
            entity_key='ev_local_charge'
        )
        self.VRGrid_to_flex = VariableMeta(
            var_name='VRGrid_to_flex', 
            attr_name='VRGrid_to_flex', 
            icon='🔋', 
            label_de='Flexible Überdeckung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope='district', 
            temporal_scope='flexible', 
            entity_group=None, 
            entity_key=None
        )
        self.VRGrid_to_building = VariableMeta(
            var_name='VRGrid_to_building', 
            attr_name='VRGrid_to_building', 
            icon='🔋', 
            label_de='Flexible Deckung → Gebäude', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='flexible_grid_use', 
            spatial_scope=None, 
            temporal_scope='flexible', 
            entity_group=None, 
            entity_key=None
        )
        self.Eev_to_plugloads = VariableMeta(
            var_name='Eev_to_plugloads', 
            attr_name='Eev_to_plugloads', 
            icon='🚗', 
            label_de='E-Car Entladung → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='user_electricity'
        )
        self.Eev_to_HVAC = VariableMeta(
            var_name='Eev_to_HVAC', 
            attr_name='Eev_to_HVAC', 
            icon=None, 
            label_de='E-Car Entladung → HKLS', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.Eev_to_Eh_min = VariableMeta(
            var_name='Eev_to_Eh_min', 
            attr_name='Eev_to_Eh_min', 
            icon='🚗', 
            label_de='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.Eev_to_Ec_min = VariableMeta(
            var_name='Eev_to_Ec_min', 
            attr_name='Eev_to_Ec_min', 
            icon='🚗', 
            label_de='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.Eev_to_Edhw_min = VariableMeta(
            var_name='Eev_to_Edhw_min', 
            attr_name='Eev_to_Edhw_min', 
            icon='🚗', 
            label_de='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.Eev_to_Ev_min = VariableMeta(
            var_name='Eev_to_Ev_min', 
            attr_name='Eev_to_Ev_min', 
            icon='🚗', 
            label_de='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.Eev_discharge_loss = VariableMeta(
            var_name='Eev_discharge_loss', 
            attr_name='Eev_discharge_loss', 
            icon='🚗', 
            label_de='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.Eev_to_district = VariableMeta(
            var_name='Eev_to_district', 
            attr_name='Eev_to_district', 
            icon='🚗', 
            label_de='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev2b_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.Grid_to_plugloads = VariableMeta(
            var_name='Grid_to_plugloads', 
            attr_name='Grid_to_plugloads', 
            icon='🔌', 
            label_de='Netzstrom → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='user_electricity'
        )
        self.Grid_to_Eh_min = VariableMeta(
            var_name='Grid_to_Eh_min', 
            attr_name='Grid_to_Eh_min', 
            icon='🔌', 
            label_de='Netzstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.Grid_to_Ec_min = VariableMeta(
            var_name='Grid_to_Ec_min', 
            attr_name='Grid_to_Ec_min', 
            icon='🔌', 
            label_de='Netzstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.Grid_to_Edhw_min = VariableMeta(
            var_name='Grid_to_Edhw_min', 
            attr_name='Grid_to_Edhw_min', 
            icon='🔌', 
            label_de='Netzstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.Grid_to_Ev_min = VariableMeta(
            var_name='Grid_to_Ev_min', 
            attr_name='Grid_to_Ev_min', 
            icon='🔌', 
            label_de='Netzstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='vent_el_demand'
        )
        self.Grid_to_building_min = VariableMeta(
            var_name='Grid_to_building_min', 
            attr_name='Grid_to_building_min', 
            icon='🔌', 
            label_de='Netzstrom → Gebäude', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.Grid_to_Eev_min = VariableMeta(
            var_name='Grid_to_Eev_min', 
            attr_name='Grid_to_Eev_min', 
            icon='🔌', 
            label_de='Netzstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='ev_local_charge'
        )
        self.Grid_to_min = VariableMeta(
            var_name='Grid_to_min', 
            attr_name='Grid_to_min', 
            icon='🔌', 
            label_de='Netzstrom → Quartier', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='grid_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.Eev_ext_charge = VariableMeta(
            var_name='Eev_ext_charge', 
            attr_name='Eev_ext_charge', 
            icon='🔌', 
            label_de='E-Car Ladung Außerhalb des Quartiers', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='electricity_dispatch', 
            measure='ev_charge_ext', 
            spatial_scope='external', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_district_heating = VariableMeta(
            var_name='EUIh_district_heating', 
            attr_name='EUIh_district_heating', 
            icon=None, 
            label_de='Fernwärme', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='district_heating_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.EUIdhw_district_heating = VariableMeta(
            var_name='EUIdhw_district_heating', 
            attr_name='EUIdhw_district_heating', 
            icon=None, 
            label_de='Fernwärme', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='district_heating_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.EUI_district_heating = VariableMeta(
            var_name='EUI_district_heating', 
            attr_name='EUI_district_heating', 
            icon=None, 
            label_de='Fernwärme', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='district_heating_use', 
            spatial_scope='district', 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_natural_gas = VariableMeta(
            var_name='EUIh_natural_gas', 
            attr_name='EUIh_natural_gas', 
            icon=None, 
            label_de='Gas', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='natural_gas_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.EUIdhw_natural_gas = VariableMeta(
            var_name='EUIdhw_natural_gas', 
            attr_name='EUIdhw_natural_gas', 
            icon=None, 
            label_de='Gas', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='natural_gas_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.EUI_natural_gas = VariableMeta(
            var_name='EUI_natural_gas', 
            attr_name='EUI_natural_gas', 
            icon=None, 
            label_de='Gas', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='natural_gas_use', 
            spatial_scope='district', 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_biomass = VariableMeta(
            var_name='EUIh_biomass', 
            attr_name='EUIh_biomass', 
            icon=None, 
            label_de='Biomasse', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='biomass_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.EUIdhw_biomass = VariableMeta(
            var_name='EUIdhw_biomass', 
            attr_name='EUIdhw_biomass', 
            icon=None, 
            label_de='Biomasse', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='biomass_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.EUI_biomass = VariableMeta(
            var_name='EUI_biomass', 
            attr_name='EUI_biomass', 
            icon=None, 
            label_de='Biomasse', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='biomass_use', 
            spatial_scope='district', 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_other = VariableMeta(
            var_name='EUIh_other', 
            attr_name='EUIh_other', 
            icon=None, 
            label_de='Sonstige', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='other_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='heating_demand'
        )
        self.EUIc_other = VariableMeta(
            var_name='EUIc_other', 
            attr_name='EUIc_other', 
            icon=None, 
            label_de='Sonstige', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='other_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='cooling_demand'
        )
        self.EUIdhw_other = VariableMeta(
            var_name='EUIdhw_other', 
            attr_name='EUIdhw_other', 
            icon=None, 
            label_de='Sonstige', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='other_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='energy_use', 
            entity_key='dhw_demand'
        )
        self.EUI_other = VariableMeta(
            var_name='EUI_other', 
            attr_name='EUI_other', 
            icon=None, 
            label_de='Sonstige', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='other_use', 
            spatial_scope='district', 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_mob_fossil = VariableMeta(
            var_name='EUI_mob_fossil', 
            attr_name='EUI_mob_fossil', 
            icon=None, 
            label_de='MIV Fossil', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='fossile_use', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group=None, 
            entity_key=None
        )
        self.EUIh_2th = VariableMeta(
            var_name='EUIh_2th', 
            attr_name='EUIh_2th', 
            icon=None, 
            label_de='Heizen 2', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='thermal_energy', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='heating', 
            entity_key='system_2'
        )
        self.EUIh_4th = VariableMeta(
            var_name='EUIh_4th', 
            attr_name='EUIh_4th', 
            icon=None, 
            label_de='Heizen 4', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='thermal_energy', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='heating', 
            entity_key='system_4'
        )
        self.EUIc_2th = VariableMeta(
            var_name='EUIc_2th', 
            attr_name='EUIc_2th', 
            icon=None, 
            label_de='Kühlen 2', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='thermal_energy', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='cooling', 
            entity_key='system_2'
        )
        self.EUIdhw_1th = VariableMeta(
            var_name='EUIdhw_1th', 
            attr_name='EUIdhw_1th', 
            icon=None, 
            label_de='WWWB1', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='thermal_energy', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='dhw', 
            entity_key='system_1'
        )
        self.EUIdhw_2th = VariableMeta(
            var_name='EUIdhw_2th', 
            attr_name='EUIdhw_2th', 
            icon=None, 
            label_de='WWWB2', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='energy_dispatch', 
            measure='thermal_energy', 
            spatial_scope=None, 
            temporal_scope='static', 
            entity_group='dhw', 
            entity_key='system_2'
        )
        self.Grid_total_flexandnotflex = VariableMeta(
            var_name='Grid_total_flexandnotflex', 
            attr_name='Grid_total_flexandnotflex', 
            icon=None, 
            label_de='Netzstrom insg. (Flexibel und Inflexibel)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='final_energy', 
            measure=None, 
            spatial_scope='Elektrisch', 
            temporal_scope='Quartier', 
            entity_group=None, 
            entity_key=None
        )
        self.context_factor_density = VariableMeta(
            var_name='context_factor_density', 
            attr_name='context_factor_density', 
            icon=None, 
            label_de='Kontextfaktor bauliche Dichte', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='PE-Bilanz', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.context_factor_mobility = VariableMeta(
            var_name='context_factor_mobility', 
            attr_name='context_factor_mobility', 
            icon=None, 
            label_de='Kontextfaktor Mobilität', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primray_energy', 
            measure='PE-Bilanz', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.context_factor_renovation = VariableMeta(
            var_name='context_factor_renovation', 
            attr_name='context_factor_renovation', 
            icon=None, 
            label_de='Kontextfaktor Sanierung', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primray_energy', 
            measure='PE-Bilanz', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_demand = VariableMeta(
            var_name='PEI_demand', 
            attr_name='PEI_demand', 
            icon=None, 
            label_de='Betriebsenergie', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='operation', 
            entity_key=None
        )
        self.PEI_el_plugloads = VariableMeta(
            var_name='PEI_el_plugloads', 
            attr_name='PEI_el_plugloads', 
            icon=None, 
            label_de='Nutzerstrom', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='plugloads', 
            entity_key='electricity'
        )
        self.PEI_el_hvac = VariableMeta(
            var_name='PEI_el_hvac', 
            attr_name='PEI_el_hvac', 
            icon=None, 
            label_de='HKLS Strom', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='hvac', 
            entity_key='electricity'
        )
        self.PEI_district_heating = VariableMeta(
            var_name='PEI_district_heating', 
            attr_name='PEI_district_heating', 
            icon=None, 
            label_de='HKLS Fernwärme', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='hvac', 
            entity_key='district_heating'
        )
        self.PEI_natural_gas = VariableMeta(
            var_name='PEI_natural_gas', 
            attr_name='PEI_natural_gas', 
            icon=None, 
            label_de='HKLS Erdgas', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='hvac', 
            entity_key='natural_gas'
        )
        self.PEI_biomass = VariableMeta(
            var_name='PEI_biomass', 
            attr_name='PEI_biomass', 
            icon=None, 
            label_de='HKLS Biomasse', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='hvac', 
            entity_key='biomass'
        )
        self.PEI_other = VariableMeta(
            var_name='PEI_other', 
            attr_name='PEI_other', 
            icon=None, 
            label_de='HKLS Sonstige', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='hvac', 
            entity_key='other'
        )
        self.PEI_mob_total = VariableMeta(
            var_name='PEI_mob_total', 
            attr_name='PEI_mob_total', 
            icon=None, 
            label_de='Mobilität (MIV)', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='mobility', 
            entity_key=None
        )
        self.PEI_mob_fossile = VariableMeta(
            var_name='PEI_mob_fossile', 
            attr_name='PEI_mob_fossile', 
            icon=None, 
            label_de='MIV Fossil', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='mobility', 
            entity_key='fossile'
        )
        self.PEI_mob_el = VariableMeta(
            var_name='PEI_mob_el', 
            attr_name='PEI_mob_el', 
            icon=None, 
            label_de='MIV Elektrisch', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='mobility', 
            entity_key='electricity'
        )
        self.PEI_storage_losses = VariableMeta(
            var_name='PEI_storage_losses', 
            attr_name='PEI_storage_losses', 
            icon=None, 
            label_de='Speicher-Verluste', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='demand', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='storage', 
            entity_key=None
        )
        self.PEI_cf_density = VariableMeta(
            var_name='PEI_cf_density', 
            attr_name='PEI_cf_density', 
            icon=None, 
            label_de='Kontext bauliche Dichte', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='supply', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='context_factor', 
            entity_key='density'
        )
        self.PEI_cf_mobility = VariableMeta(
            var_name='PEI_cf_mobility', 
            attr_name='PEI_cf_mobility', 
            icon=None, 
            label_de='Kontext Mobilität', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='supply', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='context_factor', 
            entity_key='mobility'
        )
        self.PEI_cf_renovation = VariableMeta(
            var_name='PEI_cf_renovation', 
            attr_name='PEI_cf_renovation', 
            icon=None, 
            label_de='Kontext Sanierung', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='supply', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group='context_factor', 
            entity_key='renovation'
        )
        self.PEI_sub_PV = VariableMeta(
            var_name='PEI_sub_PV', 
            attr_name='PEI_sub_PV', 
            icon=None, 
            label_de='Lokale Erneuerbare (Netzstrom Substitutionsäquivalent)', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='supply', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_sub_flex = VariableMeta(
            var_name='PEI_sub_flex', 
            attr_name='PEI_sub_flex', 
            icon=None, 
            label_de='Energieflexibilität (Netzstrom Substitutionsäquivalent)', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='supply', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_balance = VariableMeta(
            var_name='PEI_balance', 
            attr_name='PEI_balance', 
            icon=None, 
            label_de='PE-Bilanz Netzäquivalent', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='primary_energy_balance', 
            measure='balance', 
            spatial_scope=None, 
            temporal_scope='annual', 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_grid_import = VariableMeta(
            var_name='PEI_grid_import', 
            attr_name='PEI_grid_import', 
            icon=None, 
            label_de='Netzbezug', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='import', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_flex_import = VariableMeta(
            var_name='PEI_flex_import', 
            attr_name='PEI_flex_import', 
            icon=None, 
            label_de='Flexibler Bezug', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='import', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_evExtCharge_import = VariableMeta(
            var_name='PEI_evExtCharge_import', 
            attr_name='PEI_evExtCharge_import', 
            icon=None, 
            label_de='EV Externe Beladung', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='import', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_import = VariableMeta(
            var_name='PEI_import', 
            attr_name='PEI_import', 
            icon=None, 
            label_de='Primärenergie-Import', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='import', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_pv_export = VariableMeta(
            var_name='PEI_pv_export', 
            attr_name='PEI_pv_export', 
            icon=None, 
            label_de='PV Netzeinspeisung PE', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='export', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_evOtherTravel_export = VariableMeta(
            var_name='PEI_evOtherTravel_export', 
            attr_name='PEI_evOtherTravel_export', 
            icon=None, 
            label_de='EV Other Travels', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='export', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_export = VariableMeta(
            var_name='PEI_export', 
            attr_name='PEI_export', 
            icon=None, 
            label_de='Primärenergie-Export', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope='export', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_saldo_project = VariableMeta(
            var_name='PEI_saldo_project', 
            attr_name='PEI_saldo_project', 
            icon=None, 
            label_de='PE-IE-Bilanz Projektwert', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_saldo_target = VariableMeta(
            var_name='PEI_saldo_target', 
            attr_name='PEI_saldo_target', 
            icon=None, 
            label_de='PE-IE-Bilanz Zielwert', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PEI_importExport_balance = VariableMeta(
            var_name='PEI_importExport_balance', 
            attr_name='PEI_importExport_balance', 
            icon=None, 
            label_de='importExport Saldo Projektwert - Zielwert', 
            unit='kWhPEges./m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain='pe_import_export_balance', 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fPE_grid = VariableMeta(
            var_name='fPE_grid', 
            attr_name='fPE_grid', 
            icon=None, 
            label_de='PE Faktor Netzstrom Statistisch', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.fPE_eff = VariableMeta(
            var_name='fPE_eff', 
            attr_name='fPE_eff', 
            icon=None, 
            label_de='PE Faktor Netzstrom Effektiv', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_walls_fossile = VariableMeta(
            var_name='GWP_ee_walls_fossile', 
            attr_name='GWP_ee_walls_fossile', 
            icon='☁', 
            label_de='Bauteil Außenwand fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_walls_biogenic = VariableMeta(
            var_name='GWP_ee_walls_biogenic', 
            attr_name='GWP_ee_walls_biogenic', 
            icon='☁', 
            label_de='Bauteil Außenwand biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_walls = VariableMeta(
            var_name='GWP_life_walls', 
            attr_name='GWP_life_walls', 
            icon='☁', 
            label_de='Bauteil Außenwand Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_walls_fossil = VariableMeta(
            var_name='GWP_ee_lc_walls_fossil', 
            attr_name='GWP_ee_lc_walls_fossil', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_walls_biogenic = VariableMeta(
            var_name='GWP_ee_lc_walls_biogenic', 
            attr_name='GWP_ee_lc_walls_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_walls = VariableMeta(
            var_name='GWP_ee_lc_walls', 
            attr_name='GWP_ee_lc_walls', 
            icon='☁', 
            label_de='Bauteil Außenwand', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_windows_fossile = VariableMeta(
            var_name='GWP_ee_windows_fossile', 
            attr_name='GWP_ee_windows_fossile', 
            icon='☁', 
            label_de='Bauteil Fenster fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_windows_bigenic = VariableMeta(
            var_name='GWP_ee_windows_bigenic', 
            attr_name='GWP_ee_windows_bigenic', 
            icon='☁', 
            label_de='Bauteil Fenster biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_windows = VariableMeta(
            var_name='GWP_life_windows', 
            attr_name='GWP_life_windows', 
            icon='☁', 
            label_de='Bauteil Fenster Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_windows_fossile = VariableMeta(
            var_name='GWP_ee_lc_windows_fossile', 
            attr_name='GWP_ee_lc_windows_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_windows_biogenic = VariableMeta(
            var_name='GWP_ee_lc_windows_biogenic', 
            attr_name='GWP_ee_lc_windows_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_windows = VariableMeta(
            var_name='GWP_ee_lc_windows', 
            attr_name='GWP_ee_lc_windows', 
            icon='☁', 
            label_de='Bauteil Fenster', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_roof_fossile = VariableMeta(
            var_name='GWP_ee_roof_fossile', 
            attr_name='GWP_ee_roof_fossile', 
            icon='☁', 
            label_de='Bauteil Dach fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_roof_biogenic = VariableMeta(
            var_name='GWP_ee_roof_biogenic', 
            attr_name='GWP_ee_roof_biogenic', 
            icon='☁', 
            label_de='Bauteil Dach biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_roof = VariableMeta(
            var_name='GWP_life_roof', 
            attr_name='GWP_life_roof', 
            icon='☁', 
            label_de='Bauteil Dach Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_roof_fossile = VariableMeta(
            var_name='GWP_ee_lc_roof_fossile', 
            attr_name='GWP_ee_lc_roof_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_roof_biogenic = VariableMeta(
            var_name='GWP_ee_lc_roof_biogenic', 
            attr_name='GWP_ee_lc_roof_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_roof = VariableMeta(
            var_name='GWP_ee_lc_roof', 
            attr_name='GWP_ee_lc_roof', 
            icon='☁', 
            label_de='Bauteil Dach', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_ground_fossile = VariableMeta(
            var_name='GWP_ee_ground_fossile', 
            attr_name='GWP_ee_ground_fossile', 
            icon='☁', 
            label_de='Bauteil Decke gegen Erdreich / Keller fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_ground_biogenic = VariableMeta(
            var_name='GWP_ee_ground_biogenic', 
            attr_name='GWP_ee_ground_biogenic', 
            icon='☁', 
            label_de='Bauteil Decke gegen Erdreich / Keller biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_ground = VariableMeta(
            var_name='GWP_life_ground', 
            attr_name='GWP_life_ground', 
            icon='☁', 
            label_de='Bauteil Decke gegen Erdreich / Keller Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ground_fossile = VariableMeta(
            var_name='GWP_ee_lc_ground_fossile', 
            attr_name='GWP_ee_lc_ground_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ground_biogenic = VariableMeta(
            var_name='GWP_ee_lc_ground_biogenic', 
            attr_name='GWP_ee_lc_ground_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ground = VariableMeta(
            var_name='GWP_ee_lc_ground', 
            attr_name='GWP_ee_lc_ground', 
            icon='☁', 
            label_de='Bauteil Decke gegen Erdreich / Keller', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_ceilings_fossile = VariableMeta(
            var_name='GWP_ee_ceilings_fossile', 
            attr_name='GWP_ee_ceilings_fossile', 
            icon='☁', 
            label_de='Bauteil Zwischengeschoßdecken fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_ceilings_biogenic = VariableMeta(
            var_name='GWP_ee_ceilings_biogenic', 
            attr_name='GWP_ee_ceilings_biogenic', 
            icon='☁', 
            label_de='Bauteil Zwischengeschoßdecken biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_ceilings = VariableMeta(
            var_name='GWP_life_ceilings', 
            attr_name='GWP_life_ceilings', 
            icon='☁', 
            label_de='Bauteil Zwischengeschoßdecken Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ceilings_fossile = VariableMeta(
            var_name='GWP_ee_lc_ceilings_fossile', 
            attr_name='GWP_ee_lc_ceilings_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ceilings_biogenic = VariableMeta(
            var_name='GWP_ee_lc_ceilings_biogenic', 
            attr_name='GWP_ee_lc_ceilings_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ceil = VariableMeta(
            var_name='GWP_ee_lc_ceil', 
            attr_name='GWP_ee_lc_ceil', 
            icon='☁', 
            label_de='Bauteil Zwischengeschoßdecken', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_general_fossile = VariableMeta(
            var_name='GWP_ee_general_fossile', 
            attr_name='GWP_ee_general_fossile', 
            icon='☁', 
            label_de='Baulich Allgemein fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_general_bigonenic = VariableMeta(
            var_name='GWP_ee_general_bigonenic', 
            attr_name='GWP_ee_general_bigonenic', 
            icon='☁', 
            label_de='Baulich Allgemein biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_general = VariableMeta(
            var_name='GWP_life_general', 
            attr_name='GWP_life_general', 
            icon='☁', 
            label_de='Baulich Allgemein Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_general_fossile = VariableMeta(
            var_name='GWP_ee_lc_general_fossile', 
            attr_name='GWP_ee_lc_general_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_general_biogenic = VariableMeta(
            var_name='GWP_ee_lc_general_biogenic', 
            attr_name='GWP_ee_lc_general_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_general = VariableMeta(
            var_name='GWP_ee_general', 
            attr_name='GWP_ee_general', 
            icon='☁', 
            label_de='Baulich Allgemein', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_other_fossile = VariableMeta(
            var_name='GWP_ee_other_fossile', 
            attr_name='GWP_ee_other_fossile', 
            icon='☁', 
            label_de='Baulich Andere fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_other_biogenic = VariableMeta(
            var_name='GWP_ee_other_biogenic', 
            attr_name='GWP_ee_other_biogenic', 
            icon='☁', 
            label_de='Baulich Andere biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_other = VariableMeta(
            var_name='GWP_life_other', 
            attr_name='GWP_life_other', 
            icon='☁', 
            label_de='Baulich Andere Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_other_fossile = VariableMeta(
            var_name='GWP_ee_lc_other_fossile', 
            attr_name='GWP_ee_lc_other_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_other_biogenic = VariableMeta(
            var_name='GWP_ee_lc_other_biogenic', 
            attr_name='GWP_ee_lc_other_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_other = VariableMeta(
            var_name='GWP_ee_lc_other', 
            attr_name='GWP_ee_lc_other', 
            icon='☁', 
            label_de='Baulich Sammel-Maßnahmen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_direct_fossile = VariableMeta(
            var_name='GWP_ee_direct_fossile', 
            attr_name='GWP_ee_direct_fossile', 
            icon='☁', 
            label_de='Baulich Direkteingabe fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_direct_biogenic = VariableMeta(
            var_name='GWP_ee_direct_biogenic', 
            attr_name='GWP_ee_direct_biogenic', 
            icon='☁', 
            label_de='Baulich Direkteingabe biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_direct = VariableMeta(
            var_name='GWP_life_direct', 
            attr_name='GWP_life_direct', 
            icon='☁', 
            label_de='Baulich \nDirekteingabe Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_direct_fossile = VariableMeta(
            var_name='GWP_ee_lc_direct_fossile', 
            attr_name='GWP_ee_lc_direct_fossile', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_direct_biogenic = VariableMeta(
            var_name='GWP_ee_lc_direct_biogenic', 
            attr_name='GWP_ee_lc_direct_biogenic', 
            icon=None, 
            label_de=None, 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_direct = VariableMeta(
            var_name='GWP_ee_lc_direct', 
            attr_name='GWP_ee_lc_direct', 
            icon='☁', 
            label_de='Baulich Direkteingabe', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_con_build = VariableMeta(
            var_name='GWP_ee_con_build', 
            attr_name='GWP_ee_con_build', 
            icon='☁', 
            label_de='Baulich Errichtung', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_rep_build = VariableMeta(
            var_name='GWP_ee_rep_build', 
            attr_name='GWP_ee_rep_build', 
            icon='☁', 
            label_de='Baulich Instandsetzung', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_fossil = VariableMeta(
            var_name='GWP_ee_lc_fossil', 
            attr_name='GWP_ee_lc_fossil', 
            icon=None, 
            label_de='Baulich Fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_biogenic = VariableMeta(
            var_name='GWP_ee_lc_biogenic', 
            attr_name='GWP_ee_lc_biogenic', 
            icon=None, 
            label_de='Baulich Biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_construction = VariableMeta(
            var_name='GWP_ee_lc_construction', 
            attr_name='GWP_ee_lc_construction', 
            icon='☁', 
            label_de='Baulich', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_pv_fossile = VariableMeta(
            var_name='GWP_ee_tga_pv_fossile', 
            attr_name='GWP_ee_tga_pv_fossile', 
            icon='☁', 
            label_de='TGA PV fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_pv_biogenic = VariableMeta(
            var_name='GWP_ee_tga_pv_biogenic', 
            attr_name='GWP_ee_tga_pv_biogenic', 
            icon=None, 
            label_de='TGA PV biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_tga_pv = VariableMeta(
            var_name='GWP_life_tga_pv', 
            attr_name='GWP_life_tga_pv', 
            icon=None, 
            label_de='TGA PV Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_pv = VariableMeta(
            var_name='GWP_ee_lc_pv', 
            attr_name='GWP_ee_lc_pv', 
            icon='☁', 
            label_de='TGA PV', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_boreholes_fossile = VariableMeta(
            var_name='GWP_ee_tga_boreholes_fossile', 
            attr_name='GWP_ee_tga_boreholes_fossile', 
            icon='☁', 
            label_de='TGA Erdsonden fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_boreholes_biogenic = VariableMeta(
            var_name='GWP_ee_tga_boreholes_biogenic', 
            attr_name='GWP_ee_tga_boreholes_biogenic', 
            icon=None, 
            label_de='TGA Erdsonden biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_tga_boreholes = VariableMeta(
            var_name='GWP_life_tga_boreholes', 
            attr_name='GWP_life_tga_boreholes', 
            icon=None, 
            label_de='TGA Erdsonden Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_boreholes = VariableMeta(
            var_name='GWP_ee_lc_boreholes', 
            attr_name='GWP_ee_lc_boreholes', 
            icon='☁', 
            label_de='TGA Erdsonden', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_ventilation_fossile = VariableMeta(
            var_name='GWP_ee_tga_ventilation_fossile', 
            attr_name='GWP_ee_tga_ventilation_fossile', 
            icon='☁', 
            label_de='TGA Lüftung fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_ventilation_biogenic = VariableMeta(
            var_name='GWP_ee_tga_ventilation_biogenic', 
            attr_name='GWP_ee_tga_ventilation_biogenic', 
            icon=None, 
            label_de='TGA Lüftung biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_tga_ventilation = VariableMeta(
            var_name='GWP_life_tga_ventilation', 
            attr_name='GWP_life_tga_ventilation', 
            icon=None, 
            label_de='TGA Lüftung Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_ventilation = VariableMeta(
            var_name='GWP_ee_lc_ventilation', 
            attr_name='GWP_ee_lc_ventilation', 
            icon='☁', 
            label_de='TGA Lüftung', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_solarthermal_fossile = VariableMeta(
            var_name='GWP_ee_tga_solarthermal_fossile', 
            attr_name='GWP_ee_tga_solarthermal_fossile', 
            icon='☁', 
            label_de='TGA Solarthermie fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_solarthermal_biogenic = VariableMeta(
            var_name='GWP_ee_tga_solarthermal_biogenic', 
            attr_name='GWP_ee_tga_solarthermal_biogenic', 
            icon=None, 
            label_de='TGA Solarthermie biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_solarthermal = VariableMeta(
            var_name='GWP_life_solarthermal', 
            attr_name='GWP_life_solarthermal', 
            icon=None, 
            label_de='TGA Solarthermie Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_solarthermal = VariableMeta(
            var_name='GWP_ee_lc_solarthermal', 
            attr_name='GWP_ee_lc_solarthermal', 
            icon='☁', 
            label_de='TGA Solarthermie', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_battery_fossile = VariableMeta(
            var_name='GWP_ee_tga_battery_fossile', 
            attr_name='GWP_ee_tga_battery_fossile', 
            icon='☁', 
            label_de='TGA E-Batterie fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_battery_biogenic = VariableMeta(
            var_name='GWP_ee_tga_battery_biogenic', 
            attr_name='GWP_ee_tga_battery_biogenic', 
            icon=None, 
            label_de='TGA E-Batterie biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_battery = VariableMeta(
            var_name='GWP_life_battery', 
            attr_name='GWP_life_battery', 
            icon=None, 
            label_de='TGA E-Batterie Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_battery = VariableMeta(
            var_name='GWP_ee_lc_battery', 
            attr_name='GWP_ee_lc_battery', 
            icon='☁', 
            label_de='TGA E-Batterie', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_storage_fossile = VariableMeta(
            var_name='GWP_ee_tga_storage_fossile', 
            attr_name='GWP_ee_tga_storage_fossile', 
            icon=None, 
            label_de='TGA Speicher fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_storage_biogenic = VariableMeta(
            var_name='GWP_ee_tga_storage_biogenic', 
            attr_name='GWP_ee_tga_storage_biogenic', 
            icon=None, 
            label_de='TGA Speicher biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_storage = VariableMeta(
            var_name='GWP_life_storage', 
            attr_name='GWP_life_storage', 
            icon=None, 
            label_de='TGA Speicher Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_storage = VariableMeta(
            var_name='GWP_ee_lc_storage', 
            attr_name='GWP_ee_lc_storage', 
            icon=None, 
            label_de='TGA Speicher', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_general_fossile = VariableMeta(
            var_name='GWP_ee_tga_general_fossile', 
            attr_name='GWP_ee_tga_general_fossile', 
            icon=None, 
            label_de='TGA Allgemein fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_general_biogenic = VariableMeta(
            var_name='GWP_ee_tga_general_biogenic', 
            attr_name='GWP_ee_tga_general_biogenic', 
            icon=None, 
            label_de='TGA Allgemein biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_tga_general = VariableMeta(
            var_name='GWP_life_tga_general', 
            attr_name='GWP_life_tga_general', 
            icon=None, 
            label_de='TGA Allgemein Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_tga_general = VariableMeta(
            var_name='GWP_ee_lc_tga_general', 
            attr_name='GWP_ee_lc_tga_general', 
            icon=None, 
            label_de='TGA Allgemein', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_other_fossile = VariableMeta(
            var_name='GWP_ee_tga_other_fossile', 
            attr_name='GWP_ee_tga_other_fossile', 
            icon=None, 
            label_de='TGA Andere fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_tga_other_biogenic = VariableMeta(
            var_name='GWP_ee_tga_other_biogenic', 
            attr_name='GWP_ee_tga_other_biogenic', 
            icon=None, 
            label_de='TGA Andere biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_life_tga_other = VariableMeta(
            var_name='GWP_life_tga_other', 
            attr_name='GWP_life_tga_other', 
            icon=None, 
            label_de='TGA Andere Lebensdauer', 
            unit='Jahre', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_tga_other = VariableMeta(
            var_name='GWP_ee_lc_tga_other', 
            attr_name='GWP_ee_lc_tga_other', 
            icon=None, 
            label_de='TGA Sammel-Maßnahmen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_con_tga = VariableMeta(
            var_name='GWP_ee_con_tga', 
            attr_name='GWP_ee_con_tga', 
            icon='☁', 
            label_de='Errichtung TGA', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_rep_tga = VariableMeta(
            var_name='GWP_ee_rep_tga', 
            attr_name='GWP_ee_rep_tga', 
            icon='☁', 
            label_de='Instandsetzung TGA', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_tga = VariableMeta(
            var_name='GWP_ee_lc_tga', 
            attr_name='GWP_ee_lc_tga', 
            icon='☁', 
            label_de='TGA', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_mob_fossile = VariableMeta(
            var_name='GWP_ee_mob_fossile', 
            attr_name='GWP_ee_mob_fossile', 
            icon='☁', 
            label_de='Errichtung Mobilität fossil', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_mob_ev = VariableMeta(
            var_name='GWP_ee_mob_ev', 
            attr_name='GWP_ee_mob_ev', 
            icon='☁', 
            label_de='Errichtung Mobilität Elektrisch', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_ee_lc_mob = VariableMeta(
            var_name='GWP_ee_lc_mob', 
            attr_name='GWP_ee_lc_mob', 
            icon='☁', 
            label_de='Errichtung Mobilität', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Graue Emissionen', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_battery_charge = VariableMeta(
            var_name='GWP_oe_battery_charge', 
            attr_name='GWP_oe_battery_charge', 
            icon='☁', 
            label_de='Betrieb Batterie Beladung', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_emInt_grid_avg = VariableMeta(
            var_name='GWP_emInt_grid_avg', 
            attr_name='GWP_emInt_grid_avg', 
            icon='☁', 
            label_de='Emissions-Intensität Netzstrom allgemein', 
            unit='gCO2eq/kWh', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_emInt_grid = VariableMeta(
            var_name='GWP_emInt_grid', 
            attr_name='GWP_emInt_grid', 
            icon='☁', 
            label_de='Emissions-Intensität Netzstrombezug', 
            unit='gCO2eq/kWh', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_emInt_flex = VariableMeta(
            var_name='GWP_emInt_flex', 
            attr_name='GWP_emInt_flex', 
            icon='☁', 
            label_de='Emissions-Intensität Flexibler Netzbezug', 
            unit='gCO2eq/kWh', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_emInt_batt_charge = VariableMeta(
            var_name='GWP_emInt_batt_charge', 
            attr_name='GWP_emInt_batt_charge', 
            icon='☁', 
            label_de='Emissions-Intensität Batterie Beladung', 
            unit='gCO2eq/kWh', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_emInt_ev_charge = VariableMeta(
            var_name='GWP_emInt_ev_charge', 
            attr_name='GWP_emInt_ev_charge', 
            icon=None, 
            label_de='Emissions-Intensität EV ladung', 
            unit='gCO2eq/kWh', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_emInt_PV_feedin = VariableMeta(
            var_name='GWP_emInt_PV_feedin', 
            attr_name='GWP_emInt_PV_feedin', 
            icon='☁', 
            label_de='Emissions-Intensität Netzeinspeisung', 
            unit='gCO2eq/kWh', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_grid_build = VariableMeta(
            var_name='GWP_oe_grid_build', 
            attr_name='GWP_oe_grid_build', 
            icon='☁', 
            label_de='Betrieb Gebäude Netzstrombezug', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_flex_build = VariableMeta(
            var_name='GWP_oe_flex_build', 
            attr_name='GWP_oe_flex_build', 
            icon='☁', 
            label_de='Betrieb Gebäude Flexibler Netzbezug', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_district_heating = VariableMeta(
            var_name='GWP_oe_district_heating', 
            attr_name='GWP_oe_district_heating', 
            icon='☁', 
            label_de='Betrieb HKLS Fernwärme', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_natural_gas = VariableMeta(
            var_name='GWP_oe_natural_gas', 
            attr_name='GWP_oe_natural_gas', 
            icon='☁', 
            label_de='Betrieb HKLS Erdgas', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_biomass = VariableMeta(
            var_name='GWP_oe_biomass', 
            attr_name='GWP_oe_biomass', 
            icon='☁', 
            label_de='Betrieb HKLS Biomasse', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_other = VariableMeta(
            var_name='GWP_oe_other', 
            attr_name='GWP_oe_other', 
            icon='☁', 
            label_de='Betrieb HKLS Sonstige', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_grid_feedin = VariableMeta(
            var_name='GWP_oe_grid_feedin', 
            attr_name='GWP_oe_grid_feedin', 
            icon='☁', 
            label_de='Betrieb Netzeinspeisung', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_building = VariableMeta(
            var_name='GWP_oe_building', 
            attr_name='GWP_oe_building', 
            icon='☁', 
            label_de='Betrieb Gebäude', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_mob_ev = VariableMeta(
            var_name='GWP_oe_mob_ev', 
            attr_name='GWP_oe_mob_ev', 
            icon='☁', 
            label_de='GWP MIV elektrisch INSGESAMTE LADUNG', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_mob_ev_export = VariableMeta(
            var_name='GWP_oe_mob_ev_export', 
            attr_name='GWP_oe_mob_ev_export', 
            icon='☁', 
            label_de='GWP MIV Export (Anderer Verkehr)', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-ImportExport Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_mob_fossile = VariableMeta(
            var_name='GWP_oe_mob_fossile', 
            attr_name='GWP_oe_mob_fossile', 
            icon='☁', 
            label_de='GWP MIV fossil', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_mob = VariableMeta(
            var_name='GWP_oe_mob', 
            attr_name='GWP_oe_mob', 
            icon='☁', 
            label_de='Mobilität (Ursächlich)', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb', 
            temporal_scope='pro Jahr', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe = VariableMeta(
            var_name='GWP_oe', 
            attr_name='GWP_oe', 
            icon=None, 
            label_de='GWP Quartier (Gebäude+MIV)', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_grid_build = VariableMeta(
            var_name='GWP_oe_lc_grid_build', 
            attr_name='GWP_oe_lc_grid_build', 
            icon='☁', 
            label_de='LZ Betrieb Gebäude Netzstrombezug', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_flex_build = VariableMeta(
            var_name='GWP_oe_lc_flex_build', 
            attr_name='GWP_oe_lc_flex_build', 
            icon='☁', 
            label_de='LZ Betrieb Gebäude Flexibler Netzbezug', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_district_heating = VariableMeta(
            var_name='GWP_oe_lc_district_heating', 
            attr_name='GWP_oe_lc_district_heating', 
            icon='☁', 
            label_de='LZ Betrieb HKLS Fernwärme', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_natural_gas = VariableMeta(
            var_name='GWP_oe_lc_natural_gas', 
            attr_name='GWP_oe_lc_natural_gas', 
            icon='☁', 
            label_de='LZ Betrieb HKLS Erdgas', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_biomass = VariableMeta(
            var_name='GWP_oe_lc_biomass', 
            attr_name='GWP_oe_lc_biomass', 
            icon='☁', 
            label_de='LZ Betrieb HKLS Biomasse', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_other = VariableMeta(
            var_name='GWP_oe_lc_other', 
            attr_name='GWP_oe_lc_other', 
            icon='☁', 
            label_de='LZ Betrieb HKLS Sonstige', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_grid_feedin = VariableMeta(
            var_name='GWP_oe_lc_grid_feedin', 
            attr_name='GWP_oe_lc_grid_feedin', 
            icon='☁', 
            label_de='LZ Betrieb Netzeinspeisung', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_building = VariableMeta(
            var_name='GWP_oe_lc_building', 
            attr_name='GWP_oe_lc_building', 
            icon='☁', 
            label_de='LZ Betrieb Gebäude', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_emission = VariableMeta(
            var_name='GWP_oe_lc_emission', 
            attr_name='GWP_oe_lc_emission', 
            icon=None, 
            label_de='LZ Betrieb Gebäude Emissionen', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_emission_savings = VariableMeta(
            var_name='GWP_oe_lc_emission_savings', 
            attr_name='GWP_oe_lc_emission_savings', 
            icon=None, 
            label_de='LZ Betrieb Gebäude Vermiedene Emissionen', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure=None, 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_mob_ev = VariableMeta(
            var_name='GWP_oe_lc_mob_ev', 
            attr_name='GWP_oe_lc_mob_ev', 
            icon='☁', 
            label_de='LCA OE MIV elektrisch', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_mob_export = VariableMeta(
            var_name='GWP_oe_lc_mob_export', 
            attr_name='GWP_oe_lc_mob_export', 
            icon='☁', 
            label_de='LV Mobilitäts-Export', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2075', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_mob_fossile = VariableMeta(
            var_name='GWP_oe_lc_mob_fossile', 
            attr_name='GWP_oe_lc_mob_fossile', 
            icon='☁', 
            label_de='LCA OE MIV fossil', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_oe_lc_mob = VariableMeta(
            var_name='GWP_oe_lc_mob', 
            attr_name='GWP_oe_lc_mob', 
            icon='☁', 
            label_de='Mobilität', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_lc_total = VariableMeta(
            var_name='GWP_lc_total', 
            attr_name='GWP_lc_total', 
            icon='☁', 
            label_de='THG-Emissionen 2025-2075', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_lc_OE_total = VariableMeta(
            var_name='GWP_lc_OE_total', 
            attr_name='GWP_lc_OE_total', 
            icon='☁', 
            label_de='OE THG-Emissionen 2025-2075', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.GWP_lc_EE_total = VariableMeta(
            var_name='GWP_lc_EE_total', 
            attr_name='GWP_lc_EE_total', 
            icon='☁', 
            label_de='EE THG-Emissionen 2025-2075', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='THG-Bilanz', 
            spatial_scope='Betrieb 2025-2075', 
            temporal_scope='2025-2050', 
            entity_group=None, 
            entity_key=None
        )
        self.cost_E_grid = VariableMeta(
            var_name='cost_E_grid', 
            attr_name='cost_E_grid', 
            icon='💸', 
            label_de='Kosten Netzbezug', 
            unit='€', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Stromkosten', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cost_VRGrid_flex = VariableMeta(
            var_name='cost_VRGrid_flex', 
            attr_name='cost_VRGrid_flex', 
            icon='💸', 
            label_de='Kosten Flexibler Bezug', 
            unit='€', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Stromkosten', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cost_PV_to_Egrid = VariableMeta(
            var_name='cost_PV_to_Egrid', 
            attr_name='cost_PV_to_Egrid', 
            icon='💸', 
            label_de='Kosten Netzeinspeisung', 
            unit='€', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Stromkosten', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.cost_total = VariableMeta(
            var_name='cost_total', 
            attr_name='cost_total', 
            icon='💸', 
            label_de='Summe Kosten', 
            unit='€', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Stromkosten', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_signal_ratio = VariableMeta(
            var_name='flex_signal_ratio', 
            attr_name='flex_signal_ratio', 
            icon=None, 
            label_de='Freigabesignal Anteil Jahr', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Netzdienlichkeit der Energieflexibilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_signal_ratio_winter = VariableMeta(
            var_name='flex_signal_ratio_winter', 
            attr_name='flex_signal_ratio_winter', 
            icon=None, 
            label_de='Freigabesignal Anteil  Winter', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Netzdienlichkeit der Energieflexibilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_signal_ratio_summer = VariableMeta(
            var_name='flex_signal_ratio_summer', 
            attr_name='flex_signal_ratio_summer', 
            icon=None, 
            label_de='Freigabesignal Anteil  Sommer', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Netzdienlichkeit der Energieflexibilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_GSRU = VariableMeta(
            var_name='flex_GSRU', 
            attr_name='flex_GSRU', 
            icon='"', 
            label_de='Flex GSRU', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Netzdienlichkeit der Energieflexibilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_GSRI = VariableMeta(
            var_name='flex_GSRI', 
            attr_name='flex_GSRI', 
            icon=None, 
            label_de='Flex GSRI', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Netzdienlichkeit der Energieflexibilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.flex_GSR = VariableMeta(
            var_name='flex_GSR', 
            attr_name='flex_GSR', 
            icon=None, 
            label_de='Flex GSR', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Netzdienlichkeit der Energieflexibilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_own_consumption_direct = VariableMeta(
            var_name='PV_own_consumption_direct', 
            attr_name='PV_own_consumption_direct', 
            icon=None, 
            label_de='PV Eigenverbrauch direkt', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='PV', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_own_consumption_flex = VariableMeta(
            var_name='PV_own_consumption_flex', 
            attr_name='PV_own_consumption_flex', 
            icon=None, 
            label_de='PV Eigenverbrauch flex', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='PV', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.PV_own_consumption = VariableMeta(
            var_name='PV_own_consumption', 
            attr_name='PV_own_consumption', 
            icon='S', 
            label_de='PV Eigenverbrauch insgesamt', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='PV', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_self_sufficiency = VariableMeta(
            var_name='EUI_self_sufficiency', 
            attr_name='EUI_self_sufficiency', 
            icon=None, 
            label_de='Energie-Autonomie', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='PV', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_total_charge = VariableMeta(
            var_name='Batt_total_charge', 
            attr_name='Batt_total_charge', 
            icon='🔋', 
            label_de='Batterie Jährliche Beladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Batterienutzung', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_total_discharge = VariableMeta(
            var_name='Batt_total_discharge', 
            attr_name='Batt_total_discharge', 
            icon='🔋', 
            label_de='Jährliche Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Batterienutzung', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_charge_losses = VariableMeta(
            var_name='Batt_charge_losses', 
            attr_name='Batt_charge_losses', 
            icon='🔋', 
            label_de='Verluste Beladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Batterienutzung', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_discharge_losses = VariableMeta(
            var_name='Batt_discharge_losses', 
            attr_name='Batt_discharge_losses', 
            icon='🔋', 
            label_de='Verluste Entladung', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Batterienutzung', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_RTE = VariableMeta(
            var_name='Batt_RTE', 
            attr_name='Batt_RTE', 
            icon='🔋', 
            label_de='Round-Trip- Efficiency', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Batterienutzung', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Batt_FEC = VariableMeta(
            var_name='Batt_FEC', 
            attr_name='Batt_FEC', 
            icon='🔋', 
            label_de='Batterie Volladezyklen', 
            unit='x', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Batterienutzung', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.StatPAX = VariableMeta(
            var_name='StatPAX', 
            attr_name='StatPAX', 
            icon=None, 
            label_de='Quartier', 
            unit='StatPAX', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='StatPAX', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mob_annual_milage_district = VariableMeta(
            var_name='mob_annual_milage_district', 
            attr_name='mob_annual_milage_district', 
            icon=None, 
            label_de='Gesamtverkehr', 
            unit='km/a', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='Jkm', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.mob_annual_mileage_PAX = VariableMeta(
            var_name='mob_annual_mileage_PAX', 
            attr_name='mob_annual_mileage_PAX', 
            icon=None, 
            label_de='Gesamtverkehr pro STATPAX', 
            unit='km/PAX/a', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='JPkm', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.UED_mob_el_target = VariableMeta(
            var_name='UED_mob_el_target', 
            attr_name='UED_mob_el_target', 
            icon=None, 
            label_de='EE-Bedarf Zielverkehr Elektrisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='Statistisch', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUI_mob_fossile = VariableMeta(
            var_name='EUI_mob_fossile', 
            attr_name='EUI_mob_fossile', 
            icon=None, 
            label_de='EE-Bedarf Zielverkehr Fossil', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='Statistisch', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EV_FEC = VariableMeta(
            var_name='EV_FEC', 
            attr_name='EV_FEC', 
            icon=None, 
            label_de='EV Volladezyklen', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='Real', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.UED_mob_el_total = VariableMeta(
            var_name='UED_mob_el_total', 
            attr_name='UED_mob_el_total', 
            icon=None, 
            label_de='Gesamtverkehr elektrisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='Real', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.UED_mob_el_other = VariableMeta(
            var_name='UED_mob_el_other', 
            attr_name='UED_mob_el_other', 
            icon=None, 
            label_de='Quell- und anderer Verkehr elektrisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope='Real', 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.EUIev_el_total = VariableMeta(
            var_name='EUIev_el_total', 
            attr_name='EUIev_el_total', 
            icon=None, 
            label_de='EV Jährliche Beladung', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Mobilität', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_th = VariableMeta(
            var_name='Edhw_th', 
            attr_name='Edhw_th', 
            icon=None, 
            label_de='WW Endenergiebedarf Thermisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_el = VariableMeta(
            var_name='Edhw_el', 
            attr_name='Edhw_el', 
            icon=None, 
            label_de='WW Endenergiebedarf Elektrisch (inkl. Hilfsstrom)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_aux_el = VariableMeta(
            var_name='Edhw_aux_el', 
            attr_name='Edhw_aux_el', 
            icon=None, 
            label_de='WW Hilfsstrom', 
            unit=None, 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_1_th = VariableMeta(
            var_name='Edhw_1_th', 
            attr_name='Edhw_1_th', 
            icon=None, 
            label_de='WW 1 Endenergie thermisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_1_el = VariableMeta(
            var_name='Edhw_1_el', 
            attr_name='Edhw_1_el', 
            icon=None, 
            label_de='WW 1 Endenergie elektrisch (inkl. Hilfsstrom)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_1_aux_el = VariableMeta(
            var_name='Edhw_1_aux_el', 
            attr_name='Edhw_1_aux_el', 
            icon=None, 
            label_de='WW 1 Hilfsstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_2_th = VariableMeta(
            var_name='Edhw_2_th', 
            attr_name='Edhw_2_th', 
            icon=None, 
            label_de='WW 2 Endenergie thermisch', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_2_el = VariableMeta(
            var_name='Edhw_2_el', 
            attr_name='Edhw_2_el', 
            icon=None, 
            label_de='WW 2 Endenergie elektrisch (inkl.Hilfsstrom)', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )
        self.Edhw_2_aux_el = VariableMeta(
            var_name='Edhw_2_aux_el', 
            attr_name='Edhw_2_aux_el', 
            icon=None, 
            label_de='WW 2 Hilfsstrom', 
            unit='kWh/m²NGFa', 
            comment=None, 
            source='OUT', 
            ka=3, 
            domain=None, 
            measure='Warmwasser', 
            spatial_scope=None, 
            temporal_scope=None, 
            entity_group=None, 
            entity_key=None
        )

SCHEMA_META = Meta()

ATTR_NAME_MAP: dict[str, str] = {
    'scenario_version': 'scenario_version',
    'input_version_number': 'input_version_number',
    'input_version_date': 'input_version_date',
    'cfd_fPE': 'cfd_fPE',
    'cfd_A': 'cfd_A',
    'cfd_dx': 'cfd_dx',
    'cfd_EUI': 'cfd_EUI',
    'cfd_cutoff': 'cfd_cutoff',
    'cfm_budget_residential': 'cfm_budget_residential',
    'cfm_budget_office': 'cfm_budget_office',
    'cfm_budget_school': 'cfm_budget_school',
    'cfm_budget_retail': 'cfm_budget_retail',
    'cfr_budget': 'cfr_budget',
    'project_name': 'project_name',
    'project_url': 'project_url',
    'location_address': 'location_address',
    'municipality_name': 'municipality_name',
    'project_creation_date': 'project_creation_date',
    'project_description': 'project_description',
    'project_scenario_name': 'project_scenario_name',
    'location_postcode': 'location_postcode',
    'mobility_mode': 'mobility_mode',
    'weather_name': 'weather_name',
    'weather_index': 'weather_index',
    'GFA_residential': 'GFA_residential',
    'GFA_office': 'GFA_office',
    'GFA_schoolsec': 'GFA_schoolsec',
    'GFA_schoolprim': 'GFA_schoolprim',
    'GFA_retailfood': 'GFA_retailfood',
    'GFA_retailother': 'GFA_retailother',
    'GFA_other': 'GFA_other',
    'GFA_total': 'GFA_total',
    'NFA_to_GFA_ratio_residential': 'NFA_to_GFA_ratio_residential',
    'NFA_to_GFA_ratio_office': 'NFA_to_GFA_ratio_office',
    'NFA_to_GFA_ratio_schoolsec': 'NFA_to_GFA_ratio_schoolsec',
    'NFA_to_GFA_ratio_schoolprim': 'NFA_to_GFA_ratio_schoolprim',
    'NFA_to_GFA_ratio_retailfood': 'NFA_to_GFA_ratio_retailfood',
    'NFA_to_GFA_ratio_retailother': 'NFA_to_GFA_ratio_retailother',
    'NFA_to_GFA_ratio_other': 'NFA_to_GFA_ratio_other',
    'NFA_to_GFA_ratio': 'NFA_to_GFA_ratio',
    'NFA_residential': 'NFA_residential',
    'NFA_office': 'NFA_office',
    'NFA_schoolsec': 'NFA_schoolsec',
    'NFA_schoolprim': 'NFA_schoolprim',
    'NFA_retailfood': 'NFA_retailfood',
    'NFA_retailother': 'NFA_retailother',
    'NFA_other': 'NFA_other',
    'NFA_total': 'NFA_total',
    'per_NFA': 'per_NFA',
    'plot_area': 'plot_area',
    'FSI': 'FSI',
    'renovation_ratio_residential': 'renovation_ratio_residential',
    'renovation_ratio_office': 'renovation_ratio_office',
    'renovation_ratio_schoolsec': 'renovation_ratio_schoolsec',
    'renovation_ratio_schoolprim': 'renovation_ratio_schoolprim',
    'renovation_ratio_retailfood': 'renovation_ratio_retailfood',
    'renovation_ratio_retailother': 'renovation_ratio_retailother',
    'renovation_ratio_other': 'renovation_ratio_other',
    'renovation_share': 'renovation_share',
    'building_count': 'building_count',
    'storey_count_avg': 'storey_count_avg',
    'rh_residential': 'rh_residential',
    'rh_office': 'rh_office',
    'rh_schoolsec': 'rh_schoolsec',
    'rh_schoolprim': 'rh_schoolprim',
    'rh_retailfood': 'rh_retailfood',
    'rh_retailother': 'rh_retailother',
    'rh_other': 'rh_other',
    'rh_avg': 'rh_avg',
    'NFV_total': 'NFV_total',
    'NFV_u': 'NFV_u',
    'NFV_c': 'NFV_c',
    'rh_ceiling': 'rh_ceiling',
    'GFV': 'GFV',
    'hull_ext_wall_wo_window_m2': 'hull_ext_wall_wo_window_m2',
    'hull_roof_m2': 'hull_roof_m2',
    'hull_fundament_m2': 'hull_fundament_m2',
    'hull_windows_north_m2': 'hull_windows_north_m2',
    'hull_windows_east_m2': 'hull_windows_east_m2',
    'hull_windows_south_m2': 'hull_windows_south_m2',
    'hull_windows_west_m2': 'hull_windows_west_m2',
    'hull_windows_horizontal_m2': 'hull_windows_horizontal_m2',
    'hull_window_m2': 'hull_window_m2',
    'hull_fenestration_rate': 'hull_fenestration_rate',
    'hull_m2': 'hull_m2',
    'lc': 'lc',
    'hull_transmittance_walls': 'hull_transmittance_walls',
    'hull_transmittance_roof': 'hull_transmittance_roof',
    'hull_transmittance_fundament': 'hull_transmittance_fundament',
    'hull_transmittance_windows_north': 'hull_transmittance_windows_north',
    'hull_transmittance_windows_east': 'hull_transmittance_windows_east',
    'hull_transmittance_windows_south': 'hull_transmittance_windows_south',
    'hull_transmittance_windows_west': 'hull_transmittance_windows_west',
    'hull_transmittance_windows_horizontal': 'hull_transmittance_windows_horizontal',
    'hull_transmittance_heatbridge': 'hull_transmittance_heatbridge',
    'transmittance_walls_Wm2NFA': 'transmittance_walls_Wm2NFA',
    'transmittance_roof_Wm2NFA': 'transmittance_roof_Wm2NFA',
    'transmittance_fundament_Wm2NFA': 'transmittance_fundament_Wm2NFA',
    'transmittance_windows_Wm2NFA': 'transmittance_windows_Wm2NFA',
    'transmittance_heatbridge_Wm2NFA': 'transmittance_heatbridge_Wm2NFA',
    'transmittance_MW': 'transmittance_MW',
    'transmittance_Wm2': 'transmittance_Wm2',
    'heat_capacity_effective_m²': 'heat_capacity_effective_m',
    'heat_cap_eff_uncooled_m2': 'heat_cap_eff_uncooled_m2',
    'heat_cap_eff_cooled_m2': 'heat_cap_eff_cooled_m2',
    'window_total_transmittance_north': 'window_total_transmittance_north',
    'window_total_transmittance_east': 'window_total_transmittance_east',
    'window_total_transmittance_south': 'window_total_transmittance_south',
    'window_total_transmittance_west': 'window_total_transmittance_west',
    'window_total_transmittance_horizontal': 'window_total_transmittance_horizontal',
    'window_irradiation_factor_winter_north': 'window_irradiation_factor_winter_north',
    'window_irradiation_factor_winter_east': 'window_irradiation_factor_winter_east',
    'window_irradiation_factor_winter_south': 'window_irradiation_factor_winter_south',
    'window_irradiation_factor_winter_west': 'window_irradiation_factor_winter_west',
    'window_irradiation_factor_winter_horizontal': 'window_irradiation_factor_winter_horizontal',
    'window_irradiation_factor_summer_north': 'window_irradiation_factor_summer_north',
    'window_irradiation_factor_summer_east': 'window_irradiation_factor_summer_east',
    'window_irradiation_factor_summer_south': 'window_irradiation_factor_summer_south',
    'window_irradiation_factor_summer_west': 'window_irradiation_factor_summer_west',
    'window_irradiation_factor_summer_horizontal': 'window_irradiation_factor_summer_horizontal',
    'irradiation_opaque_surcharge': 'irradiation_opaque_surcharge',
    'fc_residential': 'fc_residential',
    'fc_office': 'fc_office',
    'fc_schoolsec': 'fc_schoolsec',
    'fc_schoolprim': 'fc_schoolprim',
    'fc_retailfood': 'fc_retailfood',
    'fc_retailother': 'fc_retailother',
    'fc_other': 'fc_other',
    'fc_u': 'fc_u',
    'fc_c': 'fc_c',
    'illuminance_min_residential': 'illuminance_min_residential',
    'illuminance_min_office': 'illuminance_min_office',
    'illuminance_min_schoolsec': 'illuminance_min_schoolsec',
    'illuminance_min_schoolprim': 'illuminance_min_schoolprim',
    'illuminance_min_retailfood': 'illuminance_min_retailfood',
    'illuminance_min_retailother': 'illuminance_min_retailother',
    'illuminance_min_other': 'illuminance_min_other',
    'QS_max_shading_u': 'QS_max_shading_u',
    'QS_max_shading_c': 'QS_max_shading_c',
    'illuminance_efficiency_dirt': 'illuminance_efficiency_dirt',
    'illuminance_efficiency_glazing_ratio': 'illuminance_efficiency_glazing_ratio',
    'mob_shading_factor_u': 'mob_shading_factor_u',
    'mob_shading_factor_c': 'mob_shading_factor_c',
    'vent_air_tightness': 'vent_air_tightness',
    'vent_tightness_ratio_blowerdoor_to_real': 'vent_tightness_ratio_blowerdoor_to_real',
    'vent_infiltration_ACH': 'vent_infiltration_ACH',
    'vent_share_mechanical_residential': 'vent_share_mechanical_residential',
    'vent_share_mechanical_office': 'vent_share_mechanical_office',
    'vent_share_mechanical_schoolsec': 'vent_share_mechanical_schoolsec',
    'vent_share_mechanical_schoolprim': 'vent_share_mechanical_schoolprim',
    'vent_share_mechanical_retailfood': 'vent_share_mechanical_retailfood',
    'vent_share_mechanical_retailother': 'vent_share_mechanical_retailother',
    'vent_share_mechanical_other': 'vent_share_mechanical_other',
    'NFA_windowvent': 'NFA_windowvent',
    'NFV_windowvent': 'NFV_windowvent',
    'NFA_mechvent': 'NFA_mechvent',
    'NFV_mechvent': 'NFV_mechvent',
    'vent_night_residential': 'vent_night_residential',
    'vent_night_office': 'vent_night_office',
    'vent_night_schoolsec': 'vent_night_schoolsec',
    'vent_night_schoolprim': 'vent_night_schoolprim',
    'vent_night_retailfood': 'vent_night_retailfood',
    'vent_night_retailother': 'vent_night_retailother',
    'vent_night_other': 'vent_night_other',
    'ACH_night_m³': 'ACH_night_m',
    'vent_ach_max_residential': 'vent_ach_max_residential',
    'vent_ach_max_office': 'vent_ach_max_office',
    'vent_ach_max_schoolsec': 'vent_ach_max_schoolsec',
    'vent_ach_max_schoolprim': 'vent_ach_max_schoolprim',
    'vent_ach_max_retailfood': 'vent_ach_max_retailfood',
    'vent_ach_max_retailother': 'vent_ach_max_retailother',
    'vent_ach_max_other': 'vent_ach_max_other',
    'vent_scale_residential': 'vent_scale_residential',
    'vent_scale_office': 'vent_scale_office',
    'vent_scale_school_sec': 'vent_scale_school_sec',
    'vent_scale_school_prim': 'vent_scale_school_prim',
    'vent_scale_supermarket': 'vent_scale_supermarket',
    'vent_scale_retail': 'vent_scale_retail',
    'vent_scale_other': 'vent_scale_other',
    'Ev_scale_residential': 'Ev_scale_residential',
    'Ev_scale_office': 'Ev_scale_office',
    'Ev_scale_school_sec': 'Ev_scale_school_sec',
    'Ev_scale_school_prim': 'Ev_scale_school_prim',
    'Ev_scale_retail_food': 'Ev_scale_retail_food',
    'Ev_scale_retail_other': 'Ev_scale_retail_other',
    'Ev_scale_other': 'Ev_scale_other',
    'vent_heat_recovery_winter_residential': 'vent_heat_recovery_winter_residential',
    'vent_heat_recovery_winter_office': 'vent_heat_recovery_winter_office',
    'vent_heat_recovery_winter_schoolsec': 'vent_heat_recovery_winter_schoolsec',
    'vent_heat_recovery_winter_schoolprim': 'vent_heat_recovery_winter_schoolprim',
    'vent_heat_recovery_winter_retailfood': 'vent_heat_recovery_winter_retailfood',
    'vent_heat_recovery_winter_retailother': 'vent_heat_recovery_winter_retailother',
    'vent_heat_recovery_winter_other': 'vent_heat_recovery_winter_other',
    'vent_heat_recovery_summer_residential': 'vent_heat_recovery_summer_residential',
    'vent_heat_recovery_summer_office': 'vent_heat_recovery_summer_office',
    'vent_heat_recovery_summer_schoolsec': 'vent_heat_recovery_summer_schoolsec',
    'vent_heat_recovery_summer_schoolprim': 'vent_heat_recovery_summer_schoolprim',
    'vent_heat_recovery_summer_retailfood': 'vent_heat_recovery_summer_retailfood',
    'vent_heat_recovery_summer_retailother': 'vent_heat_recovery_summer_retailother',
    'vent_heat_recovery_summer_other': 'vent_heat_recovery_summer_other',
    'Vent_share_window_uncooled': 'Vent_share_window_uncooled',
    'Vent_share_window_cooled': 'Vent_share_window_cooled',
    'Vent_share_mech_uncooled': 'Vent_share_mech_uncooled',
    'Vent_share_mech_cooled': 'Vent_share_mech_cooled',
    'test_NFV_shares': 'test_NFV_shares',
    'usage_concurrency_winter_residential': 'usage_concurrency_winter_residential',
    'usage_concurrency_winter_office': 'usage_concurrency_winter_office',
    'usage_concurrency_winter_schoolsec': 'usage_concurrency_winter_schoolsec',
    'usage_concurrency_winter_schoolprim': 'usage_concurrency_winter_schoolprim',
    'usage_concurrency_winter_retailfood': 'usage_concurrency_winter_retailfood',
    'usage_concurrency_winter_retailother': 'usage_concurrency_winter_retailother',
    'usage_concurrency_winter_other': 'usage_concurrency_winter_other',
    'usage_concurrency_summer_residential': 'usage_concurrency_summer_residential',
    'usage_concurrency_summer_office': 'usage_concurrency_summer_office',
    'usage_concurrency_summer_schoolsec': 'usage_concurrency_summer_schoolsec',
    'usage_concurrency_summer_schoolprim': 'usage_concurrency_summer_schoolprim',
    'usage_concurrency_summer_retailfood': 'usage_concurrency_summer_retailfood',
    'usage_concurrency_summer_retailother': 'usage_concurrency_summer_retailother',
    'usage_concurrency_summer_other': 'usage_concurrency_summer_other',
    'DHW_demand_residential_kWhm2': 'DHW_demand_residential_kWhm2',
    'DHW_demand_office_kWhm2': 'DHW_demand_office_kWhm2',
    'DHW_demand_schoolsec_kWhm2': 'DHW_demand_schoolsec_kWhm2',
    'DHW_demand_schoolprim_kWhm2': 'DHW_demand_schoolprim_kWhm2',
    'DHW_demand_retailfood_kWhm2': 'DHW_demand_retailfood_kWhm2',
    'DHW_demand_retailother_kWhm2': 'DHW_demand_retailother_kWhm2',
    'DHW_demand_other_kWhm2': 'DHW_demand_other_kWhm2',
    'aux_el_demand_residential_kWhm2': 'aux_el_demand_residential_kWhm2',
    'aux_el_demand_office_kWhm2': 'aux_el_demand_office_kWhm2',
    'aux_el_demand_schoolsec_kWhm2': 'aux_el_demand_schoolsec_kWhm2',
    'aux_el_demand_schoolprim_kWhm2': 'aux_el_demand_schoolprim_kWhm2',
    'aux_el_demand_retailfood_kWhm2': 'aux_el_demand_retailfood_kWhm2',
    'aux_el_demand_retailother_kWhm2': 'aux_el_demand_retailother_kWhm2',
    'aux_el_demand_other_kWhm2': 'aux_el_demand_other_kWhm2',
    'Plugloads_scale_residential': 'Plugloads_scale_residential',
    'Plugloads_scale_office': 'Plugloads_scale_office',
    'Plugloads_scale_schoolsec': 'Plugloads_scale_schoolsec',
    'Plugloads_scale_schoolprim': 'Plugloads_scale_schoolprim',
    'Plugloads_scale_retailfood': 'Plugloads_scale_retailfood',
    'Plugloads_scale_retailother': 'Plugloads_scale_retailother',
    'Plugloads_scale_other': 'Plugloads_scale_other',
    'density_NFApPers_residential': 'density_NFApPers_residential',
    'density_NFApPers_office': 'density_NFApPers_office',
    'density_NFApPers_schoolsec': 'density_NFApPers_schoolsec',
    'density_NFApPers_retail': 'density_NFApPers_retail',
    'density_NFApPers_schoolprim': 'density_NFApPers_schoolprim',
    'density_NFApPers_retail_other': 'density_NFApPers_retail_other',
    'mob_simultaneity_edu': 'mob_simultaneity_edu',
    'mob_simultaneity_retail': 'mob_simultaneity_retail',
    'mob_simultaneity_office': 'mob_simultaneity_office',
    'mob_motorization_perNFA_residential': 'mob_motorization_perNFA_residential',
    'mob_motorization_perNFA_work': 'mob_motorization_perNFA_work',
    'mob_motorization_perNFA_retail': 'mob_motorization_perNFA_retail',
    'Plight_max_office': 'Plight_max_office',
    'Plight_max_schoolsec': 'Plight_max_schoolsec',
    'Plight_max_schoolprim': 'Plight_max_schoolprim',
    'Plight_min_office': 'Plight_min_office',
    'Plight_min_schoolsec': 'Plight_min_schoolsec',
    'Plight_min_schoolprim': 'Plight_min_schoolprim',
    'lighting_factor_office': 'lighting_factor_office',
    'lighting_factor_schoolsec': 'lighting_factor_schoolsec',
    'lighting_factor_schoolprim': 'lighting_factor_schoolprim',
    'lighting_factor_retailfood': 'lighting_factor_retailfood',
    'lighting_factor_retailother': 'lighting_factor_retailother',
    'lighting_factor_other': 'lighting_factor_other',
    'Daylightcoefficient_office': 'Daylightcoefficient_office',
    'Daylightcoefficient_schoolsec': 'Daylightcoefficient_schoolsec',
    'Daylightcoefficient_schoolprim': 'Daylightcoefficient_schoolprim',
    'daylightcontr_office': 'daylightcontr_office',
    'daylightcontr_schoolsec': 'daylightcontr_schoolsec',
    'daylightcontr_schoolprim': 'daylightcontr_schoolprim',
    'heating_month1': 'heating_month1',
    'heating_month2': 'heating_month2',
    'heating_month3': 'heating_month3',
    'heating_month4': 'heating_month4',
    'heating_month5': 'heating_month5',
    'heating_month6': 'heating_month6',
    'heating_month7': 'heating_month7',
    'heating_month8': 'heating_month8',
    'heating_month9': 'heating_month9',
    'heating_month10': 'heating_month10',
    'heating_month11': 'heating_month11',
    'heating_month12': 'heating_month12',
    'QHmax_room_m²': 'QHmax_room_m',
    'QHmax_room_MW': 'QHmax_room_MW',
    'QHmax_1el_m2': 'QHmax_1el_m2',
    'QHmax_2th_m2': 'QHmax_2th_m2',
    'QHmax_3el_m2': 'QHmax_3el_m2',
    'QHmax_4th_m2': 'QHmax_4th_m2',
    'QH_distr_loss_1el': 'QH_distr_loss_1el',
    'QH_distr_loss_2th': 'QH_distr_loss_2th',
    'QH_distr_loss_3el': 'QH_distr_loss_3el',
    'QH_distr_loss_4th': 'QH_distr_loss_4th',
    'heat_cop_1el': 'heat_cop_1el',
    'heat_cop_2th': 'heat_cop_2th',
    'heat_cop_3el': 'heat_cop_3el',
    'heat_cop_4th': 'heat_cop_4th',
    'QH_generation_eff_1el': 'QH_generation_eff_1el',
    'QH_generation_eff_2th': 'QH_generation_eff_2th',
    'QH_generation_eff_3el': 'QH_generation_eff_3el',
    'QH_generation_eff_4th': 'QH_generation_eff_4th',
    'QH_aux_wasteheat': 'QH_aux_wasteheat',
    'QH_aux_el_to_th_1el': 'QH_aux_el_to_th_1el',
    'QH_aux_el_to_th_2th': 'QH_aux_el_to_th_2th',
    'QH_aux_el_to_th_3el': 'QH_aux_el_to_th_3el',
    'QH_aux_el_to_th_4th': 'QH_aux_el_to_th_4th',
    'heat_th2_carrier_type': 'heat_th2_carrier_type',
    'heat_th4_carrier_type': 'heat_th4_carrier_type',
    'Tsetheat_min': 'Tsetheat_min',
    'cooling_month1': 'cooling_month1',
    'cooling_month2': 'cooling_month2',
    'cooling_month3': 'cooling_month3',
    'cooling_month4': 'cooling_month4',
    'cooling_month5': 'cooling_month5',
    'cooling_month6': 'cooling_month6',
    'cooling_month7': 'cooling_month7',
    'cooling_month8': 'cooling_month8',
    'cooling_month9': 'cooling_month9',
    'cooling_month10': 'cooling_month10',
    'cooling_month11': 'cooling_month11',
    'cooling_month12': 'cooling_month12',
    'cool_share_residential': 'cool_share_residential',
    'cool_share_office': 'cool_share_office',
    'cool_share_schoolsec': 'cool_share_schoolsec',
    'cool_share_schoolprim': 'cool_share_schoolprim',
    'cool_share_retailfood': 'cool_share_retailfood',
    'cool_share_retailother': 'cool_share_retailother',
    'cool_share_other': 'cool_share_other',
    'NFA_cooled': 'NFA_cooled',
    'NFAfrac_c': 'NFAfrac_c',
    'NFAfrac_u': 'NFAfrac_u',
    'QCmax_room_m2': 'QCmax_room_m2',
    'QCmax_room_MW': 'QCmax_room_MW',
    'QCmax_freecooling': 'QCmax_freecooling',
    'QCmax_1el': 'QCmax_1el',
    'QCmax_2th': 'QCmax_2th',
    'QCmax_3el': 'QCmax_3el',
    'QC_distr_losses_1el': 'QC_distr_losses_1el',
    'QC_distr_losses_2th': 'QC_distr_losses_2th',
    'QC_distr_losses_3el': 'QC_distr_losses_3el',
    'cool_cop_1el': 'cool_cop_1el',
    'cool_cop_2th': 'cool_cop_2th',
    'cool_cop_3el': 'cool_cop_3el',
    'QC_to_EC_1': 'QC_to_EC_1',
    'QC_generation_eff_2th': 'QC_generation_eff_2th',
    'QC_to_EC_3': 'QC_to_EC_3',
    'QC_aux_fc': 'QC_aux_fc',
    'QC_aux_1el': 'QC_aux_1el',
    'QC_aux_2th': 'QC_aux_2th',
    'QC_aux_3el': 'QC_aux_3el',
    'cool_th2_carrier_type': 'cool_th2_carrier_type',
    'Tsetcool_max': 'Tsetcool_max',
    'DHW_Tmin': 'DHW_Tmin',
    'DHW_Tmax_input': 'DHW_Tmax_input',
    'DHW_Tmax': 'DHW_Tmax',
    'DHW_1_share_residential': 'DHW_1_share_residential',
    'DHW_1_share_office': 'DHW_1_share_office',
    'DHW_1_share_schoolsec': 'DHW_1_share_schoolsec',
    'DHW_1_share_schoolprim': 'DHW_1_share_schoolprim',
    'DHW_1_share_retailfood': 'DHW_1_share_retailfood',
    'DHW_1_share_retailother': 'DHW_1_share_retailother',
    'DHW_1_share_other': 'DHW_1_share_other',
    'DHW_storage_1_liter': 'DHW_storage_1_liter',
    'DHW_storage_2_liter': 'DHW_storage_2_liter',
    'DHW_1_is_used': 'DHW_1_is_used',
    'DHW_2_is_used': 'DHW_2_is_used',
    'DHW_thermal_power_1_kW': 'DHW_thermal_power_1_kW',
    'DHW_losses_1': 'DHW_losses_1',
    'DHW_losses_2': 'DHW_losses_2',
    'DHW_efficiency_distribution_1': 'DHW_efficiency_distribution_1',
    'DHW_efficiency_distribution_2': 'DHW_efficiency_distribution_2',
    'DHW_1_incl_distribution_factor': 'DHW_1_incl_distribution_factor',
    'DHW_2_incl_distribution_factor': 'DHW_2_incl_distribution_factor',
    'DHW_carriertype_1': 'DHW_carriertype_1',
    'DHW_1_is_electric': 'DHW_1_is_electric',
    'DHW_carriertype_2': 'DHW_carriertype_2',
    'DHW_2_is_electric': 'DHW_2_is_electric',
    'DHW_1_efficiency': 'DHW_1_efficiency',
    'DHW_2_efficiency': 'DHW_2_efficiency',
    'DHW_conversion_1': 'DHW_conversion_1',
    'DHW_conversion_2': 'DHW_conversion_2',
    'DHW_1_el_aux': 'DHW_1_el_aux',
    'DHW_2_el_aux': 'DHW_2_el_aux',
    'DHW_occupancy_residential': 'DHW_occupancy_residential',
    'DHW_occupancy_office': 'DHW_occupancy_office',
    'DHW_occupancy_schoolsec': 'DHW_occupancy_schoolsec',
    'DHW_occupancy_schoolprim': 'DHW_occupancy_schoolprim',
    'DHW_occupancy_retailfood': 'DHW_occupancy_retailfood',
    'DHW_occupancy_retailother': 'DHW_occupancy_retailother',
    'DHW_occupancy_other': 'DHW_occupancy_other',
    'DHW_concurrency_residential': 'DHW_concurrency_residential',
    'DHW_concurrency_office': 'DHW_concurrency_office',
    'DHW_concurrency_schoolsec': 'DHW_concurrency_schoolsec',
    'DHW_concurrency_schoolprim': 'DHW_concurrency_schoolprim',
    'DHW_concurrency_retailfood': 'DHW_concurrency_retailfood',
    'DHW_concurrency_retailother': 'DHW_concurrency_retailother',
    'DHW_concurrency_other': 'DHW_concurrency_other',
    'DHW_storage_liter_pPerson': 'DHW_storage_liter_pPerson',
    'DHW_thermal_power_pPerson': 'DHW_thermal_power_pPerson',
    'DHW_thermal_power_Wpl': 'DHW_thermal_power_Wpl',
    'DHW_storage_env_temp_default': 'DHW_storage_env_temp_default',
    'PV_is_used': 'PV_is_used',
    'PV_profile_name': 'PV_profile_name',
    'PV_id': 'PV_id',
    'PV_scale': 'PV_scale',
    'PV_efficiency': 'PV_efficiency',
    'PV_m2_per_kWp': 'PV_m2_per_kWp',
    'PV_kWp': 'PV_kWp',
    'PV_module_area': 'PV_module_area',
    'FLEX_PV_is_used': 'FLEX_PV_is_used',
    'FLEX_is_used': 'FLEX_is_used',
    'FLEX_signal_name': 'FLEX_signal_name',
    'FLEX_signal_ID': 'FLEX_signal_ID',
    'FLEX_grid_maxpower_Wm2': 'FLEX_grid_maxpower_Wm2',
    'FLEX_is_used_for_plugloads': 'FLEX_is_used_for_plugloads',
    'FLEX_is_used_for_HVAC_min': 'FLEX_is_used_for_HVAC_min',
    'FLEX_is_used_for_ev_min': 'FLEX_is_used_for_ev_min',
    'flex_heat_dT': 'flex_heat_dT',
    'Tsetheat_flex': 'Tsetheat_flex',
    'FLEX_choice_heat_system': 'FLEX_choice_heat_system',
    'FLEX_heat1_use': 'FLEX_heat1_use',
    'FLEX_heat3_use': 'FLEX_heat3_use',
    'flex_cool_dT': 'flex_cool_dT',
    'Tsetcool_flex': 'Tsetcool_flex',
    'FLEX_choice_cool_system': 'FLEX_choice_cool_system',
    'FLEX_cool1_use': 'FLEX_cool1_use',
    'FLEX_cool3_use': 'FLEX_cool3_use',
    'Batt_is_used': 'Batt_is_used',
    'Batt_cap_kWh': 'Batt_cap_kWh',
    'Batt_cap_Wh_per_NFA': 'Batt_cap_Wh_per_NFA',
    'Batt_c_rate': 'Batt_c_rate',
    'Batt_max_power_specific': 'Batt_max_power_specific',
    'Batt_eff_factor_charge': 'Batt_eff_factor_charge',
    'Batt_eff_factor_discharge': 'Batt_eff_factor_discharge',
    'Batt_self_discharge_rate': 'Batt_self_discharge_rate',
    'Batt_auto_discharge_factor': 'Batt_auto_discharge_factor',
    'Batt_SOC_init': 'Batt_SOC_init',
    'Batt_is_used_for_plugloads': 'Batt_is_used_for_plugloads',
    'Batt_is_used_for_HVACminimum': 'Batt_is_used_for_HVACminimum',
    'Batt_is_used_for_EV': 'Batt_is_used_for_EV',
    'Batt_is_gridcharged': 'Batt_is_gridcharged',
    'flex_dhw_use': 'flex_dhw_use',
    'flex_Signals_selected_column': 'flex_Signals_selected_column',
    'Batt_is_not_used_during_signals': 'Batt_is_not_used_during_signals',
    'mobility_is_included': 'mobility_is_included',
    'mobility_region': 'mobility_region',
    'mobshare_residential': 'mobshare_residential',
    'mobshare_office': 'mobshare_office',
    'mobshare_school': 'mobshare_school',
    'mobshare_retail': 'mobshare_retail',
    'pkm_pedestrian': 'pkm_pedestrian',
    'pkm_bike': 'pkm_bike',
    'pkm_mofa': 'pkm_mofa',
    'pkm_car_driver': 'pkm_car_driver',
    'pkm_car_passenger': 'pkm_car_passenger',
    'pkm_bus': 'pkm_bus',
    'pkm_tram_metro': 'pkm_tram_metro',
    'pkm_train': 'pkm_train',
    'pkm_distancebus': 'pkm_distancebus',
    'mobility_vehicle_count': 'mobility_vehicle_count',
    'EV_share': 'EV_share',
    'EV_demand_kWhpkm': 'EV_demand_kWhpkm',
    'EV_battsize_kWh': 'EV_battsize_kWh',
    'EV_storage_total_kWh': 'EV_storage_total_kWh',
    'EV_self_discharge_per_week': 'EV_self_discharge_per_week',
    'EV_selfdischarge_per_h': 'EV_selfdischarge_per_h',
    'EV_soc_minimum': 'EV_soc_minimum',
    'EV_charging_efficiency': 'EV_charging_efficiency',
    'EV_charging_losses_surcharge_factor': 'EV_charging_losses_surcharge_factor',
    'EV_max_charging_power_ratio': 'EV_max_charging_power_ratio',
    'EV_soc_min_work': 'EV_soc_min_work',
    'EV_soc_min_retail': 'EV_soc_min_retail',
    'moped_factor': 'moped_factor',
    'EV_share_constant_charging': 'EV_share_constant_charging',
    'mob_pkm_factor': 'mob_pkm_factor',
    'EV_experimental_calculation': 'EV_experimental_calculation',
    'EV_mileage_residential': 'EV_mileage_residential',
    'EV_mileage_work': 'EV_mileage_work',
    'EV_mileage_retail': 'EV_mileage_retail',
    'EV_soc_min_ext': 'EV_soc_min_ext',
    'EV_soc_min_discharge': 'EV_soc_min_discharge',
    'fossile_demand_kWhpkm': 'fossile_demand_kWhpkm',
    'EV_count_residential': 'EV_count_residential',
    'EV_count_work': 'EV_count_work',
    'EV_count_retail': 'EV_count_retail',
    'ev_bidirectional_use': 'ev_bidirectional_use',
    'GWP_walls_name': 'GWP_walls_name',
    'GWP_windows_name': 'GWP_windows_name',
    'GWP_roof_name': 'GWP_roof_name',
    'GWP_ground_name': 'GWP_ground_name',
    'GPW_ceilings_name': 'GPW_ceilings_name',
    'COMP_name_terrace': 'COMP_name_terrace',
    'COMP_name_basement_ceiling': 'COMP_name_basement_ceiling',
    'COMP_name_fundament': 'COMP_name_fundament',
    'COMP_name_ceil_to_air': 'COMP_name_ceil_to_air',
    'COMP_name_wall_earth_contacted': 'COMP_name_wall_earth_contacted',
    'COMP_name_internal_wall_load': 'COMP_name_internal_wall_load',
    'COMP_name_internal_wall_nonload': 'COMP_name_internal_wall_nonload',
    'COMP_name_ceiling_topfloor': 'COMP_name_ceiling_topfloor',
    'COMP_name_wall_ec_unheated': 'COMP_name_wall_ec_unheated',
    'COMP_name_basement_floor_unheated': 'COMP_name_basement_floor_unheated',
    'COMP_name_columns': 'COMP_name_columns',
    'COMP_name_internal_wall_unheated': 'COMP_name_internal_wall_unheated',
    'COMP_name_unheated_horizontal': 'COMP_name_unheated_horizontal',
    'COMP_name_balconies': 'COMP_name_balconies',
    'COMP_name_windowframe': 'COMP_name_windowframe',
    'COMP_name_windowglazing': 'COMP_name_windowglazing',
    'COMP_name_other': 'COMP_name_other',
    'GWP_general_name': 'GWP_general_name',
    'GWP_other_name': 'GWP_other_name',
    'GWP_ref_area_walls': 'GWP_ref_area_walls',
    'GWP_ref_area_windows': 'GWP_ref_area_windows',
    'GWP_ref_area_roof': 'GWP_ref_area_roof',
    'GWP_ref_area_fundament': 'GWP_ref_area_fundament',
    'GWP_ref_area_ceilings': 'GWP_ref_area_ceilings',
    'COMP_area_terrace': 'COMP_area_terrace',
    'COMP_area_basement_ceiling': 'COMP_area_basement_ceiling',
    'COMP_area_fundament': 'COMP_area_fundament',
    'COMP_area_ceil_to_air': 'COMP_area_ceil_to_air',
    'COMP_area_wall_earth_contacted': 'COMP_area_wall_earth_contacted',
    'COMP_area_internal_wall_load': 'COMP_area_internal_wall_load',
    'COMP_area_internal_wall_nonload': 'COMP_area_internal_wall_nonload',
    'COMP_area_ceiling_topfloor': 'COMP_area_ceiling_topfloor',
    'COMP_area_wall_ec_unheated': 'COMP_area_wall_ec_unheated',
    'COMP_area_basement_floor_unheated': 'COMP_area_basement_floor_unheated',
    'COMP_area_columns': 'COMP_area_columns',
    'COMP_area_internal_wall_unheated': 'COMP_area_internal_wall_unheated',
    'COMP_area_unheated_horizontal': 'COMP_area_unheated_horizontal',
    'COMP_area_balconies': 'COMP_area_balconies',
    'COMP_area_windowframe': 'COMP_area_windowframe',
    'COMP_area_windowglazing': 'COMP_area_windowglazing',
    'GWP_refratio_walls': 'GWP_refratio_walls',
    'GWP_refratio_windows': 'GWP_refratio_windows',
    'GWP_refratio_roof': 'GWP_refratio_roof',
    'GWP_refratio_fundament': 'GWP_refratio_fundament',
    'GWP_refratio_ceilings': 'GWP_refratio_ceilings',
    'GWP_pv_name': 'GWP_pv_name',
    'GWP_refratio_pv': 'GWP_refratio_pv',
    'GWP_boreholes_name': 'GWP_boreholes_name',
    'borehole_count': 'borehole_count',
    'GWP_ventilation_name': 'GWP_ventilation_name',
    'GWP_solarthermal_name': 'GWP_solarthermal_name',
    'GWP_battery_name': 'GWP_battery_name',
    'GWP_storage_name': 'GWP_storage_name',
    'GWP_tga_general_name': 'GWP_tga_general_name',
    'GWP_tga_other_name': 'GWP_tga_other_name',
    'GWP_refratio_boreholes': 'GWP_refratio_boreholes',
    'GWP_direct_fossile': 'GWP_direct_fossile',
    'GWP_direct_biogenic': 'GWP_direct_biogenic',
    'GWP_direct_biogenic_share': 'GWP_direct_biogenic_share',
    'GWP_direct_life': 'GWP_direct_life',
    'GWP_miv_count_ev': 'GWP_miv_count_ev',
    'GWP_miv_count_fossile': 'GWP_miv_count_fossile',
    'GWP_mobility_construction_fossil': 'GWP_mobility_construction_fossil',
    'GWP_mobility_construction_ev': 'GWP_mobility_construction_ev',
    'GHG_LCA_timeframe_years': 'GHG_LCA_timeframe_years',
    'GWP_mobility_moped_gpPKm': 'GWP_mobility_moped_gpPKm',
    'GWP_mobility_car_gpPKm': 'GWP_mobility_car_gpPKm',
    'year_rcp0': 'year_rcp0',
    'year_rcp1': 'year_rcp1',
    'year_rcp2': 'year_rcp2',
    'year_rcp3': 'year_rcp3',
    'grid_rcp1': 'grid_rcp1',
    'grid_rcp2': 'grid_rcp2',
    'grid_rcp3': 'grid_rcp3',
    'rcp1_renewable': 'rcp1_renewable',
    'rcp2_renewable': 'rcp2_renewable',
    'rcp3_renewable': 'rcp3_renewable',
    'rcp1_dh': 'rcp1_dh',
    'rcp2_dh': 'rcp2_dh',
    'rcp3_dh': 'rcp3_dh',
    'rcp1_fossil': 'rcp1_fossil',
    'rcp2_fossil': 'rcp2_fossil',
    'rcp3_fossil': 'rcp3_fossil',
    'GWP_rcpi_grid': 'GWP_rcpi_grid',
    'GWP_rcpi_grid_substition': 'GWP_rcpi_grid_substition',
    'GWP_rcpi_district_heating': 'GWP_rcpi_district_heating',
    'GWP_rcpi_fossil': 'GWP_rcpi_fossil',
    'GWP_rcpi_natural_gas': 'GWP_rcpi_natural_gas',
    'GWP_rcpi_biomass': 'GWP_rcpi_biomass',
    'GWP_rcpi_mob_fossile': 'GWP_rcpi_mob_fossile',
    'GWP_rcpi_renewable': 'GWP_rcpi_renewable',
    'fPE_grid_profile': 'fPE_grid_profile',
    'district_heating_conversion_profile': 'district_heating_conversion_profile',
    'fGHG_grid_profile': 'fGHG_grid_profile',
    'fPE_grid_column': 'fPE_grid_column',
    'fGHG_grid_column': 'fGHG_grid_column',
    'heat_th2_is_dh': 'heat_th2_is_dh',
    'heat_th4_is_dh': 'heat_th4_is_dh',
    'cool_th2_is_dh': 'cool_th2_is_dh',
    'dhw1_is_dh': 'dhw1_is_dh',
    'dhw2_is_dh': 'dhw2_is_dh',
    'heat_th2_is_ng': 'heat_th2_is_ng',
    'heat_th4_is_ng': 'heat_th4_is_ng',
    'cool_th2_is_ng': 'cool_th2_is_ng',
    'dhw1_is_ng': 'dhw1_is_ng',
    'dhw2_is_ng': 'dhw2_is_ng',
    'heat_th2_is_bio': 'heat_th2_is_bio',
    'heat_th4_is_bio': 'heat_th4_is_bio',
    'cool_th2_is_bio': 'cool_th2_is_bio',
    'dhw1_is_bio': 'dhw1_is_bio',
    'dhw2_is_bio': 'dhw2_is_bio',
    'heat_th2_is_other': 'heat_th2_is_other',
    'heat_th4_is_other': 'heat_th4_is_other',
    'cool_th2_is_other': 'cool_th2_is_other',
    'dhw1_is_other': 'dhw1_is_other',
    'dhw2_is_other': 'dhw2_is_other',
    'fPE_flex_factor': 'fPE_flex_factor',
    'pe_conversion_factor_gasoline': 'pe_conversion_factor_gasoline',
    'StatPAX_residential': 'StatPAX_residential',
    'StatPAX_office': 'StatPAX_office',
    'StatPAX_schoolsec': 'StatPAX_schoolsec',
    'StatPAX_schoolprim': 'StatPAX_schoolprim',
    'StatPAX_retail': 'StatPAX_retail',
    'StatPAX_retailother': 'StatPAX_retailother',
    'e_kWhm2a': 'e_kWhm2a',
    'EV_charging_stations': 'EV_charging_stations',
    'EV_charging_station_power': 'EV_charging_station_power',
    'Ta_annual_avg': 'Ta_annual_avg',
    'Ta_avg_heating_period': 'Ta_avg_heating_period',
    'Ta_avg_cooling_period': 'Ta_avg_cooling_period',
    'UED_plugloads': 'UED_plugloads',
    'UED_lighting': 'UED_lighting',
    'UED_auxiliary': 'UED_auxiliary',
    'UED_heating': 'UED_heating',
    'UED_cooling': 'UED_cooling',
    'UED_dhw': 'UED_dhw',
    'UED_ventilation': 'UED_ventilation',
    'UED_mim_electric': 'UED_mim_electric',
    'UED_mim_fossile': 'UED_mim_fossile',
    'QT': 'QT',
    'QV': 'QV',
    'QVn': 'QVn',
    'QS': 'QS',
    'QI': 'QI',
    'QH': 'QH',
    'QC': 'QC',
    'QV_heatrecovery': 'QV_heatrecovery',
    'QT_winter': 'QT_winter',
    'QV_winter': 'QV_winter',
    'QVn_winter': 'QVn_winter',
    'QS_winter': 'QS_winter',
    'QI_winter': 'QI_winter',
    'QH_winter': 'QH_winter',
    'QC_winter': 'QC_winter',
    'test_heat_balance_winter': 'test_heat_balance_winter',
    'QT_wall_winter': 'QT_wall_winter',
    'QT_roof_winter': 'QT_roof_winter',
    'QT_ground_winter': 'QT_ground_winter',
    'QT_window_winter': 'QT_window_winter',
    'QT_psi_winter': 'QT_psi_winter',
    'QV_inf_winter': 'QV_inf_winter',
    'QV_window_winter': 'QV_window_winter',
    'QV_mechvent_winter': 'QV_mechvent_winter',
    'QV_heatrecovery_winter': 'QV_heatrecovery_winter',
    'QH_min_winter': 'QH_min_winter',
    'QH_flex_winter': 'QH_flex_winter',
    'QC_min_winter': 'QC_min_winter',
    'QC_flex_winter': 'QC_flex_winter',
    'QH_flexshare_winter': 'QH_flexshare_winter',
    'QC_flexshare_winter': 'QC_flexshare_winter',
    'QT_summer': 'QT_summer',
    'QV_summer': 'QV_summer',
    'QVn_summer': 'QVn_summer',
    'QS_summer': 'QS_summer',
    'QI_summer': 'QI_summer',
    'QH_summer': 'QH_summer',
    'QC_summer': 'QC_summer',
    'test_heat_balance_summer': 'test_heat_balance_summer',
    'QT_wall_summer': 'QT_wall_summer',
    'QT_roof_summer': 'QT_roof_summer',
    'QT_ground_summer': 'QT_ground_summer',
    'QT_window_summer': 'QT_window_summer',
    'QT_psi_summer': 'QT_psi_summer',
    'QV_inf_summer': 'QV_inf_summer',
    'QV_window_summer': 'QV_window_summer',
    'QV_mechvent_summer': 'QV_mechvent_summer',
    'QV_heatrecovery_summer': 'QV_heatrecovery_summer',
    'QH_min_summer': 'QH_min_summer',
    'QH_flex_summer': 'QH_flex_summer',
    'QC_min_summer': 'QC_min_summer',
    'QC_flex_summer': 'QC_flex_summer',
    'QH_flexshare_summer': 'QH_flexshare_summer',
    'QC_flexshare_summer': 'QC_flexshare_summer',
    'test_heat_balance': 'test_heat_balance',
    'QT_u': 'QT_u',
    'QV_u': 'QV_u',
    'QVn_u': 'QVn_u',
    'QS_u': 'QS_u',
    'QI_u': 'QI_u',
    'QH_u': 'QH_u',
    'QT_wall_u': 'QT_wall_u',
    'QT_roof_u': 'QT_roof_u',
    'QT_ground_u': 'QT_ground_u',
    'QT_window_u': 'QT_window_u',
    'QT_psi_u': 'QT_psi_u',
    'QV_inf_u': 'QV_inf_u',
    'QV_window_u': 'QV_window_u',
    'QV_mechvent_u': 'QV_mechvent_u',
    'QV_heatrecovery_u': 'QV_heatrecovery_u',
    'QH_min_u': 'QH_min_u',
    'QH_flex_u': 'QH_flex_u',
    'QH_flexanteil_u': 'QH_flexanteil_u',
    'QT_c': 'QT_c',
    'QV_c': 'QV_c',
    'QVn_c': 'QVn_c',
    'QS_c': 'QS_c',
    'QI_c': 'QI_c',
    'QH_c': 'QH_c',
    'QC_c': 'QC_c',
    'QT_wall_c': 'QT_wall_c',
    'QT_roof_c': 'QT_roof_c',
    'QT_ground_c': 'QT_ground_c',
    'QT_window_c': 'QT_window_c',
    'QT_psi_c': 'QT_psi_c',
    'QV_inf_c': 'QV_inf_c',
    'QV_window_c': 'QV_window_c',
    'QV_mechvent_c': 'QV_mechvent_c',
    'QV_heatrecovery_c': 'QV_heatrecovery_c',
    'QH_min_c': 'QH_min_c',
    'QH_flex_c': 'QH_flex_c',
    'QC_min_c': 'QC_min_c',
    'QC_flex_c': 'QC_flex_c',
    'QC_flexanteil': 'QC_flexanteil',
    'QH_flexanteil_c': 'QH_flexanteil_c',
    'Tu_avg_winter': 'Tu_avg_winter',
    'Tc_avg_winter': 'Tc_avg_winter',
    'Tu_avg_summer': 'Tu_avg_summer',
    'Tc_avg_summer': 'Tc_avg_summer',
    'dTu_winter': 'dTu_winter',
    'dTc_winter': 'dTc_winter',
    'dTu_summer': 'dTu_summer',
    'dTc_summer': 'dTc_summer',
    'EUI_plugAuxLight': 'EUI_plugAuxLight',
    'EUI_plugloads': 'EUI_plugloads',
    'EUI_auxiliary': 'EUI_auxiliary',
    'EUI_lighting': 'EUI_lighting',
    'EUIh_el': 'EUIh_el',
    'EUIh_el_aux': 'EUIh_el_aux',
    'EUIc_el': 'EUIc_el',
    'EUIc_el_aux': 'EUIc_el_aux',
    'EUIdhw_el': 'EUIdhw_el',
    'EUIv_el': 'EUIv_el',
    'EUIdhwdirect_el': 'EUIdhwdirect_el',
    'Batt_total_charge_input': 'Batt_total_charge_input',
    'EUIev_el': 'EUIev_el',
    'EUI_el_total': 'EUI_el_total',
    'PV_total': 'PV_total',
    'PV_to_plugloads': 'PV_to_plugloads',
    'PV_to_Eh_min': 'PV_to_Eh_min',
    'PV_to_Ec_min': 'PV_to_Ec_min',
    'PV_to_Edhw_min': 'PV_to_Edhw_min',
    'PV_to_Ev_min': 'PV_to_Ev_min',
    'PV_to_Eev_min': 'PV_to_Eev_min',
    'PV_total_direct': 'PV_total_direct',
    'PV_to_Eh_flex': 'PV_to_Eh_flex',
    'PV_to_Ec_flex': 'PV_to_Ec_flex',
    'PV_to_Edhw': 'PV_to_Edhw',
    'PV_to_Edhw_direct': 'PV_to_Edhw_direct',
    'PV_to_Batt': 'PV_to_Batt',
    'PV_to_Eev_flex': 'PV_to_Eev_flex',
    'PV_total_flex': 'PV_total_flex',
    'PV_to_Egrid': 'PV_to_Egrid',
    'Batt_to_plugloads': 'Batt_to_plugloads',
    'Batt_to_HVAC': 'Batt_to_HVAC',
    'Batt_to_Eh_min': 'Batt_to_Eh_min',
    'Batt_to_Ec_min': 'Batt_to_Ec_min',
    'Batt_to_Edhw_min': 'Batt_to_Edhw_min',
    'Batt_to_Ev_min': 'Batt_to_Ev_min',
    'Batt_to_Eev_min': 'Batt_to_Eev_min',
    'Batt_charging_losses': 'Batt_charging_losses',
    'VRGrid_to_plugloads': 'VRGrid_to_plugloads',
    'VRGrid_to_Eh_min': 'VRGrid_to_Eh_min',
    'VRGrid_to_Ec_min': 'VRGrid_to_Ec_min',
    'VRGrid_to_Edhw_min': 'VRGrid_to_Edhw_min',
    'VRGrid_to_Ev_min': 'VRGrid_to_Ev_min',
    'VRGrid_to_Eev_min': 'VRGrid_to_Eev_min',
    'VRGrid_to_min': 'VRGrid_to_min',
    'VRGrid_to_Eh_flex': 'VRGrid_to_Eh_flex',
    'VRGrid_to_Ec_flex': 'VRGrid_to_Ec_flex',
    'VRGrid_to_Edhw_flex': 'VRGrid_to_Edhw_flex',
    'VRGrid_to_Batt': 'VRGrid_to_Batt',
    'VRGrid_to_Eev_flex': 'VRGrid_to_Eev_flex',
    'VRGrid_to_flex': 'VRGrid_to_flex',
    'VRGrid_to_building': 'VRGrid_to_building',
    'Eev_to_plugloads': 'Eev_to_plugloads',
    'Eev_to_HVAC': 'Eev_to_HVAC',
    'Eev_to_Eh_min': 'Eev_to_Eh_min',
    'Eev_to_Ec_min': 'Eev_to_Ec_min',
    'Eev_to_Edhw_min': 'Eev_to_Edhw_min',
    'Eev_to_Ev_min': 'Eev_to_Ev_min',
    'Eev_discharge_loss': 'Eev_discharge_loss',
    'Eev_to_district': 'Eev_to_district',
    'Grid_to_plugloads': 'Grid_to_plugloads',
    'Grid_to_Eh_min': 'Grid_to_Eh_min',
    'Grid_to_Ec_min': 'Grid_to_Ec_min',
    'Grid_to_Edhw_min': 'Grid_to_Edhw_min',
    'Grid_to_Ev_min': 'Grid_to_Ev_min',
    'Grid_to_building_min': 'Grid_to_building_min',
    'Grid_to_Eev_min': 'Grid_to_Eev_min',
    'Grid_to_min': 'Grid_to_min',
    'Eev_ext_charge': 'Eev_ext_charge',
    'EUIh_district_heating': 'EUIh_district_heating',
    'EUIdhw_district_heating': 'EUIdhw_district_heating',
    'EUI_district_heating': 'EUI_district_heating',
    'EUIh_natural_gas': 'EUIh_natural_gas',
    'EUIdhw_natural_gas': 'EUIdhw_natural_gas',
    'EUI_natural_gas': 'EUI_natural_gas',
    'EUIh_biomass': 'EUIh_biomass',
    'EUIdhw_biomass': 'EUIdhw_biomass',
    'EUI_biomass': 'EUI_biomass',
    'EUIh_other': 'EUIh_other',
    'EUIc_other': 'EUIc_other',
    'EUIdhw_other': 'EUIdhw_other',
    'EUI_other': 'EUI_other',
    'EUI_mob_fossil': 'EUI_mob_fossil',
    'EUIh_2th': 'EUIh_2th',
    'EUIh_4th': 'EUIh_4th',
    'EUIc_2th': 'EUIc_2th',
    'EUIdhw_1th': 'EUIdhw_1th',
    'EUIdhw_2th': 'EUIdhw_2th',
    'Grid_total_flexandnotflex': 'Grid_total_flexandnotflex',
    'context_factor_density': 'context_factor_density',
    'context_factor_mobility': 'context_factor_mobility',
    'context_factor_renovation': 'context_factor_renovation',
    'PEI_demand': 'PEI_demand',
    'PEI_el_plugloads': 'PEI_el_plugloads',
    'PEI_el_hvac': 'PEI_el_hvac',
    'PEI_district_heating': 'PEI_district_heating',
    'PEI_natural_gas': 'PEI_natural_gas',
    'PEI_biomass': 'PEI_biomass',
    'PEI_other': 'PEI_other',
    'PEI_mob_total': 'PEI_mob_total',
    'PEI_mob_fossile': 'PEI_mob_fossile',
    'PEI_mob_el': 'PEI_mob_el',
    'PEI_storage_losses': 'PEI_storage_losses',
    'PEI_cf_density': 'PEI_cf_density',
    'PEI_cf_mobility': 'PEI_cf_mobility',
    'PEI_cf_renovation': 'PEI_cf_renovation',
    'PEI_sub_PV': 'PEI_sub_PV',
    'PEI_sub_flex': 'PEI_sub_flex',
    'PEI_balance': 'PEI_balance',
    'PEI_grid_import': 'PEI_grid_import',
    'PEI_flex_import': 'PEI_flex_import',
    'PEI_evExtCharge_import': 'PEI_evExtCharge_import',
    'PEI_import': 'PEI_import',
    'PEI_pv_export': 'PEI_pv_export',
    'PEI_evOtherTravel_export': 'PEI_evOtherTravel_export',
    'PEI_export': 'PEI_export',
    'PEI_saldo_project': 'PEI_saldo_project',
    'PEI_saldo_target': 'PEI_saldo_target',
    'PEI_importExport_balance': 'PEI_importExport_balance',
    'fPE_grid': 'fPE_grid',
    'fPE_eff': 'fPE_eff',
    'GWP_ee_walls_fossile': 'GWP_ee_walls_fossile',
    'GWP_ee_walls_biogenic': 'GWP_ee_walls_biogenic',
    'GWP_life_walls': 'GWP_life_walls',
    'GWP_ee_lc_walls_fossil': 'GWP_ee_lc_walls_fossil',
    'GWP_ee_lc_walls_biogenic': 'GWP_ee_lc_walls_biogenic',
    'GWP_ee_lc_walls': 'GWP_ee_lc_walls',
    'GWP_ee_windows_fossile': 'GWP_ee_windows_fossile',
    'GWP_ee_windows_bigenic': 'GWP_ee_windows_bigenic',
    'GWP_life_windows': 'GWP_life_windows',
    'GWP_ee_lc_windows_fossile': 'GWP_ee_lc_windows_fossile',
    'GWP_ee_lc_windows_biogenic': 'GWP_ee_lc_windows_biogenic',
    'GWP_ee_lc_windows': 'GWP_ee_lc_windows',
    'GWP_ee_roof_fossile': 'GWP_ee_roof_fossile',
    'GWP_ee_roof_biogenic': 'GWP_ee_roof_biogenic',
    'GWP_life_roof': 'GWP_life_roof',
    'GWP_ee_lc_roof_fossile': 'GWP_ee_lc_roof_fossile',
    'GWP_ee_lc_roof_biogenic': 'GWP_ee_lc_roof_biogenic',
    'GWP_ee_lc_roof': 'GWP_ee_lc_roof',
    'GWP_ee_ground_fossile': 'GWP_ee_ground_fossile',
    'GWP_ee_ground_biogenic': 'GWP_ee_ground_biogenic',
    'GWP_life_ground': 'GWP_life_ground',
    'GWP_ee_lc_ground_fossile': 'GWP_ee_lc_ground_fossile',
    'GWP_ee_lc_ground_biogenic': 'GWP_ee_lc_ground_biogenic',
    'GWP_ee_lc_ground': 'GWP_ee_lc_ground',
    'GWP_ee_ceilings_fossile': 'GWP_ee_ceilings_fossile',
    'GWP_ee_ceilings_biogenic': 'GWP_ee_ceilings_biogenic',
    'GWP_life_ceilings': 'GWP_life_ceilings',
    'GWP_ee_lc_ceilings_fossile': 'GWP_ee_lc_ceilings_fossile',
    'GWP_ee_lc_ceilings_biogenic': 'GWP_ee_lc_ceilings_biogenic',
    'GWP_ee_lc_ceil': 'GWP_ee_lc_ceil',
    'GWP_ee_general_fossile': 'GWP_ee_general_fossile',
    'GWP_ee_general_bigonenic': 'GWP_ee_general_bigonenic',
    'GWP_life_general': 'GWP_life_general',
    'GWP_ee_lc_general_fossile': 'GWP_ee_lc_general_fossile',
    'GWP_ee_lc_general_biogenic': 'GWP_ee_lc_general_biogenic',
    'GWP_ee_general': 'GWP_ee_general',
    'GWP_ee_other_fossile': 'GWP_ee_other_fossile',
    'GWP_ee_other_biogenic': 'GWP_ee_other_biogenic',
    'GWP_life_other': 'GWP_life_other',
    'GWP_ee_lc_other_fossile': 'GWP_ee_lc_other_fossile',
    'GWP_ee_lc_other_biogenic': 'GWP_ee_lc_other_biogenic',
    'GWP_ee_lc_other': 'GWP_ee_lc_other',
    'GWP_ee_direct_fossile': 'GWP_ee_direct_fossile',
    'GWP_ee_direct_biogenic': 'GWP_ee_direct_biogenic',
    'GWP_life_direct': 'GWP_life_direct',
    'GWP_ee_lc_direct_fossile': 'GWP_ee_lc_direct_fossile',
    'GWP_ee_lc_direct_biogenic': 'GWP_ee_lc_direct_biogenic',
    'GWP_ee_lc_direct': 'GWP_ee_lc_direct',
    'GWP_ee_con_build': 'GWP_ee_con_build',
    'GWP_ee_rep_build': 'GWP_ee_rep_build',
    'GWP_ee_lc_fossil': 'GWP_ee_lc_fossil',
    'GWP_ee_lc_biogenic': 'GWP_ee_lc_biogenic',
    'GWP_ee_lc_construction': 'GWP_ee_lc_construction',
    'GWP_ee_tga_pv_fossile': 'GWP_ee_tga_pv_fossile',
    'GWP_ee_tga_pv_biogenic': 'GWP_ee_tga_pv_biogenic',
    'GWP_life_tga_pv': 'GWP_life_tga_pv',
    'GWP_ee_lc_pv': 'GWP_ee_lc_pv',
    'GWP_ee_tga_boreholes_fossile': 'GWP_ee_tga_boreholes_fossile',
    'GWP_ee_tga_boreholes_biogenic': 'GWP_ee_tga_boreholes_biogenic',
    'GWP_life_tga_boreholes': 'GWP_life_tga_boreholes',
    'GWP_ee_lc_boreholes': 'GWP_ee_lc_boreholes',
    'GWP_ee_tga_ventilation_fossile': 'GWP_ee_tga_ventilation_fossile',
    'GWP_ee_tga_ventilation_biogenic': 'GWP_ee_tga_ventilation_biogenic',
    'GWP_life_tga_ventilation': 'GWP_life_tga_ventilation',
    'GWP_ee_lc_ventilation': 'GWP_ee_lc_ventilation',
    'GWP_ee_tga_solarthermal_fossile': 'GWP_ee_tga_solarthermal_fossile',
    'GWP_ee_tga_solarthermal_biogenic': 'GWP_ee_tga_solarthermal_biogenic',
    'GWP_life_solarthermal': 'GWP_life_solarthermal',
    'GWP_ee_lc_solarthermal': 'GWP_ee_lc_solarthermal',
    'GWP_ee_tga_battery_fossile': 'GWP_ee_tga_battery_fossile',
    'GWP_ee_tga_battery_biogenic': 'GWP_ee_tga_battery_biogenic',
    'GWP_life_battery': 'GWP_life_battery',
    'GWP_ee_lc_battery': 'GWP_ee_lc_battery',
    'GWP_ee_tga_storage_fossile': 'GWP_ee_tga_storage_fossile',
    'GWP_ee_tga_storage_biogenic': 'GWP_ee_tga_storage_biogenic',
    'GWP_life_storage': 'GWP_life_storage',
    'GWP_ee_lc_storage': 'GWP_ee_lc_storage',
    'GWP_ee_tga_general_fossile': 'GWP_ee_tga_general_fossile',
    'GWP_ee_tga_general_biogenic': 'GWP_ee_tga_general_biogenic',
    'GWP_life_tga_general': 'GWP_life_tga_general',
    'GWP_ee_lc_tga_general': 'GWP_ee_lc_tga_general',
    'GWP_ee_tga_other_fossile': 'GWP_ee_tga_other_fossile',
    'GWP_ee_tga_other_biogenic': 'GWP_ee_tga_other_biogenic',
    'GWP_life_tga_other': 'GWP_life_tga_other',
    'GWP_ee_lc_tga_other': 'GWP_ee_lc_tga_other',
    'GWP_ee_con_tga': 'GWP_ee_con_tga',
    'GWP_ee_rep_tga': 'GWP_ee_rep_tga',
    'GWP_ee_lc_tga': 'GWP_ee_lc_tga',
    'GWP_ee_mob_fossile': 'GWP_ee_mob_fossile',
    'GWP_ee_mob_ev': 'GWP_ee_mob_ev',
    'GWP_ee_lc_mob': 'GWP_ee_lc_mob',
    'GWP_oe_battery_charge': 'GWP_oe_battery_charge',
    'GWP_emInt_grid_avg': 'GWP_emInt_grid_avg',
    'GWP_emInt_grid': 'GWP_emInt_grid',
    'GWP_emInt_flex': 'GWP_emInt_flex',
    'GWP_emInt_batt_charge': 'GWP_emInt_batt_charge',
    'GWP_emInt_ev_charge': 'GWP_emInt_ev_charge',
    'GWP_emInt_PV_feedin': 'GWP_emInt_PV_feedin',
    'GWP_oe_grid_build': 'GWP_oe_grid_build',
    'GWP_oe_flex_build': 'GWP_oe_flex_build',
    'GWP_oe_district_heating': 'GWP_oe_district_heating',
    'GWP_oe_natural_gas': 'GWP_oe_natural_gas',
    'GWP_oe_biomass': 'GWP_oe_biomass',
    'GWP_oe_other': 'GWP_oe_other',
    'GWP_oe_grid_feedin': 'GWP_oe_grid_feedin',
    'GWP_oe_building': 'GWP_oe_building',
    'GWP_oe_mob_ev': 'GWP_oe_mob_ev',
    'GWP_oe_mob_ev_export': 'GWP_oe_mob_ev_export',
    'GWP_oe_mob_fossile': 'GWP_oe_mob_fossile',
    'GWP_oe_mob': 'GWP_oe_mob',
    'GWP_oe': 'GWP_oe',
    'GWP_oe_lc_grid_build': 'GWP_oe_lc_grid_build',
    'GWP_oe_lc_flex_build': 'GWP_oe_lc_flex_build',
    'GWP_oe_lc_district_heating': 'GWP_oe_lc_district_heating',
    'GWP_oe_lc_natural_gas': 'GWP_oe_lc_natural_gas',
    'GWP_oe_lc_biomass': 'GWP_oe_lc_biomass',
    'GWP_oe_lc_other': 'GWP_oe_lc_other',
    'GWP_oe_lc_grid_feedin': 'GWP_oe_lc_grid_feedin',
    'GWP_oe_lc_building': 'GWP_oe_lc_building',
    'GWP_oe_lc_emission': 'GWP_oe_lc_emission',
    'GWP_oe_lc_emission_savings': 'GWP_oe_lc_emission_savings',
    'GWP_oe_lc_mob_ev': 'GWP_oe_lc_mob_ev',
    'GWP_oe_lc_mob_export': 'GWP_oe_lc_mob_export',
    'GWP_oe_lc_mob_fossile': 'GWP_oe_lc_mob_fossile',
    'GWP_oe_lc_mob': 'GWP_oe_lc_mob',
    'GWP_lc_total': 'GWP_lc_total',
    'GWP_lc_OE_total': 'GWP_lc_OE_total',
    'GWP_lc_EE_total': 'GWP_lc_EE_total',
    'cost_E_grid': 'cost_E_grid',
    'cost_VRGrid_flex': 'cost_VRGrid_flex',
    'cost_PV_to_Egrid': 'cost_PV_to_Egrid',
    'cost_total': 'cost_total',
    'flex_signal_ratio': 'flex_signal_ratio',
    'flex_signal_ratio_winter': 'flex_signal_ratio_winter',
    'flex_signal_ratio_summer': 'flex_signal_ratio_summer',
    'flex_GSRU': 'flex_GSRU',
    'flex_GSRI': 'flex_GSRI',
    'flex_GSR': 'flex_GSR',
    'PV_own_consumption_direct': 'PV_own_consumption_direct',
    'PV_own_consumption_flex': 'PV_own_consumption_flex',
    'PV_own_consumption': 'PV_own_consumption',
    'EUI_self_sufficiency': 'EUI_self_sufficiency',
    'Batt_total_charge': 'Batt_total_charge',
    'Batt_total_discharge': 'Batt_total_discharge',
    'Batt_charge_losses': 'Batt_charge_losses',
    'Batt_discharge_losses': 'Batt_discharge_losses',
    'Batt_RTE': 'Batt_RTE',
    'Batt_FEC': 'Batt_FEC',
    'StatPAX': 'StatPAX',
    'mob_annual_milage_district': 'mob_annual_milage_district',
    'mob_annual_mileage_PAX': 'mob_annual_mileage_PAX',
    'UED_mob_el_target': 'UED_mob_el_target',
    'EUI_mob_fossile': 'EUI_mob_fossile',
    'EV_FEC': 'EV_FEC',
    'UED_mob_el_total': 'UED_mob_el_total',
    'UED_mob_el_other': 'UED_mob_el_other',
    'EUIev_el_total': 'EUIev_el_total',
    'Edhw_th': 'Edhw_th',
    'Edhw_el': 'Edhw_el',
    'Edhw_aux_el': 'Edhw_aux_el',
    'Edhw_1_th': 'Edhw_1_th',
    'Edhw_1_el': 'Edhw_1_el',
    'Edhw_1_aux_el': 'Edhw_1_aux_el',
    'Edhw_2_th': 'Edhw_2_th',
    'Edhw_2_el': 'Edhw_2_el',
    'Edhw_2_aux_el': 'Edhw_2_aux_el',
}

def fill_values(vars_obj: ExcelNamedVariables, data: dict[str, object], attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> None:
    for var_name, value in data.items():
        attr_name = attr_name_map.get(var_name)
        if attr_name is not None:
            setattr(vars_obj, attr_name, value)


def vars_to_dict(vars_obj: ExcelNamedVariables, attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> dict[str, object]:
    out: dict[str, object] = {}
    for var_name, attr_name in attr_name_map.items():
        out[var_name] = getattr(vars_obj, attr_name)
    return out

