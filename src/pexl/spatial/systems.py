"""Draw usage emitters, air paths and roof scenes in their physical context.

All positions are schematic overlays. Drawing never changes allocated NFA or
computes system performance; inference lives in :mod:`.system_resolution`.
"""

from copy import deepcopy
from math import isfinite
from xml.etree import ElementTree as ET

from .system_resolution import EMITTERS, VENTILATION, PLANT, ROOF
from ._svg_types import CoordinateMap, ElementFactory, TextWriter


def draw_systems(
    section: dict,
    element: ElementFactory,
    text: TextWriter,
    x: CoordinateMap,
    y: CoordinateMap,
    yscale: float,
    soil_bottom: float,
) -> None:
    """Draw illustrative symbols over spaces; never change allocation or capacities."""
    settings = section.get("systems", {}).get("buildings", {})
    if not settings:
        return
    floors = {f["id"]: f for f in section["floors"]}
    envelope = section["spaces"] + section.get("voids", [])
    heat, cold, air, neutral = "#c9533d", "#277bb8", "#288e91", "#495e6c"

    def group(kind, building, label):
        node = element(
            "g", data_kind="system", data_system=kind, data_building=building
        )
        ET.SubElement(node, "title").text = label + " (schematic overlay)"
        return node

    def shape(parent, tag, **attrs):
        return ET.SubElement(
            parent, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()}
        )

    def line(parent, a, b, c, d, color=neutral, width=1.5):
        shape(parent, "line", x1=a, y1=b, x2=c, y2=d, stroke=color, stroke_width=width)

    for space in section["spaces"]:
        floor = floors[space["floor_id"]]
        bid = floor["building_id"]
        system = settings[bid]["usages"].get(space["usage"], {})
        px, sw = x(space["x_m"]), space["width_m"] * (x(1) - x(0))
        top, bottom = y(floor["z_m"] + floor["height_m"]), y(floor["z_m"])
        if sw < 36:
            continue  # too narrow for a legible symbol
        width = sw - 16
        slab_height = max(2.0, floor["slab_thickness_m"] * yscale)
        for mode, color in (("heating", heat), ("cooling", cold)):
            emitter = system.get(mode, "none")
            if emitter == "none":
                continue
            g = group(f"{mode}:{emitter}", bid, f"{space['label']}: {mode} / {emitter}")
            g.set("data-space", space["id"])
            left = px + 8
            if emitter in ("underfloor", "tabs"):
                if emitter == "tabs":
                    # The circuit is inside the structural slab, not in room air.
                    level = bottom + slab_height / 2
                    shape(
                        g,
                        "rect",
                        data_layer="concrete",
                        x=left,
                        y=bottom,
                        width=width,
                        height=slab_height,
                        fill="#b8c1c5",
                    )
                    g.set("data-location", "inside-concrete")
                else:
                    level = bottom - 7
                    shape(
                        g,
                        "rect",
                        data_layer="screed",
                        x=left,
                        y=bottom - 12,
                        width=width,
                        height=10,
                        fill="#f2e6d1",
                    )
                    shape(
                        g,
                        "rect",
                        data_layer="floor-insulation",
                        x=left,
                        y=bottom - 2,
                        width=width,
                        height=2,
                        fill="#d8bee9",
                    )
                    g.set("data-location", "above-structural-slab")
                g.set("data-anchor-x", str(left + width / 2))
                g.set("data-anchor-y", str(level))
                if mode == "cooling" and system.get("heating") == emitter:
                    level += 2  # parallel runs remain distinguishable in the same layer
                shape(
                    g,
                    "line",
                    data_pipe="straight",
                    x1=left,
                    x2=left + width,
                    y1=level,
                    y2=level,
                    stroke=color,
                    stroke_width=1.6,
                )
            else:
                w = min(29, width * 0.65)
                left = px + sw - w - 9
                level = top + 30 if emitter == "split" else bottom - 21
                if (
                    mode == "cooling"
                    and system.get("heating") in {"radiator", "fan_coil"}
                    and emitter != "split"
                ):
                    level -= 15
                g.set(
                    "data-location",
                    "facade-high" if emitter == "split" else "below-window",
                )
                g.set("data-anchor-x", str(left + w / 2))
                g.set("data-anchor-y", str(level - 4))
                shape(
                    g,
                    "rect",
                    x=left,
                    y=level - 9,
                    width=w,
                    height=10,
                    rx=2,
                    fill="white",
                    fill_opacity=0.95,
                    stroke=color,
                )
                if emitter == "radiator":
                    for n in range(1, 6):
                        line(
                            g,
                            left + w * n / 6,
                            level - 8,
                            left + w * n / 6,
                            level,
                            color,
                            1,
                        )
                    line(g, left + 3, level - 12, left + 6, level - 16, color, 1)
                else:
                    line(g, left + 3, level - 3, left + w - 3, level - 3, color, 1)
                    shape(
                        g,
                        "polyline",
                        points=f"{left+5},{level+3} {left-2},{level+10} {left-9},{level+12}",
                        fill="none",
                        stroke=color,
                    )
                    if emitter == "fan_coil":
                        shape(
                            g,
                            "circle",
                            cx=left + w / 2,
                            cy=level - 5,
                            r=2,
                            fill="none",
                            stroke=color,
                        )
        ventilation = system.get("ventilation", "none")
        if ventilation != "none":
            g = group(
                f"ventilation:{ventilation}",
                bid,
                f"{space['label']}: {ventilation} ventilation",
            )
            g.set("data-space", space["id"])
            cy = top + 10
            if ventilation == "natural":
                cx, cy = px + sw - 12, top + 35
                line(g, cx, cy, cx - 18, cy, air)
                shape(
                    g,
                    "polyline",
                    points=f"{cx-13},{cy-4} {cx-18},{cy} {cx-13},{cy+4}",
                    fill="none",
                    stroke=air,
                )
                g.set("data-location", "window")
            else:
                cx = px + sw / 2
                g.set("data-location", "below-ceiling")
                line(g, px + 8, cy, px + sw - 12, cy, air, 3)
                for fraction in (0.35, 0.75):
                    outlet = px + sw * fraction
                    line(g, outlet, cy, outlet, cy + 12, air, 1.5)
                    shape(
                        g,
                        "polygon",
                        points=f"{outlet},{cy+15} {outlet-3},{cy+10} {outlet+3},{cy+10}",
                        fill=air,
                    )
                if ventilation == "heat_recovery":
                    line(g, px + 8, cy + 5, px + sw - 12, cy + 5, "#7b9699", 1)
                    shape(
                        g,
                        "rect",
                        x=px + 10,
                        y=cy - 5,
                        width=15,
                        height=13,
                        fill="white",
                        stroke=air,
                    )
                    line(g, px + 11, cy + 6, px + 24, cy - 3, air, 1)
            g.set("data-anchor-x", str(cx))
            g.set("data-anchor-y", str(cy))

    for building in section["buildings"]:
        bid = building["id"]
        systems = settings[bid]
        members = [s for s in envelope if s["floor_id"] in building["floor_ids"]]
        if not members:
            continue
        left = x(min(s["x_m"] for s in members))
        right = x(max(s["x_m"] + s["width_m"] for s in members))
        lowest = min(
            (floors[f] for f in building["floor_ids"]), key=lambda f: f["index"]
        )
        base_y = y(lowest["z_m"])
        plant = [
            p
            for p in systems["plant"]
            if p not in ("water_well", "boreholes", "heating_room")
        ]
        lowest_members = [s for s in envelope if s["floor_id"] == lowest["id"]]
        # Prefer other/empty space and keep the room overlay local so usage colors remain readable.
        candidates = [
            s
            for s in lowest_members
            if s.get("usage") == "other" or s.get("kind") == "empty_basement"
        ] or lowest_members
        host = max(candidates, key=lambda s: s["width_m"])
        room_left = x(host["x_m"]) + 8
        room_right = x(host["x_m"] + host["width_m"]) - 8
        room_width = max(8, min(240, room_right - room_left))
        if "heating_room" in systems["plant"]:
            g = group(
                "heating_room",
                bid,
                "Plant room containing this building's specified equipment",
            )
            g.set("data-anchor-x", str(room_left + room_width / 2))
            g.set("data-anchor-y", str(base_y - 47))
            shape(
                g,
                "rect",
                x=room_left,
                y=base_y - 56,
                width=room_width,
                height=49,
                fill="#fafaf6",
                fill_opacity=0.82,
                stroke=neutral,
                stroke_width=1,
                stroke_dasharray="4 2",
            )
            shape(
                g,
                "text",
                x=room_left + 6,
                y=base_y - 43,
                font_size=10,
                font_family="sans-serif",
                fill=neutral,
            ).text = "Plant room"
        for index, symbol in enumerate(plant):
            cx = room_left + (index + 0.5) * room_width / max(1, len(plant))
            cy = base_y - 23
            g = group(symbol, bid, symbol.replace("_", " "))
            g.set("data-anchor-x", str(cx))
            g.set("data-anchor-y", str(cy))
            w = min(34, room_width / max(1, len(plant)) - 4)
            if w < 8:
                continue
            shape(
                g,
                "rect",
                x=cx - w / 2,
                y=cy - 10,
                width=w,
                height=22,
                rx=2,
                fill="white",
                stroke=neutral,
                stroke_width=1.5,
            )
            if symbol == "district_heating":
                line(g, cx - w / 2 - 8, cy - 4, cx + w / 2 + 6, cy - 4, heat, 2)
                line(g, cx - w / 2 - 8, cy + 4, cx + w / 2 + 6, cy + 4, cold, 2)
            else:
                shape(
                    g,
                    "path",
                    d=f"M {cx},{cy-7} Q {cx-11},{cy+8} {cx},{cy+9} Q {cx+9},{cy+4} {cx},{cy-7}",
                    fill=heat,
                )
                label = {"gas_boiler": "G", "oil_boiler": "O", "biomass_boiler": "B"}[
                    symbol
                ]
                shape(
                    g,
                    "text",
                    x=cx + 9,
                    y=cy - 1,
                    font_size=9,
                    font_family="sans-serif",
                    fill=neutral,
                ).text = label
        ground_sources = [
            p for p in systems["plant"] if p in ("water_well", "boreholes")
        ]
        for index, symbol in enumerate(ground_sources):
            cx = left + (index + 1) * (right - left) / (len(ground_sources) + 1)
            g = group(symbol, bid, symbol.replace("_", " "))
            gy = base_y + 18
            connection_color = cold if symbol == "water_well" else heat
            target_x = room_left + room_width * (
                0.3 + 0.4 * index / max(1, len(ground_sources) - 1)
            )
            connection = group(
                "connection:" + symbol, bid, "Illustrative connection to plant room"
            )
            shape(
                connection,
                "polyline",
                data_connection=symbol,
                points=f"{cx},{gy} {cx},{base_y+8+index*5} {target_x},{base_y+8+index*5} {target_x},{base_y-8}",
                fill="none",
                stroke=connection_color,
                stroke_width=1.2,
            )
            text(
                "Well" if symbol == "water_well" else "Boreholes",
                cx + 15,
                (gy + soil_bottom) / 2,
                size=10,
            )
            g.set("data-anchor-x", str(cx))
            g.set("data-anchor-y", str((gy + soil_bottom) / 2))
            if symbol == "boreholes":
                shape(
                    g,
                    "path",
                    d=f"M {cx-5},{gy} L {cx-5},{soil_bottom-12} Q {cx},{soil_bottom-5} {cx+5},{soil_bottom-12} L {cx+5},{gy}",
                    fill="none",
                    stroke=heat,
                    stroke_width=2,
                )
                line(g, cx - 11, gy, cx + 11, gy, neutral)
            else:
                shape(
                    g,
                    "rect",
                    x=cx - 7,
                    y=gy,
                    width=14,
                    height=max(10, soil_bottom - gy - 8),
                    fill="#c5e8f5",
                    stroke=cold,
                )
                line(g, cx - 15, soil_bottom - 16, cx + 15, soil_bottom - 16, cold)
                line(g, cx, gy + 6, cx, soil_bottom - 12, cold, 2)

        roofs = [r for r in section["roofs"] if r["building_id"] == bid]
        room_interval = None
        if "hvac_room" in systems["roof"] and roofs:
            center = (left + right) / 2
            shaft_width = min(2.0 * (x(1) - x(0)), (right - left) * 0.15)
            room_width = 2 * shaft_width
            support = next(
                (
                    r
                    for r in sorted(roofs, key=lambda r: -r["z_m"])
                    if x(r["x_m"]) <= center <= x(r["x_m"] + r["width_m"])
                ),
                None,
            )
            if support is not None:
                room_interval = (
                    support["id"],
                    center - room_width / 2 - 3,
                    center + room_width / 2 + 3,
                )
                ry = y(support["z_m"]) - 2.5
                g = group(
                    "roof:hvac_room",
                    bid,
                    "Rooftop HVAC room; twice the service shaft width",
                )
                g.set("data-anchor-x", str(center))
                g.set("data-anchor-y", str(ry - 27))
                g.set("data-shaft-width", str(shaft_width))
                g.set("data-room-width", str(room_width))
                shape(
                    g,
                    "rect",
                    x=center - room_width / 2,
                    y=ry - 48,
                    width=room_width,
                    height=48,
                    fill="#e8edef",
                    stroke=neutral,
                    stroke_width=1.5,
                )
                line(
                    g,
                    center - shaft_width / 2,
                    ry,
                    center - shaft_width / 2,
                    ry + 12,
                    neutral,
                )
                line(
                    g,
                    center + shaft_width / 2,
                    ry,
                    center + shaft_width / 2,
                    ry + 12,
                    neutral,
                )
                for offset in (-7, 0, 7):
                    line(
                        g,
                        center - room_width * 0.3,
                        ry - 25 + offset,
                        center + room_width * 0.3,
                        ry - 25 + offset,
                        air,
                    )
                shape(
                    g,
                    "text",
                    x=center,
                    y=ry - 55,
                    text_anchor="middle",
                    font_size=10,
                    fill=neutral,
                ).text = "HVAC"
        features = [r for r in systems["roof"] if r not in {"pv", "hvac_room"}]
        if not roofs or not features:
            continue
        # Tile the available roof surface; PV and the shaft room retain their positions.
        slots = []
        for roof in sorted(roofs, key=lambda r: r["x_m"]):
            start, end = x(roof["x_m"]), x(roof["x_m"] + roof["width_m"])
            intervals = [(start, end)]
            blocked = []
            if "pv" in systems["roof"]:
                blocked += [
                    (
                        x(roof["x_m"] + p["offset_m"]) - 2,
                        x(roof["x_m"] + p["offset_m"] + p["width_m"]) + 2,
                    )
                    for p in section["pv"]["placements"]
                    if p["roof_id"] == roof["id"]
                ]
            if room_interval and room_interval[0] == roof["id"]:
                blocked.append(room_interval[1:])
            for lo, hi in blocked:
                intervals = [
                    (a, b)
                    for l, r in intervals
                    for a, b in ((l, min(r, lo)), (max(l, hi), r))
                    if b - a > 1
                ]
            for l, r in intervals:
                count = int((r - l) / 64)
                slots.extend(
                    (l + i * 64, 64, y(roof["z_m"]) - 2.5) for i in range(count)
                )
                if r - l - count * 64 >= 24:
                    slots.append(
                        (l + count * 64, r - l - count * 64, y(roof["z_m"]) - 2.5)
                    )
        feature_index = 0
        for l, w, level in slots:
            small = w < 64
            if small and "garden" not in features:
                continue  # never squeeze furniture into a narrow setback
            feature = "garden" if small else features[feature_index % len(features)]
            if not small:
                feature_index += 1
            g = group(f"roof:{feature}", bid, feature.replace("_", " "))
            g.set("data-anchor-x", str(l + w / 2))
            g.set("data-anchor-y", str(level - 22))
            g.set("data-roof-tile", feature)
            g.set("data-left", str(l))
            g.set("data-width", str(w))
            g.set("data-base-y", str(level))
            scene = shape(g, "g", transform=f"translate({l},{level})")
            shape(scene, "rect", x=0, y=-3, width=w, height=3, fill="#b9a48b")
            if small:
                shape(scene, "rect", x=2, y=-12, width=w - 4, height=9, fill="#b0bd9f")
                for dx in range(7, int(w) - 3, 9):
                    shape(scene, "ellipse", cx=dx, cy=-16, rx=5, ry=7, fill="#789665")
                continue
            if feature in {"terrace", "pergola"}:
                # Deck, furniture, rail and a small planter.
                shape(scene, "rect", x=1, y=-18, width=62, height=14, fill="none")
                line(scene, 1, -18, 63, -18, "#81999c", 1)
                for dx in (2, 32, 62):
                    line(scene, dx, -18, dx, -3, "#81999c", 1)
                shape(scene, "rect", x=20, y=-16, width=24, height=3, fill="#88775e")
                for dx in (24, 40):
                    line(scene, dx, -13, dx, -3, "#88775e", 1.5)
                for dx in (10, 48):
                    shape(scene, "rect", x=dx, y=-11, width=7, height=2, fill="#bb805a")
                    line(scene, dx, -18, dx, -3, "#bb805a", 1.5)
                    line(scene, dx + 6, -9, dx + 6, -3, "#bb805a", 1)
                if feature == "pergola":
                    for dx in (4, 60):
                        shape(
                            scene,
                            "rect",
                            x=dx,
                            y=-43,
                            width=3,
                            height=40,
                            fill="#9a8160",
                        )
                    shape(scene, "rect", x=0, y=-43, width=64, height=4, fill="#9a8160")
                    for dx in range(3, 64, 8):
                        shape(
                            scene,
                            "rect",
                            x=dx,
                            y=-46,
                            width=4,
                            height=3,
                            fill="#b39a74",
                        )
                    shape(
                        scene,
                        "path",
                        d="M 3,-39 H 18 L 22,-33 H 34 L 39,-39 H 61",
                        fill="none",
                        stroke="#83956c",
                        stroke_width=3,
                    )
            elif feature == "garden":
                shape(scene, "rect", x=0, y=-6, width=64, height=3, fill="#78936a")
                for dx in (4, 43):
                    shape(
                        scene, "rect", x=dx, y=-14, width=17, height=8, fill="#ba9471"
                    )
                    for offset in (3, 8, 13):
                        shape(
                            scene,
                            "ellipse",
                            cx=dx + offset,
                            cy=-17 - offset % 3,
                            rx=5,
                            ry=7,
                            fill="#7d9e6c",
                        )
                line(scene, 32, -6, 32, -31, "#92785f", 2)
                for dx, dy, r, color in (
                    (27, -33, 9, "#9aaf7d"),
                    (36, -34, 10, "#789665"),
                    (31, -41, 8, "#8ea672"),
                ):
                    shape(scene, "circle", cx=dx, cy=dy, r=r, fill=color)
            elif feature == "solar_thermal":
                for dx in (5, 34):
                    line(scene, dx + 3, -4, dx + 3, -18, neutral, 1)
                    line(scene, dx + 23, -4, dx + 23, -27, neutral, 1)
                    shape(
                        scene,
                        "polygon",
                        points=f"{dx},-17 {dx+23},-30 {dx+25},-26 {dx+2},-13",
                        fill="#657e87",
                        stroke=neutral,
                        stroke_width=1,
                    )
                    for offset in (5, 10, 15, 20):
                        line(
                            scene,
                            dx + offset,
                            -17 - offset * 13 / 23,
                            dx + offset + 2,
                            -13 - offset * 13 / 23,
                            "#c69760",
                            1.4,
                        )
                line(scene, 6, -7, 57, -7, "#b97c55", 1.5)


