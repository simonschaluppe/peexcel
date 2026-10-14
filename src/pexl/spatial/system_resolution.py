"""Scenario hints and legacy overlay resolution, independent of SVG drawing."""

from __future__ import annotations
from copy import deepcopy
from math import isfinite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pexl.model.scenario import Scenario
EMITTERS = {"none", "tabs", "underfloor", "radiator", "split", "fan_coil"}
VENTILATION = {"none", "natural", "mechanical", "heat_recovery"}
PLANT = {
    "heating_room",
    "water_well",
    "boreholes",
    "district_heating",
    "gas_boiler",
    "oil_boiler",
    "biomass_boiler",
}
ROOF = {"pv", "solar_thermal", "pergola", "terrace", "garden", "hvac_room"}


def _merge(base: dict, override: dict) -> dict:
    """Merge nested presentation settings without modifying either input."""
    result = deepcopy(base)
    for key, value in override.items():
        result[key] = (
            _merge(result.get(key, {}), value)
            if isinstance(value, dict)
            else deepcopy(value)
        )
    return result


def _validate(settings: dict, usages: set[str]) -> None:
    """Validate component names and schema-backed usage keys."""
    if not isinstance(settings, dict) or set(settings) - {"usages", "plant", "roof"}:
        raise ValueError(
            "systems accepts only usages, plant and roof dictionaries/lists"
        )
    for field, choices in (("plant", PLANT), ("roof", ROOF)):
        if field in settings:
            values = settings[field]
            if (
                not isinstance(values, list)
                or any(not isinstance(v, str) or v not in choices for v in values)
                or len(values) != len(set(values))
            ):
                raise ValueError(
                    f"systems.{field} must be a list of unique supported symbols"
                )
    usage_settings = settings.get("usages", {})
    if not isinstance(usage_settings, dict) or set(usage_settings) - (usages | {"*"}):
        raise ValueError("systems.usages keys must be schema usage keys or '*'")
    for usage, values in usage_settings.items():
        if not isinstance(values, dict) or set(values) - {
            "heating",
            "cooling",
            "ventilation",
        }:
            raise ValueError(f"Invalid system fields for {usage}")
        for key, value in values.items():
            if not isinstance(value, str) or value not in (
                VENTILATION if key == "ventilation" else EMITTERS
            ):
                raise ValueError(f"Unsupported {key} system: {value!r}")


def resolve_systems(
    scenario: Scenario, layout: dict, buildings: list[dict], usage_keys: set[str]
) -> dict | None:
    """Apply scenario hints, shared defaults, then per-building overrides."""
    if "systems" not in layout and not any("systems" in b for b in layout["buildings"]):
        return None
    shared = layout.get("systems", {})
    _validate(shared, usage_keys)
    sources = {}

    def positive(name):
        value = getattr(scenario.v, name, None)
        try:
            number = float(value)
        except (TypeError, ValueError):
            return False
        if isfinite(number) and number > 0:
            sources[name] = number
            return True
        return False

    inferred = {"usages": {}, "plant": [], "roof": ["pv"]}
    for usage in sorted(usage_keys - {"unallocated"}):
        if positive(f"vent_share_mechanical_{usage}"):
            inferred["usages"][usage] = {"ventilation": "mechanical"}
    if positive("borehole_count"):
        inferred["plant"].append("boreholes")
    if any(positive(name) for name in ("heat_th2_is_dh", "heat_th4_is_dh")):
        inferred["plant"].append("district_heating")
    resolved = {}
    for building, raw in zip(buildings, layout["buildings"]):
        override = raw.get("systems", {})
        _validate(override, usage_keys)
        # Wildcards apply within each scope, then usage-specific settings win.
        settings = _merge(
            _merge(inferred, {k: v for k, v in shared.items() if k != "usages"}),
            {k: v for k, v in override.items() if k != "usages"},
        )
        settings["usages"] = {}
        for usage in sorted(usage_keys):
            values = {"heating": "none", "cooling": "none", "ventilation": "none"}
            values.update(inferred["usages"].get(usage, {}))
            for scope in (shared, override):
                mapping = scope.get("usages", {})
                values.update(mapping.get("*", {}))
                values.update(mapping.get(usage, {}))
            settings["usages"][usage] = values
        resolved[building["id"]] = settings
    return {
        "buildings": resolved,
        "source_values": sources,
        "defaults": deepcopy(shared),
    }


def inferred_plant(scenario: Scenario) -> list[dict]:
    """Scenario-wide evidence only: never invent a building location or heat source."""
    records = []
    for slot, suffix in ((1, "el"), (2, "th"), (3, "el"), (4, "th")):
        capacity_name = f"QHmax_{slot}{suffix}_m2"
        value = getattr(scenario.v, capacity_name, None)
        try:
            active = isfinite(float(value)) and float(value) > 0
        except (ValueError, TypeError):
            active = False
        if not active:
            continue
        evidence = {capacity_name: float(value)}
        if suffix == "el":
            # Active electric capacity alone does not distinguish resistance and HP.
            continue
        carrier_name = f"heat_th{slot}_carrier_type"
        carrier = getattr(scenario.v, carrier_name, None)
        evidence[carrier_name] = carrier
        kind = (
            "district_heating"
            if "Fernw" in str(carrier)
            else (
                "gas_boiler"
                if carrier == "Erdgas"
                else "biomass_boiler" if "Biomasse" in str(carrier) else None
            )
        )
        if kind:
            records.append(
                {
                    "id": f"inferred-heat-{slot}",
                    "kind": kind,
                    "serves": [],
                    "provenance": {
                        "origin": "inferred",
                        "source_values": evidence,
                        "scope": "scenario",
                    },
                }
            )
    return records
