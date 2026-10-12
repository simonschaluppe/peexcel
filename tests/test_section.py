import copy
import random
from collections import defaultdict

import pytest

from pexl.model.scenario import Scenario
from pexl.spatial import section_from_scenario
from pexl.spatial import section_layout_from_scenario
from pexl.spatial import suggest_section_layout


@pytest.mark.parametrize("values", [{}, {"NFA_residential": 0, "NFA_office": 161,
                                       "building_count": 5}])
def test_suggest_layout_is_editable_deterministic_and_preserves_areas(values):
    import json

    source = scenario(**values)
    before = copy.deepcopy(source.as_dict())
    suggestion = suggest_section_layout(source)
    assert suggestion == suggest_section_layout(source)
    assert json.loads(json.dumps(suggestion)) == suggestion
    assert len(suggestion["buildings"]) == source.v.building_count
    result = section_layout_from_scenario(source, layout=suggestion)
    areas = defaultdict(float)
    for space in result["spaces"]:
        areas[space["usage"]] += space["area_m2"]
    assert areas.get("office", 0) == pytest.approx(source.v.NFA_office)
    assert areas.get("residential", 0) == pytest.approx(source.v.NFA_residential)
    suggestion["buildings"][0]["max_floors"] += 1
    section_layout_from_scenario(source, layout=suggestion)
    assert source.as_dict() == before


def scenario(**values):
    result = Scenario("Example | Baseline")
    defaults = dict(NFA_residential=123.25, NFA_office=37.75, NFA_total=161,
                    building_count=2, storey_count_avg=2.5, rh_avg=3,
                    rh_ceiling=0.35, PV_is_used=1, PV_module_area=12)
    for name, value in (defaults | values).items():
        setattr(result.v, name, value)
    return result


@pytest.mark.parametrize("seed", [0, 42, 123])
def test_area_conservation_and_partial_floors(seed):
    section = section_from_scenario(scenario(), seed, layout="equalspread")
    areas = defaultdict(float)
    for space in section["spaces"]:
        areas[space["usage"]] += space["area_m2"]
        assert space["area_m2"] == pytest.approx(space["width_m"] * section["depth_m"])
    assert areas == pytest.approx({"residential": 123.25, "office": 37.75})
    assert len(section["floors"]) == 6
    assert sum(r["schematic_area_m2"] for r in section["roofs"]) == pytest.approx(161 / 2.5)


def test_deterministic_and_no_mutation():
    source = scenario()
    before = copy.deepcopy(source.as_dict())
    state = random.getstate()
    first = section_from_scenario(source)
    assert first == section_from_scenario(source)
    assert source.as_dict() == before
    assert random.getstate() == state


def test_small_areas_and_unknown_remainder():
    section = section_from_scenario(scenario(NFA_residential=0.001, NFA_office=0, NFA_total=1))
    areas = defaultdict(float)
    for space in section["spaces"]:
        areas[space["usage"]] += space["area_m2"]
    assert areas == pytest.approx({"residential": 0.001, "unallocated": 0.999})


def test_missing_counts_and_total():
    section = section_from_scenario(scenario(building_count=float("nan"), storey_count_avg=None, NFA_total=None), layout="equalspread")
    assert len(section["buildings"]) == len(section["floors"]) == 1
    assert "default_building_count" in {n["code"] for n in section["assumptions"]}


@pytest.mark.parametrize("values", [dict(NFA_total=1), dict(NFA_office=-1),
    dict(building_count=1.5), dict(storey_count_avg=0), dict(rh_avg=float("inf")),
    dict(PV_roof_area_percentage=2)])
def test_invalid_input(values):
    with pytest.raises(ValueError):
        section_from_scenario(scenario(**values))


