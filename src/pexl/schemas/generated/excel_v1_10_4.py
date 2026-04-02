"""Auto-generated schema bindings. Do not edit manually."""

from __future__ import annotations
from dataclasses import dataclass

SCHEMA_VERSION = 'v1_10_4'

@dataclass(frozen=True)
class VariableMeta:
    var_name: str
    attr_name: str
    real_name: str | None = None
    unit: str | None = None
    type_name: str | None = None
    comment: str | None = None
    source: str | None = None
    ka: int | None = None
    category: str | None = None
    area: str | None = None
    label: str | None = None
    var_cat: str | None = None

    def __repr__(self) -> str:
        parts = []

        # main identifier
        name = self.var_name
        if self.real_name:
            name += f" ({self.real_name})"

        parts.append(name)

        # unit + type
        if self.unit:
            parts.append(f"[{self.unit}]")
        if self.type_name:
            parts.append(f"<{self.type_name}>")

        # source info
        if self.source:
            parts.append(f"@{self.source}")

        # ka flag (important for your workflow)
        if self.ka is not None:
            parts.append(f"ka={self.ka}")

        return "<VarMeta " + " ".join(parts) + ">"


class ExcelNamedVariables:
    def __init__(self):
        self.ACH_night_m: object | None = None  # var_name: ACH_night_m³
        self.Batt_FEC: object | None = None
        self.Batt_RTE: object | None = None
        self.Batt_SOC_init: object | None = None
        self.Batt_auto_discharge_factor: object | None = None
        self.Batt_c_rate: object | None = None
        self.Batt_cap_Wh_per_NFA: object | None = None
        self.Batt_cap_kWh: object | None = None
        self.Batt_charge_losses: object | None = None
        self.Batt_charging_losses: object | None = None
        self.Batt_discharge_losses: object | None = None
        self.Batt_eff_factor_charge: object | None = None
        self.Batt_eff_factor_discharge: object | None = None
        self.Batt_is_gridcharged: object | None = None
        self.Batt_is_not_used_during_signals: object | None = None
        self.Batt_is_used: object | None = None
        self.Batt_is_used_for_EV: object | None = None
        self.Batt_is_used_for_HVACminimum: object | None = None
        self.Batt_is_used_for_plugloads: object | None = None
        self.Batt_max_power_specific: object | None = None
        self.Batt_self_discharge_rate: object | None = None
        self.Batt_to_Ec_min: object | None = None
        self.Batt_to_Edhw_min: object | None = None
        self.Batt_to_Eev_min: object | None = None
        self.Batt_to_Eh_min: object | None = None
        self.Batt_to_Ev_min: object | None = None
        self.Batt_to_HVAC: object | None = None
        self.Batt_to_plugloads: object | None = None
        self.Batt_total_charge: object | None = None
        self.Batt_total_charge_input: object | None = None
        self.Batt_total_discharge: object | None = None
        self.COMP_area_balconies: object | None = None
        self.COMP_area_basement_ceiling: object | None = None
        self.COMP_area_basement_floor_unheated: object | None = None
        self.COMP_area_ceil_to_air: object | None = None
        self.COMP_area_ceiling_topfloor: object | None = None
        self.COMP_area_columns: object | None = None
        self.COMP_area_fundament: object | None = None
        self.COMP_area_internal_wall_load: object | None = None
        self.COMP_area_internal_wall_nonload: object | None = None
        self.COMP_area_internal_wall_unheated: object | None = None
        self.COMP_area_terrace: object | None = None
        self.COMP_area_unheated_horizontal: object | None = None
        self.COMP_area_wall_earth_contacted: object | None = None
        self.COMP_area_wall_ec_unheated: object | None = None
        self.COMP_area_windowframe: object | None = None
        self.COMP_area_windowglazing: object | None = None
        self.COMP_name_balconies: object | None = None
        self.COMP_name_basement_ceiling: object | None = None
        self.COMP_name_basement_floor_unheated: object | None = None
        self.COMP_name_ceil_to_air: object | None = None
        self.COMP_name_ceiling_topfloor: object | None = None
        self.COMP_name_columns: object | None = None
        self.COMP_name_fundament: object | None = None
        self.COMP_name_internal_wall_load: object | None = None
        self.COMP_name_internal_wall_nonload: object | None = None
        self.COMP_name_internal_wall_unheated: object | None = None
        self.COMP_name_other: object | None = None
        self.COMP_name_terrace: object | None = None
        self.COMP_name_unheated_horizontal: object | None = None
        self.COMP_name_wall_earth_contacted: object | None = None
        self.COMP_name_wall_ec_unheated: object | None = None
        self.COMP_name_windowframe: object | None = None
        self.COMP_name_windowglazing: object | None = None
        self.COMP_name_windows: object | None = None
        self.DHW_1_efficiency: object | None = None
        self.DHW_1_el_aux: object | None = None
        self.DHW_1_incl_distribution_factor: object | None = None
        self.DHW_1_is_electric: object | None = None
        self.DHW_1_is_used: object | None = None
        self.DHW_1_share_office: object | None = None
        self.DHW_1_share_other: object | None = None
        self.DHW_1_share_residential: object | None = None
        self.DHW_1_share_retailfood: object | None = None
        self.DHW_1_share_retailother: object | None = None
        self.DHW_1_share_schoolprim: object | None = None
        self.DHW_1_share_schoolsec: object | None = None
        self.DHW_2_efficiency: object | None = None
        self.DHW_2_el_aux: object | None = None
        self.DHW_2_incl_distribution_factor: object | None = None
        self.DHW_2_is_electric: object | None = None
        self.DHW_2_is_used: object | None = None
        self.DHW_Tmax: object | None = None
        self.DHW_Tmax_input: object | None = None
        self.DHW_Tmin: object | None = None
        self.DHW_carriertype_1: object | None = None
        self.DHW_carriertype_2: object | None = None
        self.DHW_concurrency_office: object | None = None
        self.DHW_concurrency_other: object | None = None
        self.DHW_concurrency_residential: object | None = None
        self.DHW_concurrency_retailfood: object | None = None
        self.DHW_concurrency_retailother: object | None = None
        self.DHW_concurrency_schoolprim: object | None = None
        self.DHW_concurrency_schoolsec: object | None = None
        self.DHW_conversion_1: object | None = None
        self.DHW_conversion_2: object | None = None
        self.DHW_demand_office_kWhm2: object | None = None
        self.DHW_demand_other_kWhm2: object | None = None
        self.DHW_demand_residential_kWhm2: object | None = None
        self.DHW_demand_retailfood_kWhm2: object | None = None
        self.DHW_demand_retailother_kWhm2: object | None = None
        self.DHW_demand_schoolprim_kWhm2: object | None = None
        self.DHW_demand_schoolsec_kWhm2: object | None = None
        self.DHW_efficiency_distribution_1: object | None = None
        self.DHW_efficiency_distribution_2: object | None = None
        self.DHW_losses_1: object | None = None
        self.DHW_losses_2: object | None = None
        self.DHW_occupancy_office: object | None = None
        self.DHW_occupancy_other: object | None = None
        self.DHW_occupancy_residential: object | None = None
        self.DHW_occupancy_retailfood: object | None = None
        self.DHW_occupancy_retailother: object | None = None
        self.DHW_occupancy_schoolprim: object | None = None
        self.DHW_occupancy_schoolsec: object | None = None
        self.DHW_storage_1_liter: object | None = None
        self.DHW_storage_2_liter: object | None = None
        self.DHW_storage_env_temp_default: object | None = None
        self.DHW_storage_liter_pPerson: object | None = None
        self.DHW_thermal_power_1_kW: object | None = None
        self.DHW_thermal_power_Wpl: object | None = None
        self.DHW_thermal_power_pPerson: object | None = None
        self.Daylightcoefficient_office: object | None = None
        self.Daylightcoefficient_schoolprim: object | None = None
        self.Daylightcoefficient_schoolsec: object | None = None
        self.EUI_auxiliary: object | None = None
        self.EUI_biomass: object | None = None
        self.EUI_district_heating: object | None = None
        self.EUI_el_total: object | None = None
        self.EUI_lighting: object | None = None
        self.EUI_mob_fossil: object | None = None
        self.EUI_mob_fossile: object | None = None
        self.EUI_natural_gas: object | None = None
        self.EUI_other: object | None = None
        self.EUI_plugAuxLight: object | None = None
        self.EUI_plugloads: object | None = None
        self.EUI_self_sufficiency: object | None = None
        self.EUIc_2th: object | None = None
        self.EUIc_el: object | None = None
        self.EUIc_el_aux: object | None = None
        self.EUIc_other: object | None = None
        self.EUIdhw_1th: object | None = None
        self.EUIdhw_2th: object | None = None
        self.EUIdhw_biomass: object | None = None
        self.EUIdhw_district_heating: object | None = None
        self.EUIdhw_el: object | None = None
        self.EUIdhw_natural_gas: object | None = None
        self.EUIdhw_other: object | None = None
        self.EUIdhwdirect_el: object | None = None
        self.EUIev_el: object | None = None
        self.EUIev_el_total: object | None = None
        self.EUIh_2th: object | None = None
        self.EUIh_4th: object | None = None
        self.EUIh_biomass: object | None = None
        self.EUIh_district_heating: object | None = None
        self.EUIh_el: object | None = None
        self.EUIh_el_aux: object | None = None
        self.EUIh_natural_gas: object | None = None
        self.EUIh_other: object | None = None
        self.EUIv_el: object | None = None
        self.EV_FEC: object | None = None
        self.EV_battsize_kWh: object | None = None
        self.EV_charging_efficiency: object | None = None
        self.EV_charging_losses_surcharge_factor: object | None = None
        self.EV_charging_station_power: object | None = None
        self.EV_charging_stations: object | None = None
        self.EV_count_residential: object | None = None
        self.EV_count_retail: object | None = None
        self.EV_count_work: object | None = None
        self.EV_demand_kWhpkm: object | None = None
        self.EV_experimental_calculation: object | None = None
        self.EV_max_charging_power_ratio: object | None = None
        self.EV_mileage_res: object | None = None
        self.EV_mileage_retail: object | None = None
        self.EV_mileage_work: object | None = None
        self.EV_self_discharge_per_week: object | None = None
        self.EV_selfdischarge_per_h: object | None = None
        self.EV_share: object | None = None
        self.EV_share_constant_charging: object | None = None
        self.EV_soc_min_discharge: object | None = None
        self.EV_soc_min_ext: object | None = None
        self.EV_soc_min_retail: object | None = None
        self.EV_soc_min_work: object | None = None
        self.EV_soc_minimum: object | None = None
        self.EV_storage_total_kWh: object | None = None
        self.Edhw_1_aux_el: object | None = None
        self.Edhw_1_el: object | None = None
        self.Edhw_1_th: object | None = None
        self.Edhw_2_aux_el: object | None = None
        self.Edhw_2_el: object | None = None
        self.Edhw_2_th: object | None = None
        self.Edhw_aux_el: object | None = None
        self.Edhw_el: object | None = None
        self.Edhw_th: object | None = None
        self.Eev_discharge_loss: object | None = None
        self.Eev_ext_charge: object | None = None
        self.Eev_to_Ec_min: object | None = None
        self.Eev_to_Edhw_min: object | None = None
        self.Eev_to_Eh_min: object | None = None
        self.Eev_to_Ev_min: object | None = None
        self.Eev_to_HVAC: object | None = None
        self.Eev_to_district: object | None = None
        self.Eev_to_plugloads: object | None = None
        self.Ev_scale_office: object | None = None
        self.Ev_scale_other: object | None = None
        self.Ev_scale_residential: object | None = None
        self.Ev_scale_retail_food: object | None = None
        self.Ev_scale_retail_other: object | None = None
        self.Ev_scale_school_prim: object | None = None
        self.Ev_scale_school_sec: object | None = None
        self.FLEX_PV_is_used: object | None = None
        self.FLEX_choice_cool_system: object | None = None
        self.FLEX_choice_heat_system: object | None = None
        self.FLEX_cool1_use: object | None = None
        self.FLEX_cool3_use: object | None = None
        self.FLEX_grid_maxpower_Wm2: object | None = None
        self.FLEX_heat1_use: object | None = None
        self.FLEX_heat3_use: object | None = None
        self.FLEX_is_used: object | None = None
        self.FLEX_is_used_for_HVAC_min: object | None = None
        self.FLEX_is_used_for_ev_min: object | None = None
        self.FLEX_is_used_for_plugloads: object | None = None
        self.FLEX_signal_ID: object | None = None
        self.FLEX_signal_name: object | None = None
        self.FSI: object | None = None
        self.GFA_office: object | None = None
        self.GFA_other: object | None = None
        self.GFA_residential: object | None = None
        self.GFA_retailfood: object | None = None
        self.GFA_retailother: object | None = None
        self.GFA_schoolprim: object | None = None
        self.GFA_schoolsec: object | None = None
        self.GFA_total: object | None = None
        self.GFV: object | None = None
        self.GHG_LCA_timeframe_years: object | None = None
        self.GPW_ceilings_name: object | None = None
        self.GWP_battery_name: object | None = None
        self.GWP_boreholes_name: object | None = None
        self.GWP_direct_biogenic: object | None = None
        self.GWP_direct_biogenic_share: object | None = None
        self.GWP_direct_fossile: object | None = None
        self.GWP_direct_life: object | None = None
        self.GWP_ee_ceilings_biogenic: object | None = None
        self.GWP_ee_ceilings_fossile: object | None = None
        self.GWP_ee_con_build: object | None = None
        self.GWP_ee_con_tga: object | None = None
        self.GWP_ee_direct_biogenic: object | None = None
        self.GWP_ee_direct_fossile: object | None = None
        self.GWP_ee_general: object | None = None
        self.GWP_ee_general_bigonenic: object | None = None
        self.GWP_ee_general_fossile: object | None = None
        self.GWP_ee_ground_biogenic: object | None = None
        self.GWP_ee_ground_fossile: object | None = None
        self.GWP_ee_lc_battery: object | None = None
        self.GWP_ee_lc_biogenic: object | None = None
        self.GWP_ee_lc_boreholes: object | None = None
        self.GWP_ee_lc_ceil: object | None = None
        self.GWP_ee_lc_ceilings_biogenic: object | None = None
        self.GWP_ee_lc_ceilings_fossile: object | None = None
        self.GWP_ee_lc_construction: object | None = None
        self.GWP_ee_lc_direct: object | None = None
        self.GWP_ee_lc_direct_biogenic: object | None = None
        self.GWP_ee_lc_direct_fossile: object | None = None
        self.GWP_ee_lc_fossil: object | None = None
        self.GWP_ee_lc_general_biogenic: object | None = None
        self.GWP_ee_lc_general_fossile: object | None = None
        self.GWP_ee_lc_ground: object | None = None
        self.GWP_ee_lc_ground_biogenic: object | None = None
        self.GWP_ee_lc_ground_fossile: object | None = None
        self.GWP_ee_lc_mob: object | None = None
        self.GWP_ee_lc_other: object | None = None
        self.GWP_ee_lc_other_biogenic: object | None = None
        self.GWP_ee_lc_other_fossile: object | None = None
        self.GWP_ee_lc_pv: object | None = None
        self.GWP_ee_lc_roof: object | None = None
        self.GWP_ee_lc_roof_biogenic: object | None = None
        self.GWP_ee_lc_roof_fossile: object | None = None
        self.GWP_ee_lc_solarthermal: object | None = None
        self.GWP_ee_lc_storage: object | None = None
        self.GWP_ee_lc_tga: object | None = None
        self.GWP_ee_lc_tga_general: object | None = None
        self.GWP_ee_lc_tga_other: object | None = None
        self.GWP_ee_lc_ventilation: object | None = None
        self.GWP_ee_lc_walls: object | None = None
        self.GWP_ee_lc_walls_biogenic: object | None = None
        self.GWP_ee_lc_walls_fossil: object | None = None
        self.GWP_ee_lc_windows: object | None = None
        self.GWP_ee_lc_windows_biogenic: object | None = None
        self.GWP_ee_lc_windows_fossile: object | None = None
        self.GWP_ee_mob_ev: object | None = None
        self.GWP_ee_mob_fossile: object | None = None
        self.GWP_ee_other_biogenic: object | None = None
        self.GWP_ee_other_fossile: object | None = None
        self.GWP_ee_rep_build: object | None = None
        self.GWP_ee_rep_tga: object | None = None
        self.GWP_ee_roof_biogenic: object | None = None
        self.GWP_ee_roof_fossile: object | None = None
        self.GWP_ee_tga_battery_biogenic: object | None = None
        self.GWP_ee_tga_battery_fossile: object | None = None
        self.GWP_ee_tga_boreholes_biogenic: object | None = None
        self.GWP_ee_tga_boreholes_fossile: object | None = None
        self.GWP_ee_tga_general_biogenic: object | None = None
        self.GWP_ee_tga_general_fossile: object | None = None
        self.GWP_ee_tga_other_biogenic: object | None = None
        self.GWP_ee_tga_other_fossile: object | None = None
        self.GWP_ee_tga_pv_biogenic: object | None = None
        self.GWP_ee_tga_pv_fossile: object | None = None
        self.GWP_ee_tga_solarthermal_biogenic: object | None = None
        self.GWP_ee_tga_solarthermal_fossile: object | None = None
        self.GWP_ee_tga_storage_biogenic: object | None = None
        self.GWP_ee_tga_storage_fossile: object | None = None
        self.GWP_ee_tga_ventilation_biogenic: object | None = None
        self.GWP_ee_tga_ventilation_fossile: object | None = None
        self.GWP_ee_walls_biogenic: object | None = None
        self.GWP_ee_walls_fossile: object | None = None
        self.GWP_ee_windows_bigenic: object | None = None
        self.GWP_ee_windows_fossile: object | None = None
        self.GWP_emInt_PV_feedin: object | None = None
        self.GWP_emInt_batt_charge: object | None = None
        self.GWP_emInt_ev_charge: object | None = None
        self.GWP_emInt_flex: object | None = None
        self.GWP_emInt_grid: object | None = None
        self.GWP_emInt_grid_avg: object | None = None
        self.GWP_general_name: object | None = None
        self.GWP_ground_name: object | None = None
        self.GWP_lc_EE_total: object | None = None
        self.GWP_lc_OE_total: object | None = None
        self.GWP_lc_total: object | None = None
        self.GWP_life_battery: object | None = None
        self.GWP_life_ceilings: object | None = None
        self.GWP_life_direct: object | None = None
        self.GWP_life_general: object | None = None
        self.GWP_life_ground: object | None = None
        self.GWP_life_other: object | None = None
        self.GWP_life_roof: object | None = None
        self.GWP_life_solarthermal: object | None = None
        self.GWP_life_storage: object | None = None
        self.GWP_life_tga_boreholes: object | None = None
        self.GWP_life_tga_general: object | None = None
        self.GWP_life_tga_other: object | None = None
        self.GWP_life_tga_pv: object | None = None
        self.GWP_life_tga_ventilation: object | None = None
        self.GWP_life_walls: object | None = None
        self.GWP_life_windows: object | None = None
        self.GWP_miv_count_ev: object | None = None
        self.GWP_miv_count_fossile: object | None = None
        self.GWP_mobility_car_gpPKm: object | None = None
        self.GWP_mobility_construction_ev: object | None = None
        self.GWP_mobility_construction_fossil: object | None = None
        self.GWP_mobility_moped_gpPKm: object | None = None
        self.GWP_oe: object | None = None
        self.GWP_oe_battery_charge: object | None = None
        self.GWP_oe_biomass: object | None = None
        self.GWP_oe_building: object | None = None
        self.GWP_oe_district_heating: object | None = None
        self.GWP_oe_flex_build: object | None = None
        self.GWP_oe_grid_build: object | None = None
        self.GWP_oe_grid_feedin: object | None = None
        self.GWP_oe_lc_biomass: object | None = None
        self.GWP_oe_lc_building: object | None = None
        self.GWP_oe_lc_district_heating: object | None = None
        self.GWP_oe_lc_emission: object | None = None
        self.GWP_oe_lc_emission_savings: object | None = None
        self.GWP_oe_lc_flex_build: object | None = None
        self.GWP_oe_lc_grid_build: object | None = None
        self.GWP_oe_lc_grid_feedin: object | None = None
        self.GWP_oe_lc_mob: object | None = None
        self.GWP_oe_lc_mob_ev: object | None = None
        self.GWP_oe_lc_mob_export: object | None = None
        self.GWP_oe_lc_mob_fossile: object | None = None
        self.GWP_oe_lc_natural_gas: object | None = None
        self.GWP_oe_lc_other: object | None = None
        self.GWP_oe_mob: object | None = None
        self.GWP_oe_mob_ev: object | None = None
        self.GWP_oe_mob_ev_export: object | None = None
        self.GWP_oe_mob_fossile: object | None = None
        self.GWP_oe_natural_gas: object | None = None
        self.GWP_oe_other: object | None = None
        self.GWP_other_name: object | None = None
        self.GWP_pv_name: object | None = None
        self.GWP_rcpi_biomass: object | None = None
        self.GWP_rcpi_district_heating: object | None = None
        self.GWP_rcpi_fossil: object | None = None
        self.GWP_rcpi_grid: object | None = None
        self.GWP_rcpi_grid_substition: object | None = None
        self.GWP_rcpi_mob_fossile: object | None = None
        self.GWP_rcpi_natural_gas: object | None = None
        self.GWP_rcpi_renewable: object | None = None
        self.GWP_ref_area_ceilings: object | None = None
        self.GWP_ref_area_fundament: object | None = None
        self.GWP_ref_area_roof: object | None = None
        self.GWP_ref_area_walls: object | None = None
        self.GWP_ref_area_windows: object | None = None
        self.GWP_refratio_boreholes: object | None = None
        self.GWP_refratio_ceilings: object | None = None
        self.GWP_refratio_fundament: object | None = None
        self.GWP_refratio_pv: object | None = None
        self.GWP_refratio_roof: object | None = None
        self.GWP_refratio_walls: object | None = None
        self.GWP_refratio_windows: object | None = None
        self.GWP_roof_name: object | None = None
        self.GWP_solarthermal_name: object | None = None
        self.GWP_storage_name: object | None = None
        self.GWP_tga_general_name: object | None = None
        self.GWP_tga_other_name: object | None = None
        self.GWP_ventilation_name: object | None = None
        self.GWP_walls_name: object | None = None
        self.Grid_to_Ec_min: object | None = None
        self.Grid_to_Edhw_min: object | None = None
        self.Grid_to_Eev_min: object | None = None
        self.Grid_to_Eh_min: object | None = None
        self.Grid_to_Ev_min: object | None = None
        self.Grid_to_building_min: object | None = None
        self.Grid_to_min: object | None = None
        self.Grid_to_plugloads: object | None = None
        self.Grid_total_flexandnotflex: object | None = None
        self.NFA_cooled: object | None = None
        self.NFA_mechvent: object | None = None
        self.NFA_office: object | None = None
        self.NFA_other: object | None = None
        self.NFA_residential: object | None = None
        self.NFA_retailfood: object | None = None
        self.NFA_retailother: object | None = None
        self.NFA_schoolprim: object | None = None
        self.NFA_schoolsec: object | None = None
        self.NFA_to_GFA_ratio: object | None = None
        self.NFA_to_GFA_ratio_office: object | None = None
        self.NFA_to_GFA_ratio_other: object | None = None
        self.NFA_to_GFA_ratio_residential: object | None = None
        self.NFA_to_GFA_ratio_retailfood: object | None = None
        self.NFA_to_GFA_ratio_retailother: object | None = None
        self.NFA_to_GFA_ratio_schoolprim: object | None = None
        self.NFA_to_GFA_ratio_schoolsec: object | None = None
        self.NFA_total: object | None = None
        self.NFA_windowvent: object | None = None
        self.NFAfrac_c: object | None = None
        self.NFAfrac_u: object | None = None
        self.NFV_c: object | None = None
        self.NFV_mechvent: object | None = None
        self.NFV_total: object | None = None
        self.NFV_u: object | None = None
        self.NFV_windowvent: object | None = None
        self.PEI_balance: object | None = None
        self.PEI_biomass: object | None = None
        self.PEI_cf_density: object | None = None
        self.PEI_cf_mobility: object | None = None
        self.PEI_cf_renovation: object | None = None
        self.PEI_demand: object | None = None
        self.PEI_district_heating: object | None = None
        self.PEI_el_hvac: object | None = None
        self.PEI_el_plugloads: object | None = None
        self.PEI_evExtCharge_import: object | None = None
        self.PEI_evOtherTravel_export: object | None = None
        self.PEI_export: object | None = None
        self.PEI_flex_import: object | None = None
        self.PEI_grid_import: object | None = None
        self.PEI_import: object | None = None
        self.PEI_importExport_balance: object | None = None
        self.PEI_mob_el: object | None = None
        self.PEI_mob_fossile: object | None = None
        self.PEI_mob_total: object | None = None
        self.PEI_natural_gas: object | None = None
        self.PEI_other: object | None = None
        self.PEI_pv_export: object | None = None
        self.PEI_saldo_project: object | None = None
        self.PEI_saldo_target: object | None = None
        self.PEI_storage_losses: object | None = None
        self.PEI_sub_PV: object | None = None
        self.PEI_sub_flex: object | None = None
        self.PV_efficiency: object | None = None
        self.PV_id: object | None = None
        self.PV_is_used: object | None = None
        self.PV_kWp: object | None = None
        self.PV_m2_per_kWp: object | None = None
        self.PV_module_area: object | None = None
        self.PV_own_consumption: object | None = None
        self.PV_own_consumption_direct: object | None = None
        self.PV_own_consumption_flex: object | None = None
        self.PV_profile_name: object | None = None
        self.PV_scale: object | None = None
        self.PV_to_Batt: object | None = None
        self.PV_to_Ec_flex: object | None = None
        self.PV_to_Ec_min: object | None = None
        self.PV_to_Edhw: object | None = None
        self.PV_to_Edhw_direct: object | None = None
        self.PV_to_Edhw_min: object | None = None
        self.PV_to_Eev_flex: object | None = None
        self.PV_to_Eev_min: object | None = None
        self.PV_to_Egrid: object | None = None
        self.PV_to_Eh_flex: object | None = None
        self.PV_to_Eh_min: object | None = None
        self.PV_to_Ev_min: object | None = None
        self.PV_to_plugloads: object | None = None
        self.PV_total: object | None = None
        self.PV_total_direct: object | None = None
        self.PV_total_flex: object | None = None
        self.Plight_max_office: object | None = None
        self.Plight_max_schoolprim: object | None = None
        self.Plight_max_schoolsec: object | None = None
        self.Plight_min_office: object | None = None
        self.Plight_min_schoolprim: object | None = None
        self.Plight_min_schoolsec: object | None = None
        self.Plugloads_scale_office: object | None = None
        self.Plugloads_scale_other: object | None = None
        self.Plugloads_scale_res: object | None = None
        self.Plugloads_scale_retailfood: object | None = None
        self.Plugloads_scale_retailother: object | None = None
        self.Plugloads_scale_schoolprim: object | None = None
        self.Plugloads_scale_schoolsec: object | None = None
        self.QC: object | None = None
        self.QC_aux_1el: object | None = None
        self.QC_aux_2th: object | None = None
        self.QC_aux_3el: object | None = None
        self.QC_aux_fc: object | None = None
        self.QC_c: object | None = None
        self.QC_distr_losses_1el: object | None = None
        self.QC_distr_losses_2th: object | None = None
        self.QC_distr_losses_3el: object | None = None
        self.QC_flex_c: object | None = None
        self.QC_flex_summer: object | None = None
        self.QC_flex_winter: object | None = None
        self.QC_flexanteil: object | None = None
        self.QC_flexshare_summer: object | None = None
        self.QC_flexshare_winter: object | None = None
        self.QC_generation_eff_2th: object | None = None
        self.QC_min_c: object | None = None
        self.QC_min_summer: object | None = None
        self.QC_min_winter: object | None = None
        self.QC_summer: object | None = None
        self.QC_to_EC_1: object | None = None
        self.QC_to_EC_3: object | None = None
        self.QC_winter: object | None = None
        self.QCmax_1el: object | None = None
        self.QCmax_2th: object | None = None
        self.QCmax_3el: object | None = None
        self.QCmax_freecooling: object | None = None
        self.QCmax_room_MW: object | None = None
        self.QCmax_room_m2: object | None = None
        self.QH: object | None = None
        self.QH_aux_el_to_th_1el: object | None = None
        self.QH_aux_el_to_th_2th: object | None = None
        self.QH_aux_el_to_th_3el: object | None = None
        self.QH_aux_el_to_th_4th: object | None = None
        self.QH_aux_wasteheat: object | None = None
        self.QH_c: object | None = None
        self.QH_distr_loss_1el: object | None = None
        self.QH_distr_loss_2th: object | None = None
        self.QH_distr_loss_3el: object | None = None
        self.QH_distr_loss_4th: object | None = None
        self.QH_flex_c: object | None = None
        self.QH_flex_summer: object | None = None
        self.QH_flex_u: object | None = None
        self.QH_flex_winter: object | None = None
        self.QH_flexanteil_c: object | None = None
        self.QH_flexanteil_u: object | None = None
        self.QH_flexshare_summer: object | None = None
        self.QH_flexshare_winter: object | None = None
        self.QH_generation_eff_1el: object | None = None
        self.QH_generation_eff_2th: object | None = None
        self.QH_generation_eff_3el: object | None = None
        self.QH_generation_eff_4th: object | None = None
        self.QH_min_c: object | None = None
        self.QH_min_summer: object | None = None
        self.QH_min_u: object | None = None
        self.QH_min_winter: object | None = None
        self.QH_summer: object | None = None
        self.QH_u: object | None = None
        self.QH_winter: object | None = None
        self.QHmax_1el_m2: object | None = None
        self.QHmax_2th_m2: object | None = None
        self.QHmax_3el_m2: object | None = None
        self.QHmax_4th_m2: object | None = None
        self.QHmax_room_MW: object | None = None
        self.QHmax_room_m: object | None = None  # var_name: QHmax_room_m²
        self.QI: object | None = None
        self.QI_c: object | None = None
        self.QI_summer: object | None = None
        self.QI_u: object | None = None
        self.QI_winter: object | None = None
        self.QS: object | None = None
        self.QS_c: object | None = None
        self.QS_max_shading_c: object | None = None
        self.QS_max_shading_u: object | None = None
        self.QS_summer: object | None = None
        self.QS_u: object | None = None
        self.QS_winter: object | None = None
        self.QT: object | None = None
        self.QT_c: object | None = None
        self.QT_ground_c: object | None = None
        self.QT_ground_summer: object | None = None
        self.QT_ground_u: object | None = None
        self.QT_ground_winter: object | None = None
        self.QT_psi_c: object | None = None
        self.QT_psi_summer: object | None = None
        self.QT_psi_u: object | None = None
        self.QT_psi_winter: object | None = None
        self.QT_roof_c: object | None = None
        self.QT_roof_summer: object | None = None
        self.QT_roof_u: object | None = None
        self.QT_roof_winter: object | None = None
        self.QT_summer: object | None = None
        self.QT_u: object | None = None
        self.QT_wall_c: object | None = None
        self.QT_wall_summer: object | None = None
        self.QT_wall_u: object | None = None
        self.QT_wall_winter: object | None = None
        self.QT_window_c: object | None = None
        self.QT_window_summer: object | None = None
        self.QT_window_u: object | None = None
        self.QT_window_winter: object | None = None
        self.QT_winter: object | None = None
        self.QV: object | None = None
        self.QV_c: object | None = None
        self.QV_heatrecovery: object | None = None
        self.QV_heatrecovery_c: object | None = None
        self.QV_heatrecovery_summer: object | None = None
        self.QV_heatrecovery_u: object | None = None
        self.QV_heatrecovery_winter: object | None = None
        self.QV_inf_c: object | None = None
        self.QV_inf_summer: object | None = None
        self.QV_inf_u: object | None = None
        self.QV_inf_winter: object | None = None
        self.QV_mechvent_c: object | None = None
        self.QV_mechvent_summer: object | None = None
        self.QV_mechvent_u: object | None = None
        self.QV_mechvent_winter: object | None = None
        self.QV_summer: object | None = None
        self.QV_u: object | None = None
        self.QV_window_c: object | None = None
        self.QV_window_summer: object | None = None
        self.QV_window_u: object | None = None
        self.QV_window_winter: object | None = None
        self.QV_winter: object | None = None
        self.QVn: object | None = None
        self.QVn_c: object | None = None
        self.QVn_summer: object | None = None
        self.QVn_u: object | None = None
        self.QVn_winter: object | None = None
        self.StatPAX: object | None = None
        self.StatPAX_eduprim: object | None = None
        self.StatPAX_edusec: object | None = None
        self.StatPAX_office: object | None = None
        self.StatPAX_res: object | None = None
        self.StatPAX_retail: object | None = None
        self.StatPAX_retailother: object | None = None
        self.Ta_annual_avg: object | None = None
        self.Ta_avg_cooling_period: object | None = None
        self.Ta_avg_heating_period: object | None = None
        self.Tc_avg_summer: object | None = None
        self.Tc_avg_winter: object | None = None
        self.Tsetcool_flex: object | None = None
        self.Tsetcool_max: object | None = None
        self.Tsetheat_flex: object | None = None
        self.Tsetheat_min: object | None = None
        self.Tu_avg_summer: object | None = None
        self.Tu_avg_winter: object | None = None
        self.UED_auxiliary: object | None = None
        self.UED_cooling: object | None = None
        self.UED_dhw: object | None = None
        self.UED_heating: object | None = None
        self.UED_lighting: object | None = None
        self.UED_mim_electric: object | None = None
        self.UED_mim_fossile: object | None = None
        self.UED_mob_el_other: object | None = None
        self.UED_mob_el_target: object | None = None
        self.UED_mob_el_total: object | None = None
        self.UED_plugloads: object | None = None
        self.UED_ventilation: object | None = None
        self.VRGrid_to_Batt: object | None = None
        self.VRGrid_to_Ec_flex: object | None = None
        self.VRGrid_to_Ec_min: object | None = None
        self.VRGrid_to_Edhw_flex: object | None = None
        self.VRGrid_to_Edhw_min: object | None = None
        self.VRGrid_to_Eev_flex: object | None = None
        self.VRGrid_to_Eev_min: object | None = None
        self.VRGrid_to_Eh_flex: object | None = None
        self.VRGrid_to_Eh_min: object | None = None
        self.VRGrid_to_Ev_min: object | None = None
        self.VRGrid_to_building: object | None = None
        self.VRGrid_to_flex: object | None = None
        self.VRGrid_to_min: object | None = None
        self.VRGrid_to_plugloads: object | None = None
        self.Vent_share_mech_cooled: object | None = None
        self.Vent_share_mech_uncooled: object | None = None
        self.Vent_share_window_cooled: object | None = None
        self.Vent_share_window_uncooled: object | None = None
        self.aux_el_demand_office_kWhm2: object | None = None
        self.aux_el_demand_other_kWhm2: object | None = None
        self.aux_el_demand_residential_kWhm2: object | None = None
        self.aux_el_demand_retailfood_kWhm2: object | None = None
        self.aux_el_demand_retailother_kWhm2: object | None = None
        self.aux_el_demand_schoolprim_kWhm2: object | None = None
        self.aux_el_demand_schoolsec_kWhm2: object | None = None
        self.borehole_count: object | None = None
        self.building_count: object | None = None
        self.cfd_A: object | None = None
        self.cfd_EUI: object | None = None
        self.cfd_cutoff: object | None = None
        self.cfd_dx: object | None = None
        self.cfd_fPE: object | None = None
        self.cfm_budget_office: object | None = None
        self.cfm_budget_residential: object | None = None
        self.cfm_budget_retail: object | None = None
        self.cfm_budget_school: object | None = None
        self.cfr_budget: object | None = None
        self.context_factor_density: object | None = None
        self.context_factor_mobility: object | None = None
        self.context_factor_renovation: object | None = None
        self.cool_cop_1el: object | None = None
        self.cool_cop_2th: object | None = None
        self.cool_cop_3el: object | None = None
        self.cool_share_office: object | None = None
        self.cool_share_other: object | None = None
        self.cool_share_residential: object | None = None
        self.cool_share_retailfood: object | None = None
        self.cool_share_retailother: object | None = None
        self.cool_share_schoolprim: object | None = None
        self.cool_share_schoolsec: object | None = None
        self.cool_th2_carrier_type: object | None = None
        self.cool_th2_is_bio: object | None = None
        self.cool_th2_is_dh: object | None = None
        self.cool_th2_is_ng: object | None = None
        self.cool_th2_is_other: object | None = None
        self.cooling_month1: object | None = None
        self.cooling_month10: object | None = None
        self.cooling_month11: object | None = None
        self.cooling_month12: object | None = None
        self.cooling_month2: object | None = None
        self.cooling_month3: object | None = None
        self.cooling_month4: object | None = None
        self.cooling_month5: object | None = None
        self.cooling_month6: object | None = None
        self.cooling_month7: object | None = None
        self.cooling_month8: object | None = None
        self.cooling_month9: object | None = None
        self.cost_E_grid: object | None = None
        self.cost_PV_to_Egrid: object | None = None
        self.cost_VRGrid_flex: object | None = None
        self.cost_total: object | None = None
        self.dTc_summer: object | None = None
        self.dTc_winter: object | None = None
        self.dTu_summer: object | None = None
        self.dTu_winter: object | None = None
        self.daylightcontr_office: object | None = None
        self.daylightcontr_schoolprim: object | None = None
        self.daylightcontr_schoolsec: object | None = None
        self.density_NFApPers_edu: object | None = None
        self.density_NFApPers_edu_rpim: object | None = None
        self.density_NFApPers_office: object | None = None
        self.density_NFApPers_residential: object | None = None
        self.density_NFApPers_retail: object | None = None
        self.density_NFApPers_retail_other: object | None = None
        self.dhw1_is_bio: object | None = None
        self.dhw1_is_dh: object | None = None
        self.dhw1_is_ng: object | None = None
        self.dhw1_is_other: object | None = None
        self.dhw2_is_bio: object | None = None
        self.dhw2_is_dh: object | None = None
        self.dhw2_is_ng: object | None = None
        self.dhw2_is_other: object | None = None
        self.district_heating_conversion_profile: object | None = None
        self.e_kWhm2a: object | None = None
        self.ev_bidirectional_use: object | None = None
        self.fGHG_grid_column: object | None = None
        self.fGHG_grid_profile: object | None = None
        self.fPE_eff: object | None = None
        self.fPE_flex_factor: object | None = None
        self.fPE_grid: object | None = None
        self.fPE_grid_column: object | None = None
        self.fPE_grid_profile: object | None = None
        self.fc_c: object | None = None
        self.fc_eduprim: object | None = None
        self.fc_edusec: object | None = None
        self.fc_office: object | None = None
        self.fc_other: object | None = None
        self.fc_residential: object | None = None
        self.fc_retailfood: object | None = None
        self.fc_retailother: object | None = None
        self.fc_u: object | None = None
        self.flex_GSR: object | None = None
        self.flex_GSRI: object | None = None
        self.flex_GSRU: object | None = None
        self.flex_Signals_selected_column: object | None = None
        self.flex_cool_dT: object | None = None
        self.flex_dhw_use: object | None = None
        self.flex_heat_dT: object | None = None
        self.flex_signal_ratio: object | None = None
        self.flex_signal_ratio_summer: object | None = None
        self.flex_signal_ratio_winter: object | None = None
        self.fossile_demand_kWhpkm: object | None = None
        self.grid_rcp1: object | None = None
        self.grid_rcp2: object | None = None
        self.grid_rcp3: object | None = None
        self.heat_cap_eff_cooled_m2: object | None = None
        self.heat_cap_eff_uncooled_m2: object | None = None
        self.heat_capacity_effective_m: object | None = None  # var_name: heat_capacity_effective_m²
        self.heat_cop_1el: object | None = None
        self.heat_cop_2th: object | None = None
        self.heat_cop_3el: object | None = None
        self.heat_cop_4th: object | None = None
        self.heat_th2_carrier_type: object | None = None
        self.heat_th2_is_bio: object | None = None
        self.heat_th2_is_dh: object | None = None
        self.heat_th2_is_ng: object | None = None
        self.heat_th2_is_other: object | None = None
        self.heat_th4_carrier_type: object | None = None
        self.heat_th4_is_bio: object | None = None
        self.heat_th4_is_dh: object | None = None
        self.heat_th4_is_ng: object | None = None
        self.heat_th4_is_other: object | None = None
        self.heating_month1: object | None = None
        self.heating_month10: object | None = None
        self.heating_month11: object | None = None
        self.heating_month12: object | None = None
        self.heating_month2: object | None = None
        self.heating_month3: object | None = None
        self.heating_month4: object | None = None
        self.heating_month5: object | None = None
        self.heating_month6: object | None = None
        self.heating_month7: object | None = None
        self.heating_month8: object | None = None
        self.heating_month9: object | None = None
        self.hull_ext_wall_wo_window_m2: object | None = None
        self.hull_fenestration_rate: object | None = None
        self.hull_fundament_m2: object | None = None
        self.hull_m2: object | None = None
        self.hull_roof_m2: object | None = None
        self.hull_transmittance_fundament: object | None = None
        self.hull_transmittance_heatbridge: object | None = None
        self.hull_transmittance_roof: object | None = None
        self.hull_transmittance_walls: object | None = None
        self.hull_transmittance_windows_east: object | None = None
        self.hull_transmittance_windows_horizontal: object | None = None
        self.hull_transmittance_windows_north: object | None = None
        self.hull_transmittance_windows_south: object | None = None
        self.hull_transmittance_windows_west: object | None = None
        self.hull_window_m2: object | None = None
        self.hull_windows_east_m2: object | None = None
        self.hull_windows_horizontal_m2: object | None = None
        self.hull_windows_north_m2: object | None = None
        self.hull_windows_south_m2: object | None = None
        self.hull_windows_west_m2: object | None = None
        self.illuminance_efficiency_dirt: object | None = None
        self.illuminance_efficiency_glazing_ratio: object | None = None
        self.illuminance_min_office: object | None = None
        self.illuminance_min_other: object | None = None
        self.illuminance_min_residential: object | None = None
        self.illuminance_min_retailfood: object | None = None
        self.illuminance_min_retailother: object | None = None
        self.illuminance_min_schoolprim: object | None = None
        self.illuminance_min_schoolsec: object | None = None
        self.input_version_date: object | None = None
        self.input_version_number: object | None = None
        self.irradiation_opaque_surcharge: object | None = None
        self.lc: object | None = None
        self.lighting_factor_office: object | None = None
        self.lighting_factor_other: object | None = None
        self.lighting_factor_retailfood: object | None = None
        self.lighting_factor_retailother: object | None = None
        self.lighting_factor_schoolprim: object | None = None
        self.lighting_factor_schoolsec: object | None = None
        self.location_address: object | None = None
        self.location_postcode: object | None = None
        self.mob_annual_milage_district: object | None = None
        self.mob_annual_mileage_PAX: object | None = None
        self.mob_motorization_perNFA_residential: object | None = None
        self.mob_motorization_perNFA_retail: object | None = None
        self.mob_motorization_perNFA_work: object | None = None
        self.mob_pkm_factor: object | None = None
        self.mob_shading_factor_c: object | None = None
        self.mob_shading_factor_u: object | None = None
        self.mob_simultaneity_edu: object | None = None
        self.mob_simultaneity_office: object | None = None
        self.mob_simultaneity_retail: object | None = None
        self.mobility_is_included: object | None = None
        self.mobility_mode: object | None = None
        self.mobility_region: object | None = None
        self.mobility_vehicle_count: object | None = None
        self.mobshare_office: object | None = None
        self.mobshare_residential: object | None = None
        self.mobshare_retail: object | None = None
        self.mobshare_school: object | None = None
        self.moped_factor: object | None = None
        self.municipality_name: object | None = None
        self.pe_conversion_factor_gasoline: object | None = None
        self.per_NFA: object | None = None
        self.pkm_bike: object | None = None
        self.pkm_bus: object | None = None
        self.pkm_car_driver: object | None = None
        self.pkm_car_passenger: object | None = None
        self.pkm_distancebus: object | None = None
        self.pkm_mofa: object | None = None
        self.pkm_pedestrian: object | None = None
        self.pkm_train: object | None = None
        self.pkm_tram_metro: object | None = None
        self.plot_area: object | None = None
        self.project_creation_date: object | None = None
        self.project_description: object | None = None
        self.project_name: object | None = None
        self.project_scenario_name: object | None = None
        self.project_url: object | None = None
        self.rcp1_dh: object | None = None
        self.rcp1_fossil: object | None = None
        self.rcp1_renewable: object | None = None
        self.rcp2_dh: object | None = None
        self.rcp2_fossil: object | None = None
        self.rcp2_renewable: object | None = None
        self.rcp3_dh: object | None = None
        self.rcp3_fossil: object | None = None
        self.rcp3_renewable: object | None = None
        self.renovation_ratio_office: object | None = None
        self.renovation_ratio_other: object | None = None
        self.renovation_ratio_residential: object | None = None
        self.renovation_ratio_retailfood: object | None = None
        self.renovation_ratio_retailother: object | None = None
        self.renovation_ratio_schoolprim: object | None = None
        self.renovation_ratio_schoolsec: object | None = None
        self.renovation_share: object | None = None
        self.rh_avg: object | None = None
        self.rh_ceiling: object | None = None
        self.rh_office: object | None = None
        self.rh_other: object | None = None
        self.rh_residential: object | None = None
        self.rh_retailfood: object | None = None
        self.rh_retailother: object | None = None
        self.rh_schoolprim: object | None = None
        self.rh_schoolsec: object | None = None
        self.scenario_version: object | None = None
        self.storey_count_avg: object | None = None
        self.test_NFV_shares: object | None = None
        self.test_heat_balance: object | None = None
        self.transmittance_MW: object | None = None
        self.transmittance_Wm: object | None = None  # var_name: transmittance_Wm²
        self.usage_concurrency_summer_eduprim: object | None = None
        self.usage_concurrency_summer_edusec: object | None = None
        self.usage_concurrency_summer_office: object | None = None
        self.usage_concurrency_summer_other: object | None = None
        self.usage_concurrency_summer_res: object | None = None
        self.usage_concurrency_summer_retailfood: object | None = None
        self.usage_concurrency_summer_retailother: object | None = None
        self.usage_concurrency_winter_eduprim: object | None = None
        self.usage_concurrency_winter_edusec: object | None = None
        self.usage_concurrency_winter_office: object | None = None
        self.usage_concurrency_winter_other: object | None = None
        self.usage_concurrency_winter_res: object | None = None
        self.usage_concurrency_winter_retailfood: object | None = None
        self.usage_concurrency_winter_retailother: object | None = None
        self.vent_ach_max_office: object | None = None
        self.vent_ach_max_other: object | None = None
        self.vent_ach_max_residential: object | None = None
        self.vent_ach_max_retailfood: object | None = None
        self.vent_ach_max_retailother: object | None = None
        self.vent_ach_max_schoolprim: object | None = None
        self.vent_ach_max_schoolsec: object | None = None
        self.vent_air_tightness: object | None = None
        self.vent_heat_recovery_summer_office: object | None = None
        self.vent_heat_recovery_summer_other: object | None = None
        self.vent_heat_recovery_summer_residential: object | None = None
        self.vent_heat_recovery_summer_retailfood: object | None = None
        self.vent_heat_recovery_summer_retailother: object | None = None
        self.vent_heat_recovery_summer_schoolprim: object | None = None
        self.vent_heat_recovery_summer_schoolsec: object | None = None
        self.vent_heat_recovery_winter_office: object | None = None
        self.vent_heat_recovery_winter_other: object | None = None
        self.vent_heat_recovery_winter_residential: object | None = None
        self.vent_heat_recovery_winter_retailfood: object | None = None
        self.vent_heat_recovery_winter_retailother: object | None = None
        self.vent_heat_recovery_winter_schoolprim: object | None = None
        self.vent_heat_recovery_winter_schoolsec: object | None = None
        self.vent_infiltration_ACH: object | None = None
        self.vent_night_office: object | None = None
        self.vent_night_other: object | None = None
        self.vent_night_residential: object | None = None
        self.vent_night_retailfood: object | None = None
        self.vent_night_retailother: object | None = None
        self.vent_night_schoolprim: object | None = None
        self.vent_night_schoolsec: object | None = None
        self.vent_scale_office: object | None = None
        self.vent_scale_other: object | None = None
        self.vent_scale_residential: object | None = None
        self.vent_scale_retail: object | None = None
        self.vent_scale_school_prim: object | None = None
        self.vent_scale_school_sec: object | None = None
        self.vent_scale_supermarket: object | None = None
        self.vent_share_mechanical_office: object | None = None
        self.vent_share_mechanical_other: object | None = None
        self.vent_share_mechanical_residential: object | None = None
        self.vent_share_mechanical_retailfood: object | None = None
        self.vent_share_mechanical_retailother: object | None = None
        self.vent_share_mechanical_schoolprim: object | None = None
        self.vent_share_mechanical_schoolsec: object | None = None
        self.vent_tightness_ratio_blowerdoor_to_real: object | None = None
        self.weather_index: object | None = None
        self.weather_name: object | None = None
        self.window_irradiation_factor_summer_east: object | None = None
        self.window_irradiation_factor_summer_horizontal: object | None = None
        self.window_irradiation_factor_summer_north: object | None = None
        self.window_irradiation_factor_summer_south: object | None = None
        self.window_irradiation_factor_summer_west: object | None = None
        self.window_irradiation_factor_winter_east: object | None = None
        self.window_irradiation_factor_winter_horizontal: object | None = None
        self.window_irradiation_factor_winter_north: object | None = None
        self.window_irradiation_factor_winter_south: object | None = None
        self.window_irradiation_factor_winter_west: object | None = None
        self.window_total_transmittance_east: object | None = None
        self.window_total_transmittance_horizontal: object | None = None
        self.window_total_transmittance_north: object | None = None
        self.window_total_transmittance_south: object | None = None
        self.window_total_transmittance_west: object | None = None
        self.year_rcp0: object | None = None
        self.year_rcp1: object | None = None
        self.year_rcp2: object | None = None
        self.year_rcp3: object | None = None

