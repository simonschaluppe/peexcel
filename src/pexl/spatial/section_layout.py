"""Area-preserving schematic sections; no simulation or rendering logic."""

from __future__ import annotations

from math import ceil, isfinite, isnan, isclose
from copy import deepcopy

from .system_resolution import resolve_systems
from .layout_spec import normalize_layout, allocation_layout
from .resolved_layout import finish_layout, geometry_key
from random import Random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pexl.model.scenario import Scenario


def _number(value, name: str) -> float | None:
    if value is None:
        return None
    try:
        number = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{name} must be numeric or missing") from exc
    if isnan(number):
        return None
    if not isfinite(number) or number < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return number


def _note(notes: list, code: str, description: str) -> None:
    notes.append({"code": code, "description": description})


def _read_inputs(scenario: Scenario, *, custom_layout: bool = False) -> dict:
    notes = []

    def read(name):
        return _number(getattr(scenario.v, name), name)

    def default(name, value, positive=True):
        supplied = read(name)
        if supplied is None:
            _note(notes, f"default_{name}", f"Missing {name}: assumed {value}.")
            return value
        if positive and supplied == 0:
            raise ValueError(f"{name} must be positive")
        return supplied

    usages = []
    missing = []
    for meta, value in scenario.select(
        domain="usage", measure="area", spatial_scope="NFA", entity_group="usage"
    ).items():
        area = _number(value, meta.var_name)
        if area is None:
            missing.append(meta.var_name)
        elif area > 0:
            usages.append({"usage": meta.entity_key, "source_variable": meta.var_name,
                           "label": meta.label_de or meta.var_name, "area_m2": area})
    known = sum(u["area_m2"] for u in usages)
    total = read("NFA_total")
    if total is None:
        total = known
        _note(notes, "derived_total", "Missing NFA_total: using the sum of known usage areas.")
    tolerance = max(1e-9, total * 1e-12)
    if known > total + tolerance:
        raise ValueError("Usage areas exceed NFA_total")
    if known > total:
        total = known  # floating-point roundoff, never rescale usage values
    if total > known:
        usages.append({"usage": "unallocated", "source_variable": "NFA_total",
                       "label": "Unallocated usage", "area_m2": total - known})
        _note(notes, "unallocated_usage", "The remainder of NFA_total has no known usage.")
    if missing:
        _note(notes, "unknown_usage_areas", "Unknown areas: " + ", ".join(missing) + ".")
    if total <= 0:
        raise ValueError("A positive NFA_total or positive usage areas are required")
    buildings = 1 if custom_layout else default("building_count", 1)
    if not float(buildings).is_integer():
        raise ValueError("building_count must be an integer")
    storeys = 1 if custom_layout else default("storey_count_avg", 1)
    height = default("rh_avg", 3.0)
    slab = default("rh_ceiling", 0.35, positive=False)
    _note(notes, "schematic_depth", "Depth is specified per building, defaulting to 15 m." if custom_layout else "A common section depth of 15 m is assumed.")
    _note(notes, "schematic_geometry", "NFA-based widths, uniform room heights, flat roofs and building gaps are schematic.")

    enabled = read("PV_is_used")
    if enabled not in (None, 0, 1):
        raise ValueError("PV_is_used must be 0, 1 or missing")
    area, power, factor = read("PV_module_area"), read("PV_kWp"), read("PV_m2_per_kWp")
    if enabled == 0:
        pv_area = 0.0
        if (area or 0) > 0 or (power or 0) > 0:
            _note(notes, "disabled_pv", "PV_is_used is false; supplied PV sizing is not placed.")
    else:
        pv_area = area
        if area is None and power is not None and factor is not None:
            pv_area = power * factor
            _note(notes, "derived_pv_area", "PV module area derived from PV_kWp and PV_m2_per_kWp.")
        if area is not None and power is not None and factor is not None:
            if not isclose(area, power * factor, rel_tol=1e-6, abs_tol=1e-9):
                _note(notes, "pv_sizing_mismatch", "PV_module_area differs from power times specific area; module area takes precedence.")
        if enabled is None:
            _note(notes, "unknown_pv_enabled", "PV_is_used is missing; placement follows available module sizing.")
        if pv_area is None:
            _note(notes, "unknown_pv_area", "PV module area is unknown; no PV geometry is generated.")
    context = {name: read(name) for name in (
        "GFA_total", "plot_area", "FSI", "hull_roof_m2", "hull_fundament_m2",
        "PV_roof_area_percentage", "hull_fenestration_rate", "hull_window_m2",
        "hull_ext_wall_wo_window_m2", "hull_windows_horizontal_m2",
        "hull_transmittance_walls", "hull_transmittance_roof", "PV_kWp", "PV_m2_per_kWp",
    )}
    glazing = context["hull_fenestration_rate"]
    windows = context["hull_window_m2"]
    opaque = context["hull_ext_wall_wo_window_m2"]
    horizontal = context["hull_windows_horizontal_m2"]
    if windows is not None and horizontal is not None:
        if horizontal > windows:
            raise ValueError("Horizontal window area exceeds total window area")
        windows -= horizontal
    derived = windows / (windows + opaque) if windows is not None and opaque is not None and windows + opaque > 0 else None
    if glazing is not None:
        if glazing > 1:
            raise ValueError("hull_fenestration_rate must be a fraction between 0 and 1")
        glazing_source = "hull_fenestration_rate"
        if derived is not None and not isclose(glazing, derived, rel_tol=1e-6, abs_tol=1e-9):
            _note(notes, "glazing_mismatch", "Fenestration rate differs from window/(opaque wall + window) area; explicit rate takes precedence.")
    elif derived is not None:
        glazing, glazing_source = derived, "hull_window_m2 / (hull_ext_wall_wo_window_m2 + hull_window_m2)"
        _note(notes, "derived_glazing", "Fenestration derived from window and opaque-wall areas; horizontal glazing is excluded when supplied.")
    else:
        glazing, glazing_source = 0.3, "schematic_default"
        _note(notes, "default_glazing", "Missing fenestration inputs: 30% glazing assumed for above-ground facades; buried basement walls remain opaque.")
    context["section_glazing_ratio"] = glazing
    context["section_glazing_source"] = glazing_source
    ratio = context["PV_roof_area_percentage"]
    if ratio is not None and ratio > 1:
        raise ValueError("PV_roof_area_percentage must be between 0 and 1")
    if ratio is not None and context["hull_roof_m2"] is not None and pv_area is not None and enabled != 0:
        if not isclose(pv_area, ratio * context["hull_roof_m2"], rel_tol=1e-6, abs_tol=1e-9):
            _note(notes, "pv_roof_ratio_mismatch", "PV module area differs from roof area times PV roof fraction; module sizing takes precedence.")
    return {"usages": usages, "total": total, "buildings": int(buildings),
            "storeys": storeys, "height": height, "slab": slab,
            "pv_area": pv_area, "context": context, "assumptions": notes}


