"""Auto-generated schema bindings from schema_v1.10_3.xlsx.
Do not edit manually; regenerate from the schema workbook.
"""
from __future__ import annotations

SCHEMA_SOURCE = "schema_v1.10_3.xlsx"
SCHEMA_VERSION = "schema_v1.10_3"

class InputVars:
    """Auto-generated from Excel schema."""

    def __init__(self) -> None:
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
        self.transmittance_MW: object | None = None
        self.transmittance_Wm2: object | None = None  
        self.heat_capacity_effective_m2: object | None = None  
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
        self.fc_edusec: object | None = None
        self.fc_eduprim: object | None = None
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
        self.ACH_night_m3: object | None = None 
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
        self.usage_concurrency_winter_res: object | None = None
        self.usage_concurrency_winter_office: object | None = None
        self.usage_concurrency_winter_edusec: object | None = None
        self.usage_concurrency_winter_eduprim: object | None = None
        self.usage_concurrency_winter_retailfood: object | None = None
        self.usage_concurrency_winter_retailother: object | None = None
        self.usage_concurrency_winter_other: object | None = None
        self.usage_concurrency_summer_res: object | None = None
        self.usage_concurrency_summer_office: object | None = None
        self.usage_concurrency_summer_edusec: object | None = None
        self.usage_concurrency_summer_eduprim: object | None = None
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
        self.Plugloads_scale_res: object | None = None
        self.Plugloads_scale_office: object | None = None
        self.Plugloads_scale_schoolsec: object | None = None
        self.Plugloads_scale_schoolprim: object | None = None
        self.Plugloads_scale_retailfood: object | None = None
        self.Plugloads_scale_retailother: object | None = None
        self.Plugloads_scale_other: object | None = None
        self.density_NFApPers_residential: object | None = None
        self.density_NFApPers_office: object | None = None
        self.density_NFApPers_edu: object | None = None
        self.density_NFApPers_retail: object | None = None
        self.density_NFApPers_edu_rpim: object | None = None
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
        self.QHmax_room_m2: object | None = None  
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
        self.EV_mileage_res: object | None = None
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
        self.COMP_name_windows: object | None = None
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
        self.StatPAX_res: object | None = None
        self.StatPAX_office: object | None = None
        self.StatPAX_edusec: object | None = None
        self.StatPAX_eduprim: object | None = None
        self.StatPAX_retail: object | None = None
        self.StatPAX_retailother: object | None = None
        self.e_kWhm2a: object | None = None
        self.EV_charging_stations: object | None = None
        self.EV_charging_station_power: object | None = None

class UserInputVars:
    """Auto-generated from Excel schema."""

    def __init__(self) -> None:
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
        self.GFA_residential: object | None = None
        self.GFA_office: object | None = None
        self.GFA_schoolsec: object | None = None
        self.GFA_schoolprim: object | None = None
        self.GFA_retailfood: object | None = None
        self.GFA_retailother: object | None = None
        self.GFA_other: object | None = None
        self.NFA_to_GFA_ratio_residential: object | None = None
        self.NFA_to_GFA_ratio_office: object | None = None
        self.NFA_to_GFA_ratio_schoolsec: object | None = None
        self.NFA_to_GFA_ratio_schoolprim: object | None = None
        self.NFA_to_GFA_ratio_retailfood: object | None = None
        self.NFA_to_GFA_ratio_retailother: object | None = None
        self.NFA_to_GFA_ratio_other: object | None = None
        self.plot_area: object | None = None
        self.renovation_ratio_residential: object | None = None
        self.renovation_ratio_office: object | None = None
        self.renovation_ratio_schoolsec: object | None = None
        self.renovation_ratio_schoolprim: object | None = None
        self.renovation_ratio_retailfood: object | None = None
        self.renovation_ratio_retailother: object | None = None
        self.renovation_ratio_other: object | None = None
        self.building_count: object | None = None
        self.storey_count_avg: object | None = None
        self.rh_residential: object | None = None
        self.rh_office: object | None = None
        self.rh_schoolsec: object | None = None
        self.rh_schoolprim: object | None = None
        self.rh_retailfood: object | None = None
        self.rh_retailother: object | None = None
        self.rh_other: object | None = None
        self.rh_ceiling: object | None = None
        self.hull_ext_wall_wo_window_m2: object | None = None
        self.hull_roof_m2: object | None = None
        self.hull_fundament_m2: object | None = None
        self.hull_windows_north_m2: object | None = None
        self.hull_windows_east_m2: object | None = None
        self.hull_windows_south_m2: object | None = None
        self.hull_windows_west_m2: object | None = None
        self.hull_windows_horizontal_m2: object | None = None
        self.hull_transmittance_walls: object | None = None
        self.hull_transmittance_roof: object | None = None
        self.hull_transmittance_fundament: object | None = None
        self.hull_transmittance_windows_north: object | None = None
        self.hull_transmittance_windows_east: object | None = None
        self.hull_transmittance_windows_south: object | None = None
        self.hull_transmittance_windows_west: object | None = None
        self.hull_transmittance_windows_horizontal: object | None = None
        self.hull_transmittance_heatbridge: object | None = None
        self.heat_capacity_effective_m2: object | None = None 
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
        self.fc_edusec: object | None = None
        self.fc_eduprim: object | None = None
        self.fc_retailfood: object | None = None
        self.fc_retailother: object | None = None
        self.fc_other: object | None = None
        self.illuminance_min_residential: object | None = None
        self.illuminance_min_office: object | None = None
        self.illuminance_min_schoolsec: object | None = None
        self.illuminance_min_schoolprim: object | None = None
        self.illuminance_min_retailfood: object | None = None
        self.illuminance_min_retailother: object | None = None
        self.illuminance_min_other: object | None = None
        self.illuminance_efficiency_dirt: object | None = None
        self.illuminance_efficiency_glazing_ratio: object | None = None
        self.vent_air_tightness: object | None = None
        self.vent_tightness_ratio_blowerdoor_to_real: object | None = None
        self.vent_share_mechanical_residential: object | None = None
        self.vent_share_mechanical_office: object | None = None
        self.vent_share_mechanical_schoolsec: object | None = None
        self.vent_share_mechanical_schoolprim: object | None = None
        self.vent_share_mechanical_retailfood: object | None = None
        self.vent_share_mechanical_retailother: object | None = None
        self.vent_share_mechanical_other: object | None = None
        self.vent_night_residential: object | None = None
        self.vent_night_office: object | None = None
        self.vent_night_schoolsec: object | None = None
        self.vent_night_schoolprim: object | None = None
        self.vent_night_retailfood: object | None = None
        self.vent_night_retailother: object | None = None
        self.vent_night_other: object | None = None
        self.vent_ach_max_residential: object | None = None
        self.vent_ach_max_office: object | None = None
        self.vent_ach_max_schoolsec: object | None = None
        self.vent_ach_max_schoolprim: object | None = None
        self.vent_ach_max_retailfood: object | None = None
        self.vent_ach_max_retailother: object | None = None
        self.vent_ach_max_other: object | None = None
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
        self.usage_concurrency_winter_res: object | None = None
        self.usage_concurrency_winter_office: object | None = None
        self.usage_concurrency_winter_edusec: object | None = None
        self.usage_concurrency_winter_eduprim: object | None = None
        self.usage_concurrency_winter_retailfood: object | None = None
        self.usage_concurrency_winter_retailother: object | None = None
        self.usage_concurrency_winter_other: object | None = None
        self.usage_concurrency_summer_res: object | None = None
        self.usage_concurrency_summer_office: object | None = None
        self.usage_concurrency_summer_edusec: object | None = None
        self.usage_concurrency_summer_eduprim: object | None = None
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
        self.Plugloads_scale_res: object | None = None
        self.Plugloads_scale_office: object | None = None
        self.Plugloads_scale_schoolsec: object | None = None
        self.Plugloads_scale_schoolprim: object | None = None
        self.Plugloads_scale_retailfood: object | None = None
        self.Plugloads_scale_retailother: object | None = None
        self.Plugloads_scale_other: object | None = None
        self.density_NFApPers_residential: object | None = None
        self.density_NFApPers_office: object | None = None
        self.density_NFApPers_edu: object | None = None
        self.density_NFApPers_retail: object | None = None
        self.density_NFApPers_edu_rpim: object | None = None
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
        self.QHmax_room_m2: object | None = None
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
        self.QCmax_room_m2: object | None = None
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
        self.QC_aux_fc: object | None = None
        self.QC_aux_1el: object | None = None
        self.QC_aux_2th: object | None = None
        self.QC_aux_3el: object | None = None
        self.cool_th2_carrier_type: object | None = None
        self.Tsetcool_max: object | None = None
        self.DHW_Tmin: object | None = None
        self.DHW_Tmax_input: object | None = None
        self.DHW_1_share_residential: object | None = None
        self.DHW_1_share_office: object | None = None
        self.DHW_1_share_schoolsec: object | None = None
        self.DHW_1_share_schoolprim: object | None = None
        self.DHW_1_share_retailfood: object | None = None
        self.DHW_1_share_retailother: object | None = None
        self.DHW_1_share_other: object | None = None
        self.DHW_losses_1: object | None = None
        self.DHW_losses_2: object | None = None
        self.DHW_efficiency_distribution_1: object | None = None
        self.DHW_efficiency_distribution_2: object | None = None
        self.DHW_carriertype_1: object | None = None
        self.DHW_carriertype_2: object | None = None
        self.DHW_1_efficiency: object | None = None
        self.DHW_2_efficiency: object | None = None
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
        self.DHW_storage_env_temp_default: object | None = None
        self.PV_is_used: object | None = None
        self.PV_profile_name: object | None = None
        self.PV_scale: object | None = None
        self.PV_efficiency: object | None = None
        self.PV_m2_per_kWp: object | None = None
        self.FLEX_PV_is_used: object | None = None
        self.FLEX_is_used: object | None = None
        self.FLEX_signal_name: object | None = None
        self.FLEX_grid_maxpower_Wm2: object | None = None
        self.FLEX_is_used_for_plugloads: object | None = None
        self.FLEX_is_used_for_HVAC_min: object | None = None
        self.FLEX_is_used_for_ev_min: object | None = None
        self.flex_heat_dT: object | None = None
        self.FLEX_choice_heat_system: object | None = None
        self.flex_cool_dT: object | None = None
        self.FLEX_choice_cool_system: object | None = None
        self.Batt_is_used: object | None = None
        self.Batt_cap_kWh: object | None = None
        self.Batt_c_rate: object | None = None
        self.Batt_eff_factor_charge: object | None = None
        self.Batt_eff_factor_discharge: object | None = None
        self.Batt_self_discharge_rate: object | None = None
        self.Batt_SOC_init: object | None = None
        self.Batt_is_used_for_plugloads: object | None = None
        self.Batt_is_used_for_HVACminimum: object | None = None
        self.Batt_is_used_for_EV: object | None = None
        self.Batt_is_gridcharged: object | None = None
        self.flex_dhw_use: object | None = None
        self.Batt_is_not_used_during_signals: object | None = None
        self.mobility_is_included: object | None = None
        self.mobility_vehicle_count: object | None = None
        self.EV_share: object | None = None
        self.EV_demand_kWhpkm: object | None = None
        self.EV_battsize_kWh: object | None = None
        self.EV_self_discharge_per_week: object | None = None
        self.EV_soc_minimum: object | None = None
        self.EV_charging_efficiency: object | None = None
        self.EV_max_charging_power_ratio: object | None = None
        self.EV_soc_min_work: object | None = None
        self.EV_soc_min_retail: object | None = None
        self.moped_factor: object | None = None
        self.EV_share_constant_charging: object | None = None
        self.mob_pkm_factor: object | None = None
        self.EV_experimental_calculation: object | None = None
        self.EV_soc_min_ext: object | None = None
        self.EV_soc_min_discharge: object | None = None
        self.fossile_demand_kWhpkm: object | None = None
        self.ev_bidirectional_use: object | None = None
        self.GWP_walls_name: object | None = None
        self.COMP_name_windows: object | None = None
        self.GWP_roof_name: object | None = None
        self.GWP_ground_name: object | None = None
        self.GPW_ceilings_name: object | None = None
        self.GWP_general_name: object | None = None
        self.GWP_other_name: object | None = None
        self.GWP_ref_area_walls: object | None = None
        self.GWP_ref_area_windows: object | None = None
        self.GWP_ref_area_roof: object | None = None
        self.GWP_ref_area_fundament: object | None = None
        self.GWP_ref_area_ceilings: object | None = None
        self.GWP_pv_name: object | None = None
        self.GWP_boreholes_name: object | None = None
        self.borehole_count: object | None = None
        self.GWP_ventilation_name: object | None = None
        self.GWP_solarthermal_name: object | None = None
        self.GWP_battery_name: object | None = None
        self.GWP_storage_name: object | None = None
        self.GWP_tga_general_name: object | None = None
        self.GWP_tga_other_name: object | None = None
        self.GWP_direct_fossile: object | None = None
        self.GWP_direct_biogenic: object | None = None
        self.GWP_direct_biogenic_share: object | None = None
        self.GWP_direct_life: object | None = None
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
        self.rcp1_fossil: object | None = None
        self.rcp2_fossil: object | None = None
        self.rcp3_fossil: object | None = None
        self.fPE_grid_profile: object | None = None
        self.district_heating_conversion_profile: object | None = None
        self.fGHG_grid_profile: object | None = None
        self.fPE_flex_factor: object | None = None
        self.pe_conversion_factor_gasoline: object | None = None
        self.e_kWhm2a: object | None = None
        self.EV_charging_stations: object | None = None
        self.EV_charging_station_power: object | None = None

