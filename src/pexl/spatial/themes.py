"""Presentation-only style tokens and self-contained vector backgrounds.

Wall thicknesses below are drawing pixels, not inferred physical assemblies.
Palettes change the drafting sheet; heating, cooling and airflow retain their
functional colours. No image, font service or browser script is required.
"""

from colorsys import rgb_to_hls, hls_to_rgb
from xml.etree import ElementTree as ET


def _tint(color: str, hue: float, saturation: float) -> str:
    """Preserve luminance while translating one drafting colour to a palette."""
    _, lightness, _ = rgb_to_hls(*(int(color[i : i + 2], 16) / 255 for i in (1, 3, 5)))
    return "#" + "".join(
        f"{round(channel*255):02x}"
        for channel in hls_to_rgb(hue, lightness, saturation)
    )


BLUE_COLORS = {
    "#a7d1ec",
    "#d8edf9",
    "#bdddeb",
    "#8bbddc",
    "#c8e7f4",
    "#e7f3fb",
    "#78b0d1",
    "#f2f9fd",
    "#477fa5",
    "#739bb3",
    "#c2e2f5",
    "#28678f",
    "#245779",
    "#f0f8fd",
    "#a6c9df",
    "#689abc",
    "#dcecf6",
    "#dce9f1",
    "#abc1cd",
    "#b7c8d1",
    "#8fa7b5",
}


def style_tokens(style: str, palette: str | None) -> dict:
    """Resolve a fresh style dictionary; explicit palettes apply to Blueprint."""
    if style not in {"architectural", "hand_drawn", "blueprint"}:
        raise ValueError(f"Unknown section style: {style!r}")
    if palette is not None and (
        style != "blueprint" or palette not in {"blue", "green", "beige"}
    ):
        raise ValueError(
            "palette is available only for blueprint: blue, green or beige"
        )
    tokens = {
        "ink": "#26323b",
        "paper": "#ffffff",
        "paper_end": "#f8f8f4",
        "sky": "#e7f0f1",
        "horizon": "#fffefa",
        "soil": "#e7e4d9",
        "deep_soil": "#c9cbbd",
        "annotation_fill": "#fffef8",
        "annotation_edge": "#70848b",
        "font": "sans-serif",
        "wall_structure": 4.0,
        "wall_insulation": 2.5,
        "recolor": {},
    }
    if style == "hand_drawn":
        tokens.update(
            ink="#49463e",
            paper="#fffdf5",
            paper_end="#eee8db",
            sky="#e9eee3",
            horizon="#fffdf5",
            soil="#e9dfca",
            deep_soil="#c8bca4",
            annotation_fill="#fff5ce",
            annotation_edge="#807b65",
            font="Ink Free, Segoe Print, Bradley Hand, Comic Sans MS, cursive",
        )
    elif style == "blueprint":
        tokens.update(
            ink="#245779",
            paper="#f0f8fd",
            paper_end="#e7f3fb",
            sky="#d8edf9",
            horizon="#f0f8fd",
            soil="#dce9f1",
            deep_soil="#abc1cd",
            annotation_fill="#f0f8fd",
            annotation_edge="#689abc",
        )
        if palette in {"green", "beige"}:
            hue, saturation = (0.35, 0.20) if palette == "green" else (0.11, 0.27)
            tokens["recolor"] = {
                color: _tint(color, hue, saturation) for color in BLUE_COLORS
            }
            for key in (
                "ink",
                "paper",
                "paper_end",
                "sky",
                "horizon",
                "soil",
                "deep_soil",
                "annotation_fill",
                "annotation_edge",
            ):
                tokens[key] = _tint(tokens[key], hue, saturation)
    return tokens


def draw_background(
    root: ET.Element, tokens: dict, width: float, height: float, ground_y: float
) -> None:
    """Paint a softly varying sheet and sky; return soil fill by its stable ID."""
    definitions = ET.SubElement(root, "defs")
    for name, start, end, diagonal in (
        ("sheet", tokens["paper"], tokens["paper_end"], True),
        ("sky", tokens["sky"], tokens["horizon"], False),
        ("soil", tokens["soil"], tokens["deep_soil"], False),
    ):
        gradient = ET.SubElement(
            definitions,
            "linearGradient",
            id="section-" + name,
            x1="0",
            y1="0",
            x2="1" if diagonal else "0",
            y2="1",
        )
        ET.SubElement(gradient, "stop", offset="0", **{"stop-color": start})
        ET.SubElement(gradient, "stop", offset="1", **{"stop-color": end})
    ET.SubElement(
        root,
        "rect",
        x="0",
        y="0",
        width=str(width),
        height=str(height),
        fill="url(#section-sheet)",
        **{"data-background": "sheet", "pointer-events": "none"},
    )
    ET.SubElement(
        root,
        "rect",
        x="0",
        y="90",
        width=str(width),
        height=str(max(0, ground_y - 90)),
        fill="url(#section-sky)",
        **{"data-background": "sky", "pointer-events": "none"},
    )


def apply_theme(root: ET.Element, tokens: dict) -> None:
    """Apply palette and typography consistently to nested component drawings."""
    for node in root.iter():
        for attr in ("fill", "stroke", "stop-color"):
            value = node.get(attr)
            if value in tokens["recolor"]:
                node.set(attr, tokens["recolor"][value])
        if node.tag.rsplit("}", 1)[-1] == "text":
            node.set("font-family", tokens["font"])
            if "Ink Free" in tokens["font"] and not node.get("rotate"):
                node.set("rotate", "-1.5 1.2 -0.8 0.5")
