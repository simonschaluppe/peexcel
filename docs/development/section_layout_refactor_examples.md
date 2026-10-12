# Testing the proposed layout format against three examples

Status: design walkthrough for the now-supported version 1 input. The dictionaries are accepted by `section_layout_from_scenario` when the scenario supplies the stated usage budgets. See the current API documentation for implementation boundaries. No scenario inputs are changed.

This supplements [the refactor proposal](section_layout_refactor_proposal.md).
The first and third cases are synthetic teaching examples. The second uses the
source facts inspected in `howto_section_real_project.ipynb`.

## 1. One residential building: keep the common case short

Assume a scenario with 900 m² residential NFA and three above-ground storeys.
The user knows the depth and wants to illustrate underfloor heating. No plant type
or basement is known.

```json
{
  "layout_version": 1,
  "defaults": {
    "systems": {
      "usages": {"residential": {"heating": "underfloor"}}
    }
  },
  "buildings": [
    {
      "id": "A",
      "geometry": {"depth_m": 10, "max_floors": 3},
      "allocation": {"usages": ["residential"]}
    }
  ]
}
```

Expected result: a 30 m long footprint, three 300 m² floors, no basement, and
underfloor pipes. Omitted relative length normalizes to 1. The emission choice is
explicit; plant type remains unknown. The scenario still supplies glazing and room
height. A missing glazing ratio is an assumption reported in the generated result.
No plant symbol should be invented to make the drawing look complete.

**Finding:** do not require every category or a component registry for a simple
building. Preserve strings for emitters. Empty category dictionaries add no value.
Keep `suggest_section_layout(scenario)` as the convenience starting point; once
implemented, its proposed versioned result should be directly editable.

## 2. Forsthausgasse: preserve evidence and expose geometric overrides

The existing showcase reads `data/exports/ka_project_backup_v1_13.xlsx` through
`Project.from_excel` and compares:

- `Forsthausgasse | BT2 KON FW`
- `Forsthausgasse | BT2 ÖKO WP FLEX 2,6xPV`

The notebook reports approximately 5,510 m² residential NFA in both, PV module
areas of 0 and 185 m², and PV capacities of 0 and 37 kWp. Both have an active
thermal district-heating slot and zero capacity in the first electric heating
slot. The WP title does not establish an active heat pump. Building count is 70
in the export; the requested drawing deliberately uses two buildings with a 2:1
length ratio. Depth 15 m and a four-floor limit are schematic choices.

```json
{
  "layout_version": 1,
  "site": {"gap_m": 20},
  "defaults": {
    "geometry": {"depth_m": 15, "max_floors": 4},
    "allocation": {"usages": ["residential"]},
    "systems": {"roof": ["pv"]}
  },
  "buildings": [
    {"id": "A", "name": "Building 1", "geometry": {"relative_length": 2}},
    {"id": "B", "name": "Building 2", "geometry": {"relative_length": 1}}
  ]
}
```

Expected geometry, if both footprints use their four-floor capacity: approximately
61.223 m and 30.611 m long, with about 3,673.365 and 1,836.683 m² NFA. Equal depth
and floor limits make a 2:1 length ratio also a 2:1 area ratio. With different
depths or capacities, this equality would no longer hold. Each building gets its
own length origin and area scale; the gap is a separate site dimension.

The roof choice requests PV placement; it does not create additional PV area.
The baseline therefore draws no panels. The second variant places up to the
scenario's 185 m² once across eligible roofs and reports any unplaced area.
A shared default must not duplicate the entire scenario PV budget per building.

For this case, leave plant out of the input layout. Proposed inference should
report district heating as known at scenario level, with physical location and
building connections unknown. It can appear in an explicitly labelled unlocated
system annotation, but must not become two asserted plant rooms. Ventilation
follows each variant's values; heating emitters remain unspecified.

**Findings:**

- Defaults need to support geometry and allocation as well as systems/envelope.
- Distinguish unknown location from an explicit shared plant assignment.
- Report the override `building_count: 70 -> 2` without changing the scenario.
- Report missing emission and source information rather than deriving it from a name.
- Inferred components belong in the generated result, not in editable duplicated
  copies of the scenario's capacities and areas.

## 3. Mixed uses and shared plant: references only where needed

Synthetic scenario area budget: 600 m² retail food, 900 m² primary school,
900 m² office, 3,600 m² residential. Total 6,000 m². Assume an active heat pump
in the scenario; its groundwater source and physical position are explicit
illustrative choices, not facts inferred from COP.