def annotate_symbols(
    root: ET.Element,
    element: ElementFactory,
    text: TextWriter,
    width: float,
    height: float,
) -> None:
    """Number one representative of each drawn symbol and provide a readable key."""
    groups = {}
    for node in list(root.iter()):
        if node.get("data-kind") == "system" and node.get("data-anchor-x"):
            key = node.get("data-system")
            anchor = (
                float(node.get("data-anchor-x")),
                float(node.get("data-anchor-y")),
            )
        elif node.get("data-kind") == "pv":
            key = "roof:pv"
            anchor = (
                float(node.get("x")) + float(node.get("width")) / 2,
                float(node.get("y")),
            )
        else:
            continue
        groups.setdefault(key, []).append(anchor)
    panel_height = max(180, len(groups) * 46 + 105)
    new_width, new_height = width + 405, max(height, panel_height + 95)
    root.set("width", f"{new_width:g}")
    root.set("height", f"{new_height:g}")
    root.set("viewBox", f"0 0 {new_width:g} {new_height:g}")
    for node in root:
        if node.tag == "rect" and node.get("x") == "0" and node.get("y") == "0":
            node.set("width", str(new_width))
            node.set("height", str(new_height))
            break
    panel_x = width + 10
    element(
        "rect",
        x=panel_x,
        y=70,
        width=375,
        height=panel_height,
        rx=8,
        fill="#ffffff",
        stroke="#b9d1df",
    )
    text("SYMBOL REVIEW", panel_x + 18, 100, size=16, font_weight=700)
    text("Numbers identify representative occurrences.", panel_x + 18, 124, size=11)
    text(
        "Labels describe symbols, not verified connections.", panel_x + 18, 142, size=11
    )
    for number, (key, anchors) in enumerate(groups.items(), 1):
        ax, ay = anchors[0]
        bx, by = ax + 13, ay - 15
        element("line", x1=ax, y1=ay, x2=bx, y2=by, stroke="#324f65", stroke_width=1)
        element(
            "circle",
            data_annotation=key,
            cx=bx,
            cy=by,
            r=9,
            fill="white",
            stroke="#324f65",
            stroke_width=1.2,
        )
        text(str(number), bx, by + 3.5, size=10, text_anchor="middle", font_weight=700)
        row_y = 176 + (number - 1) * 46
        element(
            "circle",
            cx=panel_x + 27,
            cy=row_y - 4,
            r=10,
            fill="#e6f1f7",
            stroke="#324f65",
        )
        text(
            str(number),
            panel_x + 27,
            row_y,
            size=10,
            text_anchor="middle",
            font_weight=700,
        )
        label = (
            key.replace("_", " ")
            .replace(":", " / ")
            .capitalize()
            .replace("tabs", "TABS")
            .replace("pv", "PV")
        )
        text(label, panel_x + 47, row_y, size=13, font_weight=600)
        text(f"{len(anchors)} drawn occurrence(s)", panel_x + 47, row_y + 17, size=11)
    if not groups:
        text("No HVAC or PV symbols drawn.", panel_x + 18, 180)