def test_adjacency_and_exposed_roofs():
    section = section_from_scenario(scenario(building_count=1))
    spaces = {s["id"]: s for s in section["spaces"]}
    floors = {f["id"]: f for f in section["floors"]}
    assert any(a["axis"] == "vertical" for a in section["adjacency"])
    for edge in section["adjacency"]:
        a, b = (spaces[key] for key in edge["space_ids"])
        assert a != b
        assert edge["interval_m"][1] > edge["interval_m"][0]
        if edge["axis"] == "vertical":
            assert floors[b["floor_id"]]["index"] == floors[a["floor_id"]]["index"] + 1
            assert edge["interval_m"] == pytest.approx([
                max(a["x_m"], b["x_m"]),
                min(a["x_m"] + a["width_m"], b["x_m"] + b["width_m"]),
            ])
        else:
            assert a["floor_id"] == b["floor_id"]
            assert a["x_m"] + a["width_m"] == pytest.approx(b["x_m"])
    for roof in section["roofs"]:
        floor = floors[spaces[roof["space_id"]]["floor_id"]]
        for space in spaces.values():
            above = floors[space["floor_id"]]
            if above["index"] == floor["index"] + 1:
                overlap = min(roof["x_m"] + roof["width_m"], space["x_m"] + space["width_m"]) - max(roof["x_m"], space["x_m"])
                assert overlap <= 1e-9


def test_pv_conversion_overflow_and_disabled():
    section = section_from_scenario(scenario(PV_module_area=None, PV_kWp=100, PV_m2_per_kWp=5))
    pv = section["pv"]
    assert pv["requested_area_m2"] == 500
    assert sum(p["module_area_m2"] for p in pv["placements"]) + pv["unplaced_area_m2"] == pytest.approx(500)
    assert pv["unplaced_area_m2"] > 0
    assert section_from_scenario(scenario(PV_is_used=0))["pv"]["placements"] == []
    assert section_from_scenario(scenario(PV_module_area=None))["pv"]["requested_area_m2"] is None


def test_bundled_example():
    from pexl import Project
    source = Project.example()[0]
    section = section_from_scenario(source)
    assert sum(s["area_m2"] for s in section["spaces"]) == pytest.approx(source.v.NFA_total)


def test_office_starts_at_ground_floor_in_every_building():
    section = section_from_scenario(scenario(building_count=3, NFA_other=30, NFA_total=191), layout="equalspread")
    floors = {f["id"]: f for f in section["floors"]}
    sequences = []
    for building in section["buildings"]:
        members = [s for s in section["spaces"] if s["floor_id"] in building["floor_ids"]]
        assert members[0]["usage"] == "office"
        assert floors[members[0]["floor_id"]]["index"] == 0
        sequences.append([s["usage"] for s in members])
    assert sequences[0] == sequences[1] == sequences[2]
    assert len(section["facades"]) == 2 * len(section["floors"])


def test_roundoff_does_not_create_roofs_inside_full_storeys():
    source = scenario(building_count=3, storey_count_avg=4, NFA_total=5400)
    for key, area in dict(office=1350, retailfood=450, retailother=450,
                          schoolprim=600, schoolsec=600, other=450, residential=1500).items():
        setattr(source.v, f"NFA_{key}", area)
    section = section_from_scenario(source, layout="equalspread")
    expected_z = 4 * (source.v.rh_avg + source.v.rh_ceiling)

    assert all(r["z_m"] == pytest.approx(expected_z) for r in section["roofs"])
    assert sum(r["schematic_area_m2"] for r in section["roofs"]) == pytest.approx(1350)


@pytest.mark.parametrize("food,retail", [(450, 450), (1500, 1200), (0, 2400)])
def test_separate_residential_concentrates_usages_and_preserves_areas(food, retail):
    source = scenario(building_count=3, storey_count_avg=4)
    inputs = dict(office=1350, retailfood=food, retailother=retail,
                  schoolprim=600, schoolsec=600, other=450, residential=1500)
    for key, area in inputs.items():
        setattr(source.v, f"NFA_{key}", area)
    source.v.NFA_total = sum(inputs.values())
    section = section_from_scenario(source, layout="separateResidential")
    floors = {f["id"]: f for f in section["floors"]}
    totals = defaultdict(float)
    for space in section["spaces"]:
        floor = floors[space["floor_id"]]
        totals[space["usage"]] += space["area_m2"]
        if space["usage"] in ("retailfood", "retailother"):
            assert floor["index"] == 0
        if space["usage"] in ("retailfood", "schoolprim", "schoolsec", "other"):
            assert floor["building_id"] == "b0"
    assert totals == pytest.approx({key: area for key, area in inputs.items() if area})
    assert len(section["buildings"]) == 3
    assert section["layout"] == "separateResidential"


