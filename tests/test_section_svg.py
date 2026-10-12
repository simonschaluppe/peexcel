import copy
from math import isfinite
from xml.etree import ElementTree as ET

import pytest

from pexl.model.scenario import Scenario
from pexl.spatial import render_svg, section_from_scenario


@pytest.mark.parametrize("style", ["architectural", "hand_drawn", "blueprint"])
def test_svg_valid_deterministic_and_escaped(style):
    scenario = Scenario('Example <A> & "B"')
    scenario.v.NFA_total = 150
    scenario.v.PV_module_area = 200
    section = section_from_scenario(scenario)
    before = copy.deepcopy(section)
    svg = render_svg(section, style=style)
    assert svg == render_svg(section, style=style)
    assert section == before
    root = ET.fromstring(svg)
    assert root.tag == "{http://www.w3.org/2000/svg}svg"
    assert root.find("{http://www.w3.org/2000/svg}title").text.startswith(scenario.column_name)
    ids = [e.attrib["id"] for e in root.iter() if "id" in e.attrib]
    assert len(ids) == len(set(ids))
    _, _, width, height = map(float, root.attrib["viewBox"].split())
    for element in root.iter():
        for key in ("x", "y", "x1", "x2", "y1", "y2", "width", "height"):
            if key in element.attrib:
                assert isfinite(float(element.attrib[key]))
        if element.tag.endswith("}rect"):
            x, y, w, h = (float(element.attrib[k]) for k in ("x", "y", "width", "height"))
            assert 0 <= x <= x + w <= width
            assert 0 <= y <= y + h <= height
    assert "unplaced: 50" in svg
    assert "15 m" in svg
    with pytest.raises(ValueError, match="Unknown section style"):
        render_svg(section, style="unknown")


def test_wide_section_remains_visible_and_has_axes_and_legend():
    source = Scenario("Wide example")
    source.v.NFA_total = 15000
    source.v.PV_module_area = 200
    section = section_from_scenario(source)
    root = ET.fromstring(render_svg(section))
    by_id = {e.get("id"): e for e in root.iter() if e.get("id")}
    for space in section["spaces"]:
        assert float(by_id[space["id"]].get("height")) >= 56
    text = " ".join(e.text or "" for e in root.iter())
    assert "Ground floor" in text
    assert "tick interval 15 m" in text
    assert "PV modules" in text
    assert "Unallocated usage" in text
    panel = by_id["pv0"]
    roof = by_id[section["pv"]["placements"][0]["roof_id"]]
    assert float(roof.get("y")) - (float(panel.get("y")) + float(panel.get("height"))) >= 20
    assert {e.get("data-kind") for e in root.iter() if e.get("data-kind")} == {"facade", "roof", "pv", "slab", "insulation", "axis-tick", "underground", "interior-wall", "service-shaft", "window", "site-context"}


def test_all_usage_colors_have_matching_legend_swatches():
    source = Scenario("All usages")
    for meta, _ in source.select(domain="usage", measure="area", spatial_scope="NFA", entity_group="usage").items():
        setattr(source.v, meta.attr_name, 100)
    source.v.storey_count_avg = 4
    section = section_from_scenario(source)
    root = ET.fromstring(render_svg(section))
    rects = root.findall("{http://www.w3.org/2000/svg}rect")
    by_id = {r.get("id"): r for r in rects if r.get("id")}
    colors = {by_id[s["id"]].get("fill") for s in section["spaces"]}
    assert len(colors) == 7
    swatches = {r.get("fill") for r in rects if r.get("width") == "18"}
    assert colors <= swatches


def test_layered_facade_is_flush_with_slabs_and_wood_is_optional():
    source = Scenario("Layered construction")
    source.v.NFA_total = 900
    source.v.storey_count_avg = 3
    section = section_from_scenario(source)
    for construction, color in (("default", "#69836d"), ("wood", "#c59b6d")):
        svg = render_svg(section, construction=construction)
        root = ET.fromstring(svg)
        by_id = {e.get("id"): e for e in root.iter() if e.get("id")}
        for floor in section["floors"]:
            fid = floor["id"]
            slab = by_id[f"slab:{fid}"]
            left = by_id[f"insulation:{fid}:left"]
            right = by_id[f"insulation:{fid}:right"]
            assert float(slab.get("x")) == pytest.approx(float(left.get("x")) + float(left.get("width")))
            assert float(slab.get("x")) + float(slab.get("width")) == pytest.approx(
                float(right.get("x")))
            for insulation in (left, right):
                assert float(insulation.get("y")) <= float(slab.get("y"))
                assert float(insulation.get("y")) + float(insulation.get("height")) >= (
                    float(slab.get("y")) + float(slab.get("height")) - 1e-9)
            assert slab.get("fill") == color
            assert left.get("fill") == right.get("fill") == "#ddd2e5"
        assert "data-variable" not in svg
        assert "<script" not in svg
    with pytest.raises(ValueError, match="construction"):
        render_svg(section, construction="unknown")