class OutputVars:
    """Auto-generated from Excel schema."""

    def __init__(self) -> None:
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

INPUT_ATTR_MAP: dict[str, str] = {
    "scenario_version": "scenario_version",
    "input_version_number": "input_version_number",
    "input_version_date": "input_version_date",
    "cfd_fPE": "cfd_fPE",
    "cfd_A": "cfd_A",
    "cfd_dx": "cfd_dx",
    "cfd_EUI": "cfd_EUI",
    "cfd_cutoff": "cfd_cutoff",
    "cfm_budget_residential": "cfm_budget_residential",
    "cfm_budget_office": "cfm_budget_office",
    "cfm_budget_school": "cfm_budget_school",
    "cfm_budget_retail": "cfm_budget_retail",
    "cfr_budget": "cfr_budget",
    "project_name": "project_name",
    "project_url": "project_url",
    "location_address": "location_address",
    "municipality_name": "municipality_name",
    "project_creation_date": "project_creation_date",
    "project_description": "project_description",
    "project_scenario_name": "project_scenario_name",
    "location_postcode": "location_postcode",
    "mobility_mode": "mobility_mode",
    "weather_name": "weather_name",
    "weather_index": "weather_index",
    "GFA_residential": "GFA_residential",
    "GFA_office": "GFA_office",
    "GFA_schoolsec": "GFA_schoolsec",
    "GFA_schoolprim": "GFA_schoolprim",
    "GFA_retailfood": "GFA_retailfood",
    "GFA_retailother": "GFA_retailother",
    "GFA_other": "GFA_other",
    "GFA_total": "GFA_total",
    "NFA_to_GFA_ratio_residential": "NFA_to_GFA_ratio_residential",
    "NFA_to_GFA_ratio_office": "NFA_to_GFA_ratio_office",
    "NFA_to_GFA_ratio_schoolsec": "NFA_to_GFA_ratio_schoolsec",
    "NFA_to_GFA_ratio_schoolprim": "NFA_to_GFA_ratio_schoolprim",
    "NFA_to_GFA_ratio_retailfood": "NFA_to_GFA_ratio_retailfood",
    "NFA_to_GFA_ratio_retailother": "NFA_to_GFA_ratio_retailother",
    "NFA_to_GFA_ratio_other": "NFA_to_GFA_ratio_other",
    "NFA_to_GFA_ratio": "NFA_to_GFA_ratio",
    "NFA_residential": "NFA_residential",
    "NFA_office": "NFA_office",
    "NFA_schoolsec": "NFA_schoolsec",
    "NFA_schoolprim": "NFA_schoolprim",
    "NFA_retailfood": "NFA_retailfood",
    "NFA_retailother": "NFA_retailother",
    "NFA_other": "NFA_other",
    "NFA_total": "NFA_total",
    "per_NFA": "per_NFA",
    "plot_area": "plot_area",
    "FSI": "FSI",
    "renovation_ratio_residential": "renovation_ratio_residential",
    "renovation_ratio_office": "renovation_ratio_office",
    "renovation_ratio_schoolsec": "renovation_ratio_schoolsec",
    "renovation_ratio_schoolprim": "renovation_ratio_schoolprim",
    "renovation_ratio_retailfood": "renovation_ratio_retailfood",
    "renovation_ratio_retailother": "renovation_ratio_retailother",
    "renovation_ratio_other": "renovation_ratio_other",
    "renovation_share": "renovation_share",
    "building_count": "building_count",
    "storey_count_avg": "storey_count_avg",
    "rh_residential": "rh_residential",
    "rh_office": "rh_office",
    "rh_schoolsec": "rh_schoolsec",
    "rh_schoolprim": "rh_schoolprim",
    "rh_retailfood": "rh_retailfood",
    "rh_retailother": "rh_retailother",
    "rh_other": "rh_other",
    "rh_avg": "rh_avg",
    "NFV_total": "NFV_total",
    "NFV_u": "NFV_u",
    "NFV_c": "NFV_c",
    "rh_ceiling": "rh_ceiling",
    "GFV": "GFV",
    "hull_ext_wall_wo_window_m2": "hull_ext_wall_wo_window_m2",
    "hull_roof_m2": "hull_roof_m2",
    "hull_fundament_m2": "hull_fundament_m2",
    "hull_windows_north_m2": "hull_windows_north_m2",
    "hull_windows_east_m2": "hull_windows_east_m2",
    "hull_windows_south_m2": "hull_windows_south_m2",
    "hull_windows_west_m2": "hull_windows_west_m2",
    "hull_windows_horizontal_m2": "hull_windows_horizontal_m2",
    "hull_window_m2": "hull_window_m2",
    "hull_fenestration_rate": "hull_fenestration_rate",
    "hull_m2": "hull_m2",
    "lc": "lc",
    "hull_transmittance_walls": "hull_transmittance_walls",
    "hull_transmittance_roof": "hull_transmittance_roof",
    "hull_transmittance_fundament": "hull_transmittance_fundament",
    "hull_transmittance_windows_north": "hull_transmittance_windows_north",
    "hull_transmittance_windows_east": "hull_transmittance_windows_east",
    "hull_transmittance_windows_south": "hull_transmittance_windows_south",
    "hull_transmittance_windows_west": "hull_transmittance_windows_west",
    "hull_transmittance_windows_horizontal": "hull_transmittance_windows_horizontal",
    "hull_transmittance_heatbridge": "hull_transmittance_heatbridge",
    "transmittance_MW": "transmittance_MW",
    "transmittance_Wm²": "transmittance_Wm",
    "heat_capacity_effective_m²": "heat_capacity_effective_m",
    "heat_cap_eff_uncooled_m2": "heat_cap_eff_uncooled_m2",
    "heat_cap_eff_cooled_m2": "heat_cap_eff_cooled_m2",
    "window_total_transmittance_north": "window_total_transmittance_north",
    "window_total_transmittance_east": "window_total_transmittance_east",
    "window_total_transmittance_south": "window_total_transmittance_south",
    "window_total_transmittance_west": "window_total_transmittance_west",
    "window_total_transmittance_horizontal": "window_total_transmittance_horizontal",
    "window_irradiation_factor_winter_north": "window_irradiation_factor_winter_north",
    "window_irradiation_factor_winter_east": "window_irradiation_factor_winter_east",
    "window_irradiation_factor_winter_south": "window_irradiation_factor_winter_south",
    "window_irradiation_factor_winter_west": "window_irradiation_factor_winter_west",
    "window_irradiation_factor_winter_horizontal": "window_irradiation_factor_winter_horizontal",
    "window_irradiation_factor_summer_north": "window_irradiation_factor_summer_north",
    "window_irradiation_factor_summer_east": "window_irradiation_factor_summer_east",
    "window_irradiation_factor_summer_south": "window_irradiation_factor_summer_south",
    "window_irradiation_factor_summer_west": "window_irradiation_factor_summer_west",
    "window_irradiation_factor_summer_horizontal": "window_irradiation_factor_summer_horizontal",
    "irradiation_opaque_surcharge": "irradiation_opaque_surcharge",
    "fc_residential": "fc_residential",
    "fc_office": "fc_office",
    "fc_edusec": "fc_edusec",
    "fc_eduprim": "fc_eduprim",
    "fc_retailfood": "fc_retailfood",
    "fc_retailother": "fc_retailother",
    "fc_other": "fc_other",
    "fc_u": "fc_u",
    "fc_c": "fc_c",
    "illuminance_min_residential": "illuminance_min_residential",
    "illuminance_min_office": "illuminance_min_office",
    "illuminance_min_schoolsec": "illuminance_min_schoolsec",
    "illuminance_min_schoolprim": "illuminance_min_schoolprim",
    "illuminance_min_retailfood": "illuminance_min_retailfood",
    "illuminance_min_retailother": "illuminance_min_retailother",
    "illuminance_min_other": "illuminance_min_other",
    "QS_max_shading_u": "QS_max_shading_u",
    "QS_max_shading_c": "QS_max_shading_c",
    "illuminance_efficiency_dirt": "illuminance_efficiency_dirt",
    "illuminance_efficiency_glazing_ratio": "illuminance_efficiency_glazing_ratio",
    "mob_shading_factor_u": "mob_shading_factor_u",
    "mob_shading_factor_c": "mob_shading_factor_c",
    "vent_air_tightness": "vent_air_tightness",
    "vent_tightness_ratio_blowerdoor_to_real": "vent_tightness_ratio_blowerdoor_to_real",
    "vent_infiltration_ACH": "vent_infiltration_ACH",
    "vent_share_mechanical_residential": "vent_share_mechanical_residential",
    "vent_share_mechanical_office": "vent_share_mechanical_office",
    "vent_share_mechanical_schoolsec": "vent_share_mechanical_schoolsec",
    "vent_share_mechanical_schoolprim": "vent_share_mechanical_schoolprim",
    "vent_share_mechanical_retailfood": "vent_share_mechanical_retailfood",
    "vent_share_mechanical_retailother": "vent_share_mechanical_retailother",
    "vent_share_mechanical_other": "vent_share_mechanical_other",
    "NFA_windowvent": "NFA_windowvent",
    "NFV_windowvent": "NFV_windowvent",
    "NFA_mechvent": "NFA_mechvent",
    "NFV_mechvent": "NFV_mechvent",
    "vent_night_residential": "vent_night_residential",
    "vent_night_office": "vent_night_office",
    "vent_night_schoolsec": "vent_night_schoolsec",
    "vent_night_schoolprim": "vent_night_schoolprim",
    "vent_night_retailfood": "vent_night_retailfood",
    "vent_night_retailother": "vent_night_retailother",
    "vent_night_other": "vent_night_other",
    "ACH_night_m³": "ACH_night_m",
    "vent_ach_max_residential": "vent_ach_max_residential",
    "vent_ach_max_office": "vent_ach_max_office",
    "vent_ach_max_schoolsec": "vent_ach_max_schoolsec",
    "vent_ach_max_schoolprim": "vent_ach_max_schoolprim",
    "vent_ach_max_retailfood": "vent_ach_max_retailfood",
    "vent_ach_max_retailother": "vent_ach_max_retailother",
    "vent_ach_max_other": "vent_ach_max_other",
    "vent_scale_residential": "vent_scale_residential",
    "vent_scale_office": "vent_scale_office",
    "vent_scale_school_sec": "vent_scale_school_sec",
    "vent_scale_school_prim": "vent_scale_school_prim",
    "vent_scale_supermarket": "vent_scale_supermarket",
    "vent_scale_retail": "vent_scale_retail",
    "vent_scale_other": "vent_scale_other",
    "Ev_scale_residential": "Ev_scale_residential",
    "Ev_scale_office": "Ev_scale_office",
    "Ev_scale_school_sec": "Ev_scale_school_sec",
    "Ev_scale_school_prim": "Ev_scale_school_prim",
    "Ev_scale_retail_food": "Ev_scale_retail_food",
    "Ev_scale_retail_other": "Ev_scale_retail_other",
    "Ev_scale_other": "Ev_scale_other",
    "vent_heat_recovery_winter_residential": "vent_heat_recovery_winter_residential",
    "vent_heat_recovery_winter_office": "vent_heat_recovery_winter_office",
    "vent_heat_recovery_winter_schoolsec": "vent_heat_recovery_winter_schoolsec",
    "vent_heat_recovery_winter_schoolprim": "vent_heat_recovery_winter_schoolprim",
    "vent_heat_recovery_winter_retailfood": "vent_heat_recovery_winter_retailfood",
    "vent_heat_recovery_winter_retailother": "vent_heat_recovery_winter_retailother",
    "vent_heat_recovery_winter_other": "vent_heat_recovery_winter_other",
    "vent_heat_recovery_summer_residential": "vent_heat_recovery_summer_residential",
    "vent_heat_recovery_summer_office": "vent_heat_recovery_summer_office",
    "vent_heat_recovery_summer_schoolsec": "vent_heat_recovery_summer_schoolsec",
    "vent_heat_recovery_summer_schoolprim": "vent_heat_recovery_summer_schoolprim",
    "vent_heat_recovery_summer_retailfood": "vent_heat_recovery_summer_retailfood",
    "vent_heat_recovery_summer_retailother": "vent_heat_recovery_summer_retailother",
    "vent_heat_recovery_summer_other": "vent_heat_recovery_summer_other",
    "Vent_share_window_uncooled": "Vent_share_window_uncooled",
    "Vent_share_window_cooled": "Vent_share_window_cooled",
    "Vent_share_mech_uncooled": "Vent_share_mech_uncooled",
    "Vent_share_mech_cooled": "Vent_share_mech_cooled",
    "test_NFV_shares": "test_NFV_shares",
    "usage_concurrency_winter_res": "usage_concurrency_winter_res",
    "usage_concurrency_winter_office": "usage_concurrency_winter_office",
    "usage_concurrency_winter_edusec": "usage_concurrency_winter_edusec",
    "usage_concurrency_winter_eduprim": "usage_concurrency_winter_eduprim",
    "usage_concurrency_winter_retailfood": "usage_concurrency_winter_retailfood",
    "usage_concurrency_winter_retailother": "usage_concurrency_winter_retailother",
    "usage_concurrency_winter_other": "usage_concurrency_winter_other",
    "usage_concurrency_summer_res": "usage_concurrency_summer_res",
    "usage_concurrency_summer_office": "usage_concurrency_summer_office",
    "usage_concurrency_summer_edusec": "usage_concurrency_summer_edusec",
    "usage_concurrency_summer_eduprim": "usage_concurrency_summer_eduprim",
    "usage_concurrency_summer_retailfood": "usage_concurrency_summer_retailfood",
    "usage_concurrency_summer_retailother": "usage_concurrency_summer_retailother",
    "usage_concurrency_summer_other": "usage_concurrency_summer_other",
    "DHW_demand_residential_kWhm2": "DHW_demand_residential_kWhm2",
    "DHW_demand_office_kWhm2": "DHW_demand_office_kWhm2",
    "DHW_demand_schoolsec_kWhm2": "DHW_demand_schoolsec_kWhm2",
    "DHW_demand_schoolprim_kWhm2": "DHW_demand_schoolprim_kWhm2",
    "DHW_demand_retailfood_kWhm2": "DHW_demand_retailfood_kWhm2",
    "DHW_demand_retailother_kWhm2": "DHW_demand_retailother_kWhm2",
    "DHW_demand_other_kWhm2": "DHW_demand_other_kWhm2",
    "aux_el_demand_residential_kWhm2": "aux_el_demand_residential_kWhm2",
    "aux_el_demand_office_kWhm2": "aux_el_demand_office_kWhm2",
    "aux_el_demand_schoolsec_kWhm2": "aux_el_demand_schoolsec_kWhm2",
    "aux_el_demand_schoolprim_kWhm2": "aux_el_demand_schoolprim_kWhm2",
    "aux_el_demand_retailfood_kWhm2": "aux_el_demand_retailfood_kWhm2",
    "aux_el_demand_retailother_kWhm2": "aux_el_demand_retailother_kWhm2",
    "aux_el_demand_other_kWhm2": "aux_el_demand_other_kWhm2",
    "Plugloads_scale_res": "Plugloads_scale_res",
    "Plugloads_scale_office": "Plugloads_scale_office",
    "Plugloads_scale_schoolsec": "Plugloads_scale_schoolsec",
    "Plugloads_scale_schoolprim": "Plugloads_scale_schoolprim",
    "Plugloads_scale_retailfood": "Plugloads_scale_retailfood",
    "Plugloads_scale_retailother": "Plugloads_scale_retailother",
    "Plugloads_scale_other": "Plugloads_scale_other",
    "density_NFApPers_residential": "density_NFApPers_residential",
    "density_NFApPers_office": "density_NFApPers_office",
    "density_NFApPers_edu": "density_NFApPers_edu",
    "density_NFApPers_retail": "density_NFApPers_retail",
    "density_NFApPers_edu_rpim": "density_NFApPers_edu_rpim",
    "density_NFApPers_retail_other": "density_NFApPers_retail_other",
    "mob_simultaneity_edu": "mob_simultaneity_edu",
    "mob_simultaneity_retail": "mob_simultaneity_retail",
    "mob_simultaneity_office": "mob_simultaneity_office",
    "mob_motorization_perNFA_residential": "mob_motorization_perNFA_residential",
    "mob_motorization_perNFA_work": "mob_motorization_perNFA_work",
    "mob_motorization_perNFA_retail": "mob_motorization_perNFA_retail",
    "Plight_max_office": "Plight_max_office",
    "Plight_max_schoolsec": "Plight_max_schoolsec",
    "Plight_max_schoolprim": "Plight_max_schoolprim",
    "Plight_min_office": "Plight_min_office",
    "Plight_min_schoolsec": "Plight_min_schoolsec",
    "Plight_min_schoolprim": "Plight_min_schoolprim",
    "lighting_factor_office": "lighting_factor_office",
    "lighting_factor_schoolsec": "lighting_factor_schoolsec",
    "lighting_factor_schoolprim": "lighting_factor_schoolprim",
    "lighting_factor_retailfood": "lighting_factor_retailfood",
    "lighting_factor_retailother": "lighting_factor_retailother",
    "lighting_factor_other": "lighting_factor_other",
    "Daylightcoefficient_office": "Daylightcoefficient_office",
    "Daylightcoefficient_schoolsec": "Daylightcoefficient_schoolsec",
    "Daylightcoefficient_schoolprim": "Daylightcoefficient_schoolprim",
    "daylightcontr_office": "daylightcontr_office",
    "daylightcontr_schoolsec": "daylightcontr_schoolsec",
    "daylightcontr_schoolprim": "daylightcontr_schoolprim",
    "heating_month1": "heating_month1",
    "heating_month2": "heating_month2",
    "heating_month3": "heating_month3",
    "heating_month4": "heating_month4",
    "heating_month5": "heating_month5",
    "heating_month6": "heating_month6",
    "heating_month7": "heating_month7",
    "heating_month8": "heating_month8",
    "heating_month9": "heating_month9",
    "heating_month10": "heating_month10",
    "heating_month11": "heating_month11",
    "heating_month12": "heating_month12",
    "QHmax_room_m²": "QHmax_room_m",
    "QHmax_room_MW": "QHmax_room_MW",
    "QHmax_1el_m²": "QHmax_1el_m",
    "QHmax_2th_m²": "QHmax_2th_m",
    "QHmax_3el_m²": "QHmax_3el_m",
    "QHmax_4th_m²": "QHmax_4th_m",
    "QH_distr_loss_1el": "QH_distr_loss_1el",
    "QH_distr_loss_2th": "QH_distr_loss_2th",
    "QH_distr_loss_3el": "QH_distr_loss_3el",
    "QH_distr_loss_4th": "QH_distr_loss_4th",
    "heat_cop_1el": "heat_cop_1el",
    "heat_cop_2th": "heat_cop_2th",
    "heat_cop_3el": "heat_cop_3el",
    "heat_cop_4th": "heat_cop_4th",
    "QH_generation_eff_1el": "QH_generation_eff_1el",
    "QH_generation_eff_2th": "QH_generation_eff_2th",
    "QH_generation_eff_3el": "QH_generation_eff_3el",
    "QH_generation_eff_4th": "QH_generation_eff_4th",
    "QH_aux_wasteheat": "QH_aux_wasteheat",
    "QH_aux_el_to_th_1el": "QH_aux_el_to_th_1el",
    "QH_aux_el_to_th_2th": "QH_aux_el_to_th_2th",
    "QH_aux_el_to_th_3el": "QH_aux_el_to_th_3el",
    "QH_aux_el_to_th_4th": "QH_aux_el_to_th_4th",
    "heat_th2_carrier_type": "heat_th2_carrier_type",
    "heat_th4_carrier_type": "heat_th4_carrier_type",
    "Tsetheat_min": "Tsetheat_min",
    "cooling_month1": "cooling_month1",
    "cooling_month2": "cooling_month2",
    "cooling_month3": "cooling_month3",
    "cooling_month4": "cooling_month4",
    "cooling_month5": "cooling_month5",
    "cooling_month6": "cooling_month6",
    "cooling_month7": "cooling_month7",
    "cooling_month8": "cooling_month8",
    "cooling_month9": "cooling_month9",
    "cooling_month10": "cooling_month10",
    "cooling_month11": "cooling_month11",
    "cooling_month12": "cooling_month12",
    "cool_share_residential": "cool_share_residential",
    "cool_share_office": "cool_share_office",
    "cool_share_schoolsec": "cool_share_schoolsec",
    "cool_share_schoolprim": "cool_share_schoolprim",
    "cool_share_retailfood": "cool_share_retailfood",
    "cool_share_retailother": "cool_share_retailother",
    "cool_share_other": "cool_share_other",
    "NFA_cooled": "NFA_cooled",
    "NFAfrac_c": "NFAfrac_c",
    "NFAfrac_u": "NFAfrac_u",
    "QCmax_room_m2": "QCmax_room_m2",
    "QCmax_room_MW": "QCmax_room_MW",
    "QCmax_freecooling": "QCmax_freecooling",
    "QCmax_1el": "QCmax_1el",
    "QCmax_2th": "QCmax_2th",
    "QCmax_3el": "QCmax_3el",
    "QC_distr_losses_1el": "QC_distr_losses_1el",
    "QC_distr_losses_2th": "QC_distr_losses_2th",
    "QC_distr_losses_3el": "QC_distr_losses_3el",
    "cool_cop_1el": "cool_cop_1el",
    "cool_cop_2th": "cool_cop_2th",
    "cool_cop_3el": "cool_cop_3el",
    "QC_to_EC_1": "QC_to_EC_1",
    "QC_generation_eff_2th": "QC_generation_eff_2th",
    "QC_to_EC_3": "QC_to_EC_3",
    "QC_aux_fc": "QC_aux_fc",
    "QC_aux_1el": "QC_aux_1el",
    "QC_aux_2th": "QC_aux_2th",
    "QC_aux_3el": "QC_aux_3el",
    "cool_th2_carrier_type": "cool_th2_carrier_type",
    "Tsetcool_max": "Tsetcool_max",
    "DHW_Tmin": "DHW_Tmin",
    "DHW_Tmax_input": "DHW_Tmax_input",
    "DHW_Tmax": "DHW_Tmax",
    "DHW_1_share_residential": "DHW_1_share_residential",
    "DHW_1_share_office": "DHW_1_share_office",
    "DHW_1_share_schoolsec": "DHW_1_share_schoolsec",
    "DHW_1_share_schoolprim": "DHW_1_share_schoolprim",
    "DHW_1_share_retailfood": "DHW_1_share_retailfood",
    "DHW_1_share_retailother": "DHW_1_share_retailother",
    "DHW_1_share_other": "DHW_1_share_other",
    "DHW_storage_1_liter": "DHW_storage_1_liter",
    "DHW_storage_2_liter": "DHW_storage_2_liter",
    "DHW_1_is_used": "DHW_1_is_used",
    "DHW_2_is_used": "DHW_2_is_used",
    "DHW_thermal_power_1_kW": "DHW_thermal_power_1_kW",
    "DHW_losses_1": "DHW_losses_1",
    "DHW_losses_2": "DHW_losses_2",
    "DHW_efficiency_distribution_1": "DHW_efficiency_distribution_1",
    "DHW_efficiency_distribution_2": "DHW_efficiency_distribution_2",
    "DHW_1_incl_distribution_factor": "DHW_1_incl_distribution_factor",
    "DHW_2_incl_distribution_factor": "DHW_2_incl_distribution_factor",
    "DHW_carriertype_1": "DHW_carriertype_1",
    "DHW_1_is_electric": "DHW_1_is_electric",
    "DHW_carriertype_2": "DHW_carriertype_2",
    "DHW_2_is_electric": "DHW_2_is_electric",
    "DHW_1_efficiency": "DHW_1_efficiency",
    "DHW_2_efficiency": "DHW_2_efficiency",
    "DHW_conversion_1": "DHW_conversion_1",
    "DHW_conversion_2": "DHW_conversion_2",
    "DHW_1_el_aux": "DHW_1_el_aux",
    "DHW_2_el_aux": "DHW_2_el_aux",
    "DHW_occupancy_residential": "DHW_occupancy_residential",
    "DHW_occupancy_office": "DHW_occupancy_office",
    "DHW_occupancy_schoolsec": "DHW_occupancy_schoolsec",
    "DHW_occupancy_schoolprim": "DHW_occupancy_schoolprim",
    "DHW_occupancy_retailfood": "DHW_occupancy_retailfood",
    "DHW_occupancy_retailother": "DHW_occupancy_retailother",
    "DHW_occupancy_other": "DHW_occupancy_other",
    "DHW_concurrency_residential": "DHW_concurrency_residential",
    "DHW_concurrency_office": "DHW_concurrency_office",
    "DHW_concurrency_schoolsec": "DHW_concurrency_schoolsec",
    "DHW_concurrency_schoolprim": "DHW_concurrency_schoolprim",
    "DHW_concurrency_retailfood": "DHW_concurrency_retailfood",
    "DHW_concurrency_retailother": "DHW_concurrency_retailother",
    "DHW_concurrency_other": "DHW_concurrency_other",
    "DHW_storage_liter_pPerson": "DHW_storage_liter_pPerson",
    "DHW_thermal_power_pPerson": "DHW_thermal_power_pPerson",
    "DHW_thermal_power_Wpl": "DHW_thermal_power_Wpl",
    "DHW_storage_env_temp_default": "DHW_storage_env_temp_default",
    "PV_is_used": "PV_is_used",
    "PV_profile_name": "PV_profile_name",
    "PV_id": "PV_id",
    "PV_scale": "PV_scale",
    "PV_efficiency": "PV_efficiency",
    "PV_m2_per_kWp": "PV_m2_per_kWp",
    "PV_kWp": "PV_kWp",
    "PV_module_area": "PV_module_area",
    "FLEX_PV_is_used": "FLEX_PV_is_used",
    "FLEX_is_used": "FLEX_is_used",
    "FLEX_signal_name": "FLEX_signal_name",
    "FLEX_signal_ID": "FLEX_signal_ID",
    "FLEX_grid_maxpower_Wm2": "FLEX_grid_maxpower_Wm2",
    "FLEX_is_used_for_plugloads": "FLEX_is_used_for_plugloads",
    "FLEX_is_used_for_HVAC_min": "FLEX_is_used_for_HVAC_min",
    "FLEX_is_used_for_ev_min": "FLEX_is_used_for_ev_min",
    "flex_heat_dT": "flex_heat_dT",
    "Tsetheat_flex": "Tsetheat_flex",
    "FLEX_choice_heat_system": "FLEX_choice_heat_system",
    "FLEX_heat1_use": "FLEX_heat1_use",
    "FLEX_heat3_use": "FLEX_heat3_use",
    "flex_cool_dT": "flex_cool_dT",
    "Tsetcool_flex": "Tsetcool_flex",
    "FLEX_choice_cool_system": "FLEX_choice_cool_system",
    "FLEX_cool1_use": "FLEX_cool1_use",
    "FLEX_cool3_use": "FLEX_cool3_use",
    "Batt_is_used": "Batt_is_used",
    "Batt_cap_kWh": "Batt_cap_kWh",
    "Batt_cap_Wh_per_NFA": "Batt_cap_Wh_per_NFA",
    "Batt_c_rate": "Batt_c_rate",
    "Batt_max_power_specific": "Batt_max_power_specific",
    "Batt_eff_factor_charge": "Batt_eff_factor_charge",
    "Batt_eff_factor_discharge": "Batt_eff_factor_discharge",
    "Batt_self_discharge_rate": "Batt_self_discharge_rate",
    "Batt_auto_discharge_factor": "Batt_auto_discharge_factor",
    "Batt_SOC_init": "Batt_SOC_init",
    "Batt_is_used_for_plugloads": "Batt_is_used_for_plugloads",
    "Batt_is_used_for_HVACminimum": "Batt_is_used_for_HVACminimum",
    "Batt_is_used_for_EV": "Batt_is_used_for_EV",
    "Batt_is_gridcharged": "Batt_is_gridcharged",
    "flex_dhw_use": "flex_dhw_use",
    "flex_Signals_selected_column": "flex_Signals_selected_column",
    "Batt_is_not_used_during_signals": "Batt_is_not_used_during_signals",
    "mobility_is_included": "mobility_is_included",
    "mobility_region": "mobility_region",
    "mobshare_residential": "mobshare_residential",
    "mobshare_office": "mobshare_office",
    "mobshare_school": "mobshare_school",
    "mobshare_retail": "mobshare_retail",
    "pkm_pedestrian": "pkm_pedestrian",
    "pkm_bike": "pkm_bike",
    "pkm_mofa": "pkm_mofa",
    "pkm_car_driver": "pkm_car_driver",
    "pkm_car_passenger": "pkm_car_passenger",
    "pkm_bus": "pkm_bus",
    "pkm_tram_metro": "pkm_tram_metro",
    "pkm_train": "pkm_train",
    "pkm_distancebus": "pkm_distancebus",
    "mobility_vehicle_count": "mobility_vehicle_count",
    "EV_share": "EV_share",
    "EV_demand_kWhpkm": "EV_demand_kWhpkm",
    "EV_battsize_kWh": "EV_battsize_kWh",
    "EV_storage_total_kWh": "EV_storage_total_kWh",
    "EV_self_discharge_per_week": "EV_self_discharge_per_week",
    "EV_selfdischarge_per_h": "EV_selfdischarge_per_h",
    "EV_soc_minimum": "EV_soc_minimum",
    "EV_charging_efficiency": "EV_charging_efficiency",
    "EV_charging_losses_surcharge_factor": "EV_charging_losses_surcharge_factor",
    "EV_max_charging_power_ratio": "EV_max_charging_power_ratio",
    "EV_soc_min_work": "EV_soc_min_work",
    "EV_soc_min_retail": "EV_soc_min_retail",
    "moped_factor": "moped_factor",
    "EV_share_constant_charging": "EV_share_constant_charging",
    "mob_pkm_factor": "mob_pkm_factor",
    "EV_experimental_calculation": "EV_experimental_calculation",
    "EV_mileage_res": "EV_mileage_res",
    "EV_mileage_work": "EV_mileage_work",
    "EV_mileage_retail": "EV_mileage_retail",
    "EV_soc_min_ext": "EV_soc_min_ext",
    "EV_soc_min_discharge": "EV_soc_min_discharge",
    "fossile_demand_kWhpkm": "fossile_demand_kWhpkm",
    "EV_count_residential": "EV_count_residential",
    "EV_count_work": "EV_count_work",
    "EV_count_retail": "EV_count_retail",
    "ev_bidirectional_use": "ev_bidirectional_use",
    "GWP_walls_name": "GWP_walls_name",
    "COMP_name_windows": "COMP_name_windows",
    "GWP_roof_name": "GWP_roof_name",
    "GWP_ground_name": "GWP_ground_name",
    "GPW_ceilings_name": "GPW_ceilings_name",
    "COMP_name_terrace": "COMP_name_terrace",
    "COMP_name_basement_ceiling": "COMP_name_basement_ceiling",
    "COMP_name_fundament": "COMP_name_fundament",
    "COMP_name_ceil_to_air": "COMP_name_ceil_to_air",
    "COMP_name_wall_earth_contacted": "COMP_name_wall_earth_contacted",
    "COMP_name_internal_wall_load": "COMP_name_internal_wall_load",
    "COMP_name_internal_wall_nonload": "COMP_name_internal_wall_nonload",
    "COMP_name_ceiling_topfloor": "COMP_name_ceiling_topfloor",
    "COMP_name_wall_ec_unheated": "COMP_name_wall_ec_unheated",
    "COMP_name_basement_floor_unheated": "COMP_name_basement_floor_unheated",
    "COMP_name_columns": "COMP_name_columns",
    "COMP_name_internal_wall_unheated": "COMP_name_internal_wall_unheated",
    "COMP_name_unheated_horizontal": "COMP_name_unheated_horizontal",
    "COMP_name_balconies": "COMP_name_balconies",
    "COMP_name_windowframe": "COMP_name_windowframe",
    "COMP_name_windowglazing": "COMP_name_windowglazing",
    "COMP_name_other": "COMP_name_other",
    "GWP_general_name": "GWP_general_name",
    "GWP_other_name": "GWP_other_name",
    "GWP_ref_area_walls": "GWP_ref_area_walls",
    "GWP_ref_area_windows": "GWP_ref_area_windows",
    "GWP_ref_area_roof": "GWP_ref_area_roof",
    "GWP_ref_area_fundament": "GWP_ref_area_fundament",
    "GWP_ref_area_ceilings": "GWP_ref_area_ceilings",
    "COMP_area_terrace": "COMP_area_terrace",
    "COMP_area_basement_ceiling": "COMP_area_basement_ceiling",
    "COMP_area_fundament": "COMP_area_fundament",
    "COMP_area_ceil_to_air": "COMP_area_ceil_to_air",
    "COMP_area_wall_earth_contacted": "COMP_area_wall_earth_contacted",
    "COMP_area_internal_wall_load": "COMP_area_internal_wall_load",
    "COMP_area_internal_wall_nonload": "COMP_area_internal_wall_nonload",
    "COMP_area_ceiling_topfloor": "COMP_area_ceiling_topfloor",
    "COMP_area_wall_ec_unheated": "COMP_area_wall_ec_unheated",
    "COMP_area_basement_floor_unheated": "COMP_area_basement_floor_unheated",
    "COMP_area_columns": "COMP_area_columns",
    "COMP_area_internal_wall_unheated": "COMP_area_internal_wall_unheated",
    "COMP_area_unheated_horizontal": "COMP_area_unheated_horizontal",
    "COMP_area_balconies": "COMP_area_balconies",
    "COMP_area_windowframe": "COMP_area_windowframe",
    "COMP_area_windowglazing": "COMP_area_windowglazing",
    "GWP_refratio_walls": "GWP_refratio_walls",
    "GWP_refratio_windows": "GWP_refratio_windows",
    "GWP_refratio_roof": "GWP_refratio_roof",
    "GWP_refratio_fundament": "GWP_refratio_fundament",
    "GWP_refratio_ceilings": "GWP_refratio_ceilings",
    "GWP_pv_name": "GWP_pv_name",
    "GWP_refratio_pv": "GWP_refratio_pv",
    "GWP_boreholes_name": "GWP_boreholes_name",
    "borehole_count": "borehole_count",
    "GWP_ventilation_name": "GWP_ventilation_name",
    "GWP_solarthermal_name": "GWP_solarthermal_name",
    "GWP_battery_name": "GWP_battery_name",
    "GWP_storage_name": "GWP_storage_name",
    "GWP_tga_general_name": "GWP_tga_general_name",
    "GWP_tga_other_name": "GWP_tga_other_name",
    "GWP_refratio_boreholes": "GWP_refratio_boreholes",
    "GWP_direct_fossile": "GWP_direct_fossile",
    "GWP_direct_biogenic": "GWP_direct_biogenic",
    "GWP_direct_biogenic_share": "GWP_direct_biogenic_share",
    "GWP_direct_life": "GWP_direct_life",
    "GWP_miv_count_ev": "GWP_miv_count_ev",
    "GWP_miv_count_fossile": "GWP_miv_count_fossile",
    "GWP_mobility_construction_fossil": "GWP_mobility_construction_fossil",
    "GWP_mobility_construction_ev": "GWP_mobility_construction_ev",
    "GHG_LCA_timeframe_years": "GHG_LCA_timeframe_years",
    "GWP_mobility_moped_gpPKm": "GWP_mobility_moped_gpPKm",
    "GWP_mobility_car_gpPKm": "GWP_mobility_car_gpPKm",
    "year_rcp0": "year_rcp0",
    "year_rcp1": "year_rcp1",
    "year_rcp2": "year_rcp2",
    "year_rcp3": "year_rcp3",
    "grid_rcp1": "grid_rcp1",
    "grid_rcp2": "grid_rcp2",
    "grid_rcp3": "grid_rcp3",
    "rcp1_renewable": "rcp1_renewable",
    "rcp2_renewable": "rcp2_renewable",
    "rcp3_renewable": "rcp3_renewable",
    "rcp1_dh": "rcp1_dh",
    "rcp2_dh": "rcp2_dh",
    "rcp3_dh": "rcp3_dh",
    "rcp1_fossil": "rcp1_fossil",
    "rcp2_fossil": "rcp2_fossil",
    "rcp3_fossil": "rcp3_fossil",
    "GWP_rcpi_grid": "GWP_rcpi_grid",
    "GWP_rcpi_grid_substition": "GWP_rcpi_grid_substition",
    "GWP_rcpi_district_heating": "GWP_rcpi_district_heating",
    "GWP_rcpi_fossil": "GWP_rcpi_fossil",
    "GWP_rcpi_natural_gas": "GWP_rcpi_natural_gas",
    "GWP_rcpi_biomass": "GWP_rcpi_biomass",
    "GWP_rcpi_mob_fossile": "GWP_rcpi_mob_fossile",
    "GWP_rcpi_renewable": "GWP_rcpi_renewable",
    "fPE_grid_profile": "fPE_grid_profile",
    "district_heating_conversion_profile": "district_heating_conversion_profile",
    "fGHG_grid_profile": "fGHG_grid_profile",
    "fPE_grid_column": "fPE_grid_column",
    "fGHG_grid_column": "fGHG_grid_column",
    "heat_th2_is_dh": "heat_th2_is_dh",
    "heat_th4_is_dh": "heat_th4_is_dh",
    "cool_th2_is_dh": "cool_th2_is_dh",
    "dhw1_is_dh": "dhw1_is_dh",
    "dhw2_is_dh": "dhw2_is_dh",
    "heat_th2_is_ng": "heat_th2_is_ng",
    "heat_th4_is_ng": "heat_th4_is_ng",
    "cool_th2_is_ng": "cool_th2_is_ng",
    "dhw1_is_ng": "dhw1_is_ng",
    "dhw2_is_ng": "dhw2_is_ng",
    "heat_th2_is_bio": "heat_th2_is_bio",
    "heat_th4_is_bio": "heat_th4_is_bio",
    "cool_th2_is_bio": "cool_th2_is_bio",
    "dhw1_is_bio": "dhw1_is_bio",
    "dhw2_is_bio": "dhw2_is_bio",
    "heat_th2_is_other": "heat_th2_is_other",
    "heat_th4_is_other": "heat_th4_is_other",
    "cool_th2_is_other": "cool_th2_is_other",
    "dhw1_is_other": "dhw1_is_other",
    "dhw2_is_other": "dhw2_is_other",
    "fPE_flex_factor": "fPE_flex_factor",
    "pe_conversion_factor_gasoline": "pe_conversion_factor_gasoline",
    "StatPAX_res": "StatPAX_res",
    "StatPAX_office": "StatPAX_office",
    "StatPAX_edusec": "StatPAX_edusec",
    "StatPAX_eduprim": "StatPAX_eduprim",
    "StatPAX_retail": "StatPAX_retail",
    "StatPAX_retailother": "StatPAX_retailother",
    "e_kWhm2a": "e_kWhm2a",
    "EV_charging_stations": "EV_charging_stations",
    "EV_charging_station_power": "EV_charging_station_power",
}