def _allocate_equalspread(inputs: dict, seed: int) -> dict:
    rng = Random(seed)
    buildings, floors, spaces = [], [], []
    footprint = inputs["total"] / inputs["buildings"] / inputs["storeys"]
    depth = 15.0
    usages = [dict(u, area_m2=u["area_m2"] / inputs["buildings"]) for u in inputs["usages"]]
    rng.shuffle(usages)
    usages.sort(key=lambda u: 0 if u["usage"] == "office" else 2 if u["usage"] == "residential" else 1)
    for b in range(inputs["buildings"]):
        bid = f"b{b}"
        origin = b * (footprint / depth + 20.0)
        building = {"id": bid, "floor_ids": []}
        buildings.append(building)
        # Allocate by intersecting cumulative usage and floor-area intervals.
        start = 0.0
        intervals = []
        for usage in usages:
            end = start + usage["area_m2"]
            intervals.append((start, end, usage))
            start = end
        for f in range(ceil(inputs["storeys"])):
            fid = f"{bid}:f{f}"
            building["floor_ids"].append(fid)
            floors.append({"id": fid, "building_id": bid, "index": f,
                           "z_m": f * (inputs["height"] + inputs["slab"]),
                           "height_m": inputs["height"], "slab_thickness_m": inputs["slab"]})
            lo = f * footprint
            hi = start if f == ceil(inputs["storeys"]) - 1 else min((f + 1) * footprint, start)
            for left, right, usage in intervals:
                a, z = max(lo, left), min(hi, right)
                if z > a:
                    spaces.append({**usage, "id": f"{fid}:s{len(spaces)}", "floor_id": fid,
                                   "area_m2": z - a, "x_m": origin + (a - lo) / depth,
                                   "width_m": (z - a) / depth})
    return {"buildings": buildings, "floors": floors, "spaces": spaces}


