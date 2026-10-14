"""Room-level air paths and hot-water appliances, anchored to floor geometry."""

from xml.etree import ElementTree as ET

from .component_symbols import draw_plant_symbol, line, shape


def draw_ventilation(
    group: ET.Element, kind: str, left: float, top: float, width: float
) -> None:
    """Distinguish exhaust-only, balanced and natural air paths below a ceiling.

    Exhaust recovery has no invented mechanical supply duct. The legacy names
    ``mechanical`` and ``heat_recovery`` retain their generic/balanced depiction.
    """
    color = "#288e91"
    center, level = left + width / 2, top + 10
    if kind == "natural":
        center, level = left + width - 12, top + 35
        line(group, center, level, center - 18, level, color)
        shape(
            group,
            "polyline",
            points=f"{center-13},{level-4} {center-18},{level} {center-13},{level+4}",
            fill="none",
            stroke=color,
        )
        group.set("data-location", "window")
    else:
        exhaust_only = kind in {"exhaust", "exhaust_recovery"}
        balanced = kind in {"balanced", "balanced_recovery", "heat_recovery"}
        recovery = kind in {"heat_recovery", "balanced_recovery", "exhaust_recovery"}
        group.set("data-location", "below-ceiling")
        group.set(
            "data-topology",
            "exhaust" if exhaust_only else "balanced" if balanced else "mechanical",
        )
        line(group, left + 8, level, left + width - 12, level, color, 2.3)
        for fraction in (0.35, 0.75):
            outlet = left + width * fraction
            line(group, outlet, level, outlet, level + 12, color, 1.3)
            tip, tail = (
                (level + 2, level + 7) if exhaust_only else (level + 15, level + 10)
            )
            shape(
                group,
                "polygon",
                points=f"{outlet},{tip} {outlet-3},{tail} {outlet+3},{tail}",
                fill=color,
            )
        if balanced:
            line(
                group,
                left + 8,
                level + 6,
                left + width - 12,
                level + 6,
                "#7b9699",
                1.2,
                data_air_path="extract",
            )
            shape(
                group,
                "path",
                d=f"M {left+width*.55-3},{level+12} L {left+width*.55},{level+7} L {left+width*.55+3},{level+12}",
                stroke=color,
                fill="none",
            )
        if exhaust_only:
            # A façade inlet supplies replacement air without a second fan.
            line(group, left + width + 4, top + 34, left + width - 14, top + 34, color)
            shape(
                group,
                "path",
                d=f"M {left+width-9},{top+31} L {left+width-14},{top+34} L {left+width-9},{top+37}",
                fill="none",
                stroke=color,
            )
        if recovery:
            shape(
                group,
                "rect",
                x=left + 10,
                y=level - 5,
                width=15,
                height=13,
                fill="white",
                stroke=color,
            )
            line(group, left + 11, level + 6, left + 24, level - 3, color)
            group.set("data-recovery", "true")
    group.set("data-anchor-x", str(center))
    group.set("data-anchor-y", str(level))


def draw_hot_water(
    group: ET.Element, kind: str, left: float, bottom: float, width: float
) -> None:
    """Place a draw-off and local heater, or a central supply/return branch."""
    center = left + min(width * 0.24, 55)
    color = "#b86b58"
    group.set("data-location", "draw-off")
    group.set("data-anchor-x", str(center))
    group.set("data-anchor-y", str(bottom - 25))
    # Sink, tap and domestic-water branch; never a room-heating emitter.
    shape(
        group,
        "path",
        d=f"M {center-14},{bottom-24} H {center+14} L {center+9},{bottom-17} H {center-9} Z",
        fill="#edf0ec",
        stroke="#71858a",
    )
    shape(
        group,
        "path",
        d=f"M {center+5},{bottom-24} V {bottom-33} H {center-1}",
        fill="none",
        stroke=color,
        stroke_width=1.5,
    )
    if kind == "central":
        line(
            group,
            left + 5,
            bottom - 7,
            center,
            bottom - 7,
            color,
            1.3,
            data_service="dhw",
        )
        line(group, center, bottom - 7, center, bottom - 17, color)
        line(
            group,
            left + 5,
            bottom - 4,
            center - 4,
            bottom - 4,
            "#c39d91",
            0.8,
            data_service="dhw-return",
        )
    else:
        appliance = {
            "gas_local": "gas_water_heater",
            "electric_local": "electric_water_heater",
            "heat_pump_local": "dhw_heat_pump",
        }[kind]
        draw_plant_symbol(group, appliance, center + 35, bottom - 2, 22)
