# Schematic building sections

```python
from pathlib import Path
from pexl import Project
from pexl.spatial import section_layout_from_scenario, render_svg

project = Project()
scenario = project.get_or_create_scenario("Demo | Baseline")
scenario.v.NFA_office = 600
scenario.v.NFA_residential = 1800
scenario.v.building_count = 2
scenario.v.storey_count_avg = 3
section_layout = section_layout_from_scenario(scenario, seed=42, layout="default")
Path("section.svg").write_text(render_svg(section_layout), encoding="utf-8")
```

The generator reads the existing Scenario and schema metadata. It neither
modifies the scenario nor calculates energy demand. SVG rendering uses only
the returned dictionary and Python's standard library.

## Dictionary contract

- `source`: scenario column name, project name and scenario name.
- `seed`, `layout`: reproducibility and allocation mode. Building records hold `depth_m`; the top-level `depth_m` is the common depth, or `None` for mixed depths.
- `buildings`: stable IDs and floor IDs.
- `floors`: building ID, index, upward-positive `z_m`, room height and slab thickness.
- `spaces`: floor ID, usage key, source variable, schema label, NFA in `area_m2`,
  `x_m` and `width_m`. Width times depth equals NFA; the visible rectangle area does not.
- `voids` (default layout): an empty list retained for compatibility; unassigned
  schematic space is no longer generated.
- `adjacency`: undirected space-ID pairs, horizontal/vertical relationship and
  shared interval (z for horizontal neighbours, x for vertical neighbours).
- `roofs`: exposed upper segments with supporting space IDs and schematic area.
- `facades`: section-end surfaces with floor IDs and the existing wall U-value variable.
- `pv`: requested module area, placements referencing roof IDs, and unplaced area.
  Unknown sizing is represented by `None`, rather than zero.
- `context`: available gross area, plot, envelope and PV-ratio values, kept
  separate from the NFA-based geometry.
- `assumptions`: codes and readable explanations, also included in the SVG.

## Allocation rules

Usage variables are selected through existing schema metadata. All modes conserve
known NFA per usage and retain the supplied building count:

- `default`: food retail remains on building 1's ground floor and other retail
  extends across ground floors as needed. Footprints widen if required to keep
  retail at ground level. Primary school, secondary school and office are each
  assigned as a single continuous block to the building with the least allocated
  NFA (building order breaks ties). Blocks extend upwards as necessary. Available
  `other` area finishes each block's last floor; when exhausted, residential fills
  the remainder from its available budget. No unassigned schematic space is added.
  If neither budget suffices, the floor ends at the allocated area.
  Office can start on an unused ground floor; otherwise
  it starts above existing uses. Remaining `other` is assigned before residential.
  After buffer infill, remaining residential fills the shortest tops first, sharing
  height differences across buildings. Continuous blocks take priority over equal
  heights. Partial residential top floors form the stepped skyline ("Zinnen").
- `separateResidential`: preserves the previous default. Food retail occupies
  building 1's ground floor, widening its footprint
  if needed. Other retail uses remaining ground floors, starting with building 1;
  if necessary, footprints widen so retail never moves upstairs. Remaining ground
  space in building 1 is reserved for `other`. Its remainder and the two school
  categories continue on upper floors in that building. Offices fill available
  ground and first floors across buildings, then higher floors building by building.
  Residential use fills remaining capacity from the bottom up, building by building.
  Widths and occupied storey counts can differ from the input average; empty capacity
  is omitted. An entirely unused building retains its dictionary record but is not drawn.
- `equalspread`: each usage is divided equally among buildings. Offices appear
  below other uses and residential above. Remaining usages share one seeded order
  across all buildings. Fractional average storeys become partial upper floors.

Partial segments preserve fractional areas. The unused total
area is labelled `unallocated`, distinct from the schema's `other` usage.
Missing total NFA is derived from known usages. Usage sums exceeding a supplied
total are rejected, except for floating-point roundoff.