def _allocate_separate_residential(inputs: dict) -> dict:
    """Concentrate special uses, then offices, then residential infill."""
    count = inputs["buildings"]
    baseline = inputs["total"] / count / inputs["storeys"]
    usages = {u["usage"]: u for u in inputs["usages"]}
    area = lambda key: usages.get(key, {}).get("area_m2", 0.0)
    capacities = [baseline] * count
    capacities[0] = max(baseline, area("retailfood"))
    # Retail stays at ground level, even if every original footprint is full.
    deficit = area("retailfood") + area("retailother") - sum(capacities)
    if deficit > 0:
        recipients = list(range(1, count)) or [0]
        for b in recipients:
            capacities[b] += deficit / len(recipients)
    slots = {}

    def slot(b, f):
        return slots.setdefault((b, f), {"used": 0.0, "parts": []})

    def place(key, candidates):
        remaining = area(key)
        if remaining == 0:
            return
        usage = usages[key]
        for b, f in candidates:
            current = slot(b, f)
            take = min(remaining, max(0.0, capacities[b] - current["used"]))
            if take > 0:
                current["parts"].append((current["used"], take, usage))
                current["used"] += take
                remaining -= take
            if take > 0 and remaining <= max(1e-10, area(key) * 1e-14):
                # Preserve roundoff remainder in the final occupied segment.
                if remaining > 0 and current["parts"]:
                    offset, size, item = current["parts"][-1]
                    current["parts"][-1] = (offset, size + remaining, item)
                    current["used"] += remaining
                return
        if remaining > 0:
            raise ValueError(f"Cannot allocate {key}: insufficient schematic capacity")

    def first_building():
        f = 0
        while True:
            yield 0, f
            f += 1

    place("retailfood", [(0, 0)])
    place("retailother", [(b, 0) for b in range(count)])
    # Reserve any remaining ground-floor area for 'other' before schools.
    place("other", first_building())
    place("schoolprim", first_building())
    place("schoolsec", first_building())
    for key in sorted(usages.keys() - {"retailfood", "retailother", "other", "schoolprim", "schoolsec", "office", "residential", "unallocated"}):
        place(key, first_building())
    levels = max(ceil(inputs["storeys"]), max((f + 1 for _, f in slots), default=1))
    office_slots = [(b, f) for f in range(min(2, levels)) for b in range(count)]
    office_slots += [(b, f) for b in range(count) for f in range(2, levels)]
    place("office", office_slots)
    # Remaining residential space fills each building from the bottom upwards.
    remaining_slots = [(b, f) for b in range(count) for f in range(levels)]
    place("residential", remaining_slots)
    place("unallocated", remaining_slots)
    buildings, floors, spaces = [], [], []
    origin = 0.0
    for b in range(count):
        bid = f"b{b}"
        building = {"id": bid, "floor_ids": [], "x_m": origin,
                    "width_m": capacities[b] / 15.0}
        buildings.append(building)
        for f in range(levels):
            current = slots.get((b, f))
            if not current or not current["parts"]:
                continue
            fid = f"{bid}:f{f}"
            building["floor_ids"].append(fid)
            floors.append({"id": fid, "building_id": bid, "index": f,
                           "z_m": f * (inputs["height"] + inputs["slab"]),
                           "height_m": inputs["height"], "slab_thickness_m": inputs["slab"]})
            for offset, size, usage in current["parts"]:
                spaces.append({**usage, "id": f"{fid}:s{len(spaces)}", "floor_id": fid,
                               "area_m2": size, "x_m": origin + offset / 15.0, "width_m": size / 15.0})
        origin += capacities[b] / 15.0 + 20.0
    _note(inputs["assumptions"], "separate_residential_distribution", "Special uses concentrate in building 1; retail remains at ground level, other and schools extend upwards. Offices fill ground and first floors, then higher floors building by building; residential fills the remainder.")
    _note(inputs["assumptions"], "adapted_buildings", "Building count and usage areas are preserved; footprints and occupied storey counts may differ from the supplied average. Empty capacity is not drawn.")
    return {"buildings": buildings, "floors": floors, "spaces": spaces}


def _allocate_default(inputs: dict) -> dict:
    """Keep usage blocks together, buffer with other, balance residential tops."""
    count = inputs["buildings"]
    usages = {u["usage"]: u for u in inputs["usages"]}
    area = lambda key: usages.get(key, {}).get("area_m2", 0.0)
    capacities = [inputs["total"] / count / inputs["storeys"]] * count
    capacities[0] = max(capacities[0], area("retailfood"))
    deficit = area("retailfood") + area("retailother") - sum(capacities)
    if deficit > 0:
        recipients = list(range(1, count)) or [0]
        for b in recipients:
            capacities[b] += deficit / len(recipients)
    slots = {}
    allocated = [0.0] * count
    other_left = area("other")
    residential_left = area("residential")

    def append(b, f, key, amount):
        current = slots.setdefault((b, f), {"used": 0.0, "parts": []})
        current["parts"].append((current["used"], amount, usages[key]))
        current["used"] += amount
        allocated[b] += amount

    def next_floor(b):
        return max((f + 1 for building, f in slots if building == b), default=0)

    def least_occupied():
        return min(range(count), key=lambda b: (allocated[b], b))

    def block(b, key, amount):
        """Start above sealed floors and keep the whole block in this building."""
        f = next_floor(b)
        remaining = amount
        while remaining > 0:
            take = min(remaining, capacities[b])
            append(b, f, key, take)
            remaining -= take
            f += 1

    def close_last_floor(b):
        nonlocal other_left, residential_left
        f = next_floor(b) - 1
        if f < 0:
            return
        current = slots[b, f]
        gap = max(0.0, capacities[b] - current["used"])
        take = min(gap, other_left)
        if take > 0:
            append(b, f, "other", take)
            other_left -= take
        gap = max(0.0, capacities[b] - current["used"])
        take = min(gap, residential_left)
        if take > 0:
            append(b, f, "residential", take)
            residential_left -= take

    # Keep both retail categories at ground level before closing retail floors.
    if area("retailfood") > 0:
        append(0, 0, "retailfood", area("retailfood"))
    remaining = area("retailother")
    for b in range(count):
        free = capacities[b] - slots.get((b, 0), {}).get("used", 0.0)
        take = min(remaining, max(0.0, free))
        if take > 0:
            append(b, 0, "retailother", take)
            remaining -= take
    if remaining > max(1e-9, area("retailother") * 1e-12):
        raise ValueError("Cannot fit retail on ground floors")
    if remaining > 0:
        # Correct the final floating-point residue without losing usage area.
        b = max(b for b in range(count) if (b, 0) in slots)
        append(b, 0, "retailother", remaining)
    for b in range(count):
        if (b, 0) in slots:
            close_last_floor(b)
    for key in ("schoolprim", "schoolsec", "office"):
        if area(key) > 0:
            b = least_occupied()
            block(b, key, area(key))
            close_last_floor(b)
    if other_left > 0:
        b = least_occupied()
        block(b, "other", other_left)
        other_left = 0.0
        close_last_floor(b)
    known = {"retailfood", "retailother", "schoolprim", "schoolsec", "office", "other", "residential"}
    for key in sorted(usages.keys() - known):
        b = least_occupied()
        block(b, key, area(key))
        close_last_floor(b)

    # Water-fill the shortest tops after residential has filled buffer gaps.
    heights = [float(next_floor(b)) for b in range(count)]
    residential = [0.0] * count
    remaining = residential_left
    while remaining > 0:
        lowest = min(heights)
        group = [b for b in range(count) if isclose(heights[b], lowest, abs_tol=1e-12)]
        higher = [h for h in heights if h > lowest + 1e-12]
        step = min(higher) - lowest if higher else 1.0
        needed = step * sum(capacities[b] for b in group)
        budget = min(remaining, needed)
        distributed = 0.0
        for index, b in enumerate(group):
            take = budget - distributed if index == len(group) - 1 else budget * capacities[b] / sum(capacities[k] for k in group)
            residential[b] += take
            heights[b] += take / capacities[b]
            distributed += take
        remaining -= budget
    for b, amount in enumerate(residential):
        if amount > 0:
            block(b, "residential", amount)

    buildings, floors, spaces, voids = [], [], [], []
    origin = 0.0
    for b in range(count):
        bid = f"b{b}"
        building = {"id": bid, "floor_ids": [], "x_m": origin, "width_m": capacities[b] / 15.0}
        buildings.append(building)
        for f in range(next_floor(b)):
            current = slots[b, f]
            fid = f"{bid}:f{f}"
            building["floor_ids"].append(fid)
            floors.append({"id": fid, "building_id": bid, "index": f,
                           "z_m": f * (inputs["height"] + inputs["slab"]),
                           "height_m": inputs["height"], "slab_thickness_m": inputs["slab"]})
            for offset, size, usage in current["parts"]:
                spaces.append({**usage, "id": f"{fid}:s{len(spaces)}", "floor_id": fid,
                               "area_m2": size, "x_m": origin + offset / 15.0, "width_m": size / 15.0})
        origin += capacities[b] / 15.0 + 20.0
    _note(inputs["assumptions"], "default_distribution", "After ground-floor retail, each school and office usage forms one block in the least occupied building. Other tops up each block's last floor, followed by residential from its remaining area budget. No unassigned schematic spaces are added.")
    _note(inputs["assumptions"], "balanced_tops", "After filling buffer gaps, remaining residential fills the lowest building tops first, sharing height differences evenly where possible. Continuous blocks take priority over equal heights.")
    _note(inputs["assumptions"], "adapted_buildings", "Building count and usage areas are preserved; footprints and occupied storey counts may differ from the supplied average.")
    return {"buildings": buildings, "floors": floors, "spaces": spaces, "voids": voids}


