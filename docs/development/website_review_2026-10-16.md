# Website review and improvement plan

Review date: 16 October 2026. Scope: all 29 German pages and all 29 English counterparts, their Quarto sources, the published HTML, navigation, linked resources and relevant build/export code.

## Findings at a glance

- All **58 public pages returned HTTP 200**. The crawl checked **186 distinct HTTP(S) destinations** including page resources, downloads and external references. Internal page targets and HTML fragment anchors resolved.
- **Three URLs are confirmed broken by GET**, all currently linked from German pages: the development workbook, the publication notebook on GitHub, and the publication guide on GitHub. The English download page does not offer an equivalent direct workbook download at all.
- All **19 distinct image URLs used by page content** were reachable. Browser checks found the supplied images rendering. The missing-picture issue is primarily **omitted English illustrations and explicit placeholders for screenshots not yet supplied**, rather than missing image files. Dense screenshots still need a legibility pass at their intended reading size.
- All 58 pages were visited in the browser at a **1440 px desktop viewport** and checked for page-wide overflow at **390 px mobile width**. No desktop document overflow was detected. Seven mobile pages overflow because of tables; figures inside iframes may still clip even when the outer document fits.
- English is not consistently a translation of German: some pages are abbreviated, some omit procedures or resources, and several introduce conflicting technical instructions.
- Navbar labels are translated, but the active section is incorrect: the shared sidebar makes **Tool-Anwendung / Tool use** active across other sections. German home/examples omit the sidebar; their English counterparts include it. The language switch always returns to the other homepage.

The review combines source reading, HTTP/link and anchor checks, DOM/image inspection on every page, and selected visual inspection. It is not a workbook calculation audit or an exhaustive keyboard/screen-reader accessibility assessment. A 403 from a publisher is treated as an automated-access restriction, not proof of a broken publication link. The newsletter returned 404 to HEAD but **200 to GET** and is not classified as broken.

## Performance change implemented for this request

The only content change implemented as part of this review is the requested removal of automatically embedded interactive graphics:

- `examples.qmd` and `en/examples.qmd`: replace the four annual result iframes and seasonal F7 iframe with their **existing SVG exports**. The complete hourly F7 view remains an explicit link.
- `envelope.qmd`, `components.qmd` and their English counterparts: comment out the interactive section/catalogue iframes. Existing explanatory images remain; the interactive views are still available through explicit links.
- The original 16 iframe elements are retained in source comments for reversibility and do not create browser iframe elements. This is not CSS hiding.
- The six HTML charts formerly embedded per example page total **30,320,140 bytes**. The five reused SVGs total **227,730 bytes**. These are artifact sizes, not measured network-transfer timings; lazy loading and compression affect actual transfer. No Plotly runtime executes automatically through these removed embeds.
- Notebook reading views are unchanged: they are static documentation, not interactive graphs. The asset build still produces interactive exports for explicit links. Build-time optimization is a separate planned task.
- `notebooks/howto_website.ipynb` documents the temporary behavior, verification and reactivation using the existing Quarto build workflow.

No new figure format, persisted data schema, public Python API or parallel rendering implementation is introduced. The existing exports and QMD pages are reused.

Validation and release: `quarto render website` completed successfully for both sets of 29 pages. The six affected rendered pages contain no active chart/section iframe elements; both example pages contain five SVG images with valid local targets. Desktop and mobile visual checks confirm the static charts render (dense labels still require opening the full-size SVG on small screens). Published to the existing GitHub Pages site in `gh-pages` commit `44be7d7`; live GET checks on all six affected pages returned 200 and confirmed zero interactive embeds, with five SVG images on each example page. The remaining findings below are proposed work, not implemented fixes.

## Priority 1 — downloads and technical correctness

### 1. Restore download parity and correct the development URL

Evidence:

- [Current German development URL](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/excel/development/ka_PEQ_Nachweistool_dev.xlsb): GET **404**.
- [Repository filename with `DEV`](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/excel/development/ka_PEQ_Nachweistool_DEV.xlsb): GET **200**.
- `en/download.qmd` links to the repository homepage instead of providing stable and development workbook links. It also omits the PowerPoint and earlier tool-documentation download available in German.

Proposed change: provide matching stable/development rows, release notes and document downloads in both languages; preserve the exact case of repository filenames. Distinguish a fixed release download from a moving `master` workbook. Do not imply that a mutable branch URL is permanently the named release.