Missing building/storey counts default to one; missing average room height to
3 m and slab thickness to 0.35 m. Supplied counts must be positive, and building
count must be integral. Depth defaults to 15 m per building and building gaps are 20 m. These are
schematic assumptions, not measured geometry. Plot and thermal-envelope areas
do not constrain these widths. No building positions, usage-specific room
heights, roof slopes, setbacks or orientations are inferred.

PV disabled explicitly by `PV_is_used` is not placed. Otherwise module area is
preferred, falling back to `PV_kWp * PV_m2_per_kWp`. Missing conversion factors
are not invented. Roof fraction is checked against supplied thermal roof area
for consistency, not multiplied into module area again. Placement fills flat
schematic roofs; overflow remains in `unplaced_area_m2`. This does not establish
actual roof suitability or PV yield. A missing enable flag and conflicting
sizing values are recorded in the assumptions.

Geometry extraction is inspired by ClimTower's `create_layout`, `add_spaces`,
roof generation and `add_pv`, rewritten to preserve areas and use current schema
interfaces. No game engine, artwork or simulation classes are included.

## Rendering

The SVG has independent horizontal and vertical scales, keeping storeys legible
even for very wide sections. It includes floor names, local 15 m horizontal ticks,
usage color swatches, and raised PV symbols. Full assumptions are retained in
the section dictionary and SVG description. Wide figures should be placed in a
horizontally scrollable notebook output rather than reduced to page width.

Façades and roofs have separate construction and lilac insulation layers. Slabs
end flush with the construction face; insulation runs continuously outside their
edges, including across floor and roof slabs. Layer drawing widths are schematic, not material
measurements or thermal inputs. `render_svg(section, construction="wood")` uses
light-brown construction instead of the default dark green.

The notebook demonstrates static SVG creation, inspection and parameter changes
through `scenario.v`. For capacity sweeps, assign `scenario.v.PV_kWp` and set
`scenario.v.PV_module_area = None` so module area is derived from capacity and
the supplied `PV_m2_per_kWp`. Regenerate the section and SVG after each change.
There are no notebook controls and no formula recalculation.

## Explicit building layouts

```python
layout = {
    "buildings": [
        {"name": "Building 1", "relative_length": 2, "max_floors": 6,
         "usages": ["office", "residential"],
         "usage_shares": {"residential": 0.6}},
        {"name": "Building 2", "relative_length": 1, "max_floors": 4,
         "usages": ["residential"]},
    ]
}
section_layout = section_layout_from_scenario(scenario, layout=layout)
svg = render_svg(section_layout)
```

The example requires a scenario whose positive usage areas are office and residential.
For an all-usage scenario, include every positive usage in at least one building.

- `buildings` is a nonempty ordered list. Its length overrides scenario building count
  for this projection. `max_floors` overrides the average-storey input.
- `name` is optional; defaults to Building 1, Building 2, etc.
- `relative_length` is a positive weight, defaulting to 1. Weights 2:1 and 2/3:1/3
  describe the same ratio. These refer to nominal footprints; a building with less
  than one full floor of allocated area has a partial ground/top floor.
- `max_floors` is a required positive integer. It is a limit, not an exact floor count.
- `usages` is a required list of unique schema entity keys, ordered bottom to top.
  Usages may share a floor at their boundary. There is no automatic reordering or
  buffer infill in a custom layout. `unallocated` may explicitly represent a supplied
  NFA-total remainder whose usage is unknown.
- `usage_shares` is optional. Each value is a fraction in [0, 1] of that usage's
  scenario-wide area. Unspecified shares receive the remaining area in proportion
  to `relative_length * depth_m * max_floors`. If all eligible buildings specify shares,
  they must sum to one; sums above one are invalid.

Area allocation is performed first. With normalized length weights `w_i`, allocated
areas `A_i`, maximum floors `F_i`, and building depths `D_i`, without basements the internal drawing
scale is `L = max(A_i / (D_i * w_i * F_i))`. Building i has nominal length
`w_i * L`. The 20 m gaps are excluded from L. Full floors are filled in order and
only the final above-ground floor can be partial; basement footprints remain full, with any unused area empty. Zero-area buildings, unknown fields,
unknown/duplicate usages, uncovered positive usages and invalid shares raise
`ValueError`; no area is silently discarded. Source data and the input dict are
not mutated. No new schema variable definitions are introduced.