def _allocate_custom(inputs: dict, specification: dict, valid_usages: set[str]) -> dict:
    """Allocate scenario areas using a JSON-compatible building specification."""
    if "buildings" not in specification or set(specification) - {"buildings", "systems", "gap_m", "facade_style"}:
        raise ValueError("A custom layout accepts buildings, systems, gap_m and facade_style")
    raw_buildings = specification["buildings"]
    if not isinstance(raw_buildings, list) or not raw_buildings:
        raise ValueError("layout.buildings must be a nonempty list")
    specs = []
    for index, raw in enumerate(raw_buildings):
        if not isinstance(raw, dict):
            raise ValueError(f"Building {index + 1} must be a dictionary")
        unknown = set(raw) - {"id", "name", "relative_length", "max_floors", "usages", "usage_shares", "depth_m", "basement", "max_basements", "basement_usages", "systems", "gap_after_m", "facade_style"}
        if unknown:
            raise ValueError(f"Unknown building fields: {sorted(unknown)}")
        depth = _number(raw.get("depth_m", 15), "depth_m")
        if not depth:
            raise ValueError("depth_m must be finite and positive")
        weight = _number(raw.get("relative_length", 1), "relative_length")
        limit = _number(raw.get("max_floors"), "max_floors")
        if not weight or not limit or not limit.is_integer():
            raise ValueError("relative_length must be positive and max_floors a positive integer")
        order = raw.get("usages")
        if not isinstance(order, list) or not order or not all(isinstance(k, str) for k in order):
            raise ValueError("Each building needs an ordered nonempty list of usage keys")
        if len(order) != len(set(order)) or set(order) - valid_usages:
            raise ValueError(f"Unknown or repeated usage keys in building {index + 1}: {order}")
        legacy_basement = raw.get("basement", False)
        if not isinstance(legacy_basement, bool):
            raise ValueError("basement must be a boolean; use max_basements for a count")
        basement_count = raw.get("max_basements", int(legacy_basement))
        if isinstance(basement_count, bool) or not isinstance(basement_count, int) or basement_count < 0:
            raise ValueError("max_basements must be a nonnegative integer")
        if "basement" in raw and "max_basements" in raw and bool(basement_count) != legacy_basement:
            raise ValueError("basement and max_basements conflict")
        default_below = ["retailfood", "retailother", "schoolprim", "schoolsec", "other"]
        below = raw.get("basement_usages", default_below if basement_count else [])
        if not isinstance(below, list) or not all(isinstance(k, str) for k in below):
            raise ValueError("basement_usages must be a list of usage keys")
        if len(below) != len(set(below)) or set(below) - valid_usages:
            raise ValueError("Unknown or repeated basement_usages")
        if below and not basement_count:
            raise ValueError("basement_usages requires max_basements > 0")
        order = list(order)
        shares = raw.get("usage_shares", {})
        if not isinstance(shares, dict) or set(shares) - (set(order) | set(below)):
            raise ValueError("usage_shares keys must occur in usages or basement_usages")
        clean_shares = {}
        for key, value in shares.items():
            share = _number(value, f"usage_shares.{key}")
            if share is None or share > 1:
                raise ValueError("Explicit usage shares must be numbers between 0 and 1")
            clean_shares[key] = share
        name = raw.get("name", f"Building {index + 1}")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Building names must be nonempty strings")
        specs.append({**({"id": raw["id"]} if "id" in raw else {}), "name": name, "relative_length": weight, "max_floors": int(limit),
                      "usages": list(order), "usage_shares": clean_shares, "depth_m": depth, "max_basements": basement_count, "basement_usages": list(below)})
        for key in ("systems", "gap_after_m", "facade_style"):
            if key in raw:
                specs[-1][key] = deepcopy(raw[key])
    # Normalize before multiplying, so the ratio scale itself has no effect.
    weight_sum = sum(s["relative_length"] for s in specs)
    if not isfinite(weight_sum):
        raise ValueError("Relative lengths are too large")
    weights = [s["relative_length"] / weight_sum for s in specs]
    allocations = [{} for _ in specs]
    active = {u["usage"]: u for u in inputs["usages"]}
    def capacity(spec, key):
        levels = (spec["max_floors"] if key in spec["usages"] else 0)
        levels += spec["max_basements"] if key in spec["basement_usages"] else 0
        return spec["depth_m"] * levels

    # Validate shares even when the scenario currently has zero area for a usage.
    for key in sorted(set().union(*((set(s["usages"]) | set(s["basement_usages"])) for s in specs)) | set(active)):
        eligible = [i for i, s in enumerate(specs) if key in s["usages"] or key in s["basement_usages"]]
        if not eligible:
            raise ValueError(f"Positive scenario usage {key!r} is missing from the layout")
        explicit = {i: specs[i]["usage_shares"][key] for i in eligible if key in specs[i]["usage_shares"]}
        remainder = 1.0 - sum(explicit.values())
        automatic = [i for i in eligible if i not in explicit]
        if remainder < -1e-12 or (not automatic and abs(remainder) > 1e-12):
            raise ValueError(f"Invalid shares for {key!r}: explicit shares must total 1 when all are specified, and never exceed 1")
        portions = dict(explicit)
        denominator = sum(weights[i] * capacity(specs[i], key) for i in automatic)
        for i in automatic:
            portions[i] = max(0.0, remainder) * weights[i] * capacity(specs[i], key) / denominator
        if key not in active:
            continue
        positive = [i for i in eligible if portions.get(i, 0) > 0]
        distributed = 0.0
        for position, i in enumerate(positive):
            total = active[key]["area_m2"]
            amount = total - distributed if position == len(positive) - 1 else total * portions[i]
            allocations[i][key] = amount
            distributed += amount
    totals = [sum(a.values()) for a in allocations]
    if any(total <= 0 for total in totals):
        raise ValueError("Each specified building must receive positive scenario area")
    # Fit above-only, below-only and shared budgets without changing usage totals.
    length_limits = []
    for i, total in enumerate(totals):
        spec, amounts = specs[i], allocations[i]
        width_depth = weights[i] * spec["depth_m"]
        above_only = sum(area for key, area in amounts.items() if key not in spec["basement_usages"])
        below_only = sum(area for key, area in amounts.items() if key not in spec["usages"])
        length_limits.append(above_only / (width_depth * spec["max_floors"]))
        if spec["max_basements"]:
            length_limits.append(below_only / (width_depth * spec["max_basements"]))
        length_limits.append(total / (width_depth * (spec["max_floors"] + spec["max_basements"])))
    length_total = max(length_limits)
    if not isfinite(length_total):
        raise ValueError("The custom layout produces nonfinite dimensions")
    buildings, floors, spaces, voids = [], [], [], []
    origin = 0.0
    for i, spec in enumerate(specs):
        depth = spec["depth_m"]
        building_length = length_total * weights[i]
        footprint = building_length * depth
        amounts = allocations[i]
        below_amounts = {}
        remaining = footprint * spec["max_basements"]
        mandatory = sum(area for key, area in amounts.items() if key not in spec["usages"])
        for key in spec["basement_usages"]:
            area = amounts.get(key, 0)
            if key not in spec["usages"]:
                take = area
                mandatory -= area
            else:
                take = min(area, max(0.0, remaining - mandatory))
            below_amounts[key] = take
            remaining -= take
        above_amounts = {key: area - below_amounts.get(key, 0) for key, area in amounts.items()}
        occupied = min(spec["max_floors"], max(0, ceil(round(sum(above_amounts.values()) / footprint, 12))))
        bid = spec.get("id", f"b{i}")
        building = {"id": bid, "name": spec["name"], "floor_ids": [], "x_m": origin,
                    "width_m": building_length, "depth_m": depth, "relative_length": spec["relative_length"],
                    "max_floors": spec["max_floors"], "max_basements": spec["max_basements"],
                    "usage_areas_m2": dict(amounts)}
        buildings.append(building)
        for order, budget, count, below_ground in (
            (spec["basement_usages"], below_amounts, spec["max_basements"], True),
            (spec["usages"], above_amounts, occupied, False),
        ):
            intervals, cursor = [], 0.0
            for key in order:
                area = budget.get(key, 0)
                if area > 0:
                    intervals.append((cursor, cursor + area, active[key]))
                    cursor += area
            for level in range(count):
                floor_index = -level - 1 if below_ground else level
                fid = f"{bid}:f{floor_index}"
                building["floor_ids"].append(fid)
                floors.append({"id": fid, "building_id": bid, "index": floor_index,
                               "z_m": floor_index * (inputs["height"] + inputs["slab"]),
                               "height_m": inputs["height"], "slab_thickness_m": inputs["slab"]})
                lo, hi = level * footprint, min((level + 1) * footprint, cursor)
                if level == count - 1:
                    hi = max(hi, cursor)  # retain roundoff residual on the last floor
                used = 0.0
                for left, right, usage in intervals:
                    a, b = max(lo, left), min(hi, right)
                    if b > a:
                        spaces.append({**usage, "id": f"{fid}:s{len(spaces)}", "floor_id": fid,
                                       "area_m2": b - a, "x_m": origin + (a - lo) / depth,
                                       "width_m": (b - a) / depth})
                        used += b - a
                empty = footprint - used
                if below_ground and empty > max(1e-9, footprint * 1e-12):
                    voids.append({"id": f"{fid}:empty", "floor_id": fid, "area_m2": empty,
                                  "x_m": origin + used / depth, "width_m": empty / depth,
                                  "kind": "empty_basement"})
        origin += building_length + 20.0
    if any(spec["max_basements"] for spec in specs):
        _note(inputs["assumptions"], "basement", "Basements fill B1 downwards in basement_usages order. Retail, schools, then other are eligible by default; office and residential require explicit basement_usages. Unfilled basement footprint remains empty and is excluded from NFA. Below-only usage capacity is reserved before shared usages; no area is discarded.")
    _note(inputs["assumptions"], "custom_layout", "Building count, usage order, relative lengths and floor limits come from the custom layout, overriding scenario count and average storeys for this projection.")
    _note(inputs["assumptions"], "custom_shares", "Explicit shares apply to each scenario usage total; remaining area is split by relative length times depth times eligible above-ground and basement floor capacity among unspecified buildings.")
    _note(inputs["assumptions"], "derived_length", "Total building length is the smallest fitting the allocated areas at the supplied length ratios and floor limits. Gaps are excluded; the final above-ground floor may be partial, while basement floors retain their footprint with any unfilled area shown empty.")
    return {"buildings": buildings, "floors": floors, "spaces": spaces, "voids": voids,
            "layout_spec": {"buildings": specs, **({"systems": deepcopy(specification["systems"])} if "systems" in specification else {})}}


