# Bestandsprüfung der Website- und Hilfsskripte

Stand: 29.10.2026. Statische Quellcode- und Aufruferprüfung, keine Laufzeitabnahme.
**Dieser Audit ist eine Bestandsaufnahme, kein zweiter Umsetzungsplan.** Maßgeblich
ist ausschließlich der [konsolidierte Arbeitsplan](website_layout_refactor_plan.md).
Frühere Vorgaben zur Anzahl verbleibender Skripte, pauschalen Löschung, neuen
Viewerarchitektur und Notebook-Versionierung sind zurückgenommen. Die folgenden
Zielorte sind Prüfkandidaten; nur der dort begrenzte Plotly-Schritt ist jetzt geplant.

## Umfang und Maßstab

Ein Verzeichnis `website/scripts/` gibt es im geprüften Stand nicht. Geprüft wurden
alle zwölf Dateien unter `scripts/` (zehn Pythondateien, PowerShell und HTML), die
eigenen Browserdateien `website/output-catalog.js` und `website/_resize.html`,
eingebettetes JavaScript sowie relevante Paketfunktionen, Aufrufer und Tests.
Generierte Assets, Downloads, Quarto-Ausgaben und fremde JS-Bibliotheken zählen
nicht als eigene gepflegte Implementierungen. Notebookzellen wurden auf Aufrufer
geprüft; gespeicherte Binär-/HTML-Ausgaben ersetzen keinen Ausführungsnachweis.
Es wurden keine Simulation, Notebookausführung, Hypothesis-Abfrage oder
Veröffentlichung durchgeführt und keine Zugangsdaten gelesen.

Wiederverwendbare Fachlogik gehört in vorhandene `pexl`-Module. Konkrete
Beispielauswahl, redaktionelle Aussagen, Screenshotkoordinaten und Seitenlayout
sind dagegen keine allgemeine Fach-API. Pandas, Plotly, openpyxl und Quarto sollen
ihre vorhandenen Aufgaben übernehmen. Browserereignisse benötigen bei einer
statischen Offline-Seite Browsercode; dessen Ablage unter `scripts/` ist jedoch
nicht technisch notwendig. Weniger doppelte Implementierung ist das Ziel, keine
willkürliche Dateianzahl und kein neues Modul pro Hilfsfunktion.

## 1. `scripts/website_assets.py`

**Heute:** `build(output)` kopiert freigegebene Dokumente, Bilder und Logo, erzeugt
Lehrmodule, Kataloge und Quick-Check, bereitet Notebook-Downloads und Redirects vor.
`prepare_assessment` kopiert separat ein Tutorial. Mehrere Downloadschleifen und
historische Notebookbehandlungen überschneiden sich. Nur der CLI-Block ruft danach
`website_examples.build()` auf; Import und CLI haben verschiedene Wirkungen.

**Einordnung:** Bereitstellung ausgewählter Website-Dateien ist eine begründete
Website-Aufgabe: Das Paket kennt weder Menüziele noch öffentliche Downloadauswahl.
Fachberechnungen gehören nicht hierher. Der heutige Sammeleinstieg vermischt aber
billiges Kopieren mit teurer Erzeugung. Er ist deshalb keine sinnvolle Pflicht vor
jedem Preview. Quarto-Hooks sind aktuell deaktiviert.

**Später prüfen:** Überlappende Kopier-/Redirectpfade bündeln und Erzeugung explizit
ansprechbar halten. Kein neuer Universal-Orchestrator als Voraussetzung des
Plotly-Schritts. Aufrufer in Website-How-to und Tests vor Änderungen berücksichtigen.

## 2. `scripts/website_examples.py`

**Heute, nach Funktionsgruppen:**

- `configuration`, `_read`, `load_entry`, `load_examples`: konkrete YAML-Auswahl,
  Dateiprüfung, gecachtes Einlesen und Auswahl genau eines Beispielszenarios.
