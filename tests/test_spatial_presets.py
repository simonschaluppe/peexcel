"""Every documented preset recipe must render through the production pipeline."""

from copy import deepcopy
from xml.etree import ElementTree as ET

import pytest

from pexl import Project
from pexl.spatial import (
    normalize_layout,
    preset_visuals,
    render_svg,
    section_layout_from_scenario,
    suggest_section_layout,
)


def example_section(recipe):
    project = Project()
    scenario = project.get_or_create_scenario("Teaching | " + recipe["name"])
    for key, value in {
        "NFA_office": 600,
        "NFA_residential": 1200,
        "NFA_other": 150,
        "NFA_total": 1950,
        "rh_avg": 3,
        "rh_ceiling": 0.35,
        "PV_is_used": 0,
        "hull_fenestration_rate": 0.3,
    }.items():
        setattr(scenario.v, key, value)
    layout = {
        "layout_version": 1,
        "buildings": [
            {
                "id": "A",
                "name": recipe["name"],
                "geometry": {"max_floors": 3, "max_basements": 1, "depth_m": 15},
                "allocation": {
                    "usages": ["office", "residential"],
                    "basement_usages": ["other"],
                },
                "systems": recipe["systems"],
            }
        ],
    }
    before = deepcopy(scenario.as_dict())
    result = section_layout_from_scenario(scenario, layout=layout)
    assert scenario.as_dict() == before
    return result


@pytest.mark.parametrize(
    "recipe", preset_visuals(), ids=lambda row: row["category"] + ":" + row["name"]
)
def test_every_preset_has_a_real_section_example(recipe):
    before = deepcopy(recipe)
    section = example_section(recipe)
    root = ET.fromstring(render_svg(section))
    assert sum(space["area_m2"] for space in section["spaces"]) == pytest.approx(1950)
    assert recipe == before
    assert root.tag.endswith("svg")
    drawn = {node.get("data-system") for node in root.iter()}
    for record in section.get("equipment", []):
        assert record["kind"] in drawn
    for key, value in recipe["systems"]["usages"]["*"].items():
        if value != "none":
            assert key + ":" + value in drawn
    assert "SYS" not in " ".join(root.itertext())


def test_catalog_coverage_and_independent_results():
    rows = preset_visuals()
    assert len(rows) == 40
    assert len({(row["category"], row["source"]) for row in rows}) == 40
    assert len(preset_visuals("Cooling")) == 17
    rows[0]["systems"]["plant"].clear()
    assert preset_visuals()[0]["systems"]["plant"]
    with pytest.raises(ValueError, match="Unknown category"):
        preset_visuals("unsupported")


def test_exhaust_recovery_does_not_create_supply_duct():
    recipe = next(
        row
        for row in preset_visuals("Ventilation")
        if row["name"] == "ABL-Anlage mit WRG"
    )
    root = ET.fromstring(render_svg(example_section(recipe)))
    groups = [node for node in root.iter() if node.get("data-topology") == "exhaust"]
    assert groups and all(node.get("data-recovery") == "true" for node in groups)
    assert not any(node.get("data-air-path") == "extract" for node in root.iter())


def test_suggested_versioned_layout_retains_capacity_and_is_editable():
    scenario = Project().get_or_create_scenario("Suggestion")
    scenario.v.NFA_residential = 1200
    scenario.v.NFA_total = 1200
    scenario.v.building_count = 2
    scenario.v.storey_count_avg = 3
    compact = suggest_section_layout(scenario)
    grouped = suggest_section_layout(scenario, versioned=True)
    assert grouped == normalize_layout(compact)
    original = section_layout_from_scenario(scenario, layout=grouped)
    grouped["buildings"][0]["geometry"]["depth_m"] = 20
    changed = section_layout_from_scenario(scenario, layout=grouped)
    assert changed["geometry_signature"] != original["geometry_signature"]
    assert sum(space["area_m2"] for space in changed["spaces"]) == pytest.approx(1200)