The result has `layout="custom"`, a normalized JSON-compatible `layout_spec`,
and building records containing `name`, `width_m`, `depth_m`,
`max_floors`, `max_basements` and `usage_areas_m2` for inspection. Named modes and `layout=None`
remain supported. The module is `pexl.spatial.section_layout`; the old public
`section_from_scenario` function and module import remain compatibility aliases.

The notebook includes an illustrative two-building 2:1 Forsthausgasse-proportion
example, plus capacity-weighted and explicit-share variants.

## Suggesting an editable layout

```python
from pexl.spatial import suggest_section_layout

layout = suggest_section_layout(scenario)
layout["buildings"][0]["max_floors"] = 6
section_layout = section_layout_from_scenario(scenario, layout=layout)
svg = render_svg(section_layout)
```

The helper uses the default heuristic to propose building length ratios, occupied
floor counts and usage assignments. It groups each usage into a continuous block,
placing office below residential, and includes explicit shares to preserve the
proposed per-building areas. It returns a plain JSON-compatible dictionary and
does not mutate the scenario. The generated custom geometry may differ from the
automatic layout: length is derived again and scattered buffers become blocks.
If the heuristic leaves buildings empty, the proposal uses equal spreading to
retain the scenario building count. Floor counts in the proposal become editable
limits, rather than constraints on the initial heuristic.

Remove `usage_shares` from the relevant buildings to split their remaining shares
by capacity instead. When introducing a previously absent usage, add its schema
key to the desired buildings before regenerating. `seed=42` is the default.

## Per-building depth and local axes

Set `depth_m` in each building specification; it must be finite and positive and
defaults to 15 m. The suggestion helper includes this field for easy editing.
Space length is area divided by that building's depth. The same depth converts
roof widths to roof areas and PV module areas to drawn widths. Capacity-based
sharing uses relative length times depth times maximum floors; explicit shares
continue to override it.

The SVG uses one continuous baseline and a common metre scale. Labels restart at
zero for each building, with no ticks in the gaps. The first row shows metres;
the second shows cumulative floor area on one storey (distance times depth),
not the sum of all storeys. Each building's depth appears below its name.
No overall length is displayed or returned as `total_building_length_m`; the
internal scale only establishes schematic proportions. The notebook demonstrates
15 m and 25 m depths with equal physical tick spacing but different area labels.

## Rendering styles

```python
svg = render_svg(section_layout, style="architectural")  # default
sketch_svg = render_svg(section_layout, style="hand_drawn")
plan_svg = render_svg(section_layout, style="blueprint")
```

`architectural` retains the usage colors, dark-green construction and lilac
insulation. `hand_drawn` uses the same colors on warm paper with invisible floor/ceiling slabs, jittered fineliner wall frames and axes,
handwritten labels and yellow sticky-note building names. Its decorative strokes are deterministic
and do not change space boundaries, areas or the random state of the application.
`blueprint` is a light-blue plan style with a pale drafting grid, blue usage shades
and darker construction and PV. The legend follows the selected palette.

All styles retain building depths, local metre and floor-area axes, floor names,
PV placement and accessible SVG titles. Horizontal and vertical scales remain
independent. `construction="wood"` remains available, using a lighter construction
shade in blueprint style. These are self-contained static SVGs; no downloaded fonts, scripts, rendering libraries or network resources are required.
The sketch uses installed Ink Free, Segoe Print, Bradley Hand or Comic Sans MS, falling back
to the viewer's cursive font; exact lettering therefore varies between systems. The how-to notebook renders
the same layout in all three styles for comparison.

## Basements, ground and butterfly PV