- `numeric_frame`: benötigte Kanäle und endliche numerische Werte prüfen.
- `hourly_frame`: Stundenachse, Sortierung, Eindeutigkeit, Lücken sowie Monats-/
  Stundenfelder prüfen. Fehlende Daten werden nicht als Null ersetzt.
- `annual_reports`: native Reportmaterialisierung plus Annahmen der konkreten
  rein elektrischen Beispiele, Modellversion und PV-LCA-Prüfung.
- `balance_checks`: Deckung/Bedarf und THG-Summen prüfen; PE ist keine pauschale
  Nullabschlussprüfung.
- `input_differences`: Variantenvergleich mit festem Schema-CSV-Pfad.
- `flow_inventory`: vorhandene Kanäle, Gruppen, Summen und Stunden mit Werten;
  fehlende Kanäle bleiben von vorhandenen Nullwerten unterscheidbar.
- `dynamic_figures`: Saisonmittel und Stundenbilanz, native Renderer, aber eigene
  Profilaufbereitung, F7-Titel, Januar-/Juli-Zeitauswahl, Slider und große Ränder.
- `provenance`, `build`: Herkunft/Hashes, HTML-/SVG-/PNG-Exporte, CSV und Tabellen.

**Einordnung:** Dateiauswahl, freigegebene Modellstände und Assetnamen sind legitime
redaktionelle Rezepte. Stundenprüfung, Kanalbestand und Profilfiguren sind dagegen
auch im normalen Notebook nützlich und sollen keine Website-Konfiguration benötigen.

**Im ersten Schritt:** Wiederverwendbare Teile mit `analysis/temporal.py` und
`plot/electricity_balance.py` bündeln. Vorhandene DataFrames und Plotly-Figuren
beibehalten, keine zweite Implementierung im Skript. Konkrete Beispielannahmen
nicht als universelle Fachregel in die Bibliothek übernehmen.

## 3. `scripts/assessment_explained.py`

**Heute:** `_analysis_templates` serialisiert native Diagramme und Trace-Bindungen;
`_clean` behandelt nichtendliche Werte. `context_values` berechnet Dichte-/FSI-,
Sanierungs- und PEI-Kontextfortschreibungen unter Erhalt der Originalwerte.
`browser_data` erzeugt Szenarioauswahl, PE/GWP-Reports, kompakte Matrix, Einheiten,
Filter und Defaults; manche Defaults hängen von deutschen Namen ab. `build` liest
Projekt und Notebookprosa, bindet HTML-Vorlage, Plotly-JS und Daten ein und schreibt
einen eigenständig nutzbaren Quick-Check.

`publish_notebook` ist daneben ein eigener nbconvert-Pfad für ein anderes Tutorial:
Plotly-MIME wird in HTML umgebaut und lokale iframe-Pfade werden ersetzt.

**Einordnung:** Drei Aufgaben sind vermischt: Fachbewertung, interaktiver Export,
Website-Veröffentlichung. `analysis/targets.py` enthält bereits Zielkurven, aber
nicht die vollständige Kontextfortschreibung. Einzelfigurenexport ersetzt den
Mehrdiagramm-Viewer nicht. Das rechtfertigt eine spätere Prüfung, nicht automatisch
ein neues öffentliches Viewer-Modul. Websiteprosa und Veröffentlichung bleiben
redaktionell. Sonderexport und direkte Quarto-Tutorials auf tatsächliche Aufrufer
prüfen, bevor einer entfernt wird. Außerhalb des ersten Plotly-Schritts.

## 4. `scripts/assessment_explained.html`

**Heute:** Eigenständige Offline-Oberfläche mit Filtern, Auswahl, Kontextfeldern,
Legenden, Renderplanung und Auswahl-Download. `compose` und `composeAnalysis`
befüllen native Diagrammvorlagen. `composeLarge` verwendet bei großen Auswahlen
ScatterGL-Linien; das ist mehr als eine reine CSS-Anpassung. `contextValues`
implementiert Kontextformeln zusätzlich zur Pythonfunktion.

