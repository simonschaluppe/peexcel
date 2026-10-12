# Section layout: proposed next refactor

Status: initial design record; version 1 normalization, semantic targets and comparison reuse are now implemented. See [current API](building_sections.md#versioned-layouts-and-comparison-reuse). The initial sketch below is retained as design history; pair-addressed gaps use `between`, not `after`. `Project`, `Scenario`,
`scenario.v` and schema metadata remain authoritative. The layout describes a
schematic projection and explicit presentation choices, not another building model.

## Why consolidate now

The current dictionaries work, but geometry, allocation, equipment selection and
automatic decoration are becoming mixed. The renderer also chooses street sides,
trees, parking decoration and lift/stair circulation implicitly. These choices
should be visible in the normalized layout before more symbols are added.

Keep JSON-compatible dictionaries. Add `TypedDict` and `Literal` annotations for
editor support, explicit validation for runtime errors, and one versioned
normalization function. No generic domain framework, inheritance tree, Pydantic
dependency or duplicate schema-variable catalogue is needed.

## Suggested structure

```python
{
    "layout_version": 1,
    "site": {
        "gap_m": 20,
        "gaps": [{"after": "A", "width_m": 12, "kind": "courtyard"}],
    },
    "defaults": {
        "envelope": {"facade": {"style": "gründerzeit"}},
        "systems": {"usages": {"*": {"heating": "underfloor"}}},
    },
    "buildings": [
        {
            "id": "A", "name": "Street building",
            "geometry": {"relative_length": 2, "depth_m": 15, "max_floors": 4,
                         "max_basements": 1},
            "allocation": {"usages": ["office", "residential"],
                           "basement_usages": ["other"]},
            "envelope": {"street": {"facade": {"style": "gründerzeit"}},
                         "courtyard": {"facade": {"style": "default"}}},
            "circulation": {"kind": "elevator", "shaft_width_m": 2},
            "systems": {"plant": [{"kind": "district_heating",
                                   "location": "lowest_floor"}]},
        },
    ],
}
```

Stable building IDs let gaps and future shared plant connections survive list
reordering. IDs need not match an external asset model. Geometry and allocation
remain ordinary functions and dictionaries.

Keep graphic style (`architectural`, `hand_drawn`, `blueprint`) on `render_svg`.
Façade typology, circulation and equipment placement belong to the layout because
they describe what is drawn. Colours, line weights and silhouette templates belong
to the renderer. A historic façade does not select a wall U-value or insulation.

## Categories justified by PEexcel inputs

| Category | Existing evidence | Next visual options / boundary |
|---|---|---|
| Geometry and usage | `building_count`, `storey_count_avg`, `NFA_<usage>`, `rh_<usage>` | Existing allocation, depths, basements and gaps; geometry overrides stay explicit. |
| Envelope | `hull_fenestration_rate`, `hull_window_m2`, `hull_ext_wall_wo_window_m2`, directional window areas | Window openings, façade typology, shading and roof form; no façade orientation inferred from a section side. |
| Heat generation | `QHmax_1el_m2`, `QHmax_2th_m2`, `heat_cop_1el`, `heat_th2_carrier_type` and other slots | Active generators, source assemblies, cascades, shared versus building-local plant. Capacity gates presence; COP alone does not select source. |
| Emission | `preset_recorded_heating_emission_system`, `QHmax_room_m2`, `QCmax_room_m2` | TABS, underfloor, radiators, suspended panels and fan coils; room capacities alone do not identify equipment. |
| Cooling | `cool_share_<usage>`, `QCmax_freecooling`, `QCmax_1el`, `QCmax_2th`, `cool_th2_carrier_type` | Chillers, district cooling, passive bypass and reversible plant; preserve hybrid paths. |
| Ventilation | `vent_share_mechanical_<usage>`, `vent_heat_recovery_winter_<usage>`, `vent_night_<usage>` | Exhaust versus balanced topology, recovery, window opening and night operation. |
| Domestic hot water | `DHW_carriertype_1`, `DHW_storage_1_liter`, `DHW_1_share_<usage>` and system 2 fields | Central/decentral heaters, tanks, draw-offs and circulation; do not duplicate shared generators. |
| Sources and roof | `borehole_count`, `PV_module_area`, `PV_kWp`, `PV_is_used` | Groundwater/ground/air sources and PV; solar thermal, garden, terrace and pergola currently require explicit layout choices. |
| Storage, flexibility and mobility | Schema groups for battery, flexibility and mobility, resolved from metadata | Battery cabinet, thermal buffer, charging and parking after checking active quantities and placement. Preset names alone do not imply hardware. |
| Site and circulation | Usually absent from scenario inputs | Street/courtyard, planting, curb utilities, lifts and stairs should be configurable schematic assumptions. |

## Component records and provenance

Retain the existing string shorthand, for example `"garden"` or `"gas_boiler"`.
Normalize to a small record only when additional placement is needed:

```python
{"kind": "heat_pump", "source": "groundwater", "location": "lowest_floor"}
```

Avoid a free-form attributes bag: validate allowed fields for each component kind.
Use `"unknown"` for unresolved sources; reject unknown kind names. Keep evidence in
the generated result, alongside the selected component: source variable names,
input values and whether the choice was explicit, inferred or assumed. These are
references to the scenario, not a second set of editable energy inputs.

Shared defaults merge per field. Usage-specific settings override `*`. Building
overrides win. Lists replace; empty lists clear. Missing means inherit, not zero.
Document these rules once and test them at the normalizer boundary.

## Small implementation steps

1. Add `layout_spec.py` for type hints, validation, normalization and compatibility.
   Accept today's flat keys (`gap_m`, `gap_after_m`, `facade_style`, `depth_m`, etc.)
   and the proposed format; reject conflicting old/new representations.
2. Keep allocation in `section_layout.py`. Materialize side assignments, gaps,
   circulation and resolved appearance in the generated section.
3. Split SVG work by purpose: envelope/site details and equipment symbols. Share
   symbol functions between the section and legend rather than copying SVG nodes.
4. Separate system inference from drawing. Add the reviewed preset mappings only
   after active-capacity gates and ambiguity rules are agreed.
5. Keep existing imports, calls and result keys compatible; add migration examples
   before deprecating any shorthand. Round-trip layout JSON in tests.

Before implementation, approve the versioned grouping and placement vocabulary,
and decide how shared central plant should be assigned to buildings. New categories
can then be added without expanding one unstructured renderer or changing the
authoritative scenario interfaces.

## Worked design review

[Three worked examples](section_layout_refactor_examples.md) exercise a simple
residential building, the real Forsthausgasse showcase, and mixed uses with shared
plant. They refine this initial sketch: support geometry/allocation defaults,
normalize shared plant into root records with host and served-building references,
retain unknown locations, and address explicit site gaps by both endpoint IDs.
These are proposed refinements, not implemented input fields.

## Draft Zero boundary

The [project memo](draft_zero_project_memo.md) is the game concept reference.
The [game-focused walkthrough](section_layout_refactor_examples.md#4-draft-zero-inspect-configure-simulate-diagnose-revise-submit)
adds stable semantic target IDs, resolved-geometry reuse and scientific edit scope
to the proposed acceptance criteria. Game plans, measure catalogues, undo/redo,
progression and scoring remain in Draft Zero. Local graphical selection must not
imply finer scientific resolution than the authoritative scenario supports.