Acceptance: an anonymous visitor can reach both workbook files in either language; downloaded filenames, version labels and release destinations agree.

### 2. Resolve contradictory English technical instructions

- `hvac.qmd` describes the heating systems as a cascade; `en/hvac.qmd` says the numbers are not priority and tells readers not to infer an order. Verify against the current workbook/training and provide one consistent explanation of dispatch and capacity limits. The English wording must not override the documented cascade without evidence.
- `mobility.qmd` and both storage pages place EV charging parameters in **Mobilität**; `en/mobility.qmd` sends readers to **Flexibilität und Speicher** for charging/bidirectional operation. Confirm and use the correct worksheet and controls.
- German migration deliberately avoids an unverified export-button label; English specifies **Projekt-Datei exportieren** and attributes it to the training. Use only a verified label for the relevant version; retain the generic project-export step until verified.
- English guidance sometimes adds declaration obligations for whole system configurations, PV inputs or flexibility capacities beyond the specific declaration-value principle. Check each obligation against the applicable method; do not turn an example configuration into a declaration requirement.

Acceptance: the same technical meaning, workbook locations, constraints and uncertainty apply in both languages. Cross-check with the German technical source and current workbook, not only with machine translation.

### 3. Make the Python instructions executable and reachable

- [Publication notebook on `master`](https://github.com/simonschaluppe/peexcel/blob/master/notebooks/howto_publication.ipynb): GET **404**.
- [Publication guide on `master`](https://github.com/simonschaluppe/peexcel/blob/master/docs/development/publication.md): GET **404**.
- Both files exist locally; the local source branch is four commits ahead of `origin/master`. Published output and public source documentation are therefore out of sync.
- `en/python.qmd` calls `export_figure(..., formats=(...))`. The implementation in `src/pexl/plot/export.py` has no `formats` argument; it requires `provenance` and a filename with `.html`, `.svg`, `.png` or `.pdf` suffix. Its example data path is also a placeholder.
- English Python/dashboard pages omit the concrete install/run commands provided in German; the English page refers to embedded notebook views that it does not actually contain.

Proposed change: use the existing executable publication notebook as the source of the example, provide a real example export or clearly identified user-supplied path, and publish reviewed source changes. Alternatively use the already published notebook download where appropriate. Mirror installation, Streamlit launch and notebook access in both languages.

Acceptance: the documented snippet runs with the current package and declared dependencies, and every referenced source/download is publicly reachable.

## Priority 2 — navigation, bilingual completeness and layout

1. **Navigation:** keep both language trees structurally equivalent. Use Quarto's existing sidebar configuration to associate the main sections correctly, rather than adding a second JavaScript navigation system. Choose an intentional common layout for home/examples. Preserve the current page when switching languages; fall back to the homepage only where no counterpart exists.
2. **Excel control names:** retain the exact German workbook text inside `.excel-menu`, `.excel-action` and `.excel-field`; put English explanations alongside it. Examples currently translated incorrectly for lookup include `Weather`, `District`, `Save Current Inputs / Variants`, `Variant Comparison`, `Use Signal`, and `Results`. Unify icons and colors, including the different Scen badge color.
3. **English content parity:** restore the worksheet navigator, publication list, download choices, loading variants, declaration-sheet locations, source-document map, contact/newsletter/use information and executable application instructions. Translation can be idiomatic, but must not remove operational steps or introduce new controls.
4. **Mobile tables:** apply the existing `.table-responsive` wrapper to the actual rendered tables or improve wrapping of long labels. The class is defined in CSS but the overflowing tables have no responsive wrapper. Keep any necessary horizontal scrolling inside the table rather than across the whole document.
5. **Figures:** keep the supplied originals and lightbox. Add clearly captioned detail views for dense diagrams; distinguish German original labels from English explanatory text. English currently omits `media/mobility.png` and the research illustration, while both assets are available. Do not substitute old handbook graphics.
6. **Citations:** reconcile slide references against the current training PDF. Examples of divergent references include comparison (German 33, English 30), migration, PV and presets/navigation. Retain source dates and version notes; do not copy a slide number without checking its topic.

Measured mobile document widths at a 390 px viewport:

| Page | Document width | Source |
|---|---:|---|
| German model | 406 px | Workflow table |
| German examples | 517 px | Variant/settings table |
| German declaration | 472 px | Modelling/declaration comparison table |
| German learn | 422 px | Training-source map |
| German glossary | 407 px | Glossary table |
| German about | 409 px | Repository-directory table |
| English examples | 439 px | Variant/settings table |

Acceptance: no document-wide horizontal scroll at 390 px; meaningful current-section highlighting; equivalent language navigation; no untranslated substitute for an actual German Excel control name.

## Page-by-page inventory

Every row covers the German page and its `en/` counterpart. Shared navigation issues above apply across the inventory; “aligned” means no additional content defect was found in this review, not certification of the underlying calculation method.

| Page | Findings and proposed improvement | Priority |
|---|---|---|
| `index` | Both main images load. German uses full width/no sidebar; English has a sidebar and different action links. Align layout, level descriptions and action destinations; explain that some illustrations retain German labels. | P2 |
| `start` | Core workflow and Quick Start image align. English omits Windows unblock guidance and translates the Excel recalculation menu despite the German UI. Preserve the German control path with English explanation. | P2 |
| `presets` | Workflow and supplied preset diagram align. English translates a field name inside the control marker. Keep exact field labels; provide a readable detail view of the existing full-slide image. | P2 |
| `excel-navigation` | English omits the complete worksheet-to-page navigator. Its caption describes the overview mosaic as a readable input screenshot; German correctly says it is only a spatial overview. Restore the table and caption meaning. | P2 |
| `migration` | Export label is unverified in German but asserted in English. Align the workflow and preserve checks for custom weather/PV data. Export/import screenshots and compatibility details remain outstanding. | P1 |
| `download` | German development link has wrong filename case; English omits stable/dev direct links, release distinction, PowerPoint and earlier documentation. Align both tables. | P1 |
| `model` | Content and energy-model image largely align. German workflow table overflows on mobile. Correct active navbar section and improve table wrapping. | P2 |
| `envelope` | Thermal model image loads in both languages. Interactive embed removed for this request. Move renderer/style implementation language to developer documentation; keep engineering boundaries and link-only interactive explanation clear. | P2 |
| `components` | Original component image loads in both languages. Interactive embed removed. Match the “selector” wording to the separately opened catalogue; retain thermal versus LCA boundary distinction. | P2 |
| `hvac` | Heating-dispatch contradiction; English abbreviates capacity/operating-period checks and differs in references/icons. Current H/K/WW/L detail screenshots are still missing. Resolve technical meaning before expanding prose. | P1 |
| `pv` | Both input modes described, but detail/citations differ. Current roof-scaling and hourly-profile controls are not illustrated. Align German control labels and identify which parameters are actually declaration values. | P2 |
| `systems` | Main explanations and both diagrams align. English uses `Use Signal` instead of the actual German field label. Interactive behavior referenced here belongs to Excel and should remain distinguished from the website's static view. | P2 |
| `usage` | English omits the explicit input-group table and screenshot placeholder; introduces occupancy/schedule wording needing control-level verification. Restore common coverage and exact worksheet labels. | P2 |
| `interfaces` | English omits the energy-certificate workflow, Eco2soft cross-reference and export/schema distinction. `Weather` is not the German worksheet label. Restore equivalent input paths and version notes. | P2 |
| `mobility` | English loses the distinction between physical charging and attributed mobility, omits the larger mobility diagram, and gives a conflicting EV-control location. Resolve location and restore the boundary explanation. | P1 |
| `climate` | Three images and the important PV-LCA exclusion align. Preserve the cumulative/annual and BGF/NGF distinctions. Eco2soft import screenshot remains missing; make the English operation block consistent with German. | P2 |
| `variants` | English replaces real ribbon labels with translated pseudo-labels and does not explain loading a saved variant as clearly as German. Restore create/save/load/overwrite workflow; current manager image outstanding. | P1 |
| `results` | Both pages correctly describe Erg separately from OUT and the Dashboard, but neither contains the promised detailed result-sheet images. Request current Excel screenshots for all four balances; do not insert Python charts as Excel output. | P2 |
| `excel-dashboard` | Both supplied diagrams load; sequence and distinctions largely align. Add detail views for date selection and each chart so axes/legend are readable, and preserve the German explanation of date-window versus hourly aggregation. | P2 |
| `comparison` | Image loads. English loses the real `var`/Vergleich location and changes the training reference from 33 to 30. Restore control labels and equivalent selection steps. | P2 |
| `batch` | English omits the German Simulieren/check/confirmation sequence; Scen badge color differs. German source numbering repeats 4. Reconcile with current controls and obtain Scen/status screenshots. | P2 |
| `examples` | Six heavy chart embeds per language; removed for this request, five existing SVGs substituted. German/English layout differs, mobile settings table overflows, shared chart labels are German, and provenance footer is dense. Keep chart language explicit; put readable provenance near a table/download rather than making the chart footer carry all narrative. | P1 performance; P2 layout |
| `declaration` | English omits the PEQ/PEQ+M/KN PEQ sheet locations and detailed modelling-versus-declaration table. German table overflows on mobile. Restore parity and obtain current AUDIT/declaration-sheet images. | P2 |
| `learn` | English omits the source-slide map and several task links, and presents itself more as a summary. German source map overflows on mobile. Align task-oriented entry points and evidence references. | P2 |
| `python` | Two confirmed public-source 404s. English export call is incompatible with current API; installation/publication notebook and actual reading views missing. Repair using existing notebook functions/examples. | P1 |
| `dashboard` | German has installation/Streamlit commands; English links elsewhere without equivalent runnable instructions. Mirror the commands and clarify local runtime. Update wording to reflect static website previews and optional HTML charts. | P1 usability |
| `glossary` | The two tables contain different term sets. German lacks BGF/NGF/SOC entries found in English; English lacks several boundary/factor terms. Create equivalent coverage and clarify SIM2 calculation sheet versus exported timeseries. German table overflows. | P2 |
| `research` | English omits all six publications, the standard link and the research illustration. Restore the bibliography. Four publisher destinations block automated requests with 403; manually verify them rather than treating them as confirmed failures. | P1 completeness |
| `about` | English omits named contact, direct issues link, newsletter, repository map and use/license context. German map overflows. Newsletter works with GET. Refer to an actual license/use source rather than leaving generic wording unsupported. | P2 |

## Required current Excel screenshots

These are missing source material, not broken image URLs. Use screenshots from the current tool version, with version and context recorded:

1. **Erg:** heat balance, end-energy matrix, primary-energy balance and THG balance.
2. **Variants/migration:** project and variant selection, save/load/overwrite, project export, import and completion message.
3. **Scen:** scenario selection, Simulieren, validation/time estimate, confirmation and completion/error status.
4. **PV / PV-Import:** roof-area scaling, hourly profile layout and profile selection.
5. **H / K / WW / L:** the principal input blocks and active-system/capacity settings.
6. **Nutzungsparameter:** input groups and visible declaration-value marking.
7. **THG / Eco2soft:** import dialog and field assignment; **AUDIT** and the three declaration sheets.

The current supplied Dashboard, preset and method illustrations can be retained. Detail crops should preserve captions, units and enough surrounding Excel context to identify the control; do not invent cell addresses.

## Delivery sequence and acceptance

1. **Now:** verify and publish only the requested static-preview/performance change. Keep the remaining issues as this review plan.
2. **First corrective pass:** fix download parity/case, the two source links, Python API example and the HVAC/mobility/migration/variant-label inconsistencies. Validate public links with GET and execute the documented Python workflow through the existing how-to notebook.
3. **Navigation and translation pass:** restore equivalent page content, bibliography and exact Excel names; implement correct active-section behavior and counterpart language switching in the existing Quarto configuration. Check each of the 29 pairs against a common topic checklist.
4. **Visual pass:** integrate current screenshots, improve readable detail views and mobile tables. Verify all pages at desktop and 390 px, with keyboard navigation/lightbox checks on representative pages.
5. **Build/release pass:** preserve a reproducible reviewed source state corresponding to the published site. Separate expensive asset regeneration from text-only preview; reuse existing scripts and exports, and only regenerate figures when inputs/code/config change. Keep the explicit interactive links while embeds are disabled. Consider on-demand loading and a shared Plotly bundle only if interactivity is later reintroduced.

Before the corrective pass is released: all main pages and direct downloads respond successfully; no broken internal anchors; all figures render; both languages have equivalent operational coverage; examples execute; no whole-page horizontal overflow at 390 px; no automatic interactive-chart requests on the three affected page types. Publisher access restrictions are documented separately from confirmed broken links.

Maintainability: reuse `_quarto.yml`, existing page pairs, CSS classes, export functions and `howto_website.ipynb`. No translation database or second download registry is needed for this pass. If future duplication warrants a shared include, keep it within the existing Quarto source mechanism and document how each language is generated and checked.