```python
layout = suggest_section_layout(scenario)
layout["buildings"][0]["max_basements"] = 2
# Optional: overrides the default underground order, from B1 downwards.
layout["buildings"][0]["basement_usages"] = ["retailfood", "schoolprim", "other"]
section_layout = section_layout_from_scenario(scenario, layout=layout)
svg = render_svg(section_layout, style="hand_drawn")
```

`max_basements` is a nonnegative integer, defaulting to zero. It specifies the
number of underground levels; `max_floors` remains the above-ground limit.
Basements fill from B1 down to B2, B3, etc. Every requested basement keeps the
building footprint, even if it is partly or entirely empty. Empty areas are
returned in `voids`, rendered explicitly, and excluded from scenario NFA.

`basement_usages` is an ordered list, independent of above-ground `usages`.
When omitted for a building with basements, it defaults to
`["retailfood", "retailother", "schoolprim", "schoolsec", "other"]`.
Office and residential are never allocated underground unless explicitly listed.
An explicit empty list leaves all requested basements empty. Unknown or duplicate
usage keys are rejected; a nonempty underground list requires a positive count.

`usage_shares` still refers to the scenario-wide usage area allocated to a building.
Unspecified shares use relative length times depth times the number of floors
eligible for that usage: above-ground floors, basements, or both. For a usage in
both lists, basement placement is attempted first, reserving capacity for usages
allowed only below ground. Remaining area follows the above-ground usage order.
Only-below-ground areas constrain the derived width so they fit within the count;
no usage area is dropped or created. Suggestions retain explicit shares, so
remove those shares where capacity-based redistribution is desired.

The historical `basement=True` flag remains a compatibility shorthand for
`max_basements=1`; new layouts and suggestions use the integer field. Contradictory
old and new fields are rejected. Normalized specifications contain the integer
count and explicit basement usage list. Basement floor indices are -1, -2, etc.,
and their z coordinates are negative. Underground surfaces do not provide PV
roof capacity.

All styles show a soil band and ground line extending beyond the buildings and
below the lowest floor. Soil shading alone does not create basement floor area.
The hand-drawn style hides floor/ceiling slabs and uses fine irregular wall and
axis outlines, handwritten text and yellow building-name notes.

PV symbols are butterfly pairs with inward-sloping wings at 15 degrees in the
drawing. Supports keep them above the roof. Placement retains the schematic
flat-area convention, without tilt-adjusted footprint, shading or yield modelling.
Placements record `tilt_deg=15` and `arrangement="butterfly"`.

## Interior details and expressive sketch rendering

All rendering styles include subtle interior partitions and a central service
shaft. These are schematic overlays above usage fills: they do not create spaces,
change adjacency or floor assignments, deduct NFA, or modify the section dictionary.
Room spacing is approximately 5 m for residential, 6 m for office, 8 m for schools
and other usage, 9 m for nonfood retail and 12 m for food retail. Partitions are
evenly spaced within each usage segment; short segments remain undivided.

The shaft is centered on each building's drawn extent, up to 2 m wide (limited to
15% of the width for small buildings), and clipped to each occupied floor's extent.
It may therefore end below a partial top storey. These symbols convey an interior
arrangement, not a measured room plan or a structural/service design.

The hand-drawn style uses streaked marker fills, stronger fineliner jitter,
Ink Free handwriting with small per-letter rotations, and larger rectangular
yellow sticky notes centered over each building. Separate ceiling/roof bands are
hidden in this style, together with all green floor/ceiling slabs. The roof geometry and PV
placement remain unchanged. All decorative randomness is deterministic.

## HVAC and roof overlays: shared defaults and building overrides

Start from a suggested or explicit layout and add `systems` at the root. Every
building inherits it; a building's own `systems` overrides just the supplied
settings. These optional presentation settings do not create a second energy
model or alter scenario values, areas, adjacency, roof capacity or PV sizing.

```python
layout = suggest_section_layout(scenario)
layout["systems"] = {
    "usages": {
        "*": {"heating": "underfloor", "cooling": "tabs", "ventilation": "mechanical"},
        "office": {"ventilation": "heat_recovery"},
    },
    "plant": ["heating_room", "district_heating"],
    "roof": ["pv", "solar_thermal", "pergola", "terrace", "garden"],
}
layout["buildings"][0]["systems"] = {
    "usages": {"office": {"cooling": "split"}},
    "plant": ["heating_room", "gas_boiler"],
}
section_layout = section_layout_from_scenario(scenario, layout=layout)
svg = render_svg(section_layout)
```