**Einordnung:** Ereignisse, DOM-Zustand und Darstellungsaktualisierung sind im
Browser begründet, dafür muss Excel nicht neu eingelesen werden. Die doppelte
Fachformel braucht dagegen eine bewusste Entscheidung und verbindliche
Python-/JS-Vergleiche. Bestehende optionale Tests mit fehlenden alten Benchmarkdaten
sind dafür keine ausreichende Abnahme. Kein belegter Rechenfehler wird allein aus
der Doppelimplementierung abgeleitet.

**Später prüfen:** Datenaktualisierung vom UI-Test trennen, Formelparität absichern,
portablen Exportbedarf klären. Die Ablage unter `scripts/` ist Konvention, keine
technische Notwendigkeit. Verschiebung oder neue Viewerarchitektur sind noch nicht
beschlossen; kein Server oder zusätzlicher Python-Browserlauf wird vorausgesetzt.

## 5. `scripts/build_building_sector_results.py`

**Heute:** `inspect_sources` prüft Batchmanifest, SCEN-Zuordnung, Anzahl und Hashes
sowie rohe IN/OUT-Header, Duplikate, Quellen, Variablen und Fehlerwerte vor der
Normalisierung. `diagnostics` prüft Schema-/Restwerte. `check_roundtrip` vergleicht
Szenarien und Attribute mit Toleranzen. `build` konsolidiert über `Project.from_files`,
schreibt temporär Excel, liest zurück, prüft und ersetzt erst danach die Zieldatei;
optional Audit-JSON. Keine Simulation. `digest` nutzt `hashlib.file_digest`, obwohl
das Projekt Python >=3.10 angibt: Kompatibilität bei Bearbeitung prüfen.

**Einordnung:** Generische Offline-Konsolidierung und Datenintegrität sind Batch-/IO-
Aufgaben. Die vorhandenen `Project`-APIs übernehmen bereits Ein-/Ausgabe.
`batch._verify_manifest` überschneidet sich teilweise; `inspect_batch` ist kein
unmittelbarer Ersatz, weil es Originalarbeitsmappe, Resume-/Lock-Kontext und teilweise
Schreiboperationen voraussetzt. Konkreter Datensatz und erwartete Szenarienanzahl
bleiben Beispielparameter. Später gemeinsame Prüfung erwägen, keine sofortige
Löschung oder zweite Manifeststruktur. Nicht für normalen Preview erforderlich.

## 6. `scripts/output_catalog.py`

**Heute:** `export_preset_snapshot` liest Excel-META/IN/PRESETS, prüft ungelöste
Formeln, übernimmt Labels/Einheiten/Orte/Hashes und schreibt einen vorhandenen
Schemasnapshot. `build_presets` verbindet diesen mit redaktionellen Presetnotizen
und erzeugt Katalog-/Hilfeseiten. `preset_anchor` erstellt Links. Weitere Funktionen
selektieren Variablen, gruppieren/escapen Inhalte und schreiben Website-QMD/HTML.
`DOMAIN_LABELS` enthält Übersetzungszuordnungen.

**Einordnung:** Excel-Snapshotimport ist Schema-/IO-Logik, keine Website-Fachlogik.
Vorhandener Schemakonverter deckt Standardtabellen, aber nicht automatisch PRESETS-
Semantik ab. Kataloglayout, Hilfetexte und Websiteanker sind berechtigt redaktionell.
`VariableSelection.select(source=...)` bietet bereits exakte Quellselektion;
`for_source` schließt BOTH ein und wäre kein unveränderter Ersatz.

**Später prüfen:** Import in vorhandene IO-/Schema-Erzeugung integrieren, Format
beibehalten und Auswahl wiederverwenden. Der vollständige Presetsnapshot ist nicht
mit visuellen HVAC-Rezepten in `spatial.presets` gleichzusetzen. Kein Neuimport beim
Text-Preview. Übersetzung nach `i18n.py` zurückgestellt.