def _build_adjacency(spaces: list[dict], floors: list[dict]) -> list[dict]:
    floor_by_id = {f["id"]: f for f in floors}
    result = []
    for i, a in enumerate(spaces):
        fa = floor_by_id[a["floor_id"]]
        for b in spaces[i + 1:]:
            fb = floor_by_id[b["floor_id"]]
            if fa["building_id"] != fb["building_id"]:
                continue
            if fa["index"] == fb["index"]:
                if isclose(a["x_m"] + a["width_m"], b["x_m"], abs_tol=1e-9, rel_tol=0):
                    result.append({"space_ids": [a["id"], b["id"]], "axis": "horizontal",
                                   "interval_m": [fa["z_m"], fa["z_m"] + fa["height_m"]]})
            elif abs(fb["index"] - fa["index"]) == 1:
                lo = max(a["x_m"], b["x_m"])
                hi = min(a["x_m"] + a["width_m"], b["x_m"] + b["width_m"])
                if hi > lo:
                    result.append({"space_ids": [a["id"], b["id"]], "axis": "vertical",
                                   "interval_m": [lo, hi]})
    return result


def _build_roofs(spaces: list[dict], floors: list[dict]) -> list[dict]:
    floor_by_id = {f["id"]: f for f in floors}
    roofs = []
    for space in spaces:
        floor = floor_by_id[space["floor_id"]]
        if floor["index"] < 0:
            continue  # below-ground surfaces are not PV roofs
        exposed = [(space["x_m"], space["x_m"] + space["width_m"])]
        for upper in spaces:
            other = floor_by_id[upper["floor_id"]]
            if other["building_id"] != floor["building_id"] or other["index"] != floor["index"] + 1:
                continue
            left, right = upper["x_m"], upper["x_m"] + upper["width_m"]
            remaining = []
            for a, b in exposed:
                # Snap coincident boundaries before subtracting coverage. Tiny
                # roundoff gaps must not become roofs (and acquire PV symbols).
                edge_left = a if isclose(left, a, abs_tol=1e-10, rel_tol=0) else left
                edge_right = b if isclose(right, b, abs_tol=1e-10, rel_tol=0) else right
                if edge_right <= a or edge_left >= b:
                    remaining.append((a, b))
                else:
                    if edge_left > a:
                        remaining.append((a, edge_left))
                    if edge_right < b:
                        remaining.append((edge_right, b))
            exposed = remaining
        for a, b in exposed:
            roofs.append({"id": f"r{len(roofs)}", "building_id": floor["building_id"],
                          "space_id": space["id"], "x_m": a,
                          "z_m": floor["z_m"] + floor["height_m"] + floor["slab_thickness_m"],
                          "width_m": b - a, "depth_m": floor["depth_m"],
                          "schematic_area_m2": (b - a) * floor["depth_m"]})
    return roofs