def test_office_fills_lower_levels_before_upper_buildings():
    source = scenario(NFA_office=500, NFA_residential=100, NFA_total=600,
                      building_count=2, storey_count_avg=3)
    section = section_from_scenario(source, layout="separateResidential")
    usage_by_floor = {s["floor_id"]: s["usage"] for s in section["spaces"]}
    assert usage_by_floor == {
        "b0:f0": "office", "b0:f1": "office", "b0:f2": "office",
        "b1:f0": "office", "b1:f1": "office", "b1:f2": "residential",
    }
    with pytest.raises(ValueError, match="Unknown section layout"):
        section_from_scenario(source, layout="invalid")


def test_single_building_can_expand_for_all_ground_floor_retail():
    source = scenario(NFA_office=0, NFA_residential=0, NFA_retailfood=900,
                      NFA_retailother=300, NFA_total=1200, building_count=1, storey_count_avg=5)
    section = section_from_scenario(source)
    assert len(section["floors"]) == 1
    assert sum(s["area_m2"] for s in section["spaces"]) == pytest.approx(1200)
    assert section["buildings"][0]["width_m"] == pytest.approx(1200 / 15)


def test_default_uses_least_occupied_buildings_and_other_buffers():
    source = scenario(building_count=3, storey_count_avg=4, NFA_total=5400)
    expected = dict(office=1350, retailfood=450, retailother=450,
                    schoolprim=600, schoolsec=600, other=450, residential=1500)
    for key, amount in expected.items():
        setattr(source.v, f"NFA_{key}", amount)
    section = section_from_scenario(source)
    floors = {f["id"]: f for f in section["floors"]}
    for usage, building in (("schoolprim", "b2"), ("schoolsec", "b0"), ("office", "b1")):
        blocks = [s for s in section["spaces"] if s["usage"] == usage]
        assert {floors[s["floor_id"]]["building_id"] for s in blocks} == {building}
        indices = sorted({floors[s["floor_id"]]["index"] for s in blocks})
        assert indices == list(range(min(indices), max(indices) + 1))
    totals = defaultdict(float)
    for space in section["spaces"]:
        totals[space["usage"]] += space["area_m2"]
    assert totals == pytest.approx(expected)
    assert section["voids"] == []
    assert all(f["index"] < 4 for f in section["floors"])
    for void in section["voids"]:
        for space in section["spaces"]:
            if space["floor_id"] == void["floor_id"]:
                overlap = min(void["x_m"] + void["width_m"], space["x_m"] + space["width_m"]) - max(void["x_m"], space["x_m"])
                assert overlap <= 1e-9
    for building in section["buildings"]:
        assigned = [s for s in section["spaces"] if s["floor_id"] in building["floor_ids"]]
        residential = [floors[s["floor_id"]]["index"] for s in assigned if s["usage"] == "residential"]
        other = [floors[s["floor_id"]]["index"] for s in assigned if s["usage"] != "residential"]
        if residential and other:
            assert min(residential) >= max(other)


def test_default_residential_fills_exhausted_other_buffer():
    source = scenario(NFA_office=40, NFA_residential=160, NFA_total=200,
                      NFA_other=0, building_count=1, storey_count_avg=2)
    section = section_from_scenario(source)
    assert section["voids"] == []
    ground_residential = [s for s in section["spaces"] if s["floor_id"] == "b0:f0" and s["usage"] == "residential"]
    assert sum(s["area_m2"] for s in ground_residential) == pytest.approx(60)
    assert len(section["floors"]) == 2
    assert sum(s["area_m2"] for s in section["spaces"]) == pytest.approx(200)


def test_residential_top_differences_are_distributed_evenly():
    source = scenario(NFA_office=0, NFA_residential=1000, NFA_total=1000,
                      building_count=3, storey_count_avg=2.5)
    section = section_from_scenario(source)
    for building in section["buildings"]:
        areas = [s["area_m2"] for s in section["spaces"] if s["floor_id"] in building["floor_ids"]]
        assert sum(areas) == pytest.approx(1000 / 3)
        assert len(building["floor_ids"]) == 3
    assert section["voids"] == []