def draw_construction_details(
    section: dict,
    element: ElementFactory,
    text: TextWriter,
    left: float,
    top: float,
    width: float,
) -> None:
    """Enlarged reading aids for physical placement, without new model geometry."""
    if not section.get("systems"):
        return
    values = [
        v
        for b in section["systems"]["buildings"].values()
        for v in b["usages"].values()
    ]
    tabs = any(v.get(k) == "tabs" for v in values for k in ("heating", "cooling"))
    tabs_color = (
        "#277bb8" if any(v.get("cooling") == "tabs" for v in values) else "#c9533d"
    )
    underfloor_color = (
        "#c9533d"
        if any(v.get("heating") == "underfloor" for v in values)
        else "#277bb8"
    )
    underfloor = any(
        v.get(k) == "underfloor" for v in values for k in ("heating", "cooling")
    )
    vents = any(v.get("ventilation") in ("mechanical", "heat_recovery") for v in values)
    ac = any(v.get("cooling") in ("split", "fan_coil") for v in values)
    text(
        "Construction details - enlarged, not to scale",
        left,
        top,
        size=14,
        font_weight=600,
    )
    card_width = (width - 28) / 3
    for i, title in enumerate(
        (
            "TABS / concrete activation",
            "Underfloor circuit",
            "Ceiling duct / facade-side AC",
        )
    ):
        cx = left + i * (card_width + 14)
        element(
            "rect",
            data_kind="construction-detail",
            x=cx,
            y=top + 16,
            width=card_width,
            height=172,
            rx=5,
            fill="#fbfcfc",
            stroke="#becbd2",
        )
        text(title, cx + 10, top + 40, size=12, font_weight=600)
        a, b = cx + 14, cx + card_width - 14
        if i == 0 and tabs:
            element("rect", x=a, y=top + 70, width=b - a, height=38, fill="#b8c1c5")
            element(
                "line",
                data_pipe="straight",
                x1=a + 8,
                x2=b - 8,
                y1=top + 89,
                y2=top + 89,
                stroke=tabs_color,
                stroke_width=2,
            )
            text("Circuit inside structural concrete", a, top + 140, size=11)
        elif i == 1 and underfloor:
            for yy, h, color in (
                (66, 5, "#bd9f74"),
                (71, 19, "#f2e6d1"),
                (90, 7, "#d8bee9"),
                (97, 28, "#b8c1c5"),
            ):
                element("rect", x=a, y=top + yy, width=b - a, height=h, fill=color)
            element(
                "line",
                data_pipe="straight",
                x1=a + 8,
                x2=b - 8,
                y1=top + 81,
                y2=top + 81,
                stroke=underfloor_color,
                stroke_width=2,
            )
            text("Pipe in screed, above insulation", a, top + 148, size=11)
            text("Structural slab below", a, top + 166, size=11)
        elif i == 2 and (vents or ac):
            element("rect", x=a, y=top + 64, width=b - a, height=16, fill="#b8c1c5")
            if vents:
                element(
                    "line",
                    x1=a + 8,
                    x2=b - 36,
                    y1=top + 94,
                    y2=top + 94,
                    stroke="#288e91",
                    stroke_width=5,
                )
                mid = (a + b) / 2
                element(
                    "line",
                    x1=mid,
                    x2=mid,
                    y1=top + 94,
                    y2=top + 108,
                    stroke="#288e91",
                    stroke_width=2,
                )
                element(
                    "polygon",
                    points=f"{mid},{top+112} {mid-4},{top+104} {mid+4},{top+104}",
                    fill="#288e91",
                )
            if ac:
                element("rect", x=b - 4, y=top + 82, width=5, height=48, fill="#bfe4ef")
                element(
                    "rect",
                    x=b - 40,
                    y=top + 105,
                    width=27,
                    height=12,
                    rx=2,
                    fill="white",
                    stroke="#277bb8",
                )
                element(
                    "polyline",
                    points=f"{b-31},{top+119} {b-38},{top+126} {b-48},{top+129}",
                    fill="none",
                    stroke="#277bb8",
                )
            text("Duct below ceiling; unit by window", a, top + 148, size=11)
        else:
            text("Not configured in this example", a, top + 100, size=11)