def test_styles_preserve_geometry_and_change_appearance():
    scenario = Scenario("Styles")
    scenario.v.NFA_residential = 900
    scenario.v.NFA_office = 300
    section = section_from_scenario(scenario)
    roots = [ET.fromstring(render_svg(section, style=style))
             for style in ("architectural", "hand_drawn", "blueprint")]
    geometry = []
    for root in roots:
        geometry.append({e.get("id"): tuple(e.get(k) for k in ("x", "y", "width", "height"))
                         for e in root.iter() if e.get("id") and not e.get("id").startswith("wash:")})
    assert geometry[0] == geometry[1] == geometry[2]
    assert any(e.tag.endswith("}path") for e in roots[1].iter())
    fills = [{e.get("id"): e.get("fill") for e in root.iter() if e.get("id")}
             for root in roots]
    assert fills[0] != fills[2]


def test_sketch_brush_notes_and_butterfly_angles():
    from math import atan, degrees
    source = Scenario("Sketch")
    source.v.NFA_office = 600
    source.v.PV_module_area = 120
    root = ET.fromstring(render_svg(section_from_scenario(source), style="hand_drawn"))
    assert not any(e.get("data-decoration") == "brush-stroke" for e in root.iter())
    slabs = [e for e in root.iter() if e.get("data-kind") == "slab"]
    assert slabs and all(e.get("visibility") == "hidden" for e in slabs)
    assert any(e.get("data-decoration") == "sticky-note" for e in root.iter())
    texts = [e for e in root.iter() if e.tag.endswith("}text")]
    assert all("Segoe Print" in e.get("font-family", "") for e in texts)
    wings = [e for e in root.iter() if e.get("data-module-tilt-deg")]
    assert wings
    for wing in wings:
        a, b, *_ = [tuple(map(float, point.split(','))) for point in wing.get("points").split()]
        angle = degrees(atan(abs((b[1] - a[1]) / (b[0] - a[0]))))
        assert angle == pytest.approx(15, abs=0.02)


@pytest.mark.parametrize("style", ["architectural", "hand_drawn", "blueprint"])
def test_interior_overlays_preserve_areas_and_stay_inside_floors(style):
    source = Scenario("Interior details")
    source.v.NFA_residential = 1800
    source.v.NFA_office = 600
    source.v.building_count = 2
    source.v.storey_count_avg = 3
    section = section_from_scenario(source)
    before = copy.deepcopy(section)
    root = ET.fromstring(render_svg(section, style=style))
    assert section == before
    shafts = [e for e in root.iter() if e.get("data-kind") == "service-shaft"]
    walls = [e for e in root.iter() if e.get("data-kind") == "interior-wall"]
    assert shafts and walls
    by_id = {e.get("id"): e for e in root.iter() if e.get("id")}
    for shaft in shafts:
        members = [by_id[s["id"]] for s in section["spaces"] if s["floor_id"] == shaft.get("data-floor")]
        assert float(shaft.get("x")) >= min(float(e.get("x")) for e in members) - 1e-9
        assert float(shaft.get("x")) + float(shaft.get("width")) <= max(float(e.get("x")) + float(e.get("width")) for e in members) + 1e-9
        assert float(shaft.get("y")) == pytest.approx(float(members[0].get("y")))
        assert float(shaft.get("height")) == pytest.approx(float(members[0].get("height")))
    assert {e.get("data-building") for e in shafts} == {b["id"] for b in section["buildings"]}
    if style == "hand_drawn":
        assert all(e.get("rotate") for e in root.iter() if e.tag.endswith("}text"))
        assert any(e.get("data-decoration") == "usage-strokes" for e in root.iter())
        by_id = {e.get("id"): e for e in root.iter() if e.get("id")}
        assert all(by_id[r["id"]].get("visibility") == "hidden" for r in section["roofs"])



