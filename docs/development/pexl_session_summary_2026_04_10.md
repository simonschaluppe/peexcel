# PEXL session summary

## Core reframing
The main problem is not primarily plotting or query-object design. It is a **scenario audit and comparison** problem with three related layers:

1. **Comparison layer**
   - high-priority curated comparison for `primary_energy_balance` and `ghg_balance`
2. **Diagnostics layer**
   - explain suspicious result differences through input differences
   - example: unexpectedly high `QT` should lead to likely relevant input differences
3. **Scenario lineage layer**
   - base scenario -> derived scenarios / branches
   - explicit parent-child relationships are missing in Excel today

## Public Python API direction
The desired public API should be **discoverable and family-first**, mainly through autocomplete on `Scenario`, `District`, and `Project`.

Preferred style:
- `district.heat_balance()`
- `district.primary_energy_balance()`
- `district.ghg_balance()`

These should mean the same family across all scopes:
- `Scenario` -> one scenario
- `District` -> all district scenarios
- `Project` -> all project scenarios

The main value of the call is:
- semantic discoverability
- stable downstream contract for dataframe + plotting/reporting

## Important architectural insight
The key design problem is not "ScenarioView vs VariableSelection".
It is defining a stable **producer-consumer contract** for named result families.

Useful framing:
- `district.primary_energy_balance()` produces a stable family-shaped result
- `pexl.plot.primary_energy_balance(...)` consumes that contract

This suggests:
- family-first public methods
- plotting/reporting built on top of the family contract
- generic metadata selection only as secondary/internal machinery

## Result-family direction
For now, do **not** overengineer a formal spec system for every family.
A lightweight path is enough:

- `scenario.primary_energy_balance()` / `district.primary_energy_balance()` / `project.primary_energy_balance()`
- `scenario.ghg_balance()` / `district.ghg_balance()` / `project.ghg_balance()`
- plotting as external functions:
  - `pexl.plot.primary_energy_balance(obj)`
  - `pexl.plot.ghg_balance(obj)`

This keeps notebook prototyping easy for coworkers and allows later extraction into library code.

## Dataframe / result contract
The important contract is between:
- the family-producing methods, and
- plotting / reporting / diff consumers

For comparison workflows, the natural default remains **wide tables**, because this matches Excel and scenario-column thinking.

Likely default shape:
- metadata columns first, minimally:
  - `var_name`
  - `label_de`
  - `unit`
- then one column per scenario

## Heat balance conclusion
Heat balance plotting exists, but it is **not the main comparison priority**.
The most important comparison families are:
- `primary_energy_balance`
- `ghg_balance`

Heat balance remains useful more for:
- finding anomalies
- validating assumptions
- tracing causes

## Bigger problem discovered: hidden scenario drift
The central operational problem is that users copy old Excel projects and silently inherit non-obvious assumptions.
Typical risky examples:
- special usage scalings
- mobility options
- declaration-related variables
- detailed HVAC assumptions

This causes:
- hidden inherited inputs
- invisible drift from defaults or declaration values
- no clear provenance of why a value differs
- poor diagnosis from surprising results back to changed inputs

## Better framing of the overall problem
This is best framed as a **scenario audit and governance** problem.

PEXL / Excel should help answer:
- which inputs differ from default?
- which declaration-relevant inputs differ from required values?
- which inputs differ from the parent / baseline scenario?
- which of those differences are high-risk?
- which result anomalies are likely caused by which input differences?

## Excel-side implications
This is not only a Python-wrapper problem. The Excel model itself should better support auditability.

Most important Excel-side ideas identified:
- keep `IN` as source of truth
- add explicit audit/reference concepts rather than hiding logic
- use a separate `AUDIT` sheet rather than overloading the main input sheets

Promising additions in / around `IN`:
- explicit declaration reference values for the small subset where relevant
- audit classification / risk grouping for important rows
- explicit parent/baseline scenario metadata
- boolean flags such as:
  - changed from default
  - changed from declaration reference
  - changed from parent/baseline
  - high-risk change

## IN table conclusion
The current IN table already contains a lot of rich metadata. It likely does **not** need a full redesign.
The main missing pieces are:
- clearer reference states
- explicit audit/risk classes
- explicit parent scenario / baseline information

Most valuable Excel-side additions identified:
1. `audit_class` (for example `normal`, `expert`, `declaration`, `mobility`, `hvac_core`)
2. `decl_ref` for the relatively small declaration-controlled subset
3. explicit scenario parentage / baseline metadata
4. audit flags derived from those references

## Preset / user-intent problem
Another structural problem is that many users cannot meaningfully set detailed technical inputs and instead rely on domain presets.

The current design choice — storing **all resolved first-class variables in IN** rather than only a preset key — was identified as **the correct direction**.

Why this is good:
- projects store explicit truth
- scenarios remain diffable and exportable
- preset-table drift cannot silently change project meaning
- version migration is safer than with hidden lookup semantics

## Remaining preset problem
What is missing is not the resolved explicit inputs, but the representation of **user intent / preset provenance**.

A useful conceptual split:
1. **intent**
   - what user selected, e.g. `heating_preset_name = "WP effizient"`
2. **resolved state**
   - actual IN values after preset application
3. **match status**
   - whether the current resolved values still match the preset exactly or have been manually modified

## Recommended preset direction
Add a **small number of explicit IN variables per presettable group**, not row-wise provenance for every variable.

Example for heating:
- `heating_preset_name`
- `heating_preset_version`
- `heating_preset_match_status`
- optionally `heating_preset_scope`

Important principle:
- presets are **authoring shortcuts / bulk-edit tools**
- resolved IN variables remain the **stored project truth**

This should later support:
- diffing against preset expectations
- export/import of preset provenance
- sidecars and schema integration
- clearer user orientation on input sheets

## Long-term preset structure
The likely long-term direction is **tabular presets**:
- rows = relevant `var_name`s
- columns = available preset names
- optionally grouped by scope

That would map distinct subspaces of the IN variable space, instead of creating hidden lookup semantics.

## Immediate practical technical direction for presets
The best technical storage location for preset provenance is explicit IN variables.
Do **not** store provenance only in VBA or comments.
Do **not** add row-wise provenance columns for every variable yet.

Minimal first step:
- `heating_preset_name`
- `cooling_preset_name`
- `dhw_preset_name`
- `mobility_preset_name`

Later extend with:
- version
- match status

## Main strategic conclusion
The session shifted the framing from:
- plotting API design
- query/view abstraction debates

toward:
- scenario audit and governance
- result-family contracts for comparison
- explicit reference states in Excel
- preset intent + resolved truth + match status

## Recommended near-term priorities
1. Prioritize curated comparison support for:
   - `primary_energy_balance`
   - `ghg_balance`
2. Design a lightweight family contract for producer -> plot/report consumer
3. Improve Excel auditability with explicit references and risk classes
4. Add explicit parent/baseline scenario metadata
5. Add preset provenance variables for major presettable groups
6. Treat heat balance mainly as a diagnostic family, not the primary comparison product

## Candidate future feature areas
- input audit against default / declaration / parent
- result diffs across scenarios
- diagnosis from result anomaly to likely input causes
- scenario tree / lineage visualization
- preset match / drift reporting