def tone_system_symbols(root: ET.Element) -> None:
    """Give each object one hue; preserve heat/cold semantics between objects."""
    from colorsys import rgb_to_hls, hls_to_rgb

    bases = {
        "garden": "#a0aaa0",
        "pergola": "#a9a69e",
        "terrace": "#a0a9a9",
        "solar_thermal": "#657e87",
        "hvac_room": "#607e89",
        "district_heating": "#718591",
        "gas_boiler": "#718591",
        "oil_boiler": "#718591",
        "biomass_boiler": "#718591",
        "water_well": "#277bb8",
        "boreholes": "#c9533d",
    }
    for group in root.iter():
        kind = group.get("data-system", "").removeprefix("roof:")
        if kind not in bases:
            continue
        base = bases[kind]
        hue, _, saturation = rgb_to_hls(
            *(int(base[i : i + 2], 16) / 255 for i in (1, 3, 5))
        )
        silhouette = kind in {"garden", "pergola", "terrace"}
        for node in group.iter():
            if silhouette and node.get("fill-opacity"):
                node.set("fill-opacity", "1")
            for attr in ("fill", "stroke"):
                color = node.get(attr, "")
                if not color.startswith("#") or len(color) != 7:
                    continue
                _, brightness, _ = rgb_to_hls(
                    *(int(color[i : i + 2], 16) / 255 for i in (1, 3, 5))
                )
                rgb = hls_to_rgb(
                    hue,
                    0.65 if silhouette else max(0.35, min(0.82, brightness)),
                    min(saturation, 0.12),
                )
                node.set(attr, "#" + "".join(f"{round(v*255):02x}" for v in rgb))