@pytest.mark.parametrize("layout", ["default", "separateResidential", "equalspread"])
def test_twenty_metre_building_spacing(layout):
    source = scenario(NFA_office=0, NFA_residential=900, NFA_total=900,
                      building_count=3, storey_count_avg=2)
    section = section_from_scenario(source, layout=layout)
    previous_end = None
    for building in section["buildings"]:
        members = [s for s in section["spaces"] if s["floor_id"] in building["floor_ids"]]
        start = min(s["x_m"] for s in members)
        end = max(s["x_m"] + s["width_m"] for s in members)
        if previous_end is not None:
            assert start - previous_end == pytest.approx(20)
        previous_end = end


def custom_spec():
    return {"buildings": [
        {"name": "Long building", "relative_length": 2, "max_floors": 6, "usages": ["office", "residential"]},
        {"name": "Short building", "relative_length": 1, "max_floors": 4, "usages": ["residential"]},
    ]}


def test_custom_layout_capacity_ratios_floor_limits_and_no_mutation():
    source = scenario(NFA_office=600, NFA_residential=2400, NFA_total=3000,
                      building_count=-1, storey_count_avg=0)
    spec = custom_spec()
    before = copy.deepcopy(spec)
    result = section_layout_from_scenario(source, layout=spec)
    assert spec == before
    a, b = result["buildings"]
    assert a["usage_areas_m2"] == pytest.approx({"office": 600, "residential": 1800})
    assert b["usage_areas_m2"] == pytest.approx({"residential": 600})
    assert a["width_m"] / b["width_m"] == pytest.approx(2)
    assert b["x_m"] - a["width_m"] == pytest.approx(20)
    assert len(a["floor_ids"]) == 6 and len(b["floor_ids"]) == 3
    assert "total_building_length_m" not in result
    assert sum(s["area_m2"] for s in result["spaces"]) == pytest.approx(3000)
    sequence = [s["usage"] for s in result["spaces"] if s["floor_id"] in a["floor_ids"]]
    assert sequence == sorted(sequence, key=["office", "residential"].index)
    result["layout_spec"]["buildings"][0]["usages"].append("other")
    assert spec == before


def test_custom_explicit_share_and_partial_top():
    source = scenario(NFA_office=600, NFA_residential=2400, NFA_total=3000)
    spec = custom_spec()
    spec["buildings"][0]["usage_shares"] = {"residential": 0.6}
    result = section_layout_from_scenario(source, layout=spec)
    assert result["buildings"][0]["usage_areas_m2"]["residential"] == pytest.approx(1440)
    assert result["buildings"][1]["usage_areas_m2"]["residential"] == pytest.approx(960)
    for building in result["buildings"]:
        assert len(building["floor_ids"]) <= building["max_floors"]
        for fid in building["floor_ids"][:-1]:
            floor_area = sum(s["area_m2"] for s in result["spaces"] if s["floor_id"] == fid)
            assert floor_area == pytest.approx(building["width_m"] * 15)
    assert len(result["buildings"][0]["floor_ids"]) == 5


@pytest.mark.parametrize("change", [
    {"max_floors": 0}, {"max_floors": 2.5}, {"relative_length": -1},
    {"usages": ["offcie"]}, {"usages": ["office", "office"]},
    {"usage_shares": {"residential": 1.1}}, {"length": 10},
])
def test_custom_layout_invalid_fields(change):
    spec = custom_spec()
    spec["buildings"][0].update(change)
    with pytest.raises(ValueError):
        section_layout_from_scenario(scenario(), layout=spec)


def test_custom_missing_usage_and_bad_share_totals():
    spec = custom_spec()
    spec["buildings"][0]["usages"] = ["residential"]
    with pytest.raises(ValueError, match="missing"):
        section_layout_from_scenario(scenario(), layout=spec)
    spec = custom_spec()
    for building in spec["buildings"]:
        building["usage_shares"] = {"residential": 0.7}
    with pytest.raises(ValueError, match="shares"):
        section_layout_from_scenario(scenario(), layout=spec)


def test_section_layout_compatibility_alias():
    from pexl.spatial.section import section_from_scenario as old_import
    assert old_import is section_from_scenario is section_layout_from_scenario
    assert section_layout_from_scenario(scenario()) == section_from_scenario(scenario(), layout="default")


