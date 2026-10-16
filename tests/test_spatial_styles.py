"""Style options are independent of geometry and component interpretation."""

from copy import deepcopy
import re
from xml.etree import ElementTree as ET

import pytest

from pexl.spatial import preset_visuals, render_svg
from tests.test_spatial_presets import example_section


@pytest.mark.parametrize(
    "style,palette",
    [
        ("architectural", None),
        ("hand_drawn", None),
        ("blueprint", None),
        ("blueprint", "blue"),
        ("blueprint", "green"),
        ("blueprint", "beige"),
    ],
)
def test_annotations_on_each_style_and_palette(style, palette):
    recipe = next(
        row
        for row in preset_visuals("Heating")
        if row["name"] == "Wärmepumpe (Grundwasser)"
    )
    section = example_section(recipe)
    before = deepcopy(section)
    plain = ET.fromstring(render_svg(section, style=style, palette=palette))
    marked = ET.fromstring(
        render_svg(section, style=style, palette=palette, annotations=True)
    )
    assert section == before
    assert not any(n.get("data-annotation") for n in plain.iter())
    labels = [
        n.get("data-annotation") for n in marked.iter() if n.get("data-annotation")
    ]
    assert {"heat_pump", "source:groundwater"} <= set(labels)
    assert len(labels) == len(set(labels))

    def targets(root):
        return {
            n.get("id"): tuple(
                n.get(k) for k in ("x", "y", "width", "height", "data-semantic-id")
            )
            for n in root.iter()
            if n.get("id") and n.get("data-semantic-id")
        }

    assert targets(plain) == targets(marked)
    if style == "hand_drawn":
        assert all(
            "Ink Free" in n.get("font-family", "")
            for n in marked.iter()
            if n.tag.endswith("}text")
        )
    assert {n.get("id") for n in plain.iter() if n.tag.endswith("}linearGradient")} == {
        "section-sheet",
        "section-sky",
        "section-soil",
    }
    ids = {n.get("id") for n in marked.iter() if n.get("id")}
    for node in marked.iter():
        for value in node.attrib.values():
            for ref in re.findall(r"url\(#([^)]+)\)", value):
                assert ref in ids


def test_legacy_annotations_alias_and_palette_validation():
    section = example_section(preset_visuals("Ventilation")[0])
    assert render_svg(section, style="annotations") == render_svg(
        section, style="blueprint", annotations=True
    )
    for style, palette in [
        ("architectural", "blue"),
        ("hand_drawn", "green"),
        ("blueprint", "pink"),
    ]:
        with pytest.raises(ValueError, match="palette"):
            render_svg(section, style=style, palette=palette)
    with pytest.raises(ValueError, match="usage_labels"):
        render_svg(section, usage_labels="invalid")


def test_direct_usage_labels_are_optional_and_palettes_are_distinct():
    section = example_section(preset_visuals("Emission")[0])
    default = ET.fromstring(render_svg(section))
    hidden = ET.fromstring(render_svg(section, usage_labels="none"))
    assert any(n.get("data-usage-label") for n in default.iter())
    assert not any(n.get("data-usage-label") for n in hidden.iter())
    fills = []
    for palette in ("blue", "green", "beige"):
        root = ET.fromstring(render_svg(section, style="blueprint", palette=palette))
        fills.append(
            {
                n.get("fill")
                for n in root.iter()
                if n.get("id") in {s["id"] for s in section["spaces"]}
            }
        )
    assert len({frozenset(v) for v in fills}) == 3
