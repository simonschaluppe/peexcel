# Changelog

All notable changes to PEExcel / klimaaktiv Nachweistool should be documented in this file.

This changelog was reconstructed from the public GitHub commit history and milestone history. Entries before a formal Git tag/release workflow are therefore grouped by visible version commits, milestone descriptions, issue references, and commit-message clusters. Future entries should be maintained manually at release time.

The format follows a lightweight `Added / Changed / Fixed / Compatibility / Notes` structure.

## [Unreleased]

### Added

### Changed

### Fixed

### Compatibility

### Notes

---

## [v1.12.7] - 2026-07-08

### Added

- Extended the life-cycle assessment model from the previous coarse component model to a detailed component structure with 20 differentiated building components.
- Added an extensive construction/component catalogue based on baubook.at data.
- Added example construction assemblies as selectable presets.
- Added new preset navigation for faster and clearer selection of predefined input configurations.
- Added preset recording for tabular presets: applying a preset from a `Presets_XXX_table` can record the selected preset name to a corresponding IN named range.
- Added logic to check whether recorded preset variables still match the selected preset when saving a scenario; non-matching preset recordings can be cleared.
- Added new THG/LCA named ranges and outputs for the extended component model.
- Added or updated LCA handling for PV-related inputs, calculations, and outputs.
- Added deployment support for dry-run style checks/logging during release preparation.
- Added schema export file `schema_v1_12_7.xlsx` for Python translation.
- Updated/generated the Python schema wrapper to schema version `1_12_7`.
- Added new ribbon callbacks for preset loading.

### Changed

- Migrated HVAC examples to the new `LCA_Komponenten` structure.
- Updated LCA input lines in `IN` and corresponding output/recording logic in `OUT`.
- Renamed or duplicated selected GWP outputs to preserve legacy outputs while supporting the new output structure.
- Updated deployment behavior so `var_name` handling in the `IN` table is reviewed/updated during deploy.
- Improved diagrams and release-oriented workbook cleanup.
- Updated documentation and release notes for the new LCA model and preset workflow.

### Fixed

- Fixed ribbon toggles related to the updated preset workflow.
- Fixed or closed compatibility issues related to old names in the workbook.
- Fixed/check-closed the heating power limitation issue (`Heizleistungsbeschränkung greift nicht`).
- Closed release test/deploy issues for the `v1.12.7` milestone.

### Compatibility

- This release changes the life-cycle assessment input and output model substantially.
- Existing project files may require review of LCA component mappings after import.
- The rowwise `var_name` importer should reduce sensitivity to row order changes, but semantic changes to variables, renamed outputs, and new component structures still require migration awareness.
- Legacy GWP outputs were renamed/duplicated where possible to reduce disruption.

### Notes

- Milestone `v1.12.7` was completed before release and contained 15 closed issues.
- Main release themes: detailed LCA model, baubook-based component presets, preset navigation, compatibility checks, updated Python schema.

---

## [v1.11.x] - 2026-04 to 2026-05

### Added

- Added semantic metadata to the schema and/or schema-generation workflow.
- Added generated Python schema module `excel_v1_11_5`.
- Added additional explanation and step-by-step documentation to `howto_schema`.
- Added type-related structures and schema support.
- Added preliminary or extended LCA calculation work.
- Added baubook import/export or data-handling groundwork.

### Changed

- Refactored the model and schema tooling.
- Improved schema explanations and schema-use notebooks.
- Updated output schema and documentation.
- Continued cleanup of the Python wrapper and schema-generation pipeline.
- Introduced or refined `Scenario`, `District`, and `Usage` abstractions in the Python side.
- Continued repository cleanup and renaming/housekeeping of schema-related files.

### Fixed

- Fixed wrong caching behavior in schema/model calculation code, with remaining performance caveats noted in the commit history.
- Improved import and loading speed.
- Fixed naming and input-version issues around the transition to newer schema versions.

### Compatibility

- Schema `v1_11_5` indicates a structured schema/codegen checkpoint.
- Some schema and metadata changes may affect generated Python wrappers and downstream code using older schema assumptions.

---

## [v1.10.x] - 2026-02 to 2026-04

### Added

- Added `v1.10` release checkpoint.
- Added `v1.10_4` schema checkpoint.
- Added rowwise / name-based import capability for more robust imports across changing row order.
- Added type preset selection.
- Added TSD export, including use in scenario batches.
- Added early LCA structures and prepared table preset foundations.
- Added or improved scenario definitions and typology import structures.
- Added Energieausweis data import groundwork.
- Added `SIM2` to schema export.

### Changed

- Reworked import logic toward named/range-based mapping instead of relying on fragile row positions.
- Removed or prepared removal of old input structures.
- Updated schema reporting so schema checks can report errors more clearly.
- Improved variable screen handling.
- Continued GHG update work.
- Updated README and user-facing documentation.

### Fixed

- Fixed naming issue associated with input version 2.
- Fixed issues around OIB/line-related or formula-related checks referenced in issue history.
- Fixed missing named ranges and missing plugs during schema/input evolution.
- Fixed copy-table VBA behavior when using different source files.

### Compatibility

- `v1.10` is an important compatibility boundary because the rowwise/name-based importer starts reducing dependence on input row order.
- Scenario and schema files from older versions should be imported through the newer mapping/import path rather than by assuming row alignment.

