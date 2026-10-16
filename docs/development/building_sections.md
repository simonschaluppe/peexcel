# Schematic building sections

`pexl.spatial` projects a `pexl.Scenario` into an area-preserving section and renders
it as a static SVG. `Project`, `Scenario`, `scenario.v` and the generated schema
remain the authoritative scientific interfaces. A layout describes presentation
choices, not a second building or simulation model.

The executable guide is [Visualize your pexl project](../../notebooks/howto_visualize_project.ipynb).
It combines project import, a manually assembled project with all seven usages,
layout choices, styles, HVAC examples, real-project comparison and export. It replaces
the three earlier section/gallery/showcase notebooks. There is no notebook helper module.

## Public API

```python
from pexl.spatial import section_layout_from_scenario, render_svg

section = section_layout_from_scenario(scenario, seed=42)
svg = render_svg(section, style="architectural", annotations=True)
```

| Function | Purpose |
|---|---|
| `section_layout_from_scenario(scenario, seed=42, *, layout=None, gap_m=20, reuse_geometry=None)` | Allocate usage budgets and create floors, spaces, adjacency, façades, roofs and PV. |
| `render_svg(section, style="architectural", *, construction="default", facade_style=None, annotations=False, palette=None, usage_labels="auto")` | Return an SVG string without modifying the section or scenario. |
| `suggest_section_layout(scenario, seed=42, *, versioned=False)` | Return an editable suggestion; `versioned=True` selects the grouped specification. |
| `normalize_layout(layout)` | Validate and copy a compact or version-1 layout into the grouped form. |
| `preset_visuals(category=None)` | Return runnable teaching overlays for the recorded HVAC presets, with names, values, source ranges and assumptions. |

`section_from_scenario` remains an alias. Compact layout dictionaries and
`render_emission_details_svg` remain supported. The how-to uses the main renderer for
component illustrations. Generation and rendering use the standard library; no
Pygame, browser, image service or plotting dependency is required.

## Schema inputs and units

Usage variables and labels are selected through metadata (`domain="usage"`,
`measure="area"`, `spatial_scope="NFA"`, `entity_group="usage"`).

| Existing input | Interpretation |
|---|---|
| `NFA_office`, `NFA_residential`, `NFA_retailfood`, `NFA_retailother`, `NFA_schoolprim`, `NFA_schoolsec`, `NFA_other` | Usage budgets in m². Layout keys are schema entity keys such as `office`. |
| `NFA_total` | Total NFA in m²; derived from known usages when missing. |
| `building_count`, `storey_count_avg` | Heuristic building count and average storeys. Custom layouts supply their own count and limits. |
| `rh_avg`, `rh_ceiling` | Clear room height and slab thickness in metres. |
| `hull_fenestration_rate` | Explicit window fraction between 0 and 1. |
| `hull_window_m2`, `hull_ext_wall_wo_window_m2`, `hull_windows_horizontal_m2` | Fallback window fraction: vertical glazing / (vertical glazing + opaque wall). |
| `PV_is_used`, `PV_module_area`, `PV_kWp`, `PV_m2_per_kWp` | Enable flag and module-area budget. Explicit area wins; otherwise derive power × specific area. |
| `hull_roof_m2`, `PV_roof_area_percentage` | PV consistency checks; do not replace the NFA-based schematic footprint. |
| `hull_transmittance_walls`, `hull_transmittance_roof` | Source context, not physical layer thicknesses. |

`GFA_total`, `plot_area`, `FSI` and `hull_fundament_m2` are also retained as context.
Supported thermal-plant inference uses positive `QHmax_2th_m2` / `QHmax_4th_m2` with
`heat_th2_carrier_type` / `heat_th4_carrier_type`. Ventilation hints use
`vent_share_mechanical_<usage>`. A preset name, COP or unused equipment field alone
does not establish active plant or its location. Explicit overlays are illustrative
choices and do not activate scenario capacities.

Coordinates are metres, with `z_m` positive upwards. A space's NFA equals
`width_m * depth_m`, independent of room height. Invalid or contradictory areas fail
validation. Unknown usage within a known total is labelled `unallocated`, not silently
relabeled residential. Empty schematic capacity never creates additional NFA.

## Named layouts

