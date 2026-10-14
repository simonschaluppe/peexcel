"""Static architectural sections with schematic construction layers."""

from __future__ import annotations

from math import ceil, isfinite, radians, tan
from random import Random
from copy import deepcopy
from xml.etree import ElementTree as ET

from .equipment_svg import draw_equipment, attach_semantic_targets
from .themes import apply_theme, draw_background, style_tokens
from .annotations import label_usages
from .site_svg import draw_site_context, front_car
from .systems import (
    draw_systems,
    annotate_symbols,
    draw_construction_details,
    tone_system_symbols,
)

# Presentation only: variable definitions and labels remain in the schema.
_COLORS = {
    "office": "#bfd6e5",
    "residential": "#ecdbab",
    "schoolprim": "#ccdcca",
    "schoolsec": "#afd3cb",
    "retailfood": "#ebc4b7",
    "retailother": "#dbcee4",
    "other": "#c4c9ce",
    "unallocated": "#eeeeee",
}
_PV_COLOR = "#70868f"
_CONSTRUCTION_COLORS = {"default": "#69836d", "wood": "#c59b6d"}
_INSULATION_COLOR = "#ddd2e5"


def _floor_label(index: int) -> str:
    """Format a zero-based floor index, with negative indices for basements."""
    if index < 0:
        return "Basement" if index == -1 else f"Basement {abs(index)}"
    if index == 0:
        return "Ground floor"
    suffix = (
        "th"
        if 10 <= index % 100 <= 20
        else {1: "st", 2: "nd", 3: "rd"}.get(index % 10, "th")
    )
    return f"{index}{suffix} Floor"