Precedence is scenario hints, shared wildcard, shared usage, building wildcard,
then building usage. Usage dictionaries merge field by field. Plant and roof lists
replace their inherited lists; `[]` clears one. `"none"` disables an inherited
heating, cooling or ventilation symbol. Unknown options are rejected.

| Setting | Supported values |
| --- | --- |
| `heating`, `cooling` | `none`, `tabs`, `underfloor`, `radiator`, `split`, `fan_coil` |
| `ventilation` | `none`, `natural`, `mechanical`, `heat_recovery` |
| `plant` | `heating_room`, `water_well`, `boreholes`, `district_heating`, `gas_boiler`, `oil_boiler`, `biomass_boiler` |
| `roof` | `pv`, `solar_thermal`, `pergola`, `terrace`, `garden` |

Enable the overlay with `systems={}` to use available scenario hints. Positive
`vent_share_mechanical_<usage>` selects a mechanical ventilation symbol;
`borehole_count` selects boreholes; `heat_th2_is_dh` or `heat_th4_is_dh` selects a
district-heating connection. Values used are retained in
`section_layout["systems"]["source_values"]`. Emitters and other heat sources
are not inferred from ambiguous carrier labels. Layout overrides describe the
drawing only: change `scenario.v` to change authoritative energy inputs.

Resolved per-building settings are available under
`section_layout["systems"]["buildings"]`. Inferred symbols are repeated per
building as shared schematic defaults, not as additional installed capacity.
Usage-level symbols appear on occupied spaces, including basements. Very narrow
segments (less than 36 rendered pixels) omit symbols to remain legible; their
settings remain in the returned dictionary. Plant symbols overlay the lowest
floor. Well and borehole symbols extend into soil below it. No plant-room NFA is
deducted. Boiler letters G, O and B denote gas, oil and biomass.

Roof amenities are symbolic callouts above the widest exposed roof, with leaders
back to it. Multiple amenities can coexist as annotations, but no roof area
fraction, stacking feasibility, equipment count or dimensions are inferred.
PV continues to use existing scenario-derived placements. Omitting `pv` from a
building's roof list hides its panels, without reallocating capacity; the footer
reports any hidden module area. Adding `pv` does not invent panels when module
area is missing or disabled. Roof features and HVAC do not affect energy results.
The notebook shows the same overlay in all three styles.

## Annotated symbol review and physical drawing design

```python
svg = render_svg(section_layout, style="annotations")
```

The annotations style uses the blue plan palette and adds a numbered key beside
the section. Each distinct drawn system symbol receives one numbered representative
and a readable label with its occurrence count. PV is included. Only symbols
actually drawn are listed. This is a review view of the current symbols, not a
claim that their connections or physical construction details have been designed.
The normal geometry and scenario data remain unchanged.

The next design direction under review prioritizes which building and usage has
which system, and its physical placement: TABS embedded in concrete, underfloor
loops above the structural slab, ventilation ducts below ceilings, plant equipment
inside the relevant building, and AC units near windows. Usage colors and symbol
positions should remain consistent so differences are immediately apparent.
Teaching-level arrows and a few labels are preferred over dense engineering data.
Three review directions are a whole-building sectional overview, enlarged physical
construction details, and consistently drawn building comparisons. The section and enlarged construction details are available as separate SVGs. Physical placement is implemented; full circuit connection logic is not inferred.

See the [three physical drawing proposals](hvac_design_directions.svg) for the current design review.

## Physical section with enlarged construction details