- `default` favours continuous blocks, ground-floor retail and schools, office below
  residential, and residential tops. Schools and office favour the least occupied
  building. Available `other`, then residential budgets complete occupied floors.
  Office can use otherwise unassigned ground floors. Block continuity takes priority
  over identical heights.
- `separateResidential` retains concentrated special-use allocation, then offices
  in lower levels and residential in remaining capacity.
- `equalspread` divides usages among buildings. Office stays below residential;
  the seed controls intermediate usage order.

Default depth is 15 m and gap is 20 m. Missing building count, storeys, room height and
slab thickness use 1, 1, 3 m and 0.35 m respectively. Missing fenestration uses 30%
above ground. Defaults, unknowns and discrepancies are returned as
`{"code": ..., "description": ...}` in `section["assumptions"]`.

## Versioned layouts and comparison reuse

```python
layout = {
    "layout_version": 1,
    "site": {
        "gap_m": 20,
        "gaps": [{"between": ["A", "B"], "width_m": 25, "kind": "courtyard"}],
    },
    "defaults": {
        "geometry": {"depth_m": 15, "max_floors": 4, "max_basements": 1},
        "allocation": {
            "usages": ["office", "residential"],
            "basement_usages": ["other"],
        },
        "systems": {"usages": {"*": {"heating": "underfloor"}}},
    },
    "buildings": [
        {"id": "A", "name": "Building A", "geometry": {"relative_length": 2}},
        {"id": "B", "name": "Building B",
         "geometry": {"relative_length": 1, "depth_m": 20}},
    ],
}
section = section_layout_from_scenario(scenario, layout=layout)
```

Use schema usage keys present in the scenario. Every positive usage budget needs an
eligible building; impossible allocations raise `ValueError`.

| Category | Fields and rules |
|---|---|
| Identity | Persistent `id`, optional `name`. IDs start with a letter and use letters, digits, `-` or `_`. |
| `geometry` | Positive `relative_length`, `depth_m`, integer `max_floors`; nonnegative integer `max_basements`. |
| `allocation` | Bottom-to-top `usages`, ground-down `basement_usages`, optional `usage_shares` fractions per usage. |
| `envelope` | `facade.style`, or `street.facade.style` / `courtyard.facade.style`: `default` or `gründerzeit` (ASCII aliases accepted). |
| `circulation` | `kind`: `elevator`, `stairs`, `none`; optional positive `shaft_width_m` smaller than the building. |
| `systems` | Usage terminals, local plant and roof options. |
| Building `site` | `street_side`: `left` or `right`; positional `gap_after_m`. Street sides alternate by default. |
| Root `site` | Default `gap_m`; pair-addressed `gaps` with `between`, `width_m`, optional `kind` (`street` or `courtyard`). Pairs must remain adjacent. |

Defaults merge into building values. Nested mappings merge; lists replace. Missing
inherits; `[]` clears a list. Within each systems scope, `*` resolves before a named
usage. Root plant is separate from per-building defaults.

Shared usages follow relative length × depth × eligible floor capacity unless explicit
shares allocate some of the budget. Remaining shares follow capacity. Lengths are
derived together to preserve ratios and floor limits. Maximum floors are limits,
not a promise to fill every level; a partial top floor preserves area.

Basements fill from level -1 down. Default eligible uses are retail, schools, then
`other`; office and residential require explicit basement entries. Unfilled underground
space is schematic parking, excluded from NFA. `max_basements` controls the count.

Both horizontal axes restart per building. Length uses one continuous scale; floor
area per storey depends on depth: 15 m length gives 225 m² at 15 m depth or 300 m²
at 20 m depth. Horizontal and vertical drawing scales are independent.

```python
scenario.v.PV_kWp = 180
scenario.v.PV_module_area = None
updated = section_layout_from_scenario(
    scenario, layout=layout, reuse_geometry=section,
)
```

`reuse_geometry` validates actual allocation before reusing detached geometry.
Changed area, depth or allocation raises an error. A seed alone is not a stable
comparison contract. JSON round trips preserve normalized settings.

## Styles and annotations

