"""Checks for the explicit teaching fixture; no project geometry is inferred."""
import importlib.util
from pathlib import Path
from xml.etree import ElementTree as ET

from pexl.model.scenario import Scenario
from pexl.spatial import section_layout_from_scenario, render_svg

spec = importlib.util.spec_from_file_location(
    "section_teaching_preview",
    Path(__file__).resolve().parents[1] / "scripts/section_teaching_preview.py",
)
preview = importlib.util.module_from_spec(spec)
spec.loader.exec_module(preview)


def test_original_geometry_is_preserved():
    scenario = Scenario("Fixture")
    scenario.v.NFA_residential = scenario.v.NFA_total = 600
    scenario.v.building_count = 1
    scenario.v.storey_count_avg = 2
    scenario.v.PV_is_used = False
    original = ET.fromstring(render_svg(section_layout_from_scenario(scenario), usage_labels="none"))
    by_id = {n.get("id"): n for n in original.iter() if n.get("id")}
    result = ET.fromstring(preview.teaching_svg())
    base = next(n for n in result if n.get("id") == "base")
    assert len(base) > 10
    for node in base:
        source = by_id[node.get("id")]
        for key in ("x", "y", "width", "height", "d", "transform"):
            assert node.get(key) == source.get(key)
    ids = [n.get("id") for n in result.iter() if n.get("id")]
    assert len(ids) == len(set(ids))


def test_fixture_boundary_and_zone_specific_flows():
    root = ET.fromstring(preview.teaching_svg())
    components = {n.get("id"): n.get("data-component") for n in root.iter() if n.get("data-component")}
    assert components["slab:b0:f0"] == "ground"
    assert components["slab:b0:f1"] == "floor"
    assert set(components.values()) == {"wall", "roof", "window", "ground", "floor"}
    flows = {n.get("data-flow"): n.get("data-zone") for n in root.iter() if n.get("data-flow")}
    assert flows["cooling"] == "cooled"
    assert flows["night"] == "uncooled"
    assert flows["heating"] == "both"
    # Every arrow and its label stays within the reserved illustration canvas.
    for node in root.iter():
        for key in ("x1", "x2"):
            if key in node.attrib:
                assert 0 <= float(node.get(key)) <= 640
        for key in ("y1", "y2"):
            if key in node.attrib:
                assert 100 <= float(node.get(key)) <= 440


def test_preview_is_reproducible_and_self_contained(tmp_path):
    path = preview.build_preview(tmp_path)
    first = path.read_bytes()
    preview.build_preview(tmp_path)
    assert path.read_bytes() == first
    text = first.decode("utf-8")
    assert "<svg" in text
    assert "<script src=" not in text
    assert "keine berechneten Wärmeflusswerte" in text