The system overlay shows the whole-building view. Enlarged construction details
are emitted separately with `render_emission_details_svg(section_layout)`. TABS circuits sit within the structural slab; underfloor loops
sit in a screed layer above insulation and structure. Mechanical ducts run below
the ceiling with supply arrows; split units are high on the facade side, while
radiators and fan coils sit lower beside a representative window. Windows are
illustrative room context, not new thermal-envelope inputs. Natural ventilation
is shown through the window rather than as a mechanical duct.

The specified plant equipment appears within the lowest floor's plant-room
outline when `heating_room` is enabled. The enclosure is an overlay, not a new NFA
allocation. Enlarged detail cards explain TABS, underfloor construction, and
ceiling/facade systems in the separate SVG; they are marked as not to scale. Small construction
cutaways remain visible with hand-drawn systems even though the normal green
slabs remain hidden. Supply arrows illustrate local emission and ventilation;
a complete plant-to-emitter network is not invented from the available inputs.

The notebook applies this drawing to its worked two-building scenario. SVG remains
the renderer output; a PNG export of that figure is provided for review. Its
values are illustrative notebook inputs, not a surveyed building or installation.

## Street/courtyard sides and facade windows

Buildings alternate street side: building 1 faces the street on the left and
courtyard on the right; building 2 reverses this, then the pattern repeats.
The generated building records contain `street_side` and `courtyard_side`;
each facade records `exposure`. A shared gap is drawn once: courtyard between
buildings 1 and 2, street between 2 and 3. Curb, parked-car and cycle-lane cues
identify the street. Trees, shrubs and a small play frame identify the courtyard.
These are schematic context drawings, not measured site geometry or added area.

Above-ground facades on both sides receive equivalent window bands. Their clear
height fraction follows `scenario.v.hull_fenestration_rate` when supplied (0 to 1,
so 0.35 means 35%). Otherwise the generator derives
`hull_window_m2 / (hull_ext_wall_wo_window_m2 + hull_window_m2)`, subtracting
`hull_windows_horizontal_m2` from the glazing numerator and denominator when
available. The wall variable explicitly excludes windows. A conflicting explicit
fraction takes precedence and is noted in assumptions. Missing inputs use a
recorded 30% schematic default; an explicit zero remains opaque. Invalid fractions
and horizontal areas exceeding total glazing are rejected. Basement walls remain
opaque; light wells are not inferred.

`glazing_ratio`, `window_height_m` and `glazing_source` are recorded per facade.
The band represents the supplied area fraction across an equivalent facade width;
it is not a surveyed window schedule. Street/courtyard-specific glazing ratios
cannot be inferred from the aggregate inputs. Windows and context graphics do not
change scenario areas or thermal inputs. The notebook demonstrates 35% glazing.


### Modular roof scenes, rooftop HVAC and parking

Use `systems.roof=["garden", "pergola", "terrace", "solar_thermal", "hvac_room"]`
in shared settings or a building override. Gardens, furnished terraces, pergolas
and collectors form repeatable side-on scene tiles directly on exposed roofs.
These original SVG drawings take inspiration from Project Highrise's compact
cutaway scenes; no game artwork is included. There is no ceramic `tiles` option.

PV keeps its generated placement. The scene tiles fill the remaining roof spans,
avoiding the HVAC room, which continues the shaft at twice its width. Full scenes use fixed 64-pixel bays without stretching furniture. Narrow
remainders of at least 24 pixels can contain a planting bed when garden is enabled;
otherwise they stay clear. Features cycle through full bays in list order; if roof space is insufficient, later features may
not appear. Scene widths are illustrative, not equipment sizing or roof-area
allocations. Neither these drawings nor the HVAC room create floor area or plant
capacity. `plant=["heating_room"]` remains the lower-level plant room.

Underfloor and TABS pipes are straight horizontal runs in their respective layers,
including the enlarged construction details. Heating and cooling use parallel
runs when configured in the same layer.

Unassigned basement capacity is displayed as a parking garage, with cars and a
parking label where space permits. It remains in `voids`, excluded from scenario
NFA totals. Legends group Usage, Material overlay and HVAC overlay.


### Graphic hierarchy and separate emission details