| Option | Behaviour |
|---|---|
| `style="architectural"` | Pastel usages, site silhouettes, construction and lilac insulation. |
| `style="hand_drawn"` | Marker strokes, irregular fine frames/axes, warm paper, rectangular yellow building notes. Solid ceiling bands are hidden. |
| `style="blueprint"` | Light drafting grid and limited colour family. |
| `style="teaching"` | Neutral spaces, facade, roof, slabs and windows; same geometry/IDs, without environment, equipment, usage labels or decorative interior elements. `annotations=True` is rejected. Explicit lesson overlays live outside the renderer. |
| `palette="blue"`, `"green"`, `"beige"` | Blueprint palette; `None` means blue. Explicit palettes on other styles raise an error. |
| `annotations=True` | Numbered callouts refer to actual components in the same section, using the selected font, colours and line treatment. |
| `usage_labels="auto"` | Schema labels inside spaces where they fit. Narrow fragments retain the legend/title. `"none"` hides internal labels. |
| `construction="wood"` | Light-brown schematic construction; Blueprint translates it to its palette. |
| `facade_style="gründerzeit"` | Global relief override; omit to use per-building/per-side settings. |

`style="annotations"` remains an alias for Blueprint with annotations. All styles have
subtle paper, sky and soil gradients. Functional HVAC colours remain distinct.
Hand-drawn typography uses locally available Ink Free / Segoe Print / Bradley Hand /
cursive fallbacks, so font appearance can vary between computers.

Slabs finish flush with construction; insulation continues outside. Thicknesses are
drawing widths, not a material take-off. Partitions and shafts overlay usages without
subtracting area. Streets, curbs, underground services, front-view cars and vegetation
are schematic context. PV is raised above the roof in 15° butterfly pairs; the budget
uses flat schematic roof capacity.

Legends separate usage, materials and HVAC. Plant and roof legends reuse their drawn
symbols. Annotation margins expand the canvas without moving buildings or semantic IDs.

## HVAC, shared plant and roof uses

```python
systems = {
    "usages": {
        "*": {"heating": "underfloor", "ventilation": "balanced_recovery"},
        "office": {"heating": "tabs", "cooling": "ceiling_panel"},
        "residential": {"dhw": "electric_local"},
    },
    "plant": [{"kind": "heat_pump", "source": "groundwater"}],
    "roof": ["pv", "garden", "pergola", "terrace"],
}
```

Set these in `defaults.systems` or a building's `systems`.

| Field | Choices |
|---|---|
| Usage `heating` / `cooling` | `none`, `tabs`, `underfloor`, `radiator`, `lt_radiator`, `ceiling_panel`, `split`, `fan_coil` |
| Usage `ventilation` | `none`, `natural`, `exhaust`, `exhaust_recovery`, `balanced`, `balanced_recovery`; legacy `mechanical`, `heat_recovery` remain supported. |
| Usage `dhw` | `none`, `central`, `gas_local`, `electric_local`, `heat_pump_local` |
| Plant `kind` | `heating_room`, `water_well`, `boreholes`, `district_heating`, `district_cooling`, `gas_boiler`, `oil_boiler`, `biomass_boiler`, `heat_pump`, `chiller`, `passive_exchanger`, `air_handler`, `outdoor_unit`, `hot_water_tank`, `dhw_heat_pump`, `gas_water_heater`, `electric_water_heater` |
| Plant `source` | `unknown`, `groundwater`, `ground`, `air`; for heat pumps, DHW heat pumps and passive exchangers. Ground illustrates a generic horizontal source, not confirmed boreholes. |
| Plant `mode` | `heating` (default), `cooling`, `reversible` |
| Plant `services` | List of `heating`, `cooling`, `dhw`; DHW adds a schematic distribution branch. |
| `roof` | `pv`, `solar_thermal`, `pergola`, `terrace`, `garden`, `hvac_room` |

Local plant receives an ID, host and `level="lowest_floor"` by default. A partial local
location such as `{"level": "roof"}` inherits the host. Defaults create one local
instance per building. For shared equipment use one root record:

```python
layout["systems"] = {"plant": [{
    "id": "central-hp", "kind": "heat_pump", "source": "groundwater",
    "location": {"building": "A", "level": "lowest_floor"},
    "serves": ["A", "B"],
}]}
```

Levels are integer indices (ground = 0, basements negative), `"roof"` or
`"lowest_floor"`. Unknown root locations remain unplaced and reported. Host references,
served buildings, IDs and existing levels are validated. Shared plant is drawn once.