def _build_facades(spaces: list[dict], floors: list[dict]) -> list[dict]:
    """Expose the two section-end facades of every occupied floor."""
    facades = []
    for floor in floors:
        members = [s for s in spaces if s["floor_id"] == floor["id"]]
        if not members:
            continue
        left = min(s["x_m"] for s in members)
        right = max(s["x_m"] + s["width_m"] for s in members)
        for side, x in (("left", left), ("right", right)):
            facades.append({"id": f"{floor['id']}:{side}", "floor_id": floor["id"],
                            "building_id": floor["building_id"], "side": side,
                            "x_m": x, "z_m": floor["z_m"], "height_m": floor["height_m"],
                            "source_variable": "hull_transmittance_walls"})
    return facades


def _place_pv(area: float | None, roofs: list[dict]) -> dict:
    remaining = area
    placements = []
    if remaining is not None:
        for roof in roofs:
            placed = min(remaining, roof["schematic_area_m2"])
            if placed > 0:
                placements.append({"roof_id": roof["id"], "offset_m": 0.0,
                                   "width_m": placed / roof["depth_m"], "module_area_m2": placed, "tilt_deg": 15.0, "arrangement": "butterfly"})
                remaining -= placed
    return {"requested_area_m2": area, "unplaced_area_m2": remaining, "placements": placements}


