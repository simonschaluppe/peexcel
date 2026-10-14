"""Optional, style-aware callouts that refer to symbols in the same section."""

from textwrap import wrap
from xml.etree import ElementTree as ET

from ._svg_types import CoordinateMap, ElementFactory, TextWriter


def label_usages(
    section: dict,
    text: TextWriter,
    x: CoordinateMap,
    y: CoordinateMap,
    yscale: float,
    *,
    hand_drawn: bool = False,
) -> None:
    """Label the clear part of each space without covering the central shaft.

    Long metadata labels wrap to two lines; narrow fragments use the full legend
    and SVG title instead of reducing the font to an unreadable size.
    """
    floors = {floor["id"]: floor for floor in section["floors"]}
    buildings = {building["id"]: building for building in section["buildings"]}
    for space in section["spaces"]:
        floor = floors[space["floor_id"]]
        building = buildings[floor["building_id"]]
        left, right = x(space["x_m"]), x(space["x_m"] + space["width_m"])
        center = x(building["x_m"] + building["width_m"] / 2)
        shaft_width = building.get("circulation", {}).get(
            "shaft_width_m", min(2, building["width_m"] * 0.15)
        ) * (x(1) - x(0))
        spans = [
            (left + 10, min(right - 10, center - shaft_width / 2 - 7)),
            (max(left + 10, center + shaft_width / 2 + 7), right - 10),
        ]
        start, end = max(spans, key=lambda span: span[1] - span[0])
        char_width = 7 if hand_drawn else 5.8
        max_chars = int((end - start) / char_width)
        label = space["label"].removeprefix("NGF ").removeprefix("NFA ")
        lines = wrap(label, width=max(1, max_chars), break_long_words=False)
        if (
            max_chars < 9
            or len(lines) > 2
            or any(len(line) > max_chars for line in lines)
        ):
            continue
        top = y(floor["z_m"] + floor["height_m"])
        baseline = top + floor["height_m"] * yscale * 0.53 - 7 * (len(lines) - 1)
        for row, label_line in enumerate(lines):
            text(
                label_line,
                start,
                baseline + 14 * row,
                size=10,
                data_usage_label=space["usage"],
                data_semantic_id=space.get("semantic_id", space["id"]),
            )


def annotate_symbols(
    root: ET.Element,
    element: ElementFactory,
    text: TextWriter,
    width: float,
    height: float,
    *,
    tokens: dict | None = None,
) -> None:
    """Add non-overlapping margin callouts with leaders to representative symbols.

    Symbols retain their coordinates and semantic IDs. Labels occupy a dedicated
    margin, so equipment and usage labels in the building remain unobscured.
    The legacy SYMBOL REVIEW title remains for downstream consumers.
    """
    if tokens is None:
        from .themes import style_tokens

        tokens = style_tokens("blueprint", None)
    groups = {}
    for node in root.iter():
        if node.get("data-kind") in {"system", "equipment"} and node.get(
            "data-anchor-x"
        ):
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
    ordered = sorted(
        groups.items(), key=lambda item: (item[1][0][1], item[1][0][0], item[0])
    )
    new_width = width + 315
    new_height = max(height, 190 + len(ordered) * 56)
    root.set("width", f"{new_width:g}")
    root.set("height", f"{new_height:g}")
    root.set("viewBox", f"0 0 {new_width:g} {new_height:g}")
    for node in root:
        if node.get("data-background") == "sheet" or (
            node.tag == "rect" and node.get("x") == "0" and node.get("y") == "0"
        ):
            node.set("width", str(new_width))
            node.set("height", str(new_height))
        elif node.get("data-background") == "sky":
            node.set("width", str(new_width))
    margin = width + 20
    text("SYMBOL REVIEW", margin, 97, size=14, font_weight=600)
    text("Schematic components in this section", margin, 118, size=10)
    marker_positions = []
    for index, (key, anchors) in enumerate(ordered):
        number = index + 1
        ax, ay = anchors[0]
        label_y = 164 + index * 56
        # Leaders occupy the right margin; the local marker identifies the anchor.
        # Dense rooms can contain several distinct systems at the same anchor.
        # Choose the nearest clear marker position without moving the equipment.
        candidates = [
            (ax + dx * distance, ay + dy * distance)
            for distance in (12, 30, 48, 66, 84)
            for dx, dy in ((1, -1), (-1, -1), (1, 1), (-1, 1))
        ]
        bx, by = next(
            (
                (cx, cy)
                for cx, cy in candidates
                if 12 <= cx <= width - 12
                and 12 <= cy <= height - 12
                and all(
                    (cx - px) ** 2 + (cy - py) ** 2 >= 22**2
                    for px, py in marker_positions
                )
            ),
            candidates[-1],
        )
        marker_positions.append((bx, by))
        element(
            "line",
            x1=ax,
            x2=bx,
            y1=ay,
            y2=by,
            stroke=tokens["annotation_edge"],
            stroke_width=0.9,
        )
        element(
            "circle",
            data_annotation=key,
            cx=bx,
            cy=by,
            r=9,
            fill=tokens["annotation_fill"],
            stroke=tokens["annotation_edge"],
            stroke_width=1,
        )
        text(str(number), bx, by + 3.5, size=9, text_anchor="middle")
        element(
            "line",
            x1=width - 5,
            x2=margin - 3,
            y1=label_y - 4,
            y2=label_y - 4,
            stroke=tokens["annotation_edge"],
            stroke_width=0.8,
        )
        text(f"{number:02d}", margin, label_y, size=11, font_weight=600)
        label = (
            key.replace("_", " ")
            .replace(":", " / ")
            .capitalize()
            .replace("tabs", "TABS")
            .replace("pv", "PV")
            .replace("dhw", "DHW")
        )
        for row, value in enumerate(wrap(label, 29)):
            text(value, margin + 30, label_y + row * 14, size=11)
        text(f"{len(anchors)} occurrence(s)", margin + 30, label_y + 32, size=9)
    if not ordered:
        text("No HVAC or PV symbols drawn.", margin, 164, size=11)