TABS sits inside concrete, underfloor pipes above it, panels below the ceiling, air
ducts beneath the ceiling and split units beside windows. Exhaust-only recovery does
not create balanced ventilation. Plant cutaways show flues, compressors, exchangers,
fans, storage coils and flow arrows. Small spaces may omit illegible symbols. These
are teaching topologies, not sized hydraulic designs.

Roof modules sit on their roof and reserve drawing room around PV and the shaft
continuation. They do not jointly optimise roof occupancy or determine plant capacity.

## Preset catalogue and real project

```python
from pexl.spatial import preset_visuals

case = next(row for row in preset_visuals("Ventilation")
            if row["name"] == "ABL-Anlage mit WRG")
layout["buildings"][0]["systems"] = case["systems"]
section = section_layout_from_scenario(scenario, layout=layout)
svg = render_svg(section, style="hand_drawn", annotations=True)
```

The packaged [snapshot](../../src/pexl/spatial/data/hvac_presets.json) retains 40 entries:
7 heating, 17 cooling, 5 emission, 4 ventilation, 7 hot water. Recipes match exact category
and name, never row order. Each detached row includes `values`, `source`,
`catalog_source`, `catalog_sha256`, `systems` and `notes`. This is recorded example
provenance, not another scientific schema or live workbook synchronisation.

Recipes do not apply physical presets to scenarios. Unknown sources and unspecified
terminals remain unresolved. Hybrid cooling retains passive and compressor components;
central DHW illustrates a generator, tank and distribution, while local DHW illustrates
local appliances. All 40 entries run through the production renderer in tests and in
the notebook's technical checks.

The real example imports `data/exports/ka_project_backup_v1_13.xlsx` and compares two
Forsthausgasse variants with a 2:1 layout. This local asset may need to be supplied in
a fresh checkout or replaced with another export. Dummy-project examples need no
workbook. Stored values are inspected: the variant titled `WP` still has active
district heating in this export, so its name is not used to draw an unverified heat pump.

## Resolved data and scientific scope

The result contains `buildings`, `floors`, `spaces`, `voids`, `adjacency`,
`facades`, `roofs`, `pv`, `assumptions`, source context and optional equipment/systems.
PV reports requested, placed and unplaced area. `layout_spec` and `normalized_layout`
retain versioned choices; `geometry_signature` protects reuse.

Stable semantic IDs identify buildings, floors, usage spaces, surfaces and equipment.
SVG `data-semantic-id` attributes preserve those targets across styles. They enable
selection, not independent physical simulation of a schematic surface. Never weight
aggregate U-values using invented section lengths. Browser interaction, renovation
measures, gameplay and simulation revisions belong to consumers such as Draft Zero.

## Implementation and checks

| Module | Responsibility |
|---|---|
| `section_layout.py` | Schema inputs, allocation, adjacency, envelope and PV budgets. |
| `layout_spec.py` | Typed dictionary hints, validation and compatibility normalization. |
| `resolved_layout.py` | Semantic IDs, provenance, equipment and geometry reuse. |
| `system_resolution.py` | Scenario hints, allowed component names and precedence. |
| `svg.py` | Main composition, envelope, axes, legends and circulation. |
| `themes.py`, `annotations.py` | Style tokens/gradients, usage labels and callouts. |
| `systems.py`, `usage_symbols.py` | Room terminals, ventilation, DHW and roof scenes. |
| `component_symbols.py`, `equipment_svg.py` | Plant/source primitives, placement and service references. |
| `site_svg.py` | Streets, courtyards and front-view cars. |
| `presets.py`, `data/hvac_presets.json` | Named examples and source provenance. |

Drawing helpers take coordinates and callbacks; geometry has no rendering dependency.
Functions document units and assumptions. Existing public compatibility entry points remain.

With `src` on `PYTHONPATH`, run:

```text
python -m pytest tests/test_section.py tests/test_section_svg.py tests/test_spatial_presets.py tests/test_spatial_styles.py
```

Checks cover area conservation, determinism, mutation, allocation limits, partial
floors, basements, JSON normalization, geometry reuse, semantic IDs, SVG validity,
layer placement, style-independent geometry, palettes and all preset recipes.
Execute the how-to in a fresh kernel to refresh its output. Inspect exported SVGs
visually as well: XML validity alone does not establish legibility.