USER_INPUT_ATTR_MAP: dict[str, str] = {
    "cfd_fPE": "cfd_fPE",
    "cfd_A": "cfd_A",
    "cfd_dx": "cfd_dx",
    "cfd_EUI": "cfd_EUI",
    "cfd_cutoff": "cfd_cutoff",
    "cfm_budget_residential": "cfm_budget_residential",
    "cfm_budget_office": "cfm_budget_office",
    "cfm_budget_school": "cfm_budget_school",
    "cfm_budget_retail": "cfm_budget_retail",
    "cfr_budget": "cfr_budget",
    "project_name": "project_name",
    "project_url": "project_url",
    "location_address": "location_address",
    "municipality_name": "municipality_name",
    "project_creation_date": "project_creation_date",
    "project_description": "project_description",
    "project_scenario_name": "project_scenario_name",
    "location_postcode": "location_postcode",
    "mobility_mode": "mobility_mode",
    "weather_name": "weather_name",
    "GFA_residential": "GFA_residential",
    "GFA_office": "GFA_office",
    "GFA_schoolsec": "GFA_schoolsec",
    "GFA_schoolprim": "GFA_schoolprim",
    "GFA_retailfood": "GFA_retailfood",
    "GFA_retailother": "GFA_retailother",
    "GFA_other": "GFA_other",
    "NFA_to_GFA_ratio_residential": "NFA_to_GFA_ratio_residential",
    "NFA_to_GFA_ratio_office": "NFA_to_GFA_ratio_office",
    "NFA_to_GFA_ratio_schoolsec": "NFA_to_GFA_ratio_schoolsec",
    "NFA_to_GFA_ratio_schoolprim": "NFA_to_GFA_ratio_schoolprim",
    "NFA_to_GFA_ratio_retailfood": "NFA_to_GFA_ratio_retailfood",
    "NFA_to_GFA_ratio_retailother": "NFA_to_GFA_ratio_retailother",
    "NFA_to_GFA_ratio_other": "NFA_to_GFA_ratio_other",
    "plot_area": "plot_area",
    "renovation_ratio_residential": "renovation_ratio_residential",
    "renovation_ratio_office": "renovation_ratio_office",
    "renovation_ratio_schoolsec": "renovation_ratio_schoolsec",
    "renovation_ratio_schoolprim": "renovation_ratio_schoolprim",
    "renovation_ratio_retailfood": "renovation_ratio_retailfood",
    "renovation_ratio_retailother": "renovation_ratio_retailother",
    "renovation_ratio_other": "renovation_ratio_other",
    "building_count": "building_count",
    "storey_count_avg": "storey_count_avg",
    "rh_residential": "rh_residential",
    "rh_office": "rh_office",
    "rh_schoolsec": "rh_schoolsec",
    "rh_schoolprim": "rh_schoolprim",
    "rh_retailfood": "rh_retailfood",
    "rh_retailother": "rh_retailother",
    "rh_other": "rh_other",
    "rh_ceiling": "rh_ceiling",
    "hull_ext_wall_wo_window_m2": "hull_ext_wall_wo_window_m2",
    "hull_roof_m2": "hull_roof_m2",
    "hull_fundament_m2": "hull_fundament_m2",
    "hull_windows_north_m2": "hull_windows_north_m2",
    "hull_windows_east_m2": "hull_windows_east_m2",
    "hull_windows_south_m2": "hull_windows_south_m2",
    "hull_windows_west_m2": "hull_windows_west_m2",
    "hull_windows_horizontal_m2": "hull_windows_horizontal_m2",
    "hull_transmittance_walls": "hull_transmittance_walls",
    "hull_transmittance_roof": "hull_transmittance_roof",
    "hull_transmittance_fundament": "hull_transmittance_fundament",
    "hull_transmittance_windows_north": "hull_transmittance_windows_north",
    "hull_transmittance_windows_east": "hull_transmittance_windows_east",
    "hull_transmittance_windows_south": "hull_transmittance_windows_south",
    "hull_transmittance_windows_west": "hull_transmittance_windows_west",
    "hull_transmittance_windows_horizontal": "hull_transmittance_windows_horizontal",
    "hull_transmittance_heatbridge": "hull_transmittance_heatbridge",
    "heat_capacity_effective_m²": "heat_capacity_effective_m",
    "window_total_transmittance_north": "window_total_transmittance_north",
    "window_total_transmittance_east": "window_total_transmittance_east",
    "window_total_transmittance_south": "window_total_transmittance_south",
    "window_total_transmittance_west": "window_total_transmittance_west",
    "window_total_transmittance_horizontal": "window_total_transmittance_horizontal",
    "window_irradiation_factor_winter_north": "window_irradiation_factor_winter_north",
    "window_irradiation_factor_winter_east": "window_irradiation_factor_winter_east",
    "window_irradiation_factor_winter_south": "window_irradiation_factor_winter_south",
    "window_irradiation_factor_winter_west": "window_irradiation_factor_winter_west",
    "window_irradiation_factor_winter_horizontal": "window_irradiation_factor_winter_horizontal",
    "window_irradiation_factor_summer_north": "window_irradiation_factor_summer_north",
    "window_irradiation_factor_summer_east": "window_irradiation_factor_summer_east",
    "window_irradiation_factor_summer_south": "window_irradiation_factor_summer_south",
    "window_irradiation_factor_summer_west": "window_irradiation_factor_summer_west",
    "window_irradiation_factor_summer_horizontal": "window_irradiation_factor_summer_horizontal",
    "irradiation_opaque_surcharge": "irradiation_opaque_surcharge",
    "fc_residential": "fc_residential",
    "fc_office": "fc_office",
    "fc_edusec": "fc_edusec",
    "fc_eduprim": "fc_eduprim",
    "fc_retailfood": "fc_retailfood",
    "fc_retailother": "fc_retailother",
    "fc_other": "fc_other",
    "illuminance_min_residential": "illuminance_min_residential",
    "illuminance_min_office": "illuminance_min_office",
    "illuminance_min_schoolsec": "illuminance_min_schoolsec",
    "illuminance_min_schoolprim": "illuminance_min_schoolprim",
    "illuminance_min_retailfood": "illuminance_min_retailfood",
    "illuminance_min_retailother": "illuminance_min_retailother",
    "illuminance_min_other": "illuminance_min_other",
    "illuminance_efficiency_dirt": "illuminance_efficiency_dirt",
    "illuminance_efficiency_glazing_ratio": "illuminance_efficiency_glazing_ratio",
    "vent_air_tightness": "vent_air_tightness",
    "vent_tightness_ratio_blowerdoor_to_real": "vent_tightness_ratio_blowerdoor_to_real",
    "vent_share_mechanical_residential": "vent_share_mechanical_residential",
    "vent_share_mechanical_office": "vent_share_mechanical_office",
    "vent_share_mechanical_schoolsec": "vent_share_mechanical_schoolsec",
    "vent_share_mechanical_schoolprim": "vent_share_mechanical_schoolprim",
    "vent_share_mechanical_retailfood": "vent_share_mechanical_retailfood",
    "vent_share_mechanical_retailother": "vent_share_mechanical_retailother",
    "vent_share_mechanical_other": "vent_share_mechanical_other",
    "vent_night_residential": "vent_night_residential",
    "vent_night_office": "vent_night_office",
    "vent_night_schoolsec": "vent_night_schoolsec",
    "vent_night_schoolprim": "vent_night_schoolprim",
    "vent_night_retailfood": "vent_night_retailfood",
    "vent_night_retailother": "vent_night_retailother",
    "vent_night_other": "vent_night_other",
    "vent_ach_max_residential": "vent_ach_max_residential",
    "vent_ach_max_office": "vent_ach_max_office",
    "vent_ach_max_schoolsec": "vent_ach_max_schoolsec",
    "vent_ach_max_schoolprim": "vent_ach_max_schoolprim",
    "vent_ach_max_retailfood": "vent_ach_max_retailfood",
    "vent_ach_max_retailother": "vent_ach_max_retailother",
    "vent_ach_max_other": "vent_ach_max_other",
    "Ev_scale_residential": "Ev_scale_residential",
    "Ev_scale_office": "Ev_scale_office",
    "Ev_scale_school_sec": "Ev_scale_school_sec",
    "Ev_scale_school_prim": "Ev_scale_school_prim",
    "Ev_scale_retail_food": "Ev_scale_retail_food",
    "Ev_scale_retail_other": "Ev_scale_retail_other",
    "Ev_scale_other": "Ev_scale_other",
    "vent_heat_recovery_winter_residential": "vent_heat_recovery_winter_residential",
    "vent_heat_recovery_winter_office": "vent_heat_recovery_winter_office",
    "vent_heat_recovery_winter_schoolsec": "vent_heat_recovery_winter_schoolsec",
    "vent_heat_recovery_winter_schoolprim": "vent_heat_recovery_winter_schoolprim",
    "vent_heat_recovery_winter_retailfood": "vent_heat_recovery_winter_retailfood",
    "vent_heat_recovery_winter_retailother": "vent_heat_recovery_winter_retailother",
    "vent_heat_recovery_winter_other": "vent_heat_recovery_winter_other",
    "vent_heat_recovery_summer_residential": "vent_heat_recovery_summer_residential",
    "vent_heat_recovery_summer_office": "vent_heat_recovery_summer_office",
    "vent_heat_recovery_summer_schoolsec": "vent_heat_recovery_summer_schoolsec",
    "vent_heat_recovery_summer_schoolprim": "vent_heat_recovery_summer_schoolprim",
    "vent_heat_recovery_summer_retailfood": "vent_heat_recovery_summer_retailfood",
    "vent_heat_recovery_summer_retailother": "vent_heat_recovery_summer_retailother",
    "vent_heat_recovery_summer_other": "vent_heat_recovery_summer_other",
    "usage_concurrency_winter_res": "usage_concurrency_winter_res",
    "usage_concurrency_winter_office": "usage_concurrency_winter_office",
    "usage_concurrency_winter_edusec": "usage_concurrency_winter_edusec",
    "usage_concurrency_winter_eduprim": "usage_concurrency_winter_eduprim",
    "usage_concurrency_winter_retailfood": "usage_concurrency_winter_retailfood",
    "usage_concurrency_winter_retailother": "usage_concurrency_winter_retailother",
    "usage_concurrency_winter_other": "usage_concurrency_winter_other",
    "usage_concurrency_summer_res": "usage_concurrency_summer_res",
    "usage_concurrency_summer_office": "usage_concurrency_summer_office",
    "usage_concurrency_summer_edusec": "usage_concurrency_summer_edusec",
    "usage_concurrency_summer_eduprim": "usage_concurrency_summer_eduprim",
    "usage_concurrency_summer_retailfood": "usage_concurrency_summer_retailfood",
    "usage_concurrency_summer_retailother": "usage_concurrency_summer_retailother",
    "usage_concurrency_summer_other": "usage_concurrency_summer_other",
    "DHW_demand_residential_kWhm2": "DHW_demand_residential_kWhm2",
    "DHW_demand_office_kWhm2": "DHW_demand_office_kWhm2",
    "DHW_demand_schoolsec_kWhm2": "DHW_demand_schoolsec_kWhm2",
    "DHW_demand_schoolprim_kWhm2": "DHW_demand_schoolprim_kWhm2",
    "DHW_demand_retailfood_kWhm2": "DHW_demand_retailfood_kWhm2",
    "DHW_demand_retailother_kWhm2": "DHW_demand_retailother_kWhm2",
    "DHW_demand_other_kWhm2": "DHW_demand_other_kWhm2",
    "aux_el_demand_residential_kWhm2": "aux_el_demand_residential_kWhm2",
    "aux_el_demand_office_kWhm2": "aux_el_demand_office_kWhm2",
    "aux_el_demand_schoolsec_kWhm2": "aux_el_demand_schoolsec_kWhm2",
    "aux_el_demand_schoolprim_kWhm2": "aux_el_demand_schoolprim_kWhm2",
    "aux_el_demand_retailfood_kWhm2": "aux_el_demand_retailfood_kWhm2",
    "aux_el_demand_retailother_kWhm2": "aux_el_demand_retailother_kWhm2",
    "aux_el_demand_other_kWhm2": "aux_el_demand_other_kWhm2",
    "Plugloads_scale_res": "Plugloads_scale_res",
    "Plugloads_scale_office": "Plugloads_scale_office",
    "Plugloads_scale_schoolsec": "Plugloads_scale_schoolsec",
    "Plugloads_scale_schoolprim": "Plugloads_scale_schoolprim",
    "Plugloads_scale_retailfood": "Plugloads_scale_retailfood",
    "Plugloads_scale_retailother": "Plugloads_scale_retailother",
    "Plugloads_scale_other": "Plugloads_scale_other",
    "density_NFApPers_residential": "density_NFApPers_residential",
    "density_NFApPers_office": "density_NFApPers_office",
    "density_NFApPers_edu": "density_NFApPers_edu",
    "density_NFApPers_retail": "density_NFApPers_retail",
    "density_NFApPers_edu_rpim": "density_NFApPers_edu_rpim",
    "density_NFApPers_retail_other": "density_NFApPers_retail_other",
    "mob_simultaneity_edu": "mob_simultaneity_edu",
    "mob_simultaneity_retail": "mob_simultaneity_retail",
    "mob_simultaneity_office": "mob_simultaneity_office",
    "mob_motorization_perNFA_residential": "mob_motorization_perNFA_residential",
    "mob_motorization_perNFA_work": "mob_motorization_perNFA_work",
    "mob_motorization_perNFA_retail": "mob_motorization_perNFA_retail",
    "Plight_max_office": "Plight_max_office",
    "Plight_max_schoolsec": "Plight_max_schoolsec",
    "Plight_max_schoolprim": "Plight_max_schoolprim",
    "Plight_min_office": "Plight_min_office",
    "Plight_min_schoolsec": "Plight_min_schoolsec",
    "Plight_min_schoolprim": "Plight_min_schoolprim",
    "lighting_factor_office": "lighting_factor_office",
    "lighting_factor_schoolsec": "lighting_factor_schoolsec",
    "lighting_factor_schoolprim": "lighting_factor_schoolprim",
    "lighting_factor_retailfood": "lighting_factor_retailfood",
    "lighting_factor_retailother": "lighting_factor_retailother",
    "lighting_factor_other": "lighting_factor_other",
    "Daylightcoefficient_office": "Daylightcoefficient_office",
    "Daylightcoefficient_schoolsec": "Daylightcoefficient_schoolsec",
    "Daylightcoefficient_schoolprim": "Daylightcoefficient_schoolprim",
    "daylightcontr_office": "daylightcontr_office",
    "daylightcontr_schoolsec": "daylightcontr_schoolsec",
    "daylightcontr_schoolprim": "daylightcontr_schoolprim",
    "heating_month1": "heating_month1",
    "heating_month2": "heating_month2",
    "heating_month3": "heating_month3",
    "heating_month4": "heating_month4",
    "heating_month5": "heating_month5",
    "heating_month6": "heating_month6",
    "heating_month7": "heating_month7",
    "heating_month8": "heating_month8",
    "heating_month9": "heating_month9",
    "heating_month10": "heating_month10",
    "heating_month11": "heating_month11",
    "heating_month12": "heating_month12",
    "QHmax_room_m²": "QHmax_room_m",
    "QHmax_1el_m²": "QHmax_1el_m",
    "QHmax_2th_m²": "QHmax_2th_m",
    "QHmax_3el_m²": "QHmax_3el_m",
    "QHmax_4th_m²": "QHmax_4th_m",
    "QH_distr_loss_1el": "QH_distr_loss_1el",
    "QH_distr_loss_2th": "QH_distr_loss_2th",
    "QH_distr_loss_3el": "QH_distr_loss_3el",
    "QH_distr_loss_4th": "QH_distr_loss_4th",
    "heat_cop_1el": "heat_cop_1el",
    "heat_cop_2th": "heat_cop_2th",
    "heat_cop_3el": "heat_cop_3el",
    "heat_cop_4th": "heat_cop_4th",
    "QH_aux_wasteheat": "QH_aux_wasteheat",
    "QH_aux_el_to_th_1el": "QH_aux_el_to_th_1el",
    "QH_aux_el_to_th_2th": "QH_aux_el_to_th_2th",
    "QH_aux_el_to_th_3el": "QH_aux_el_to_th_3el",
    "QH_aux_el_to_th_4th": "QH_aux_el_to_th_4th",
    "heat_th2_carrier_type": "heat_th2_carrier_type",
    "heat_th4_carrier_type": "heat_th4_carrier_type",
    "Tsetheat_min": "Tsetheat_min",
    "cooling_month1": "cooling_month1",
    "cooling_month2": "cooling_month2",
    "cooling_month3": "cooling_month3",
    "cooling_month4": "cooling_month4",
    "cooling_month5": "cooling_month5",
    "cooling_month6": "cooling_month6",
    "cooling_month7": "cooling_month7",
    "cooling_month8": "cooling_month8",
    "cooling_month9": "cooling_month9",
    "cooling_month10": "cooling_month10",
    "cooling_month11": "cooling_month11",
    "cooling_month12": "cooling_month12",
    "cool_share_residential": "cool_share_residential",
    "cool_share_office": "cool_share_office",
    "cool_share_schoolsec": "cool_share_schoolsec",
    "cool_share_schoolprim": "cool_share_schoolprim",
    "cool_share_retailfood": "cool_share_retailfood",
    "cool_share_retailother": "cool_share_retailother",
    "cool_share_other": "cool_share_other",
    "QCmax_room_m2": "QCmax_room_m2",
    "QCmax_freecooling": "QCmax_freecooling",
    "QCmax_1el": "QCmax_1el",
    "QCmax_2th": "QCmax_2th",
    "QCmax_3el": "QCmax_3el",
    "QC_distr_losses_1el": "QC_distr_losses_1el",
    "QC_distr_losses_2th": "QC_distr_losses_2th",
    "QC_distr_losses_3el": "QC_distr_losses_3el",
    "cool_cop_1el": "cool_cop_1el",
    "cool_cop_2th": "cool_cop_2th",
    "cool_cop_3el": "cool_cop_3el",
    "QC_aux_fc": "QC_aux_fc",
    "QC_aux_1el": "QC_aux_1el",
    "QC_aux_2th": "QC_aux_2th",
    "QC_aux_3el": "QC_aux_3el",
    "cool_th2_carrier_type": "cool_th2_carrier_type",
    "Tsetcool_max": "Tsetcool_max",
    "DHW_Tmin": "DHW_Tmin",
    "DHW_Tmax_input": "DHW_Tmax_input",
    "DHW_1_share_residential": "DHW_1_share_residential",
    "DHW_1_share_office": "DHW_1_share_office",
    "DHW_1_share_schoolsec": "DHW_1_share_schoolsec",
    "DHW_1_share_schoolprim": "DHW_1_share_schoolprim",
    "DHW_1_share_retailfood": "DHW_1_share_retailfood",
    "DHW_1_share_retailother": "DHW_1_share_retailother",
    "DHW_1_share_other": "DHW_1_share_other",
    "DHW_losses_1": "DHW_losses_1",
    "DHW_losses_2": "DHW_losses_2",
    "DHW_efficiency_distribution_1": "DHW_efficiency_distribution_1",
    "DHW_efficiency_distribution_2": "DHW_efficiency_distribution_2",
    "DHW_carriertype_1": "DHW_carriertype_1",
    "DHW_carriertype_2": "DHW_carriertype_2",
    "DHW_1_efficiency": "DHW_1_efficiency",
    "DHW_2_efficiency": "DHW_2_efficiency",
    "DHW_1_el_aux": "DHW_1_el_aux",
    "DHW_2_el_aux": "DHW_2_el_aux",
    "DHW_occupancy_residential": "DHW_occupancy_residential",
    "DHW_occupancy_office": "DHW_occupancy_office",
    "DHW_occupancy_schoolsec": "DHW_occupancy_schoolsec",
    "DHW_occupancy_schoolprim": "DHW_occupancy_schoolprim",
    "DHW_occupancy_retailfood": "DHW_occupancy_retailfood",
    "DHW_occupancy_retailother": "DHW_occupancy_retailother",
    "DHW_occupancy_other": "DHW_occupancy_other",
    "DHW_concurrency_residential": "DHW_concurrency_residential",
    "DHW_concurrency_office": "DHW_concurrency_office",
    "DHW_concurrency_schoolsec": "DHW_concurrency_schoolsec",
    "DHW_concurrency_schoolprim": "DHW_concurrency_schoolprim",
    "DHW_concurrency_retailfood": "DHW_concurrency_retailfood",
    "DHW_concurrency_retailother": "DHW_concurrency_retailother",
    "DHW_concurrency_other": "DHW_concurrency_other",
    "DHW_storage_liter_pPerson": "DHW_storage_liter_pPerson",
    "DHW_thermal_power_pPerson": "DHW_thermal_power_pPerson",
    "DHW_storage_env_temp_default": "DHW_storage_env_temp_default",
    "PV_is_used": "PV_is_used",
    "PV_profile_name": "PV_profile_name",
    "PV_scale": "PV_scale",
    "PV_efficiency": "PV_efficiency",
    "PV_m2_per_kWp": "PV_m2_per_kWp",
    "FLEX_PV_is_used": "FLEX_PV_is_used",
    "FLEX_is_used": "FLEX_is_used",
    "FLEX_signal_name": "FLEX_signal_name",
    "FLEX_grid_maxpower_Wm2": "FLEX_grid_maxpower_Wm2",
    "FLEX_is_used_for_plugloads": "FLEX_is_used_for_plugloads",
    "FLEX_is_used_for_HVAC_min": "FLEX_is_used_for_HVAC_min",
    "FLEX_is_used_for_ev_min": "FLEX_is_used_for_ev_min",
    "flex_heat_dT": "flex_heat_dT",
    "FLEX_choice_heat_system": "FLEX_choice_heat_system",
    "flex_cool_dT": "flex_cool_dT",
    "FLEX_choice_cool_system": "FLEX_choice_cool_system",
    "Batt_is_used": "Batt_is_used",
    "Batt_cap_kWh": "Batt_cap_kWh",
    "Batt_c_rate": "Batt_c_rate",
    "Batt_eff_factor_charge": "Batt_eff_factor_charge",
    "Batt_eff_factor_discharge": "Batt_eff_factor_discharge",
    "Batt_self_discharge_rate": "Batt_self_discharge_rate",
    "Batt_SOC_init": "Batt_SOC_init",
    "Batt_is_used_for_plugloads": "Batt_is_used_for_plugloads",
    "Batt_is_used_for_HVACminimum": "Batt_is_used_for_HVACminimum",
    "Batt_is_used_for_EV": "Batt_is_used_for_EV",
    "Batt_is_gridcharged": "Batt_is_gridcharged",
    "flex_dhw_use": "flex_dhw_use",
    "Batt_is_not_used_during_signals": "Batt_is_not_used_during_signals",
    "mobility_is_included": "mobility_is_included",
    "mobility_vehicle_count": "mobility_vehicle_count",
    "EV_share": "EV_share",
    "EV_demand_kWhpkm": "EV_demand_kWhpkm",
    "EV_battsize_kWh": "EV_battsize_kWh",
    "EV_self_discharge_per_week": "EV_self_discharge_per_week",
    "EV_soc_minimum": "EV_soc_minimum",
    "EV_charging_efficiency": "EV_charging_efficiency",
    "EV_max_charging_power_ratio": "EV_max_charging_power_ratio",
    "EV_soc_min_work": "EV_soc_min_work",
    "EV_soc_min_retail": "EV_soc_min_retail",
    "moped_factor": "moped_factor",
    "EV_share_constant_charging": "EV_share_constant_charging",
    "mob_pkm_factor": "mob_pkm_factor",
    "EV_experimental_calculation": "EV_experimental_calculation",
    "EV_soc_min_ext": "EV_soc_min_ext",
    "EV_soc_min_discharge": "EV_soc_min_discharge",
    "fossile_demand_kWhpkm": "fossile_demand_kWhpkm",
    "ev_bidirectional_use": "ev_bidirectional_use",
    "GWP_walls_name": "GWP_walls_name",
    "COMP_name_windows": "COMP_name_windows",
    "GWP_roof_name": "GWP_roof_name",
    "GWP_ground_name": "GWP_ground_name",
    "GPW_ceilings_name": "GPW_ceilings_name",
    "GWP_general_name": "GWP_general_name",
    "GWP_other_name": "GWP_other_name",
    "GWP_ref_area_walls": "GWP_ref_area_walls",
    "GWP_ref_area_windows": "GWP_ref_area_windows",
    "GWP_ref_area_roof": "GWP_ref_area_roof",
    "GWP_ref_area_fundament": "GWP_ref_area_fundament",
    "GWP_ref_area_ceilings": "GWP_ref_area_ceilings",
    "GWP_pv_name": "GWP_pv_name",
    "GWP_boreholes_name": "GWP_boreholes_name",
    "borehole_count": "borehole_count",
    "GWP_ventilation_name": "GWP_ventilation_name",
    "GWP_solarthermal_name": "GWP_solarthermal_name",
    "GWP_battery_name": "GWP_battery_name",
    "GWP_storage_name": "GWP_storage_name",
    "GWP_tga_general_name": "GWP_tga_general_name",
    "GWP_tga_other_name": "GWP_tga_other_name",
    "GWP_direct_fossile": "GWP_direct_fossile",
    "GWP_direct_biogenic": "GWP_direct_biogenic",
    "GWP_direct_biogenic_share": "GWP_direct_biogenic_share",
    "GWP_direct_life": "GWP_direct_life",
    "GWP_mobility_construction_fossil": "GWP_mobility_construction_fossil",
    "GWP_mobility_construction_ev": "GWP_mobility_construction_ev",
    "GHG_LCA_timeframe_years": "GHG_LCA_timeframe_years",
    "GWP_mobility_moped_gpPKm": "GWP_mobility_moped_gpPKm",
    "GWP_mobility_car_gpPKm": "GWP_mobility_car_gpPKm",
    "year_rcp0": "year_rcp0",
    "year_rcp1": "year_rcp1",
    "year_rcp2": "year_rcp2",
    "year_rcp3": "year_rcp3",
    "grid_rcp1": "grid_rcp1",
    "grid_rcp2": "grid_rcp2",
    "grid_rcp3": "grid_rcp3",
    "rcp1_renewable": "rcp1_renewable",
    "rcp2_renewable": "rcp2_renewable",
    "rcp3_renewable": "rcp3_renewable",
    "rcp1_fossil": "rcp1_fossil",
    "rcp2_fossil": "rcp2_fossil",
    "rcp3_fossil": "rcp3_fossil",
    "fPE_grid_profile": "fPE_grid_profile",
    "district_heating_conversion_profile": "district_heating_conversion_profile",
    "fGHG_grid_profile": "fGHG_grid_profile",
    "fPE_flex_factor": "fPE_flex_factor",
    "pe_conversion_factor_gasoline": "pe_conversion_factor_gasoline",
    "e_kWhm2a": "e_kWhm2a",
    "EV_charging_stations": "EV_charging_stations",
    "EV_charging_station_power": "EV_charging_station_power",
}