@pytest.mark.parametrize("depth", [0, -1, float("inf"), float("nan"), None])
def test_custom_depth_must_be_positive(depth):
    spec = {"buildings": [{"depth_m": depth, "max_floors": 3,
                           "usages": ["office", "residential"]}]}
    with pytest.raises(ValueError, match="depth_m"):
        section_layout_from_scenario(scenario(), layout=spec)


def test_mixed_depth_capacity_roofs_pv_and_local_axes():
    from xml.etree import ElementTree as ET
    from pexl.spatial import render_svg

    source = scenario(NFA_office=0, NFA_residential=4800, NFA_total=4800,
                      PV_module_area=2400)
    spec = {"buildings": [
        {"depth_m": 15, "max_floors": 2, "usages": ["residential"]},
        {"depth_m": 25, "max_floors": 2, "usages": ["residential"]},
    ]}
    result = section_layout_from_scenario(source, layout=spec)
    a, b = result["buildings"]
    assert a["width_m"] == pytest.approx(60)
    assert b["width_m"] == pytest.approx(60)
    assert a["usage_areas_m2"]["residential"] == pytest.approx(1800)
    assert b["usage_areas_m2"]["residential"] == pytest.approx(3000)
    assert result["depth_m"] is None
    floors = {f["id"]: f for f in result["floors"]}
    for space in result["spaces"]:
        assert space["area_m2"] == pytest.approx(space["width_m"] * floors[space["floor_id"]]["depth_m"])
    roofs = {r["id"]: r for r in result["roofs"]}
    assert sum(r["schematic_area_m2"] for r in roofs.values()) == pytest.approx(2400)
    assert result["pv"]["unplaced_area_m2"] == pytest.approx(0)
    for placement in result["pv"]["placements"]:
        assert placement["module_area_m2"] == pytest.approx(placement["width_m"] * roofs[placement["roof_id"]]["depth_m"])
    root = ET.fromstring(render_svg(result))
    ticks = [e for e in root.iter() if e.get("data-kind") == "axis-tick"]
    for building, area in [(a, 225), (b, 375)]:
        local = [t for t in ticks if t.get("data-building") == building["id"]]
        assert float(local[0].get("data-distance-m")) == 0
        assert float(local[1].get("data-area-m2")) == area
        assert float(local[1].get("x1")) - float(local[0].get("x1")) == pytest.approx(15 * 900 / 140)


@pytest.mark.parametrize("other", [0, 100, 1500])
def test_basement_conserves_area_and_respects_above_ground_limit(other):
    source = scenario(NFA_office=600, NFA_residential=1200,
                      NFA_other=other, NFA_total=1800 + other, PV_module_area=10000)
    spec = {"buildings": [{"basement": True, "max_floors": 3,
                           "usages": ["office", "residential"], "depth_m": 20}]}
    result = section_layout_from_scenario(source, layout=spec)
    assert "other" not in spec["buildings"][0]["usages"]
    floors = {f["id"]: f for f in result["floors"]}
    basement = [s for s in result["spaces"] if floors[s["floor_id"]]["index"] < 0]
    assert bool(basement) == bool(other)
    assert all(s["usage"] == "other" for s in basement)
    assert all(f["index"] < 3 for f in floors.values())
    assert sum(s["area_m2"] for s in result["spaces"]) == pytest.approx(1800 + other)
    for usage, area in [("office", 600), ("residential", 1200), ("other", other)]:
        assert sum(s["area_m2"] for s in result["spaces"] if s["usage"] == usage) == pytest.approx(area)
    assert all(r["z_m"] > 0 for r in result["roofs"])
    assert all(p["tilt_deg"] == 15 and p["arrangement"] == "butterfly" for p in result["pv"]["placements"])


def test_basement_flag_requires_boolean():
    with pytest.raises(ValueError, match="basement"):
        section_layout_from_scenario(scenario(), layout={"buildings": [
            {"basement": 1, "max_floors": 3, "usages": ["office", "residential"]}]})


@pytest.mark.parametrize("count", [-1, 1.5, True, "2", None])
def test_max_basements_requires_nonnegative_integer(count):
    with pytest.raises(ValueError, match="max_basements"):
        section_layout_from_scenario(scenario(), layout={"buildings": [
            {"max_basements": count, "max_floors": 2, "usages": ["office", "residential"]}]})


