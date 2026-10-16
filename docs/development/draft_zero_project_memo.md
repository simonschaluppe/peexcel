# Draft Zero — Project Memo

Working title: Draft Zero  
Date: 9 October 2026  
Status: Concept and architecture defined; initial implementation pending.

## 1. Game concept

Draft Zero is a single-player, browser-based engineering puzzle game about sustainable building renovation.

Inspiration:

- Project Highrise: Interactive 2D building sections.
- Caesar III: Scenarios with different restrictions, objectives and success ratings.
- Engineering puzzle games: Experimentation, optimization and multiple viable solutions.
- Skill progression: Technologies and configuration options unlocked through experience.

Core gameplay loop:

Inspect → Configure → Simulate → Diagnose → Revise → Submit

Players develop renovation plans under financial, technical, environmental and comfort constraints. They can repeatedly modify their plans and run simulations before submitting their final solution.

The game is a configuration puzzle, not a continuous construction or economic management simulator.

## 2. Measures and progression

Measures are parametrized rather than fixed upgrades:

- Insulation: Material (EPS, mineral wool, wood fibre, etc.) and thickness.
- Heating: Technology, installed capacity and eventually detailed control.
- PV: Module dimensions, nominal power and quantity.
- Inverters: Rated power and eventually string/electrical compatibility.
- Later: Storage, heat distribution, ventilation and flexibility.

Use human-readable YAML/CSV catalogs with physical properties, costs, embodied emissions and skill requirements.

Measures transform simulation inputs. Their actual consequences are calculated by the physical model, not hard-coded as bonuses.

XP rewards completed scenarios and milestones, unlocking additional technologies or configuration capabilities.

## 3. Shared scientific infrastructure: pexl

The existing `pexl.Project`, `pexl.Scenario` and generated `pexl.schema` remain the authoritative data model.

Reuse `scenario.v`, `scenario.meta`, `scenario.inn`, `scenario.out` and `scenario.timeseries`.

Avoid introducing a separate `BuildingSpec`, duplicated simulation variables, generic frameworks or large class hierarchies.

The game can maintain a renovation plan and graphical layout, but scientific quantities remain defined by pexl.

## 4. ClimTower refactor

ClimTower already contains prototype logic for generating 2D spatial building sections from PEExcel data.

Relevant functions include:

- `create_district()`
- `create_layout()`
- `add_spaces()`
- `update_adjacency()`
- `create_roof_spaces()`
- `add_pv()`

Decision: Extract and simplify this logic into pexl itself.

The resulting section is a deterministic, schematic visualization of a `pexl.Scenario`, not a separate physical building model.

Proposed functions:

- `section_from_scenario(scenario, seed=42)`
- `render_svg(section, style="architectural")`

Important requirements:

- Read variables through the current pexl schema.
- Maintain consistent usage areas.
- Generate stable semantic IDs for graphical elements.
- Separate inferred geometry from actual building data.
- Reuse spatial layouts when comparing scenarios.
- Remove old Pygame dependencies and hard-coded energy-demand calculations.
- Keep geometry generation separate from SVG rendering.

## 5. Visual design

SVG is the preferred initial representation.

The same generated geometry serves two purposes.

Professional pexl visualization: Clean architectural/CAD-inspired building sections, with building uses, technologies and energy overlays. Useful for notebooks, reports and potentially the existing Streamlit dashboard.

Draft Zero game: Hand-drawn architectural planning sheets, marker colors, sketch annotations, graphical interventions and know-how indicators.

Browser interactions use inline SVG, HTML/CSS and TypeScript, supporting tooltips, menus, configuration sliders, animations and audio.

The renderer and geometry generator remain reusable; game artwork and styling remain separate.

## 6. Repository architecture

Repository: `pexl`

Owns the scientific model, PEExcel schema, Excel IO, reusable spatial section generator, SVG renderer and future Python simulation.

Repository: `draft-zero` (working name)

Owns gameplay, renovation measures, level objectives, skill progression, scoring, browser interface, sketchboard artwork, sound and publishing.

Legacy repositories:

- ClimTower: Source for the spatial generation refactor.
- passyBuird: Source for the initial simplified Python building simulation.

Do not migrate their old game-state architectures wholesale.

## 7. Python simulation strategy

Long-term objective: Incrementally port PEExcel's calculations from Excel to Python inside pexl.

Start from the simplified hourly building simulation in passyBuird.

The same physical engine should ultimately support:

- Full-year simulation: 8760 hourly timesteps.
- Fast game simulation (candidate): Four representative seasonal weeks, 672 hours.

Benchmark the full-year model before introducing time reduction. Representative periods require weighting, initialization, peak-condition checks and validation against annual results.

Avoid developing a separate physics engine exclusively for the game.

## 8. Web distribution

Initial development: HTML/SVG/TypeScript frontend with a local Python/FastAPI simulation backend.

Potential publication: Pyodide running a compatible Python simulation subset locally in the browser, enabling static hosting without a permanent simulation server.

This remains an open technical decision pending performance and compatibility tests.

## 9. Immediate implementation milestone

M1: ClimTower → pexl spatial section generator and professional SVG.

Implementation tasks:

1. Inspect the current pexl schema, model and plotting infrastructure.
2. Identify and extract useful ClimTower spatial-generation logic.
3. Replace legacy Excel variable lookups with schema-backed scenario access.
4. Generate deterministic spatial layouts.
5. Implement a minimal professional SVG renderer.
6. Add tests for area conservation, reproducibility and SVG validity.
7. Demonstrate the functionality using an actual imported PEExcel scenario.

Out of scope for M1: Gameplay, XP, renovation measures, simulation refactoring, sound and comprehensive browser UI.

The first deliverable is a professional section generated from a real `pexl.Scenario`.

## 10. Development principles

- Simple Python functions and dictionaries where practical.
- Minimal dependencies and abstractions.
- Reuse existing interfaces before introducing new ones.
- One authoritative scientific variable schema.
- Distinguish inferred geometry from actual building information.
- Explicit units, assumptions and data provenance.
- Small, testable development milestones.
- Prioritize validating the core gameplay before developing an extensive game engine.

Overall strategy: Build reusable scientific and graphical functionality in pexl, then use it to create a distinctive and publishable renovation puzzle game.