OUTPUT_ATTR_MAP: dict[str, str] = {
    "UED_plugloads": "UED_plugloads",
    "UED_lighting": "UED_lighting",
    "UED_auxiliary": "UED_auxiliary",
    "UED_heating": "UED_heating",
    "UED_cooling": "UED_cooling",
    "UED_dhw": "UED_dhw",
    "UED_ventilation": "UED_ventilation",
    "UED_mim_electric": "UED_mim_electric",
    "UED_mim_fossile": "UED_mim_fossile",
    "QT": "QT",
    "QV": "QV",
    "QVn": "QVn",
    "QS": "QS",
    "QI": "QI",
    "QH": "QH",
    "QC": "QC",
    "QV_heatrecovery": "QV_heatrecovery",
    "QT_winter": "QT_winter",
    "QV_winter": "QV_winter",
    "QVn_winter": "QVn_winter",
    "QS_winter": "QS_winter",
    "QI_winter": "QI_winter",
    "QH_winter": "QH_winter",
    "QC_winter": "QC_winter",
    "QT_wall_winter": "QT_wall_winter",
    "QT_roof_winter": "QT_roof_winter",
    "QT_ground_winter": "QT_ground_winter",
    "QT_window_winter": "QT_window_winter",
    "QT_psi_winter": "QT_psi_winter",
    "QV_inf_winter": "QV_inf_winter",
    "QV_window_winter": "QV_window_winter",
    "QV_mechvent_winter": "QV_mechvent_winter",
    "QV_heatrecovery_winter": "QV_heatrecovery_winter",
    "QH_min_winter": "QH_min_winter",
    "QH_flex_winter": "QH_flex_winter",
    "QC_min_winter": "QC_min_winter",
    "QC_flex_winter": "QC_flex_winter",
    "QH_flexshare_winter": "QH_flexshare_winter",
    "QC_flexshare_winter": "QC_flexshare_winter",
    "QT_summer": "QT_summer",
    "QV_summer": "QV_summer",
    "QVn_summer": "QVn_summer",
    "QS_summer": "QS_summer",
    "QI_summer": "QI_summer",
    "QH_summer": "QH_summer",
    "QC_summer": "QC_summer",
    "QT_wall_summer": "QT_wall_summer",
    "QT_roof_summer": "QT_roof_summer",
    "QT_ground_summer": "QT_ground_summer",
    "QT_window_summer": "QT_window_summer",
    "QT_psi_summer": "QT_psi_summer",
    "QV_inf_summer": "QV_inf_summer",
    "QV_window_summer": "QV_window_summer",
    "QV_mechvent_summer": "QV_mechvent_summer",
    "QV_heatrecovery_summer": "QV_heatrecovery_summer",
    "QH_min_summer": "QH_min_summer",
    "QH_flex_summer": "QH_flex_summer",
    "QC_min_summer": "QC_min_summer",
    "QC_flex_summer": "QC_flex_summer",
    "QH_flexshare_summer": "QH_flexshare_summer",
    "QC_flexshare_summer": "QC_flexshare_summer",
    "QT_u": "QT_u",
    "QV_u": "QV_u",
    "QVn_u": "QVn_u",
    "QS_u": "QS_u",
    "QI_u": "QI_u",
    "QH_u": "QH_u",
    "QT_wall_u": "QT_wall_u",
    "QT_roof_u": "QT_roof_u",
    "QT_ground_u": "QT_ground_u",
    "QT_window_u": "QT_window_u",
    "QT_psi_u": "QT_psi_u",
    "QV_inf_u": "QV_inf_u",
    "QV_window_u": "QV_window_u",
    "QV_mechvent_u": "QV_mechvent_u",
    "QV_heatrecovery_u": "QV_heatrecovery_u",
    "QH_min_u": "QH_min_u",
    "QH_flex_u": "QH_flex_u",
    "QH_flexanteil_u": "QH_flexanteil_u",
    "QT_c": "QT_c",
    "QV_c": "QV_c",
    "QVn_c": "QVn_c",
    "QS_c": "QS_c",
    "QI_c": "QI_c",
    "QH_c": "QH_c",
    "QC_c": "QC_c",
    "QT_wall_c": "QT_wall_c",
    "QT_roof_c": "QT_roof_c",
    "QT_ground_c": "QT_ground_c",
    "QT_window_c": "QT_window_c",
    "QT_psi_c": "QT_psi_c",
    "QV_inf_c": "QV_inf_c",
    "QV_window_c": "QV_window_c",
    "QV_mechvent_c": "QV_mechvent_c",
    "QV_heatrecovery_c": "QV_heatrecovery_c",
    "QH_min_c": "QH_min_c",
    "QH_flex_c": "QH_flex_c",
    "QC_min_c": "QC_min_c",
    "QC_flex_c": "QC_flex_c",
    "QC_flexanteil": "QC_flexanteil",
    "QH_flexanteil_c": "QH_flexanteil_c",
    "dTu winter": "dTu_winter",
    "dTc winter": "dTc_winter",
    "dTu summer": "dTu_summer",
    "dTc summer": "dTc_summer",
    "EUI_plugAuxLight": "EUI_plugAuxLight",
    "EUI_plugloads": "EUI_plugloads",
    "EUI_auxiliary": "EUI_auxiliary",
    "EUI_lighting": "EUI_lighting",
    "EUIh_el": "EUIh_el",
    "EUIh_el_aux": "EUIh_el_aux",
    "EUIc_el": "EUIc_el",
    "EUIc_el_aux": "EUIc_el_aux",
    "EUIdhw_el": "EUIdhw_el",
    "EUIv_el": "EUIv_el",
    "EUIdhwdirect_el": "EUIdhwdirect_el",
    "Batt_total_charge_input": "Batt_total_charge_input",
    "EUIev_el": "EUIev_el",
    "EUI_el_total": "EUI_el_total",
    "PV_total": "PV_total",
    "PV_to_plugloads": "PV_to_plugloads",
    "PV_to_Eh_min": "PV_to_Eh_min",
    "PV_to_Ec_min": "PV_to_Ec_min",
    "PV_to_Edhw_min": "PV_to_Edhw_min",
    "PV_to_Ev_min": "PV_to_Ev_min",
    "PV_to_Eev_min": "PV_to_Eev_min",
    "PV_total_direct": "PV_total_direct",
    "PV_to_Eh_flex": "PV_to_Eh_flex",
    "PV_to_Ec_flex": "PV_to_Ec_flex",
    "PV_to_Edhw": "PV_to_Edhw",
    "PV_to_Edhw_direct": "PV_to_Edhw_direct",
    "PV_to_Batt": "PV_to_Batt",
    "PV_to_Eev_flex": "PV_to_Eev_flex",
    "PV_total_flex": "PV_total_flex",
    "PV_to_Egrid": "PV_to_Egrid",
    "Batt_to_plugloads": "Batt_to_plugloads",
    "Batt_to_HVAC": "Batt_to_HVAC",
    "Batt_to_Eh_min": "Batt_to_Eh_min",
    "Batt_to_Ec_min": "Batt_to_Ec_min",
    "Batt_to_Edhw_min": "Batt_to_Edhw_min",
    "Batt_to_Ev_min": "Batt_to_Ev_min",
    "Batt_to_Eev_min": "Batt_to_Eev_min",
    "VRGrid_to_plugloads": "VRGrid_to_plugloads",
    "VRGrid_to_Eh_min": "VRGrid_to_Eh_min",
    "VRGrid_to_Ec_min": "VRGrid_to_Ec_min",
    "VRGrid_to_Edhw_min": "VRGrid_to_Edhw_min",
    "VRGrid_to_Ev_min": "VRGrid_to_Ev_min",
    "VRGrid_to_Eev_min": "VRGrid_to_Eev_min",
    "VRGrid_to_min": "VRGrid_to_min",
    "VRGrid_to_Eh_flex": "VRGrid_to_Eh_flex",
    "VRGrid_to_Ec_flex": "VRGrid_to_Ec_flex",
    "VRGrid_to_Edhw_flex": "VRGrid_to_Edhw_flex",
    "VRGrid_to_Batt": "VRGrid_to_Batt",
    "VRGrid_to_Eev_flex": "VRGrid_to_Eev_flex",
    "VRGrid_to_flex": "VRGrid_to_flex",
    "VRGrid_to_building": "VRGrid_to_building",
    "Eev_to_plugloads": "Eev_to_plugloads",
    "Eev_to_HVAC": "Eev_to_HVAC",
    "Eev_to_Eh_min": "Eev_to_Eh_min",
    "Eev_to_Ec_min": "Eev_to_Ec_min",
    "Eev_to_Edhw_min": "Eev_to_Edhw_min",
    "Eev_to_Ev_min": "Eev_to_Ev_min",
    "Eev_discharge_loss": "Eev_discharge_loss",
    "Eev_to_district": "Eev_to_district",
    "Grid_to_plugloads": "Grid_to_plugloads",
    "Grid_to_Eh_min": "Grid_to_Eh_min",
    "Grid_to_Ec_min": "Grid_to_Ec_min",
    "Grid_to_Edhw_min": "Grid_to_Edhw_min",
    "Grid_to_Ev_min": "Grid_to_Ev_min",
    "Grid_to_building_min": "Grid_to_building_min",
    "Grid_to_Eev_min": "Grid_to_Eev_min",
    "Grid_to_min": "Grid_to_min",
    "Eev_ext_charge": "Eev_ext_charge",
    "EUIh_district_heating": "EUIh_district_heating",
    "EUIdhw_district_heating": "EUIdhw_district_heating",
    "EUI_district_heating": "EUI_district_heating",
    "EUIh_natural_gas": "EUIh_natural_gas",
    "EUIdhw_natural_gas": "EUIdhw_natural_gas",
    "EUI_natural_gas": "EUI_natural_gas",
    "EUIh_biomass": "EUIh_biomass",
    "EUIdhw_biomass": "EUIdhw_biomass",
    "EUI_biomass": "EUI_biomass",
    "EUIh_other": "EUIh_other",
    "EUIc_other": "EUIc_other",
    "EUIdhw_other": "EUIdhw_other",
    "EUI_other": "EUI_other",
    "EUI_mob_fossil": "EUI_mob_fossil",
    "EUIh_2th": "EUIh_2th",
    "EUIh_4th": "EUIh_4th",
    "EUIc_2th": "EUIc_2th",
    "EUIdhw_1th": "EUIdhw_1th",
    "EUIdhw_2th": "EUIdhw_2th",
    "Grid_total_flexandnotflex": "Grid_total_flexandnotflex",
    "context_factor_density": "context_factor_density",
    "context_factor_mobility": "context_factor_mobility",
    "context_factor_renovation": "context_factor_renovation",
    "PEI_demand": "PEI_demand",
    "PEI_el_plugloads": "PEI_el_plugloads",
    "PEI_el_hvac": "PEI_el_hvac",
    "PEI_district_heating": "PEI_district_heating",
    "PEI_natural_gas": "PEI_natural_gas",
    "PEI_biomass": "PEI_biomass",
    "PEI_other": "PEI_other",
    "PEI_mob_total": "PEI_mob_total",
    "PEI_mob_fossile": "PEI_mob_fossile",
    "PEI_mob_el": "PEI_mob_el",
    "PEI_storage_losses": "PEI_storage_losses",
    "PEI_cf_density": "PEI_cf_density",
    "PEI_cf_mobility": "PEI_cf_mobility",
    "PEI_cf_renovation": "PEI_cf_renovation",
    "PEI_sub_PV": "PEI_sub_PV",
    "PEI_sub_flex": "PEI_sub_flex",
    "PEI_balance": "PEI_balance",
    "PEI_grid_import": "PEI_grid_import",
    "PEI_flex_import": "PEI_flex_import",
    "PEI_evExtCharge_import": "PEI_evExtCharge_import",
    "PEI_import": "PEI_import",
    "PEI_pv_export": "PEI_pv_export",
    "PEI_evOtherTravel_export": "PEI_evOtherTravel_export",
    "PEI_export": "PEI_export",
    "PEI_saldo_project": "PEI_saldo_project",
    "PEI_saldo_target": "PEI_saldo_target",
    "PEI_importExport_balance": "PEI_importExport_balance",
    "fPE_grid": "fPE_grid",
    "fPE_eff": "fPE_eff",
    "GWP_ee_walls_fossile": "GWP_ee_walls_fossile",
    "GWP_ee_walls_biogenic": "GWP_ee_walls_biogenic",
    "GWP_life_walls": "GWP_life_walls",
    "GWP_ee_lc_walls_fossil": "GWP_ee_lc_walls_fossil",
    "GWP_ee_lc_walls_biogenic": "GWP_ee_lc_walls_biogenic",
    "GWP_ee_lc_walls": "GWP_ee_lc_walls",
    "GWP_ee_windows_fossile": "GWP_ee_windows_fossile",
    "GWP_ee_windows_bigenic": "GWP_ee_windows_bigenic",
    "GWP_life_windows": "GWP_life_windows",
    "GWP_ee_lc_windows_fossile": "GWP_ee_lc_windows_fossile",
    "GWP_ee_lc_windows_biogenic": "GWP_ee_lc_windows_biogenic",
    "GWP_ee_lc_windows": "GWP_ee_lc_windows",
    "GWP_ee_roof_fossile": "GWP_ee_roof_fossile",
    "GWP_ee_roof_biogenic": "GWP_ee_roof_biogenic",
    "GWP_life_roof": "GWP_life_roof",
    "GWP_ee_lc_roof_fossile": "GWP_ee_lc_roof_fossile",
    "GWP_ee_lc_roof_biogenic": "GWP_ee_lc_roof_biogenic",
    "GWP_ee_lc_roof": "GWP_ee_lc_roof",
    "GWP_ee_ground_fossile": "GWP_ee_ground_fossile",
    "GWP_ee_ground_biogenic": "GWP_ee_ground_biogenic",
    "GWP_life_ground": "GWP_life_ground",
    "GWP_ee_lc_ground_fossile": "GWP_ee_lc_ground_fossile",
    "GWP_ee_lc_ground_biogenic": "GWP_ee_lc_ground_biogenic",
    "GWP_ee_lc_ground": "GWP_ee_lc_ground",
    "GWP_ee_ceilings_fossile": "GWP_ee_ceilings_fossile",
    "GWP_ee_ceilings_biogenic": "GWP_ee_ceilings_biogenic",
    "GWP_life_ceilings": "GWP_life_ceilings",
    "GWP_ee_lc_ceilings_fossile": "GWP_ee_lc_ceilings_fossile",
    "GWP_ee_lc_ceilings_biogenic": "GWP_ee_lc_ceilings_biogenic",
    "GWP_ee_lc_ceil": "GWP_ee_lc_ceil",
    "GWP_ee_general_fossile": "GWP_ee_general_fossile",
    "GWP_ee_general_bigonenic": "GWP_ee_general_bigonenic",
    "GWP_life_general": "GWP_life_general",
    "GWP_ee_lc_general_fossile": "GWP_ee_lc_general_fossile",
    "GWP_ee_lc_general_biogenic": "GWP_ee_lc_general_biogenic",
    "GWP_ee_general": "GWP_ee_general",
    "GWP_ee_other_fossile": "GWP_ee_other_fossile",
    "GWP_ee_other_biogenic": "GWP_ee_other_biogenic",
    "GWP_life_other": "GWP_life_other",
    "GWP_ee_lc_other_fossile": "GWP_ee_lc_other_fossile",
    "GWP_ee_lc_other_biogenic": "GWP_ee_lc_other_biogenic",
    "GWP_ee_lc_other": "GWP_ee_lc_other",
    "GWP_ee_direct_fossile": "GWP_ee_direct_fossile",
    "GWP_ee_direct_biogenic": "GWP_ee_direct_biogenic",
    "GWP_life_direct": "GWP_life_direct",
    "GWP_ee_lc_direct_fossile": "GWP_ee_lc_direct_fossile",
    "GWP_ee_lc_direct_biogenic": "GWP_ee_lc_direct_biogenic",
    "GWP_ee_lc_direct": "GWP_ee_lc_direct",
    "GWP_ee_con_build": "GWP_ee_con_build",
    "GWP_ee_rep_build": "GWP_ee_rep_build",
    "GWP_ee_lc_fossil": "GWP_ee_lc_fossil",
    "GWP_ee_lc_biogenic": "GWP_ee_lc_biogenic",
    "GWP_ee_lc_construction": "GWP_ee_lc_construction",
    "GWP_ee_tga_pv_fossile": "GWP_ee_tga_pv_fossile",
    "GWP_ee_tga_pv_biogenic": "GWP_ee_tga_pv_biogenic",
    "GWP_life_tga_pv": "GWP_life_tga_pv",
    "GWP_ee_lc_pv": "GWP_ee_lc_pv",
    "GWP_ee_tga_boreholes_fossile": "GWP_ee_tga_boreholes_fossile",
    "GWP_ee_tga_boreholes_biogenic": "GWP_ee_tga_boreholes_biogenic",
    "GWP_life_tga_boreholes": "GWP_life_tga_boreholes",
    "GWP_ee_lc_boreholes": "GWP_ee_lc_boreholes",
    "GWP_ee_tga_ventilation_fossile": "GWP_ee_tga_ventilation_fossile",
    "GWP_ee_tga_ventilation_biogenic": "GWP_ee_tga_ventilation_biogenic",
    "GWP_life_tga_ventilation": "GWP_life_tga_ventilation",
    "GWP_ee_lc_ventilation": "GWP_ee_lc_ventilation",
    "GWP_ee_tga_solarthermal_fossile": "GWP_ee_tga_solarthermal_fossile",
    "GWP_ee_tga_solarthermal_biogenic": "GWP_ee_tga_solarthermal_biogenic",
    "GWP_life_solarthermal": "GWP_life_solarthermal",
    "GWP_ee_lc_solarthermal": "GWP_ee_lc_solarthermal",
    "GWP_ee_tga_battery_fossile": "GWP_ee_tga_battery_fossile",
    "GWP_ee_tga_battery_biogenic": "GWP_ee_tga_battery_biogenic",
    "GWP_life_battery": "GWP_life_battery",
    "GWP_ee_lc_battery": "GWP_ee_lc_battery",
    "GWP_ee_tga_storage_fossile": "GWP_ee_tga_storage_fossile",
    "GWP_ee_tga_storage_biogenic": "GWP_ee_tga_storage_biogenic",
    "GWP_life_storage": "GWP_life_storage",
    "GWP_ee_lc_storage": "GWP_ee_lc_storage",
    "GWP_ee_tga_general_fossile": "GWP_ee_tga_general_fossile",
    "GWP_ee_tga_general_biogenic": "GWP_ee_tga_general_biogenic",
    "GWP_life_tga_general": "GWP_life_tga_general",
    "GWP_ee_lc_tga_general": "GWP_ee_lc_tga_general",
    "GWP_ee_tga_other_fossile": "GWP_ee_tga_other_fossile",
    "GWP_ee_tga_other_biogenic": "GWP_ee_tga_other_biogenic",
    "GWP_life_tga_other": "GWP_life_tga_other",
    "GWP_ee_lc_tga_other": "GWP_ee_lc_tga_other",
    "GWP_ee_con_tga": "GWP_ee_con_tga",
    "GWP_ee_rep_tga": "GWP_ee_rep_tga",
    "GWP_ee_lc_tga": "GWP_ee_lc_tga",
    "GWP_ee_mob_fossile": "GWP_ee_mob_fossile",
    "GWP_ee_mob_ev": "GWP_ee_mob_ev",
    "GWP_ee_lc_mob": "GWP_ee_lc_mob",
    "GWP_oe_battery_charge": "GWP_oe_battery_charge",
    "GWP_emInt_grid_avg": "GWP_emInt_grid_avg",
    "GWP_emInt_grid": "GWP_emInt_grid",
    "GWP_emInt_flex": "GWP_emInt_flex",
    "GWP_emInt_batt_charge": "GWP_emInt_batt_charge",
    "GWP_emInt_ev_charge": "GWP_emInt_ev_charge",
    "GWP_emInt_PV_feedin": "GWP_emInt_PV_feedin",
    "GWP_oe_grid_build": "GWP_oe_grid_build",
    "GWP_oe_flex_build": "GWP_oe_flex_build",
    "GWP_oe_district_heating": "GWP_oe_district_heating",
    "GWP_oe_natural_gas": "GWP_oe_natural_gas",
    "GWP_oe_biomass": "GWP_oe_biomass",
    "GWP_oe_other": "GWP_oe_other",
    "GWP_oe_grid_feedin": "GWP_oe_grid_feedin",
    "GWP_oe_building": "GWP_oe_building",
    "GWP_oe_mob_ev": "GWP_oe_mob_ev",
    "GWP_oe_mob_ev_export": "GWP_oe_mob_ev_export",
    "GWP_oe_mob_fossile": "GWP_oe_mob_fossile",
    "GWP_oe_mob": "GWP_oe_mob",
    "GWP_oe": "GWP_oe",
    "GWP_oe_lc_grid_build": "GWP_oe_lc_grid_build",
    "GWP_oe_lc_flex_build": "GWP_oe_lc_flex_build",
    "GWP_oe_lc_district_heating": "GWP_oe_lc_district_heating",
    "GWP_oe_lc_natural_gas": "GWP_oe_lc_natural_gas",
    "GWP_oe_lc_biomass": "GWP_oe_lc_biomass",
    "GWP_oe_lc_other": "GWP_oe_lc_other",
    "GWP_oe_lc_grid_feedin": "GWP_oe_lc_grid_feedin",
    "GWP_oe_lc_building": "GWP_oe_lc_building",
    "GWP_oe_lc_emission": "GWP_oe_lc_emission",
    "GWP_oe_lc_emission_savings": "GWP_oe_lc_emission_savings",
    "GWP_oe_lc_mob_ev": "GWP_oe_lc_mob_ev",
    "GWP_oe_lc_mob_export": "GWP_oe_lc_mob_export",
    "GWP_oe_lc_mob_fossile": "GWP_oe_lc_mob_fossile",
    "GWP_oe_lc_mob": "GWP_oe_lc_mob",
    "GWP_lc_total": "GWP_lc_total",
    "GWP_lc_OE_total": "GWP_lc_OE_total",
    "GWP_lc_EE_total": "GWP_lc_EE_total",
    "cost_E_grid": "cost_E_grid",
    "cost_VRGrid_flex": "cost_VRGrid_flex",
    "cost_PV_to_Egrid": "cost_PV_to_Egrid",
    "cost_total": "cost_total",
    "flex_signal_ratio": "flex_signal_ratio",
    "flex_signal_ratio_winter": "flex_signal_ratio_winter",
    "flex_signal_ratio_summer": "flex_signal_ratio_summer",
    "flex_GSRU": "flex_GSRU",
    "flex_GSRI": "flex_GSRI",
    "flex_GSR": "flex_GSR",
    "PV_own_consumption_direct": "PV_own_consumption_direct",
    "PV_own_consumption_flex": "PV_own_consumption_flex",
    "PV_own_consumption": "PV_own_consumption",
    "EUI_self_sufficiency": "EUI_self_sufficiency",
    "Batt_total_charge": "Batt_total_charge",
    "Batt_total_discharge": "Batt_total_discharge",
    "Batt_charge_losses": "Batt_charge_losses",
    "Batt_discharge_losses": "Batt_discharge_losses",
    "Batt_RTE": "Batt_RTE",
    "Batt_FEC": "Batt_FEC",
    "StatPAX": "StatPAX",
    "mob_annual_milage_district": "mob_annual_milage_district",
    "mob_annual_mileage_PAX": "mob_annual_mileage_PAX",
    "UED_mob_el_target": "UED_mob_el_target",
    "EUI_mob_fossile": "EUI_mob_fossile",
    "EV_FEC": "EV_FEC",
    "UED_mob_el_total": "UED_mob_el_total",
    "UED_mob_el_other": "UED_mob_el_other",
    "EUIev_el_total": "EUIev_el_total",
    "Edhw_th": "Edhw_th",
    "Edhw_el": "Edhw_el",
    "Edhw_aux_el": "Edhw_aux_el",
    "Edhw_1_th": "Edhw_1_th",
    "Edhw_1_el": "Edhw_1_el",
    "Edhw_1_aux_el": "Edhw_1_aux_el",
    "Edhw_2_th": "Edhw_2_th",
    "Edhw_2_el": "Edhw_2_el",
    "Edhw_2_aux_el": "Edhw_2_aux_el",
}

def fill_attrs(obj: object, data: dict[str, object], attr_map: dict[str, str]) -> None:
    for var_name, attr_name in attr_map.items():
        if var_name in data:
            setattr(obj, attr_name, data[var_name])