def system_example():
    from pexl.spatial import section_layout_from_scenario
    source = Scenario("System overlays")
    source.v.NFA_office = 1200
    source.v.NFA_residential = 2400
    source.v.NFA_total = 3600
    source.v.PV_module_area = 900
    source.v.borehole_count = 4
    source.v.vent_share_mechanical_office = 0.8
    layout = {"systems": {
        "usages": {"*": {"heating": "underfloor", "cooling": "tabs"},
                   "office": {"ventilation": "heat_recovery"}},
        "plant": ["heating_room", "water_well", "boreholes", "district_heating"],
        "roof": ["pv", "solar_thermal", "pergola", "terrace", "garden"],
    }, "buildings": [
        {"max_floors": 3, "usages": ["office", "residential"]},
        {"max_floors": 3, "usages": ["office", "residential"],
         "systems": {"usages": {"office": {"heating": "radiator", "cooling": "split"},
                                "residential": {"cooling": "fan_coil", "ventilation": "natural"}},
                     "plant": ["gas_boiler", "oil_boiler", "biomass_boiler"], "roof": []}},
    ]}
    return source, layout, section_layout_from_scenario


def test_system_inheritance_is_nonmutating_and_area_neutral():
    source, layout, generate = system_example()
    before_source, before_layout = copy.deepcopy(source.as_dict()), copy.deepcopy(layout)
    section = generate(source, layout=layout)
    settings = section["systems"]["buildings"]
    assert settings["b0"]["usages"]["office"]["heating"] == "underfloor"
    assert settings["b1"]["usages"]["office"] == {"heating": "radiator", "cooling": "split", "ventilation": "heat_recovery"}
    assert settings["b1"]["usages"]["residential"]["heating"] == "underfloor"
    assert settings["b1"]["roof"] == []
    assert settings["b1"]["plant"] == ["gas_boiler", "oil_boiler", "biomass_boiler"]
    assert source.as_dict() == before_source and layout == before_layout
    plain_layout = copy.deepcopy(layout)
    plain_layout.pop("systems")
    for building in plain_layout["buildings"]:
        building.pop("systems", None)
    plain = generate(source, layout=plain_layout)
    for key in ("spaces", "floors", "roofs", "pv", "adjacency"):
        assert section[key] == plain[key]
    assert section == generate(source, layout=layout)


@pytest.mark.parametrize("style", ["architectural", "hand_drawn", "blueprint"])
def test_all_system_symbols_are_valid_and_styled_without_mutation(style):
    source, layout, generate = system_example()
    source.v.PV_module_area = 30  # Free roof surface for all amenity tiles.
    section = generate(source, layout=layout)
    before = copy.deepcopy(section)
    svg = render_svg(section, style=style)
    assert svg == render_svg(section, style=style) and section == before
    root = ET.fromstring(svg)
    kinds = {e.get("data-system") for e in root.iter() if e.get("data-system")}
    assert {"heating:underfloor", "heating:radiator", "cooling:tabs", "cooling:split", "cooling:fan_coil",
            "ventilation:heat_recovery", "ventilation:natural", "heating_room", "water_well", "boreholes",
            "district_heating", "gas_boiler", "oil_boiler", "biomass_boiler",
            "roof:solar_thermal", "roof:pergola", "roof:terrace", "roof:garden"} <= kinds
    source.v.PV_module_area = 900
    assert "Hidden by overlay" in render_svg(generate(source, layout=layout), style=style)
    assert not any(e.tag.endswith("}script") for e in root.iter())


def test_scenario_system_hints_and_building_wildcard_override():
    source, layout, generate = system_example()
    layout["systems"] = {}
    layout["buildings"][1]["systems"] = {"usages": {"*": {"ventilation": "none"}}, "plant": []}
    result = generate(source, layout=layout)["systems"]
    assert result["buildings"]["b0"]["plant"] == ["boreholes"]
    assert result["buildings"]["b0"]["usages"]["office"]["ventilation"] == "mechanical"
    assert result["buildings"]["b1"]["usages"]["office"]["ventilation"] == "none"
    assert result["source_values"]["borehole_count"] == 4


@pytest.mark.parametrize("bad", [None, {"unknown": 1}, {"plant": ["nuclear"]},
    {"roof": ["pv", "pv"]}, {"usages": {"office": {"heating": "invalid"}}},
    {"usages": {"invalid_usage": {"heating": "tabs"}}}])
def test_invalid_system_options_rejected(bad):
    source, layout, generate = system_example()
    layout["systems"] = bad
    with pytest.raises(ValueError):
        generate(source, layout=layout)



