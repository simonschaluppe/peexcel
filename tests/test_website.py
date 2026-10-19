"""Structural and publication checks for the website teaching workflow."""
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

import nbformat
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from component_teaching import categories, cellar_svg
from website_assets import build, prepare_assessment, NOTEBOOKS, MANUAL_FIGURES
from pexl.model.scenario import Scenario
from pexl.spatial import render_svg, section_layout_from_scenario


def test_teaching_style_preserves_geometry_and_input():
    from copy import deepcopy
    s = Scenario("Teaching")
    s.v.NFA_total = s.v.NFA_residential = 600
    s.v.building_count, s.v.storey_count_avg = 1, 2
    section = section_layout_from_scenario(s)
    before = deepcopy(section)
    source = ET.fromstring(render_svg(section))
    result = ET.fromstring(render_svg(section, style="teaching"))
    assert section == before
    original = {n.get("id"): n for n in source.iter() if n.get("id")}
    for node in result:
        if node.get("data-kind"):
            assert node.get("id") in original
            for key in ("x", "y", "width", "height", "d", "transform"):
                assert node.get(key) == original[node.get("id")].get(key)
    with pytest.raises(ValueError, match="annotations"):
        render_svg(section, style="teaching", annotations=True)


def test_cellar_boundary_and_category_identity():
    names = dict(categories())
    assert len(names) == 20
    root = ET.fromstring(cellar_svg())
    nodes = {n.get("id"): n for n in root.iter() if n.get("id")}
    assert nodes["slab:A:f0"].get("data-category") == "COMP_name_basement_ceiling"
    assert nodes["slab:A:f1"].get("data-category") == "COMP_name_ceiling"
    assert nodes["slab:A:f-1"].get("data-category") == "COMP_name_basement_floor_unheated"
    assert nodes["A:f-1:left"].get("data-category") == "COMP_name_wall_ec_unheated"
    assert {n.get("data-category") for n in root.iter() if n.get("data-category")} <= names.keys()
    boundary = nodes["boundary"]
    bottom = float(boundary.get("y")) + float(boundary.get("height"))
    assert bottom <= float(nodes["A:f-1:s0"].get("y")) + 0.001
    assert bottom > float(nodes["slab:A:f0"].get("y"))


def test_build_publishes_only_clean_notebook_copies(tmp_path):
    before = {name: (ROOT / "notebooks" / f"{name}.ipynb").read_bytes() for name in NOTEBOOKS}
    build(tmp_path)
    for name in NOTEBOOKS:
        assert (ROOT / "notebooks" / f"{name}.ipynb").read_bytes() == before[name]
        copy = nbformat.read(tmp_path / "downloads" / f"{name}.ipynb", as_version=4)
        assert all(not c.outputs and c.execution_count is None for c in copy.cells if c.cell_type == "code")
    assert not (tmp_path / "assets/primary_energy_balance.html").exists()
    assert (tmp_path / "assets/components/index.html").exists()
    for name in MANUAL_FIGURES:
        assert (tmp_path / "media/manual" / f"{name}.png").read_bytes() == (ROOT / "docs/website" / f"{name}.png").read_bytes()


def test_assessment_page_keeps_outputs_without_modifying_source(tmp_path):
    source = ROOT / "notebooks/howto_assess.ipynb"
    before = source.read_bytes()
    original = nbformat.read(source, as_version=4)
    page = nbformat.read(prepare_assessment(tmp_path), as_version=4)
    assert source.read_bytes() == before
    assert page.cells[0].cell_type == "raw"
    assert "enabled: false" in page.cells[0].source
    assert page.cells[3:] == original.cells[1:]
    assert any(c.get("outputs") for c in page.cells if c.cell_type == "code")
    download = nbformat.read(tmp_path / "downloads/howto_assess.ipynb", as_version=4)
    assert [c.source for c in download.cells] == [c.source for c in original.cells]
    assert all(not c.outputs and c.execution_count is None
               for c in download.cells if c.cell_type == "code")
