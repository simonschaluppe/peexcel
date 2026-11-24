from numbers import Real

import pandas as pd
import plotly.graph_objects as go
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


def style_boxes(figure, *, colors=None, language="de"):
    """Style vertical, overlay-mode box plots in place, including facets.

    ``colors`` maps box trace names to (fill, outline) colors. The boxes use
    slim outlines and outlier dots, with inset red median lines and triangular
    mean markers. Numeric group positions are expected to be one unit apart.
    """
    colors = colors or {}
    width = 0.6
    median_half_width = width * 0.45
    mean_label = "Mittelwert" if language == "de" else "Mean"
    for trace in list(figure.data):
        if trace.type != "box" or trace.x is None or trace.y is None:
            continue
        fill, outline = colors.get(trace.name, ("#b9d7ea", "#36648b"))
        trace.update(fillcolor=fill, line=dict(color=outline, width=0.6),
                     width=width, boxpoints="outliers",
                     marker=dict(color=outline, size=3, opacity=0.4))
        stats = pd.DataFrame({"group": trace.x, "value": trace.y}).dropna()
        stats = stats.groupby("group")["value"].agg(["median", "mean"])
        for center, median in stats["median"].items():
            if isinstance(center, Real):
                endpoints = dict(x0=center - median_half_width, x1=center + median_half_width)
            else:
                endpoints = dict(x0=center, x1=center, x0shift=-median_half_width,
                                 x1shift=median_half_width)
            figure.add_shape(type="line", xref=trace.xaxis or "x", yref=trace.yaxis or "y",
                             y0=median, y1=median, line=dict(color="#b22222", width=1),
                             **endpoints)
        figure.add_trace(go.Scatter(
            x=stats.index, y=stats["mean"], mode="markers",
            marker=dict(symbol="triangle-up", size=6, color=outline),
            xaxis=trace.xaxis, yaxis=trace.yaxis, showlegend=False,
            hovertemplate=f"{mean_label}: %{{y:.1f}}<extra></extra>",
        ))
    figure.update_layout(template="plotly_white", boxmode="overlay")
    figure.update_yaxes(gridcolor="#e6e6e6")