def test_basements_fill_downwards_in_default_order_and_keep_empty_space():
    source = scenario(NFA_office=600, NFA_residential=0, NFA_retailfood=100,
                      NFA_schoolprim=100, NFA_schoolsec=100, NFA_other=100, NFA_total=1000)
    spec = {"buildings": [{"max_floors": 2, "max_basements": 2, "usages": ["office"]}]}
    result = section_layout_from_scenario(source, layout=spec)
    floors = {f["id"]: f for f in result["floors"]}
    below = [s for s in result["spaces"] if floors[s["floor_id"]]["index"] < 0]
    assert [s["usage"] for s in below] == ["retailfood", "schoolprim", "schoolsec", "other"]
    assert [floors[s["floor_id"]]["index"] for s in below] == [-1, -1, -1, -2]
    assert sum(v["area_m2"] for v in result["voids"]) == pytest.approx(200)
    assert sum(s["area_m2"] for s in result["spaces"]) == pytest.approx(1000)
    assert any(floors[next(s["floor_id"] for s in result["spaces"] if s["id"] == a["space_ids"][0])]["index"] == -1
               and floors[next(s["floor_id"] for s in result["spaces"] if s["id"] == a["space_ids"][1])]["index"] == -2
               for a in result["adjacency"] if a["axis"] == "vertical")


@pytest.mark.parametrize("usage", ["office", "residential"])
def test_office_and_residential_only_below_when_explicit(usage):
    source = scenario(NFA_office=600, NFA_residential=600, NFA_total=1200)
    spec = {"buildings": [{"max_floors": 2, "max_basements": 2,
                            "usages": ["office", "residential"]}]}
    default = section_layout_from_scenario(source, layout=spec)
    assert len(default["voids"]) == 2
    assert all(":f-" not in s["floor_id"] for s in default["spaces"])
    spec["buildings"][0]["basement_usages"] = [usage]
    explicit = section_layout_from_scenario(source, layout=spec)
    below = [s for s in explicit["spaces"] if ":f-" in s["floor_id"]]
    assert below and all(s["usage"] == usage for s in below)
    assert sum(s["area_m2"] for s in explicit["spaces"]) == pytest.approx(1200)


def test_empty_basements_render_and_suggested_count_can_be_enabled():
    from xml.etree import ElementTree as ET
    from pexl.spatial import render_svg
    source = scenario(NFA_other=100, NFA_total=261)
    spec = suggest_section_layout(source)
    spec["buildings"][0]["max_basements"] = 2
    result = section_layout_from_scenario(source, layout=spec)
    assert result["layout_spec"]["buildings"][0]["basement_usages"][-1] == "other"
    for style in ("architectural", "hand_drawn", "blueprint"):
        root = ET.fromstring(render_svg(result, style=style))
        text = " ".join(root.itertext())
        assert "Basement 2" in text and "parking garage" in text
    spec["buildings"][0]["basement_usages"] = []
    result = section_layout_from_scenario(source, layout=spec)
    assert len(result["voids"]) == 2


@pytest.mark.parametrize("values, expected", [
    ({"hull_fenestration_rate": 0.4}, 0.4),
    ({"hull_window_m2": 100, "hull_ext_wall_wo_window_m2": 300}, 0.25),
    ({"hull_window_m2": 150, "hull_windows_horizontal_m2": 50, "hull_ext_wall_wo_window_m2": 300}, 0.25),
    ({"hull_fenestration_rate": 0.0}, 0.0),
    ({}, 0.3),
])
def test_facade_glazing_uses_schema_inputs(values, expected):
    result = section_layout_from_scenario(scenario(**values))
    assert result["facades"]
    for facade in result["facades"]:
        assert facade["glazing_ratio"] == pytest.approx(expected)
        assert facade["window_height_m"] == pytest.approx(facade["height_m"] * expected)


def test_invalid_fenestration_rate_rejected():
    with pytest.raises(ValueError, match="fenestration"):
        section_layout_from_scenario(scenario(hull_fenestration_rate=30))



def test_alternating_street_courtyard_sides():
    result=section_layout_from_scenario(scenario(building_count=4),layout="equalspread")
    assert [b["street_side"] for b in result["buildings"]] == ["left","right","left","right"]
    buildings={b["id"]:b for b in result["buildings"]}
    for facade in result["facades"]:
        expected="street" if facade["side"] == buildings[facade["building_id"]]["street_side"] else "courtyard"
        assert facade["exposure"] == expected


