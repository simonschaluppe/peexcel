# Schema Diff

- **Old:** `data\schemas\dev`
- **New:** `data\schemas\dev2`
- **Key:** `var_name`

## IN

### Columns
- Added: []
- Removed: ['bind_type']
- Common count: 8

### Rows
- Old count: 417
- New count: 579
- var_name added: ['ACH_night_m³', 'Batt_auto_discharge_factor', 'Batt_cap_Wh_per_NFA', 'Batt_max_power_specific', 'DHW_1_incl_distribution_factor', 'DHW_1_is_electric', 'DHW_1_is_used', 'DHW_2_incl_distribution_factor', 'DHW_2_is_electric', 'DHW_2_is_used', 'DHW_Tmax', 'DHW_conversion_1', 'DHW_conversion_2', 'DHW_storage_1_liter', 'DHW_storage_2_liter', 'DHW_thermal_power_1_kW', 'DHW_thermal_power_Wpl', 'EV_charging_losses_surcharge_factor', 'EV_count_residential', 'EV_count_retail', 'EV_count_work', 'EV_mileage_res', 'EV_mileage_retail', 'EV_mileage_work', 'EV_selfdischarge_per_h', 'EV_storage_total_kWh', 'FLEX_cool1_use', 'FLEX_cool3_use', 'FLEX_heat1_use', 'FLEX_heat3_use', 'FLEX_signal_ID', 'FSI', 'GFA_total', 'GFV', 'GWP_direct_biogenic', 'GWP_direct_biogenic_share', 'GWP_direct_fossile', 'GWP_direct_life', 'GWP_miv_count_ev', 'GWP_miv_count_fossile', 'GWP_rcpi_biomass', 'GWP_rcpi_district_heating', 'GWP_rcpi_fossil', 'GWP_rcpi_grid', 'GWP_rcpi_grid_substition', 'GWP_rcpi_mob_fossile', 'GWP_rcpi_natural_gas', 'GWP_rcpi_renewable', 'GWP_refratio_boreholes', 'GWP_refratio_ceilings', 'GWP_refratio_fundament', 'GWP_refratio_pv', 'GWP_refratio_roof', 'GWP_refratio_walls', 'GWP_refratio_windows', 'NFA_cooled', 'NFA_mechvent', 'NFA_office', 'NFA_other', 'NFA_residential', 'NFA_retailfood', 'NFA_retailother', 'NFA_schoolprim', 'NFA_schoolsec', 'NFA_to_GFA_ratio', 'NFA_total', 'NFA_windowvent', 'NFAfrac_c', 'NFAfrac_u', 'NFV_c', 'NFV_mechvent', 'NFV_total', 'NFV_u', 'NFV_windowvent', 'PV_id', 'PV_kWp', 'PV_module_area', 'QC_generation_eff_2th', 'QC_to_EC_1', 'QC_to_EC_3', 'QCmax_room_MW', 'QH_generation_eff_1el', 'QH_generation_eff_2th', 'QH_generation_eff_3el', 'QH_generation_eff_4th', 'QHmax_room_MW', 'QS_max_shading_c', 'QS_max_shading_u', 'StatPAX_eduprim', 'StatPAX_edusec', 'StatPAX_office', 'StatPAX_res', 'StatPAX_retail', 'StatPAX_retailother', 'Tsetcool_flex', 'Tsetheat_flex', 'Vent_share_mech_cooled', 'Vent_share_mech_uncooled', 'Vent_share_window_cooled', 'Vent_share_window_uncooled', 'cool_th2_is_bio', 'cool_th2_is_dh', 'cool_th2_is_ng', 'cool_th2_is_other', 'dhw1_is_bio', 'dhw1_is_dh', 'dhw1_is_ng', 'dhw1_is_other', 'dhw2_is_bio', 'dhw2_is_dh', 'dhw2_is_ng', 'dhw2_is_other', 'fGHG_grid_column', 'fPE_grid_column', 'fc_c', 'fc_u', 'flex_Signals_selected_column', 'ghg_conversion_factor_gasoline', 'heat_cap_eff_cooled_m2', 'heat_cap_eff_uncooled_m2', 'heat_th2_is_bio', 'heat_th2_is_dh', 'heat_th2_is_ng', 'heat_th2_is_other', 'heat_th4_is_bio', 'heat_th4_is_dh', 'heat_th4_is_ng', 'heat_th4_is_other', 'hull_fenestration_rate', 'hull_m2', 'hull_window_m2', 'lc', 'mob_shading_factor_c', 'mob_shading_factor_u', 'mobility_region', 'mobshare_office', 'mobshare_residential', 'mobshare_retail', 'mobshare_school', 'per_NFA', 'pkm_bike', 'pkm_bus', 'pkm_car_driver', 'pkm_car_passenger', 'pkm_distancebus', 'pkm_mofa', 'pkm_pedestrian', 'pkm_train', 'pkm_tram_metro', 'rcp1_dh', 'rcp2_dh', 'rcp3_dh', 'renovation_share', 'rh_avg', 'test_NFV_shares', 'transmittance_MW', 'transmittance_Wm²', 'vent_infiltration_ACH', 'vent_scale_office', 'vent_scale_other', 'vent_scale_residential', 'vent_scale_retail', 'vent_scale_school_prim', 'vent_scale_school_sec', 'vent_scale_supermarket', 'weather_index']
- var_name removed: ['']
- ⚠ Duplicates (old): ['']