## 7. `scripts/section_teaching_preview.py`

**Heute:** `teaching_svg` baut ein explizites zweigeschossiges Lehrmodell, rendert
nativ, vereinfacht/kopiert semantische SVG-Knoten und ergänzt Farben, Beschriftungen,
thermische Grenze und qualitative Wärmepfeile. `build_preview` schreibt SVG und
HTML. Eingebettetes JavaScript steuert Modi, Ebenen, Zonen sowie Druck/SVG-Export.

**Einordnung:** `spatial.teaching.simplify_section` deckt bereits Teile der
SVG-Vereinfachung ab. Diese Doppelarbeit ist ein Bereinigungskandidat. Das konkrete
Lehrmodell und seine thermischen Annahmen sind dagegen redaktionell; sie sind keine
allgemeine automatische Gebäudeinterpretation. Browsersteuerung ist für die
interaktive Lektion begründet. Später vorhandene Spatial-Funktionen nutzen und
Viewerbedarf klären; kein zwingender neuer Bibliotheksviewer im ersten Schritt.

## 8. `scripts/component_teaching.py`

**Heute:** `categories` liest Kategorien aus einem festen CSV-Bereich. `cellar_svg`
baut eine zweite konkrete Lektion mit zwei beheizten Geschossen und unbeheiztem
Keller, nutzt den nativen Renderer und annotiert bekannte IDs und thermische Grenze.
`build_catalog` liefert HTML-Auswahl, Tastatursteuerung und Grenzumschaltung.

**Einordnung:** Überschneidung mit der anderen Lehrvorlage spricht für spätere
Bündelung. Konkrete IDs, Kellerannahmen und Lehrtexte gehören nicht als universelle
Regeln ins Paket. Native Metadatenauswahl und gemeinsame SVG-Funktionen bevorzugen.
Ein eigenständiges Skript ist organisatorisch, nicht technisch erforderlich;
Zusammenführung erst mit Aufrufer-/Funktionsabgleich, keine pauschale Löschzusage.

## 9. `scripts/website_editorial_figures.py`

**Heute:** Fünf feste Screenshotrezepte mit Ausschnitt, Titel und nummerierten
Annotationen. `build` prüft PNG/Ausschnitt und bettet Originalpixel in annotierte
SVG-Abbildungen ein.

**Einordnung:** Koordinaten und Erläuterungen sind redaktionelle Entscheidungen,
keine Fachbibliotheksfunktion. Nutzeranforderung: Original und fertige Abbildung
behalten, einmaliges Erzeugungsskript nicht als dauerhaftes Produkt pflegen.
Das Skript ist daher ein späterer Entfernungskandidat, sobald fertige Ergebnisse
und seine How-to-/Build-Aufrufer geklärt sind. Keine Neuerzeugung im Preview und
keine neue Screenshot-API als Ersatz.

## 10. `scripts/publication_example.py`

**Heute:** Synthetisches Beispielprojekt, Dichtegrafik mit historischer Zielkurve,
synthetisch gewichtetes Mobilitätsbudget, weitere Figuren, Herkunft und Export.
Tests hängen davon ab.

**Einordnung:** Ein nachvollziehbares Entwicklerbeispiel kann außerhalb des Pakets
sinnvoll sein. Seine synthetischen Annahmen sind kein belegtes allgemeines Modell
und dürfen nicht allein zur Skriptreduktion in die Fachbibliothek wandern. Später
Überschneidung mit How-tos und Exporttests prüfen. Kein notwendiger zweiter
Website-Build und kein Grund, es jetzt ungeprüft zu löschen.

## 11. `scripts/collect_website_annotations.ps1`

**Heute:** Lesender Hypothesis-Abruf mit Pagination, Gruppen-/URL-Filter und lokalem
Windows-DPAPI-Token. Keine Fachberechnung.

