"""Draw resolved equipment records once, with explicit location and service links."""

from xml.etree import ElementTree as ET
from ._svg_types import CoordinateMap, ElementFactory, TextWriter
from .component_symbols import draw_plant_symbol, draw_source, line, shape


def draw_equipment(
    section: dict,
    element: ElementFactory,
    text: TextWriter,
    x: CoordinateMap,
    y: CoordinateMap,
    yscale: float,
    soil_bottom: float | None = None,
) -> None:
    """Draw explicitly located plant once and connect served building references."""
    buildings = {b["id"]: b for b in section["buildings"]}
    occupied = {}
    for record in section.get("equipment", []):
        location = record.get("resolved_location")
        if not location:
            continue  # Listed as unlocated in assumptions; no invented physical position.
        b = buildings[location["building"]]
        level = location["level"]
        if level == "roof":
            z = max(r["z_m"] for r in section["roofs"] if r["building_id"] == b["id"])
        else:
            f = next(
                f
                for f in section["floors"]
                if f["building_id"] == b["id"] and f["index"] == level
            )
            z = f["z_m"]
        key = (b["id"], level)
        index = occupied.get(key, 0)
        occupied[key] = index + 1
        # Reserve space for pipe connections and the central service shaft.
        span = x(b["x_m"] + b["width_m"]) - x(b["x_m"])
        width = max(8, min(38, span / 5))
        columns = max(1, int((span * 0.45 - 16) / (width + 24)))
        px = x(b["x_m"]) + 14 + (index % columns) * (width + 24)
        py = y(z) - 4 - 48 * (index // columns)
        g = element(
            "g",
            data_kind="equipment",
            data_system=record["kind"],
            data_semantic_id=record["semantic_id"],
            data_building=b["id"],
        )
        ET.SubElement(g, "title").text = (
            record["kind"].replace("_", " ")
            + "; serves "
            + ", ".join(record.get("serves", []))
            + " (schematic)"
        )
        kind = record["kind"]
        center = px + width / 2
        if kind == "heating_room":
            shape(
                g,
                "rect",
                x=px - 5,
                y=py - 49,
                width=max(width, span * 0.4),
                height=49,
                fill="none",
                stroke="#80939a",
                stroke_dasharray="4 2",
            )
            g.set("data-anchor-x", str(center))
            g.set("data-anchor-y", str(py - 49))
        elif kind in {"water_well", "boreholes"}:
            draw_source(
                g,
                "groundwater" if kind == "water_well" else "boreholes",
                center,
                y(0),
                soil_bottom or y(0) + 60,
            )
            g.set("data-anchor-x", str(center))
            g.set("data-anchor-y", str(y(0) + 28))
        else:
            draw_plant_symbol(
                g, kind, center, py, width, mode=record.get("mode", "heating")
            )
        source = record.get("source", "unknown")
        if source != "unknown":
            source_x = x(b["x_m"]) - 52
            source_group = element(
                "g",
                data_kind="system",
                data_system="source:" + source,
                data_building=b["id"],
                data_semantic_id=record["semantic_id"],
                data_anchor_x=source_x,
                data_anchor_y=y(0) + 20,
            )
            draw_source(source_group, source, source_x, y(0), soil_bottom or y(0) + 70)
            shape(
                source_group,
                "path",
                d=f"M {source_x},{y(0)+8} H {px-8} V {py-10} H {px}",
                fill="none",
                stroke="#668b9b",
                stroke_width=1.3,
            )
        if "dhw" in record.get("services", []):
            shape(
                g,
                "path",
                data_service="dhw",
                d=f"M {px+width},{py-10} H {px+width+10} V {y(0)-25}",
                fill="none",
                stroke="#b86b58",
                stroke_width=1.5,
            )
        for target in record.get("serves", []):
            if target == b["id"]:
                continue
            other = buildings[target]
            tx = x(other["x_m"] + other["width_m"] / 2)
            element(
                "path",
                data_kind="service-connection",
                data_equipment=record["id"],
                data_serves=target,
                data_semantic_id=record["semantic_id"],
                d=f"M {px+width/2} {py} V {y(0)+12} H {tx} V {y(0)}",
                fill="none",
                stroke="#8a9ca2",
                stroke_width=1,
                stroke_dasharray="4 3",
            )


def attach_semantic_targets(root: ET.Element, section: dict) -> None:
    """Attach style-independent selection targets to SVG surfaces and layers."""
    targets = {}
    for category in ("spaces", "floors", "facades", "roofs"):
        for item in section.get(category, []):
            if "semantic_id" in item:
                targets[item["id"]] = item["semantic_id"]
    for i, pv in enumerate(section["pv"]["placements"]):
        targets[f"pv{i}"] = pv.get("semantic_id", "pv:" + str(i))
    for node in root.iter():
        key = node.get("id", "")
        owner = node.get("data-facade")
        if key.startswith(("insulation:", "window:", "slab:")):
            owner = key.split(":", 1)[1]
        target = targets.get(key) or targets.get(owner)
        if target:
            node.set("data-semantic-id", target)
