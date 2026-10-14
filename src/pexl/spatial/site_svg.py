"""Schematic street and courtyard context; no surveyed site geometry is implied."""

from xml.etree import ElementTree as ET
from ._svg_types import ElementFactory, TextWriter, CoordinateMap


def front_car(draw: ElementFactory, cx: float, ground: float, width: float) -> None:
    """Draw a muted front-view car shared by streets and basement parking."""
    g = draw("g", data_vehicle="front")

    def part(tag, **attrs):
        return ET.SubElement(
            g, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()}
        )

    half = width / 2
    part(
        "path",
        d=f"M {cx-half},{ground-3} V {ground-13} L {cx-half+3},{ground-23} H {cx+half-3} L {cx+half},{ground-13} V {ground-3} Z",
        fill="#a7adaf",
    )
    part(
        "path",
        d=f"M {cx-half+4},{ground-14} L {cx-half+6},{ground-21} H {cx+half-6} L {cx+half-4},{ground-14} Z",
        fill="#e1e4e4",
    )
    for dx in (-half + 3, half - 7):
        part("rect", x=cx + dx, y=ground - 5, width=4, height=5, fill="#727c80")
        part("rect", x=cx + dx, y=ground - 11, width=4, height=2, fill="#eceeee")
    part("rect", x=cx - 4, y=ground - 7, width=8, height=2, fill="#727c80")