Usage fills are muted and envelope layers use lighter colours and narrower facade
bands. Each roof/plant object uses one hue with brightness variations. Heat, cold
and air circuits retain their separate semantic colours. Legend samples reuse
actual object drawings, with line samples for emission and ventilation systems.
The shaft has clear boundaries and continuous service risers overlaid above local
systems. Orthogonal well/borehole connections illustrate the relation to the plant
room; they do not specify a hydraulic network.

`render_svg(section_layout)` emits only the section and grouped legend. To create
an independent teaching figure, use:

```python
from pexl.spatial import render_emission_details_svg
emission_svg = render_emission_details_svg(section_layout)
```

The standalone SVG shows the configured TABS, underfloor and ventilation/AC
construction details; it is not appended to the main section.


### Site silhouettes and circulation

Site and roof furnishings use muted architectural silhouettes. Cars are shown
in front elevation in both streets and parking garages; the courtyard tree is
three times the earlier schematic size. Roof scenes and HVAC rooms meet the roof
finish directly, and PV supports meet the insulation surface.

Street sections connect to the building envelope. They show raised curbs, pavement,
road base, utility inspection chambers and horizontal conduits. These dimensions
are illustrative drawing dimensions, not a surveyed street or utility network.
The service shafts alternate a lift (first building) and switchback stairs
(second building), repeating for additional buildings. The lift car is shown at
ground floor; rails continue through the shaft. Circulation is a drawing overlay:
it neither consumes NFA nor constitutes a stair or lift sizing calculation.


### HVAC preset mapping gallery

The [gallery notebook](../../notebooks/howto_hvac_gallery.ipynb) reviews 40 actual
workbook presets across emission, heating, cooling, ventilation and domestic hot
water. Six SVG boards distinguish available, partial and proposed symbols; three
sections use scenarios from the v1_13 project used in the other how-tos.
The [catalogue snapshot](hvac_preset_catalog.json) preserves internal names, dropdown
labels, cached values, source cells and the workbook SHA-256.

The gallery does not apply presets or add automatic inference to the library. It
checks active generator capacities before using carrier names, leaves unspecified
emitters unresolved, and flags heat-pump sources, exhaust-only ventilation and
central/decentral hot-water arrangements that need more precise representation.
The notebook-local `_hvac_gallery.py` contains design-review drawings only.


### Forsthausgasse real-project showcase

The [dedicated notebook](../../notebooks/howto_section_real_project.ipynb) compares
two stored Forsthausgasse scenarios with identical 2:1 building layouts, using
actual NFA, fenestration, PV and active generator inputs. A comparison SVG and
full-size sections distinguish the PV changes and document the conflict between
the WP variant title and its populated district-heating configuration. The layout
overrides the stored building count with the user-specified two buildings; it does
not overwrite scenario values. Notebook checks validate conserved NFA and unchanged
source inputs.


### Configurable gaps and Gründerzeit façades

For named layouts, `section_layout_from_scenario(scenario, gap_m=12)` changes the
common 20 m gap. Custom layouts accept a top-level `gap_m` and per-building
`gap_after_m` (to the next building). Values must be finite and nonnegative; zero
is valid. The last building has no following gap. Gaps are measured between
schematic floor footprints; fixed drawing-thickness envelope/relief is not a
measured site setback. Area allocations and PV capacity remain unchanged.

Set top-level or per-building `facade_style="gründerzeit"` (ASCII alias
`"gruenderzeit"`) for rusticated bases, sill/lintel mouldings, floor bands and
stepped cornices. Courtyard relief is simpler. `"default"` retains the plain layered
façade. `render_svg(section, facade_style=...)` overrides all buildings for a visual
comparison. Omit the renderer override to retain individual building settings.
Relief is decorative section geometry, independent of wall U-values, window area,
construction quantities and the graphic style. It works with all renderer styles.

See the [versioned layout refactor proposal](section_layout_refactor_proposal.md)
for future site, envelope, circulation, storage, DHW and HVAC categories. The
proposal preserves schema authority and existing shorthand; it is not implemented.


## Versioned layouts and comparison reuse