### Value changes
- Compared columns: ['ka', 'Type', 'Einheit', 'Formel', 'Name']
- Change count: 50

| var_name | column | old | new |
|---|---|---|---|
| Batt_is_gridcharged | Type | userinput | ui_writeback |
| Batt_is_used | Type | userinput | ui_writeback |
| DHW_concurrency_office | Formel |  | 💧WW!D52 |
| DHW_concurrency_other | Formel |  | 💧WW!D57 |
| DHW_concurrency_residential | Formel |  | 💧WW!D51 |
| DHW_concurrency_retailfood | Formel |  | 💧WW!D55 |
| DHW_concurrency_retailother | Formel |  | 💧WW!D56 |
| DHW_concurrency_schoolprim | Formel |  | 💧WW!D54 |
| DHW_concurrency_schoolsec | Formel |  | 💧WW!D53 |
| DHW_occupancy_office | Formel |  | 💧WW!D61 |
| DHW_occupancy_other | Formel |  | 💧WW!D66 |
| DHW_occupancy_residential | Formel |  | 💧WW!D60 |
| DHW_occupancy_retailfood | Formel |  | 💧WW!D64 |
| DHW_occupancy_retailother | Formel |  | 💧WW!D65 |
| DHW_occupancy_schoolprim | Formel |  | 💧WW!D63 |
| DHW_occupancy_schoolsec | Formel |  | 💧WW!D62 |
| DHW_storage_env_temp_default | Formel |  | 💧WW!D47 |
| DHW_storage_liter_pPerson | Formel |  | 💧WW!D46 |
| DHW_thermal_power_pPerson | ka | 2 | 1 |
| DHW_thermal_power_pPerson | Type | userinput | value |
| FLEX_PV_is_used | Type | userinput | ui_writeback |
| FLEX_is_used | Type | userinput | ui_writeback |
| PV_is_used | Type | userinput | ui_writeback |
| cooling_month1 | Type | userinput | ui_writeback |
| cooling_month10 | Type | userinput | ui_writeback |
| cooling_month11 | Type | userinput | ui_writeback |
| cooling_month12 | Type | userinput | ui_writeback |
| cooling_month2 | Type | userinput | ui_writeback |
| cooling_month3 | Type | userinput | ui_writeback |
| cooling_month4 | Type | userinput | ui_writeback |
| cooling_month5 | Type | userinput | ui_writeback |
| cooling_month6 | Type | userinput | ui_writeback |
| cooling_month7 | Type | userinput | ui_writeback |
| cooling_month8 | Type | userinput | ui_writeback |
| cooling_month9 | Type | userinput | ui_writeback |
| ev_bidirectional_use | Type | userinput | ui_writeback |
| heating_month1 | Type | userinput | ui_writeback |
| heating_month10 | Type | userinput | ui_writeback |
| heating_month11 | Type | userinput | ui_writeback |
| heating_month12 | Type | userinput | ui_writeback |
| heating_month2 | Type | userinput | ui_writeback |
| heating_month3 | Type | userinput | ui_writeback |
| heating_month4 | Type | userinput | ui_writeback |
| heating_month5 | Type | userinput | ui_writeback |
| heating_month6 | Type | userinput | ui_writeback |
| heating_month7 | Type | userinput | ui_writeback |
| heating_month8 | Type | userinput | ui_writeback |
| heating_month9 | Type | userinput | ui_writeback |
| mobility_is_included | Type | userinput | ui_writeback |
| usage_concurrency_winter_eduprim | Formel |  | 👤!F24 |

## OUT

### Columns
- Added: ['Formel']
- Removed: ['ID']
- Common count: 7

### Rows
- Old count: 391
- New count: 391
- var_name added: []
- var_name removed: []

### Value changes
- Compared columns: ['Kategorie', 'Bereich', 'Einheit', 'Label', 'Name']
- Change count: 0

_No value changes._

## Audit summary

- Raw audit present (old): False
- Raw audit present (new): True

### Empty var_name exclusions (converter)

**Old:**
```json
{}
```
**New:**
```json
{'IN': {'empty_var_name_count': 420}, 'OUT': {'empty_var_name_count': 117}}
```