def suggest_section_layout(scenario: Scenario, seed: int = 42, *, versioned: bool = False) -> dict:
    """Return an editable, JSON-compatible building specification for a scenario.

    Use the default heuristic's building allocations, widths and occupied floor
    counts. Explicit shares retain those allocations when generating the custom
    layout. Each usage becomes one continuous block, with office below residential;
    this is a starting proposal, not an exact copy of the heuristic geometry.
    If the heuristic leaves buildings empty, use equal spreading instead.
    """
    section = section_layout_from_scenario(scenario, seed=seed)
    if any(not b["floor_ids"] for b in section["buildings"]):
        section = section_layout_from_scenario(scenario, seed=seed, layout="equalspread")
    floor_by_id = {f["id"]: f for f in section["floors"]}
    totals = {}
    allocations = {b["id"]: {} for b in section["buildings"]}
    for space in sorted(section["spaces"], key=lambda s: (floor_by_id[s["floor_id"]]["index"], s["x_m"])):
        key, area = space["usage"], space["area_m2"]
        bid = floor_by_id[space["floor_id"]]["building_id"]
        allocations[bid][key] = allocations[bid].get(key, 0.0) + area
        totals[key] = totals.get(key, 0.0) + area
    buildings = []
    for index, building in enumerate(section["buildings"]):
        areas = allocations[building["id"]]
        order = sorted(areas, key=lambda key: {"office": 1, "residential": 2}.get(key, 0))
        buildings.append({
            "name": f"Building {index + 1}",
            "relative_length": building.get("width_m", 1.0),
            "depth_m": building["depth_m"],
            "max_basements": 0,
            "max_floors": len(building["floor_ids"]),
            "usages": order,
            "usage_shares": {key: area / totals[key] for key, area in areas.items()},
        })
    return {"gap_m": 20.0, "facade_style": "default", "buildings": buildings}