class Meta:
    def __init__(self):
        self.ACH_night_m = VariableMeta(
            var_name='ACH_night_m³', 
            attr_name='ACH_night_m', 
            real_name='Nachtauskühlung Luftwechsel', 
            unit='m³/h', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_FEC = VariableMeta(
            var_name='Batt_FEC', 
            attr_name='Batt_FEC', 
            real_name='Batterie Volladezyklen', 
            unit='x', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Batterienutzung', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_RTE = VariableMeta(
            var_name='Batt_RTE', 
            attr_name='Batt_RTE', 
            real_name='Round-Trip- Efficiency', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Batterienutzung', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_SOC_init = VariableMeta(
            var_name='Batt_SOC_init', 
            attr_name='Batt_SOC_init', 
            real_name='Batterie Initialer SOC', 
            unit='%', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_auto_discharge_factor = VariableMeta(
            var_name='Batt_auto_discharge_factor', 
            attr_name='Batt_auto_discharge_factor', 
            real_name='Batterie Selbstentladung pro Stunde', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_c_rate = VariableMeta(
            var_name='Batt_c_rate', 
            attr_name='Batt_c_rate', 
            real_name='Maximale Be/Entladeleistung', 
            unit='%', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_cap_Wh_per_NFA = VariableMeta(
            var_name='Batt_cap_Wh_per_NFA', 
            attr_name='Batt_cap_Wh_per_NFA', 
            real_name='Batterie Kapazität spezifisch', 
            unit='W/m²', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_cap_kWh = VariableMeta(
            var_name='Batt_cap_kWh', 
            attr_name='Batt_cap_kWh', 
            real_name='Batterie Kapazität', 
            unit='kWh', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_charge_losses = VariableMeta(
            var_name='Batt_charge_losses', 
            attr_name='Batt_charge_losses', 
            real_name='Verluste Beladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Batterienutzung', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_charging_losses = VariableMeta(
            var_name='Batt_charging_losses', 
            attr_name='Batt_charging_losses', 
            real_name='E-Batterie Verluste', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_discharge_losses = VariableMeta(
            var_name='Batt_discharge_losses', 
            attr_name='Batt_discharge_losses', 
            real_name='Verluste Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Batterienutzung', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_eff_factor_charge = VariableMeta(
            var_name='Batt_eff_factor_charge', 
            attr_name='Batt_eff_factor_charge', 
            real_name='Wirkungsgrad Ladung', 
            unit='%', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_eff_factor_discharge = VariableMeta(
            var_name='Batt_eff_factor_discharge', 
            attr_name='Batt_eff_factor_discharge', 
            real_name='Wirkungsgrad Entladung', 
            unit='%', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_is_gridcharged = VariableMeta(
            var_name='Batt_is_gridcharged', 
            attr_name='Batt_is_gridcharged', 
            real_name='Batterie wird flexibel  durch Netz geladen?', 
            unit='bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_is_not_used_during_signals = VariableMeta(
            var_name='Batt_is_not_used_during_signals', 
            attr_name='Batt_is_not_used_during_signals', 
            real_name='Batterie wird während Netzsignal nicht entladen', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_is_used = VariableMeta(
            var_name='Batt_is_used', 
            attr_name='Batt_is_used', 
            real_name='Batterie Nutzung', 
            unit=None, 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_is_used_for_EV = VariableMeta(
            var_name='Batt_is_used_for_EV', 
            attr_name='Batt_is_used_for_EV', 
            real_name='Batterie Nutzung für Ecars', 
            unit='bool', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_is_used_for_HVACminimum = VariableMeta(
            var_name='Batt_is_used_for_HVACminimum', 
            attr_name='Batt_is_used_for_HVACminimum', 
            real_name='Batterie Nutzung für HKLS Minimum', 
            unit='bool', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_is_used_for_plugloads = VariableMeta(
            var_name='Batt_is_used_for_plugloads', 
            attr_name='Batt_is_used_for_plugloads', 
            real_name='Batterie Nutzung für Nutzerstrom', 
            unit='bool', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_max_power_specific = VariableMeta(
            var_name='Batt_max_power_specific', 
            attr_name='Batt_max_power_specific', 
            real_name='Batterie Leistung spezifisch', 
            unit='W/m²', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_self_discharge_rate = VariableMeta(
            var_name='Batt_self_discharge_rate', 
            attr_name='Batt_self_discharge_rate', 
            real_name='Batterie Selbstentladung', 
            unit='%/h', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_to_Ec_min = VariableMeta(
            var_name='Batt_to_Ec_min', 
            attr_name='Batt_to_Ec_min', 
            real_name='E-Batterie', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.Batt_to_Edhw_min = VariableMeta(
            var_name='Batt_to_Edhw_min', 
            attr_name='Batt_to_Edhw_min', 
            real_name='E-Batterie', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.Batt_to_Eev_min = VariableMeta(
            var_name='Batt_to_Eev_min', 
            attr_name='Batt_to_Eev_min', 
            real_name='E-Batterie', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='MIV', 
            label=None, 
            var_cat=None
)
        self.Batt_to_Eh_min = VariableMeta(
            var_name='Batt_to_Eh_min', 
            attr_name='Batt_to_Eh_min', 
            real_name='E-Batterie', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.Batt_to_Ev_min = VariableMeta(
            var_name='Batt_to_Ev_min', 
            attr_name='Batt_to_Ev_min', 
            real_name='E-Batterie', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Lüftung', 
            label=None, 
            var_cat=None
)
        self.Batt_to_HVAC = VariableMeta(
            var_name='Batt_to_HVAC', 
            attr_name='Batt_to_HVAC', 
            real_name='E-Batterie → HKLS', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_to_plugloads = VariableMeta(
            var_name='Batt_to_plugloads', 
            attr_name='Batt_to_plugloads', 
            real_name='E-Batterie → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Haushaltsstrom', 
            label=None, 
            var_cat=None
)
        self.Batt_total_charge = VariableMeta(
            var_name='Batt_total_charge', 
            attr_name='Batt_total_charge', 
            real_name='Batterie Jährliche Beladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Batterienutzung', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Batt_total_charge_input = VariableMeta(
            var_name='Batt_total_charge_input', 
            attr_name='Batt_total_charge_input', 
            real_name='e-Speicher Beladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.Batt_total_discharge = VariableMeta(
            var_name='Batt_total_discharge', 
            attr_name='Batt_total_discharge', 
            real_name='Jährliche Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Batterienutzung', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_balconies = VariableMeta(
            var_name='COMP_area_balconies', 
            attr_name='COMP_area_balconies', 
            real_name='FU Balkone', 
            unit='m²', 
            type_name=None, 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_basement_ceiling = VariableMeta(
            var_name='COMP_area_basement_ceiling', 
            attr_name='COMP_area_basement_ceiling', 
            real_name='FU Kellerdecke', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_basement_floor_unheated = VariableMeta(
            var_name='COMP_area_basement_floor_unheated', 
            attr_name='COMP_area_basement_floor_unheated', 
            real_name='FU Erdb. Fußboden Keller', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_ceil_to_air = VariableMeta(
            var_name='COMP_area_ceil_to_air', 
            attr_name='COMP_area_ceil_to_air', 
            real_name='FU Außendecke gg. Außenluft', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_ceiling_topfloor = VariableMeta(
            var_name='COMP_area_ceiling_topfloor', 
            attr_name='COMP_area_ceiling_topfloor', 
            real_name='FU Oberste Geschoßdecke', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_columns = VariableMeta(
            var_name='COMP_area_columns', 
            attr_name='COMP_area_columns', 
            real_name='FU Stützen', 
            unit='Stk', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_fundament = VariableMeta(
            var_name='COMP_area_fundament', 
            attr_name='COMP_area_fundament', 
            real_name='FU Bodenplatte', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_internal_wall_load = VariableMeta(
            var_name='COMP_area_internal_wall_load', 
            attr_name='COMP_area_internal_wall_load', 
            real_name='FU Innenwand tragend', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_internal_wall_nonload = VariableMeta(
            var_name='COMP_area_internal_wall_nonload', 
            attr_name='COMP_area_internal_wall_nonload', 
            real_name='FU Innenwand nicht tragend', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_internal_wall_unheated = VariableMeta(
            var_name='COMP_area_internal_wall_unheated', 
            attr_name='COMP_area_internal_wall_unheated', 
            real_name='FU Innenwand unbeheizt', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_terrace = VariableMeta(
            var_name='COMP_area_terrace', 
            attr_name='COMP_area_terrace', 
            real_name='FU Terasse', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_unheated_horizontal = VariableMeta(
            var_name='COMP_area_unheated_horizontal', 
            attr_name='COMP_area_unheated_horizontal', 
            real_name='FU Zwischendecke unbeheizt / Keller / TG', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_wall_earth_contacted = VariableMeta(
            var_name='COMP_area_wall_earth_contacted', 
            attr_name='COMP_area_wall_earth_contacted', 
            real_name='FU Erdb. Wand beheizt', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_wall_ec_unheated = VariableMeta(
            var_name='COMP_area_wall_ec_unheated', 
            attr_name='COMP_area_wall_ec_unheated', 
            real_name='FU Erdb. Wand Keller', 
            unit='m²', 
            type_name='userinput', 
            comment='functional unit', 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_windowframe = VariableMeta(
            var_name='COMP_area_windowframe', 
            attr_name='COMP_area_windowframe', 
            real_name='FU Fensterrahmen', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_area_windowglazing = VariableMeta(
            var_name='COMP_area_windowglazing', 
            attr_name='COMP_area_windowglazing', 
            real_name='FU Fensterglas', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_balconies = VariableMeta(
            var_name='COMP_name_balconies', 
            attr_name='COMP_name_balconies', 
            real_name='Bauweise Balkone', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_basement_ceiling = VariableMeta(
            var_name='COMP_name_basement_ceiling', 
            attr_name='COMP_name_basement_ceiling', 
            real_name='Bauweise Kellerdecke', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_basement_floor_unheated = VariableMeta(
            var_name='COMP_name_basement_floor_unheated', 
            attr_name='COMP_name_basement_floor_unheated', 
            real_name='Bauweise  Erdb. Fußboden unbeheizt', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_ceil_to_air = VariableMeta(
            var_name='COMP_name_ceil_to_air', 
            attr_name='COMP_name_ceil_to_air', 
            real_name='Bauweise Außendecke gg. Außenluft', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_ceiling_topfloor = VariableMeta(
            var_name='COMP_name_ceiling_topfloor', 
            attr_name='COMP_name_ceiling_topfloor', 
            real_name='Bauweise Oberste Geschoßdecke', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_columns = VariableMeta(
            var_name='COMP_name_columns', 
            attr_name='COMP_name_columns', 
            real_name='Bauweise Stützen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_fundament = VariableMeta(
            var_name='COMP_name_fundament', 
            attr_name='COMP_name_fundament', 
            real_name='Bauweise Bodenplatte', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_internal_wall_load = VariableMeta(
            var_name='COMP_name_internal_wall_load', 
            attr_name='COMP_name_internal_wall_load', 
            real_name='Bauweise Innenwand tragend', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_internal_wall_nonload = VariableMeta(
            var_name='COMP_name_internal_wall_nonload', 
            attr_name='COMP_name_internal_wall_nonload', 
            real_name='Bauweise Innenwand nicht tragend', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_internal_wall_unheated = VariableMeta(
            var_name='COMP_name_internal_wall_unheated', 
            attr_name='COMP_name_internal_wall_unheated', 
            real_name='Bauweise Innenwand unbeheizt', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_other = VariableMeta(
            var_name='COMP_name_other', 
            attr_name='COMP_name_other', 
            real_name='Bauweise Sonstige', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_terrace = VariableMeta(
            var_name='COMP_name_terrace', 
            attr_name='COMP_name_terrace', 
            real_name='Bauweise Terasse', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_unheated_horizontal = VariableMeta(
            var_name='COMP_name_unheated_horizontal', 
            attr_name='COMP_name_unheated_horizontal', 
            real_name='Bauweise Zwischendecke unbeheizt / Keller / TG', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_wall_earth_contacted = VariableMeta(
            var_name='COMP_name_wall_earth_contacted', 
            attr_name='COMP_name_wall_earth_contacted', 
            real_name='Bauweise Erdb. Wand beheizt', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_wall_ec_unheated = VariableMeta(
            var_name='COMP_name_wall_ec_unheated', 
            attr_name='COMP_name_wall_ec_unheated', 
            real_name='Bauweise Erdb. Wand Keller', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_windowframe = VariableMeta(
            var_name='COMP_name_windowframe', 
            attr_name='COMP_name_windowframe', 
            real_name='Bauweise Fensterrahmen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_windowglazing = VariableMeta(
            var_name='COMP_name_windowglazing', 
            attr_name='COMP_name_windowglazing', 
            real_name='Bauweise Fensterglas', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.COMP_name_windows = VariableMeta(
            var_name='COMP_name_windows', 
            attr_name='COMP_name_windows', 
            real_name='Bauweise Fenster', 
            unit=None, 
            type_name='userinput', 
            comment='COMP_name_windows', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_efficiency = VariableMeta(
            var_name='DHW_1_efficiency', 
            attr_name='DHW_1_efficiency', 
            real_name='Warmwasser System 1 Wirkungsgrad', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_el_aux = VariableMeta(
            var_name='DHW_1_el_aux', 
            attr_name='DHW_1_el_aux', 
            real_name='WW-System 1 Hilfsstromanteil', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_incl_distribution_factor = VariableMeta(
            var_name='DHW_1_incl_distribution_factor', 
            attr_name='DHW_1_incl_distribution_factor', 
            real_name='Warmwasser Verlustaufschlag Verteilsystem 1', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_is_electric = VariableMeta(
            var_name='DHW_1_is_electric', 
            attr_name='DHW_1_is_electric', 
            real_name='Warmwasser System 1 ist elektrisch', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_is_used = VariableMeta(
            var_name='DHW_1_is_used', 
            attr_name='DHW_1_is_used', 
            real_name='Warmwasser System 1 in Verwendung', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_office = VariableMeta(
            var_name='DHW_1_share_office', 
            attr_name='DHW_1_share_office', 
            real_name='Warmwasser System 1 Anteil Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_other = VariableMeta(
            var_name='DHW_1_share_other', 
            attr_name='DHW_1_share_other', 
            real_name='Warmwasser System 1 Anteil Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_residential = VariableMeta(
            var_name='DHW_1_share_residential', 
            attr_name='DHW_1_share_residential', 
            real_name='Warmwasser System 1 Anteil Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_retailfood = VariableMeta(
            var_name='DHW_1_share_retailfood', 
            attr_name='DHW_1_share_retailfood', 
            real_name='Warmwasser System 1 Anteil Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_retailother = VariableMeta(
            var_name='DHW_1_share_retailother', 
            attr_name='DHW_1_share_retailother', 
            real_name='Warmwasser System 1 Anteil Handel Sonstige', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_schoolprim = VariableMeta(
            var_name='DHW_1_share_schoolprim', 
            attr_name='DHW_1_share_schoolprim', 
            real_name='Warmwasser System 1 Anteil Schule primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_1_share_schoolsec = VariableMeta(
            var_name='DHW_1_share_schoolsec', 
            attr_name='DHW_1_share_schoolsec', 
            real_name='Warmwasser System 1 Anteil Schule sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_2_efficiency = VariableMeta(
            var_name='DHW_2_efficiency', 
            attr_name='DHW_2_efficiency', 
            real_name='Warmwasser System 2 Wirkungsgrad', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_2_el_aux = VariableMeta(
            var_name='DHW_2_el_aux', 
            attr_name='DHW_2_el_aux', 
            real_name='WW-System 2 Hilfsstromanteil', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_2_incl_distribution_factor = VariableMeta(
            var_name='DHW_2_incl_distribution_factor', 
            attr_name='DHW_2_incl_distribution_factor', 
            real_name='Warmwasser Verlustaufschlag Verteilsystem 2', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_2_is_electric = VariableMeta(
            var_name='DHW_2_is_electric', 
            attr_name='DHW_2_is_electric', 
            real_name='Warmwasser System 2 ist elektrisch', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_2_is_used = VariableMeta(
            var_name='DHW_2_is_used', 
            attr_name='DHW_2_is_used', 
            real_name='Warmwasser System 2 in Verwendung', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_Tmax = VariableMeta(
            var_name='DHW_Tmax', 
            attr_name='DHW_Tmax', 
            real_name='Temperatur Maximum Effektiv', 
            unit='°C', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_Tmax_input = VariableMeta(
            var_name='DHW_Tmax_input', 
            attr_name='DHW_Tmax_input', 
            real_name='Temperatur Maximum Eingabe', 
            unit='°C', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_Tmin = VariableMeta(
            var_name='DHW_Tmin', 
            attr_name='DHW_Tmin', 
            real_name='Temperatur Minimum', 
            unit='°C', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_carriertype_1 = VariableMeta(
            var_name='DHW_carriertype_1', 
            attr_name='DHW_carriertype_1', 
            real_name='Warmwasser System 1 Energieträger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_carriertype_2 = VariableMeta(
            var_name='DHW_carriertype_2', 
            attr_name='DHW_carriertype_2', 
            real_name='Warmwasser System 2 Energieträger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_office = VariableMeta(
            var_name='DHW_concurrency_office', 
            attr_name='DHW_concurrency_office', 
            real_name='WW Gleichzeitigkeitsfaktor Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_other = VariableMeta(
            var_name='DHW_concurrency_other', 
            attr_name='DHW_concurrency_other', 
            real_name='WW Gleichzeitigkeitsfaktor Sonstige', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_residential = VariableMeta(
            var_name='DHW_concurrency_residential', 
            attr_name='DHW_concurrency_residential', 
            real_name='WW Gleichzeitigkeitsfaktor Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_retailfood = VariableMeta(
            var_name='DHW_concurrency_retailfood', 
            attr_name='DHW_concurrency_retailfood', 
            real_name='WW Gleichzeitigkeitsfaktor Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_retailother = VariableMeta(
            var_name='DHW_concurrency_retailother', 
            attr_name='DHW_concurrency_retailother', 
            real_name='WW Gleichzeitigkeitsfaktor handel sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_schoolprim = VariableMeta(
            var_name='DHW_concurrency_schoolprim', 
            attr_name='DHW_concurrency_schoolprim', 
            real_name='WW Gleichzeitigkeitsfaktor bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_concurrency_schoolsec = VariableMeta(
            var_name='DHW_concurrency_schoolsec', 
            attr_name='DHW_concurrency_schoolsec', 
            real_name='WW Gleichzeitigkeitsfaktor Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_conversion_1 = VariableMeta(
            var_name='DHW_conversion_1', 
            attr_name='DHW_conversion_1', 
            real_name='Warmwasser System 1 Wirkungsgradkehrwert', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_conversion_2 = VariableMeta(
            var_name='DHW_conversion_2', 
            attr_name='DHW_conversion_2', 
            real_name='Warmwasser System 2 Wirkungsgradkehrwert', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_office_kWhm2 = VariableMeta(
            var_name='DHW_demand_office_kWhm2', 
            attr_name='DHW_demand_office_kWhm2', 
            real_name='WWWB Büro', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_other_kWhm2 = VariableMeta(
            var_name='DHW_demand_other_kWhm2', 
            attr_name='DHW_demand_other_kWhm2', 
            real_name='WWWB Sonstige Nutzung', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_residential_kWhm2 = VariableMeta(
            var_name='DHW_demand_residential_kWhm2', 
            attr_name='DHW_demand_residential_kWhm2', 
            real_name='WWWB Wohnen', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_retailfood_kWhm2 = VariableMeta(
            var_name='DHW_demand_retailfood_kWhm2', 
            attr_name='DHW_demand_retailfood_kWhm2', 
            real_name='WWWB Handel Lebensmittel', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_retailother_kWhm2 = VariableMeta(
            var_name='DHW_demand_retailother_kWhm2', 
            attr_name='DHW_demand_retailother_kWhm2', 
            real_name='WWWB Handel sonstiger', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_schoolprim_kWhm2 = VariableMeta(
            var_name='DHW_demand_schoolprim_kWhm2', 
            attr_name='DHW_demand_schoolprim_kWhm2', 
            real_name='WWWB Bildung primär', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_demand_schoolsec_kWhm2 = VariableMeta(
            var_name='DHW_demand_schoolsec_kWhm2', 
            attr_name='DHW_demand_schoolsec_kWhm2', 
            real_name='WWWB Bildung sekundär', 
            unit='kWh/m²NGFa', 
            type_name='value', 
            comment='Input fehlt', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_efficiency_distribution_1 = VariableMeta(
            var_name='DHW_efficiency_distribution_1', 
            attr_name='DHW_efficiency_distribution_1', 
            real_name='Warmwasser Verluste: Wirkungsgrad Verteilsystem 1', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_efficiency_distribution_2 = VariableMeta(
            var_name='DHW_efficiency_distribution_2', 
            attr_name='DHW_efficiency_distribution_2', 
            real_name='Warmwasser Verluste: Wirkungsgrad Verteilsystem 2', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_losses_1 = VariableMeta(
            var_name='DHW_losses_1', 
            attr_name='DHW_losses_1', 
            real_name='Warmwasser Verluste: Speicher1', 
            unit=None, 
            type_name='userinput', 
            comment='0-100%', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_losses_2 = VariableMeta(
            var_name='DHW_losses_2', 
            attr_name='DHW_losses_2', 
            real_name='Warmwasser Verluste: Speicher2', 
            unit=None, 
            type_name='userinput', 
            comment='0-100%', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_office = VariableMeta(
            var_name='DHW_occupancy_office', 
            attr_name='DHW_occupancy_office', 
            real_name='Personenbelegung Büro', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_other = VariableMeta(
            var_name='DHW_occupancy_other', 
            attr_name='DHW_occupancy_other', 
            real_name='Personenbelegung Sonstige', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_residential = VariableMeta(
            var_name='DHW_occupancy_residential', 
            attr_name='DHW_occupancy_residential', 
            real_name='Personenbelegung Wohnen', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_retailfood = VariableMeta(
            var_name='DHW_occupancy_retailfood', 
            attr_name='DHW_occupancy_retailfood', 
            real_name='Personenbelegung Handel Lebensmittel', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_retailother = VariableMeta(
            var_name='DHW_occupancy_retailother', 
            attr_name='DHW_occupancy_retailother', 
            real_name='Personenbelegung Handel sonstiger', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_schoolprim = VariableMeta(
            var_name='DHW_occupancy_schoolprim', 
            attr_name='DHW_occupancy_schoolprim', 
            real_name='Personenbelegung Bildung primär', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_occupancy_schoolsec = VariableMeta(
            var_name='DHW_occupancy_schoolsec', 
            attr_name='DHW_occupancy_schoolsec', 
            real_name='Personenbelegung Bildung sekundär', 
            unit='m²NF/Pers', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_storage_1_liter = VariableMeta(
            var_name='DHW_storage_1_liter', 
            attr_name='DHW_storage_1_liter', 
            real_name='Warmwasser-Speichergröße 1', 
            unit='liter', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_storage_2_liter = VariableMeta(
            var_name='DHW_storage_2_liter', 
            attr_name='DHW_storage_2_liter', 
            real_name='Warmwasser-Speichergröße 2', 
            unit='liter', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_storage_env_temp_default = VariableMeta(
            var_name='DHW_storage_env_temp_default', 
            attr_name='DHW_storage_env_temp_default', 
            real_name='Warmwasser Speicher Umgebungstemperatur', 
            unit='°C', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_storage_liter_pPerson = VariableMeta(
            var_name='DHW_storage_liter_pPerson', 
            attr_name='DHW_storage_liter_pPerson', 
            real_name='Warmwasser Speicher pro Person', 
            unit='l/Pers/Tag', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_thermal_power_1_kW = VariableMeta(
            var_name='DHW_thermal_power_1_kW', 
            attr_name='DHW_thermal_power_1_kW', 
            real_name='Warmwasser Ladeleistung 1', 
            unit='kW', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_thermal_power_Wpl = VariableMeta(
            var_name='DHW_thermal_power_Wpl', 
            attr_name='DHW_thermal_power_Wpl', 
            real_name='Warmwasser Ladeleistung Thermisch pro Speicher', 
            unit='W/l', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.DHW_thermal_power_pPerson = VariableMeta(
            var_name='DHW_thermal_power_pPerson', 
            attr_name='DHW_thermal_power_pPerson', 
            real_name='Warmwasser Ladeleistung Thermisch', 
            unit='W/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Daylightcoefficient_office = VariableMeta(
            var_name='Daylightcoefficient_office', 
            attr_name='Daylightcoefficient_office', 
            real_name='Tageslichtkoeffizient Büro', 
            unit='-', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Daylightcoefficient_schoolprim = VariableMeta(
            var_name='Daylightcoefficient_schoolprim', 
            attr_name='Daylightcoefficient_schoolprim', 
            real_name='Tageslichtkoeffizient Ausbildung Primär', 
            unit='-', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Daylightcoefficient_schoolsec = VariableMeta(
            var_name='Daylightcoefficient_schoolsec', 
            attr_name='Daylightcoefficient_schoolsec', 
            real_name='Tageslichtkoeffizient Ausbildung Sekundär', 
            unit='-', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EUI_auxiliary = VariableMeta(
            var_name='EUI_auxiliary', 
            attr_name='EUI_auxiliary', 
            real_name='Beleuchtung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUI_biomass = VariableMeta(
            var_name='EUI_biomass', 
            attr_name='EUI_biomass', 
            real_name='Biomasse', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUI_district_heating = VariableMeta(
            var_name='EUI_district_heating', 
            attr_name='EUI_district_heating', 
            real_name='Fernwärme', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUI_el_total = VariableMeta(
            var_name='EUI_el_total', 
            attr_name='EUI_el_total', 
            real_name='Quartier', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label='Ohne Speicher', 
            var_cat=None
)
        self.EUI_lighting = VariableMeta(
            var_name='EUI_lighting', 
            attr_name='EUI_lighting', 
            real_name='Allgemeinstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUI_mob_fossil = VariableMeta(
            var_name='EUI_mob_fossil', 
            attr_name='EUI_mob_fossil', 
            real_name='MIV Fossil', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EUI_mob_fossile = VariableMeta(
            var_name='EUI_mob_fossile', 
            attr_name='EUI_mob_fossile', 
            real_name='EE-Bedarf Zielverkehr Fossil', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EUI_natural_gas = VariableMeta(
            var_name='EUI_natural_gas', 
            attr_name='EUI_natural_gas', 
            real_name='Gas', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUI_other = VariableMeta(
            var_name='EUI_other', 
            attr_name='EUI_other', 
            real_name='Sonstige', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUI_plugAuxLight = VariableMeta(
            var_name='EUI_plugAuxLight', 
            attr_name='EUI_plugAuxLight', 
            real_name='Nutzerstrom, Beleuchtung und Allgemeinstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUI_plugloads = VariableMeta(
            var_name='EUI_plugloads', 
            attr_name='EUI_plugloads', 
            real_name='Nutzerstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUI_self_sufficiency = VariableMeta(
            var_name='EUI_self_sufficiency', 
            attr_name='EUI_self_sufficiency', 
            real_name='Energie-Autonomie', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PV', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EUIc_2th = VariableMeta(
            var_name='EUIc_2th', 
            attr_name='EUIc_2th', 
            real_name='Kühlen 2', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUIc_el = VariableMeta(
            var_name='EUIc_el', 
            attr_name='EUIc_el', 
            real_name='Kühlen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIc_el_aux = VariableMeta(
            var_name='EUIc_el_aux', 
            attr_name='EUIc_el_aux', 
            real_name='Heizen Hilfsstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIc_other = VariableMeta(
            var_name='EUIc_other', 
            attr_name='EUIc_other', 
            real_name='Sonstige', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_1th = VariableMeta(
            var_name='EUIdhw_1th', 
            attr_name='EUIdhw_1th', 
            real_name='WWWB1', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_2th = VariableMeta(
            var_name='EUIdhw_2th', 
            attr_name='EUIdhw_2th', 
            real_name='WWWB2', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_biomass = VariableMeta(
            var_name='EUIdhw_biomass', 
            attr_name='EUIdhw_biomass', 
            real_name='Biomasse', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_district_heating = VariableMeta(
            var_name='EUIdhw_district_heating', 
            attr_name='EUIdhw_district_heating', 
            real_name='Fernwärme', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_el = VariableMeta(
            var_name='EUIdhw_el', 
            attr_name='EUIdhw_el', 
            real_name='Warmwasser', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_natural_gas = VariableMeta(
            var_name='EUIdhw_natural_gas', 
            attr_name='EUIdhw_natural_gas', 
            real_name='Gas', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.EUIdhw_other = VariableMeta(
            var_name='EUIdhw_other', 
            attr_name='EUIdhw_other', 
            real_name='Sonstige', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.EUIdhwdirect_el = VariableMeta(
            var_name='EUIdhwdirect_el', 
            attr_name='EUIdhwdirect_el', 
            real_name='WW\nE-Stab', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIev_el = VariableMeta(
            var_name='EUIev_el', 
            attr_name='EUIev_el', 
            real_name='EV Quartiersladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIev_el_total = VariableMeta(
            var_name='EUIev_el_total', 
            attr_name='EUIev_el_total', 
            real_name='EV Jährliche Beladung', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EUIh_2th = VariableMeta(
            var_name='EUIh_2th', 
            attr_name='EUIh_2th', 
            real_name='Heizen 2', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUIh_4th = VariableMeta(
            var_name='EUIh_4th', 
            attr_name='EUIh_4th', 
            real_name='Heizen 4', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.EUIh_biomass = VariableMeta(
            var_name='EUIh_biomass', 
            attr_name='EUIh_biomass', 
            real_name='Biomasse', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.EUIh_district_heating = VariableMeta(
            var_name='EUIh_district_heating', 
            attr_name='EUIh_district_heating', 
            real_name='Fernwärme', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.EUIh_el = VariableMeta(
            var_name='EUIh_el', 
            attr_name='EUIh_el', 
            real_name='Heizen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIh_el_aux = VariableMeta(
            var_name='EUIh_el_aux', 
            attr_name='EUIh_el_aux', 
            real_name='Heizen Hilfsstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EUIh_natural_gas = VariableMeta(
            var_name='EUIh_natural_gas', 
            attr_name='EUIh_natural_gas', 
            real_name='Gas', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.EUIh_other = VariableMeta(
            var_name='EUIh_other', 
            attr_name='EUIh_other', 
            real_name='Sonstige', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.EUIv_el = VariableMeta(
            var_name='EUIv_el', 
            attr_name='EUIv_el', 
            real_name='Lüftung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Endenergiebedarf', 
            label=None, 
            var_cat=None
)
        self.EV_FEC = VariableMeta(
            var_name='EV_FEC', 
            attr_name='EV_FEC', 
            real_name='EV Volladezyklen', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_battsize_kWh = VariableMeta(
            var_name='EV_battsize_kWh', 
            attr_name='EV_battsize_kWh', 
            real_name='Ecar Speicher pro Fahrzeug', 
            unit='kWh/EV', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_charging_efficiency = VariableMeta(
            var_name='EV_charging_efficiency', 
            attr_name='EV_charging_efficiency', 
            real_name='Ecar Batterie-Effizienz Beladung', 
            unit='%', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_charging_losses_surcharge_factor = VariableMeta(
            var_name='EV_charging_losses_surcharge_factor', 
            attr_name='EV_charging_losses_surcharge_factor', 
            real_name='Ecar Batterie-Effizienz Beladung Kehrwert', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_charging_station_power = VariableMeta(
            var_name='EV_charging_station_power', 
            attr_name='EV_charging_station_power', 
            real_name='Leistung Ladestation', 
            unit='kW', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_charging_stations = VariableMeta(
            var_name='EV_charging_stations', 
            attr_name='EV_charging_stations', 
            real_name='Anzahl Ladestationen', 
            unit='-', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_count_residential = VariableMeta(
            var_name='EV_count_residential', 
            attr_name='EV_count_residential', 
            real_name='Ecar Anzahl Wohnen', 
            unit='🚗', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_count_retail = VariableMeta(
            var_name='EV_count_retail', 
            attr_name='EV_count_retail', 
            real_name='Ecar Anzahl Einkaufen', 
            unit='🚗', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_count_work = VariableMeta(
            var_name='EV_count_work', 
            attr_name='EV_count_work', 
            real_name='Ecar Anzahl Arbeit', 
            unit='🚗', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_demand_kWhpkm = VariableMeta(
            var_name='EV_demand_kWhpkm', 
            attr_name='EV_demand_kWhpkm', 
            real_name='Ecar Energieverbrauch', 
            unit='kWh/km', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_experimental_calculation = VariableMeta(
            var_name='EV_experimental_calculation', 
            attr_name='EV_experimental_calculation', 
            real_name='New Calculation Method', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_max_charging_power_ratio = VariableMeta(
            var_name='EV_max_charging_power_ratio', 
            attr_name='EV_max_charging_power_ratio', 
            real_name='Ecar Batterie Maximale Beladungsleistung', 
            unit='%', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_mileage_res = VariableMeta(
            var_name='EV_mileage_res', 
            attr_name='EV_mileage_res', 
            real_name='Ecar Pkm Real Wohnen (Insgesamt)', 
            unit='Pkm/a', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_mileage_retail = VariableMeta(
            var_name='EV_mileage_retail', 
            attr_name='EV_mileage_retail', 
            real_name='Ecar Pkm Real Einkaufen (Insgesamt)', 
            unit='Pkm/a', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_mileage_work = VariableMeta(
            var_name='EV_mileage_work', 
            attr_name='EV_mileage_work', 
            real_name='Ecar Pkm Real Arbeiten (Insgesamt)', 
            unit='Pkm/a', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_self_discharge_per_week = VariableMeta(
            var_name='EV_self_discharge_per_week', 
            attr_name='EV_self_discharge_per_week', 
            real_name='Ecar Selbstentladung wöchentlich', 
            unit='%/Woche', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_selfdischarge_per_h = VariableMeta(
            var_name='EV_selfdischarge_per_h', 
            attr_name='EV_selfdischarge_per_h', 
            real_name='Ecar Selbstentladung stündlich', 
            unit='%/h', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_share = VariableMeta(
            var_name='EV_share', 
            attr_name='EV_share', 
            real_name='Anteil Ecars', 
            unit='%', 
            type_name='userinput', 
            comment='Am Mobilitätsbedarf', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_share_constant_charging = VariableMeta(
            var_name='EV_share_constant_charging', 
            attr_name='EV_share_constant_charging', 
            real_name='Anteil Ecars, die konstant vor Ort laden', 
            unit='%', 
            type_name='value', 
            comment='Rest konstantes Laden', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_soc_min_discharge = VariableMeta(
            var_name='EV_soc_min_discharge', 
            attr_name='EV_soc_min_discharge', 
            real_name='Ecar Mindest-Speicherstand Entladung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_soc_min_ext = VariableMeta(
            var_name='EV_soc_min_ext', 
            attr_name='EV_soc_min_ext', 
            real_name='Ecar Mindest-Speicherstand Extern', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_soc_min_retail = VariableMeta(
            var_name='EV_soc_min_retail', 
            attr_name='EV_soc_min_retail', 
            real_name='Ecar Mindestspeicherstand Handel', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_soc_min_work = VariableMeta(
            var_name='EV_soc_min_work', 
            attr_name='EV_soc_min_work', 
            real_name='Ecar Mindestspeicherstand Arbeit', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_soc_minimum = VariableMeta(
            var_name='EV_soc_minimum', 
            attr_name='EV_soc_minimum', 
            real_name='Ecar Mindest-Speicherstand', 
            unit='%', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.EV_storage_total_kWh = VariableMeta(
            var_name='EV_storage_total_kWh', 
            attr_name='EV_storage_total_kWh', 
            real_name='Ecar Speicher im Quartier', 
            unit='kWh', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_1_aux_el = VariableMeta(
            var_name='Edhw_1_aux_el', 
            attr_name='Edhw_1_aux_el', 
            real_name='WW 1 Hilfsstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_1_el = VariableMeta(
            var_name='Edhw_1_el', 
            attr_name='Edhw_1_el', 
            real_name='WW 1 Endenergie elektrisch (inkl. Hilfsstrom)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_1_th = VariableMeta(
            var_name='Edhw_1_th', 
            attr_name='Edhw_1_th', 
            real_name='WW 1 Endenergie thermisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_2_aux_el = VariableMeta(
            var_name='Edhw_2_aux_el', 
            attr_name='Edhw_2_aux_el', 
            real_name='WW 2 Hilfsstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_2_el = VariableMeta(
            var_name='Edhw_2_el', 
            attr_name='Edhw_2_el', 
            real_name='WW 2 Endenergie elektrisch (inkl.Hilfsstrom)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_2_th = VariableMeta(
            var_name='Edhw_2_th', 
            attr_name='Edhw_2_th', 
            real_name='WW 2 Endenergie thermisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_aux_el = VariableMeta(
            var_name='Edhw_aux_el', 
            attr_name='Edhw_aux_el', 
            real_name='WW Hilfsstrom', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_el = VariableMeta(
            var_name='Edhw_el', 
            attr_name='Edhw_el', 
            real_name='WW Endenergiebedarf Elektrisch (inkl. Hilfsstrom)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Edhw_th = VariableMeta(
            var_name='Edhw_th', 
            attr_name='Edhw_th', 
            real_name='WW Endenergiebedarf Thermisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Warmwasser', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Eev_discharge_loss = VariableMeta(
            var_name='Eev_discharge_loss', 
            attr_name='Eev_discharge_loss', 
            real_name='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Verluste', 
            label=None, 
            var_cat=None
)
        self.Eev_ext_charge = VariableMeta(
            var_name='Eev_ext_charge', 
            attr_name='Eev_ext_charge', 
            real_name='E-Car Ladung Außerhalb des Quartiers', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.Eev_to_Ec_min = VariableMeta(
            var_name='Eev_to_Ec_min', 
            attr_name='Eev_to_Ec_min', 
            real_name='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.Eev_to_Edhw_min = VariableMeta(
            var_name='Eev_to_Edhw_min', 
            attr_name='Eev_to_Edhw_min', 
            real_name='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.Eev_to_Eh_min = VariableMeta(
            var_name='Eev_to_Eh_min', 
            attr_name='Eev_to_Eh_min', 
            real_name='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.Eev_to_Ev_min = VariableMeta(
            var_name='Eev_to_Ev_min', 
            attr_name='Eev_to_Ev_min', 
            real_name='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Lüftung', 
            label=None, 
            var_cat=None
)
        self.Eev_to_HVAC = VariableMeta(
            var_name='Eev_to_HVAC', 
            attr_name='Eev_to_HVAC', 
            real_name='E-Car Entladung → HKLS', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area='HKLS', 
            label=None, 
            var_cat=None
)
        self.Eev_to_district = VariableMeta(
            var_name='Eev_to_district', 
            attr_name='Eev_to_district', 
            real_name='E-Car Entladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.Eev_to_plugloads = VariableMeta(
            var_name='Eev_to_plugloads', 
            attr_name='Eev_to_plugloads', 
            real_name='E-Car Entladung → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Haushaltsstrom', 
            label=None, 
            var_cat=None
)
        self.Ev_scale_office = VariableMeta(
            var_name='Ev_scale_office', 
            attr_name='Ev_scale_office', 
            real_name='Lüfterstrom mech. Büro', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ev_scale_other = VariableMeta(
            var_name='Ev_scale_other', 
            attr_name='Ev_scale_other', 
            real_name='Lüfterstrom mech.  Sonstige Nutzung', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ev_scale_residential = VariableMeta(
            var_name='Ev_scale_residential', 
            attr_name='Ev_scale_residential', 
            real_name='Lüfterstrom mech. Wohnen', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ev_scale_retail_food = VariableMeta(
            var_name='Ev_scale_retail_food', 
            attr_name='Ev_scale_retail_food', 
            real_name='Lüfterstrom mech.  Handel Lebensmittel', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ev_scale_retail_other = VariableMeta(
            var_name='Ev_scale_retail_other', 
            attr_name='Ev_scale_retail_other', 
            real_name='Lüfterstrom mech.  Handel sonstiger', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ev_scale_school_prim = VariableMeta(
            var_name='Ev_scale_school_prim', 
            attr_name='Ev_scale_school_prim', 
            real_name='Lüfterstrom mech.  Bildung primär', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ev_scale_school_sec = VariableMeta(
            var_name='Ev_scale_school_sec', 
            attr_name='Ev_scale_school_sec', 
            real_name='Lüfterstrom mech.  Bildung sekundär', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_PV_is_used = VariableMeta(
            var_name='FLEX_PV_is_used', 
            attr_name='FLEX_PV_is_used', 
            real_name='Flex PV Nutzung', 
            unit=None, 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_choice_cool_system = VariableMeta(
            var_name='FLEX_choice_cool_system', 
            attr_name='FLEX_choice_cool_system', 
            real_name='Flexibles Kühlsystem', 
            unit='Text', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_choice_heat_system = VariableMeta(
            var_name='FLEX_choice_heat_system', 
            attr_name='FLEX_choice_heat_system', 
            real_name='Flexibles Heizsystem', 
            unit='Text', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_cool1_use = VariableMeta(
            var_name='FLEX_cool1_use', 
            attr_name='FLEX_cool1_use', 
            real_name='Flexibles Kühlen mit Kühlsystem 1', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_cool3_use = VariableMeta(
            var_name='FLEX_cool3_use', 
            attr_name='FLEX_cool3_use', 
            real_name='Flexibles Kühlen mit Kühlsystem 3', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_grid_maxpower_Wm2 = VariableMeta(
            var_name='FLEX_grid_maxpower_Wm2', 
            attr_name='FLEX_grid_maxpower_Wm2', 
            real_name='Flex Maximale Leistung', 
            unit='W/m²', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_heat1_use = VariableMeta(
            var_name='FLEX_heat1_use', 
            attr_name='FLEX_heat1_use', 
            real_name='Flexibles Heizen mit Heizsystem 1', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_heat3_use = VariableMeta(
            var_name='FLEX_heat3_use', 
            attr_name='FLEX_heat3_use', 
            real_name='Flexibles Heizen mit Heizsystem 3', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_is_used = VariableMeta(
            var_name='FLEX_is_used', 
            attr_name='FLEX_is_used', 
            real_name='Flex Signal Nutzung', 
            unit=None, 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_is_used_for_HVAC_min = VariableMeta(
            var_name='FLEX_is_used_for_HVAC_min', 
            attr_name='FLEX_is_used_for_HVAC_min', 
            real_name='Flex Netzbezug deckt HVAC Minimum', 
            unit='bool', 
            type_name='value', 
            comment='muss jetzt nicht mehr automatisch Wahr sein', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_is_used_for_ev_min = VariableMeta(
            var_name='FLEX_is_used_for_ev_min', 
            attr_name='FLEX_is_used_for_ev_min', 
            real_name='Flex Netzbezug deckt EV Minimum', 
            unit='bool', 
            type_name='value', 
            comment='muss jetzt nicht mehr automatisch Wahr sein', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_is_used_for_plugloads = VariableMeta(
            var_name='FLEX_is_used_for_plugloads', 
            attr_name='FLEX_is_used_for_plugloads', 
            real_name='Flex Netzbezug deckt Nutzerstrom', 
            unit='bool', 
            type_name='value', 
            comment='muss jetzt nicht mehr automatisch Wahr sein', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_signal_ID = VariableMeta(
            var_name='FLEX_signal_ID', 
            attr_name='FLEX_signal_ID', 
            real_name='Flex Signal ID', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FLEX_signal_name = VariableMeta(
            var_name='FLEX_signal_name', 
            attr_name='FLEX_signal_name', 
            real_name='Flex Signal Name', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.FSI = VariableMeta(
            var_name='FSI', 
            attr_name='FSI', 
            real_name='Geschoßflächenzahl', 
            unit='GFZ', 
            type_name='calculation', 
            comment=None, 
            source='BOTH', 
            ka=0, 
            category='Quartier', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_office = VariableMeta(
            var_name='GFA_office', 
            attr_name='GFA_office', 
            real_name='BGF Büro', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_other = VariableMeta(
            var_name='GFA_other', 
            attr_name='GFA_other', 
            real_name='BGF Sonstige', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_residential = VariableMeta(
            var_name='GFA_residential', 
            attr_name='GFA_residential', 
            real_name='BGF Wohnen', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_retailfood = VariableMeta(
            var_name='GFA_retailfood', 
            attr_name='GFA_retailfood', 
            real_name='BGF Lebensmittelhandel', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_retailother = VariableMeta(
            var_name='GFA_retailother', 
            attr_name='GFA_retailother', 
            real_name='BGF Handel sonstiger', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_schoolprim = VariableMeta(
            var_name='GFA_schoolprim', 
            attr_name='GFA_schoolprim', 
            real_name='BGF Bildung primär', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_schoolsec = VariableMeta(
            var_name='GFA_schoolsec', 
            attr_name='GFA_schoolsec', 
            real_name='BGF Bildung sekundär', 
            unit='m²BGF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFA_total = VariableMeta(
            var_name='GFA_total', 
            attr_name='GFA_total', 
            real_name='BGF Quartier', 
            unit='m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GFV = VariableMeta(
            var_name='GFV', 
            attr_name='GFV', 
            real_name='Raumvolumen Quartier brutto', 
            unit='m³brutto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GHG_LCA_timeframe_years = VariableMeta(
            var_name='GHG_LCA_timeframe_years', 
            attr_name='GHG_LCA_timeframe_years', 
            real_name='Betrachtungszeitraum Ökobilanz', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GPW_ceilings_name = VariableMeta(
            var_name='GPW_ceilings_name', 
            attr_name='GPW_ceilings_name', 
            real_name='Bauweise Geschossdecke', 
            unit=None, 
            type_name='userinput', 
            comment='COMP_name_ceiling', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_battery_name = VariableMeta(
            var_name='GWP_battery_name', 
            attr_name='GWP_battery_name', 
            real_name='Typ E-Batterie', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_boreholes_name = VariableMeta(
            var_name='GWP_boreholes_name', 
            attr_name='GWP_boreholes_name', 
            real_name='Typ Erdwärmesonden', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_direct_biogenic = VariableMeta(
            var_name='GWP_direct_biogenic', 
            attr_name='GWP_direct_biogenic', 
            real_name='Direkteingabe GWP Biogen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_direct_biogenic_share = VariableMeta(
            var_name='GWP_direct_biogenic_share', 
            attr_name='GWP_direct_biogenic_share', 
            real_name='Direkteingabe Biogener Anteil', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_direct_fossile = VariableMeta(
            var_name='GWP_direct_fossile', 
            attr_name='GWP_direct_fossile', 
            real_name='Direkteingabe GWP Fossil', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_direct_life = VariableMeta(
            var_name='GWP_direct_life', 
            attr_name='GWP_direct_life', 
            real_name='Direkteingabe Lebensdauer', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_ceilings_biogenic = VariableMeta(
            var_name='GWP_ee_ceilings_biogenic', 
            attr_name='GWP_ee_ceilings_biogenic', 
            real_name='Bauteil Zwischengeschoßdecken biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_ceilings_fossile = VariableMeta(
            var_name='GWP_ee_ceilings_fossile', 
            attr_name='GWP_ee_ceilings_fossile', 
            real_name='Bauteil Zwischengeschoßdecken fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_con_build = VariableMeta(
            var_name='GWP_ee_con_build', 
            attr_name='GWP_ee_con_build', 
            real_name='Baulich Errichtung', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_con_tga = VariableMeta(
            var_name='GWP_ee_con_tga', 
            attr_name='GWP_ee_con_tga', 
            real_name='Errichtung TGA', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_direct_biogenic = VariableMeta(
            var_name='GWP_ee_direct_biogenic', 
            attr_name='GWP_ee_direct_biogenic', 
            real_name='Baulich Direkteingabe biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_direct_fossile = VariableMeta(
            var_name='GWP_ee_direct_fossile', 
            attr_name='GWP_ee_direct_fossile', 
            real_name='Baulich Direkteingabe fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_general = VariableMeta(
            var_name='GWP_ee_general', 
            attr_name='GWP_ee_general', 
            real_name='Baulich Allgemein', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_general_bigonenic = VariableMeta(
            var_name='GWP_ee_general_bigonenic', 
            attr_name='GWP_ee_general_bigonenic', 
            real_name='Baulich Allgemein biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_general_fossile = VariableMeta(
            var_name='GWP_ee_general_fossile', 
            attr_name='GWP_ee_general_fossile', 
            real_name='Baulich Allgemein fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_ground_biogenic = VariableMeta(
            var_name='GWP_ee_ground_biogenic', 
            attr_name='GWP_ee_ground_biogenic', 
            real_name='Bauteil Decke gegen Erdreich / Keller biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_ground_fossile = VariableMeta(
            var_name='GWP_ee_ground_fossile', 
            attr_name='GWP_ee_ground_fossile', 
            real_name='Bauteil Decke gegen Erdreich / Keller fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_battery = VariableMeta(
            var_name='GWP_ee_lc_battery', 
            attr_name='GWP_ee_lc_battery', 
            real_name='TGA E-Batterie', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_biogenic = VariableMeta(
            var_name='GWP_ee_lc_biogenic', 
            attr_name='GWP_ee_lc_biogenic', 
            real_name='Baulich Biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_boreholes = VariableMeta(
            var_name='GWP_ee_lc_boreholes', 
            attr_name='GWP_ee_lc_boreholes', 
            real_name='TGA Erdsonden', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ceil = VariableMeta(
            var_name='GWP_ee_lc_ceil', 
            attr_name='GWP_ee_lc_ceil', 
            real_name='Bauteil Zwischengeschoßdecken', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ceilings_biogenic = VariableMeta(
            var_name='GWP_ee_lc_ceilings_biogenic', 
            attr_name='GWP_ee_lc_ceilings_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ceilings_fossile = VariableMeta(
            var_name='GWP_ee_lc_ceilings_fossile', 
            attr_name='GWP_ee_lc_ceilings_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_construction = VariableMeta(
            var_name='GWP_ee_lc_construction', 
            attr_name='GWP_ee_lc_construction', 
            real_name='Baulich', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_direct = VariableMeta(
            var_name='GWP_ee_lc_direct', 
            attr_name='GWP_ee_lc_direct', 
            real_name='Baulich Direkteingabe', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_direct_biogenic = VariableMeta(
            var_name='GWP_ee_lc_direct_biogenic', 
            attr_name='GWP_ee_lc_direct_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_direct_fossile = VariableMeta(
            var_name='GWP_ee_lc_direct_fossile', 
            attr_name='GWP_ee_lc_direct_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_fossil = VariableMeta(
            var_name='GWP_ee_lc_fossil', 
            attr_name='GWP_ee_lc_fossil', 
            real_name='Baulich Fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_general_biogenic = VariableMeta(
            var_name='GWP_ee_lc_general_biogenic', 
            attr_name='GWP_ee_lc_general_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_general_fossile = VariableMeta(
            var_name='GWP_ee_lc_general_fossile', 
            attr_name='GWP_ee_lc_general_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ground = VariableMeta(
            var_name='GWP_ee_lc_ground', 
            attr_name='GWP_ee_lc_ground', 
            real_name='Bauteil Decke gegen Erdreich / Keller', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ground_biogenic = VariableMeta(
            var_name='GWP_ee_lc_ground_biogenic', 
            attr_name='GWP_ee_lc_ground_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ground_fossile = VariableMeta(
            var_name='GWP_ee_lc_ground_fossile', 
            attr_name='GWP_ee_lc_ground_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_mob = VariableMeta(
            var_name='GWP_ee_lc_mob', 
            attr_name='GWP_ee_lc_mob', 
            real_name='Errichtung Mobilität', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_other = VariableMeta(
            var_name='GWP_ee_lc_other', 
            attr_name='GWP_ee_lc_other', 
            real_name='Baulich Sammel-Maßnahmen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_other_biogenic = VariableMeta(
            var_name='GWP_ee_lc_other_biogenic', 
            attr_name='GWP_ee_lc_other_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_other_fossile = VariableMeta(
            var_name='GWP_ee_lc_other_fossile', 
            attr_name='GWP_ee_lc_other_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_pv = VariableMeta(
            var_name='GWP_ee_lc_pv', 
            attr_name='GWP_ee_lc_pv', 
            real_name='TGA PV', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_roof = VariableMeta(
            var_name='GWP_ee_lc_roof', 
            attr_name='GWP_ee_lc_roof', 
            real_name='Bauteil Dach', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_roof_biogenic = VariableMeta(
            var_name='GWP_ee_lc_roof_biogenic', 
            attr_name='GWP_ee_lc_roof_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_roof_fossile = VariableMeta(
            var_name='GWP_ee_lc_roof_fossile', 
            attr_name='GWP_ee_lc_roof_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_solarthermal = VariableMeta(
            var_name='GWP_ee_lc_solarthermal', 
            attr_name='GWP_ee_lc_solarthermal', 
            real_name='TGA Solarthermie', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_storage = VariableMeta(
            var_name='GWP_ee_lc_storage', 
            attr_name='GWP_ee_lc_storage', 
            real_name='TGA Speicher', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_tga = VariableMeta(
            var_name='GWP_ee_lc_tga', 
            attr_name='GWP_ee_lc_tga', 
            real_name='TGA', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_tga_general = VariableMeta(
            var_name='GWP_ee_lc_tga_general', 
            attr_name='GWP_ee_lc_tga_general', 
            real_name='TGA Allgemein', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_tga_other = VariableMeta(
            var_name='GWP_ee_lc_tga_other', 
            attr_name='GWP_ee_lc_tga_other', 
            real_name='TGA Sammel-Maßnahmen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_ventilation = VariableMeta(
            var_name='GWP_ee_lc_ventilation', 
            attr_name='GWP_ee_lc_ventilation', 
            real_name='TGA Lüftung', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_walls = VariableMeta(
            var_name='GWP_ee_lc_walls', 
            attr_name='GWP_ee_lc_walls', 
            real_name='Bauteil Außenwand', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_walls_biogenic = VariableMeta(
            var_name='GWP_ee_lc_walls_biogenic', 
            attr_name='GWP_ee_lc_walls_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_walls_fossil = VariableMeta(
            var_name='GWP_ee_lc_walls_fossil', 
            attr_name='GWP_ee_lc_walls_fossil', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_windows = VariableMeta(
            var_name='GWP_ee_lc_windows', 
            attr_name='GWP_ee_lc_windows', 
            real_name='Bauteil Fenster', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_windows_biogenic = VariableMeta(
            var_name='GWP_ee_lc_windows_biogenic', 
            attr_name='GWP_ee_lc_windows_biogenic', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_lc_windows_fossile = VariableMeta(
            var_name='GWP_ee_lc_windows_fossile', 
            attr_name='GWP_ee_lc_windows_fossile', 
            real_name=None, 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_mob_ev = VariableMeta(
            var_name='GWP_ee_mob_ev', 
            attr_name='GWP_ee_mob_ev', 
            real_name='Errichtung Mobilität Elektrisch', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_mob_fossile = VariableMeta(
            var_name='GWP_ee_mob_fossile', 
            attr_name='GWP_ee_mob_fossile', 
            real_name='Errichtung Mobilität fossil', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_other_biogenic = VariableMeta(
            var_name='GWP_ee_other_biogenic', 
            attr_name='GWP_ee_other_biogenic', 
            real_name='Baulich Andere biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_other_fossile = VariableMeta(
            var_name='GWP_ee_other_fossile', 
            attr_name='GWP_ee_other_fossile', 
            real_name='Baulich Andere fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_rep_build = VariableMeta(
            var_name='GWP_ee_rep_build', 
            attr_name='GWP_ee_rep_build', 
            real_name='Baulich Instandsetzung', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_rep_tga = VariableMeta(
            var_name='GWP_ee_rep_tga', 
            attr_name='GWP_ee_rep_tga', 
            real_name='Instandsetzung TGA', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_roof_biogenic = VariableMeta(
            var_name='GWP_ee_roof_biogenic', 
            attr_name='GWP_ee_roof_biogenic', 
            real_name='Bauteil Dach biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_roof_fossile = VariableMeta(
            var_name='GWP_ee_roof_fossile', 
            attr_name='GWP_ee_roof_fossile', 
            real_name='Bauteil Dach fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_battery_biogenic = VariableMeta(
            var_name='GWP_ee_tga_battery_biogenic', 
            attr_name='GWP_ee_tga_battery_biogenic', 
            real_name='TGA E-Batterie biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_battery_fossile = VariableMeta(
            var_name='GWP_ee_tga_battery_fossile', 
            attr_name='GWP_ee_tga_battery_fossile', 
            real_name='TGA E-Batterie fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_boreholes_biogenic = VariableMeta(
            var_name='GWP_ee_tga_boreholes_biogenic', 
            attr_name='GWP_ee_tga_boreholes_biogenic', 
            real_name='TGA Erdsonden biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_boreholes_fossile = VariableMeta(
            var_name='GWP_ee_tga_boreholes_fossile', 
            attr_name='GWP_ee_tga_boreholes_fossile', 
            real_name='TGA Erdsonden fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_general_biogenic = VariableMeta(
            var_name='GWP_ee_tga_general_biogenic', 
            attr_name='GWP_ee_tga_general_biogenic', 
            real_name='TGA Allgemein biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_general_fossile = VariableMeta(
            var_name='GWP_ee_tga_general_fossile', 
            attr_name='GWP_ee_tga_general_fossile', 
            real_name='TGA Allgemein fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_other_biogenic = VariableMeta(
            var_name='GWP_ee_tga_other_biogenic', 
            attr_name='GWP_ee_tga_other_biogenic', 
            real_name='TGA Andere biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_other_fossile = VariableMeta(
            var_name='GWP_ee_tga_other_fossile', 
            attr_name='GWP_ee_tga_other_fossile', 
            real_name='TGA Andere fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_pv_biogenic = VariableMeta(
            var_name='GWP_ee_tga_pv_biogenic', 
            attr_name='GWP_ee_tga_pv_biogenic', 
            real_name='TGA PV biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_pv_fossile = VariableMeta(
            var_name='GWP_ee_tga_pv_fossile', 
            attr_name='GWP_ee_tga_pv_fossile', 
            real_name='TGA PV fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_solarthermal_biogenic = VariableMeta(
            var_name='GWP_ee_tga_solarthermal_biogenic', 
            attr_name='GWP_ee_tga_solarthermal_biogenic', 
            real_name='TGA Solarthermie biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_solarthermal_fossile = VariableMeta(
            var_name='GWP_ee_tga_solarthermal_fossile', 
            attr_name='GWP_ee_tga_solarthermal_fossile', 
            real_name='TGA Solarthermie fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_storage_biogenic = VariableMeta(
            var_name='GWP_ee_tga_storage_biogenic', 
            attr_name='GWP_ee_tga_storage_biogenic', 
            real_name='TGA Speicher biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_storage_fossile = VariableMeta(
            var_name='GWP_ee_tga_storage_fossile', 
            attr_name='GWP_ee_tga_storage_fossile', 
            real_name='TGA Speicher fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_ventilation_biogenic = VariableMeta(
            var_name='GWP_ee_tga_ventilation_biogenic', 
            attr_name='GWP_ee_tga_ventilation_biogenic', 
            real_name='TGA Lüftung biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_tga_ventilation_fossile = VariableMeta(
            var_name='GWP_ee_tga_ventilation_fossile', 
            attr_name='GWP_ee_tga_ventilation_fossile', 
            real_name='TGA Lüftung fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_walls_biogenic = VariableMeta(
            var_name='GWP_ee_walls_biogenic', 
            attr_name='GWP_ee_walls_biogenic', 
            real_name='Bauteil Außenwand biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_walls_fossile = VariableMeta(
            var_name='GWP_ee_walls_fossile', 
            attr_name='GWP_ee_walls_fossile', 
            real_name='Bauteil Außenwand fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_windows_bigenic = VariableMeta(
            var_name='GWP_ee_windows_bigenic', 
            attr_name='GWP_ee_windows_bigenic', 
            real_name='Bauteil Fenster biogen', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ee_windows_fossile = VariableMeta(
            var_name='GWP_ee_windows_fossile', 
            attr_name='GWP_ee_windows_fossile', 
            real_name='Bauteil Fenster fossil', 
            unit='GWP 100A (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_emInt_PV_feedin = VariableMeta(
            var_name='GWP_emInt_PV_feedin', 
            attr_name='GWP_emInt_PV_feedin', 
            real_name='Emissions-Intensität Netzeinspeisung', 
            unit='gCO2eq/kWh', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_emInt_batt_charge = VariableMeta(
            var_name='GWP_emInt_batt_charge', 
            attr_name='GWP_emInt_batt_charge', 
            real_name='Emissions-Intensität Batterie Beladung', 
            unit='gCO2eq/kWh', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_emInt_ev_charge = VariableMeta(
            var_name='GWP_emInt_ev_charge', 
            attr_name='GWP_emInt_ev_charge', 
            real_name='Emissions-Intensität EV ladung', 
            unit='gCO2eq/kWh', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_emInt_flex = VariableMeta(
            var_name='GWP_emInt_flex', 
            attr_name='GWP_emInt_flex', 
            real_name='Emissions-Intensität Flexibler Netzbezug', 
            unit='gCO2eq/kWh', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_emInt_grid = VariableMeta(
            var_name='GWP_emInt_grid', 
            attr_name='GWP_emInt_grid', 
            real_name='Emissions-Intensität Netzstrombezug', 
            unit='gCO2eq/kWh', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_emInt_grid_avg = VariableMeta(
            var_name='GWP_emInt_grid_avg', 
            attr_name='GWP_emInt_grid_avg', 
            real_name='Emissions-Intensität Netzstrom allgemein', 
            unit='gCO2eq/kWh', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_general_name = VariableMeta(
            var_name='GWP_general_name', 
            attr_name='GWP_general_name', 
            real_name='Typ Bauliche Maßnahmen Allgemein', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ground_name = VariableMeta(
            var_name='GWP_ground_name', 
            attr_name='GWP_ground_name', 
            real_name='Bauweise Erdb. Fußboden beheizt', 
            unit=None, 
            type_name='userinput', 
            comment='COMP_name_floor', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_lc_EE_total = VariableMeta(
            var_name='GWP_lc_EE_total', 
            attr_name='GWP_lc_EE_total', 
            real_name='EE THG-Emissionen 2025-2075', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_lc_OE_total = VariableMeta(
            var_name='GWP_lc_OE_total', 
            attr_name='GWP_lc_OE_total', 
            real_name='OE THG-Emissionen 2025-2075', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_lc_total = VariableMeta(
            var_name='GWP_lc_total', 
            attr_name='GWP_lc_total', 
            real_name='THG-Emissionen 2025-2075', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_life_battery = VariableMeta(
            var_name='GWP_life_battery', 
            attr_name='GWP_life_battery', 
            real_name='TGA E-Batterie Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_ceilings = VariableMeta(
            var_name='GWP_life_ceilings', 
            attr_name='GWP_life_ceilings', 
            real_name='Bauteil Zwischengeschoßdecken Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_direct = VariableMeta(
            var_name='GWP_life_direct', 
            attr_name='GWP_life_direct', 
            real_name='Baulich \nDirekteingabe Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_general = VariableMeta(
            var_name='GWP_life_general', 
            attr_name='GWP_life_general', 
            real_name='Baulich Allgemein Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_ground = VariableMeta(
            var_name='GWP_life_ground', 
            attr_name='GWP_life_ground', 
            real_name='Bauteil Decke gegen Erdreich / Keller Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_other = VariableMeta(
            var_name='GWP_life_other', 
            attr_name='GWP_life_other', 
            real_name='Baulich Andere Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_roof = VariableMeta(
            var_name='GWP_life_roof', 
            attr_name='GWP_life_roof', 
            real_name='Bauteil Dach Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_solarthermal = VariableMeta(
            var_name='GWP_life_solarthermal', 
            attr_name='GWP_life_solarthermal', 
            real_name='TGA Solarthermie Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_storage = VariableMeta(
            var_name='GWP_life_storage', 
            attr_name='GWP_life_storage', 
            real_name='TGA Speicher Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_tga_boreholes = VariableMeta(
            var_name='GWP_life_tga_boreholes', 
            attr_name='GWP_life_tga_boreholes', 
            real_name='TGA Erdsonden Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_tga_general = VariableMeta(
            var_name='GWP_life_tga_general', 
            attr_name='GWP_life_tga_general', 
            real_name='TGA Allgemein Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_tga_other = VariableMeta(
            var_name='GWP_life_tga_other', 
            attr_name='GWP_life_tga_other', 
            real_name='TGA Andere Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_tga_pv = VariableMeta(
            var_name='GWP_life_tga_pv', 
            attr_name='GWP_life_tga_pv', 
            real_name='TGA PV Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_tga_ventilation = VariableMeta(
            var_name='GWP_life_tga_ventilation', 
            attr_name='GWP_life_tga_ventilation', 
            real_name='TGA Lüftung Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_walls = VariableMeta(
            var_name='GWP_life_walls', 
            attr_name='GWP_life_walls', 
            real_name='Bauteil Außenwand Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_life_windows = VariableMeta(
            var_name='GWP_life_windows', 
            attr_name='GWP_life_windows', 
            real_name='Bauteil Fenster Lebensdauer', 
            unit='Jahre', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_miv_count_ev = VariableMeta(
            var_name='GWP_miv_count_ev', 
            attr_name='GWP_miv_count_ev', 
            real_name='GWP Herstellung E-Cars', 
            unit='Anzahl Fahrzeuge', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_miv_count_fossile = VariableMeta(
            var_name='GWP_miv_count_fossile', 
            attr_name='GWP_miv_count_fossile', 
            real_name='GWP Herstellung Verbrenner', 
            unit='Anzahl Fahrzeuge', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_mobility_car_gpPKm = VariableMeta(
            var_name='GWP_mobility_car_gpPKm', 
            attr_name='GWP_mobility_car_gpPKm', 
            real_name='GWP Mobilität PKW', 
            unit='GWP 100S (gCO2equiv/Pkm)', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_mobility_construction_ev = VariableMeta(
            var_name='GWP_mobility_construction_ev', 
            attr_name='GWP_mobility_construction_ev', 
            real_name='GWP E-Car', 
            unit='t CO2/Fahrzeug', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_mobility_construction_fossil = VariableMeta(
            var_name='GWP_mobility_construction_fossil', 
            attr_name='GWP_mobility_construction_fossil', 
            real_name='GWP Verbrenner', 
            unit='t CO2/Fahrzeug', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_mobility_moped_gpPKm = VariableMeta(
            var_name='GWP_mobility_moped_gpPKm', 
            attr_name='GWP_mobility_moped_gpPKm', 
            real_name='GWP Mobilität Moped', 
            unit='GWP 100S (gCO2equiv/Pkm)', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_oe = VariableMeta(
            var_name='GWP_oe', 
            attr_name='GWP_oe', 
            real_name='GWP Quartier (Gebäude+MIV)', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_oe_battery_charge = VariableMeta(
            var_name='GWP_oe_battery_charge', 
            attr_name='GWP_oe_battery_charge', 
            real_name='Betrieb Batterie Beladung', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_biomass = VariableMeta(
            var_name='GWP_oe_biomass', 
            attr_name='GWP_oe_biomass', 
            real_name='Betrieb HKLS Biomasse', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_building = VariableMeta(
            var_name='GWP_oe_building', 
            attr_name='GWP_oe_building', 
            real_name='Betrieb Gebäude', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_district_heating = VariableMeta(
            var_name='GWP_oe_district_heating', 
            attr_name='GWP_oe_district_heating', 
            real_name='Betrieb HKLS Fernwärme', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_flex_build = VariableMeta(
            var_name='GWP_oe_flex_build', 
            attr_name='GWP_oe_flex_build', 
            real_name='Betrieb Gebäude Flexibler Netzbezug', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_grid_build = VariableMeta(
            var_name='GWP_oe_grid_build', 
            attr_name='GWP_oe_grid_build', 
            real_name='Betrieb Gebäude Netzstrombezug', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_grid_feedin = VariableMeta(
            var_name='GWP_oe_grid_feedin', 
            attr_name='GWP_oe_grid_feedin', 
            real_name='Betrieb Netzeinspeisung', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_biomass = VariableMeta(
            var_name='GWP_oe_lc_biomass', 
            attr_name='GWP_oe_lc_biomass', 
            real_name='LZ Betrieb HKLS Biomasse', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_building = VariableMeta(
            var_name='GWP_oe_lc_building', 
            attr_name='GWP_oe_lc_building', 
            real_name='LZ Betrieb Gebäude', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_district_heating = VariableMeta(
            var_name='GWP_oe_lc_district_heating', 
            attr_name='GWP_oe_lc_district_heating', 
            real_name='LZ Betrieb HKLS Fernwärme', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_emission = VariableMeta(
            var_name='GWP_oe_lc_emission', 
            attr_name='GWP_oe_lc_emission', 
            real_name='LZ Betrieb Gebäude Emissionen', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_emission_savings = VariableMeta(
            var_name='GWP_oe_lc_emission_savings', 
            attr_name='GWP_oe_lc_emission_savings', 
            real_name='LZ Betrieb Gebäude Vermiedene Emissionen', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_flex_build = VariableMeta(
            var_name='GWP_oe_lc_flex_build', 
            attr_name='GWP_oe_lc_flex_build', 
            real_name='LZ Betrieb Gebäude Flexibler Netzbezug', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_grid_build = VariableMeta(
            var_name='GWP_oe_lc_grid_build', 
            attr_name='GWP_oe_lc_grid_build', 
            real_name='LZ Betrieb Gebäude Netzstrombezug', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_grid_feedin = VariableMeta(
            var_name='GWP_oe_lc_grid_feedin', 
            attr_name='GWP_oe_lc_grid_feedin', 
            real_name='LZ Betrieb Netzeinspeisung', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_mob = VariableMeta(
            var_name='GWP_oe_lc_mob', 
            attr_name='GWP_oe_lc_mob', 
            real_name='Mobilität', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_mob_ev = VariableMeta(
            var_name='GWP_oe_lc_mob_ev', 
            attr_name='GWP_oe_lc_mob_ev', 
            real_name='LCA OE MIV elektrisch', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_mob_export = VariableMeta(
            var_name='GWP_oe_lc_mob_export', 
            attr_name='GWP_oe_lc_mob_export', 
            real_name='LV Mobilitäts-Export', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_mob_fossile = VariableMeta(
            var_name='GWP_oe_lc_mob_fossile', 
            attr_name='GWP_oe_lc_mob_fossile', 
            real_name='LCA OE MIV fossil', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2050', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_natural_gas = VariableMeta(
            var_name='GWP_oe_lc_natural_gas', 
            attr_name='GWP_oe_lc_natural_gas', 
            real_name='LZ Betrieb HKLS Erdgas', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_lc_other = VariableMeta(
            var_name='GWP_oe_lc_other', 
            attr_name='GWP_oe_lc_other', 
            real_name='LZ Betrieb HKLS Sonstige', 
            unit='GWP 100S (kgCO2equiv/m²BGF)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='2025-2075', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_mob = VariableMeta(
            var_name='GWP_oe_mob', 
            attr_name='GWP_oe_mob', 
            real_name='Mobilität (Ursächlich)', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_mob_ev = VariableMeta(
            var_name='GWP_oe_mob_ev', 
            attr_name='GWP_oe_mob_ev', 
            real_name='GWP MIV elektrisch INSGESAMTE LADUNG', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_mob_ev_export = VariableMeta(
            var_name='GWP_oe_mob_ev_export', 
            attr_name='GWP_oe_mob_ev_export', 
            real_name='GWP MIV Export (Anderer Verkehr)', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_mob_fossile = VariableMeta(
            var_name='GWP_oe_mob_fossile', 
            attr_name='GWP_oe_mob_fossile', 
            real_name='GWP MIV fossil', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_natural_gas = VariableMeta(
            var_name='GWP_oe_natural_gas', 
            attr_name='GWP_oe_natural_gas', 
            real_name='Betrieb HKLS Erdgas', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_oe_other = VariableMeta(
            var_name='GWP_oe_other', 
            attr_name='GWP_oe_other', 
            real_name='Betrieb HKLS Sonstige', 
            unit='GWP pro Jahr (kgCO2equiv/m²BGFa)', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='THG-ImportExport Bilanz', 
            area='pro Jahr', 
            label=None, 
            var_cat=None
)
        self.GWP_other_name = VariableMeta(
            var_name='GWP_other_name', 
            attr_name='GWP_other_name', 
            real_name='Typ Andere bauliche Maßnahmen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_pv_name = VariableMeta(
            var_name='GWP_pv_name', 
            attr_name='GWP_pv_name', 
            real_name='Typ PV-Anlage', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_biomass = VariableMeta(
            var_name='GWP_rcpi_biomass', 
            attr_name='GWP_rcpi_biomass', 
            real_name='Absenkpfad-Integral Biomasse', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_district_heating = VariableMeta(
            var_name='GWP_rcpi_district_heating', 
            attr_name='GWP_rcpi_district_heating', 
            real_name='Absenkpfad-Integral Fernwärme', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_fossil = VariableMeta(
            var_name='GWP_rcpi_fossil', 
            attr_name='GWP_rcpi_fossil', 
            real_name='Absenkpfad-Integral Fossil', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_grid = VariableMeta(
            var_name='GWP_rcpi_grid', 
            attr_name='GWP_rcpi_grid', 
            real_name='Absenkpfad-Integral Netzstrom', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_grid_substition = VariableMeta(
            var_name='GWP_rcpi_grid_substition', 
            attr_name='GWP_rcpi_grid_substition', 
            real_name='Absenkpfad-Integral Substi', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_mob_fossile = VariableMeta(
            var_name='GWP_rcpi_mob_fossile', 
            attr_name='GWP_rcpi_mob_fossile', 
            real_name='Absenkpfad-Integral MIV Fossil', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_natural_gas = VariableMeta(
            var_name='GWP_rcpi_natural_gas', 
            attr_name='GWP_rcpi_natural_gas', 
            real_name='Absenkpfad-Integral Gas', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_rcpi_renewable = VariableMeta(
            var_name='GWP_rcpi_renewable', 
            attr_name='GWP_rcpi_renewable', 
            real_name='Absenkpfad-Integral Erneuerbar', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ref_area_ceilings = VariableMeta(
            var_name='GWP_ref_area_ceilings', 
            attr_name='GWP_ref_area_ceilings', 
            real_name='FU Geschossdecke', 
            unit='m²', 
            type_name='userinput', 
            comment='COMP_area_ceilings', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ref_area_fundament = VariableMeta(
            var_name='GWP_ref_area_fundament', 
            attr_name='GWP_ref_area_fundament', 
            real_name='FU Erdb. Fußboden beheizt', 
            unit='m²', 
            type_name='userinput', 
            comment='COMP_area_floor', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ref_area_roof = VariableMeta(
            var_name='GWP_ref_area_roof', 
            attr_name='GWP_ref_area_roof', 
            real_name='FU Dach', 
            unit='m²', 
            type_name='userinput', 
            comment='COMP_area_roof', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ref_area_walls = VariableMeta(
            var_name='GWP_ref_area_walls', 
            attr_name='GWP_ref_area_walls', 
            real_name='FU Außenwand', 
            unit='m²', 
            type_name='userinput', 
            comment='COMP_area_wall', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ref_area_windows = VariableMeta(
            var_name='GWP_ref_area_windows', 
            attr_name='GWP_ref_area_windows', 
            real_name='FU Fenster', 
            unit='m²', 
            type_name='userinput', 
            comment='COMP_area_windows', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_boreholes = VariableMeta(
            var_name='GWP_refratio_boreholes', 
            attr_name='GWP_refratio_boreholes', 
            real_name='Bezug pro BGF (Erdsonden)', 
            unit='StkErdsonden/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_ceilings = VariableMeta(
            var_name='GWP_refratio_ceilings', 
            attr_name='GWP_refratio_ceilings', 
            real_name='Bezug pro BGF (Zwischengeschoßdecken)', 
            unit='m²Zwd/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_fundament = VariableMeta(
            var_name='GWP_refratio_fundament', 
            attr_name='GWP_refratio_fundament', 
            real_name='Bezug pro BGF (Fundament)', 
            unit='m²KB/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_pv = VariableMeta(
            var_name='GWP_refratio_pv', 
            attr_name='GWP_refratio_pv', 
            real_name='Bezug pro BGF (PV)', 
            unit='m²PV/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_roof = VariableMeta(
            var_name='GWP_refratio_roof', 
            attr_name='GWP_refratio_roof', 
            real_name='Bezug pro BGF (Dach)', 
            unit='m²Dach/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_walls = VariableMeta(
            var_name='GWP_refratio_walls', 
            attr_name='GWP_refratio_walls', 
            real_name='Bezug pro BGF (Außenwand)', 
            unit='m²AW/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_refratio_windows = VariableMeta(
            var_name='GWP_refratio_windows', 
            attr_name='GWP_refratio_windows', 
            real_name='Bezug pro BGF (Fenster)', 
            unit='m²Fe/m²BGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_roof_name = VariableMeta(
            var_name='GWP_roof_name', 
            attr_name='GWP_roof_name', 
            real_name='Bauweise Dach', 
            unit=None, 
            type_name='userinput', 
            comment='COMP_name_roof', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_solarthermal_name = VariableMeta(
            var_name='GWP_solarthermal_name', 
            attr_name='GWP_solarthermal_name', 
            real_name='Typ Solarthermie', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_storage_name = VariableMeta(
            var_name='GWP_storage_name', 
            attr_name='GWP_storage_name', 
            real_name='Typ Pufferspeicher', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_tga_general_name = VariableMeta(
            var_name='GWP_tga_general_name', 
            attr_name='GWP_tga_general_name', 
            real_name='Typ  Allgemein', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_tga_other_name = VariableMeta(
            var_name='GWP_tga_other_name', 
            attr_name='GWP_tga_other_name', 
            real_name='Typ  Andere bauliche Maßnahmen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_ventilation_name = VariableMeta(
            var_name='GWP_ventilation_name', 
            attr_name='GWP_ventilation_name', 
            real_name='Typ Komfortlüftung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.GWP_walls_name = VariableMeta(
            var_name='GWP_walls_name', 
            attr_name='GWP_walls_name', 
            real_name='Bauweise Außenwand', 
            unit=None, 
            type_name='userinput', 
            comment='COMP_name_wall', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Grid_to_Ec_min = VariableMeta(
            var_name='Grid_to_Ec_min', 
            attr_name='Grid_to_Ec_min', 
            real_name='Netzstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.Grid_to_Edhw_min = VariableMeta(
            var_name='Grid_to_Edhw_min', 
            attr_name='Grid_to_Edhw_min', 
            real_name='Netzstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.Grid_to_Eev_min = VariableMeta(
            var_name='Grid_to_Eev_min', 
            attr_name='Grid_to_Eev_min', 
            real_name='Netzstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='MIV', 
            label=None, 
            var_cat=None
)
        self.Grid_to_Eh_min = VariableMeta(
            var_name='Grid_to_Eh_min', 
            attr_name='Grid_to_Eh_min', 
            real_name='Netzstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.Grid_to_Ev_min = VariableMeta(
            var_name='Grid_to_Ev_min', 
            attr_name='Grid_to_Ev_min', 
            real_name='Netzstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Lüftung', 
            label=None, 
            var_cat=None
)
        self.Grid_to_building_min = VariableMeta(
            var_name='Grid_to_building_min', 
            attr_name='Grid_to_building_min', 
            real_name='Netzstrom → Gebäude', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Gebäude', 
            label=None, 
            var_cat=None
)
        self.Grid_to_min = VariableMeta(
            var_name='Grid_to_min', 
            attr_name='Grid_to_min', 
            real_name='Netzstrom → Quartier', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.Grid_to_plugloads = VariableMeta(
            var_name='Grid_to_plugloads', 
            attr_name='Grid_to_plugloads', 
            real_name='Netzstrom → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Haushaltsstrom', 
            label=None, 
            var_cat=None
)
        self.Grid_total_flexandnotflex = VariableMeta(
            var_name='Grid_total_flexandnotflex', 
            attr_name='Grid_total_flexandnotflex', 
            real_name='Netzstrom insg. (Flexibel und Inflexibel)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.NFA_cooled = VariableMeta(
            var_name='NFA_cooled', 
            attr_name='NFA_cooled', 
            real_name='Fläche Aktive Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_mechvent = VariableMeta(
            var_name='NFA_mechvent', 
            attr_name='NFA_mechvent', 
            real_name='Mechanische Lüftung Nettogeschoßfläche', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_office = VariableMeta(
            var_name='NFA_office', 
            attr_name='NFA_office', 
            real_name='NGF Büro', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_other = VariableMeta(
            var_name='NFA_other', 
            attr_name='NFA_other', 
            real_name='NGF Sonstige', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_residential = VariableMeta(
            var_name='NFA_residential', 
            attr_name='NFA_residential', 
            real_name='NGF Wohnen', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_retailfood = VariableMeta(
            var_name='NFA_retailfood', 
            attr_name='NFA_retailfood', 
            real_name='NGF Handel Lebensmittel', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_retailother = VariableMeta(
            var_name='NFA_retailother', 
            attr_name='NFA_retailother', 
            real_name='NGF Handel sonstiger', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_schoolprim = VariableMeta(
            var_name='NFA_schoolprim', 
            attr_name='NFA_schoolprim', 
            real_name='NGF Bildung primär', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_schoolsec = VariableMeta(
            var_name='NFA_schoolsec', 
            attr_name='NFA_schoolsec', 
            real_name='NGF Bildung sekundär', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio = VariableMeta(
            var_name='NFA_to_GFA_ratio', 
            attr_name='NFA_to_GFA_ratio', 
            real_name='NGF/BGF Quartier', 
            unit='Faktor', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_office = VariableMeta(
            var_name='NFA_to_GFA_ratio_office', 
            attr_name='NFA_to_GFA_ratio_office', 
            real_name='NGF/BGF  Büro', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_other = VariableMeta(
            var_name='NFA_to_GFA_ratio_other', 
            attr_name='NFA_to_GFA_ratio_other', 
            real_name='NGF/BGF Sonstige', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_residential = VariableMeta(
            var_name='NFA_to_GFA_ratio_residential', 
            attr_name='NFA_to_GFA_ratio_residential', 
            real_name='NGF/BGF Wohnen', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_retailfood = VariableMeta(
            var_name='NFA_to_GFA_ratio_retailfood', 
            attr_name='NFA_to_GFA_ratio_retailfood', 
            real_name='NGF/BGF Lebensmittelhandel', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_retailother = VariableMeta(
            var_name='NFA_to_GFA_ratio_retailother', 
            attr_name='NFA_to_GFA_ratio_retailother', 
            real_name='NGF/BGF Handel sonstiger', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_schoolprim = VariableMeta(
            var_name='NFA_to_GFA_ratio_schoolprim', 
            attr_name='NFA_to_GFA_ratio_schoolprim', 
            real_name='NGF/BGF Bildung primär', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_to_GFA_ratio_schoolsec = VariableMeta(
            var_name='NFA_to_GFA_ratio_schoolsec', 
            attr_name='NFA_to_GFA_ratio_schoolsec', 
            real_name='NGF/BGF Bildung sekundär', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_total = VariableMeta(
            var_name='NFA_total', 
            attr_name='NFA_total', 
            real_name='NGF Quartier', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFA_windowvent = VariableMeta(
            var_name='NFA_windowvent', 
            attr_name='NFA_windowvent', 
            real_name='Fensterlüftung Nettogeschoßfläche', 
            unit='m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFAfrac_c = VariableMeta(
            var_name='NFAfrac_c', 
            attr_name='NFAfrac_c', 
            real_name='NGF Anteil Aktive Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFAfrac_u = VariableMeta(
            var_name='NFAfrac_u', 
            attr_name='NFAfrac_u', 
            real_name='NGF Anteil ohne aktive Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFV_c = VariableMeta(
            var_name='NFV_c', 
            attr_name='NFV_c', 
            real_name='Raumvolumen gekühlt', 
            unit='m³netto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFV_mechvent = VariableMeta(
            var_name='NFV_mechvent', 
            attr_name='NFV_mechvent', 
            real_name='Mechanische Lüftung Raumvolumen', 
            unit='m³netto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFV_total = VariableMeta(
            var_name='NFV_total', 
            attr_name='NFV_total', 
            real_name='Raumvolumen Quartier', 
            unit='m³netto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFV_u = VariableMeta(
            var_name='NFV_u', 
            attr_name='NFV_u', 
            real_name='Raumvolumen ungekühlt', 
            unit='m³netto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.NFV_windowvent = VariableMeta(
            var_name='NFV_windowvent', 
            attr_name='NFV_windowvent', 
            real_name='Fensterlüftung Raumvolumen', 
            unit='m³netto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_balance = VariableMeta(
            var_name='PEI_balance', 
            attr_name='PEI_balance', 
            real_name='PE-Bilanz Netzäquivalent', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_biomass = VariableMeta(
            var_name='PEI_biomass', 
            attr_name='PEI_biomass', 
            real_name='HKLS Biomasse', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_cf_density = VariableMeta(
            var_name='PEI_cf_density', 
            attr_name='PEI_cf_density', 
            real_name='Kontext bauliche Dichte', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_cf_mobility = VariableMeta(
            var_name='PEI_cf_mobility', 
            attr_name='PEI_cf_mobility', 
            real_name='Kontext Mobilität', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_cf_renovation = VariableMeta(
            var_name='PEI_cf_renovation', 
            attr_name='PEI_cf_renovation', 
            real_name='Kontext Sanierung', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_demand = VariableMeta(
            var_name='PEI_demand', 
            attr_name='PEI_demand', 
            real_name='Betriebsenergie', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_district_heating = VariableMeta(
            var_name='PEI_district_heating', 
            attr_name='PEI_district_heating', 
            real_name='HKLS Fernwärme', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_el_hvac = VariableMeta(
            var_name='PEI_el_hvac', 
            attr_name='PEI_el_hvac', 
            real_name='HKLS Strom', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_el_plugloads = VariableMeta(
            var_name='PEI_el_plugloads', 
            attr_name='PEI_el_plugloads', 
            real_name='Nutzerstrom', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_evExtCharge_import = VariableMeta(
            var_name='PEI_evExtCharge_import', 
            attr_name='PEI_evExtCharge_import', 
            real_name='EV Externe Beladung', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_evOtherTravel_export = VariableMeta(
            var_name='PEI_evOtherTravel_export', 
            attr_name='PEI_evOtherTravel_export', 
            real_name='EV Other Travels', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_export = VariableMeta(
            var_name='PEI_export', 
            attr_name='PEI_export', 
            real_name='Primärenergie-Export', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_flex_import = VariableMeta(
            var_name='PEI_flex_import', 
            attr_name='PEI_flex_import', 
            real_name='Flexibler Bezug', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_grid_import = VariableMeta(
            var_name='PEI_grid_import', 
            attr_name='PEI_grid_import', 
            real_name='Netzbezug', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_import = VariableMeta(
            var_name='PEI_import', 
            attr_name='PEI_import', 
            real_name='Primärenergie-Import', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_importExport_balance = VariableMeta(
            var_name='PEI_importExport_balance', 
            attr_name='PEI_importExport_balance', 
            real_name='importExport Saldo Projektwert - Zielwert', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_mob_el = VariableMeta(
            var_name='PEI_mob_el', 
            attr_name='PEI_mob_el', 
            real_name='MIV Elektrisch', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_mob_fossile = VariableMeta(
            var_name='PEI_mob_fossile', 
            attr_name='PEI_mob_fossile', 
            real_name='MIV Fossil', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_mob_total = VariableMeta(
            var_name='PEI_mob_total', 
            attr_name='PEI_mob_total', 
            real_name='Mobilität (MIV)', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_natural_gas = VariableMeta(
            var_name='PEI_natural_gas', 
            attr_name='PEI_natural_gas', 
            real_name='HKLS Erdgas', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_other = VariableMeta(
            var_name='PEI_other', 
            attr_name='PEI_other', 
            real_name='HKLS Sonstige', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_pv_export = VariableMeta(
            var_name='PEI_pv_export', 
            attr_name='PEI_pv_export', 
            real_name='PV Netzeinspeisung PE', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_saldo_project = VariableMeta(
            var_name='PEI_saldo_project', 
            attr_name='PEI_saldo_project', 
            real_name='PE-IE-Bilanz Projektwert', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_saldo_target = VariableMeta(
            var_name='PEI_saldo_target', 
            attr_name='PEI_saldo_target', 
            real_name='PE-IE-Bilanz Zielwert', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-ImportExport Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_storage_losses = VariableMeta(
            var_name='PEI_storage_losses', 
            attr_name='PEI_storage_losses', 
            real_name='Speicher-Verluste', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_sub_PV = VariableMeta(
            var_name='PEI_sub_PV', 
            attr_name='PEI_sub_PV', 
            real_name='Lokale Erneuerbare (Netzstrom Substitutionsäquivalent)', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PEI_sub_flex = VariableMeta(
            var_name='PEI_sub_flex', 
            attr_name='PEI_sub_flex', 
            real_name='Energieflexibilität (Netzstrom Substitutionsäquivalent)', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Netzäquivalenz-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_efficiency = VariableMeta(
            var_name='PV_efficiency', 
            attr_name='PV_efficiency', 
            real_name='PV Wechselrichter Effizienz', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_id = VariableMeta(
            var_name='PV_id', 
            attr_name='PV_id', 
            real_name='PV Profil ID', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_is_used = VariableMeta(
            var_name='PV_is_used', 
            attr_name='PV_is_used', 
            real_name='PV Nutzung', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_kWp = VariableMeta(
            var_name='PV_kWp', 
            attr_name='PV_kWp', 
            real_name='PV Installierte Leistung', 
            unit='kWp', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_m2_per_kWp = VariableMeta(
            var_name='PV_m2_per_kWp', 
            attr_name='PV_m2_per_kWp', 
            real_name='Spezifische PV Fläche', 
            unit='m2/kWp', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_module_area = VariableMeta(
            var_name='PV_module_area', 
            attr_name='PV_module_area', 
            real_name='PV-Modulfläche', 
            unit='m²', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_own_consumption = VariableMeta(
            var_name='PV_own_consumption', 
            attr_name='PV_own_consumption', 
            real_name='PV Eigenverbrauch insgesamt', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PV', 
            area=None, 
            label='SCR', 
            var_cat=None
)
        self.PV_own_consumption_direct = VariableMeta(
            var_name='PV_own_consumption_direct', 
            attr_name='PV_own_consumption_direct', 
            real_name='PV Eigenverbrauch direkt', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PV', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_own_consumption_flex = VariableMeta(
            var_name='PV_own_consumption_flex', 
            attr_name='PV_own_consumption_flex', 
            real_name='PV Eigenverbrauch flex', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PV', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_profile_name = VariableMeta(
            var_name='PV_profile_name', 
            attr_name='PV_profile_name', 
            real_name='PV Profil Name', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_scale = VariableMeta(
            var_name='PV_scale', 
            attr_name='PV_scale', 
            real_name='PV Skalierungsfaktor Profil', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_to_Batt = VariableMeta(
            var_name='PV_to_Batt', 
            attr_name='PV_to_Batt', 
            real_name='PV Überdeckung e-Speicher Beladung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='e-Speicher Beladung', 
            label=None, 
            var_cat=None
)
        self.PV_to_Ec_flex = VariableMeta(
            var_name='PV_to_Ec_flex', 
            attr_name='PV_to_Ec_flex', 
            real_name='PV Überdeckung Kühlen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.PV_to_Ec_min = VariableMeta(
            var_name='PV_to_Ec_min', 
            attr_name='PV_to_Ec_min', 
            real_name='PV Direktdeckung Kühlen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.PV_to_Edhw = VariableMeta(
            var_name='PV_to_Edhw', 
            attr_name='PV_to_Edhw', 
            real_name='PV Überdeckung Warmwasser', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.PV_to_Edhw_direct = VariableMeta(
            var_name='PV_to_Edhw_direct', 
            attr_name='PV_to_Edhw_direct', 
            real_name='PV Überdeckung WW\nE-Stab', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='WW\nE-Stab', 
            label=None, 
            var_cat=None
)
        self.PV_to_Edhw_min = VariableMeta(
            var_name='PV_to_Edhw_min', 
            attr_name='PV_to_Edhw_min', 
            real_name='PV Direktdeckung Warmwasser', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.PV_to_Eev_flex = VariableMeta(
            var_name='PV_to_Eev_flex', 
            attr_name='PV_to_Eev_flex', 
            real_name='PV Überdeckung MIV', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='MIV', 
            label=None, 
            var_cat=None
)
        self.PV_to_Eev_min = VariableMeta(
            var_name='PV_to_Eev_min', 
            attr_name='PV_to_Eev_min', 
            real_name='PV Direktdeckung MIV', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='MIV', 
            label=None, 
            var_cat=None
)
        self.PV_to_Egrid = VariableMeta(
            var_name='PV_to_Egrid', 
            attr_name='PV_to_Egrid', 
            real_name='PV Netzeinspeisung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.PV_to_Eh_flex = VariableMeta(
            var_name='PV_to_Eh_flex', 
            attr_name='PV_to_Eh_flex', 
            real_name='PV Überdeckung Heizen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.PV_to_Eh_min = VariableMeta(
            var_name='PV_to_Eh_min', 
            attr_name='PV_to_Eh_min', 
            real_name='PV Direktdeckung Heizen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.PV_to_Ev_min = VariableMeta(
            var_name='PV_to_Ev_min', 
            attr_name='PV_to_Ev_min', 
            real_name='PV Direktdeckung Lüftung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Lüftung', 
            label=None, 
            var_cat=None
)
        self.PV_to_plugloads = VariableMeta(
            var_name='PV_to_plugloads', 
            attr_name='PV_to_plugloads', 
            real_name='PV Direktdeckung Haushaltsstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Haushaltsstrom', 
            label=None, 
            var_cat=None
)
        self.PV_total = VariableMeta(
            var_name='PV_total', 
            attr_name='PV_total', 
            real_name='PV Ertrag', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Erneuerbare Erzeugung', 
            label=None, 
            var_cat=None
)
        self.PV_total_direct = VariableMeta(
            var_name='PV_total_direct', 
            attr_name='PV_total_direct', 
            real_name='PV Direktdeckung Quartier', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.PV_total_flex = VariableMeta(
            var_name='PV_total_flex', 
            attr_name='PV_total_flex', 
            real_name='PV Überdeckung Quartier', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.Plight_max_office = VariableMeta(
            var_name='Plight_max_office', 
            attr_name='Plight_max_office', 
            real_name='Beleuchtung maximal Büro', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plight_max_schoolprim = VariableMeta(
            var_name='Plight_max_schoolprim', 
            attr_name='Plight_max_schoolprim', 
            real_name='Beleuchtung maximal Ausbildung Primär', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plight_max_schoolsec = VariableMeta(
            var_name='Plight_max_schoolsec', 
            attr_name='Plight_max_schoolsec', 
            real_name='Beleuchtung maximal Ausbildung Sekundär', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plight_min_office = VariableMeta(
            var_name='Plight_min_office', 
            attr_name='Plight_min_office', 
            real_name='Beleuchtung minimal Büro', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plight_min_schoolprim = VariableMeta(
            var_name='Plight_min_schoolprim', 
            attr_name='Plight_min_schoolprim', 
            real_name='Beleuchtung minimal Ausbildung Primär', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plight_min_schoolsec = VariableMeta(
            var_name='Plight_min_schoolsec', 
            attr_name='Plight_min_schoolsec', 
            real_name='Beleuchtung minimal Ausbildung Sekundär', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_office = VariableMeta(
            var_name='Plugloads_scale_office', 
            attr_name='Plugloads_scale_office', 
            real_name='Nutzerstrom Büro', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_other = VariableMeta(
            var_name='Plugloads_scale_other', 
            attr_name='Plugloads_scale_other', 
            real_name='Nutzerstrom Sonstige Nutzung', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_res = VariableMeta(
            var_name='Plugloads_scale_res', 
            attr_name='Plugloads_scale_res', 
            real_name='Nutzerstrom Wohnen', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_retailfood = VariableMeta(
            var_name='Plugloads_scale_retailfood', 
            attr_name='Plugloads_scale_retailfood', 
            real_name='Nutzerstrom Handel Lebensmittel', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_retailother = VariableMeta(
            var_name='Plugloads_scale_retailother', 
            attr_name='Plugloads_scale_retailother', 
            real_name='Nutzerstrom Handel sonstiger', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_schoolprim = VariableMeta(
            var_name='Plugloads_scale_schoolprim', 
            attr_name='Plugloads_scale_schoolprim', 
            real_name='Nutzerstrom Bildung primär', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Plugloads_scale_schoolsec = VariableMeta(
            var_name='Plugloads_scale_schoolsec', 
            attr_name='Plugloads_scale_schoolsec', 
            real_name='Nutzerstrom Bildung sekundär', 
            unit='Faktor', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC = VariableMeta(
            var_name='QC', 
            attr_name='QC', 
            real_name='Kühlbedarf (KB)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='❄️ Kühlbedarf (KB)', 
            var_cat=None
)
        self.QC_aux_1el = VariableMeta(
            var_name='QC_aux_1el', 
            attr_name='QC_aux_1el', 
            real_name='Hilfsstromanteil KLEL1', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_aux_2th = VariableMeta(
            var_name='QC_aux_2th', 
            attr_name='QC_aux_2th', 
            real_name='Hilfsstromanteil KLTh2', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_aux_3el = VariableMeta(
            var_name='QC_aux_3el', 
            attr_name='QC_aux_3el', 
            real_name='Hilfsstromanteil KLEL3', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_aux_fc = VariableMeta(
            var_name='QC_aux_fc', 
            attr_name='QC_aux_fc', 
            real_name='Hilfsstromanteil Freecooling', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_c = VariableMeta(
            var_name='QC_c', 
            attr_name='QC_c', 
            real_name='Kühlbedarf (KB)', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='❄️ Kühlbedarf (KB)', 
            var_cat=None
)
        self.QC_distr_losses_1el = VariableMeta(
            var_name='QC_distr_losses_1el', 
            attr_name='QC_distr_losses_1el', 
            real_name='Verteilverluste 1 El', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_distr_losses_2th = VariableMeta(
            var_name='QC_distr_losses_2th', 
            attr_name='QC_distr_losses_2th', 
            real_name='Verteilverluste 2th', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_distr_losses_3el = VariableMeta(
            var_name='QC_distr_losses_3el', 
            attr_name='QC_distr_losses_3el', 
            real_name='Verteilverluste 3el', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_flex_c = VariableMeta(
            var_name='QC_flex_c', 
            attr_name='QC_flex_c', 
            real_name='Kühlbedarf Flexibel', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='❄️ Kühlbedarf Flexibel', 
            var_cat=None
)
        self.QC_flex_summer = VariableMeta(
            var_name='QC_flex_summer', 
            attr_name='QC_flex_summer', 
            real_name='Kühlbedarf Flexibel', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QC_flex_winter = VariableMeta(
            var_name='QC_flex_winter', 
            attr_name='QC_flex_winter', 
            real_name='Kühlbedarf Flexibel', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QC_flexanteil = VariableMeta(
            var_name='QC_flexanteil', 
            attr_name='QC_flexanteil', 
            real_name='Flexibilitätsanteil', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='Flexibilitätsanteil', 
            var_cat=None
)
        self.QC_flexshare_summer = VariableMeta(
            var_name='QC_flexshare_summer', 
            attr_name='QC_flexshare_summer', 
            real_name='Anteil Flexibler Kühlung an Gesamtkühlung', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QC_flexshare_winter = VariableMeta(
            var_name='QC_flexshare_winter', 
            attr_name='QC_flexshare_winter', 
            real_name='Anteil Flexibler Kühlung an Gesamtkühlung', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label='Flexibilitätsanteil', 
            var_cat=None
)
        self.QC_generation_eff_2th = VariableMeta(
            var_name='QC_generation_eff_2th', 
            attr_name='QC_generation_eff_2th', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung 2 TH', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_min_c = VariableMeta(
            var_name='QC_min_c', 
            attr_name='QC_min_c', 
            real_name='Kühlbedarf Statisch', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='❄️ Kühlbedarf Statisch', 
            var_cat=None
)
        self.QC_min_summer = VariableMeta(
            var_name='QC_min_summer', 
            attr_name='QC_min_summer', 
            real_name='Kühlbedarf Statisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QC_min_winter = VariableMeta(
            var_name='QC_min_winter', 
            attr_name='QC_min_winter', 
            real_name='Kühlbedarf Statisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QC_summer = VariableMeta(
            var_name='QC_summer', 
            attr_name='QC_summer', 
            real_name='Kühlbedarf (KB)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QC_to_EC_1 = VariableMeta(
            var_name='QC_to_EC_1', 
            attr_name='QC_to_EC_1', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung 1 El', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_to_EC_3 = VariableMeta(
            var_name='QC_to_EC_3', 
            attr_name='QC_to_EC_3', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung 3 EL', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QC_winter = VariableMeta(
            var_name='QC_winter', 
            attr_name='QC_winter', 
            real_name='Kühlbedarf (KB)', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QCmax_1el = VariableMeta(
            var_name='QCmax_1el', 
            attr_name='QCmax_1el', 
            real_name='Thermische Leistung 1 EL', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QCmax_2th = VariableMeta(
            var_name='QCmax_2th', 
            attr_name='QCmax_2th', 
            real_name='Thermische Leistung 2 TH', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QCmax_3el = VariableMeta(
            var_name='QCmax_3el', 
            attr_name='QCmax_3el', 
            real_name='Thermische Leistung 3 EL', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QCmax_freecooling = VariableMeta(
            var_name='QCmax_freecooling', 
            attr_name='QCmax_freecooling', 
            real_name='Thermische Leistung Freecooling', 
            unit='W/m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QCmax_room_MW = VariableMeta(
            var_name='QCmax_room_MW', 
            attr_name='QCmax_room_MW', 
            real_name='Thermische Leistung Aufnahmesystem', 
            unit='MW', 
            type_name='calculation', 
            comment='raumseitig', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QCmax_room_m2 = VariableMeta(
            var_name='QCmax_room_m2', 
            attr_name='QCmax_room_m2', 
            real_name='spez. thermische Leistung Aufnahmesystem', 
            unit='W/m²', 
            type_name='userinput', 
            comment='raumseitig', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH = VariableMeta(
            var_name='QH', 
            attr_name='QH', 
            real_name='Heizwärmebedarf', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='♨️ Heizwärmebedarf', 
            var_cat=None
)
        self.QH_aux_el_to_th_1el = VariableMeta(
            var_name='QH_aux_el_to_th_1el', 
            attr_name='QH_aux_el_to_th_1el', 
            real_name='Hilfsstromanteil HZEL1', 
            unit=None, 
            type_name='userinput', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_aux_el_to_th_2th = VariableMeta(
            var_name='QH_aux_el_to_th_2th', 
            attr_name='QH_aux_el_to_th_2th', 
            real_name='Hilfsstromanteil HZTH2', 
            unit=None, 
            type_name='userinput', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_aux_el_to_th_3el = VariableMeta(
            var_name='QH_aux_el_to_th_3el', 
            attr_name='QH_aux_el_to_th_3el', 
            real_name='Hilfsstromanteil HZEL3', 
            unit=None, 
            type_name='userinput', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_aux_el_to_th_4th = VariableMeta(
            var_name='QH_aux_el_to_th_4th', 
            attr_name='QH_aux_el_to_th_4th', 
            real_name='Hilfsstromanteil HZTH4', 
            unit=None, 
            type_name='userinput', 
            comment='am thermischen Energiebedarf', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_aux_wasteheat = VariableMeta(
            var_name='QH_aux_wasteheat', 
            attr_name='QH_aux_wasteheat', 
            real_name='Hilfsstromanteil HZAbwärme', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_c = VariableMeta(
            var_name='QH_c', 
            attr_name='QH_c', 
            real_name='Heizwärmebedarf', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='♨️ Heizwärmebedarf', 
            var_cat=None
)
        self.QH_distr_loss_1el = VariableMeta(
            var_name='QH_distr_loss_1el', 
            attr_name='QH_distr_loss_1el', 
            real_name='Verteilverluste HZEL1', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_distr_loss_2th = VariableMeta(
            var_name='QH_distr_loss_2th', 
            attr_name='QH_distr_loss_2th', 
            real_name='Verteilverluste HZTH2', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_distr_loss_3el = VariableMeta(
            var_name='QH_distr_loss_3el', 
            attr_name='QH_distr_loss_3el', 
            real_name='Verteilverluste HZEL3', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_distr_loss_4th = VariableMeta(
            var_name='QH_distr_loss_4th', 
            attr_name='QH_distr_loss_4th', 
            real_name='Verteilverluste HZTH4', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_flex_c = VariableMeta(
            var_name='QH_flex_c', 
            attr_name='QH_flex_c', 
            real_name='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='♨️ Heizwärmebedarf Flexibel', 
            var_cat=None
)
        self.QH_flex_summer = VariableMeta(
            var_name='QH_flex_summer', 
            attr_name='QH_flex_summer', 
            real_name='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QH_flex_u = VariableMeta(
            var_name='QH_flex_u', 
            attr_name='QH_flex_u', 
            real_name='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='♨️ Heizwärmebedarf Flexibel', 
            var_cat=None
)
        self.QH_flex_winter = VariableMeta(
            var_name='QH_flex_winter', 
            attr_name='QH_flex_winter', 
            real_name='Heizwärmebedarf Flexibel', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QH_flexanteil_c = VariableMeta(
            var_name='QH_flexanteil_c', 
            attr_name='QH_flexanteil_c', 
            real_name='Flexibilitätsanteil', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='Flexibilitätsanteil', 
            var_cat=None
)
        self.QH_flexanteil_u = VariableMeta(
            var_name='QH_flexanteil_u', 
            attr_name='QH_flexanteil_u', 
            real_name='Flexibilitätsanteil', 
            unit='%', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='Flexibilitätsanteil', 
            var_cat=None
)
        self.QH_flexshare_summer = VariableMeta(
            var_name='QH_flexshare_summer', 
            attr_name='QH_flexshare_summer', 
            real_name='Anteil Flexibler Heizung an Gesamtheizung', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QH_flexshare_winter = VariableMeta(
            var_name='QH_flexshare_winter', 
            attr_name='QH_flexshare_winter', 
            real_name='Anteil Flexibler Heizung an Gesamtheizung', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QH_generation_eff_1el = VariableMeta(
            var_name='QH_generation_eff_1el', 
            attr_name='QH_generation_eff_1el', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung HZEL1', 
            unit=None, 
            type_name='calculation', 
            comment='weil schneller als divison durch Wirkugsgrad', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_generation_eff_2th = VariableMeta(
            var_name='QH_generation_eff_2th', 
            attr_name='QH_generation_eff_2th', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung HZTH2', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_generation_eff_3el = VariableMeta(
            var_name='QH_generation_eff_3el', 
            attr_name='QH_generation_eff_3el', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung HZEL3', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_generation_eff_4th = VariableMeta(
            var_name='QH_generation_eff_4th', 
            attr_name='QH_generation_eff_4th', 
            real_name='Wirkungsgrad-Kehrwert Erzeugung HZTH4', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QH_min_c = VariableMeta(
            var_name='QH_min_c', 
            attr_name='QH_min_c', 
            real_name='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='♨️ Heizwärmebedarf Statisch', 
            var_cat=None
)
        self.QH_min_summer = VariableMeta(
            var_name='QH_min_summer', 
            attr_name='QH_min_summer', 
            real_name='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QH_min_u = VariableMeta(
            var_name='QH_min_u', 
            attr_name='QH_min_u', 
            real_name='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='♨️ Heizwärmebedarf Statisch', 
            var_cat=None
)
        self.QH_min_winter = VariableMeta(
            var_name='QH_min_winter', 
            attr_name='QH_min_winter', 
            real_name='Heizwärmebedarf Statisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QH_summer = VariableMeta(
            var_name='QH_summer', 
            attr_name='QH_summer', 
            real_name='Heizwärmebedarf', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QH_u = VariableMeta(
            var_name='QH_u', 
            attr_name='QH_u', 
            real_name='Heizwärmebedarf', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='♨️ Heizwärmebedarf', 
            var_cat=None
)
        self.QH_winter = VariableMeta(
            var_name='QH_winter', 
            attr_name='QH_winter', 
            real_name='Heizwärmebedarf', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QHmax_1el_m2 = VariableMeta(
            var_name='QHmax_1el_m2', 
            attr_name='QHmax_1el_m2', 
            real_name='Thermische Leistung HZEL1', 
            unit='W/m²', 
            type_name='userinput', 
            comment='raumseitig, Elektrische Heizung PRIO1', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QHmax_2th_m2 = VariableMeta(
            var_name='QHmax_2th_m2', 
            attr_name='QHmax_2th_m2', 
            real_name='Thermische Leistung HZTH2', 
            unit='W/m²', 
            type_name='userinput', 
            comment='raumseitig, thermische Heizung PRIO 2', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QHmax_3el_m2 = VariableMeta(
            var_name='QHmax_3el_m2', 
            attr_name='QHmax_3el_m2', 
            real_name='Thermische Leistung HZEL3', 
            unit='W/m²', 
            type_name='userinput', 
            comment='raumseitig, Elektrisch, PRIO3', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QHmax_4th_m2 = VariableMeta(
            var_name='QHmax_4th_m2', 
            attr_name='QHmax_4th_m2', 
            real_name='Thermische Leistung HZTH4', 
            unit='W/m²', 
            type_name='userinput', 
            comment='raumseitig, thermisch PRIO4', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QHmax_room_MW = VariableMeta(
            var_name='QHmax_room_MW', 
            attr_name='QHmax_room_MW', 
            real_name='Thermische Leistung Abgabesystem', 
            unit='MW', 
            type_name='calculation', 
            comment='raumseitig', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QHmax_room_m = VariableMeta(
            var_name='QHmax_room_m²', 
            attr_name='QHmax_room_m', 
            real_name='spez. thermische Leistung Abgabesystem', 
            unit='W/m²', 
            type_name='userinput', 
            comment='raumseitig', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QI = VariableMeta(
            var_name='QI', 
            attr_name='QI', 
            real_name='Innere Wärmen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='👤 Innere Wärmen', 
            var_cat=None
)
        self.QI_c = VariableMeta(
            var_name='QI_c', 
            attr_name='QI_c', 
            real_name='Innere Wärmen', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='👤 Innere Wärmen', 
            var_cat=None
)
        self.QI_summer = VariableMeta(
            var_name='QI_summer', 
            attr_name='QI_summer', 
            real_name='Innere Wärmen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QI_u = VariableMeta(
            var_name='QI_u', 
            attr_name='QI_u', 
            real_name='Innere Wärmen', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='👤 Innere Wärmen', 
            var_cat=None
)
        self.QI_winter = VariableMeta(
            var_name='QI_winter', 
            attr_name='QI_winter', 
            real_name='Innere Wärmen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QS = VariableMeta(
            var_name='QS', 
            attr_name='QS', 
            real_name='Solare Gewinne', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='🌞 Solare Gewinne', 
            var_cat=None
)
        self.QS_c = VariableMeta(
            var_name='QS_c', 
            attr_name='QS_c', 
            real_name='Solare Gewinne', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🌞 Solare Gewinne', 
            var_cat=None
)
        self.QS_max_shading_c = VariableMeta(
            var_name='QS_max_shading_c', 
            attr_name='QS_max_shading_c', 
            real_name='Strahlungsschwellenwert Jalousie Gekühlt', 
            unit='W/m²', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QS_max_shading_u = VariableMeta(
            var_name='QS_max_shading_u', 
            attr_name='QS_max_shading_u', 
            real_name='Strahlungsschwellenwert Jalousie Ungekühlt', 
            unit='W/m²', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.QS_summer = VariableMeta(
            var_name='QS_summer', 
            attr_name='QS_summer', 
            real_name='Solare Gewinne', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QS_u = VariableMeta(
            var_name='QS_u', 
            attr_name='QS_u', 
            real_name='Solare Gewinne', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🌞 Solare Gewinne', 
            var_cat=None
)
        self.QS_winter = VariableMeta(
            var_name='QS_winter', 
            attr_name='QS_winter', 
            real_name='Solare Gewinne', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QT = VariableMeta(
            var_name='QT', 
            attr_name='QT', 
            real_name='Transmissionswärmeverl.', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='🧱 Transmissionswärmeverl.', 
            var_cat=None
)
        self.QT_c = VariableMeta(
            var_name='QT_c', 
            attr_name='QT_c', 
            real_name='Transmissionswärmeverl.', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🧱 Transmissionswärmeverl.', 
            var_cat=None
)
        self.QT_ground_c = VariableMeta(
            var_name='QT_ground_c', 
            attr_name='QT_ground_c', 
            real_name='Transmission KD/EFB', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🧱 Transmission KD/EFB', 
            var_cat=None
)
        self.QT_ground_summer = VariableMeta(
            var_name='QT_ground_summer', 
            attr_name='QT_ground_summer', 
            real_name='Transmission KD/EFB', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QT_ground_u = VariableMeta(
            var_name='QT_ground_u', 
            attr_name='QT_ground_u', 
            real_name='Transmission KD/EFB', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🧱 Transmission KD/EFB', 
            var_cat=None
)
        self.QT_ground_winter = VariableMeta(
            var_name='QT_ground_winter', 
            attr_name='QT_ground_winter', 
            real_name='Transmission KD/EFB', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QT_psi_c = VariableMeta(
            var_name='QT_psi_c', 
            attr_name='QT_psi_c', 
            real_name='Transmission Wärmebrücken', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🧱 Transmission Wärmebrücken', 
            var_cat=None
)
        self.QT_psi_summer = VariableMeta(
            var_name='QT_psi_summer', 
            attr_name='QT_psi_summer', 
            real_name='Transmission Wärmebrücken', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QT_psi_u = VariableMeta(
            var_name='QT_psi_u', 
            attr_name='QT_psi_u', 
            real_name='Transmission Wärmebrücken', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🧱 Transmission Wärmebrücken', 
            var_cat=None
)
        self.QT_psi_winter = VariableMeta(
            var_name='QT_psi_winter', 
            attr_name='QT_psi_winter', 
            real_name='Transmission Wärmebrücken', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QT_roof_c = VariableMeta(
            var_name='QT_roof_c', 
            attr_name='QT_roof_c', 
            real_name='Transmission Dach', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🧱 Transmission Dach', 
            var_cat=None
)
        self.QT_roof_summer = VariableMeta(
            var_name='QT_roof_summer', 
            attr_name='QT_roof_summer', 
            real_name='Transmission Dach', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QT_roof_u = VariableMeta(
            var_name='QT_roof_u', 
            attr_name='QT_roof_u', 
            real_name='Transmission Dach', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🧱 Transmission Dach', 
            var_cat=None
)
        self.QT_roof_winter = VariableMeta(
            var_name='QT_roof_winter', 
            attr_name='QT_roof_winter', 
            real_name='Transmission Dach', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QT_summer = VariableMeta(
            var_name='QT_summer', 
            attr_name='QT_summer', 
            real_name='Transmissionswärmeverl.', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QT_u = VariableMeta(
            var_name='QT_u', 
            attr_name='QT_u', 
            real_name='Transmissionswärmeverl.', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🧱 Transmissionswärmeverl.', 
            var_cat=None
)
        self.QT_wall_c = VariableMeta(
            var_name='QT_wall_c', 
            attr_name='QT_wall_c', 
            real_name='Transmission AW', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🧱 Transmission AW', 
            var_cat=None
)
        self.QT_wall_summer = VariableMeta(
            var_name='QT_wall_summer', 
            attr_name='QT_wall_summer', 
            real_name='Transmission AW', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QT_wall_u = VariableMeta(
            var_name='QT_wall_u', 
            attr_name='QT_wall_u', 
            real_name='Transmission AW', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🧱 Transmission AW', 
            var_cat=None
)
        self.QT_wall_winter = VariableMeta(
            var_name='QT_wall_winter', 
            attr_name='QT_wall_winter', 
            real_name='Transmission AW', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QT_window_c = VariableMeta(
            var_name='QT_window_c', 
            attr_name='QT_window_c', 
            real_name='Transmission Fenster', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🧱 Transmission Fenster', 
            var_cat=None
)
        self.QT_window_summer = VariableMeta(
            var_name='QT_window_summer', 
            attr_name='QT_window_summer', 
            real_name='Transmission Fenster', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QT_window_u = VariableMeta(
            var_name='QT_window_u', 
            attr_name='QT_window_u', 
            real_name='Transmission Fenster', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🧱 Transmission Fenster', 
            var_cat=None
)
        self.QT_window_winter = VariableMeta(
            var_name='QT_window_winter', 
            attr_name='QT_window_winter', 
            real_name='Transmission Fenster', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QT_winter = VariableMeta(
            var_name='QT_winter', 
            attr_name='QT_winter', 
            real_name='Transmissionswärmeverl.', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QV = VariableMeta(
            var_name='QV', 
            attr_name='QV', 
            real_name='Lüftungswärmeverluste', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='💨 Lüftungswärmeverluste', 
            var_cat=None
)
        self.QV_c = VariableMeta(
            var_name='QV_c', 
            attr_name='QV_c', 
            real_name='Lüftungswärmeverluste', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='💨 Lüftungswärmeverluste', 
            var_cat=None
)
        self.QV_heatrecovery = VariableMeta(
            var_name='QV_heatrecovery', 
            attr_name='QV_heatrecovery', 
            real_name='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.QV_heatrecovery_c = VariableMeta(
            var_name='QV_heatrecovery_c', 
            attr_name='QV_heatrecovery_c', 
            real_name='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🔀 ML Wärmerückgewinnung', 
            var_cat=None
)
        self.QV_heatrecovery_summer = VariableMeta(
            var_name='QV_heatrecovery_summer', 
            attr_name='QV_heatrecovery_summer', 
            real_name='ML Wärmerückgewinnung 2', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QV_heatrecovery_u = VariableMeta(
            var_name='QV_heatrecovery_u', 
            attr_name='QV_heatrecovery_u', 
            real_name='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🔀 ML Wärmerückgewinnung', 
            var_cat=None
)
        self.QV_heatrecovery_winter = VariableMeta(
            var_name='QV_heatrecovery_winter', 
            attr_name='QV_heatrecovery_winter', 
            real_name='ML Wärmerückgewinnung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QV_inf_c = VariableMeta(
            var_name='QV_inf_c', 
            attr_name='QV_inf_c', 
            real_name='Infiltration', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='💨 Infiltration', 
            var_cat=None
)
        self.QV_inf_summer = VariableMeta(
            var_name='QV_inf_summer', 
            attr_name='QV_inf_summer', 
            real_name='Infiltration', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QV_inf_u = VariableMeta(
            var_name='QV_inf_u', 
            attr_name='QV_inf_u', 
            real_name='Infiltration', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='💨 Infiltration', 
            var_cat=None
)
        self.QV_inf_winter = VariableMeta(
            var_name='QV_inf_winter', 
            attr_name='QV_inf_winter', 
            real_name='Infiltration', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QV_mechvent_c = VariableMeta(
            var_name='QV_mechvent_c', 
            attr_name='QV_mechvent_c', 
            real_name='Mechanische Lüftung', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='💨 Mechanische Lüftung', 
            var_cat=None
)
        self.QV_mechvent_summer = VariableMeta(
            var_name='QV_mechvent_summer', 
            attr_name='QV_mechvent_summer', 
            real_name='Mechanische Lüftung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QV_mechvent_u = VariableMeta(
            var_name='QV_mechvent_u', 
            attr_name='QV_mechvent_u', 
            real_name='Mechanische Lüftung', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='💨 Mechanische Lüftung', 
            var_cat=None
)
        self.QV_mechvent_winter = VariableMeta(
            var_name='QV_mechvent_winter', 
            attr_name='QV_mechvent_winter', 
            real_name='Mechanische Lüftung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QV_summer = VariableMeta(
            var_name='QV_summer', 
            attr_name='QV_summer', 
            real_name='Lüftungswärmeverluste', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QV_u = VariableMeta(
            var_name='QV_u', 
            attr_name='QV_u', 
            real_name='Lüftungswärmeverluste', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='💨 Lüftungswärmeverluste', 
            var_cat=None
)
        self.QV_window_c = VariableMeta(
            var_name='QV_window_c', 
            attr_name='QV_window_c', 
            real_name='Lüftung Fenster', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='💨 Lüftung Fenster', 
            var_cat=None
)
        self.QV_window_summer = VariableMeta(
            var_name='QV_window_summer', 
            attr_name='QV_window_summer', 
            real_name='Lüftung Fenster', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QV_window_u = VariableMeta(
            var_name='QV_window_u', 
            attr_name='QV_window_u', 
            real_name='Lüftung Fenster', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='💨 Lüftung Fenster', 
            var_cat=None
)
        self.QV_window_winter = VariableMeta(
            var_name='QV_window_winter', 
            attr_name='QV_window_winter', 
            real_name='Lüftung Fenster', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QV_winter = VariableMeta(
            var_name='QV_winter', 
            attr_name='QV_winter', 
            real_name='Lüftungswärmeverluste', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.QVn = VariableMeta(
            var_name='QVn', 
            attr_name='QVn', 
            real_name='Nachtlüftung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Quartier', 
            label='🌒 Nachtlüftung', 
            var_cat=None
)
        self.QVn_c = VariableMeta(
            var_name='QVn_c', 
            attr_name='QVn_c', 
            real_name='Nachtlüftung gekühlt', 
            unit='kWh/m²NGFgekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Gekühlt', 
            label='🌒 Nachtlüftung', 
            var_cat=None
)
        self.QVn_summer = VariableMeta(
            var_name='QVn_summer', 
            attr_name='QVn_summer', 
            real_name='Nachtlüftung gekühlt', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Kühlperiode', 
            label=None, 
            var_cat=None
)
        self.QVn_u = VariableMeta(
            var_name='QVn_u', 
            attr_name='QVn_u', 
            real_name='Nachtlüftung', 
            unit='kWh/m²NGFungekühlta', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Ungekühlt', 
            label='🌒 Nachtlüftung', 
            var_cat=None
)
        self.QVn_winter = VariableMeta(
            var_name='QVn_winter', 
            attr_name='QVn_winter', 
            real_name='Nachtlüftung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area='Heizperiode', 
            label=None, 
            var_cat=None
)
        self.StatPAX = VariableMeta(
            var_name='StatPAX', 
            attr_name='StatPAX', 
            real_name='Quartier', 
            unit='StatPAX', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.StatPAX_eduprim = VariableMeta(
            var_name='StatPAX_eduprim', 
            attr_name='StatPAX_eduprim', 
            real_name='Mobilitätsstatistische Nutzer Schule primär', 
            unit='StatPAX', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.StatPAX_edusec = VariableMeta(
            var_name='StatPAX_edusec', 
            attr_name='StatPAX_edusec', 
            real_name='Mobilitätsstatistische Nutzer Schule sekundär', 
            unit='StatPAX', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.StatPAX_office = VariableMeta(
            var_name='StatPAX_office', 
            attr_name='StatPAX_office', 
            real_name='Mobilitätsstatistische Nutzer Büro', 
            unit='StatPAX', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.StatPAX_res = VariableMeta(
            var_name='StatPAX_res', 
            attr_name='StatPAX_res', 
            real_name='Mobilitätsstatistische Nutzer Wohnen', 
            unit='StatPAX', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.StatPAX_retail = VariableMeta(
            var_name='StatPAX_retail', 
            attr_name='StatPAX_retail', 
            real_name='Mobilitätsstatistische Nutzer Handel Supermarkt', 
            unit='StatPAX', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.StatPAX_retailother = VariableMeta(
            var_name='StatPAX_retailother', 
            attr_name='StatPAX_retailother', 
            real_name='Mobilitätsstatistische Nutzer Handel Sonstige', 
            unit='StatPAX', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ta_annual_avg = VariableMeta(
            var_name='Ta_annual_avg', 
            attr_name='Ta_annual_avg', 
            real_name='Außentemperatur Jahresmittel', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wetter', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ta_avg_cooling_period = VariableMeta(
            var_name='Ta_avg_cooling_period', 
            attr_name='Ta_avg_cooling_period', 
            real_name='Mittelaußentemperatur Kühlperiode', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wetter', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Ta_avg_heating_period = VariableMeta(
            var_name='Ta_avg_heating_period', 
            attr_name='Ta_avg_heating_period', 
            real_name='Mittelaußentemperatur Heizperiode', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wetter', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tc_avg_summer = VariableMeta(
            var_name='Tc_avg_summer', 
            attr_name='Tc_avg_summer', 
            real_name='Mitteltemperatur gekühlt', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tc_avg_winter = VariableMeta(
            var_name='Tc_avg_winter', 
            attr_name='Tc_avg_winter', 
            real_name='Mitteltemperatur gekühlt', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tsetcool_flex = VariableMeta(
            var_name='Tsetcool_flex', 
            attr_name='Tsetcool_flex', 
            real_name='Flexibles Kühlen Minimale Raumtemperatur', 
            unit=None, 
            type_name='calculation', 
            comment='°C', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tsetcool_max = VariableMeta(
            var_name='Tsetcool_max', 
            attr_name='Tsetcool_max', 
            real_name='Kühlen Solltemperatur Maximum', 
            unit='°C', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tsetheat_flex = VariableMeta(
            var_name='Tsetheat_flex', 
            attr_name='Tsetheat_flex', 
            real_name='Flexibles Heizen Maximale Raumtemperatur', 
            unit=None, 
            type_name='calculation', 
            comment='°C', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tsetheat_min = VariableMeta(
            var_name='Tsetheat_min', 
            attr_name='Tsetheat_min', 
            real_name='Heizen Raumtemperatur Minimum', 
            unit='°C', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tu_avg_summer = VariableMeta(
            var_name='Tu_avg_summer', 
            attr_name='Tu_avg_summer', 
            real_name='Mitteltemperatur ungekühlt', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Tu_avg_winter = VariableMeta(
            var_name='Tu_avg_winter', 
            attr_name='Tu_avg_winter', 
            real_name='Mitteltemperatur ungekühlt', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.UED_auxiliary = VariableMeta(
            var_name='UED_auxiliary', 
            attr_name='UED_auxiliary', 
            real_name='Allgemeinstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_cooling = VariableMeta(
            var_name='UED_cooling', 
            attr_name='UED_cooling', 
            real_name='Külenergiebedarf', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_dhw = VariableMeta(
            var_name='UED_dhw', 
            attr_name='UED_dhw', 
            real_name='WWWB', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_heating = VariableMeta(
            var_name='UED_heating', 
            attr_name='UED_heating', 
            real_name='Heiwärmebedarf', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_lighting = VariableMeta(
            var_name='UED_lighting', 
            attr_name='UED_lighting', 
            real_name='Beleuchtung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_mim_electric = VariableMeta(
            var_name='UED_mim_electric', 
            attr_name='UED_mim_electric', 
            real_name='E-Mobilität', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_mim_fossile = VariableMeta(
            var_name='UED_mim_fossile', 
            attr_name='UED_mim_fossile', 
            real_name='Fossile Mobilität', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_mob_el_other = VariableMeta(
            var_name='UED_mob_el_other', 
            attr_name='UED_mob_el_other', 
            real_name='Quell- und anderer Verkehr elektrisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.UED_mob_el_target = VariableMeta(
            var_name='UED_mob_el_target', 
            attr_name='UED_mob_el_target', 
            real_name='EE-Bedarf Zielverkehr Elektrisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.UED_mob_el_total = VariableMeta(
            var_name='UED_mob_el_total', 
            attr_name='UED_mob_el_total', 
            real_name='Gesamtverkehr elektrisch', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.UED_plugloads = VariableMeta(
            var_name='UED_plugloads', 
            attr_name='UED_plugloads', 
            real_name='Nutzerstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.UED_ventilation = VariableMeta(
            var_name='UED_ventilation', 
            attr_name='UED_ventilation', 
            real_name='Lüftungsenergiebedarf', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Nutzenergiebedarfe', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Batt = VariableMeta(
            var_name='VRGrid_to_Batt', 
            attr_name='VRGrid_to_Batt', 
            real_name='Flexible Überdeckung → Batterie', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='e-Speicher Beladung', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Ec_flex = VariableMeta(
            var_name='VRGrid_to_Ec_flex', 
            attr_name='VRGrid_to_Ec_flex', 
            real_name='Flexible Überdeckung → Kühlen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Ec_min = VariableMeta(
            var_name='VRGrid_to_Ec_min', 
            attr_name='VRGrid_to_Ec_min', 
            real_name='Flexible Direktdeckung → Kühlen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Kühlen', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Edhw_flex = VariableMeta(
            var_name='VRGrid_to_Edhw_flex', 
            attr_name='VRGrid_to_Edhw_flex', 
            real_name='Flexible Überdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Edhw_min = VariableMeta(
            var_name='VRGrid_to_Edhw_min', 
            attr_name='VRGrid_to_Edhw_min', 
            real_name='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Warmwasser', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Eev_flex = VariableMeta(
            var_name='VRGrid_to_Eev_flex', 
            attr_name='VRGrid_to_Eev_flex', 
            real_name='Flexible Überdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='MIV', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Eev_min = VariableMeta(
            var_name='VRGrid_to_Eev_min', 
            attr_name='VRGrid_to_Eev_min', 
            real_name='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='MIV', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Eh_flex = VariableMeta(
            var_name='VRGrid_to_Eh_flex', 
            attr_name='VRGrid_to_Eh_flex', 
            real_name='Flexible Überdeckung → Heizen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Eh_min = VariableMeta(
            var_name='VRGrid_to_Eh_min', 
            attr_name='VRGrid_to_Eh_min', 
            real_name='Flexible Direktdeckung → Heizen', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Heizen', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_Ev_min = VariableMeta(
            var_name='VRGrid_to_Ev_min', 
            attr_name='VRGrid_to_Ev_min', 
            real_name='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Lüftung', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_building = VariableMeta(
            var_name='VRGrid_to_building', 
            attr_name='VRGrid_to_building', 
            real_name='Flexible Deckung → Gebäude', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Gebäude', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_flex = VariableMeta(
            var_name='VRGrid_to_flex', 
            attr_name='VRGrid_to_flex', 
            real_name='Flexible Überdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_min = VariableMeta(
            var_name='VRGrid_to_min', 
            attr_name='VRGrid_to_min', 
            real_name='Flexible Direktdeckung', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Quartier', 
            label=None, 
            var_cat=None
)
        self.VRGrid_to_plugloads = VariableMeta(
            var_name='VRGrid_to_plugloads', 
            attr_name='VRGrid_to_plugloads', 
            real_name='Flexible Direktdeckung → Nutzerstrom', 
            unit='kWh/m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='EE-Bilanz', 
            area='Haushaltsstrom', 
            label=None, 
            var_cat=None
)
        self.Vent_share_mech_cooled = VariableMeta(
            var_name='Vent_share_mech_cooled', 
            attr_name='Vent_share_mech_cooled', 
            real_name='Quartiersanteil Mechanische Lüftung mit aktiver Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Vent_share_mech_uncooled = VariableMeta(
            var_name='Vent_share_mech_uncooled', 
            attr_name='Vent_share_mech_uncooled', 
            real_name='Quartiersanteil Mechanische Lüftung ohne aktiver Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Vent_share_window_cooled = VariableMeta(
            var_name='Vent_share_window_cooled', 
            attr_name='Vent_share_window_cooled', 
            real_name='Fensterlüftung Anteil mit aktiver Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.Vent_share_window_uncooled = VariableMeta(
            var_name='Vent_share_window_uncooled', 
            attr_name='Vent_share_window_uncooled', 
            real_name='Fensterlüftung Anteil ohne aktive Kühlung', 
            unit=None, 
            type_name='calculation', 
            comment='pro Quartiersvolumen!', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_office_kWhm2 = VariableMeta(
            var_name='aux_el_demand_office_kWhm2', 
            attr_name='aux_el_demand_office_kWhm2', 
            real_name='Allgemeinstrom Büro', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_other_kWhm2 = VariableMeta(
            var_name='aux_el_demand_other_kWhm2', 
            attr_name='aux_el_demand_other_kWhm2', 
            real_name='Allgemeinstrom Sonstige Nutzung', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_residential_kWhm2 = VariableMeta(
            var_name='aux_el_demand_residential_kWhm2', 
            attr_name='aux_el_demand_residential_kWhm2', 
            real_name='Allgemeinstrom Wohnen', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_retailfood_kWhm2 = VariableMeta(
            var_name='aux_el_demand_retailfood_kWhm2', 
            attr_name='aux_el_demand_retailfood_kWhm2', 
            real_name='Allgemeinstrom Handel lebensmittel', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_retailother_kWhm2 = VariableMeta(
            var_name='aux_el_demand_retailother_kWhm2', 
            attr_name='aux_el_demand_retailother_kWhm2', 
            real_name='Allgemeinstrom Handel sonstiger', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_schoolprim_kWhm2 = VariableMeta(
            var_name='aux_el_demand_schoolprim_kWhm2', 
            attr_name='aux_el_demand_schoolprim_kWhm2', 
            real_name='Allgemeinstrom Bildung primär', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.aux_el_demand_schoolsec_kWhm2 = VariableMeta(
            var_name='aux_el_demand_schoolsec_kWhm2', 
            attr_name='aux_el_demand_schoolsec_kWhm2', 
            real_name='Allgemeinstrom Bildung sekundär', 
            unit='kWh/m²NGFa', 
            type_name='userinput', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.borehole_count = VariableMeta(
            var_name='borehole_count', 
            attr_name='borehole_count', 
            real_name='Anzahl Erdsonden', 
            unit='Stk Erdsonden', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.building_count = VariableMeta(
            var_name='building_count', 
            attr_name='building_count', 
            real_name='Anzahl Baukörper', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfd_A = VariableMeta(
            var_name='cfd_A', 
            attr_name='cfd_A', 
            real_name='Ausnutzungsfaktor Erneuerbare', 
            unit='kWhEE/m²GF', 
            type_name='value', 
            comment='A', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfd_EUI = VariableMeta(
            var_name='cfd_EUI', 
            attr_name='cfd_EUI', 
            real_name='Energieintensität Bedarf', 
            unit='kWhEE/m²NGFa', 
            type_name='value', 
            comment='EUI', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfd_cutoff = VariableMeta(
            var_name='cfd_cutoff', 
            attr_name='cfd_cutoff', 
            real_name='Maximum', 
            unit='kWhPE/m²NGFa', 
            type_name='value', 
            comment='cutoff', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfd_dx = VariableMeta(
            var_name='cfd_dx', 
            attr_name='cfd_dx', 
            real_name='Skalierungsfaktor', 
            unit='-', 
            type_name='value', 
            comment='dx', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfd_fPE = VariableMeta(
            var_name='cfd_fPE', 
            attr_name='cfd_fPE', 
            real_name='Primärenergiefaktor', 
            unit='kWhPE/kWhEE', 
            type_name='value', 
            comment='f_PE', 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfm_budget_office = VariableMeta(
            var_name='cfm_budget_office', 
            attr_name='cfm_budget_office', 
            real_name='Mobilitätsbudget Büro', 
            unit='kWhPE/m²NGFa', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfm_budget_residential = VariableMeta(
            var_name='cfm_budget_residential', 
            attr_name='cfm_budget_residential', 
            real_name='Mobilitätsbudget Wohnen', 
            unit='kWhPE/m²NGFa', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfm_budget_retail = VariableMeta(
            var_name='cfm_budget_retail', 
            attr_name='cfm_budget_retail', 
            real_name='Mobilitätsbudget Handel + Sonstige', 
            unit='kWhPE/m²NGFa', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfm_budget_school = VariableMeta(
            var_name='cfm_budget_school', 
            attr_name='cfm_budget_school', 
            real_name='Mobilitätsbudget Ausbildung', 
            unit='kWhPE/m²NGFa', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cfr_budget = VariableMeta(
            var_name='cfr_budget', 
            attr_name='cfr_budget', 
            real_name='Kontextfaktor Sanierung', 
            unit='kWhPE/m²NGFa', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.context_factor_density = VariableMeta(
            var_name='context_factor_density', 
            attr_name='context_factor_density', 
            real_name='Kontextfaktor bauliche Dichte', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.context_factor_mobility = VariableMeta(
            var_name='context_factor_mobility', 
            attr_name='context_factor_mobility', 
            real_name='Kontextfaktor Mobilität', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.context_factor_renovation = VariableMeta(
            var_name='context_factor_renovation', 
            attr_name='context_factor_renovation', 
            real_name='Kontextfaktor Sanierung', 
            unit='kWhPEges./m²NGFa', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='PE-Bilanz', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_cop_1el = VariableMeta(
            var_name='cool_cop_1el', 
            attr_name='cool_cop_1el', 
            real_name='Wirkungsgrad Erzeugung 1 El', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_cop_2th = VariableMeta(
            var_name='cool_cop_2th', 
            attr_name='cool_cop_2th', 
            real_name='Wirkungsgrad Erzeugung 2 TH', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_cop_3el = VariableMeta(
            var_name='cool_cop_3el', 
            attr_name='cool_cop_3el', 
            real_name='Wirkungsgrad Erzeugung 3 EL', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_office = VariableMeta(
            var_name='cool_share_office', 
            attr_name='cool_share_office', 
            real_name='Aktive Kühlung Anteil Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_other = VariableMeta(
            var_name='cool_share_other', 
            attr_name='cool_share_other', 
            real_name='Aktive Kühlung Anteil Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_residential = VariableMeta(
            var_name='cool_share_residential', 
            attr_name='cool_share_residential', 
            real_name='Aktive Kühlung Anteil Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_retailfood = VariableMeta(
            var_name='cool_share_retailfood', 
            attr_name='cool_share_retailfood', 
            real_name='Aktive Kühlung Anteil Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_retailother = VariableMeta(
            var_name='cool_share_retailother', 
            attr_name='cool_share_retailother', 
            real_name='Aktive Kühlung Anteil Handel Sonstige', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_schoolprim = VariableMeta(
            var_name='cool_share_schoolprim', 
            attr_name='cool_share_schoolprim', 
            real_name='Aktive Kühlung Anteil Schule primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_share_schoolsec = VariableMeta(
            var_name='cool_share_schoolsec', 
            attr_name='cool_share_schoolsec', 
            real_name='Aktive Kühlung Anteil Schule sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_th2_carrier_type = VariableMeta(
            var_name='cool_th2_carrier_type', 
            attr_name='cool_th2_carrier_type', 
            real_name='Energieträger System 2 Thermisch', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_th2_is_bio = VariableMeta(
            var_name='cool_th2_is_bio', 
            attr_name='cool_th2_is_bio', 
            real_name='PE Kühlen 2 ist Biomasse', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_th2_is_dh = VariableMeta(
            var_name='cool_th2_is_dh', 
            attr_name='cool_th2_is_dh', 
            real_name='PE Kühlen 2 ist Fernwärme', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_th2_is_ng = VariableMeta(
            var_name='cool_th2_is_ng', 
            attr_name='cool_th2_is_ng', 
            real_name='PE Kühlen 2 ist Erdgas', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cool_th2_is_other = VariableMeta(
            var_name='cool_th2_is_other', 
            attr_name='cool_th2_is_other', 
            real_name='PE Kühlen 2 ist Sonstige', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month1 = VariableMeta(
            var_name='cooling_month1', 
            attr_name='cooling_month1', 
            real_name='Kühlperiode Jänner', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month10 = VariableMeta(
            var_name='cooling_month10', 
            attr_name='cooling_month10', 
            real_name='Kühlperiode Oktober', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month11 = VariableMeta(
            var_name='cooling_month11', 
            attr_name='cooling_month11', 
            real_name='Kühlperiode November', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month12 = VariableMeta(
            var_name='cooling_month12', 
            attr_name='cooling_month12', 
            real_name='Kühlperiode Dezember', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month2 = VariableMeta(
            var_name='cooling_month2', 
            attr_name='cooling_month2', 
            real_name='Kühlperiode Februar', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month3 = VariableMeta(
            var_name='cooling_month3', 
            attr_name='cooling_month3', 
            real_name='Kühlperiode März', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month4 = VariableMeta(
            var_name='cooling_month4', 
            attr_name='cooling_month4', 
            real_name='Kühlperiode April', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month5 = VariableMeta(
            var_name='cooling_month5', 
            attr_name='cooling_month5', 
            real_name='Kühlperiode Mai', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month6 = VariableMeta(
            var_name='cooling_month6', 
            attr_name='cooling_month6', 
            real_name='Kühlperiode Juni', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month7 = VariableMeta(
            var_name='cooling_month7', 
            attr_name='cooling_month7', 
            real_name='Kühlperiode Juli', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month8 = VariableMeta(
            var_name='cooling_month8', 
            attr_name='cooling_month8', 
            real_name='Kühlperiode August', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cooling_month9 = VariableMeta(
            var_name='cooling_month9', 
            attr_name='cooling_month9', 
            real_name='Kühlperiode September', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cost_E_grid = VariableMeta(
            var_name='cost_E_grid', 
            attr_name='cost_E_grid', 
            real_name='Kosten Netzbezug', 
            unit='€', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Stromkosten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cost_PV_to_Egrid = VariableMeta(
            var_name='cost_PV_to_Egrid', 
            attr_name='cost_PV_to_Egrid', 
            real_name='Kosten Netzeinspeisung', 
            unit='€', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Stromkosten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cost_VRGrid_flex = VariableMeta(
            var_name='cost_VRGrid_flex', 
            attr_name='cost_VRGrid_flex', 
            real_name='Kosten Flexibler Bezug', 
            unit='€', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Stromkosten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.cost_total = VariableMeta(
            var_name='cost_total', 
            attr_name='cost_total', 
            real_name='Summe Kosten', 
            unit='€', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Stromkosten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dTc_summer = VariableMeta(
            var_name='dTc_summer', 
            attr_name='dTc_summer', 
            real_name='Mittlere Temperaturunterschreitung gekühlt', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dTc_winter = VariableMeta(
            var_name='dTc_winter', 
            attr_name='dTc_winter', 
            real_name='Mittlere Temperaturüberschreitung gekühlt', 
            unit='K', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dTu_summer = VariableMeta(
            var_name='dTu_summer', 
            attr_name='dTu_summer', 
            real_name='Mittlere Temperaturunterschreitung ungekühlt', 
            unit='°C', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dTu_winter = VariableMeta(
            var_name='dTu_winter', 
            attr_name='dTu_winter', 
            real_name='Mittlere Temperaturüberschreitung ungekühlt', 
            unit='K', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Komfort', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.daylightcontr_office = VariableMeta(
            var_name='daylightcontr_office', 
            attr_name='daylightcontr_office', 
            real_name='Anteil Tageslichtgesteuert Büro', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.daylightcontr_schoolprim = VariableMeta(
            var_name='daylightcontr_schoolprim', 
            attr_name='daylightcontr_schoolprim', 
            real_name='Anteil Tageslichtgesteuert Ausbildung Primär', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.daylightcontr_schoolsec = VariableMeta(
            var_name='daylightcontr_schoolsec', 
            attr_name='daylightcontr_schoolsec', 
            real_name='Anteil Tageslichtgesteuert Ausbildung Sekundär', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.density_NFApPers_edu = VariableMeta(
            var_name='density_NFApPers_edu', 
            attr_name='density_NFApPers_edu', 
            real_name='Belegungsdichte Ausbildung Sekundär', 
            unit='m²NF/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.density_NFApPers_edu_rpim = VariableMeta(
            var_name='density_NFApPers_edu_rpim', 
            attr_name='density_NFApPers_edu_rpim', 
            real_name='Belegungsdichte Ausbildung Primär', 
            unit='m²NF/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.density_NFApPers_office = VariableMeta(
            var_name='density_NFApPers_office', 
            attr_name='density_NFApPers_office', 
            real_name='Belegungsdichte Büro', 
            unit='m²NF/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.density_NFApPers_residential = VariableMeta(
            var_name='density_NFApPers_residential', 
            attr_name='density_NFApPers_residential', 
            real_name='Belegungsdichte Wohnen', 
            unit='m²NF/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.density_NFApPers_retail = VariableMeta(
            var_name='density_NFApPers_retail', 
            attr_name='density_NFApPers_retail', 
            real_name='Belegungsdichte Handel Supermarkt', 
            unit='m²NF/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.density_NFApPers_retail_other = VariableMeta(
            var_name='density_NFApPers_retail_other', 
            attr_name='density_NFApPers_retail_other', 
            real_name='Belegungsdichte Handel Sonstige', 
            unit='m²NF/Pers', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw1_is_bio = VariableMeta(
            var_name='dhw1_is_bio', 
            attr_name='dhw1_is_bio', 
            real_name='PE WWWB 1 ist Biomasse', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw1_is_dh = VariableMeta(
            var_name='dhw1_is_dh', 
            attr_name='dhw1_is_dh', 
            real_name='PE WWWB 1 ist Fernwärme', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw1_is_ng = VariableMeta(
            var_name='dhw1_is_ng', 
            attr_name='dhw1_is_ng', 
            real_name='PE WWWB 1 ist Erdgas', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw1_is_other = VariableMeta(
            var_name='dhw1_is_other', 
            attr_name='dhw1_is_other', 
            real_name='PE WWWB 1 ist Sonstige', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw2_is_bio = VariableMeta(
            var_name='dhw2_is_bio', 
            attr_name='dhw2_is_bio', 
            real_name='PE WWWB 2 ist Biomasse', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw2_is_dh = VariableMeta(
            var_name='dhw2_is_dh', 
            attr_name='dhw2_is_dh', 
            real_name='PE WWWB 2 ist Fernwärme', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw2_is_ng = VariableMeta(
            var_name='dhw2_is_ng', 
            attr_name='dhw2_is_ng', 
            real_name='PE WWWB 2 ist Erdgas', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.dhw2_is_other = VariableMeta(
            var_name='dhw2_is_other', 
            attr_name='dhw2_is_other', 
            real_name='PE WWWB 2 ist Sonstige', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.district_heating_conversion_profile = VariableMeta(
            var_name='district_heating_conversion_profile', 
            attr_name='district_heating_conversion_profile', 
            real_name='Fernwärme Konversionsprofil', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.e_kWhm2a = VariableMeta(
            var_name='e_kWhm2a', 
            attr_name='e_kWhm2a', 
            real_name='Test precision kWhm2NFAa', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.ev_bidirectional_use = VariableMeta(
            var_name='ev_bidirectional_use', 
            attr_name='ev_bidirectional_use', 
            real_name='Bidirektionales Laden', 
            unit=None, 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fGHG_grid_column = VariableMeta(
            var_name='fGHG_grid_column', 
            attr_name='fGHG_grid_column', 
            real_name='Strom Konversionsprofil ID THG', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fGHG_grid_profile = VariableMeta(
            var_name='fGHG_grid_profile', 
            attr_name='fGHG_grid_profile', 
            real_name='Strom Konversionsprofil THG', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fPE_eff = VariableMeta(
            var_name='fPE_eff', 
            attr_name='fPE_eff', 
            real_name='PE Faktor Netzstrom Effektiv', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fPE_flex_factor = VariableMeta(
            var_name='fPE_flex_factor', 
            attr_name='fPE_flex_factor', 
            real_name='Flexibler Netzbezug Anteil PE-Faktor', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fPE_grid = VariableMeta(
            var_name='fPE_grid', 
            attr_name='fPE_grid', 
            real_name='PE Faktor Netzstrom Statistisch', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fPE_grid_column = VariableMeta(
            var_name='fPE_grid_column', 
            attr_name='fPE_grid_column', 
            real_name='Strom Konversionsprofil ID PE', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fPE_grid_profile = VariableMeta(
            var_name='fPE_grid_profile', 
            attr_name='fPE_grid_profile', 
            real_name='Strom Konversionsprofil PE', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_c = VariableMeta(
            var_name='fc_c', 
            attr_name='fc_c', 
            real_name='Fc-Wert gekühlt', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_eduprim = VariableMeta(
            var_name='fc_eduprim', 
            attr_name='fc_eduprim', 
            real_name='Fc-Wert Kindergarten und Volksschule', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_edusec = VariableMeta(
            var_name='fc_edusec', 
            attr_name='fc_edusec', 
            real_name='Fc-Wert Sekundäre Bildungseinrichtung oder Universität', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_office = VariableMeta(
            var_name='fc_office', 
            attr_name='fc_office', 
            real_name='Fc-Wert Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_other = VariableMeta(
            var_name='fc_other', 
            attr_name='fc_other', 
            real_name='Fc-Wert Sonstige', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_residential = VariableMeta(
            var_name='fc_residential', 
            attr_name='fc_residential', 
            real_name='Fc-Wert Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_retailfood = VariableMeta(
            var_name='fc_retailfood', 
            attr_name='fc_retailfood', 
            real_name='Fc-Wert Lebensmittelhandel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_retailother = VariableMeta(
            var_name='fc_retailother', 
            attr_name='fc_retailother', 
            real_name='Fc-Wert Handel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fc_u = VariableMeta(
            var_name='fc_u', 
            attr_name='fc_u', 
            real_name='Fc-Wert ungekühlt', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_GSR = VariableMeta(
            var_name='flex_GSR', 
            attr_name='flex_GSR', 
            real_name='Flex GSR', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Netzdienlichkeit der Energieflexibilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_GSRI = VariableMeta(
            var_name='flex_GSRI', 
            attr_name='flex_GSRI', 
            real_name='Flex GSRI', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Netzdienlichkeit der Energieflexibilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_GSRU = VariableMeta(
            var_name='flex_GSRU', 
            attr_name='flex_GSRU', 
            real_name='Flex GSRU', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Netzdienlichkeit der Energieflexibilität', 
            area=None, 
            label='"Zufällige Netzdienlichkeit, Deckung Mindestbedarfe"', 
            var_cat=None
)
        self.flex_Signals_selected_column = VariableMeta(
            var_name='flex_Signals_selected_column', 
            attr_name='flex_Signals_selected_column', 
            real_name='Flex Signal Table', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_cool_dT = VariableMeta(
            var_name='flex_cool_dT', 
            attr_name='flex_cool_dT', 
            real_name='Flexibles Kühlen unter Solltemperatur', 
            unit=None, 
            type_name='userinput', 
            comment='Kelvin', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_dhw_use = VariableMeta(
            var_name='flex_dhw_use', 
            attr_name='flex_dhw_use', 
            real_name='Flexible WW-Speicherbeladung', 
            unit='bool', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_heat_dT = VariableMeta(
            var_name='flex_heat_dT', 
            attr_name='flex_heat_dT', 
            real_name='Flexibles Heizen über Solltemperatur', 
            unit=None, 
            type_name='userinput', 
            comment='Kelvin', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_signal_ratio = VariableMeta(
            var_name='flex_signal_ratio', 
            attr_name='flex_signal_ratio', 
            real_name='Freigabesignal Anteil Jahr', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Netzdienlichkeit der Energieflexibilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_signal_ratio_summer = VariableMeta(
            var_name='flex_signal_ratio_summer', 
            attr_name='flex_signal_ratio_summer', 
            real_name='Freigabesignal Anteil  Sommer', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Netzdienlichkeit der Energieflexibilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.flex_signal_ratio_winter = VariableMeta(
            var_name='flex_signal_ratio_winter', 
            attr_name='flex_signal_ratio_winter', 
            real_name='Freigabesignal Anteil  Winter', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Netzdienlichkeit der Energieflexibilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.fossile_demand_kWhpkm = VariableMeta(
            var_name='fossile_demand_kWhpkm', 
            attr_name='fossile_demand_kWhpkm', 
            real_name='Fossiler Energieverbrauch', 
            unit='kWh/km', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.grid_rcp1 = VariableMeta(
            var_name='grid_rcp1', 
            attr_name='grid_rcp1', 
            real_name='Absenkfaktor 1 Netzstrom', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.grid_rcp2 = VariableMeta(
            var_name='grid_rcp2', 
            attr_name='grid_rcp2', 
            real_name='Absenkfaktor 2 Netzstrom', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.grid_rcp3 = VariableMeta(
            var_name='grid_rcp3', 
            attr_name='grid_rcp3', 
            real_name='Absenkfaktor 3 Netzstrom', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_cap_eff_cooled_m2 = VariableMeta(
            var_name='heat_cap_eff_cooled_m2', 
            attr_name='heat_cap_eff_cooled_m2', 
            real_name='Spezif. wirksame Wärmekapazität gekühlter Bereich', 
            unit='Wh/m²K', 
            type_name='calculation', 
            comment='Kann separat eingegebn werden', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_cap_eff_uncooled_m2 = VariableMeta(
            var_name='heat_cap_eff_uncooled_m2', 
            attr_name='heat_cap_eff_uncooled_m2', 
            real_name='Spezif. wirksame Wärmekapazität ungekühlter Bereich', 
            unit='Wh/m²K', 
            type_name='calculation', 
            comment='Kann separat eingegebn werden', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_capacity_effective_m = VariableMeta(
            var_name='heat_capacity_effective_m²', 
            attr_name='heat_capacity_effective_m', 
            real_name='Spezif. wirksame Wärmekapazität', 
            unit='Wh/m²K', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_cop_1el = VariableMeta(
            var_name='heat_cop_1el', 
            attr_name='heat_cop_1el', 
            real_name='Wirkungsgrad Erzeugung HZEL1', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_cop_2th = VariableMeta(
            var_name='heat_cop_2th', 
            attr_name='heat_cop_2th', 
            real_name='Wirkungsgrad Erzeugung HZTH2', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_cop_3el = VariableMeta(
            var_name='heat_cop_3el', 
            attr_name='heat_cop_3el', 
            real_name='Wirkungsgrad Erzeugung HZEL3', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_cop_4th = VariableMeta(
            var_name='heat_cop_4th', 
            attr_name='heat_cop_4th', 
            real_name='Wirkungsgrad Erzeugung HZTH4', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th2_carrier_type = VariableMeta(
            var_name='heat_th2_carrier_type', 
            attr_name='heat_th2_carrier_type', 
            real_name='Energieträger HZTH2', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th2_is_bio = VariableMeta(
            var_name='heat_th2_is_bio', 
            attr_name='heat_th2_is_bio', 
            real_name='PE Heizen 2 ist Biomasse', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th2_is_dh = VariableMeta(
            var_name='heat_th2_is_dh', 
            attr_name='heat_th2_is_dh', 
            real_name='PE Heizen 2 ist Fernwärme', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th2_is_ng = VariableMeta(
            var_name='heat_th2_is_ng', 
            attr_name='heat_th2_is_ng', 
            real_name='PE Heizen 2 ist Erdgas', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th2_is_other = VariableMeta(
            var_name='heat_th2_is_other', 
            attr_name='heat_th2_is_other', 
            real_name='PE Heizen 2 ist Sonstige', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th4_carrier_type = VariableMeta(
            var_name='heat_th4_carrier_type', 
            attr_name='heat_th4_carrier_type', 
            real_name='Energieträger HZTH4', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th4_is_bio = VariableMeta(
            var_name='heat_th4_is_bio', 
            attr_name='heat_th4_is_bio', 
            real_name='PE Heizen 4 ist Biomasse', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th4_is_dh = VariableMeta(
            var_name='heat_th4_is_dh', 
            attr_name='heat_th4_is_dh', 
            real_name='PE Heizen 4 ist Fernwärme', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th4_is_ng = VariableMeta(
            var_name='heat_th4_is_ng', 
            attr_name='heat_th4_is_ng', 
            real_name='PE Heizen 4 ist Erdgas', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heat_th4_is_other = VariableMeta(
            var_name='heat_th4_is_other', 
            attr_name='heat_th4_is_other', 
            real_name='PE Heizen 4 ist Sonstige', 
            unit='bool', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month1 = VariableMeta(
            var_name='heating_month1', 
            attr_name='heating_month1', 
            real_name='Heizperiode Jänner', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month10 = VariableMeta(
            var_name='heating_month10', 
            attr_name='heating_month10', 
            real_name='Heizperiode Oktober', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month11 = VariableMeta(
            var_name='heating_month11', 
            attr_name='heating_month11', 
            real_name='Heizperiode November', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month12 = VariableMeta(
            var_name='heating_month12', 
            attr_name='heating_month12', 
            real_name='Heizperiode Dezember', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month2 = VariableMeta(
            var_name='heating_month2', 
            attr_name='heating_month2', 
            real_name='Heizperiode Februar', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month3 = VariableMeta(
            var_name='heating_month3', 
            attr_name='heating_month3', 
            real_name='Heizperiode März', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month4 = VariableMeta(
            var_name='heating_month4', 
            attr_name='heating_month4', 
            real_name='Heizperiode April', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month5 = VariableMeta(
            var_name='heating_month5', 
            attr_name='heating_month5', 
            real_name='Heizperiode Mai', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month6 = VariableMeta(
            var_name='heating_month6', 
            attr_name='heating_month6', 
            real_name='Heizperiode Juni', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month7 = VariableMeta(
            var_name='heating_month7', 
            attr_name='heating_month7', 
            real_name='Heizperiode Juli', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month8 = VariableMeta(
            var_name='heating_month8', 
            attr_name='heating_month8', 
            real_name='Heizperiode August', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.heating_month9 = VariableMeta(
            var_name='heating_month9', 
            attr_name='heating_month9', 
            real_name='Heizperiode September', 
            unit='Bool', 
            type_name='ui_writeback', 
            comment='Input fehlt', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_ext_wall_wo_window_m2 = VariableMeta(
            var_name='hull_ext_wall_wo_window_m2', 
            attr_name='hull_ext_wall_wo_window_m2', 
            real_name='Hüllfläche Außenwand', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment='exkl. Fenster', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_fenestration_rate = VariableMeta(
            var_name='hull_fenestration_rate', 
            attr_name='hull_fenestration_rate', 
            real_name='Hüllfläche Fensterflächenanteil', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_fundament_m2 = VariableMeta(
            var_name='hull_fundament_m2', 
            attr_name='hull_fundament_m2', 
            real_name='Hüllfläche Kellerdecke / Fundament', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_m2 = VariableMeta(
            var_name='hull_m2', 
            attr_name='hull_m2', 
            real_name='Hüllfläche gesamt', 
            unit='m² Brutto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_roof_m2 = VariableMeta(
            var_name='hull_roof_m2', 
            attr_name='hull_roof_m2', 
            real_name='Hüllfläche Dach', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_fundament = VariableMeta(
            var_name='hull_transmittance_fundament', 
            attr_name='hull_transmittance_fundament', 
            real_name='U-Wert Kellerdecke / Fundament', 
            unit='W/m²K', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_heatbridge = VariableMeta(
            var_name='hull_transmittance_heatbridge', 
            attr_name='hull_transmittance_heatbridge', 
            real_name='Wärmebrückenzuschlag', 
            unit=None, 
            type_name='userinput', 
            comment='Anteil des Transmissionsleitwerts', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_roof = VariableMeta(
            var_name='hull_transmittance_roof', 
            attr_name='hull_transmittance_roof', 
            real_name='U-Wert Dach', 
            unit='W/m²K', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_walls = VariableMeta(
            var_name='hull_transmittance_walls', 
            attr_name='hull_transmittance_walls', 
            real_name='U-Wert Außenwände', 
            unit='W/m²K', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_windows_east = VariableMeta(
            var_name='hull_transmittance_windows_east', 
            attr_name='hull_transmittance_windows_east', 
            real_name='U-Wert Fenster Ost', 
            unit='W/m²K', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_windows_horizontal = VariableMeta(
            var_name='hull_transmittance_windows_horizontal', 
            attr_name='hull_transmittance_windows_horizontal', 
            real_name='U-Wert Fenster Horizontal', 
            unit='W/m²K', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_windows_north = VariableMeta(
            var_name='hull_transmittance_windows_north', 
            attr_name='hull_transmittance_windows_north', 
            real_name='U-Wert Fenster Nord', 
            unit='W/m²K', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_windows_south = VariableMeta(
            var_name='hull_transmittance_windows_south', 
            attr_name='hull_transmittance_windows_south', 
            real_name='U-Wert Fenster Süd', 
            unit='W/m²K', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_transmittance_windows_west = VariableMeta(
            var_name='hull_transmittance_windows_west', 
            attr_name='hull_transmittance_windows_west', 
            real_name='U-Wert Fenster West', 
            unit='W/m²K', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_window_m2 = VariableMeta(
            var_name='hull_window_m2', 
            attr_name='hull_window_m2', 
            real_name='Hüllfläche Fenster gesamt', 
            unit='m² Brutto', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_windows_east_m2 = VariableMeta(
            var_name='hull_windows_east_m2', 
            attr_name='hull_windows_east_m2', 
            real_name='Hüllfläche Fenster Ost', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_windows_horizontal_m2 = VariableMeta(
            var_name='hull_windows_horizontal_m2', 
            attr_name='hull_windows_horizontal_m2', 
            real_name='Hüllfläche Fenster Horizontal', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_windows_north_m2 = VariableMeta(
            var_name='hull_windows_north_m2', 
            attr_name='hull_windows_north_m2', 
            real_name='Hüllfläche Fenster Nord', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_windows_south_m2 = VariableMeta(
            var_name='hull_windows_south_m2', 
            attr_name='hull_windows_south_m2', 
            real_name='Hüllfläche Fenster Süd', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.hull_windows_west_m2 = VariableMeta(
            var_name='hull_windows_west_m2', 
            attr_name='hull_windows_west_m2', 
            real_name='Hüllfläche Fenster West', 
            unit='m² Brutto', 
            type_name='userinput', 
            comment='inkl. Rahmen', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_efficiency_dirt = VariableMeta(
            var_name='illuminance_efficiency_dirt', 
            attr_name='illuminance_efficiency_dirt', 
            real_name='Abminderungsfaktor Verschmutzung', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_efficiency_glazing_ratio = VariableMeta(
            var_name='illuminance_efficiency_glazing_ratio', 
            attr_name='illuminance_efficiency_glazing_ratio', 
            real_name='Abminderungsfaktor Verglasungsanteil', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_office = VariableMeta(
            var_name='illuminance_min_office', 
            attr_name='illuminance_min_office', 
            real_name='Lux-Wert Büro', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_other = VariableMeta(
            var_name='illuminance_min_other', 
            attr_name='illuminance_min_other', 
            real_name='Lux-Wert Sonstige', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_residential = VariableMeta(
            var_name='illuminance_min_residential', 
            attr_name='illuminance_min_residential', 
            real_name='Lux-Wert Wohnen', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_retailfood = VariableMeta(
            var_name='illuminance_min_retailfood', 
            attr_name='illuminance_min_retailfood', 
            real_name='Lux-Wert Lebensmittelhandel', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_retailother = VariableMeta(
            var_name='illuminance_min_retailother', 
            attr_name='illuminance_min_retailother', 
            real_name='Lux-Wert Handel', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_schoolprim = VariableMeta(
            var_name='illuminance_min_schoolprim', 
            attr_name='illuminance_min_schoolprim', 
            real_name='Lux-Wert Kindergarten und Volksschule', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.illuminance_min_schoolsec = VariableMeta(
            var_name='illuminance_min_schoolsec', 
            attr_name='illuminance_min_schoolsec', 
            real_name='Lux-Wert Sekundäre Bildungseinrichtung oder Universität', 
            unit='lux', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.input_version_date = VariableMeta(
            var_name='input_version_date', 
            attr_name='input_version_date', 
            real_name='Inputdatenstruktur Datum', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='IN', 
            ka=None, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.input_version_number = VariableMeta(
            var_name='input_version_number', 
            attr_name='input_version_number', 
            real_name='Inputdatenstruktur Version', 
            unit=None, 
            type_name=None, 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.irradiation_opaque_surcharge = VariableMeta(
            var_name='irradiation_opaque_surcharge', 
            attr_name='irradiation_opaque_surcharge', 
            real_name='Zuschlag opake Bauteile', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lc = VariableMeta(
            var_name='lc', 
            attr_name='lc', 
            real_name='lc', 
            unit='m', 
            type_name='calculation', 
            comment=None, 
            source='BOTH', 
            ka=0, 
            category='Quartier', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lighting_factor_office = VariableMeta(
            var_name='lighting_factor_office', 
            attr_name='lighting_factor_office', 
            real_name='Beleuchtung Skalierung Büro', 
            unit='kWh/m²a', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lighting_factor_other = VariableMeta(
            var_name='lighting_factor_other', 
            attr_name='lighting_factor_other', 
            real_name='Beleuchtung Skalierung Sonstige Nutzung', 
            unit='kWh/m²a', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lighting_factor_retailfood = VariableMeta(
            var_name='lighting_factor_retailfood', 
            attr_name='lighting_factor_retailfood', 
            real_name='Beleuchtung Skalierung Handel Food', 
            unit='kWh/m²a', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lighting_factor_retailother = VariableMeta(
            var_name='lighting_factor_retailother', 
            attr_name='lighting_factor_retailother', 
            real_name='Beleuchtung Skalierung handel Non-Food', 
            unit='kWh/m²a', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lighting_factor_schoolprim = VariableMeta(
            var_name='lighting_factor_schoolprim', 
            attr_name='lighting_factor_schoolprim', 
            real_name='Beleuchtung Skalierung Ausbildung Primär', 
            unit='kWh/m²a', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.lighting_factor_schoolsec = VariableMeta(
            var_name='lighting_factor_schoolsec', 
            attr_name='lighting_factor_schoolsec', 
            real_name='Beleuchtung Skalierung Ausbildung Sekundär', 
            unit='kWh/m²a', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.location_address = VariableMeta(
            var_name='location_address', 
            attr_name='location_address', 
            real_name='Adresse', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='BOTH', 
            ka=2, 
            category='Metadaten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.location_postcode = VariableMeta(
            var_name='location_postcode', 
            attr_name='location_postcode', 
            real_name='Postleitzahl', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_annual_milage_district = VariableMeta(
            var_name='mob_annual_milage_district', 
            attr_name='mob_annual_milage_district', 
            real_name='Gesamtverkehr', 
            unit='km/a', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_annual_mileage_PAX = VariableMeta(
            var_name='mob_annual_mileage_PAX', 
            attr_name='mob_annual_mileage_PAX', 
            real_name='Gesamtverkehr pro STATPAX', 
            unit='km/PAX/a', 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Mobilität', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_motorization_perNFA_residential = VariableMeta(
            var_name='mob_motorization_perNFA_residential', 
            attr_name='mob_motorization_perNFA_residential', 
            real_name='Autos pro Nutzung Wohnen', 
            unit='pro 100m²', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_motorization_perNFA_retail = VariableMeta(
            var_name='mob_motorization_perNFA_retail', 
            attr_name='mob_motorization_perNFA_retail', 
            real_name='Autos pro Nutzung Einkaufen', 
            unit='pro 100m²', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_motorization_perNFA_work = VariableMeta(
            var_name='mob_motorization_perNFA_work', 
            attr_name='mob_motorization_perNFA_work', 
            real_name='Autos pro Nutzung Arbeit', 
            unit='pro 100m²', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_pkm_factor = VariableMeta(
            var_name='mob_pkm_factor', 
            attr_name='mob_pkm_factor', 
            real_name='Reduktionsfaktor JPkm MIV', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_shading_factor_c = VariableMeta(
            var_name='mob_shading_factor_c', 
            attr_name='mob_shading_factor_c', 
            real_name='Abschattungseffekt Mobiler Sonnenschutz gekühlt', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_shading_factor_u = VariableMeta(
            var_name='mob_shading_factor_u', 
            attr_name='mob_shading_factor_u', 
            real_name='Abschattungseffekt Mobiler Sonnenschutz ungekühlt', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_simultaneity_edu = VariableMeta(
            var_name='mob_simultaneity_edu', 
            attr_name='mob_simultaneity_edu', 
            real_name='Gleichzeitigkeitsfaktorsfaktor Ausbildung', 
            unit=None, 
            type_name='userinput', 
            comment='1 statistische Nutzer ist x realer Nutzer zwecks Wege, die ins Quartier führen)', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_simultaneity_office = VariableMeta(
            var_name='mob_simultaneity_office', 
            attr_name='mob_simultaneity_office', 
            real_name='Gleichzetigkeitsfaktor Arbeit', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mob_simultaneity_retail = VariableMeta(
            var_name='mob_simultaneity_retail', 
            attr_name='mob_simultaneity_retail', 
            real_name='Gleichzeitigkeitsfaktorsfaktor Einkaufen', 
            unit=None, 
            type_name='userinput', 
            comment='wieviele Verkaufsflchen werden von mehreren Nutzern aufgesucht?', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobility_is_included = VariableMeta(
            var_name='mobility_is_included', 
            attr_name='mobility_is_included', 
            real_name='MIV simulieren', 
            unit='bool', 
            type_name='ui_writeback', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobility_mode = VariableMeta(
            var_name='mobility_mode', 
            attr_name='mobility_mode', 
            real_name='Mobilitätsverfahren', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobility_region = VariableMeta(
            var_name='mobility_region', 
            attr_name='mobility_region', 
            real_name='Mobilitätsregion', 
            unit='str', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobility_vehicle_count = VariableMeta(
            var_name='mobility_vehicle_count', 
            attr_name='mobility_vehicle_count', 
            real_name='Fahrzeuge', 
            unit='Anzahl', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobshare_office = VariableMeta(
            var_name='mobshare_office', 
            attr_name='mobshare_office', 
            real_name='Zielverkehrsanteil Büro', 
            unit='%', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobshare_residential = VariableMeta(
            var_name='mobshare_residential', 
            attr_name='mobshare_residential', 
            real_name='Zielverkehrsanteil Wohnen', 
            unit='%', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobshare_retail = VariableMeta(
            var_name='mobshare_retail', 
            attr_name='mobshare_retail', 
            real_name='Zielverkehrsanteil Handel', 
            unit='%', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.mobshare_school = VariableMeta(
            var_name='mobshare_school', 
            attr_name='mobshare_school', 
            real_name='Zielverkehrsanteil Ausbildung', 
            unit='%', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.moped_factor = VariableMeta(
            var_name='moped_factor', 
            attr_name='moped_factor', 
            real_name='Moped im Verhältnis zu Auto', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.municipality_name = VariableMeta(
            var_name='municipality_name', 
            attr_name='municipality_name', 
            real_name='Gemeinde', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pe_conversion_factor_gasoline = VariableMeta(
            var_name='pe_conversion_factor_gasoline', 
            attr_name='pe_conversion_factor_gasoline', 
            real_name='PE-Konversionsfaktor Kraftstoff', 
            unit='kWhPE/kWhEE', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.per_NFA = VariableMeta(
            var_name='per_NFA', 
            attr_name='per_NFA', 
            real_name='Pro NGF ( Kehrwert NGF)', 
            unit='1/m²NGF', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_bike = VariableMeta(
            var_name='pkm_bike', 
            attr_name='pkm_bike', 
            real_name='Pkm Fahrrad', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_bus = VariableMeta(
            var_name='pkm_bus', 
            attr_name='pkm_bus', 
            real_name='Pkm Stadt/ Regionalbus', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_car_driver = VariableMeta(
            var_name='pkm_car_driver', 
            attr_name='pkm_car_driver', 
            real_name='Pkm PKW-LenkerIn', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_car_passenger = VariableMeta(
            var_name='pkm_car_passenger', 
            attr_name='pkm_car_passenger', 
            real_name='Pkm PKW-MitfahrerIn', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_distancebus = VariableMeta(
            var_name='pkm_distancebus', 
            attr_name='pkm_distancebus', 
            real_name='Pkm Reisebus', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_mofa = VariableMeta(
            var_name='pkm_mofa', 
            attr_name='pkm_mofa', 
            real_name='Pkm Moped', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_pedestrian = VariableMeta(
            var_name='pkm_pedestrian', 
            attr_name='pkm_pedestrian', 
            real_name='Pkm Zu Fuß', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_train = VariableMeta(
            var_name='pkm_train', 
            attr_name='pkm_train', 
            real_name='Pkm Eisenbahn', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.pkm_tram_metro = VariableMeta(
            var_name='pkm_tram_metro', 
            attr_name='pkm_tram_metro', 
            real_name='Pkm Straßenbahn/U-Bahn', 
            unit='Pkm', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.plot_area = VariableMeta(
            var_name='plot_area', 
            attr_name='plot_area', 
            real_name='Bebaubare Grundstücksfläche', 
            unit='m²GF', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.project_creation_date = VariableMeta(
            var_name='project_creation_date', 
            attr_name='project_creation_date', 
            real_name='Erstellungsdatum', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='BOTH', 
            ka=2, 
            category='Metadaten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.project_description = VariableMeta(
            var_name='project_description', 
            attr_name='project_description', 
            real_name='Projektbeschreibung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.project_name = VariableMeta(
            var_name='project_name', 
            attr_name='project_name', 
            real_name='Projektname', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='BOTH', 
            ka=2, 
            category='Metadaten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.project_scenario_name = VariableMeta(
            var_name='project_scenario_name', 
            attr_name='project_scenario_name', 
            real_name='Variante / Scenario', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='BOTH', 
            ka=2, 
            category='Metadaten', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.project_url = VariableMeta(
            var_name='project_url', 
            attr_name='project_url', 
            real_name='ProjektURL', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp1_dh = VariableMeta(
            var_name='rcp1_dh', 
            attr_name='rcp1_dh', 
            real_name='Absenkfaktor 1 Fernwärme', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp1_fossil = VariableMeta(
            var_name='rcp1_fossil', 
            attr_name='rcp1_fossil', 
            real_name='Absenkfaktor 1 Andere Fossile', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp1_renewable = VariableMeta(
            var_name='rcp1_renewable', 
            attr_name='rcp1_renewable', 
            real_name='Absenkfaktor 1 Erneuerbare', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp2_dh = VariableMeta(
            var_name='rcp2_dh', 
            attr_name='rcp2_dh', 
            real_name='Absenkfaktor 2 Fernwärme', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp2_fossil = VariableMeta(
            var_name='rcp2_fossil', 
            attr_name='rcp2_fossil', 
            real_name='Absenkfaktor 2 Andere Fossile', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp2_renewable = VariableMeta(
            var_name='rcp2_renewable', 
            attr_name='rcp2_renewable', 
            real_name='Absenkfaktor 2 Erneuerbare', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp3_dh = VariableMeta(
            var_name='rcp3_dh', 
            attr_name='rcp3_dh', 
            real_name='Absenkfaktor 3 Fernwärme', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp3_fossil = VariableMeta(
            var_name='rcp3_fossil', 
            attr_name='rcp3_fossil', 
            real_name='Absenkfaktor 3 Andere Fossile', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rcp3_renewable = VariableMeta(
            var_name='rcp3_renewable', 
            attr_name='rcp3_renewable', 
            real_name='Absenkfaktor 3 Erneuerbare', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_office = VariableMeta(
            var_name='renovation_ratio_office', 
            attr_name='renovation_ratio_office', 
            real_name='Sanierung Anteil Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_other = VariableMeta(
            var_name='renovation_ratio_other', 
            attr_name='renovation_ratio_other', 
            real_name='Sanierung Anteil Sonstige', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_residential = VariableMeta(
            var_name='renovation_ratio_residential', 
            attr_name='renovation_ratio_residential', 
            real_name='Sanierung Anteil Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_retailfood = VariableMeta(
            var_name='renovation_ratio_retailfood', 
            attr_name='renovation_ratio_retailfood', 
            real_name='Sanierung Anteil Lebensmittelhandel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_retailother = VariableMeta(
            var_name='renovation_ratio_retailother', 
            attr_name='renovation_ratio_retailother', 
            real_name='Sanierung Anteil Handel Sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_schoolprim = VariableMeta(
            var_name='renovation_ratio_schoolprim', 
            attr_name='renovation_ratio_schoolprim', 
            real_name='Sanierung Anteil Bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_ratio_schoolsec = VariableMeta(
            var_name='renovation_ratio_schoolsec', 
            attr_name='renovation_ratio_schoolsec', 
            real_name='Sanierung Anteil Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.renovation_share = VariableMeta(
            var_name='renovation_share', 
            attr_name='renovation_share', 
            real_name='Sanierungsanteil im Quartier', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='BOTH', 
            ka=0, 
            category='Quartier', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_avg = VariableMeta(
            var_name='rh_avg', 
            attr_name='rh_avg', 
            real_name='Raumhöhe Quartier', 
            unit='m Netto', 
            type_name='calculation', 
            comment=None, 
            source='BOTH', 
            ka=0, 
            category='Quartier', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_ceiling = VariableMeta(
            var_name='rh_ceiling', 
            attr_name='rh_ceiling', 
            real_name='Höhe Geschoßdecken', 
            unit='m', 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_office = VariableMeta(
            var_name='rh_office', 
            attr_name='rh_office', 
            real_name='Raumhöhe Büro', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_other = VariableMeta(
            var_name='rh_other', 
            attr_name='rh_other', 
            real_name='Raumhöhe Sonstige Nutzung', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_residential = VariableMeta(
            var_name='rh_residential', 
            attr_name='rh_residential', 
            real_name='Raumhöhe Wohnen', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_retailfood = VariableMeta(
            var_name='rh_retailfood', 
            attr_name='rh_retailfood', 
            real_name='Raumhöhe Lebensmittelhandel', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_retailother = VariableMeta(
            var_name='rh_retailother', 
            attr_name='rh_retailother', 
            real_name='Raumhöhe Handel sonstiger', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_schoolprim = VariableMeta(
            var_name='rh_schoolprim', 
            attr_name='rh_schoolprim', 
            real_name='Raumhöhe primäre Bildundseinrichtung/ Kindergarten', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.rh_schoolsec = VariableMeta(
            var_name='rh_schoolsec', 
            attr_name='rh_schoolsec', 
            real_name='Raumhöhe sekundäre Bildungseinrichtung/ Universität', 
            unit='m Netto', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.scenario_version = VariableMeta(
            var_name='scenario_version', 
            attr_name='scenario_version', 
            real_name='Tool Version', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.storey_count_avg = VariableMeta(
            var_name='storey_count_avg', 
            attr_name='storey_count_avg', 
            real_name='Anzahl Geschoße', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.test_NFV_shares = VariableMeta(
            var_name='test_NFV_shares', 
            attr_name='test_NFV_shares', 
            real_name='Test', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.test_heat_balance = VariableMeta(
            var_name='test_heat_balance', 
            attr_name='test_heat_balance', 
            real_name='Wärmebilanz', 
            unit=True, 
            type_name=None, 
            comment=None, 
            source='OUT', 
            ka=None, 
            category='Wärmebilanz', 
            area=None, 
            label='Wärmebilanztest', 
            var_cat=None
)
        self.transmittance_MW = VariableMeta(
            var_name='transmittance_MW', 
            attr_name='transmittance_MW', 
            real_name='Transmissionsleitwert absolut', 
            unit='MW/K', 
            type_name='calculation', 
            comment='ink. Wärmebrückenzuschlag', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.transmittance_Wm = VariableMeta(
            var_name='transmittance_Wm²', 
            attr_name='transmittance_Wm', 
            real_name='Transmissionsleitwert spezifisch', 
            unit='W/m²K', 
            type_name='calculation', 
            comment='ink. Wärmebrückenzuschlag', 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_eduprim = VariableMeta(
            var_name='usage_concurrency_summer_eduprim', 
            attr_name='usage_concurrency_summer_eduprim', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_edusec = VariableMeta(
            var_name='usage_concurrency_summer_edusec', 
            attr_name='usage_concurrency_summer_edusec', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_office = VariableMeta(
            var_name='usage_concurrency_summer_office', 
            attr_name='usage_concurrency_summer_office', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_other = VariableMeta(
            var_name='usage_concurrency_summer_other', 
            attr_name='usage_concurrency_summer_other', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_res = VariableMeta(
            var_name='usage_concurrency_summer_res', 
            attr_name='usage_concurrency_summer_res', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_retailfood = VariableMeta(
            var_name='usage_concurrency_summer_retailfood', 
            attr_name='usage_concurrency_summer_retailfood', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_summer_retailother = VariableMeta(
            var_name='usage_concurrency_summer_retailother', 
            attr_name='usage_concurrency_summer_retailother', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Sommer Handel sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_eduprim = VariableMeta(
            var_name='usage_concurrency_winter_eduprim', 
            attr_name='usage_concurrency_winter_eduprim', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_edusec = VariableMeta(
            var_name='usage_concurrency_winter_edusec', 
            attr_name='usage_concurrency_winter_edusec', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_office = VariableMeta(
            var_name='usage_concurrency_winter_office', 
            attr_name='usage_concurrency_winter_office', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_other = VariableMeta(
            var_name='usage_concurrency_winter_other', 
            attr_name='usage_concurrency_winter_other', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_res = VariableMeta(
            var_name='usage_concurrency_winter_res', 
            attr_name='usage_concurrency_winter_res', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_retailfood = VariableMeta(
            var_name='usage_concurrency_winter_retailfood', 
            attr_name='usage_concurrency_winter_retailfood', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.usage_concurrency_winter_retailother = VariableMeta(
            var_name='usage_concurrency_winter_retailother', 
            attr_name='usage_concurrency_winter_retailother', 
            real_name='Gleichzeitigkeitsfaktor Innere Wärmen Winter Handel sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_office = VariableMeta(
            var_name='vent_ach_max_office', 
            attr_name='vent_ach_max_office', 
            real_name='Luftwechsel Büro', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_other = VariableMeta(
            var_name='vent_ach_max_other', 
            attr_name='vent_ach_max_other', 
            real_name='Luftwechsel Sonstige Nutzung', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_residential = VariableMeta(
            var_name='vent_ach_max_residential', 
            attr_name='vent_ach_max_residential', 
            real_name='Luftwechsel Wohnen', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_retailfood = VariableMeta(
            var_name='vent_ach_max_retailfood', 
            attr_name='vent_ach_max_retailfood', 
            real_name='Luftwechsel Handel Lebensmittel', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_retailother = VariableMeta(
            var_name='vent_ach_max_retailother', 
            attr_name='vent_ach_max_retailother', 
            real_name='Luftwechsel Handel sonstiger', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_schoolprim = VariableMeta(
            var_name='vent_ach_max_schoolprim', 
            attr_name='vent_ach_max_schoolprim', 
            real_name='Luftwechsel Bildung primär', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_ach_max_schoolsec = VariableMeta(
            var_name='vent_ach_max_schoolsec', 
            attr_name='vent_ach_max_schoolsec', 
            real_name='Luftwechsel Bildung sekundär', 
            unit='1/h', 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_air_tightness = VariableMeta(
            var_name='vent_air_tightness', 
            attr_name='vent_air_tightness', 
            real_name='Luftdichtheit n50', 
            unit='1/h', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_office = VariableMeta(
            var_name='vent_heat_recovery_summer_office', 
            attr_name='vent_heat_recovery_summer_office', 
            real_name='Wärmerückgewinnung Sommer Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_other = VariableMeta(
            var_name='vent_heat_recovery_summer_other', 
            attr_name='vent_heat_recovery_summer_other', 
            real_name='Wärmerückgewinnung Sommer Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_residential = VariableMeta(
            var_name='vent_heat_recovery_summer_residential', 
            attr_name='vent_heat_recovery_summer_residential', 
            real_name='Wärmerückgewinnung Sommer Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_retailfood = VariableMeta(
            var_name='vent_heat_recovery_summer_retailfood', 
            attr_name='vent_heat_recovery_summer_retailfood', 
            real_name='Wärmerückgewinnung Sommer Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_retailother = VariableMeta(
            var_name='vent_heat_recovery_summer_retailother', 
            attr_name='vent_heat_recovery_summer_retailother', 
            real_name='Wärmerückgewinnung Sommer Handel sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_schoolprim = VariableMeta(
            var_name='vent_heat_recovery_summer_schoolprim', 
            attr_name='vent_heat_recovery_summer_schoolprim', 
            real_name='Wärmerückgewinnung Sommer Bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_summer_schoolsec = VariableMeta(
            var_name='vent_heat_recovery_summer_schoolsec', 
            attr_name='vent_heat_recovery_summer_schoolsec', 
            real_name='Wärmerückgewinnung Sommer Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_office = VariableMeta(
            var_name='vent_heat_recovery_winter_office', 
            attr_name='vent_heat_recovery_winter_office', 
            real_name='Wärmerückgewinnung Winter Büro', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_other = VariableMeta(
            var_name='vent_heat_recovery_winter_other', 
            attr_name='vent_heat_recovery_winter_other', 
            real_name='Wärmerückgewinnung Winter Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_residential = VariableMeta(
            var_name='vent_heat_recovery_winter_residential', 
            attr_name='vent_heat_recovery_winter_residential', 
            real_name='Wärmerückgewinnung Winter Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_retailfood = VariableMeta(
            var_name='vent_heat_recovery_winter_retailfood', 
            attr_name='vent_heat_recovery_winter_retailfood', 
            real_name='Wärmerückgewinnung Winter Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_retailother = VariableMeta(
            var_name='vent_heat_recovery_winter_retailother', 
            attr_name='vent_heat_recovery_winter_retailother', 
            real_name='Wärmerückgewinnung Winter Handel sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_schoolprim = VariableMeta(
            var_name='vent_heat_recovery_winter_schoolprim', 
            attr_name='vent_heat_recovery_winter_schoolprim', 
            real_name='Wärmerückgewinnung Winter Bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_heat_recovery_winter_schoolsec = VariableMeta(
            var_name='vent_heat_recovery_winter_schoolsec', 
            attr_name='vent_heat_recovery_winter_schoolsec', 
            real_name='Wärmerückgewinnung Winter Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment='Maximal', 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_infiltration_ACH = VariableMeta(
            var_name='vent_infiltration_ACH', 
            attr_name='vent_infiltration_ACH', 
            real_name='Luftwechsel Infiltration', 
            unit='1/h', 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_office = VariableMeta(
            var_name='vent_night_office', 
            attr_name='vent_night_office', 
            real_name='Nachtauskühlung Fensterstellung Büro', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_other = VariableMeta(
            var_name='vent_night_other', 
            attr_name='vent_night_other', 
            real_name='Nachtauskühlung Fensterstellung Sonstige Nutzung', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_residential = VariableMeta(
            var_name='vent_night_residential', 
            attr_name='vent_night_residential', 
            real_name='Nachtauskühlung Fensterstellung Wohnen', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_retailfood = VariableMeta(
            var_name='vent_night_retailfood', 
            attr_name='vent_night_retailfood', 
            real_name='Nachtauskühlung Fensterstellung Handel Lebensmittel', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_retailother = VariableMeta(
            var_name='vent_night_retailother', 
            attr_name='vent_night_retailother', 
            real_name='Nachtauskühlung Fensterstellung Handel sonstiger', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_schoolprim = VariableMeta(
            var_name='vent_night_schoolprim', 
            attr_name='vent_night_schoolprim', 
            real_name='Nachtauskühlung Fensterstellung Bildung primär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_night_schoolsec = VariableMeta(
            var_name='vent_night_schoolsec', 
            attr_name='vent_night_schoolsec', 
            real_name='Nachtauskühlung Fensterstellung Bildung sekundär', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_office = VariableMeta(
            var_name='vent_scale_office', 
            attr_name='vent_scale_office', 
            real_name='Skalierung Luftwechsel Büro', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_other = VariableMeta(
            var_name='vent_scale_other', 
            attr_name='vent_scale_other', 
            real_name='Skalierung Luftwechsel Sonstige Nutzung', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_residential = VariableMeta(
            var_name='vent_scale_residential', 
            attr_name='vent_scale_residential', 
            real_name='Skalierung Luftwechsel Wohnen', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_retail = VariableMeta(
            var_name='vent_scale_retail', 
            attr_name='vent_scale_retail', 
            real_name='Skalierung Luftwechsel Handel sonstiger', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_school_prim = VariableMeta(
            var_name='vent_scale_school_prim', 
            attr_name='vent_scale_school_prim', 
            real_name='Skalierung Luftwechsel Bildung primär', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_school_sec = VariableMeta(
            var_name='vent_scale_school_sec', 
            attr_name='vent_scale_school_sec', 
            real_name='Skalierung Luftwechsel Bildung sekundär', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_scale_supermarket = VariableMeta(
            var_name='vent_scale_supermarket', 
            attr_name='vent_scale_supermarket', 
            real_name='Skalierung Luftwechsel Handel Lebensmittel', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='IN', 
            ka=0, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_office = VariableMeta(
            var_name='vent_share_mechanical_office', 
            attr_name='vent_share_mechanical_office', 
            real_name='Mechanische Lüftung Büro', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_other = VariableMeta(
            var_name='vent_share_mechanical_other', 
            attr_name='vent_share_mechanical_other', 
            real_name='Mechanische Lüftung Sonstige Nutzung', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_residential = VariableMeta(
            var_name='vent_share_mechanical_residential', 
            attr_name='vent_share_mechanical_residential', 
            real_name='Mechanische Lüftung Wohnen', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_retailfood = VariableMeta(
            var_name='vent_share_mechanical_retailfood', 
            attr_name='vent_share_mechanical_retailfood', 
            real_name='Mechanische Lüftung Handel Lebensmittel', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_retailother = VariableMeta(
            var_name='vent_share_mechanical_retailother', 
            attr_name='vent_share_mechanical_retailother', 
            real_name='Mechanische Lüftung Handel sonstiger', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_schoolprim = VariableMeta(
            var_name='vent_share_mechanical_schoolprim', 
            attr_name='vent_share_mechanical_schoolprim', 
            real_name='Mechanische Lüftung Bildung primär', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_share_mechanical_schoolsec = VariableMeta(
            var_name='vent_share_mechanical_schoolsec', 
            attr_name='vent_share_mechanical_schoolsec', 
            real_name='Mechanische Lüftung Bildung sekundär', 
            unit='Anteil', 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.vent_tightness_ratio_blowerdoor_to_real = VariableMeta(
            var_name='vent_tightness_ratio_blowerdoor_to_real', 
            attr_name='vent_tightness_ratio_blowerdoor_to_real', 
            real_name='Verhältnis Blower Door / Reale Infiltration', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.weather_index = VariableMeta(
            var_name='weather_index', 
            attr_name='weather_index', 
            real_name='Wetterdatensatz Nummer', 
            unit=None, 
            type_name='calculation', 
            comment=None, 
            source='BOTH', 
            ka=0, 
            category='Wetter', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.weather_name = VariableMeta(
            var_name='weather_name', 
            attr_name='weather_name', 
            real_name='Wetterdatensatz Name', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='BOTH', 
            ka=2, 
            category='Wetter', 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_summer_east = VariableMeta(
            var_name='window_irradiation_factor_summer_east', 
            attr_name='window_irradiation_factor_summer_east', 
            real_name='Einstrahlungsfaktor Sommer Ost', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_summer_horizontal = VariableMeta(
            var_name='window_irradiation_factor_summer_horizontal', 
            attr_name='window_irradiation_factor_summer_horizontal', 
            real_name='Einstrahlungsfaktor Sommer  Horizontal', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_summer_north = VariableMeta(
            var_name='window_irradiation_factor_summer_north', 
            attr_name='window_irradiation_factor_summer_north', 
            real_name='Einstrahlungsfaktor Sommer Nord', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_summer_south = VariableMeta(
            var_name='window_irradiation_factor_summer_south', 
            attr_name='window_irradiation_factor_summer_south', 
            real_name='Einstrahlungsfaktor Sommer Süd', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_summer_west = VariableMeta(
            var_name='window_irradiation_factor_summer_west', 
            attr_name='window_irradiation_factor_summer_west', 
            real_name='Einstrahlungsfaktor Sommer  West', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_winter_east = VariableMeta(
            var_name='window_irradiation_factor_winter_east', 
            attr_name='window_irradiation_factor_winter_east', 
            real_name='Einstrahlungsfaktor Fenster Ost', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_winter_horizontal = VariableMeta(
            var_name='window_irradiation_factor_winter_horizontal', 
            attr_name='window_irradiation_factor_winter_horizontal', 
            real_name='Einstrahlungsfaktor Fenster Horizontal', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_winter_north = VariableMeta(
            var_name='window_irradiation_factor_winter_north', 
            attr_name='window_irradiation_factor_winter_north', 
            real_name='Einstrahlungsfaktor Fenster Nord', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_winter_south = VariableMeta(
            var_name='window_irradiation_factor_winter_south', 
            attr_name='window_irradiation_factor_winter_south', 
            real_name='Einstrahlungsfaktor Fenster Süd', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_irradiation_factor_winter_west = VariableMeta(
            var_name='window_irradiation_factor_winter_west', 
            attr_name='window_irradiation_factor_winter_west', 
            real_name='Einstrahlungsfaktor Fenster West', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_total_transmittance_east = VariableMeta(
            var_name='window_total_transmittance_east', 
            attr_name='window_total_transmittance_east', 
            real_name='g-Wert Fenster Ost', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_total_transmittance_horizontal = VariableMeta(
            var_name='window_total_transmittance_horizontal', 
            attr_name='window_total_transmittance_horizontal', 
            real_name='g-Wert Fenster Horizontal', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_total_transmittance_north = VariableMeta(
            var_name='window_total_transmittance_north', 
            attr_name='window_total_transmittance_north', 
            real_name='g-Wert Fenster Nord', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_total_transmittance_south = VariableMeta(
            var_name='window_total_transmittance_south', 
            attr_name='window_total_transmittance_south', 
            real_name='g-Wert Fenster Süd', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.window_total_transmittance_west = VariableMeta(
            var_name='window_total_transmittance_west', 
            attr_name='window_total_transmittance_west', 
            real_name='g-Wert Fenster West', 
            unit=None, 
            type_name='userinput', 
            comment=None, 
            source='IN', 
            ka=2, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.year_rcp0 = VariableMeta(
            var_name='year_rcp0', 
            attr_name='year_rcp0', 
            real_name='Bezugsjahr Ausgangssituation', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.year_rcp1 = VariableMeta(
            var_name='year_rcp1', 
            attr_name='year_rcp1', 
            real_name='Bezugsjahr Stütztstelle 1', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.year_rcp2 = VariableMeta(
            var_name='year_rcp2', 
            attr_name='year_rcp2', 
            real_name='Bezugsjahr Stütztstelle 2', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)
        self.year_rcp3 = VariableMeta(
            var_name='year_rcp3', 
            attr_name='year_rcp3', 
            real_name='Bezugsjahr Stütztstelle 3', 
            unit=None, 
            type_name='value', 
            comment=None, 
            source='IN', 
            ka=1, 
            category=None, 
            area=None, 
            label=None, 
            var_cat=None
)

SCHEMA_META = Meta()

ATTR_NAME_MAP: dict[str, str] = {
    'ACH_night_m³': 'ACH_night_m',
    'Batt_FEC': 'Batt_FEC',
    'Batt_RTE': 'Batt_RTE',
    'Batt_SOC_init': 'Batt_SOC_init',
    'Batt_auto_discharge_factor': 'Batt_auto_discharge_factor',
    'Batt_c_rate': 'Batt_c_rate',
    'Batt_cap_Wh_per_NFA': 'Batt_cap_Wh_per_NFA',
    'Batt_cap_kWh': 'Batt_cap_kWh',
    'Batt_charge_losses': 'Batt_charge_losses',
    'Batt_charging_losses': 'Batt_charging_losses',
    'Batt_discharge_losses': 'Batt_discharge_losses',
    'Batt_eff_factor_charge': 'Batt_eff_factor_charge',
    'Batt_eff_factor_discharge': 'Batt_eff_factor_discharge',
    'Batt_is_gridcharged': 'Batt_is_gridcharged',
    'Batt_is_not_used_during_signals': 'Batt_is_not_used_during_signals',
    'Batt_is_used': 'Batt_is_used',
    'Batt_is_used_for_EV': 'Batt_is_used_for_EV',
    'Batt_is_used_for_HVACminimum': 'Batt_is_used_for_HVACminimum',
    'Batt_is_used_for_plugloads': 'Batt_is_used_for_plugloads',
    'Batt_max_power_specific': 'Batt_max_power_specific',
    'Batt_self_discharge_rate': 'Batt_self_discharge_rate',
    'Batt_to_Ec_min': 'Batt_to_Ec_min',
    'Batt_to_Edhw_min': 'Batt_to_Edhw_min',
    'Batt_to_Eev_min': 'Batt_to_Eev_min',
    'Batt_to_Eh_min': 'Batt_to_Eh_min',
    'Batt_to_Ev_min': 'Batt_to_Ev_min',
    'Batt_to_HVAC': 'Batt_to_HVAC',
    'Batt_to_plugloads': 'Batt_to_plugloads',
    'Batt_total_charge': 'Batt_total_charge',
    'Batt_total_charge_input': 'Batt_total_charge_input',
    'Batt_total_discharge': 'Batt_total_discharge',
    'COMP_area_balconies': 'COMP_area_balconies',
    'COMP_area_basement_ceiling': 'COMP_area_basement_ceiling',
    'COMP_area_basement_floor_unheated': 'COMP_area_basement_floor_unheated',
    'COMP_area_ceil_to_air': 'COMP_area_ceil_to_air',
    'COMP_area_ceiling_topfloor': 'COMP_area_ceiling_topfloor',
    'COMP_area_columns': 'COMP_area_columns',
    'COMP_area_fundament': 'COMP_area_fundament',
    'COMP_area_internal_wall_load': 'COMP_area_internal_wall_load',
    'COMP_area_internal_wall_nonload': 'COMP_area_internal_wall_nonload',
    'COMP_area_internal_wall_unheated': 'COMP_area_internal_wall_unheated',
    'COMP_area_terrace': 'COMP_area_terrace',
    'COMP_area_unheated_horizontal': 'COMP_area_unheated_horizontal',
    'COMP_area_wall_earth_contacted': 'COMP_area_wall_earth_contacted',
    'COMP_area_wall_ec_unheated': 'COMP_area_wall_ec_unheated',
    'COMP_area_windowframe': 'COMP_area_windowframe',
    'COMP_area_windowglazing': 'COMP_area_windowglazing',
    'COMP_name_balconies': 'COMP_name_balconies',
    'COMP_name_basement_ceiling': 'COMP_name_basement_ceiling',
    'COMP_name_basement_floor_unheated': 'COMP_name_basement_floor_unheated',
    'COMP_name_ceil_to_air': 'COMP_name_ceil_to_air',
    'COMP_name_ceiling_topfloor': 'COMP_name_ceiling_topfloor',
    'COMP_name_columns': 'COMP_name_columns',
    'COMP_name_fundament': 'COMP_name_fundament',
    'COMP_name_internal_wall_load': 'COMP_name_internal_wall_load',
    'COMP_name_internal_wall_nonload': 'COMP_name_internal_wall_nonload',
    'COMP_name_internal_wall_unheated': 'COMP_name_internal_wall_unheated',
    'COMP_name_other': 'COMP_name_other',
    'COMP_name_terrace': 'COMP_name_terrace',
    'COMP_name_unheated_horizontal': 'COMP_name_unheated_horizontal',
    'COMP_name_wall_earth_contacted': 'COMP_name_wall_earth_contacted',
    'COMP_name_wall_ec_unheated': 'COMP_name_wall_ec_unheated',
    'COMP_name_windowframe': 'COMP_name_windowframe',
    'COMP_name_windowglazing': 'COMP_name_windowglazing',
    'COMP_name_windows': 'COMP_name_windows',
    'DHW_1_efficiency': 'DHW_1_efficiency',
    'DHW_1_el_aux': 'DHW_1_el_aux',
    'DHW_1_incl_distribution_factor': 'DHW_1_incl_distribution_factor',
    'DHW_1_is_electric': 'DHW_1_is_electric',
    'DHW_1_is_used': 'DHW_1_is_used',
    'DHW_1_share_office': 'DHW_1_share_office',
    'DHW_1_share_other': 'DHW_1_share_other',
    'DHW_1_share_residential': 'DHW_1_share_residential',
    'DHW_1_share_retailfood': 'DHW_1_share_retailfood',
    'DHW_1_share_retailother': 'DHW_1_share_retailother',
    'DHW_1_share_schoolprim': 'DHW_1_share_schoolprim',
    'DHW_1_share_schoolsec': 'DHW_1_share_schoolsec',
    'DHW_2_efficiency': 'DHW_2_efficiency',
    'DHW_2_el_aux': 'DHW_2_el_aux',
    'DHW_2_incl_distribution_factor': 'DHW_2_incl_distribution_factor',
    'DHW_2_is_electric': 'DHW_2_is_electric',
    'DHW_2_is_used': 'DHW_2_is_used',
    'DHW_Tmax': 'DHW_Tmax',
    'DHW_Tmax_input': 'DHW_Tmax_input',
    'DHW_Tmin': 'DHW_Tmin',
    'DHW_carriertype_1': 'DHW_carriertype_1',
    'DHW_carriertype_2': 'DHW_carriertype_2',
    'DHW_concurrency_office': 'DHW_concurrency_office',
    'DHW_concurrency_other': 'DHW_concurrency_other',
    'DHW_concurrency_residential': 'DHW_concurrency_residential',
    'DHW_concurrency_retailfood': 'DHW_concurrency_retailfood',
    'DHW_concurrency_retailother': 'DHW_concurrency_retailother',
    'DHW_concurrency_schoolprim': 'DHW_concurrency_schoolprim',
    'DHW_concurrency_schoolsec': 'DHW_concurrency_schoolsec',
    'DHW_conversion_1': 'DHW_conversion_1',
    'DHW_conversion_2': 'DHW_conversion_2',
    'DHW_demand_office_kWhm2': 'DHW_demand_office_kWhm2',
    'DHW_demand_other_kWhm2': 'DHW_demand_other_kWhm2',
    'DHW_demand_residential_kWhm2': 'DHW_demand_residential_kWhm2',
    'DHW_demand_retailfood_kWhm2': 'DHW_demand_retailfood_kWhm2',
    'DHW_demand_retailother_kWhm2': 'DHW_demand_retailother_kWhm2',
    'DHW_demand_schoolprim_kWhm2': 'DHW_demand_schoolprim_kWhm2',
    'DHW_demand_schoolsec_kWhm2': 'DHW_demand_schoolsec_kWhm2',
    'DHW_efficiency_distribution_1': 'DHW_efficiency_distribution_1',
    'DHW_efficiency_distribution_2': 'DHW_efficiency_distribution_2',
    'DHW_losses_1': 'DHW_losses_1',
    'DHW_losses_2': 'DHW_losses_2',
    'DHW_occupancy_office': 'DHW_occupancy_office',
    'DHW_occupancy_other': 'DHW_occupancy_other',
    'DHW_occupancy_residential': 'DHW_occupancy_residential',
    'DHW_occupancy_retailfood': 'DHW_occupancy_retailfood',
    'DHW_occupancy_retailother': 'DHW_occupancy_retailother',
    'DHW_occupancy_schoolprim': 'DHW_occupancy_schoolprim',
    'DHW_occupancy_schoolsec': 'DHW_occupancy_schoolsec',
    'DHW_storage_1_liter': 'DHW_storage_1_liter',
    'DHW_storage_2_liter': 'DHW_storage_2_liter',
    'DHW_storage_env_temp_default': 'DHW_storage_env_temp_default',
    'DHW_storage_liter_pPerson': 'DHW_storage_liter_pPerson',
    'DHW_thermal_power_1_kW': 'DHW_thermal_power_1_kW',
    'DHW_thermal_power_Wpl': 'DHW_thermal_power_Wpl',
    'DHW_thermal_power_pPerson': 'DHW_thermal_power_pPerson',
    'Daylightcoefficient_office': 'Daylightcoefficient_office',
    'Daylightcoefficient_schoolprim': 'Daylightcoefficient_schoolprim',
    'Daylightcoefficient_schoolsec': 'Daylightcoefficient_schoolsec',
    'EUI_auxiliary': 'EUI_auxiliary',
    'EUI_biomass': 'EUI_biomass',
    'EUI_district_heating': 'EUI_district_heating',
    'EUI_el_total': 'EUI_el_total',
    'EUI_lighting': 'EUI_lighting',
    'EUI_mob_fossil': 'EUI_mob_fossil',
    'EUI_mob_fossile': 'EUI_mob_fossile',
    'EUI_natural_gas': 'EUI_natural_gas',
    'EUI_other': 'EUI_other',
    'EUI_plugAuxLight': 'EUI_plugAuxLight',
    'EUI_plugloads': 'EUI_plugloads',
    'EUI_self_sufficiency': 'EUI_self_sufficiency',
    'EUIc_2th': 'EUIc_2th',
    'EUIc_el': 'EUIc_el',
    'EUIc_el_aux': 'EUIc_el_aux',
    'EUIc_other': 'EUIc_other',
    'EUIdhw_1th': 'EUIdhw_1th',
    'EUIdhw_2th': 'EUIdhw_2th',
    'EUIdhw_biomass': 'EUIdhw_biomass',
    'EUIdhw_district_heating': 'EUIdhw_district_heating',
    'EUIdhw_el': 'EUIdhw_el',
    'EUIdhw_natural_gas': 'EUIdhw_natural_gas',
    'EUIdhw_other': 'EUIdhw_other',
    'EUIdhwdirect_el': 'EUIdhwdirect_el',
    'EUIev_el': 'EUIev_el',
    'EUIev_el_total': 'EUIev_el_total',
    'EUIh_2th': 'EUIh_2th',
    'EUIh_4th': 'EUIh_4th',
    'EUIh_biomass': 'EUIh_biomass',
    'EUIh_district_heating': 'EUIh_district_heating',
    'EUIh_el': 'EUIh_el',
    'EUIh_el_aux': 'EUIh_el_aux',
    'EUIh_natural_gas': 'EUIh_natural_gas',
    'EUIh_other': 'EUIh_other',
    'EUIv_el': 'EUIv_el',
    'EV_FEC': 'EV_FEC',
    'EV_battsize_kWh': 'EV_battsize_kWh',
    'EV_charging_efficiency': 'EV_charging_efficiency',
    'EV_charging_losses_surcharge_factor': 'EV_charging_losses_surcharge_factor',
    'EV_charging_station_power': 'EV_charging_station_power',
    'EV_charging_stations': 'EV_charging_stations',
    'EV_count_residential': 'EV_count_residential',
    'EV_count_retail': 'EV_count_retail',
    'EV_count_work': 'EV_count_work',
    'EV_demand_kWhpkm': 'EV_demand_kWhpkm',
    'EV_experimental_calculation': 'EV_experimental_calculation',
    'EV_max_charging_power_ratio': 'EV_max_charging_power_ratio',
    'EV_mileage_res': 'EV_mileage_res',
    'EV_mileage_retail': 'EV_mileage_retail',
    'EV_mileage_work': 'EV_mileage_work',
    'EV_self_discharge_per_week': 'EV_self_discharge_per_week',
    'EV_selfdischarge_per_h': 'EV_selfdischarge_per_h',
    'EV_share': 'EV_share',
    'EV_share_constant_charging': 'EV_share_constant_charging',
    'EV_soc_min_discharge': 'EV_soc_min_discharge',
    'EV_soc_min_ext': 'EV_soc_min_ext',
    'EV_soc_min_retail': 'EV_soc_min_retail',
    'EV_soc_min_work': 'EV_soc_min_work',
    'EV_soc_minimum': 'EV_soc_minimum',
    'EV_storage_total_kWh': 'EV_storage_total_kWh',
    'Edhw_1_aux_el': 'Edhw_1_aux_el',
    'Edhw_1_el': 'Edhw_1_el',
    'Edhw_1_th': 'Edhw_1_th',
    'Edhw_2_aux_el': 'Edhw_2_aux_el',
    'Edhw_2_el': 'Edhw_2_el',
    'Edhw_2_th': 'Edhw_2_th',
    'Edhw_aux_el': 'Edhw_aux_el',
    'Edhw_el': 'Edhw_el',
    'Edhw_th': 'Edhw_th',
    'Eev_discharge_loss': 'Eev_discharge_loss',
    'Eev_ext_charge': 'Eev_ext_charge',
    'Eev_to_Ec_min': 'Eev_to_Ec_min',
    'Eev_to_Edhw_min': 'Eev_to_Edhw_min',
    'Eev_to_Eh_min': 'Eev_to_Eh_min',
    'Eev_to_Ev_min': 'Eev_to_Ev_min',
    'Eev_to_HVAC': 'Eev_to_HVAC',
    'Eev_to_district': 'Eev_to_district',
    'Eev_to_plugloads': 'Eev_to_plugloads',
    'Ev_scale_office': 'Ev_scale_office',
    'Ev_scale_other': 'Ev_scale_other',
    'Ev_scale_residential': 'Ev_scale_residential',
    'Ev_scale_retail_food': 'Ev_scale_retail_food',
    'Ev_scale_retail_other': 'Ev_scale_retail_other',
    'Ev_scale_school_prim': 'Ev_scale_school_prim',
    'Ev_scale_school_sec': 'Ev_scale_school_sec',
    'FLEX_PV_is_used': 'FLEX_PV_is_used',
    'FLEX_choice_cool_system': 'FLEX_choice_cool_system',
    'FLEX_choice_heat_system': 'FLEX_choice_heat_system',
    'FLEX_cool1_use': 'FLEX_cool1_use',
    'FLEX_cool3_use': 'FLEX_cool3_use',
    'FLEX_grid_maxpower_Wm2': 'FLEX_grid_maxpower_Wm2',
    'FLEX_heat1_use': 'FLEX_heat1_use',
    'FLEX_heat3_use': 'FLEX_heat3_use',
    'FLEX_is_used': 'FLEX_is_used',
    'FLEX_is_used_for_HVAC_min': 'FLEX_is_used_for_HVAC_min',
    'FLEX_is_used_for_ev_min': 'FLEX_is_used_for_ev_min',
    'FLEX_is_used_for_plugloads': 'FLEX_is_used_for_plugloads',
    'FLEX_signal_ID': 'FLEX_signal_ID',
    'FLEX_signal_name': 'FLEX_signal_name',
    'FSI': 'FSI',
    'GFA_office': 'GFA_office',
    'GFA_other': 'GFA_other',
    'GFA_residential': 'GFA_residential',
    'GFA_retailfood': 'GFA_retailfood',
    'GFA_retailother': 'GFA_retailother',
    'GFA_schoolprim': 'GFA_schoolprim',
    'GFA_schoolsec': 'GFA_schoolsec',
    'GFA_total': 'GFA_total',
    'GFV': 'GFV',
    'GHG_LCA_timeframe_years': 'GHG_LCA_timeframe_years',
    'GPW_ceilings_name': 'GPW_ceilings_name',
    'GWP_battery_name': 'GWP_battery_name',
    'GWP_boreholes_name': 'GWP_boreholes_name',
    'GWP_direct_biogenic': 'GWP_direct_biogenic',
    'GWP_direct_biogenic_share': 'GWP_direct_biogenic_share',
    'GWP_direct_fossile': 'GWP_direct_fossile',
    'GWP_direct_life': 'GWP_direct_life',
    'GWP_ee_ceilings_biogenic': 'GWP_ee_ceilings_biogenic',
    'GWP_ee_ceilings_fossile': 'GWP_ee_ceilings_fossile',
    'GWP_ee_con_build': 'GWP_ee_con_build',
    'GWP_ee_con_tga': 'GWP_ee_con_tga',
    'GWP_ee_direct_biogenic': 'GWP_ee_direct_biogenic',
    'GWP_ee_direct_fossile': 'GWP_ee_direct_fossile',
    'GWP_ee_general': 'GWP_ee_general',
    'GWP_ee_general_bigonenic': 'GWP_ee_general_bigonenic',
    'GWP_ee_general_fossile': 'GWP_ee_general_fossile',
    'GWP_ee_ground_biogenic': 'GWP_ee_ground_biogenic',
    'GWP_ee_ground_fossile': 'GWP_ee_ground_fossile',
    'GWP_ee_lc_battery': 'GWP_ee_lc_battery',
    'GWP_ee_lc_biogenic': 'GWP_ee_lc_biogenic',
    'GWP_ee_lc_boreholes': 'GWP_ee_lc_boreholes',
    'GWP_ee_lc_ceil': 'GWP_ee_lc_ceil',
    'GWP_ee_lc_ceilings_biogenic': 'GWP_ee_lc_ceilings_biogenic',
    'GWP_ee_lc_ceilings_fossile': 'GWP_ee_lc_ceilings_fossile',
    'GWP_ee_lc_construction': 'GWP_ee_lc_construction',
    'GWP_ee_lc_direct': 'GWP_ee_lc_direct',
    'GWP_ee_lc_direct_biogenic': 'GWP_ee_lc_direct_biogenic',
    'GWP_ee_lc_direct_fossile': 'GWP_ee_lc_direct_fossile',
    'GWP_ee_lc_fossil': 'GWP_ee_lc_fossil',
    'GWP_ee_lc_general_biogenic': 'GWP_ee_lc_general_biogenic',
    'GWP_ee_lc_general_fossile': 'GWP_ee_lc_general_fossile',
    'GWP_ee_lc_ground': 'GWP_ee_lc_ground',
    'GWP_ee_lc_ground_biogenic': 'GWP_ee_lc_ground_biogenic',
    'GWP_ee_lc_ground_fossile': 'GWP_ee_lc_ground_fossile',
    'GWP_ee_lc_mob': 'GWP_ee_lc_mob',
    'GWP_ee_lc_other': 'GWP_ee_lc_other',
    'GWP_ee_lc_other_biogenic': 'GWP_ee_lc_other_biogenic',
    'GWP_ee_lc_other_fossile': 'GWP_ee_lc_other_fossile',
    'GWP_ee_lc_pv': 'GWP_ee_lc_pv',
    'GWP_ee_lc_roof': 'GWP_ee_lc_roof',
    'GWP_ee_lc_roof_biogenic': 'GWP_ee_lc_roof_biogenic',
    'GWP_ee_lc_roof_fossile': 'GWP_ee_lc_roof_fossile',
    'GWP_ee_lc_solarthermal': 'GWP_ee_lc_solarthermal',
    'GWP_ee_lc_storage': 'GWP_ee_lc_storage',
    'GWP_ee_lc_tga': 'GWP_ee_lc_tga',
    'GWP_ee_lc_tga_general': 'GWP_ee_lc_tga_general',
    'GWP_ee_lc_tga_other': 'GWP_ee_lc_tga_other',
    'GWP_ee_lc_ventilation': 'GWP_ee_lc_ventilation',
    'GWP_ee_lc_walls': 'GWP_ee_lc_walls',
    'GWP_ee_lc_walls_biogenic': 'GWP_ee_lc_walls_biogenic',
    'GWP_ee_lc_walls_fossil': 'GWP_ee_lc_walls_fossil',
    'GWP_ee_lc_windows': 'GWP_ee_lc_windows',
    'GWP_ee_lc_windows_biogenic': 'GWP_ee_lc_windows_biogenic',
    'GWP_ee_lc_windows_fossile': 'GWP_ee_lc_windows_fossile',
    'GWP_ee_mob_ev': 'GWP_ee_mob_ev',
    'GWP_ee_mob_fossile': 'GWP_ee_mob_fossile',
    'GWP_ee_other_biogenic': 'GWP_ee_other_biogenic',
    'GWP_ee_other_fossile': 'GWP_ee_other_fossile',
    'GWP_ee_rep_build': 'GWP_ee_rep_build',
    'GWP_ee_rep_tga': 'GWP_ee_rep_tga',
    'GWP_ee_roof_biogenic': 'GWP_ee_roof_biogenic',
    'GWP_ee_roof_fossile': 'GWP_ee_roof_fossile',
    'GWP_ee_tga_battery_biogenic': 'GWP_ee_tga_battery_biogenic',
    'GWP_ee_tga_battery_fossile': 'GWP_ee_tga_battery_fossile',
    'GWP_ee_tga_boreholes_biogenic': 'GWP_ee_tga_boreholes_biogenic',
    'GWP_ee_tga_boreholes_fossile': 'GWP_ee_tga_boreholes_fossile',
    'GWP_ee_tga_general_biogenic': 'GWP_ee_tga_general_biogenic',
    'GWP_ee_tga_general_fossile': 'GWP_ee_tga_general_fossile',
    'GWP_ee_tga_other_biogenic': 'GWP_ee_tga_other_biogenic',
    'GWP_ee_tga_other_fossile': 'GWP_ee_tga_other_fossile',
    'GWP_ee_tga_pv_biogenic': 'GWP_ee_tga_pv_biogenic',
    'GWP_ee_tga_pv_fossile': 'GWP_ee_tga_pv_fossile',
    'GWP_ee_tga_solarthermal_biogenic': 'GWP_ee_tga_solarthermal_biogenic',
    'GWP_ee_tga_solarthermal_fossile': 'GWP_ee_tga_solarthermal_fossile',
    'GWP_ee_tga_storage_biogenic': 'GWP_ee_tga_storage_biogenic',
    'GWP_ee_tga_storage_fossile': 'GWP_ee_tga_storage_fossile',
    'GWP_ee_tga_ventilation_biogenic': 'GWP_ee_tga_ventilation_biogenic',
    'GWP_ee_tga_ventilation_fossile': 'GWP_ee_tga_ventilation_fossile',
    'GWP_ee_walls_biogenic': 'GWP_ee_walls_biogenic',
    'GWP_ee_walls_fossile': 'GWP_ee_walls_fossile',
    'GWP_ee_windows_bigenic': 'GWP_ee_windows_bigenic',
    'GWP_ee_windows_fossile': 'GWP_ee_windows_fossile',
    'GWP_emInt_PV_feedin': 'GWP_emInt_PV_feedin',
    'GWP_emInt_batt_charge': 'GWP_emInt_batt_charge',
    'GWP_emInt_ev_charge': 'GWP_emInt_ev_charge',
    'GWP_emInt_flex': 'GWP_emInt_flex',
    'GWP_emInt_grid': 'GWP_emInt_grid',
    'GWP_emInt_grid_avg': 'GWP_emInt_grid_avg',
    'GWP_general_name': 'GWP_general_name',
    'GWP_ground_name': 'GWP_ground_name',
    'GWP_lc_EE_total': 'GWP_lc_EE_total',
    'GWP_lc_OE_total': 'GWP_lc_OE_total',
    'GWP_lc_total': 'GWP_lc_total',
    'GWP_life_battery': 'GWP_life_battery',
    'GWP_life_ceilings': 'GWP_life_ceilings',
    'GWP_life_direct': 'GWP_life_direct',
    'GWP_life_general': 'GWP_life_general',
    'GWP_life_ground': 'GWP_life_ground',
    'GWP_life_other': 'GWP_life_other',
    'GWP_life_roof': 'GWP_life_roof',
    'GWP_life_solarthermal': 'GWP_life_solarthermal',
    'GWP_life_storage': 'GWP_life_storage',
    'GWP_life_tga_boreholes': 'GWP_life_tga_boreholes',
    'GWP_life_tga_general': 'GWP_life_tga_general',
    'GWP_life_tga_other': 'GWP_life_tga_other',
    'GWP_life_tga_pv': 'GWP_life_tga_pv',
    'GWP_life_tga_ventilation': 'GWP_life_tga_ventilation',
    'GWP_life_walls': 'GWP_life_walls',
    'GWP_life_windows': 'GWP_life_windows',
    'GWP_miv_count_ev': 'GWP_miv_count_ev',
    'GWP_miv_count_fossile': 'GWP_miv_count_fossile',
    'GWP_mobility_car_gpPKm': 'GWP_mobility_car_gpPKm',
    'GWP_mobility_construction_ev': 'GWP_mobility_construction_ev',
    'GWP_mobility_construction_fossil': 'GWP_mobility_construction_fossil',
    'GWP_mobility_moped_gpPKm': 'GWP_mobility_moped_gpPKm',
    'GWP_oe': 'GWP_oe',
    'GWP_oe_battery_charge': 'GWP_oe_battery_charge',
    'GWP_oe_biomass': 'GWP_oe_biomass',
    'GWP_oe_building': 'GWP_oe_building',
    'GWP_oe_district_heating': 'GWP_oe_district_heating',
    'GWP_oe_flex_build': 'GWP_oe_flex_build',
    'GWP_oe_grid_build': 'GWP_oe_grid_build',
    'GWP_oe_grid_feedin': 'GWP_oe_grid_feedin',
    'GWP_oe_lc_biomass': 'GWP_oe_lc_biomass',
    'GWP_oe_lc_building': 'GWP_oe_lc_building',
    'GWP_oe_lc_district_heating': 'GWP_oe_lc_district_heating',
    'GWP_oe_lc_emission': 'GWP_oe_lc_emission',
    'GWP_oe_lc_emission_savings': 'GWP_oe_lc_emission_savings',
    'GWP_oe_lc_flex_build': 'GWP_oe_lc_flex_build',
    'GWP_oe_lc_grid_build': 'GWP_oe_lc_grid_build',
    'GWP_oe_lc_grid_feedin': 'GWP_oe_lc_grid_feedin',
    'GWP_oe_lc_mob': 'GWP_oe_lc_mob',
    'GWP_oe_lc_mob_ev': 'GWP_oe_lc_mob_ev',
    'GWP_oe_lc_mob_export': 'GWP_oe_lc_mob_export',
    'GWP_oe_lc_mob_fossile': 'GWP_oe_lc_mob_fossile',
    'GWP_oe_lc_natural_gas': 'GWP_oe_lc_natural_gas',
    'GWP_oe_lc_other': 'GWP_oe_lc_other',
    'GWP_oe_mob': 'GWP_oe_mob',
    'GWP_oe_mob_ev': 'GWP_oe_mob_ev',
    'GWP_oe_mob_ev_export': 'GWP_oe_mob_ev_export',
    'GWP_oe_mob_fossile': 'GWP_oe_mob_fossile',
    'GWP_oe_natural_gas': 'GWP_oe_natural_gas',
    'GWP_oe_other': 'GWP_oe_other',
    'GWP_other_name': 'GWP_other_name',
    'GWP_pv_name': 'GWP_pv_name',
    'GWP_rcpi_biomass': 'GWP_rcpi_biomass',
    'GWP_rcpi_district_heating': 'GWP_rcpi_district_heating',
    'GWP_rcpi_fossil': 'GWP_rcpi_fossil',
    'GWP_rcpi_grid': 'GWP_rcpi_grid',
    'GWP_rcpi_grid_substition': 'GWP_rcpi_grid_substition',
    'GWP_rcpi_mob_fossile': 'GWP_rcpi_mob_fossile',
    'GWP_rcpi_natural_gas': 'GWP_rcpi_natural_gas',
    'GWP_rcpi_renewable': 'GWP_rcpi_renewable',
    'GWP_ref_area_ceilings': 'GWP_ref_area_ceilings',
    'GWP_ref_area_fundament': 'GWP_ref_area_fundament',
    'GWP_ref_area_roof': 'GWP_ref_area_roof',
    'GWP_ref_area_walls': 'GWP_ref_area_walls',
    'GWP_ref_area_windows': 'GWP_ref_area_windows',
    'GWP_refratio_boreholes': 'GWP_refratio_boreholes',
    'GWP_refratio_ceilings': 'GWP_refratio_ceilings',
    'GWP_refratio_fundament': 'GWP_refratio_fundament',
    'GWP_refratio_pv': 'GWP_refratio_pv',
    'GWP_refratio_roof': 'GWP_refratio_roof',
    'GWP_refratio_walls': 'GWP_refratio_walls',
    'GWP_refratio_windows': 'GWP_refratio_windows',
    'GWP_roof_name': 'GWP_roof_name',
    'GWP_solarthermal_name': 'GWP_solarthermal_name',
    'GWP_storage_name': 'GWP_storage_name',
    'GWP_tga_general_name': 'GWP_tga_general_name',
    'GWP_tga_other_name': 'GWP_tga_other_name',
    'GWP_ventilation_name': 'GWP_ventilation_name',
    'GWP_walls_name': 'GWP_walls_name',
    'Grid_to_Ec_min': 'Grid_to_Ec_min',
    'Grid_to_Edhw_min': 'Grid_to_Edhw_min',
    'Grid_to_Eev_min': 'Grid_to_Eev_min',
    'Grid_to_Eh_min': 'Grid_to_Eh_min',
    'Grid_to_Ev_min': 'Grid_to_Ev_min',
    'Grid_to_building_min': 'Grid_to_building_min',
    'Grid_to_min': 'Grid_to_min',
    'Grid_to_plugloads': 'Grid_to_plugloads',
    'Grid_total_flexandnotflex': 'Grid_total_flexandnotflex',
    'NFA_cooled': 'NFA_cooled',
    'NFA_mechvent': 'NFA_mechvent',
    'NFA_office': 'NFA_office',
    'NFA_other': 'NFA_other',
    'NFA_residential': 'NFA_residential',
    'NFA_retailfood': 'NFA_retailfood',
    'NFA_retailother': 'NFA_retailother',
    'NFA_schoolprim': 'NFA_schoolprim',
    'NFA_schoolsec': 'NFA_schoolsec',
    'NFA_to_GFA_ratio': 'NFA_to_GFA_ratio',
    'NFA_to_GFA_ratio_office': 'NFA_to_GFA_ratio_office',
    'NFA_to_GFA_ratio_other': 'NFA_to_GFA_ratio_other',
    'NFA_to_GFA_ratio_residential': 'NFA_to_GFA_ratio_residential',
    'NFA_to_GFA_ratio_retailfood': 'NFA_to_GFA_ratio_retailfood',
    'NFA_to_GFA_ratio_retailother': 'NFA_to_GFA_ratio_retailother',
    'NFA_to_GFA_ratio_schoolprim': 'NFA_to_GFA_ratio_schoolprim',
    'NFA_to_GFA_ratio_schoolsec': 'NFA_to_GFA_ratio_schoolsec',
    'NFA_total': 'NFA_total',
    'NFA_windowvent': 'NFA_windowvent',
    'NFAfrac_c': 'NFAfrac_c',
    'NFAfrac_u': 'NFAfrac_u',
    'NFV_c': 'NFV_c',
    'NFV_mechvent': 'NFV_mechvent',
    'NFV_total': 'NFV_total',
    'NFV_u': 'NFV_u',
    'NFV_windowvent': 'NFV_windowvent',
    'PEI_balance': 'PEI_balance',
    'PEI_biomass': 'PEI_biomass',
    'PEI_cf_density': 'PEI_cf_density',
    'PEI_cf_mobility': 'PEI_cf_mobility',
    'PEI_cf_renovation': 'PEI_cf_renovation',
    'PEI_demand': 'PEI_demand',
    'PEI_district_heating': 'PEI_district_heating',
    'PEI_el_hvac': 'PEI_el_hvac',
    'PEI_el_plugloads': 'PEI_el_plugloads',
    'PEI_evExtCharge_import': 'PEI_evExtCharge_import',
    'PEI_evOtherTravel_export': 'PEI_evOtherTravel_export',
    'PEI_export': 'PEI_export',
    'PEI_flex_import': 'PEI_flex_import',
    'PEI_grid_import': 'PEI_grid_import',
    'PEI_import': 'PEI_import',
    'PEI_importExport_balance': 'PEI_importExport_balance',
    'PEI_mob_el': 'PEI_mob_el',
    'PEI_mob_fossile': 'PEI_mob_fossile',
    'PEI_mob_total': 'PEI_mob_total',
    'PEI_natural_gas': 'PEI_natural_gas',
    'PEI_other': 'PEI_other',
    'PEI_pv_export': 'PEI_pv_export',
    'PEI_saldo_project': 'PEI_saldo_project',
    'PEI_saldo_target': 'PEI_saldo_target',
    'PEI_storage_losses': 'PEI_storage_losses',
    'PEI_sub_PV': 'PEI_sub_PV',
    'PEI_sub_flex': 'PEI_sub_flex',
    'PV_efficiency': 'PV_efficiency',
    'PV_id': 'PV_id',
    'PV_is_used': 'PV_is_used',
    'PV_kWp': 'PV_kWp',
    'PV_m2_per_kWp': 'PV_m2_per_kWp',
    'PV_module_area': 'PV_module_area',
    'PV_own_consumption': 'PV_own_consumption',
    'PV_own_consumption_direct': 'PV_own_consumption_direct',
    'PV_own_consumption_flex': 'PV_own_consumption_flex',
    'PV_profile_name': 'PV_profile_name',
    'PV_scale': 'PV_scale',
    'PV_to_Batt': 'PV_to_Batt',
    'PV_to_Ec_flex': 'PV_to_Ec_flex',
    'PV_to_Ec_min': 'PV_to_Ec_min',
    'PV_to_Edhw': 'PV_to_Edhw',
    'PV_to_Edhw_direct': 'PV_to_Edhw_direct',
    'PV_to_Edhw_min': 'PV_to_Edhw_min',
    'PV_to_Eev_flex': 'PV_to_Eev_flex',
    'PV_to_Eev_min': 'PV_to_Eev_min',
    'PV_to_Egrid': 'PV_to_Egrid',
    'PV_to_Eh_flex': 'PV_to_Eh_flex',
    'PV_to_Eh_min': 'PV_to_Eh_min',
    'PV_to_Ev_min': 'PV_to_Ev_min',
    'PV_to_plugloads': 'PV_to_plugloads',
    'PV_total': 'PV_total',
    'PV_total_direct': 'PV_total_direct',
    'PV_total_flex': 'PV_total_flex',
    'Plight_max_office': 'Plight_max_office',
    'Plight_max_schoolprim': 'Plight_max_schoolprim',
    'Plight_max_schoolsec': 'Plight_max_schoolsec',
    'Plight_min_office': 'Plight_min_office',
    'Plight_min_schoolprim': 'Plight_min_schoolprim',
    'Plight_min_schoolsec': 'Plight_min_schoolsec',
    'Plugloads_scale_office': 'Plugloads_scale_office',
    'Plugloads_scale_other': 'Plugloads_scale_other',
    'Plugloads_scale_res': 'Plugloads_scale_res',
    'Plugloads_scale_retailfood': 'Plugloads_scale_retailfood',
    'Plugloads_scale_retailother': 'Plugloads_scale_retailother',
    'Plugloads_scale_schoolprim': 'Plugloads_scale_schoolprim',
    'Plugloads_scale_schoolsec': 'Plugloads_scale_schoolsec',
    'QC': 'QC',
    'QC_aux_1el': 'QC_aux_1el',
    'QC_aux_2th': 'QC_aux_2th',
    'QC_aux_3el': 'QC_aux_3el',
    'QC_aux_fc': 'QC_aux_fc',
    'QC_c': 'QC_c',
    'QC_distr_losses_1el': 'QC_distr_losses_1el',
    'QC_distr_losses_2th': 'QC_distr_losses_2th',
    'QC_distr_losses_3el': 'QC_distr_losses_3el',
    'QC_flex_c': 'QC_flex_c',
    'QC_flex_summer': 'QC_flex_summer',
    'QC_flex_winter': 'QC_flex_winter',
    'QC_flexanteil': 'QC_flexanteil',
    'QC_flexshare_summer': 'QC_flexshare_summer',
    'QC_flexshare_winter': 'QC_flexshare_winter',
    'QC_generation_eff_2th': 'QC_generation_eff_2th',
    'QC_min_c': 'QC_min_c',
    'QC_min_summer': 'QC_min_summer',
    'QC_min_winter': 'QC_min_winter',
    'QC_summer': 'QC_summer',
    'QC_to_EC_1': 'QC_to_EC_1',
    'QC_to_EC_3': 'QC_to_EC_3',
    'QC_winter': 'QC_winter',
    'QCmax_1el': 'QCmax_1el',
    'QCmax_2th': 'QCmax_2th',
    'QCmax_3el': 'QCmax_3el',
    'QCmax_freecooling': 'QCmax_freecooling',
    'QCmax_room_MW': 'QCmax_room_MW',
    'QCmax_room_m2': 'QCmax_room_m2',
    'QH': 'QH',
    'QH_aux_el_to_th_1el': 'QH_aux_el_to_th_1el',
    'QH_aux_el_to_th_2th': 'QH_aux_el_to_th_2th',
    'QH_aux_el_to_th_3el': 'QH_aux_el_to_th_3el',
    'QH_aux_el_to_th_4th': 'QH_aux_el_to_th_4th',
    'QH_aux_wasteheat': 'QH_aux_wasteheat',
    'QH_c': 'QH_c',
    'QH_distr_loss_1el': 'QH_distr_loss_1el',
    'QH_distr_loss_2th': 'QH_distr_loss_2th',
    'QH_distr_loss_3el': 'QH_distr_loss_3el',
    'QH_distr_loss_4th': 'QH_distr_loss_4th',
    'QH_flex_c': 'QH_flex_c',
    'QH_flex_summer': 'QH_flex_summer',
    'QH_flex_u': 'QH_flex_u',
    'QH_flex_winter': 'QH_flex_winter',
    'QH_flexanteil_c': 'QH_flexanteil_c',
    'QH_flexanteil_u': 'QH_flexanteil_u',
    'QH_flexshare_summer': 'QH_flexshare_summer',
    'QH_flexshare_winter': 'QH_flexshare_winter',
    'QH_generation_eff_1el': 'QH_generation_eff_1el',
    'QH_generation_eff_2th': 'QH_generation_eff_2th',
    'QH_generation_eff_3el': 'QH_generation_eff_3el',
    'QH_generation_eff_4th': 'QH_generation_eff_4th',
    'QH_min_c': 'QH_min_c',
    'QH_min_summer': 'QH_min_summer',
    'QH_min_u': 'QH_min_u',
    'QH_min_winter': 'QH_min_winter',
    'QH_summer': 'QH_summer',
    'QH_u': 'QH_u',
    'QH_winter': 'QH_winter',
    'QHmax_1el_m2': 'QHmax_1el_m2',
    'QHmax_2th_m2': 'QHmax_2th_m2',
    'QHmax_3el_m2': 'QHmax_3el_m2',
    'QHmax_4th_m2': 'QHmax_4th_m2',
    'QHmax_room_MW': 'QHmax_room_MW',
    'QHmax_room_m²': 'QHmax_room_m',
    'QI': 'QI',
    'QI_c': 'QI_c',
    'QI_summer': 'QI_summer',
    'QI_u': 'QI_u',
    'QI_winter': 'QI_winter',
    'QS': 'QS',
    'QS_c': 'QS_c',
    'QS_max_shading_c': 'QS_max_shading_c',
    'QS_max_shading_u': 'QS_max_shading_u',
    'QS_summer': 'QS_summer',
    'QS_u': 'QS_u',
    'QS_winter': 'QS_winter',
    'QT': 'QT',
    'QT_c': 'QT_c',
    'QT_ground_c': 'QT_ground_c',
    'QT_ground_summer': 'QT_ground_summer',
    'QT_ground_u': 'QT_ground_u',
    'QT_ground_winter': 'QT_ground_winter',
    'QT_psi_c': 'QT_psi_c',
    'QT_psi_summer': 'QT_psi_summer',
    'QT_psi_u': 'QT_psi_u',
    'QT_psi_winter': 'QT_psi_winter',
    'QT_roof_c': 'QT_roof_c',
    'QT_roof_summer': 'QT_roof_summer',
    'QT_roof_u': 'QT_roof_u',
    'QT_roof_winter': 'QT_roof_winter',
    'QT_summer': 'QT_summer',
    'QT_u': 'QT_u',
    'QT_wall_c': 'QT_wall_c',
    'QT_wall_summer': 'QT_wall_summer',
    'QT_wall_u': 'QT_wall_u',
    'QT_wall_winter': 'QT_wall_winter',
    'QT_window_c': 'QT_window_c',
    'QT_window_summer': 'QT_window_summer',
    'QT_window_u': 'QT_window_u',
    'QT_window_winter': 'QT_window_winter',
    'QT_winter': 'QT_winter',
    'QV': 'QV',
    'QV_c': 'QV_c',
    'QV_heatrecovery': 'QV_heatrecovery',
    'QV_heatrecovery_c': 'QV_heatrecovery_c',
    'QV_heatrecovery_summer': 'QV_heatrecovery_summer',
    'QV_heatrecovery_u': 'QV_heatrecovery_u',
    'QV_heatrecovery_winter': 'QV_heatrecovery_winter',
    'QV_inf_c': 'QV_inf_c',
    'QV_inf_summer': 'QV_inf_summer',
    'QV_inf_u': 'QV_inf_u',
    'QV_inf_winter': 'QV_inf_winter',
    'QV_mechvent_c': 'QV_mechvent_c',
    'QV_mechvent_summer': 'QV_mechvent_summer',
    'QV_mechvent_u': 'QV_mechvent_u',
    'QV_mechvent_winter': 'QV_mechvent_winter',
    'QV_summer': 'QV_summer',
    'QV_u': 'QV_u',
    'QV_window_c': 'QV_window_c',
    'QV_window_summer': 'QV_window_summer',
    'QV_window_u': 'QV_window_u',
    'QV_window_winter': 'QV_window_winter',
    'QV_winter': 'QV_winter',
    'QVn': 'QVn',
    'QVn_c': 'QVn_c',
    'QVn_summer': 'QVn_summer',
    'QVn_u': 'QVn_u',
    'QVn_winter': 'QVn_winter',
    'StatPAX': 'StatPAX',
    'StatPAX_eduprim': 'StatPAX_eduprim',
    'StatPAX_edusec': 'StatPAX_edusec',
    'StatPAX_office': 'StatPAX_office',
    'StatPAX_res': 'StatPAX_res',
    'StatPAX_retail': 'StatPAX_retail',
    'StatPAX_retailother': 'StatPAX_retailother',
    'Ta_annual_avg': 'Ta_annual_avg',
    'Ta_avg_cooling_period': 'Ta_avg_cooling_period',
    'Ta_avg_heating_period': 'Ta_avg_heating_period',
    'Tc_avg_summer': 'Tc_avg_summer',
    'Tc_avg_winter': 'Tc_avg_winter',
    'Tsetcool_flex': 'Tsetcool_flex',
    'Tsetcool_max': 'Tsetcool_max',
    'Tsetheat_flex': 'Tsetheat_flex',
    'Tsetheat_min': 'Tsetheat_min',
    'Tu_avg_summer': 'Tu_avg_summer',
    'Tu_avg_winter': 'Tu_avg_winter',
    'UED_auxiliary': 'UED_auxiliary',
    'UED_cooling': 'UED_cooling',
    'UED_dhw': 'UED_dhw',
    'UED_heating': 'UED_heating',
    'UED_lighting': 'UED_lighting',
    'UED_mim_electric': 'UED_mim_electric',
    'UED_mim_fossile': 'UED_mim_fossile',
    'UED_mob_el_other': 'UED_mob_el_other',
    'UED_mob_el_target': 'UED_mob_el_target',
    'UED_mob_el_total': 'UED_mob_el_total',
    'UED_plugloads': 'UED_plugloads',
    'UED_ventilation': 'UED_ventilation',
    'VRGrid_to_Batt': 'VRGrid_to_Batt',
    'VRGrid_to_Ec_flex': 'VRGrid_to_Ec_flex',
    'VRGrid_to_Ec_min': 'VRGrid_to_Ec_min',
    'VRGrid_to_Edhw_flex': 'VRGrid_to_Edhw_flex',
    'VRGrid_to_Edhw_min': 'VRGrid_to_Edhw_min',
    'VRGrid_to_Eev_flex': 'VRGrid_to_Eev_flex',
    'VRGrid_to_Eev_min': 'VRGrid_to_Eev_min',
    'VRGrid_to_Eh_flex': 'VRGrid_to_Eh_flex',
    'VRGrid_to_Eh_min': 'VRGrid_to_Eh_min',
    'VRGrid_to_Ev_min': 'VRGrid_to_Ev_min',
    'VRGrid_to_building': 'VRGrid_to_building',
    'VRGrid_to_flex': 'VRGrid_to_flex',
    'VRGrid_to_min': 'VRGrid_to_min',
    'VRGrid_to_plugloads': 'VRGrid_to_plugloads',
    'Vent_share_mech_cooled': 'Vent_share_mech_cooled',
    'Vent_share_mech_uncooled': 'Vent_share_mech_uncooled',
    'Vent_share_window_cooled': 'Vent_share_window_cooled',
    'Vent_share_window_uncooled': 'Vent_share_window_uncooled',
    'aux_el_demand_office_kWhm2': 'aux_el_demand_office_kWhm2',
    'aux_el_demand_other_kWhm2': 'aux_el_demand_other_kWhm2',
    'aux_el_demand_residential_kWhm2': 'aux_el_demand_residential_kWhm2',
    'aux_el_demand_retailfood_kWhm2': 'aux_el_demand_retailfood_kWhm2',
    'aux_el_demand_retailother_kWhm2': 'aux_el_demand_retailother_kWhm2',
    'aux_el_demand_schoolprim_kWhm2': 'aux_el_demand_schoolprim_kWhm2',
    'aux_el_demand_schoolsec_kWhm2': 'aux_el_demand_schoolsec_kWhm2',
    'borehole_count': 'borehole_count',
    'building_count': 'building_count',
    'cfd_A': 'cfd_A',
    'cfd_EUI': 'cfd_EUI',
    'cfd_cutoff': 'cfd_cutoff',
    'cfd_dx': 'cfd_dx',
    'cfd_fPE': 'cfd_fPE',
    'cfm_budget_office': 'cfm_budget_office',
    'cfm_budget_residential': 'cfm_budget_residential',
    'cfm_budget_retail': 'cfm_budget_retail',
    'cfm_budget_school': 'cfm_budget_school',
    'cfr_budget': 'cfr_budget',
    'context_factor_density': 'context_factor_density',
    'context_factor_mobility': 'context_factor_mobility',
    'context_factor_renovation': 'context_factor_renovation',
    'cool_cop_1el': 'cool_cop_1el',
    'cool_cop_2th': 'cool_cop_2th',
    'cool_cop_3el': 'cool_cop_3el',
    'cool_share_office': 'cool_share_office',
    'cool_share_other': 'cool_share_other',
    'cool_share_residential': 'cool_share_residential',
    'cool_share_retailfood': 'cool_share_retailfood',
    'cool_share_retailother': 'cool_share_retailother',
    'cool_share_schoolprim': 'cool_share_schoolprim',
    'cool_share_schoolsec': 'cool_share_schoolsec',
    'cool_th2_carrier_type': 'cool_th2_carrier_type',
    'cool_th2_is_bio': 'cool_th2_is_bio',
    'cool_th2_is_dh': 'cool_th2_is_dh',
    'cool_th2_is_ng': 'cool_th2_is_ng',
    'cool_th2_is_other': 'cool_th2_is_other',
    'cooling_month1': 'cooling_month1',
    'cooling_month10': 'cooling_month10',
    'cooling_month11': 'cooling_month11',
    'cooling_month12': 'cooling_month12',
    'cooling_month2': 'cooling_month2',
    'cooling_month3': 'cooling_month3',
    'cooling_month4': 'cooling_month4',
    'cooling_month5': 'cooling_month5',
    'cooling_month6': 'cooling_month6',
    'cooling_month7': 'cooling_month7',
    'cooling_month8': 'cooling_month8',
    'cooling_month9': 'cooling_month9',
    'cost_E_grid': 'cost_E_grid',
    'cost_PV_to_Egrid': 'cost_PV_to_Egrid',
    'cost_VRGrid_flex': 'cost_VRGrid_flex',
    'cost_total': 'cost_total',
    'dTc_summer': 'dTc_summer',
    'dTc_winter': 'dTc_winter',
    'dTu_summer': 'dTu_summer',
    'dTu_winter': 'dTu_winter',
    'daylightcontr_office': 'daylightcontr_office',
    'daylightcontr_schoolprim': 'daylightcontr_schoolprim',
    'daylightcontr_schoolsec': 'daylightcontr_schoolsec',
    'density_NFApPers_edu': 'density_NFApPers_edu',
    'density_NFApPers_edu_rpim': 'density_NFApPers_edu_rpim',
    'density_NFApPers_office': 'density_NFApPers_office',
    'density_NFApPers_residential': 'density_NFApPers_residential',
    'density_NFApPers_retail': 'density_NFApPers_retail',
    'density_NFApPers_retail_other': 'density_NFApPers_retail_other',
    'dhw1_is_bio': 'dhw1_is_bio',
    'dhw1_is_dh': 'dhw1_is_dh',
    'dhw1_is_ng': 'dhw1_is_ng',
    'dhw1_is_other': 'dhw1_is_other',
    'dhw2_is_bio': 'dhw2_is_bio',
    'dhw2_is_dh': 'dhw2_is_dh',
    'dhw2_is_ng': 'dhw2_is_ng',
    'dhw2_is_other': 'dhw2_is_other',
    'district_heating_conversion_profile': 'district_heating_conversion_profile',
    'e_kWhm2a': 'e_kWhm2a',
    'ev_bidirectional_use': 'ev_bidirectional_use',
    'fGHG_grid_column': 'fGHG_grid_column',
    'fGHG_grid_profile': 'fGHG_grid_profile',
    'fPE_eff': 'fPE_eff',
    'fPE_flex_factor': 'fPE_flex_factor',
    'fPE_grid': 'fPE_grid',
    'fPE_grid_column': 'fPE_grid_column',
    'fPE_grid_profile': 'fPE_grid_profile',
    'fc_c': 'fc_c',
    'fc_eduprim': 'fc_eduprim',
    'fc_edusec': 'fc_edusec',
    'fc_office': 'fc_office',
    'fc_other': 'fc_other',
    'fc_residential': 'fc_residential',
    'fc_retailfood': 'fc_retailfood',
    'fc_retailother': 'fc_retailother',
    'fc_u': 'fc_u',
    'flex_GSR': 'flex_GSR',
    'flex_GSRI': 'flex_GSRI',
    'flex_GSRU': 'flex_GSRU',
    'flex_Signals_selected_column': 'flex_Signals_selected_column',
    'flex_cool_dT': 'flex_cool_dT',
    'flex_dhw_use': 'flex_dhw_use',
    'flex_heat_dT': 'flex_heat_dT',
    'flex_signal_ratio': 'flex_signal_ratio',
    'flex_signal_ratio_summer': 'flex_signal_ratio_summer',
    'flex_signal_ratio_winter': 'flex_signal_ratio_winter',
    'fossile_demand_kWhpkm': 'fossile_demand_kWhpkm',
    'grid_rcp1': 'grid_rcp1',
    'grid_rcp2': 'grid_rcp2',
    'grid_rcp3': 'grid_rcp3',
    'heat_cap_eff_cooled_m2': 'heat_cap_eff_cooled_m2',
    'heat_cap_eff_uncooled_m2': 'heat_cap_eff_uncooled_m2',
    'heat_capacity_effective_m²': 'heat_capacity_effective_m',
    'heat_cop_1el': 'heat_cop_1el',
    'heat_cop_2th': 'heat_cop_2th',
    'heat_cop_3el': 'heat_cop_3el',
    'heat_cop_4th': 'heat_cop_4th',
    'heat_th2_carrier_type': 'heat_th2_carrier_type',
    'heat_th2_is_bio': 'heat_th2_is_bio',
    'heat_th2_is_dh': 'heat_th2_is_dh',
    'heat_th2_is_ng': 'heat_th2_is_ng',
    'heat_th2_is_other': 'heat_th2_is_other',
    'heat_th4_carrier_type': 'heat_th4_carrier_type',
    'heat_th4_is_bio': 'heat_th4_is_bio',
    'heat_th4_is_dh': 'heat_th4_is_dh',
    'heat_th4_is_ng': 'heat_th4_is_ng',
    'heat_th4_is_other': 'heat_th4_is_other',
    'heating_month1': 'heating_month1',
    'heating_month10': 'heating_month10',
    'heating_month11': 'heating_month11',
    'heating_month12': 'heating_month12',
    'heating_month2': 'heating_month2',
    'heating_month3': 'heating_month3',
    'heating_month4': 'heating_month4',
    'heating_month5': 'heating_month5',
    'heating_month6': 'heating_month6',
    'heating_month7': 'heating_month7',
    'heating_month8': 'heating_month8',
    'heating_month9': 'heating_month9',
    'hull_ext_wall_wo_window_m2': 'hull_ext_wall_wo_window_m2',
    'hull_fenestration_rate': 'hull_fenestration_rate',
    'hull_fundament_m2': 'hull_fundament_m2',
    'hull_m2': 'hull_m2',
    'hull_roof_m2': 'hull_roof_m2',
    'hull_transmittance_fundament': 'hull_transmittance_fundament',
    'hull_transmittance_heatbridge': 'hull_transmittance_heatbridge',
    'hull_transmittance_roof': 'hull_transmittance_roof',
    'hull_transmittance_walls': 'hull_transmittance_walls',
    'hull_transmittance_windows_east': 'hull_transmittance_windows_east',
    'hull_transmittance_windows_horizontal': 'hull_transmittance_windows_horizontal',
    'hull_transmittance_windows_north': 'hull_transmittance_windows_north',
    'hull_transmittance_windows_south': 'hull_transmittance_windows_south',
    'hull_transmittance_windows_west': 'hull_transmittance_windows_west',
    'hull_window_m2': 'hull_window_m2',
    'hull_windows_east_m2': 'hull_windows_east_m2',
    'hull_windows_horizontal_m2': 'hull_windows_horizontal_m2',
    'hull_windows_north_m2': 'hull_windows_north_m2',
    'hull_windows_south_m2': 'hull_windows_south_m2',
    'hull_windows_west_m2': 'hull_windows_west_m2',
    'illuminance_efficiency_dirt': 'illuminance_efficiency_dirt',
    'illuminance_efficiency_glazing_ratio': 'illuminance_efficiency_glazing_ratio',
    'illuminance_min_office': 'illuminance_min_office',
    'illuminance_min_other': 'illuminance_min_other',
    'illuminance_min_residential': 'illuminance_min_residential',
    'illuminance_min_retailfood': 'illuminance_min_retailfood',
    'illuminance_min_retailother': 'illuminance_min_retailother',
    'illuminance_min_schoolprim': 'illuminance_min_schoolprim',
    'illuminance_min_schoolsec': 'illuminance_min_schoolsec',
    'input_version_date': 'input_version_date',
    'input_version_number': 'input_version_number',
    'irradiation_opaque_surcharge': 'irradiation_opaque_surcharge',
    'lc': 'lc',
    'lighting_factor_office': 'lighting_factor_office',
    'lighting_factor_other': 'lighting_factor_other',
    'lighting_factor_retailfood': 'lighting_factor_retailfood',
    'lighting_factor_retailother': 'lighting_factor_retailother',
    'lighting_factor_schoolprim': 'lighting_factor_schoolprim',
    'lighting_factor_schoolsec': 'lighting_factor_schoolsec',
    'location_address': 'location_address',
    'location_postcode': 'location_postcode',
    'mob_annual_milage_district': 'mob_annual_milage_district',
    'mob_annual_mileage_PAX': 'mob_annual_mileage_PAX',
    'mob_motorization_perNFA_residential': 'mob_motorization_perNFA_residential',
    'mob_motorization_perNFA_retail': 'mob_motorization_perNFA_retail',
    'mob_motorization_perNFA_work': 'mob_motorization_perNFA_work',
    'mob_pkm_factor': 'mob_pkm_factor',
    'mob_shading_factor_c': 'mob_shading_factor_c',
    'mob_shading_factor_u': 'mob_shading_factor_u',
    'mob_simultaneity_edu': 'mob_simultaneity_edu',
    'mob_simultaneity_office': 'mob_simultaneity_office',
    'mob_simultaneity_retail': 'mob_simultaneity_retail',
    'mobility_is_included': 'mobility_is_included',
    'mobility_mode': 'mobility_mode',
    'mobility_region': 'mobility_region',
    'mobility_vehicle_count': 'mobility_vehicle_count',
    'mobshare_office': 'mobshare_office',
    'mobshare_residential': 'mobshare_residential',
    'mobshare_retail': 'mobshare_retail',
    'mobshare_school': 'mobshare_school',
    'moped_factor': 'moped_factor',
    'municipality_name': 'municipality_name',
    'pe_conversion_factor_gasoline': 'pe_conversion_factor_gasoline',
    'per_NFA': 'per_NFA',
    'pkm_bike': 'pkm_bike',
    'pkm_bus': 'pkm_bus',
    'pkm_car_driver': 'pkm_car_driver',
    'pkm_car_passenger': 'pkm_car_passenger',
    'pkm_distancebus': 'pkm_distancebus',
    'pkm_mofa': 'pkm_mofa',
    'pkm_pedestrian': 'pkm_pedestrian',
    'pkm_train': 'pkm_train',
    'pkm_tram_metro': 'pkm_tram_metro',
    'plot_area': 'plot_area',
    'project_creation_date': 'project_creation_date',
    'project_description': 'project_description',
    'project_name': 'project_name',
    'project_scenario_name': 'project_scenario_name',
    'project_url': 'project_url',
    'rcp1_dh': 'rcp1_dh',
    'rcp1_fossil': 'rcp1_fossil',
    'rcp1_renewable': 'rcp1_renewable',
    'rcp2_dh': 'rcp2_dh',
    'rcp2_fossil': 'rcp2_fossil',
    'rcp2_renewable': 'rcp2_renewable',
    'rcp3_dh': 'rcp3_dh',
    'rcp3_fossil': 'rcp3_fossil',
    'rcp3_renewable': 'rcp3_renewable',
    'renovation_ratio_office': 'renovation_ratio_office',
    'renovation_ratio_other': 'renovation_ratio_other',
    'renovation_ratio_residential': 'renovation_ratio_residential',
    'renovation_ratio_retailfood': 'renovation_ratio_retailfood',
    'renovation_ratio_retailother': 'renovation_ratio_retailother',
    'renovation_ratio_schoolprim': 'renovation_ratio_schoolprim',
    'renovation_ratio_schoolsec': 'renovation_ratio_schoolsec',
    'renovation_share': 'renovation_share',
    'rh_avg': 'rh_avg',
    'rh_ceiling': 'rh_ceiling',
    'rh_office': 'rh_office',
    'rh_other': 'rh_other',
    'rh_residential': 'rh_residential',
    'rh_retailfood': 'rh_retailfood',
    'rh_retailother': 'rh_retailother',
    'rh_schoolprim': 'rh_schoolprim',
    'rh_schoolsec': 'rh_schoolsec',
    'scenario_version': 'scenario_version',
    'storey_count_avg': 'storey_count_avg',
    'test_NFV_shares': 'test_NFV_shares',
    'test_heat_balance': 'test_heat_balance',
    'transmittance_MW': 'transmittance_MW',
    'transmittance_Wm²': 'transmittance_Wm',
    'usage_concurrency_summer_eduprim': 'usage_concurrency_summer_eduprim',
    'usage_concurrency_summer_edusec': 'usage_concurrency_summer_edusec',
    'usage_concurrency_summer_office': 'usage_concurrency_summer_office',
    'usage_concurrency_summer_other': 'usage_concurrency_summer_other',
    'usage_concurrency_summer_res': 'usage_concurrency_summer_res',
    'usage_concurrency_summer_retailfood': 'usage_concurrency_summer_retailfood',
    'usage_concurrency_summer_retailother': 'usage_concurrency_summer_retailother',
    'usage_concurrency_winter_eduprim': 'usage_concurrency_winter_eduprim',
    'usage_concurrency_winter_edusec': 'usage_concurrency_winter_edusec',
    'usage_concurrency_winter_office': 'usage_concurrency_winter_office',
    'usage_concurrency_winter_other': 'usage_concurrency_winter_other',
    'usage_concurrency_winter_res': 'usage_concurrency_winter_res',
    'usage_concurrency_winter_retailfood': 'usage_concurrency_winter_retailfood',
    'usage_concurrency_winter_retailother': 'usage_concurrency_winter_retailother',
    'vent_ach_max_office': 'vent_ach_max_office',
    'vent_ach_max_other': 'vent_ach_max_other',
    'vent_ach_max_residential': 'vent_ach_max_residential',
    'vent_ach_max_retailfood': 'vent_ach_max_retailfood',
    'vent_ach_max_retailother': 'vent_ach_max_retailother',
    'vent_ach_max_schoolprim': 'vent_ach_max_schoolprim',
    'vent_ach_max_schoolsec': 'vent_ach_max_schoolsec',
    'vent_air_tightness': 'vent_air_tightness',
    'vent_heat_recovery_summer_office': 'vent_heat_recovery_summer_office',
    'vent_heat_recovery_summer_other': 'vent_heat_recovery_summer_other',
    'vent_heat_recovery_summer_residential': 'vent_heat_recovery_summer_residential',
    'vent_heat_recovery_summer_retailfood': 'vent_heat_recovery_summer_retailfood',
    'vent_heat_recovery_summer_retailother': 'vent_heat_recovery_summer_retailother',
    'vent_heat_recovery_summer_schoolprim': 'vent_heat_recovery_summer_schoolprim',
    'vent_heat_recovery_summer_schoolsec': 'vent_heat_recovery_summer_schoolsec',
    'vent_heat_recovery_winter_office': 'vent_heat_recovery_winter_office',
    'vent_heat_recovery_winter_other': 'vent_heat_recovery_winter_other',
    'vent_heat_recovery_winter_residential': 'vent_heat_recovery_winter_residential',
    'vent_heat_recovery_winter_retailfood': 'vent_heat_recovery_winter_retailfood',
    'vent_heat_recovery_winter_retailother': 'vent_heat_recovery_winter_retailother',
    'vent_heat_recovery_winter_schoolprim': 'vent_heat_recovery_winter_schoolprim',
    'vent_heat_recovery_winter_schoolsec': 'vent_heat_recovery_winter_schoolsec',
    'vent_infiltration_ACH': 'vent_infiltration_ACH',
    'vent_night_office': 'vent_night_office',
    'vent_night_other': 'vent_night_other',
    'vent_night_residential': 'vent_night_residential',
    'vent_night_retailfood': 'vent_night_retailfood',
    'vent_night_retailother': 'vent_night_retailother',
    'vent_night_schoolprim': 'vent_night_schoolprim',
    'vent_night_schoolsec': 'vent_night_schoolsec',
    'vent_scale_office': 'vent_scale_office',
    'vent_scale_other': 'vent_scale_other',
    'vent_scale_residential': 'vent_scale_residential',
    'vent_scale_retail': 'vent_scale_retail',
    'vent_scale_school_prim': 'vent_scale_school_prim',
    'vent_scale_school_sec': 'vent_scale_school_sec',
    'vent_scale_supermarket': 'vent_scale_supermarket',
    'vent_share_mechanical_office': 'vent_share_mechanical_office',
    'vent_share_mechanical_other': 'vent_share_mechanical_other',
    'vent_share_mechanical_residential': 'vent_share_mechanical_residential',
    'vent_share_mechanical_retailfood': 'vent_share_mechanical_retailfood',
    'vent_share_mechanical_retailother': 'vent_share_mechanical_retailother',
    'vent_share_mechanical_schoolprim': 'vent_share_mechanical_schoolprim',
    'vent_share_mechanical_schoolsec': 'vent_share_mechanical_schoolsec',
    'vent_tightness_ratio_blowerdoor_to_real': 'vent_tightness_ratio_blowerdoor_to_real',
    'weather_index': 'weather_index',
    'weather_name': 'weather_name',
    'window_irradiation_factor_summer_east': 'window_irradiation_factor_summer_east',
    'window_irradiation_factor_summer_horizontal': 'window_irradiation_factor_summer_horizontal',
    'window_irradiation_factor_summer_north': 'window_irradiation_factor_summer_north',
    'window_irradiation_factor_summer_south': 'window_irradiation_factor_summer_south',
    'window_irradiation_factor_summer_west': 'window_irradiation_factor_summer_west',
    'window_irradiation_factor_winter_east': 'window_irradiation_factor_winter_east',
    'window_irradiation_factor_winter_horizontal': 'window_irradiation_factor_winter_horizontal',
    'window_irradiation_factor_winter_north': 'window_irradiation_factor_winter_north',
    'window_irradiation_factor_winter_south': 'window_irradiation_factor_winter_south',
    'window_irradiation_factor_winter_west': 'window_irradiation_factor_winter_west',
    'window_total_transmittance_east': 'window_total_transmittance_east',
    'window_total_transmittance_horizontal': 'window_total_transmittance_horizontal',
    'window_total_transmittance_north': 'window_total_transmittance_north',
    'window_total_transmittance_south': 'window_total_transmittance_south',
    'window_total_transmittance_west': 'window_total_transmittance_west',
    'year_rcp0': 'year_rcp0',
    'year_rcp1': 'year_rcp1',
    'year_rcp2': 'year_rcp2',
    'year_rcp3': 'year_rcp3',
}

def fill_values(vars_obj: Vars, data: dict[str, object], attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> None:
    for var_name, value in data.items():
        attr_name = attr_name_map.get(var_name)
        if attr_name is not None:
            setattr(vars_obj, attr_name, value)


def vars_to_dict(vars_obj: Vars, attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> dict[str, object]:
    out: dict[str, object] = {}
    for var_name, attr_name in attr_name_map.items():
        out[var_name] = getattr(vars_obj, attr_name)
    return out