Version 1 is now accepted alongside the existing flat dictionaries and named modes.
`normalize_layout(layout)` returns a detached JSON-compatible specification with
resolved defaults and validated references. No scenario input is modified.

```python
from pexl.spatial import normalize_layout, section_layout_from_scenario, render_svg

layout = {
    "layout_version": 1,
    "site": {"gap_m": 20,
             "gaps": [{"between": ["A", "B"], "width_m": 28, "kind": "courtyard"}]},
    "defaults": {
        "geometry": {"depth_m": 15, "max_floors": 4},
        "allocation": {"usages": ["office", "residential"]},
        "systems": {"usages": {"*": {"heating": "underfloor"}}},
    },
    "buildings": [
        {"id": "A", "geometry": {"relative_length": 2},
         "envelope": {"street": {"facade": {"style": "gründerzeit"}}}},
        {"id": "B", "circulation": {"kind": "stairs"}},
    ],
    "systems": {"plant": [
        {"id": "DH1", "kind": "district_heating",
         "location": {"building": "A", "level": "lowest_floor"},
         "serves": ["A", "B"]},
    ]},
}
# Supply a scenario whose positive usage areas are eligible in this layout.
section = section_layout_from_scenario(scenario, layout=layout)
scenario.v.PV_module_area = 100
variant = section_layout_from_scenario(scenario, layout=layout, reuse_geometry=section)
svg = render_svg(variant)
```

Geometry/allocation, envelope, circulation, systems and building site options inherit
per field from `defaults`. Building overrides win; within each scope usage-specific
settings override `*`. Lists replace, and `[]` clears. IDs must start with an ASCII
letter and contain only letters, digits, hyphens or underscores. Mixed flat/versioned
keys are rejected. Building order remains the order drawn. Pair-addressed gaps must
remain adjacent. `site.street_side` on a building explicitly selects left or right.

Root `systems.plant` records describe shared or unlocated equipment once. A record's
`serves` references buildings, without assigning heat shares or capacities. Local
`buildings[].systems.plant` and `defaults.systems.plant` accept string shorthand or
records and normalize to the same root list. A default local plant means a separate
instance per building. Set root `systems.plant=[]` to disable plant inference when
no local plants are specified. Omitted plant settings permit conservative active
thermal-slot inference; a scenario-wide inferred plant has no invented host.

Locations accept a building ID and `level`: 0 for ground, negative integers for
basements, positive integers for upper floors, `lowest_floor` or `roof`. A level
must exist in the generated geometry. New heat-pump records accept source values
`unknown`, `air`, `ground` or `groundwater`; these are explicit visual choices,
not additional simulation inputs. Shared connections are schematic. Unlocated
records appear in the legend, not at an invented building position.

Generated records add `semantic_id`; SVG elements expose `data-semantic-id`.
Existing IDs/result keys remain available. Semantic IDs encode building/floor/usage
ownership, not drawing order; structural edits can still invalidate targets.
Decoration and window/insulation layers reference their owning façade or roof.
The game must reconcile missing targets after a structural edit.

`reuse_geometry=previous_section` verifies the actual allocation and dimensions,
then copies detached geometry into the new result. This is a correctness guard,
not a performance cache: allocation is regenerated to check compatibility. Changing
PV or thermal properties is allowed; changing NFA, floor geometry or gaps rejects
reuse. New context and overlays always follow the current scenario. Never mutate
the previous section to bypass this check.

Roof eligibility in a versioned layout controls placement of the one scenario-wide
PV budget. Area not fitting eligible roofs is reported unplaced. Façade style and
fixed drawing layers do not change U-values. Generated `equipment` carries explicit
or inferred provenance; geometry is labelled schematic. A selected graphical
surface does not imply independently simulated surface properties.

The [design examples](section_layout_refactor_examples.md) explain the decisions;
the [Draft Zero memo](draft_zero_project_memo.md) defines the game boundary. The
notebook contains an executed versioned example. Catalogue/measure mapping,
local scientific aggregation, gameplay and floor-specific emitter overrides are
outside this refactor.