def render_svg(
    section: dict,
    style: str = "architectural",
    *,
    construction: str = "default",
    facade_style: str | None = None,
    annotations: bool = False,
    palette: str | None = None,
    usage_labels: str = "auto",
) -> str:
    """Return an SVG with usage legend, floor labels and 15 m horizontal ticks.

    Horizontal and vertical scales are independent to keep storeys legible.
    Construction and insulation layers have fixed schematic drawing thicknesses.
    Styles are ``architectural``, ``hand_drawn`` (brush strokes and fineliner on warm paper),
    ``blueprint`` (drafting palette and grid). ``annotations=True`` enables
    matching callouts on any style; legacy ``style='annotations'`` aliases
    Blueprint with callouts. ``palette`` selects blue (default), green or beige
    for Blueprint only. ``usage_labels`` is 'auto' or 'none'.
    ``construction='wood'`` changes the construction color to light brown.
    ``facade_style='gründerzeit'`` adds schematic relief profiles. Omit this
    override to use per-building styles from the layout.
    """
    if style not in ("architectural", "hand_drawn", "blueprint", "annotations"):
        raise ValueError(f"Unknown section style: {style!r}")
    if not isinstance(annotations, bool):
        raise ValueError("annotations must be a boolean")
    if usage_labels not in {"auto", "none"}:
        raise ValueError("usage_labels must be auto or none")
    if style == "annotations":
        style, annotations = "blueprint", True
    tokens = style_tokens(style, palette)
    show_usage_labels = usage_labels == "auto"
    if construction not in _CONSTRUCTION_COLORS:
        raise ValueError(f"Unknown construction appearance: {construction!r}")
    if facade_style in ("gruenderzeit", "grunderzeit"):
        facade_style = "gründerzeit"
    if facade_style not in (None, "default", "gründerzeit"):
        raise ValueError("facade_style must be default or gründerzeit")
    colors = dict(_COLORS)
    construction_color = _CONSTRUCTION_COLORS[construction]
    insulation_color, pv_color = _INSULATION_COLOR, _PV_COLOR
    ink, paper = "#26323b", "white"
    if style in ("blueprint", "annotations"):
        colors = dict(
            zip(
                _COLORS,
                (
                    "#a7d1ec",
                    "#d8edf9",
                    "#bdddeb",
                    "#8bbddc",
                    "#c8e7f4",
                    "#e7f3fb",
                    "#78b0d1",
                    "#f2f9fd",
                ),
            )
        )
        construction_color = "#477fa5" if construction == "default" else "#739bb3"
        insulation_color, pv_color = "#c2e2f5", "#28678f"
        ink, paper = "#245779", "#f0f8fd"
    elif style == "hand_drawn":
        ink, paper = "#49463e", "#fffdf5"
    sketch_random = Random(42)
    wall_structure, wall_insulation = (
        tokens["wall_structure"],
        tokens["wall_insulation"],
    )
    wall_total = wall_structure + wall_insulation
    if not section["spaces"]:
        raise ValueError("The section must contain spaces")
    floors = {f["id"]: f for f in section["floors"]}
    roofs = {r["id"]: r for r in section["roofs"]}
    envelope = section["spaces"] + section.get("voids", [])
    xs, zs = [], []
    for space in envelope:
        floor = floors[space["floor_id"]]
        xs.extend([space["x_m"], space["x_m"] + space["width_m"]])
        zs.extend(
            [floor["z_m"] - floor["slab_thickness_m"], floor["z_m"] + floor["height_m"]]
        )
    for roof in roofs.values():
        xs.extend([roof["x_m"], roof["x_m"] + roof["width_m"]])
        zs.append(roof["z_m"])
    if not all(isfinite(v) for v in xs + zs):
        raise ValueError("Section coordinates must be finite")
    xmin, xmax, zmin, zmax = min(xs), max(xs), min(zs), max(zs)
    system_settings = section.get("systems", {}).get("buildings", {})
    if any(
        record.get("source") in {"ground", "groundwater"}
        or record["kind"] in {"boreholes", "water_well"}
        for record in section.get("equipment", [])
    ) or any(
        set(v["plant"]) & {"water_well", "boreholes"} for v in system_settings.values()
    ):
        zmin -= 3.5
    zmin = min(zmin - 0.6, -1.5)  # soil continues below the lowest floor
    # Wide districts can scroll horizontally; their storeys remain visible.
    xscale = max(4.0, min(18.0, 900 / max(xmax - xmin, 1)))
    yscale = max(22.0, 56 / min(f["height_m"] for f in floors.values()))
    roof_equipment = any(
        set(settings["roof"]) - {"pv"} for settings in system_settings.values()
    ) or any(
        record.get("resolved_location", {}).get("level") == "roof"
        for record in section.get("equipment", [])
    )
    left, top = 140.0, 220.0 if roof_equipment else 180.0
    width = max(1050.0, (xmax - xmin) * xscale + left + 142)
    bottom = top + (zmax - zmin) * yscale
    usage_names = {s["usage"]: s["label"] for s in section["spaces"]}
    usage_legend = [
        (usage_names[key], colors.get(key, "#c4c9ce")) for key in sorted(usage_names)
    ]
    if section.get("voids"):
        usage_legend.append(("Parking garage (schematic)", "#e2e5e7"))
    material_legend = [
        (
            "Wood construction" if construction == "wood" else "Construction",
            construction_color,
        ),
        ("Insulation", insulation_color),
        ("Windows", "#bfe5f2"),
        ("Service shaft / lift or stairs", "#d4d9db"),
    ]
    hvac_legend = [("PV modules (15° butterfly)", pv_color)]
    legend_symbols = {}
    if system_settings:
        for service, label, color in (
            ("heating", "Heating emission", "#c9533d"),
            ("cooling", "Cooling emission", "#277bb8"),
            ("ventilation", "Ventilation", "#288e91"),
            ("dhw", "Domestic hot water", "#b86b58"),
        ):
            if any(
                usage.get(service, "none") != "none"
                for settings in system_settings.values()
                for usage in settings["usages"].values()
            ):
                hvac_legend.append((label, color))
        symbols = sorted(
            set().union(
                *(
                    set(v["plant"]) | (set(v["roof"]) - {"pv"})
                    for v in system_settings.values()
                )
            )
        )
        for symbol in symbols:
            target = (
                material_legend
                if symbol in {"garden", "terrace", "pergola"}
                else hvac_legend
            )
            label = (
                "HVAC room"
                if symbol == "hvac_room"
                else symbol.replace("_", " ").capitalize()
            )
            target.append((label, "#495e6c"))
    for record in section.get("equipment", []):
        label = record["kind"].replace("_", " ").capitalize()
        label += (
            " (unlocated)"
            if not record.get("resolved_location")
            else " " + record["id"]
        )
        hvac_legend.append((label, "#7e969f"))
        if record.get("resolved_location"):
            legend_symbols[label] = record["kind"]
    legend_groups = [
        ("Usage", usage_legend),
        ("Material overlay", material_legend),
        ("HVAC overlay", hvac_legend),
    ]
    legend_top = bottom + 140
    legend_rows = max(len(items) for _, items in legend_groups) + 1
    height = legend_top + legend_rows * 29 + 88
    root = ET.Element(
        "svg",
        {
            "xmlns": "http://www.w3.org/2000/svg",
            "viewBox": f"0 0 {width:g} {height:g}",
            "width": f"{width:g}",
            "height": f"{height:g}",
            "data-style": style,
            "data-palette": (palette or "blue") if style == "blueprint" else "default",
            "data-annotations": str(annotations).lower(),
            "role": "img",
            "aria-label": "Schematic building section",
        },
    )

    def element(tag, **attrs):
        if style in ("blueprint", "annotations") and attrs.get("stroke") in (
            "white",
            "#687680",
            "#e5eaed",
        ):
            attrs["stroke"] = "#a6c9df" if attrs["stroke"] == "#e5eaed" else "#689abc"
        identifier = attrs.get("id", "")
        frame = (
            style == "hand_drawn"
            and tag == "rect"
            and identifier.endswith((":left", ":right"))
            and not identifier.startswith(("insulation:", "window:"))
        )
        if frame:
            attrs["fill"] = "none"
        if (
            style == "hand_drawn"
            and tag == "rect"
            and (
                identifier.startswith("slab:")
                or (identifier.startswith("r") and identifier[1:].isdigit())
                or identifier.startswith("insulation:r")
            )
        ):
            attrs["visibility"] = (
                "hidden"  # no separate ceiling/roof bands in the sketch
            )
        if style == "hand_drawn" and identifier.startswith("insulation:"):
            attrs["fill_opacity"] = 0.45
        node = ET.SubElement(
            root, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()}
        )
        if (
            style == "hand_drawn"
            and tag == "line"
            and attrs.get("stroke")
            in ("#687680", ink, "#71818a", tokens["annotation_edge"])
        ):
            node.set("opacity", "0")
            ax, ay, bx, by = (float(attrs[k]) for k in ("x1", "y1", "x2", "y2"))
            points = [
                (
                    ax + (bx - ax) * f,
                    ay + (by - ay) * f + sketch_random.uniform(-1.6, 1.6),
                )
                for f in (0, 0.25, 0.5, 0.75, 1)
            ]
            ET.SubElement(
                root,
                "path",
                {
                    "d": "M " + " L ".join(f"{a:.2f},{b:.2f}" for a, b in points),
                    "stroke": ink,
                    "stroke-width": "0.85",
                    "opacity": str(attrs.get("opacity", 1)),
                    "fill": "none",
                    "aria-hidden": "true",
                },
            )
        # Pencil outlines are decorative only: exact rectangles remain the geometry.
        identifier = attrs.get("id", "")
        if style == "hand_drawn" and tag == "rect" and (":s" in identifier or frame):
            px, py, w, h = (float(attrs[k]) for k in ("x", "y", "width", "height"))
            for pass_index in range(2):
                points = [
                    (px, py),
                    (px + w / 2, py),
                    (px + w, py),
                    (px + w, py + h / 2),
                    (px + w, py + h),
                    (px + w / 2, py + h),
                    (px, py + h),
                    (px, py + h / 2),
                    (px, py),
                ]
                jitter = min(2.4, max(0.5, w / 3), h / 5)
                coords = [
                    (
                        a + sketch_random.uniform(-jitter, jitter),
                        b + sketch_random.uniform(-jitter, jitter),
                    )
                    for a, b in points
                ]
                path = "M " + " L ".join(f"{a:.2f},{b:.2f}" for a, b in coords)
                ET.SubElement(
                    root,
                    "path",
                    {
                        "d": path,
                        "fill": "none",
                        "stroke": ink,
                        "stroke-width": "0.8",
                        "opacity": "0.5" if pass_index else "0.7",
                        "pointer-events": "none",
                        "aria-hidden": "true",
                    },
                )
        return node

    def text(value, x, y, size=12, **attrs):
        if style == "hand_drawn":
            attrs.setdefault("font_weight", 700)
            size += 2
        node = element(
            "text",
            x=x,
            y=y,
            font_family=(
                "Ink Free, Segoe Print, Bradley Hand, Comic Sans MS, cursive"
                if style == "hand_drawn"
                else "sans-serif"
            ),
            font_size=size,
            fill=ink,
            **attrs,
        )
        if style == "hand_drawn":
            # Small per-letter rotations keep handwriting lively without changing words.
            node.set(
                "rotate", " ".join(f"{sketch_random.uniform(-5, 5):.1f}" for _ in value)
            )
        node.text = value

    def x(value):
        return left + (value - xmin) * xscale

    def y(value):
        return top + (zmax - value) * yscale

    def describe(node, kind, description):
        node.set("data-kind", kind)
        node.set("aria-label", description)
        ET.SubElement(node, "title").text = description

    element("title").text = f"{section['source']['column_name']} — schematic section"
    element("desc").text = (
        "Independent horizontal and vertical scales; fixed schematic construction and insulation layers. "
        + " ".join(n["description"] for n in section["assumptions"])
    )
    draw_background(root, tokens, width, height, y(0))
    if style in ("blueprint", "annotations"):
        # A pale drafting grid sits behind the geometry, never behind the labels.
        for gx in range(int(left), int(x(xmax)) + 1, 20):
            element(
                "line",
                x1=gx,
                x2=gx,
                y1=top - 35,
                y2=bottom,
                stroke="#dcecf6",
                stroke_width=0.6,
            )
        for gy in range(int(top - 35), int(bottom) + 1, 20):
            element(
                "line",
                x1=left,
                x2=x(xmax),
                y1=gy,
                y2=gy,
                stroke="#dcecf6",
                stroke_width=0.6,
            )
    soil_top = y(0)
    element(
        "rect",
        data_kind="underground",
        x=left - 118,
        y=soil_top,
        width=x(xmax) - left + 236,
        height=bottom - soil_top,
        fill="url(#section-soil)",
    )
    for gx in range(int(left - 110), int(x(xmax) + 100), 22):
        element(
            "line",
            x1=gx,
            x2=gx + 7,
            y1=soil_top + 8,
            y2=soil_top + 14,
            stroke="#abc1cd" if style in ("blueprint", "annotations") else "#d3c8b7",
            stroke_width=0.8,
        )
    element(
        "line",
        x1=left - 118,
        x2=x(xmax) + 118,
        y1=soil_top,
        y2=soil_top,
        stroke=ink,
        stroke_width=1.1,
    )
    text(section["source"]["column_name"], left, 30, size=18, font_weight=600)
    text("Schematic section · independent horizontal and vertical scales", left, 52)
    for index in sorted({f["index"] for f in floors.values()}):
        floor = next(f for f in floors.values() if f["index"] == index)
        cy = y(floor["z_m"] + floor["height_m"] / 2)
        text(_floor_label(index), left - 14, cy + 4, text_anchor="end")
        element(
            "line",
            x1=left - 6,
            x2=x(xmax),
            y1=y(floor["z_m"]),
            y2=y(floor["z_m"]),
            stroke="#e5eaed",
            stroke_width=1,
        )
    building_axes = []
    for building_index, building in enumerate(section["buildings"]):
        members = [s for s in envelope if s["floor_id"] in building["floor_ids"]]
        if not members:
            continue
        a = min(s["x_m"] for s in members)
        b = max(s["x_m"] + s["width_m"] for s in members)
        depth = building.get("depth_m", section.get("depth_m") or 15.0)
        building_axes.append((building["id"], a, b, depth))
        text(
            f"Depth {depth:g} m",
            x((a + b) / 2),
            130 if style == "hand_drawn" else 99,
            text_anchor="middle",
        )
        name = building.get("name", f"Building {building_index + 1}")
        center = x((a + b) / 2)
        if style == "hand_drawn":
            note_width = max(150, min(310, len(name) * 9 + 34))
            angle = 0
            transform = f"rotate({angle} {center} 76)"
            element(
                "rect",
                x=center - note_width / 2 + 2,
                y=69,
                width=note_width,
                height=44,
                fill="#c6b98a",
                opacity=0.25,
                transform=transform,
            )
            element(
                "rect",
                data_decoration="sticky-note",
                x=center - note_width / 2,
                y=66,
                width=note_width,
                height=44,
                fill="#ffe879",
                transform=transform,
            )
            text(
                name,
                center,
                94,
                size=16,
                text_anchor="middle",
                transform=transform,
                font_weight=700,
            )
        else:
            text(name, center, 79, text_anchor="middle")

    draw_site_context(section, building_axes, element, text, x, y, xscale, wall_total)
    for space in section["spaces"]:
        floor = floors[space["floor_id"]]
        rect = element(
            "rect",
            id=space["id"],
            x=x(space["x_m"]),
            y=y(floor["z_m"] + floor["height_m"]),
            width=space["width_m"] * xscale,
            height=floor["height_m"] * yscale,
            fill=colors.get(space["usage"], "#c4c9ce"),
            stroke="white",
            stroke_width=1,
        )
        ET.SubElement(rect, "title").text = f"{space['label']}: {space['area_m2']:g} m²"
        if style == "hand_drawn":
            rect.set("fill-opacity", "0.18")
            rect.set("stroke", "none")
            px, py, sw, sh = (float(rect.get(k)) for k in ("x", "y", "width", "height"))
            clip_id = f"wash:{space['id']}"
            clip = ET.SubElement(root, "clipPath", {"id": clip_id})
            ET.SubElement(
                clip,
                "rect",
                {"x": str(px), "y": str(py), "width": str(sw), "height": str(sh)},
            )
            wash = ET.SubElement(
                root,
                "g",
                {
                    "clip-path": f"url(#{clip_id})",
                    "data-decoration": "usage-strokes",
                    "aria-hidden": "true",
                },
            )
            for row in range(ceil(sh / 7) + 1):
                sy = py + row * 7 + sketch_random.uniform(-2, 2)
                inset = sketch_random.uniform(0, min(7, sw / 5))
                path = f"M {px + inset},{sy} Q {px + sw / 2},{sy + sketch_random.uniform(-5, 5)} {px + sw - inset},{sy + sketch_random.uniform(-3, 3)}"
                ET.SubElement(
                    wash,
                    "path",
                    {
                        "d": path,
                        "fill": "none",
                        "stroke": colors.get(space["usage"], "#c4c9ce"),
                        "stroke-width": f"{sketch_random.uniform(5, 11):.2f}",
                        "opacity": "0.65",
                        "stroke-linecap": "round",
                    },
                )
    for void in section.get("voids", []):
        floor = floors[void["floor_id"]]
        node = element(
            "rect",
            id=void["id"],
            x=x(void["x_m"]),
            y=y(floor["z_m"] + floor["height_m"]),
            width=void["width_m"] * xscale,
            height=floor["height_m"] * yscale,
            fill="#e2e5e7",
            stroke="#b6bdc4",
            stroke_width=1,
            stroke_dasharray="3 3",
        )
        ET.SubElement(node, "title").text = (
            f"Schematic parking garage: {void['area_m2']:g} m², excluded from scenario NFA"
        )
        node.set("data-use", "parking-garage")
        garage_left, garage_width = x(void["x_m"]), void["width_m"] * xscale
        garage_bottom = y(floor["z_m"])
        settings = system_settings.get(floor["building_id"], {})
        building_floors = [
            f for f in floors.values() if f["building_id"] == floor["building_id"]
        ]
        candidates = [
            s
            for s in envelope
            if s["floor_id"] == floor["id"]
            and (s.get("usage") == "other" or s.get("kind") == "empty_basement")
        ]
        if (
            "heating_room" in settings.get("plant", [])
            and floor["index"] == min(f["index"] for f in building_floors)
            and candidates
            and max(candidates, key=lambda s: s["width_m"])["id"] == void["id"]
        ):
            # Keep parking symbols outside the plant-room overlay drawn later.
            reserved = min(240, max(8, garage_width - 16)) + 16
            garage_left += reserved
            garage_width = max(0, garage_width - reserved)
        for n in range(max(1, int(garage_width / 65)) if garage_width >= 20 else 0):
            cx = garage_left + (n + 0.5) * garage_width / max(1, int(garage_width / 65))
            front_car(element, cx, garage_bottom, min(26, garage_width * 0.65))
        if garage_width > 65:
            text(
                "P · Parking",
                garage_left + 8,
                y(floor["z_m"] + floor["height_m"]) + 19,
                size=11,
            )
    # Interior details are overlays only, never additional scenario spaces.
    shaft_spans = {}
    for building in section["buildings"]:
        members = [s for s in envelope if s["floor_id"] in building["floor_ids"]]
        if not members:
            continue
        a = min(s["x_m"] for s in members)
        b = max(s["x_m"] + s["width_m"] for s in members)
        center, shaft_width = (a + b) / 2, building.get("circulation", {}).get(
            "shaft_width_m", min(2.0, (b - a) * 0.15)
        )
        shaft_spans[building["id"]] = (
            center - shaft_width / 2,
            center + shaft_width / 2,
        )
    room_spacing = {
        "residential": 5,
        "office": 6,
        "schoolprim": 8,
        "schoolsec": 8,
        "retailfood": 12,
        "retailother": 9,
        "other": 8,
    }
    for space in section["spaces"]:
        floor = floors[space["floor_id"]]
        shaft_left, shaft_right = shaft_spans[floor["building_id"]]
        rooms = max(1, round(space["width_m"] / room_spacing.get(space["usage"], 8)))
        for index in range(1, rooms):
            wall_x = space["x_m"] + space["width_m"] * index / rooms
            if shaft_left - 0.3 <= wall_x <= shaft_right + 0.3:
                continue
            element(
                "line",
                data_kind="interior-wall",
                x1=x(wall_x),
                x2=x(wall_x),
                y1=y(floor["z_m"] + floor["height_m"]),
                y2=y(floor["z_m"]),
                stroke="#71818a",
                stroke_width=1.1,
                opacity=0.28,
            )
    for floor in floors.values():
        members = [s for s in envelope if s["floor_id"] == floor["id"]]
        if not members:
            continue
        shaft_left, shaft_right = shaft_spans[floor["building_id"]]
        a = max(shaft_left, min(s["x_m"] for s in members))
        b = min(shaft_right, max(s["x_m"] + s["width_m"] for s in members))
        if b <= a:
            continue
        py = y(floor["z_m"] + floor["height_m"])
        node = element(
            "rect",
            data_kind="service-shaft",
            data_building=floor["building_id"],
            data_floor=floor["id"],
            x=x(a),
            y=py,
            width=(b - a) * xscale,
            height=floor["height_m"] * yscale,
            fill="#d4d9db",
            fill_opacity=0.85,
            stroke="#71818a",
            stroke_width=0.8,
        )
        ET.SubElement(node, "title").text = (
            "Schematic service shaft overlay; no area deducted"
        )
        element(
            "line",
            x1=x((a + b) / 2),
            x2=x((a + b) / 2),
            y1=py + 3,
            y2=y(floor["z_m"]) - 3,
            stroke="#71818a",
            stroke_width=1,
            stroke_dasharray="3 4",
            opacity=0.5,
        )
    # Slabs meet the construction face; insulation continues outside them.
    for floor in floors.values():
        members = [s for s in envelope if s["floor_id"] == floor["id"]]
        if not members:
            continue
        a = min(s["x_m"] for s in members)
        b = max(s["x_m"] + s["width_m"] for s in members)
        element(
            "rect",
            id=f"slab:{floor['id']}",
            data_kind="slab",
            x=x(a) - wall_structure,
            y=y(floor["z_m"]),
            width=(b - a) * xscale + 2 * wall_structure,
            height=floor["slab_thickness_m"] * yscale,
            fill=construction_color,
        )
    for facade in section.get("facades", []):
        px = x(facade["x_m"])
        left_side = facade["side"] == "left"
        py = y(facade["z_m"] + facade["height_m"])
        fh = facade["height_m"] * yscale
        slab_height = floors[facade["floor_id"]]["slab_thickness_m"] * yscale
        node = element(
            "rect",
            id=facade["id"],
            x=px - wall_structure if left_side else px,
            y=py,
            width=wall_structure,
            height=fh,
            fill=construction_color,
        )
        describe(node, "facade", "Façade construction — schematic thickness")
        element(
            "rect",
            id=f"insulation:{facade['id']}",
            data_kind="insulation",
            x=px - wall_total if left_side else px + wall_structure,
            y=py - slab_height,
            width=wall_insulation,
            height=fh + 2 * slab_height,
            fill=insulation_color,
        )
    # Equivalent window bands represent the supplied glazing fraction, not measured openings.
    for facade in section.get("facades", []):
        wh = facade.get("window_height_m", 0) * yscale
        if wh <= 0:
            continue
        px = x(facade["x_m"])
        py = y(facade["z_m"] + facade["height_m"] / 2) - wh / 2
        wx = px - wall_total if facade["side"] == "left" else px
        element("rect", x=wx, y=py, width=wall_total, height=wh, fill=paper)
        node = element(
            "rect",
            id=f"window:{facade['id']}",
            data_kind="window",
            data_glazing_ratio=facade["glazing_ratio"],
            x=wx + 1,
            y=py,
            width=wall_total - 2,
            height=wh,
            fill="#bfe5f2",
            stroke="#40869b",
            stroke_width=0.8,
        )
        ET.SubElement(node, "title").text = (
            f"{facade.get('exposure', facade['side']).capitalize()} facade: {facade['glazing_ratio']:.0%} glazing; equivalent opening"
        )
        element(
            "line",
            x1=wx + wall_total / 2,
            x2=wx + wall_total / 2,
            y1=py,
            y2=py + wh,
            stroke="#40869b",
            stroke_width=0.7,
        )
    for roof in roofs.values():
        supporting_space = next(s for s in envelope if s["id"] == roof["space_id"])
        slab_height = floors[supporting_space["floor_id"]]["slab_thickness_m"] * yscale
        node = element(
            "rect",
            id=roof["id"],
            x=x(roof["x_m"]) - wall_structure,
            y=y(roof["z_m"]),
            width=roof["width_m"] * xscale + 2 * wall_structure,
            height=max(slab_height, wall_structure),
            fill=construction_color,
        )
        describe(node, "roof", "Roof construction — schematic thickness")
        element(
            "rect",
            id=f"insulation:{roof['id']}",
            data_kind="insulation",
            x=x(roof["x_m"]) - wall_total,
            y=y(roof["z_m"]) - wall_insulation,
            width=roof["width_m"] * xscale + 2 * wall_total,
            height=wall_insulation,
            fill=insulation_color,
        )
    # Historic relief is an exterior section profile, never an inferred wall assembly.
    buildings_by_id = {b["id"]: b for b in section["buildings"]}
    for facade in section.get("facades", []):
        building = buildings_by_id[facade["building_id"]]
        appearance = facade_style or facade.get(
            "facade_style", building.get("facade_style", "default")
        )
        floor = floors[facade["floor_id"]]
        if appearance != "gründerzeit" or floor["index"] < 0:
            continue
        outward = -1 if facade["side"] == "left" else 1
        face_x = x(facade["x_m"]) + outward * wall_total
        top_y = y(facade["z_m"] + facade["height_m"])
        base_y = y(facade["z_m"])
        wh = facade.get("window_height_m", 0) * yscale
        window_top = (top_y + base_y - wh) / 2
        window_bottom = window_top + wh
        relief = element(
            "g",
            data_decoration="facade-relief",
            data_facade_style="gründerzeit",
            data_building=building["id"],
            data_facade=facade["id"],
        )
        ET.SubElement(relief, "title").text = (
            "Gründerzeit section profile: rusticated base, sill and lintel mouldings, stringcourses and stepped cornice; schematic relief"
        )

        def mould(level, height, projection, shade):
            ET.SubElement(
                relief,
                "rect",
                {
                    "x": str(face_x - projection if outward < 0 else face_x),
                    "y": str(level),
                    "width": str(projection),
                    "height": str(max(0.1, height)),
                    "fill": shade,
                },
            )

        stone, shade = (
            ("#b7c8d1", "#8fa7b5")
            if style in ("blueprint", "annotations")
            else ("#d2ccbf", "#aaa497")
        )
        mould(top_y, max(0, window_top - top_y), 2.5, stone)
        mould(window_bottom, max(0, base_y - window_bottom), 2.5, stone)
        projection = 8 if facade.get("exposure") == "street" else 5
        if wh > 0:
            mould(window_top - 4, 2, projection, stone)
            mould(window_top - 2, 1, projection - 2, shade)
            mould(window_bottom, 2.5, projection, stone)
            mould(window_bottom + 2.5, 1, projection - 1, shade)
        mould(base_y, 2, projection - 1, stone)  # continuous floor band
        if floor["index"] == 0:
            for level in range(int(top_y + 7), int(base_y), 9):
                if not window_top - 4 <= level <= window_bottom + 4:
                    mould(level, 1, 3.5, shade)
        roof_level = any(
            r["building_id"] == building["id"]
            and abs(r["z_m"] - facade["z_m"] - facade["height_m"]) < 1e-7
            and r["x_m"] - 1e-7 <= facade["x_m"] <= r["x_m"] + r["width_m"] + 1e-7
            for r in roofs.values()
        )
        if roof_level:
            for offset, reach in (
                (0, projection + 4),
                (2, projection + 2),
                (4, projection),
            ):
                mould(top_y + offset, 2, reach, stone if offset != 2 else shade)
    hidden_pv = 0.0
    for index, placement in enumerate(section["pv"]["placements"]):
        roof = roofs[placement["roof_id"]]
        if (
            roof["building_id"] in system_settings
            and "pv" not in system_settings[roof["building_id"]]["roof"]
        ):
            hidden_pv += placement["module_area_m2"]
            continue
        px = x(roof["x_m"] + placement["offset_m"])
        pw = placement["width_m"] * xscale
        py = y(roof["z_m"])
        pairs = max(1, ceil(pw / 48))
        pair_width = pw / pairs
        rise = pair_width / 2 * tan(radians(placement.get("tilt_deg", 15)))
        valley = py - 24
        node = element(
            "g",
            id=f"pv{index}",
            x=px,
            y=valley - rise,
            width=pw,
            height=rise + 3,
            data_tilt_deg=15,
        )
        describe(
            node,
            "pv",
            f"PV module area: {placement['module_area_m2']:g} m²; butterfly modules tilted 15 degrees",
        )
        for pair in range(pairs):
            start, middle, end = (
                px + pair * pair_width,
                px + (pair + 0.5) * pair_width,
                px + (pair + 1) * pair_width,
            )
            ET.SubElement(
                node,
                "line",
                {
                    "x1": str(middle),
                    "x2": str(middle),
                    "y1": str(valley + 3),
                    "y2": str(py - wall_insulation),
                    "stroke": pv_color,
                    "stroke-width": "1.5",
                },
            )
            for wing, (a, ay, b, by) in enumerate(
                (
                    (start, valley - rise, middle, valley),
                    (middle, valley, end, valley - rise),
                )
            ):
                points = ((a, ay), (b, by), (b, by + 3), (a, ay + 3))
                ET.SubElement(
                    node,
                    "polygon",
                    {
                        "points": " ".join(f"{u:.3f},{v:.3f}" for u, v in points),
                        "fill": pv_color if wing == 0 else "#9aa9b0",
                        "stroke": ink,
                        "stroke-width": "0.7",
                        "data-module-tilt-deg": "15",
                    },
                )
    draw_systems(section, element, text, x, y, yscale, bottom)
    draw_equipment(section, element, text, x, y, yscale, bottom)
    tone_system_symbols(root)
    # Shaft stays legible above local equipment and pipes; it is an area-neutral overlay.
    for shaft in [e for e in root if e.get("data-kind") == "service-shaft"]:
        sx, sy, sw, sh = (float(shaft.get(k)) for k in ("x", "y", "width", "height"))
        shaft.set("fill-opacity", "1")
        root.remove(shaft)
        root.append(shaft)
        bid = shaft.get("data-building")
        building_index = next(
            i for i, b in enumerate(section["buildings"]) if b["id"] == bid
        )
        circulation = (
            section["buildings"][building_index]
            .get("circulation", {})
            .get("kind", "elevator" if building_index % 2 == 0 else "stairs")
        )
        if circulation == "none":
            continue
        shaft.set("data-circulation", circulation)
        g = element("g", data_circulation=circulation, data_building=bid)

        def circulation_shape(tag, **attrs):
            return ET.SubElement(
                g, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()}
            )

        if circulation == "elevator":
            for fraction in (0.18, 0.82):
                element(
                    "line",
                    data_service="riser",
                    x1=sx + sw * fraction,
                    x2=sx + sw * fraction,
                    y1=sy,
                    y2=sy
                    + sh
                    + floors[shaft.get("data-floor")]["slab_thickness_m"] * yscale,
                    stroke="#909c9f",
                    stroke_width=0.8,
                )
            if floors[shaft.get("data-floor")]["index"] == 0:
                circulation_shape(
                    "rect",
                    x=sx + 2,
                    y=sy + sh * 0.2,
                    width=max(1, sw - 4),
                    height=sh * 0.73,
                    fill="#eff1f0",
                    stroke="#768589",
                    stroke_width=1,
                )
                circulation_shape(
                    "line",
                    x1=sx + sw / 2,
                    x2=sx + sw / 2,
                    y1=sy + sh * 0.2,
                    y2=sy + sh * 0.93,
                    stroke="#a2abad",
                    stroke_width=0.7,
                )
                circulation_shape(
                    "line",
                    x1=sx + sw / 2,
                    x2=sx + sw / 2,
                    y1=sy,
                    y2=sy + sh * 0.2,
                    stroke="#768589",
                    stroke_width=0.8,
                )
        else:
            # Two switchback flights and a half landing, shown as a section symbol.
            for flight in range(2):
                yy = sy + sh - flight * sh / 2
                path = f"M {sx+2 if flight==0 else sx+sw-2},{yy}"
                for step in range(1, 7):
                    xx = (
                        sx + 2 + (sw - 4) * step / 6
                        if flight == 0
                        else sx + sw - 2 - (sw - 4) * step / 6
                    )
                    path += f" H {xx} V {yy-step*sh/12}"
                circulation_shape(
                    "path", d=path, fill="none", stroke="#7d8a8d", stroke_width=1
                )
            circulation_shape(
                "line",
                x1=sx + 1,
                x2=sx + sw - 1,
                y1=sy + sh / 2,
                y2=sy + sh / 2,
                stroke="#7d8a8d",
                stroke_width=1,
            )

    axis_y = bottom + 23
    element("line", x1=left, x2=x(xmax), y1=axis_y, y2=axis_y, stroke="#687680")
    text("m", left - 25, axis_y + 22, text_anchor="end")
    text("m²", left - 25, axis_y + 42, text_anchor="end")
    for bid, start, end, depth in building_axes:
        for tick in range(0, int(end - start + 1e-9) + 1, 15):
            tx = x(start + tick)
            element(
                "line",
                data_kind="axis-tick",
                data_building=bid,
                data_distance_m=tick,
                data_area_m2=tick * depth,
                x1=tx,
                x2=tx,
                y1=axis_y,
                y2=axis_y + 6,
                stroke="#687680",
            )
            text(str(tick), tx, axis_y + 22, text_anchor="middle")
            text(f"{tick * depth:g}", tx, axis_y + 42, text_anchor="middle")
    text(
        "Per-building length and floor area per storey · tick interval 15 m",
        left,
        axis_y + 67,
    )
    for column, (heading, items) in enumerate(legend_groups):
        lx = left + column * ((width - left - 25) / 3)
        text(heading, lx, legend_top, size=15, font_weight=700)
        for row, (label, color) in enumerate(items, 1):
            ly = legend_top + row * 29
            key = legend_symbols.get(label, label.lower().replace(" ", "_"))
            if key in {"garden", "pergola", "terrace", "solar_thermal", "hvac_room"}:
                key = "roof:" + key
            sample = next((e for e in root.iter() if e.get("data-system") == key), None)
            if sample is not None:
                ax, ay = float(sample.get("data-anchor-x", 0)), float(
                    sample.get("data-anchor-y", 0)
                )
                if sample.get("data-roof-tile"):
                    box = (
                        float(sample.get("data-left")),
                        float(sample.get("data-base-y")) - 50,
                        float(sample.get("data-width")),
                        52,
                    )
                elif key == "roof:hvac_room":
                    rw = float(sample.get("data-room-width"))
                    box = (ax - rw / 2 - 2, ay - 25, rw + 4, 65)
                elif key in {"water_well", "boreholes"}:
                    box = (ax - 16, ay - 35, 32, 70)
                elif key == "heating_room":
                    box = (ax - 120, ay - 10, 240, 52)
                else:
                    box = (ax - 28, ay - 14, 56, 30)
                preview = element(
                    "svg",
                    data_legend_symbol=key,
                    x=lx,
                    y=ly - 21,
                    width=39,
                    height=25,
                    viewBox=" ".join(str(v) for v in box),
                )
                clone = deepcopy(sample)
                for node in clone.iter():
                    for attr in list(node.attrib):
                        if attr.startswith("data-") or attr == "id":
                            del node.attrib[attr]
                preview.append(clone)
            elif label in {
                "Heating emission",
                "Cooling emission",
                "Ventilation",
                "Domestic hot water",
            }:
                element(
                    "line",
                    x1=lx,
                    x2=lx + 35,
                    y1=ly - 5,
                    y2=ly - 5,
                    stroke=color,
                    stroke_width=2,
                )
            elif label.startswith("PV modules"):
                element(
                    "polyline",
                    points=f"{lx},{ly-12} {lx+17},{ly-6} {lx+34},{ly-12}",
                    fill="none",
                    stroke=color,
                    stroke_width=3,
                )
            else:
                element("rect", x=lx, y=ly - 12, width=18, height=14, fill=color)
            text(label, lx + 46, ly)
    foot_y = legend_top + legend_rows * 29 + 12
    pv = section["pv"]
    requested, unplaced = pv["requested_area_m2"], pv["unplaced_area_m2"]
    summary = (
        "PV area unknown."
        if requested is None
        else (
            f"PV module area: {requested:g} m²; placed: {requested - unplaced:g} m²; unplaced: {unplaced:g} m²."
        )
    )
    if hidden_pv:
        summary += f" Hidden by overlay: {hidden_pv:g} m²."
    text(summary, left, foot_y)
    text(
        "Depth shown per building \u00b7 gaps [m]: "
        + (", ".join(f"{g:g}" for g in section.get("gaps_m", [20])) or "none")
        + (" \u00b7 HVAC/roof symbols are illustrative" if system_settings else ""),
        left,
        foot_y + 23,
    )
    if show_usage_labels:
        label_usages(section, text, x, y, yscale, hand_drawn=style == "hand_drawn")
    if annotations:
        annotate_symbols(root, element, text, width, height, tokens=tokens)
    attach_semantic_targets(root, section)
    apply_theme(root, tokens)
    return ET.tostring(root, encoding="unicode")


def render_emission_details_svg(section: dict) -> str:
    """Return the enlarged emission construction details as an independent SVG."""
    root = ET.Element(
        "svg",
        xmlns="http://www.w3.org/2000/svg",
        width="1080",
        height="230",
        viewBox="0 0 1080 230",
        role="img",
    )
    ET.SubElement(root, "title").text = "Emission systems: construction details"

    def element(tag, **attrs):
        return ET.SubElement(
            root, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()}
        )

    def text(value, x, y, size=12, **attrs):
        element(
            "text",
            x=x,
            y=y,
            font_family="sans-serif",
            font_size=size,
            fill="#26323b",
            **attrs,
        ).text = value

    element("rect", x=0, y=0, width=1080, height=230, fill="white")
    if section.get("systems"):
        draw_construction_details(section, element, text, 20, 28, 1040)
    else:
        text("No emission systems configured.", 20, 35)
    return ET.tostring(root, encoding="unicode")