@pytest.mark.parametrize("mode", ["default", "equalspread", "separateResidential"])
def test_configurable_gaps_preserve_area(mode):
    source = scenario()
    source.v.building_count = 3
    a = section_layout_from_scenario(source,layout=mode,gap_m=0)
    b = section_layout_from_scenario(source,layout=mode,gap_m=35)
    assert b["gaps_m"] == [35,35]
    assert [s["area_m2"] for s in a["spaces"]] == [s["area_m2"] for s in b["spaces"]]
    for i, building in enumerate(b["buildings"]):
        assert building["x_m"] == pytest.approx(a["buildings"][i]["x_m"]+35*i)
    for left,right in zip(b["buildings"],b["buildings"][1:]):
        assert right["x_m"]-left["x_m"]-left["width_m"] == pytest.approx(35)


def test_gap_override_and_suggested_roundtrip():
    source = scenario()
    source.v.building_count=3
    spec=suggest_section_layout(source)
    spec["gap_m"]=12
    spec["buildings"][0]["gap_after_m"]=7
    result=section_layout_from_scenario(source,layout=spec)
    assert result["gaps_m"]==[7,12]
    assert section_layout_from_scenario(source,layout=result["layout_spec"])["gaps_m"]==[7,12]


@pytest.mark.parametrize("gap", [-1, float("inf"), float("nan"), None, True])
def test_invalid_gap_rejected(gap):
    with pytest.raises(ValueError):
        section_layout_from_scenario(scenario(),gap_m=gap)


# Versioned presentation specifications keep scenario quantities authoritative.
def versioned_layout():
    return {"layout_version": 1, "site": {"gap_m": 12},
            "defaults": {"geometry": {"depth_m": 15, "max_floors": 3},
                         "allocation": {"usages": ["office", "residential"]},
                         "systems": {"usages": {"office": {"heating": "tabs"}}}},
            "buildings": [{"id": "A"}, {"id": "B", "geometry": {"relative_length": 2}}]}


def test_versioned_normalization_json_roundtrip_and_no_mutation():
    import json
    from pexl.spatial import normalize_layout
    layout = versioned_layout()
    before = copy.deepcopy(layout)
    normalized = normalize_layout(layout)
    assert normalize_layout(json.loads(json.dumps(normalized))) == normalized
    assert layout == before
    source = scenario()
    original = copy.deepcopy(source.as_dict())
    section = section_from_scenario(source, layout=layout)
    assert [b['id'] for b in section['buildings']] == ['A','B']
    assert sum(s['area_m2'] for s in section['spaces']) == pytest.approx(161)
    assert section['buildings'][1]['width_m'] == pytest.approx(2*section['buildings'][0]['width_m'])
    assert source.as_dict() == original


def test_versioned_wildcard_building_override_and_pair_gap():
    layout = versioned_layout()
    layout['buildings'][0]['systems'] = {'usages': {'*': {'heating': 'radiator'}}, 'roof': []}
    layout['site']['gaps'] = [{'between':['A','B'], 'width_m':28, 'kind':'street'}]
    section = section_from_scenario(scenario(), layout=layout)
    assert section['systems']['buildings']['A']['usages']['office']['heating'] == 'radiator'
    assert section['systems']['buildings']['B']['usages']['office']['heating'] == 'tabs'
    assert section['gaps_m'] == [28]
    roof_ids = {r['id'] for r in section['roofs'] if r['building_id']=='B'}
    assert all(p['roof_id'] in roof_ids for p in section['pv']['placements'])


@pytest.mark.parametrize('change', [
    lambda l: l['buildings'][1].update(id='A'),
    lambda l: l.update(layout_version=2),
    lambda l: l.update(gap_m=15),
    lambda l: l['defaults']['geometry'].update(depth_m=True),
    lambda l: l['site'].update(gaps=[{'between':['A','X'],'width_m':3}]),
    lambda l: l.update(systems={'plant':[{'id':'P','kind':'heat_pump','location':{'building':'X','level':0}}]}),
])
def test_versioned_invalid_inputs_rejected(change):
    layout = versioned_layout(); change(layout)
    with pytest.raises(ValueError): section_from_scenario(scenario(), layout=layout)


