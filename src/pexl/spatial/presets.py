"""Explicit teaching overlays for the recorded PEExcel HVAC preset catalogue.

The catalogue preserves source names, cached values and workbook provenance.
These functions return detached visual settings only. They neither apply presets
to scenarios nor infer installed equipment from names. Assumed source locations
and unspecified terminals remain explicit in each example's notes.
"""

from copy import deepcopy
from importlib.resources import files
import json


def _plant(kind: str, **options) -> dict:
    """Create a local plant recipe; the normalizer supplies its host and ID."""
    return {"kind": kind, **options}


def _recipe(category: str, name: str) -> tuple[dict, str]:
    """Map exact category/name pairs, never workbook row order, to drawings."""
    settings = {"usages": {"*": {}}, "plant": [], "roof": []}
    usage = settings["usages"]["*"]
    notes = "Placement is a teaching assumption. Capacities remain scenario inputs."
    if category == "Emission":
        mode, emitter = {
            "Bauteilaktivierung": ("heating", "tabs"),
            "Fußbodenheizung": ("heating", "underfloor"),
            "Hochtemperatur-Heizkörper": ("heating", "radiator"),
            "Kühlpaneele": ("cooling", "ceiling_panel"),
            "NT-WP-Heizkörper": ("heating", "lt_radiator"),
        }[name]
        usage[mode] = emitter
        notes += " Emitter selection does not identify its generator."
    elif category == "Ventilation":
        usage["ventilation"] = {
            "ABL-Anlage": "exhaust",
            "ABL-Anlage mit WRG": "exhaust_recovery",
            "Mech. Lüftung mit WRG": "balanced_recovery",
            "Mech. Lüftung ohne WRG": "balanced",
        }[name]
    elif category == "Heating":
        if name in {"Biomasse", "Erdgas", "Fernwärme Wien"}:
            settings["plant"] = [
                _plant(
                    {
                        "Biomasse": "biomass_boiler",
                        "Erdgas": "gas_boiler",
                        "Fernwärme Wien": "district_heating",
                    }[name]
                )
            ]
        elif name == "Klimasplitgerät":
            usage["heating"] = "split"
            settings["plant"] = [_plant("outdoor_unit", location={"level": "roof"})]
        else:
            source = {
                "Wärmepumpe (Erdwärme)": "ground",
                "Wärmepumpe (Grundwasser)": "groundwater",
                "Wärmepumpe (Luft-Wasser)": "air",
            }[name]
            settings["plant"] = [_plant("heat_pump", source=source)]
            notes += (
                " Ground means a generic horizontal source, not verified boreholes."
            )
    elif category == "Cooling":
        if name == "Keine Kühlung":
            usage["cooling"] = "none"
        elif name == "Fensterlüftung":
            usage["ventilation"] = "natural"
        elif name in {"Fernkälte", "Fernkälte Wien"}:
            settings["plant"] = [_plant("district_cooling", mode="cooling")]
        elif name in {"KKM zentral", "Kompressionskältemaschine zentral"}:
            settings["plant"] = [_plant("chiller", mode="cooling")]
        elif name == "Klimaanlage (Luft-Luft)":
            settings["plant"] = [_plant("air_handler", mode="cooling")]
            usage["ventilation"] = "balanced"
        elif name in {
            "Mono-/Mulit-Splitgerät, Einzelraum",
            "Klimasplitgerät",
            "Freecooling + Klimasplit",
        }:
            usage["cooling"] = "split"
            settings["plant"] = [
                _plant("outdoor_unit", mode="cooling", location={"level": "roof"})
            ]
            if name == "Freecooling + Klimasplit":
                settings["plant"].append(_plant("passive_exchanger", source="unknown"))
                notes += " The passive source is unresolved; it is not assumed to be window ventilation."
        elif name == "Freecooling":
            settings["plant"] = [_plant("passive_exchanger", source="unknown")]
            notes += " Passive source unresolved."
        else:
            source, passive = {
                "Wärmepumpe mit Grundwasser oder Erdwärme": ("unknown", False),
                "WP reversibel - FreeCooling Anteil": ("unknown", True),
                "WP reversibel": ("unknown", False),
                "Wärmepumpe (Erdwärme)": ("ground", False),
                "Geothermie Freecooling": ("ground", True),
                "Wärmepumpe (Grundwasser)": ("groundwater", False),
            }[name]
            settings["plant"] = [_plant("heat_pump", source=source, mode="reversible")]
            if passive:
                settings["plant"].append(_plant("passive_exchanger", mode="cooling"))
                notes += " Both compressor and passive paths are shown; no performance split is inferred."
            if source == "unknown":
                notes += " Heat-pump source unresolved."
        notes += " Unspecified room terminals are left unspecified."
    elif category == "Hot water":
        local = {
            "Gas dezentral": "gas_local",
            "Direkt Elektrisch": "electric_local",
            "Wärmepumpe dezentral": "heat_pump_local",
        }
        if name in local:
            usage["dhw"] = local[name]
            notes += " Local appliance count is illustrative, not inferred from NFA."
        else:
            kind = {
                "Gas Zentral": "gas_boiler",
                "Fernwärme": "district_heating",
                "zentrale WP": "dhw_heat_pump",
                "Biomasse": "biomass_boiler",
            }[name]
            usage["dhw"] = "central"
            settings["plant"] = [
                _plant(kind, services=["dhw"]),
                _plant("hot_water_tank"),
            ]
            notes += " Tank and circulation topology are explicit teaching choices."
    else:
        raise ValueError(f"Unsupported preset category {category!r}")
    return settings, notes


def preset_visuals(category: str | None = None) -> list[dict]:
    """Return all matching catalogue rows with executable visual recipes.

    Parameters
    ----------
    category : str or None
        Heating, Cooling, Emission, Ventilation or Hot water; None returns all 40.

    Returns
    -------
    list of dict
        Each row contains the original name, source range and cached values,
        plus ``systems`` for a building's versioned layout and ``notes``.
        The normalizer binds local plant locations to that building's ID.
        Returned recipes do not modify scenario values or run calculations.
    """
    catalog = json.loads(
        files("pexl.spatial")
        .joinpath("data/hvac_presets.json")
        .read_text(encoding="utf-8")
    )
    categories = {row["category"] for row in catalog["presets"]}
    if category is not None and category not in categories:
        raise ValueError(
            f"Unknown category {category!r}; choose from {sorted(categories)}"
        )
    result = []
    for row in catalog["presets"]:
        if category is not None and row["category"] != category:
            continue
        try:
            settings, notes = _recipe(row["category"], row["name"])
        except KeyError as exc:
            raise ValueError(
                f"Review the visual recipe for {row['category']}: {row['name']}"
            ) from exc
        result.append(
            {
                **deepcopy(row),
                "systems": settings,
                "notes": notes,
                "catalog_source": catalog["source_workbook"],
                "catalog_sha256": catalog["sha256"],
            }
        )
    return result