---

## [v1.09] - 2026-02

### Added

- Added clean `v1.09` deployment checkpoint.
- Added deployment/cleanup work around the public workbook.
- Added continued scenario and preset handling improvements.

### Changed

- Removed old tool sheets from the workbook.
- Cleaned up default settings and workbook state.
- Prepared the workbook for a cleaner stable/development split.

### Fixed

- Fixed missing plug-related items.
- Fixed diagram and workbook bugs before deployment.

### Compatibility

- Workbook cleanup may affect workflows that relied on old/legacy sheets.

---

## [v1.08] - 2025-12 to 2026-01

### Added

- Added schema `v1.08` checkpoint.
- Added SIM formulas to schema export.
- Added basic schema validation.
- Added CSV conversion/normalization utilities.
- Added converter updates.
- Added `SIM2` handling in schema export.

### Changed

- Refactored repository and schema-support code.
- Updated support documentation.
- Cleaned up schema and export tooling.

### Fixed

- Fixed variable-name issue to restore functionality.

### Compatibility

- Schema export became more complete and suitable for automated validation/code generation.

---

## [v1.07] - 2025-12

### Added

- Added/refined `v1.07` release checkpoint.
- Added TRUE/FALSE UI checkboxes for toggles.
- Added or exposed additional domestic hot water (`WW`) parameters in the UI and `IN` sheet.

### Changed

- Replaced earlier simple/dumb checkboxes with VBA-backed linked checkboxes.
- Improved result-sheet typography by changing hyphens to en dashes.
- Applied minor formatting changes.

### Fixed

- Fixed checkbox-related bugs.
- Fixed input value loading when values were not written to the expected reference cell.

### Compatibility

- UI checkbox behavior changed; old workbook interaction assumptions may no longer apply directly.

---

## [v1.06] - 2025-11

### Added

- Added/refined `v1.06` release checkpoint.
- Added diagram formatting improvements.
- Added fixes for mobile shading system behavior.
- Added or updated documentation.

### Changed

- Continued workbook formatting and cleanup.
- Applied minor fixes and documentation updates.

### Fixed

- Fixed splashscreen-related issue.

---

## [v1.05] - 2025-09 to 2025-10

### Added

- Added/refined `v1.05` release checkpoint.
- Added DEV workbook version for active development.
- Added deployment workflow from DEV workbook to release workbook via deploy macro.
- Added initial PV implementation and PV import work.
- Added detailed end-energy demand output/pivot improvements.
- Added two mobility input modes:
  - simple mode (`Vereinfacht`) using an optimized region variant with fewer inputs,
  - detailed mode (`Detailliert`) with explicit mobility inputs.
- Added or updated regional/community data files.

### Changed

- Switched cooling energy balance signs for consistency.
- Updated summer/winter balance representation.
- Updated heat recovery representations.
- Updated DHW auxiliary electricity handling.
- Updated README and public-facing repository information.

### Fixed

- Fixed DHW2 calculation issues.
- Fixed end-energy demand pivot view.
- Fixed geometry shading default values.
- Fixed double application of `mob_pkm_factor` in mobility calculations.
- Fixed `fc` shading/g-value behavior.

### Compatibility

- Introduction of the DEV/release workbook split is an important workflow boundary.
- Cooling balance sign changes may affect comparison with older outputs.
- Mobility calculation fixes may change mobility results compared with prior versions.

---

## [v1.02 and early 2025 development] - 2025-06 to 2025-08

### Added

- Added early `v1.02` release checkpoint.
- Added examples.
- Added splashscreen.
- Added weather to project export.
- Added transposed version-comparison tab.
- Added summer/winter heat-balance work.
- Added mobility-related calculation structures.
- Added THG/GHG balance structures.
- Added GWP/carbon pathway handling.
- Added GWP waterfall diagram.
- Added first scenario/batch-scenario drafts.
- Added predefined construction/component catalogue groundwork.
- Added support documentation and README updates.
- Added publication/support material updates.

### Changed

- Improved GWP diagrams and early scenario outputs.
- Updated handbook files and later removed obsolete handbook source files.
- Changed paths and repository structure during early consolidation.

### Fixed

- Fixed default value overrides.
- Fixed CO2/GHG balancing issues.
- Fixed import/export balance representation for GHG balance.
- Fixed summer/winter energy balance.
- Fixed EV final-energy calculation.
- Fixed battery discharging during signal hours before signal use.
- Fixed winter heat balance for uncooled cases.

### Compatibility

- This period predates the more formal schema/release workflow. Results from these versions should be treated as early-development outputs unless reproduced in a later stable version.

---

## Source reconstruction notes

- The repository did not yet have formal GitHub Releases at the time this changelog was reconstructed.
- Version boundaries are inferred from explicit version commits such as `v1.12.7`, `v1.11`, `v1.10`, `v1.09`, `v1.08`, `v1.07`, `v1.06`, `v1.05`, and `v1.02`, plus the `v1.12.7` milestone description.
- Some historic commit messages are terse (`cleanup`, `works`, `save`, `predeploy`). Those were not expanded beyond what could be safely inferred from adjacent commits and milestone context.
- Future releases should update this file manually before tagging the release.

