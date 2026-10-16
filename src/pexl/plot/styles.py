from matplotlib.colors import LinearSegmentedColormap


BALANCE_CMAP = LinearSegmentedColormap.from_list(
    "pexl_balance",
    [
        "red",
        "white",
        "lightgreen",
        "green",
        "darkgreen",
        "black",
        "black",
        "black",
        "black",
        "darkgreen",
        "green",
        "lightgreen",
        "white",
        "red",
    ],
    N=17,
)


# pexl/plot/styles.py

COLORS = {
    "electricity_user": "#EC4298",
    "electricity_heating": "#F57F67",
    "electricity_cooling": "#05B0EF",
    "electricity_ventilation": "#3BACBE",
    "electricity_dhw": "#E1320F",
    "electricity_ev": "#FFC560",

    "pv_direct": "#5FB564",
    "pv_flexible": "#9FD3A2",
    "pv_feedin": "#B4E0B6",

    "battery": "#BCCF00",
    "grid": "#950F53",
    "grid_flexible": "#FAF2BF",
    "v2b": "#FBC472",
}


VAR_COLOR_GROUPS = {
    # User electricity
    "EUI_plugAuxLight": "electricity_user",
    "E_plugAuxLight": "electricity_user",

    # Heating
    "EUIh_el": "electricity_heating",
    "Eh_min": "electricity_heating",
    "Eh_flex_1el_final": "electricity_heating",
    "Eh_flex_3el_final": "electricity_heating",

    # Cooling
    "EUIc_el": "electricity_cooling",
    "Ec_min": "electricity_cooling",
    "Ec_flex_1el_final": "electricity_cooling",
    "Ec_flex_3el_final": "electricity_cooling",

    # Ventilation
    "EUIv_el": "electricity_ventilation",
    "Ev_min": "electricity_ventilation",

    # DHW
    "EUIdhw_el": "electricity_dhw",
    "Edhw_min": "electricity_dhw",
    "Edhw1_flex_final": "electricity_dhw",
    "Edhw2_flex_final": "electricity_dhw",

    # EV
    "EUIev_el": "electricity_ev",
    "Eev_min": "electricity_ev",
    "PV_to_Eev_flex":  "electricity_ev",

    # PV
    "PV_to_user": "pv_direct",
    "PV_total_direct": "pv_direct",
    "PV_total_direct_use": "pv_direct",

    "PV_total_flex": "pv_flexible",
    "PV_total_flex_use": "pv_flexible",

    "PV_to_Egrid": "pv_feedin",

    # Battery
    "Batt_total_discharge": "battery",
    "Batt_to_user": "battery",
    "Batt_to_HVAC_min": "battery",
    "Batt_to_Eev_min": "battery",

    # Grid
    "Grid_to_min": "grid",
    "E_grid": "grid",

    "VRGrid_to_min": "grid_flexible",
    "VRGrid_total_min_use": "grid_flexible",

    # V2B
    "Eev_to_district": "v2b",
    "Eev_to_user": "v2b",
    "Eev_to_HVAC": "v2b",
}


def color_for(var_name: str) -> str | None:
    group = VAR_COLOR_GROUPS.get(var_name)

    if group is None:
        return None

    return COLORS[group]