```json
{
  "layout_version": 1,
  "site": {
    "gap_m": 20,
    "gaps": [{"between": ["A", "B"], "width_m": 12, "kind": "courtyard"}]
  },
  "defaults": {
    "geometry": {"depth_m": 15, "max_floors": 4},
    "systems": {
      "usages": {"*": {"heating": "underfloor"}}
    }
  },
  "systems": {
    "plant": [
      {
        "id": "HP1",
        "kind": "heat_pump",
        "source": "groundwater",
        "location": {"building": "A", "level": -1},
        "serves": ["A", "B", "C"]
      }
    ]
  },
  "buildings": [
    {
      "id": "A",
      "geometry": {"relative_length": 2, "max_basements": 1},
      "allocation": {
        "usages": ["retailfood", "residential"],
        "usage_shares": {"residential": 0.5},
        "basement_usages": []
      },
      "envelope": {"facade": {"style": "gründerzeit"}},
      "circulation": {"kind": "elevator", "shaft_width_m": 2}
    },
    {
      "id": "B",
      "geometry": {"relative_length": 1},
      "allocation": {
        "usages": ["schoolprim", "residential"],
        "usage_shares": {"residential": 0.25}
      },
      "circulation": {"kind": "stairs"},
      "systems": {
        "usages": {"schoolprim": {"heating": "tabs", "ventilation": "heat_recovery"}},
        "roof": ["garden"]
      }
    },
    {
      "id": "C",
      "geometry": {"relative_length": 1},
      "allocation": {
        "usages": ["office", "residential"],
        "usage_shares": {"residential": 0.25}
      },
      "systems": {
        "usages": {"office": {"heating": "radiator"}},
        "roof": ["pergola", "terrace"]
      }
    }
  ]
}
```

Shares refer to fractions of the scenario usage total, not the building floor
area. Residential allocations are 1,800/900/900 m²; total building NFAs are
2,400/1,800/1,800 m². At four floors maximum, the two shorter buildings require
at least 450 m² footprints each. The 2:1:1 length ratio consequently gives
900/450/450 m² footprints and lengths 60/30/30 m. Building A has two full floors
and a 600 m² partial third floor; B and C have four full floors. Food retail fits
on A's ground floor, with residential filling the remaining 300 m². B's school
occupies two floors below residential; C's office does the same.

This exposes why a maximum floor count is a limit, not an instruction to fill all
buildings to that height. Continuity and the requested shares take precedence over
matching heights. Above-ground area is conserved; no blank filler is introduced.

A's 900 m² basement is deliberately empty of NFA usages. It may show schematic
parking and the plant overlay. Neither those symbols nor the shaft add to the
scenario NFA. The heat pump is drawn once in A at B1; schematic distribution
connections serve all three buildings. No flow rates, temperatures, pipe sizes
or heat shares are inferred. A groundwater source needs separate site positioning
if its well is to be placed precisely; the first version can mark that position
as an assumption.

**Findings:**

- Shared plant belongs in a root `systems.plant` list with stable IDs, host
  location and `serves` references. Building-local plant shorthand can normalize
  into this same representation. `defaults.systems.plant` instead explicitly means
  one local instance per building, never one shared instance.
- Use the same location record for local and shared equipment. Level 0 is ground,
  negative levels are basements, positive levels are upper floors; `"roof"` and
  `"lowest_floor"` are symbolic alternatives. Omitted location remains unknown.
- A gap associated with two buildings should use `between`, not just `after`.
  If reordering makes that pair non-adjacent, validation asks the user to resolve
  it instead of moving the courtyard silently. Existing `gap_after_m` remains a
  positional shorthand through compatibility normalization.
- Side assignment needs an explicit `site.street_side` per building (`left` or
  `right`) with the current alternating rule as a reported default. Street does
  not imply a compass orientation.
- Do not add floor-by-floor HVAC exceptions yet. Usage-level settings plus
  explicit plant locations cover these cases. Add exceptions only with a real
  example, rather than introducing a general query language now.

## Decisions and acceptance checks before implementation

| Question | Recommended rule / acceptance check |
|---|---|
| Does layout change energy inputs? | Never. Compare scenario values before and after generation. |
| What if geometry conflicts? | Error on an impossible allocation; report deliberate count/depth/storey overrides. Widen footprints when length is derived. |
| What if a drawn plant conflicts with an inactive scenario slot? | Report the conflict prominently; explicit illustrative symbols do not imply active capacity. Inference never activates an inactive plant. |
| How are defaults resolved? | Merge defaults then building values per field; within each scope resolve `*` before usage-specific entries. Lists replace; `[]` clears. Missing inherits; zero is not missing. |
| What if an explicit share is invalid? | Reject negative or over-budget shares and usage shares for ineligible buildings; allocate the remainder by eligible capacity. |
| What is an unknown location? | Keep it unresolved and labelled; do not invent a host or duplicate plant. |
| Can an HTML editor consume this? | JSON round trip, stable IDs, enum choices, units and field-addressed errors, e.g. `buildings[1].geometry.depth_m`. Reuse schema metadata for scenario fields. |
| Does it preserve current APIs? | Normalize legacy dictionaries; compare generated area/geometry and SVG semantics with legacy fixtures. Reject conflicting old/new keys rather than guessing. |
| Are shared quantities conserved? | PV and usage budgets are scenario-wide; shared plant is instantiated once. |
| Are references safe? | Reject duplicate IDs, missing hosts/served buildings, unavailable levels and non-adjacent gap endpoints. |