def test_annotations_style_identifies_drawn_symbols_without_changing_layout():
    source, layout, generate = system_example()
    section = generate(source, layout=layout)
    before = copy.deepcopy(section)
    svg = render_svg(section, style="annotations")
    root = ET.fromstring(svg)
    assert section == before and svg == render_svg(section, style="annotations")
    labels = [e.get("data-annotation") for e in root.iter() if e.get("data-annotation")]
    symbols = {e.get("data-system") for e in root.iter() if e.get("data-system") and e.get("data-anchor-x")}
    assert len(labels) == len(set(labels))
    assert symbols | {"roof:pv"} == set(labels)
    assert "SYMBOL REVIEW" in " ".join(root.itertext())
    plain = ET.fromstring(render_svg(section, style="blueprint"))
    assert float(root.get("width")) > float(plain.get("width"))
    def coordinates(tree):
        return {e.get("id"): tuple(e.get(k) for k in ("x", "y", "width", "height"))
                for e in tree.iter() if e.get("id")}
    assert coordinates(root) == coordinates(plain)


def test_annotations_style_without_systems_or_pv():
    source = Scenario("Empty symbol review")
    source.v.NFA_office = 100
    source.v.PV_is_used = 0
    root = ET.fromstring(render_svg(section_from_scenario(source), style="annotations"))
    assert "No HVAC or PV symbols drawn." in " ".join(root.itertext())



def test_physical_emitters_use_correct_layers_and_facade_positions():
    source, layout, generate = system_example()
    section = generate(source, layout=layout)
    before = copy.deepcopy(section)
    root = ET.fromstring(render_svg(section))
    by_id = {e.get("id"): e for e in root.iter() if e.get("id")}
    for node in root.iter():
        location, sid = node.get("data-location"), node.get("data-space")
        if not location or not sid:
            continue
        room = by_id[sid]
        top = float(room.get("y"))
        bottom = top + float(room.get("height"))
        anchor = float(node.get("data-anchor-y"))
        if location == "inside-concrete":
            floor_id = next(s["floor_id"] for s in section["spaces"] if s["id"] == sid)
            slab = by_id[f"slab:{floor_id}"]
            assert bottom <= anchor <= bottom + float(slab.get("height"))
        elif location == "above-structural-slab":
            assert bottom - 12 < anchor < bottom
        elif location == "below-ceiling":
            assert top < anchor < top + 20
        elif location in ("facade-high", "below-window", "window"):
            assert float(node.get("data-anchor-x")) > float(room.get("x")) + float(room.get("width")) / 2
    assert not any(e.get("data-kind") == "construction-detail" for e in root.iter())
    from pexl.spatial import render_emission_details_svg
    details = ET.fromstring(render_emission_details_svg(section))
    assert len([e for e in details.iter() if e.get("data-kind") == "construction-detail"]) == 3
    assert section == before


@pytest.mark.parametrize("style", ["architectural", "hand_drawn", "blueprint", "annotations"])
def test_roof_tiles_hvac_room_and_grouped_legend(style):
    source, layout, generate = system_example()
    layout["systems"]["roof"] = ["garden", "pergola", "terrace", "hvac_room"]
    for building in layout["buildings"]:
        building.setdefault("systems", {})["roof"] = ["garden", "pergola", "terrace", "hvac_room"]
    section = generate(source, layout=layout)
    before = copy.deepcopy(section)
    root = ET.fromstring(render_svg(section, style=style))
    rooms = [e for e in root.iter() if e.get("data-system") == "roof:hvac_room"]
    assert len(rooms) == len(section["buildings"])
    for room in rooms:
        assert float(room.get("data-room-width")) == 2 * float(room.get("data-shaft-width"))
        bid = room.get("data-building")
        shaft = next(e for e in root.iter() if e.get("data-kind") == "service-shaft" and e.get("data-building") == bid)
        assert float(room.get("data-anchor-x")) == pytest.approx(float(shaft.get("x")) + float(shaft.get("width"))/2)
    assert any(e.get("data-roof-tile") == "garden" for e in root.iter())
    labels = " ".join(root.itertext())
    assert all(label in labels for label in ("Usage", "Material overlay", "HVAC overlay"))
    assert section == before


