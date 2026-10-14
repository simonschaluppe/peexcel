"""Shared vector cutaways for plant, sources and domestic hot water.

Coordinates are drawing pixels. These functions illustrate equipment topology;
they do not size equipment, calculate pipe routes or add to scenario floor area.
Both legacy overlays and resolved equipment records use these same primitives.
"""

from xml.etree import ElementTree as ET

INK = "#586f78"
PALE = "#e7edef"
HEAT = "#b86b58"
COLD = "#527d98"


def shape(parent: ET.Element, tag: str, **attributes) -> ET.Element:
    """Append an SVG element, converting Python-style attribute names."""
    return ET.SubElement(
        parent,
        tag,
        {key.replace("_", "-"): str(value) for key, value in attributes.items()},
    )


def line(
    parent: ET.Element,
    x1: float,
    y1: float,
    x2: float,
    y2: float,
    color: str = INK,
    width: float = 1.2,
    **attributes,
) -> ET.Element:
    """Draw one straight connection or construction line."""
    return shape(
        parent,
        "line",
        x1=x1,
        y1=y1,
        x2=x2,
        y2=y2,
        stroke=color,
        stroke_width=width,
        **attributes,
    )


def arrow(
    parent: ET.Element, x: float, y: float, direction: int, color: str = INK
) -> None:
    """Draw a horizontal flow arrow; direction is -1 or +1."""
    line(parent, x - 7 * direction, y, x + 7 * direction, y, color)
    shape(
        parent,
        "path",
        d=f"M {x+3*direction},{y-3} L {x+7*direction},{y} L {x+3*direction},{y+3}",
        fill="none",
        stroke=color,
        stroke_width=1.2,
    )