def test_shared_plant_single_record_and_level_validation():
    layout = versioned_layout()
    layout['buildings'][0]['geometry'] = {'max_basements':1}
    layout['buildings'][0]['allocation'] = {'basement_usages':[]}
    layout['systems'] = {'plant':[{'id':'HP1','kind':'heat_pump','source':'groundwater',
                                   'location':{'building':'A','level':-1}, 'serves':['A','B']}]}
    section = section_from_scenario(scenario(), layout=layout)
    assert len(section['equipment']) == 1
    assert section['equipment'][0]['resolved_location'] == {'building':'A','level':-1}
    assert all(not s['plant'] for s in section['systems']['buildings'].values())
    layout['systems']['plant'][0]['location']['level']=-2
    with pytest.raises(ValueError, match='does not exist'):
        section_from_scenario(scenario(), layout=layout)


def test_geometry_reuse_preserves_semantics_and_rejects_area_changes():
    layout = versioned_layout(); source=scenario()
    section=section_from_scenario(source,layout=layout)
    original=copy.deepcopy(section)
    source.v.PV_module_area=20
    revised=section_from_scenario(source,layout=layout,reuse_geometry=section)
    assert revised['geometry_reused']
    assert revised['spaces'] == section['spaces']
    assert revised['pv']['requested_area_m2']==20
    assert section == original
    source.v.NFA_residential+=10;source.v.NFA_total+=10
    with pytest.raises(ValueError,match='geometry changed'):
        section_from_scenario(source,layout=layout,reuse_geometry=section)


def test_semantic_ids_survive_building_reorder():
    layout=versioned_layout()
    before=section_from_scenario(scenario(),layout=layout)
    layout['buildings'].reverse()
    after=section_from_scenario(scenario(),layout=layout)
    for key in ('spaces','facades','roofs'):
        assert {r['semantic_id'] for r in before[key]} == {r['semantic_id'] for r in after[key]}


def test_inferred_equipment_stays_unlocated_and_explicit_empty_clears():
    source=scenario(QHmax_2th_m2=25,heat_th2_carrier_type='Fernwärme Wien')
    layout=versioned_layout()
    section=section_from_scenario(source,layout=layout)
    assert section['equipment'][0]['kind']=='district_heating'
    assert 'resolved_location' not in section['equipment'][0]
    layout['systems']={'plant':[]}
    assert section_from_scenario(source,layout=layout)['equipment']==[]


@pytest.mark.parametrize('style',['architectural','hand_drawn','blueprint','annotations'])
def test_versioned_svg_semantic_targets_and_shared_equipment(style):
    from xml.etree import ElementTree as ET
    from pexl.spatial import render_svg
    layout=versioned_layout()
    layout['systems']={'plant':[{'id':'HP1','kind':'heat_pump','location':{'building':'A','level':0},'serves':['A','B']}]}
    layout['buildings'][0]['envelope']={'street':{'facade':{'style':'gruenderzeit'}}}
    section=section_from_scenario(scenario(),layout=layout)
    before=copy.deepcopy(section)
    root=ET.fromstring(render_svg(section,style=style))
    assert len([n for n in root.iter() if n.get('data-kind')=='equipment'])==1
    assert len([n for n in root.iter() if n.get('data-kind')=='service-connection'])==1
    actual={n.get('data-semantic-id') for n in root.iter()}
    for key in ('spaces','facades','roofs'):
        assert {s['semantic_id'] for s in section[key]} <= actual
    assert section==before


def test_normalized_local_plant_is_idempotent():
    from pexl.spatial import normalize_layout
    layout=versioned_layout()
    layout['defaults']['systems']['plant']=['district_heating']
    norm=normalize_layout(layout)
    assert len(norm['systems']['plant'])==2
    assert normalize_layout(norm)==norm


def test_legacy_normalization_preserves_area_allocation():
    from pexl.spatial import normalize_layout
    legacy={'buildings':[{'name':'One','max_floors':3,'usages':['office','residential']}]}
    old=section_from_scenario(scenario(),layout=legacy)
    new=section_from_scenario(scenario(),layout=normalize_layout(legacy))
    assert old['geometry_signature']==new['geometry_signature']