**Einordnung:** Begründetes separates Redaktionswerkzeug, unabhängig von Plotly
und Paketlaufzeit. Windows-Zugangsverwaltung gehört nicht in die energietechnische
Bibliothek. Abruf nur auf Aufforderung; konkrete redaktionelle Maßnahmen gemäß
Redaktionsablauf freigeben lassen. Kein Preview-/Build-Schritt.

## 12. `scripts/render_english_site.py`

**Heute:** Kleiner separater Quarto-EN-Aufruf; Ausführung bereits beim Import.

**Einordnung:** Veröffentlichungskonfiguration, keine native Fachfunktion. Englisch
ist derzeit kein Funktions-/Abnahmeziel. Aufgaben sind in `src/pexl/i18n.py`
gesammelt. Weder Übersetzung noch ersatzlose Löschung sind Teil des Plotly-Schritts.
Bei späterer Bearbeitung Importnebenwirkung und Aufrufer klären.

## 13. `website/output-catalog.js`

**Heute:** Glossarlinks, Suche mit OR/AND, Domänen-/Entitätsfilter, Trefferanzahlen,
Auf-/Zuklappen, Reset und Anker. Keine Modellrechnung.

**Einordnung:** Echte Website-DOM-Aufgabe; im Paket würde sie gewöhnlichen
Notebooknutzern nicht helfen. Der Standort ist sachgerecht. Deutsche UI-Texte und
Locale später gemeinsam mit i18n bearbeiten.

## 14. `website/_resize.html`

**Heute:** Passt Höhen markierter gleichursprünglicher iframes über Größenbeobachtung
an und fängt nicht zugängliche Frames ab.

**Einordnung:** Kleine Website-Einbettungsaufgabe. Kein Diagrammrenderer und keine
Lösung für feste Plotly-Breiten. Die native Plotfunktion darf nicht von diesem
Snippet abhängen. Der Standort als Website-Include ist sachgerecht.

## Aufrufer und Prüfung bei späterer Bearbeitung

Betroffen sein können die How-tos für Strombilanz, Publikation, Bewertung,
Gebäudesektorergebnisse, Lehrschnitte, Preset-/Outputkataloge, redaktionelle Figuren
und Website; außerdem Website-Tutorials für Stromprofile, Netzlast, Grafikexport,
Bewertung, Gebäudeschnitt und Website. Relevante Tests liegen unter den Bereichen
building_sector, output_catalog, section_teaching_preview, publication, website,
website_examples und tutorials. QMD-Einbettungen, Downloadziele und Quarto-
Konfiguration gehören jeweils zur konkreten Aufruferprüfung.

Keine Skriptdatei zuerst löschen und erst danach abhängige Notebooks reparieren.
Für jeden tatsächlich erweiterten Ablauf das passende ausführbare How-to mit
identischen Implementierungsfunktionen aktualisieren. Neue öffentliche APIs oder
persistierte Strukturen müssen Nutzen, fehlende bestehende Alternative und Pflege
begründen; dieser Audit genehmigt weder neue Viewerformate noch Registraturen.

## Abgrenzung zur aktuellen Umsetzung

Der erste geplante Schritt betrifft native Stromprofil-/Plotly-Funktionen,
responsive Darstellung und betroffene Notebooks. Die übrigen Befunde bleiben
gezielt bearbeitbarer Bestand. Notebook-Versionierung bleibt vorerst bestehen;
gespeicherte Tutorialoutputs werden im Preview nicht neu berechnet. Generierte
Assets sind derzeit ignoriert: Ihre Bereitstellung in frischen Arbeitskopien ist
ein eigenes offenes Thema, keine Begründung für automatische Neuberechnung.

Englisch-TODOs stehen in `src/pexl/i18n.py`; bestehende englische Bibliotheksaufrufe
sollen erhalten bleiben. Dieser Bericht enthält keine Veröffentlichung oder
Laufzeitabnahme und macht den Gesamtumbau nicht zur Voraussetzung der Plotly-Korrektur.