def test_emission_pipes_are_straight_and_roof_tiles_do_not_overlap():
    source, layout, generate = system_example()
    source.v.PV_module_area = 30
    root = ET.fromstring(render_svg(generate(source, layout=layout)))
    pipes = [e for e in root.iter() if e.get("data-pipe") == "straight"]
    assert pipes and all(e.get("y1") == e.get("y2") for e in pipes)
    tiles = [e for e in root.iter() if e.get("data-roof-tile")]
    assert tiles
    for i, a in enumerate(tiles):
        for b in tiles[i+1:]:
            if (a.get("data-building"), a.get("data-base-y")) != (b.get("data-building"), b.get("data-base-y")):
                continue
            al, bl = float(a.get("data-left")), float(b.get("data-left"))
            assert min(al+float(a.get("data-width")), bl+float(b.get("data-width"))) <= max(al, bl)+1e-8


def test_roof_scenes_respect_full_pv_coverage():
    source, layout, generate = system_example()
    source.v.PV_module_area = 100000
    root = ET.fromstring(render_svg(generate(source, layout=layout)))
    assert not any(e.get("data-roof-tile") for e in root.iter())


def test_roof_modules_are_not_stretched_and_legend_reuses_symbols():
    from colorsys import rgb_to_hls
    source, layout, generate = system_example()
    source.v.PV_module_area = 30
    root = ET.fromstring(render_svg(generate(source, layout=layout)))
    tiles = [e for e in root.iter() if e.get("data-roof-tile")]
    assert tiles
    for tile in tiles:
        assert not any("scale(" in e.get("transform", "") for e in tile.iter())
        if tile.get("data-roof-tile") != "garden":
            assert float(tile.get("data-width")) == 64
        hues = []
        for e in tile.iter():
            for key in ("fill", "stroke"):
                c = e.get(key, "")
                if c.startswith("#") and len(c) == 7:
                    h, _, sat = rgb_to_hls(*(int(c[i:i+2],16)/255 for i in (1,3,5)))
                    if sat > .05: hues.append(h)
        assert max(hues)-min(hues) < .025
    assert any(e.get("data-legend-symbol") == "roof:garden" for e in root.iter())
    ids = [e.get("id") for e in root.iter() if e.get("id")]
    assert len(ids) == len(set(ids))
    assert any(e.get("data-connection") == "water_well" for e in root.iter())
    assert any(e.get("data-service") == "riser" for e in root.iter())


def test_emission_details_without_systems_is_valid_svg():
    from pexl.spatial import render_emission_details_svg
    root = ET.fromstring(render_emission_details_svg({}))
    assert "No emission systems configured." in " ".join(root.itertext())


def test_site_circulation_and_roof_supports():
    source, layout, generate = system_example()
    source.v.PV_module_area = 30
    root = ET.fromstring(render_svg(generate(source, layout=layout)))
    assert any(e.get("data-vehicle") == "front" for e in root.iter())
    assert any(e.get("data-landscape") == "courtyard-tree" and e.get("data-scale") == "3" for e in root.iter())
    assert {e.get("data-infrastructure") for e in root.iter()} >= {"chamber", "duct"}
    circulation = {e.get("data-building"):e.get("data-circulation") for e in root.iter() if e.get("data-kind") == "service-shaft"}
    assert list(circulation.values())[:2] == ["elevator", "stairs"]
    assert any(e.get("data-site-layer") == "curb" for e in root.iter())
    roof_tops = [float(e.get("y")) for e in root.iter() if (e.get("id") or "").startswith("insulation:r")]
    for tile in (e for e in root.iter() if e.get("data-roof-tile")):
        assert any(abs(float(tile.get("data-base-y"))-top)<1e-7 for top in roof_tops)


@pytest.mark.parametrize("style", ["architectural", "hand_drawn", "blueprint", "annotations"])
def test_historic_relief_is_decorative_and_can_be_overridden(style):
    source, layout, generate = system_example()
    layout["facade_style"] = "gruenderzeit"
    layout["buildings"][1]["facade_style"] = "default"
    section = generate(source, layout=layout)
    before = copy.deepcopy(section)
    root = ET.fromstring(render_svg(section,style=style))
    relief = [e for e in root.iter() if e.get("data-decoration") == "facade-relief"]
    assert relief and {e.get("data-building") for e in relief} == {section["buildings"][0]["id"]}
    assert not any(e.get("data-decoration") == "facade-relief" for e in
                   ET.fromstring(render_svg(section,facade_style="default")).iter())
    assert section == before
    ordinary = ET.fromstring(render_svg(section,facade_style="default"))
    def windows(tree):
        return [(e.get("id"),e.get("data-glazing-ratio"),e.get("height")) for e in tree.iter() if e.get("data-kind")=="window"]
    assert windows(root) == windows(ordinary)