def draw_plant_symbol(
    parent: ET.Element,
    kind: str,
    cx: float,
    base: float,
    width: float = 38,
    *,
    mode: str = "heating",
) -> None:
    """Draw a plant cutaway resting on ``base`` and centred at ``cx``.

    Boilers include a flue; exchangers show two separated circuits; heat pumps
    and chillers show a compressor and heat-exchange connections. Tanks include
    a storage vessel and coil. No letter-only placeholder substitutes for a kind.
    """
    color = (
        COLD
        if mode == "cooling"
        or kind in {"district_cooling", "chiller", "passive_exchanger"}
        else HEAT
    )
    width = max(14, width)  # preserve positive internal widths at small drawing scales
    left, top = cx - width / 2, base - 32
    parent.set("data-anchor-x", str(cx))
    parent.set("data-anchor-y", str(top + 16))
    parent.set("data-symbol-kind", kind)
    if kind == "hot_water_tank":
        shape(
            parent,
            "rect",
            x=left + 5,
            y=top - 6,
            width=width - 10,
            height=38,
            rx=7,
            fill=PALE,
            stroke=INK,
            stroke_width=1.2,
        )
        shape(
            parent,
            "polyline",
            points=" ".join(f"{cx+(-7 if i%2 else 7)},{top+3+i*4}" for i in range(6)),
            fill="none",
            stroke=color,
            stroke_width=1.5,
        )
        line(parent, cx, top - 6, cx, top - 12, color)
        line(parent, cx, base, cx, base + 3, color)
        return
    shape(
        parent,
        "rect",
        x=left,
        y=top,
        width=width,
        height=32,
        rx=2,
        fill=PALE,
        stroke=INK,
        stroke_width=1.2,
    )
    if kind in {"district_heating", "district_cooling", "passive_exchanger"}:
        for offset in (-5, 5):
            line(
                parent,
                left - 8,
                top + 16 + offset,
                left + width + 8,
                top + 16 + offset,
                color,
                1.5,
            )
        for offset in (-6, 0, 6):
            line(parent, cx + offset - 3, top + 8, cx + offset + 3, top + 24, INK, 0.8)
        arrow(parent, left - 10, top + 11, 1, color)
        arrow(parent, left + width + 10, top + 21, -1, color)
        if kind == "passive_exchanger":
            shape(
                parent,
                "path",
                d=f"M {left-6},{base-5} V {base+7} H {left+width+6} V {base-5}",
                fill="none",
                stroke=color,
                stroke_dasharray="3 2",
            )
    elif kind in {"heat_pump", "chiller", "dhw_heat_pump"}:
        shape(
            parent,
            "circle",
            cx=cx,
            cy=top + 16,
            r=7,
            fill="none",
            stroke=color,
            stroke_width=1.5,
        )
        shape(
            parent,
            "path",
            d=f"M {cx-4},{top+20} L {cx+4},{top+16} L {cx-4},{top+12} Z",
            fill=color,
        )
        for side in (-1, 1):
            px = cx + side * (width / 2 - 5)
            line(parent, px, top + 5, px, top + 27, INK, 2)
            line(parent, px, top + 10, cx + side * 6, top + 10, color)
            line(parent, px, top + 22, cx + side * 6, top + 22, color)
        if mode == "reversible":
            arrow(parent, cx, top - 5, 1, HEAT)
            arrow(parent, cx, base + 6, -1, COLD)
    elif kind in {"air_handler", "outdoor_unit"}:
        shape(parent, "circle", cx=cx, cy=top + 16, r=11, fill="none", stroke=INK)
        for dx, dy in ((0, -8), (7, 5), (-7, 5)):
            shape(
                parent,
                "path",
                d=f"M {cx},{top+16} Q {cx+dx-4},{top+16+dy-3} {cx+dx},{top+16+dy}",
                stroke=INK,
                stroke_width=2.5,
                fill="none",
            )
        if kind == "air_handler":
            line(parent, left - 10, top + 8, left, top + 8, COLD, 3)
            line(parent, left + width, top + 24, left + width + 10, top + 24, COLD, 3)
    elif kind in {"gas_boiler", "oil_boiler", "biomass_boiler", "gas_water_heater"}:
        line(parent, left + width - 6, top, left + width - 6, top - 12, INK, 2)
        shape(
            parent,
            "path",
            d=f"M {cx},{top+7} Q {cx-13},{base-3} {cx},{base-4} Q {cx+11},{base-7} {cx},{top+7}",
            fill=color,
        )
        if kind == "biomass_boiler":
            shape(
                parent,
                "path",
                d=f"M {left-22},{top+5} H {left-5} V {base-8} L {left-13},{base} L {left-22},{base-8} Z",
                fill=PALE,
                stroke=INK,
            )
            line(parent, left - 13, base, left, base - 5, color, 2)
    elif kind == "electric_water_heater":
        shape(
            parent,
            "polyline",
            points=f"{cx+3},{top+6} {cx-4},{top+17} {cx+4},{top+17} {cx-3},{top+27}",
            fill="none",
            stroke=color,
            stroke_width=2,
        )
    else:
        raise ValueError(f"No plant drawing registered for {kind!r}")


def draw_source(
    parent: ET.Element, source: str, cx: float, ground: float, bottom: float
) -> None:
    """Draw an explicit source: outdoor fan, horizontal loop or paired wells."""
    if source == "air":
        draw_plant_symbol(parent, "outdoor_unit", cx, ground - 4)
    elif source == "ground":
        shape(
            parent,
            "polyline",
            points=f"{cx-22},{ground+12} {cx-22},{bottom-12} {cx+22},{bottom-12} {cx+22},{bottom-6} {cx-22},{bottom-6}",
            fill="none",
            stroke=COLD,
            stroke_width=2,
        )
    elif source == "groundwater":
        for index, offset in enumerate((-12, 12)):
            line(parent, cx + offset, ground + 8, cx + offset, bottom - 4, COLD, 2)
            shape(
                parent,
                "path",
                d=f"M {cx+offset-4},{bottom-12} L {cx+offset},{bottom-6} L {cx+offset+4},{bottom-12}",
                fill="none",
                stroke=COLD,
                transform=f"rotate({180 if index else 0} {cx+offset} {bottom-9})",
            )
        line(parent, cx - 20, bottom - 3, cx + 20, bottom - 3, COLD, 0.8)
    elif source == "boreholes":
        shape(
            parent,
            "path",
            d=f"M {cx-5},{ground+8} V {bottom-10} Q {cx},{bottom} {cx+5},{bottom-10} V {ground+8}",
            fill="none",
            stroke=HEAT,
            stroke_width=2,
        )
    elif source != "unknown":
        raise ValueError(f"Unknown heat source {source!r}")