def draw_site_context(
    section: dict,
    building_axes: list,
    element: ElementFactory,
    text: TextWriter,
    x: CoordinateMap,
    y: CoordinateMap,
    xscale: float,
    wall_total: float,
) -> None:
    """Fill explicit/default gaps with a coherent street or courtyard section."""
    # Streets and courtyards occupy the schematic gaps, not the scenario floor area.
    context_regions = []
    if building_axes:
        context_regions.append(
            (
                (
                    "street"
                    if section["buildings"][0]["street_side"] == "left"
                    else "courtyard"
                ),
                building_axes[0][1] - 108 / xscale,
                building_axes[0][1] - wall_total / xscale,
            )
        )
        for index, (previous, following) in enumerate(
            zip(building_axes, building_axes[1:])
        ):
            before, after = section["buildings"][index : index + 2]
            gap = next(
                (
                    g
                    for g in section.get("site", {}).get("gaps", [])
                    if set(g["between"]) == {before["id"], after["id"]}
                ),
                {},
            )
            kind = gap.get(
                "kind", "street" if before["street_side"] == "right" else "courtyard"
            )
            context_regions.append(
                (
                    kind,
                    previous[2] + wall_total / xscale,
                    following[1] - wall_total / xscale,
                )
            )
        last_index = len(building_axes) - 1
        context_regions.append(
            (
                (
                    "street"
                    if section["buildings"][-1]["street_side"] == "right"
                    else "courtyard"
                ),
                building_axes[-1][2] + wall_total / xscale,
                building_axes[-1][2] + 108 / xscale,
            )
        )
    for index, (kind, a, b) in enumerate(context_regions):
        a, b = x(a), x(b)
        if b - a < 20:
            continue
        center = (a + b) / 2
        ground = y(0)
        group = element("g", data_kind="site-context", data_exposure=kind)
        ET.SubElement(group, "title").text = (
            f"Schematic {kind}; no site survey or area allocation implied"
        )

        def site(tag, **attrs):
            return ET.SubElement(
                group, tag, {k.replace("_", "-"): str(v) for k, v in attrs.items()}
            )

        site("rect", x=a, y=ground, width=b - a, height=5, fill="#d3d5d1")
        if kind == "street":
            # Connected pavement, raised curbs, road base and accessible utility duct.
            curb_width = min(13, (b - a) * 0.15)
            site(
                "rect",
                data_site_layer="road-base",
                x=a,
                y=ground + 5,
                width=b - a,
                height=11,
                fill="#d8d7d2",
            )
            site(
                "rect",
                data_site_layer="road-surface",
                x=a + curb_width,
                y=ground,
                width=b - a - 2 * curb_width,
                height=4,
                fill="#a5aaa9",
            )
            for edge in (a, b - curb_width):
                site(
                    "rect",
                    data_site_layer="curb",
                    x=edge,
                    y=ground - 4,
                    width=curb_width,
                    height=13,
                    fill="#c6cac8",
                    stroke="#909895",
                    stroke_width=0.6,
                )
                site(
                    "line",
                    x1=edge + 2,
                    x2=edge + curb_width - 2,
                    y1=ground - 2,
                    y2=ground - 2,
                    stroke="#eef0ec",
                    stroke_width=1,
                )
            site(
                "rect",
                x=a + curb_width,
                y=ground + 4,
                width=b - a - 2 * curb_width,
                height=2,
                fill="#bcc3bd",
            )
            front_car(site, center, ground, min(26, (b - a) * 0.45))
            # Utility inspection chamber and horizontal conduits are in section.
            ux = a + curb_width / 2
            site(
                "rect",
                data_infrastructure="chamber",
                x=ux - 5,
                y=ground + 7,
                width=10,
                height=24,
                fill="#e9e9e4",
                stroke="#959e9c",
                stroke_width=0.7,
            )
            site("rect", x=ux - 6, y=ground - 4, width=12, height=2, fill="#87928f")
            site(
                "line",
                x1=ux,
                x2=ux,
                y1=ground - 2,
                y2=ground + 9,
                stroke="#959e9c",
                stroke_width=1,
            )
            for dy in (21, 27):
                site(
                    "line",
                    data_infrastructure="duct",
                    x1=a,
                    x2=b,
                    y1=ground + dy,
                    y2=ground + dy,
                    stroke="#a7afac",
                    stroke_width=2,
                )
            text("Street", center, ground + 66, size=10, text_anchor="middle")
            # Cycle-lane marking in the pavement section.
            for dx in (-4, 4):
                site(
                    "circle",
                    cx=center + dx,
                    cy=ground + 5,
                    r=1.5,
                    fill="none",
                    stroke="#f4f5f2",
                    stroke_width=0.7,
                )
        else:
            tree_x = a + (b - a) * 0.42
            # Mature tree: three times the original height and canopy, solid silhouette.
            tree = site("g", data_landscape="courtyard-tree", data_scale=3)
            ET.SubElement(
                tree,
                "path",
                {
                    "d": f"M {tree_x-3},{ground} L {tree_x-2},{ground-65} L {tree_x-16},{ground-80} L {tree_x-12},{ground-84} L {tree_x},{ground-71} L {tree_x+14},{ground-91} L {tree_x+18},{ground-88} L {tree_x+3},{ground-64} L {tree_x+3},{ground} Z",
                    "fill": "#a0aaa0",
                },
            )
            for dx, dy, radius in ((-17, -94, 23), (16, -101, 26), (0, -119, 22)):
                ET.SubElement(
                    tree,
                    "circle",
                    {
                        "cx": str(tree_x + dx),
                        "cy": str(ground + dy),
                        "r": str(radius),
                        "fill": "#a0aaa0",
                    },
                )
            for dx in (0, 7, 14):
                site("circle", cx=a + 7 + dx, cy=ground - 4, r=5, fill="#a0aaa0")
            if b - a > 70:
                play_x = a + (b - a) * 0.82
                site(
                    "path",
                    d=f"M {play_x-12},{ground} L {play_x-7},{ground-25} H {play_x+7} L {play_x+12},{ground} H {play_x+9} L {play_x+5},{ground-22} H {play_x-5} L {play_x-9},{ground} Z",
                    fill="#aaa99f",
                )
                site(
                    "rect",
                    x=play_x - 1,
                    y=ground - 23,
                    width=2,
                    height=17,
                    fill="#aaa99f",
                )
                site(
                    "rect",
                    x=play_x - 5,
                    y=ground - 7,
                    width=10,
                    height=3,
                    fill="#aaa99f",
                )
            text("Courtyard", center, ground + 23, size=10, text_anchor="middle")