def section_layout_from_scenario(scenario: Scenario, seed: int = 42, *, layout: str | dict | None = None, gap_m: float = 20.0, reuse_geometry: dict | None = None) -> dict:
    """Project a Scenario into an area-preserving schematic section dictionary.

    Coordinates are metres, with z increasing upwards. Floor area is NFA and
    equals width times the building depth (15 m by default), not width times room height.
    Unknown distributions and defaults are recorded in ``assumptions``.
    The scenario and global random state are never modified.

    ``default`` assigns continuous blocks to the least occupied buildings,
    fills buffers with other then residential, and balances residential tops.
    ``separateResidential`` retains the earlier concentrated-special-use layout.
    ``equalspread`` divides usages equally and seeds intermediate usage order.
    A dict with a ``buildings`` list specifies bottom-to-top ``usages``,
    ``max_floors``, optional ``relative_length`` and ``usage_shares`` per building.
    Shared usages follow length times depth times floor capacity unless shares are explicit;
    total length is derived to fit the allocated areas within the floor limits.
    ``gap_m`` sets spacing for named layouts (default 20 m). Custom layouts may
    set ``gap_m`` and per-building ``gap_after_m``; the latter refers to the next building.
    ``facade_style`` can be set on a custom layout or individual building.
    ``layout_version=1`` accepts grouped defaults, geometry, allocation and systems.
    ``reuse_geometry`` accepts a previous section; incompatible geometry raises ValueError.
    All layouts preserve usage totals.
    """
    normalized = normalize_layout(layout) if isinstance(layout, dict) and "layout_version" in layout else None
    original_layout = deepcopy(layout)
    if normalized is not None:
        layout = allocation_layout(normalized)
    if layout is None:
        layout = "default"
    if not isinstance(layout, dict) and layout not in ("default", "equalspread", "separateResidential"):
        raise ValueError(f"Unknown section layout: {layout!r}")
    inputs = _read_inputs(scenario, custom_layout=isinstance(layout, dict))
    if isinstance(layout, dict):
        valid_usages = {meta.entity_key for meta, _ in scenario.select(
            domain="usage", measure="area", spatial_scope="NFA", entity_group="usage"
        ).items()}
        section = _allocate_custom(inputs, layout, valid_usages | {"unallocated"})
        systems = resolve_systems(scenario, layout, section["buildings"], valid_usages | {"unallocated"})
        if systems is not None:
            section["systems"] = systems
            _note(inputs["assumptions"], "system_overlays", "HVAC and roof systems are symbolic overlays: scenario hints are overridden by shared then per-building presentation settings. They do not change scenario inputs, areas, roof capacity or energy calculations.")
    elif layout == "default":
        section = _allocate_default(inputs)
    elif layout == "separateResidential":
        section = _allocate_separate_residential(inputs)
    else:
        _note(inputs["assumptions"], "usage_distribution", "Usages are divided equally among buildings: office below other uses, residential above; remaining uses share one seeded order.")
        if not float(inputs["storeys"]).is_integer():
            _note(inputs["assumptions"], "partial_top_floor", "Fractional average storeys are represented by partial upper floors.")
        section = _allocate_equalspread(inputs, seed)
    # One positioning pass keeps every allocation mode independent of inter-building gaps.
    settings = layout if isinstance(layout, dict) else {}
    shared_gap = _number(settings.get("gap_m", gap_m), "gap_m")
    if shared_gap is None or isinstance(settings.get("gap_m", gap_m), bool):
        raise ValueError("gap_m must be a finite nonnegative number")
    def facade_name(value):
        if value in ("gruenderzeit", "grunderzeit", "gründerzeit"):
            return "gründerzeit"
        if value == "default":
            return value
        raise ValueError("facade_style must be default or gründerzeit")
    shared_facade = facade_name(settings.get("facade_style", "default"))
    origin = 0.0
    section["gaps_m"] = []
    for i, building in enumerate(section["buildings"]):
        raw = settings.get("buildings", [{}] * len(section["buildings"]))[i]
        gap = _number(raw.get("gap_after_m", shared_gap), "gap_after_m")
        if gap is None or isinstance(raw.get("gap_after_m", shared_gap), bool):
            raise ValueError("gap_after_m must be a finite nonnegative number")
        building["facade_style"] = facade_name(raw.get("facade_style", shared_facade))
        members = [space for space in section["spaces"] + section.get("voids", []) if space["floor_id"] in building["floor_ids"]]
        previous = building.get("x_m", min((v["x_m"] for v in members), default=origin))
        for space in members:
            space["x_m"] += origin - previous
        building["x_m"] = origin
        building.setdefault("width_m", max((v["x_m"]+v["width_m"]-origin for v in members), default=0.0))
        building["gap_after_m"] = gap if i < len(section["buildings"])-1 else None
        if i < len(section["buildings"])-1:
            section["gaps_m"].append(gap)
        origin += building["width_m"] + gap
    if "layout_spec" in section:
        section["layout_spec"].update(gap_m=shared_gap, facade_style=shared_facade)
    _note(inputs["assumptions"], "building_gaps", "Gaps between schematic floor footprints [m]: " + str(section["gaps_m"]) + ". Facade relief has drawing thickness only.")
    building_by_id = {b["id"]: b for b in section["buildings"]}
    for index, building in enumerate(section["buildings"]):
        building.setdefault("depth_m", 15.0)
        building["street_side"] = "left" if index % 2 == 0 else "right"
        building["courtyard_side"] = "right" if index % 2 == 0 else "left"
    for floor in section["floors"]:
        floor["depth_m"] = building_by_id[floor["building_id"]]["depth_m"]
    # Keep legacy IDs intact, while adding stable semantic targets below.
    section["adjacency"] = _build_adjacency(section["spaces"], section["floors"])
    envelope = section["spaces"] + section.get("voids", [])
    section["roofs"] = _build_roofs(envelope, section["floors"])
    section["facades"] = _build_facades(envelope, section["floors"])
    floor_by_id = {f["id"]: f for f in section["floors"]}
    for facade in section["facades"]:
        ratio = inputs["context"]["section_glazing_ratio"] if floor_by_id[facade["floor_id"]]["index"] >= 0 else 0.0
        facade["exposure"] = "street" if facade["side"] == building_by_id[facade["building_id"]]["street_side"] else "courtyard"
        facade["glazing_ratio"] = ratio
        facade["window_height_m"] = facade["height_m"] * ratio
        facade["glazing_source"] = inputs["context"]["section_glazing_source"]
    section["pv"] = _place_pv(inputs["pv_area"], section["roofs"])
    _note(inputs["assumptions"], "roof_pv", "PV area placement uses flat schematic roof capacity with no setback; butterfly module symbols show 15 degree tilt. Tilt does not alter the schematic area budget or establish actual suitability.")
    if (section["pv"]["unplaced_area_m2"] or 0) > 0:
        _note(inputs["assumptions"], "pv_overflow", "Some PV module area does not fit on the schematic roofs.")
    depths = {b["depth_m"] for b in section["buildings"]}
    section.update(source={"column_name": scenario.column_name,
                           "project_name": scenario.project_name,
                           "scenario_name": scenario.name}, seed=seed, layout="custom" if isinstance(layout, dict) else layout,
                   depth_m=next(iter(depths)) if len(depths) == 1 else None,
                   context=inputs["context"], assumptions=inputs["assumptions"])
    finish_layout(section, normalized, inputs, original_layout, reuse_geometry, scenario)
    return section