The grouping survives these examples. The changes worth incorporating before
coding are: geometry/allocation defaults, one normalized plant representation,
explicit unknown locations, and pair-addressed gaps. No new generic domain model
is needed. Proposed heat-pump drawing and connection routing remain additional
renderer work, not functionality implied by these example dictionaries.

## 4. Draft Zero: inspect, configure, simulate, diagnose, revise, submit

The [Draft Zero project memo](draft_zero_project_memo.md) defines a configuration
puzzle, not a continuous building-management game. This review therefore tests
renovation edits and comparison, not tenants, construction queues or economic ticks.
No gameplay implementation is proposed in pexl.

### Walkthrough: insulate a façade and change roof PV

1. The player selects a façade in the SVG. Its semantic target ID resolves to a
   generated section element and its known scope, independent of SVG path IDs,
   drawing style and decorative relief. The game opens a material/thickness form.
2. Draft Zero records the measure, catalogue reference and target in its renovation
   plan. Its measure application code resolves physical properties into supported
   pexl scenario inputs. The layout does not become another store of editable
   U-values, costs or embodied emissions.
3. Before applying the measure, the game checks scope. A schematic façade does not
   establish that pexl supports an independently simulated façade or building.
   Where only aggregate inputs exist, the game must declare aggregate application,
   implement a scientifically justified aggregation using authoritative areas, or
   disallow local application. It must not area-weight U-values using invented
   section lengths or schematic depths.
4. Changing PV module count/power updates supported scenario inputs through the
   measure application code. Layout specifies placement preferences and roof
   eligibility. The section reports placed and unplaced area without duplicating
   the global PV budget. Illustrated modules are not automatically an exact
   electrical/module/string design; any exact packing feature needs real dimensions
   and its own validated placement rules.
5. Regenerate the overlay against the same resolved geometry for comparison.
   Insulation or PV changes must not unexpectedly redistribute usages or rename
   selection targets. A seed alone does not guarantee edit stability.
6. The game runs the simulation for a recorded scenario revision and displays its
   results. Any subsequent edit invalidates that result for submission. Undo/redo,
   revision tracking, scoring and save games belong to Draft Zero.

### Refinements required by this use case

| Concern | Proposed pexl boundary | Draft Zero responsibility |
|---|---|---|
| Selection | Stable semantic IDs for buildings, spaces, envelope surfaces and equipment; SVG `data-*` references them. Decorations reference their owning surface. | Hit handling, selection state, menus and accessibility controls. |
| Identity after edits | IDs derive from persistent layout identities and semantic ownership, not drawing order or random coordinates. Structural reallocation explicitly invalidates affected targets. | Reconcile or flag renovation measures with missing targets; never silently retarget. |
| Before/after comparison | Support reusing resolved geometry when geometry-driving inputs are unchanged. Reject stale geometry or request regeneration when areas/depths/allocation change. | Select baseline/variant and manage comparison state. |
| Scientific scope | Expose evidence and actual scope of inputs; distinguish assumed geometry from physical quantities. | Map measures to schema-backed inputs and explain aggregate versus local effects. |
| Appearance of interventions | Keep selectable layers and semantic component/material roles accessible to renderers. Fixed schematic thickness is not physical insulation thickness. | Game artwork, unlocked options, highlights and plan annotations. |
| Save/load | Versioned, JSON-compatible layout and documented ID rules. | Save scenario reference/revision, plan, catalogue version, seed/layout and progress. |
| Diagnosis | Associate outputs with their real scope; do not invent room-level performance from aggregate results. | Result panels, educational explanation and submission rules. |

This strengthens the proposed structure without requiring a game-state model in
pexl. Add semantic target/identity rules and resolved-layout reuse to the refactor
acceptance criteria. Do not add XP, catalogue prices, scenario objectives, gameplay
commands or a generic event system to the layout.

### Acceptance scenarios for the later implementation

- Applying and undoing insulation preserves unaffected surface IDs and geometry.
- Rendering architectural and hand-drawn views exposes the same semantic targets.
- A changed PV budget changes only the relevant overlay; the budget is conserved.
- Deleting a host building reports orphaned plant references and affected targets.
- Save/reload reproduces layout and IDs; catalogue/plan replay is tested in Draft Zero.
- A request to edit one schematic façade cannot silently masquerade as a locally
  resolved physical change when the scientific model only supports an aggregate.
- Results from an earlier scenario revision cannot count as the submitted result
  after an edit; that guard is tested in Draft Zero, not the SVG renderer.

**Recommendation:** proceed with the small normalization refactor, but specify
stable semantic identities and comparison reuse before adding browser controls.
The main unresolved scientific decision is the supported scope of local renovation
measures. The memo does not settle that; it needs checking against actual schema
capabilities for each measure.
