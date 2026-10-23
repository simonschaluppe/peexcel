# Publikationsgrafiken und lokale Quarto-Website

## Aktueller Tutorial-Publikationsweg (23.10.2026)

Die deutschen Reinschriften liegen als gepflegte `website/tutorial_*.ipynb` vor.
Quarto rendert diese Dateien direkt gemäß `website/_quarto.yml`, einschließlich
vorher lokal erzeugter Ausgaben. `execute.enabled: false` verhindert eine erneute
Ausführung beim Website-Build. Der Asset-Schritt kopiert die Tutorialdateien
unverändert in `downloads/`; er erzeugt keine Notebook-Seitenkopien mehr.

Die ursprünglichen `notebooks/howto_*` bleiben unverändert. Bestehende Downloads
für die englischen Seiten bleiben verfügbar; alte HTML-Lesefassungsadressen
führen zu den entsprechenden deutschen Tutorials. `prepare_assessment` bleibt
für das bestehende Arbeitsnotebook aufrufbar, liefert jetzt aber die direkt
gepflegte Tutorialquelle zurück. Die URLs `assessment.html` und
`batch-python.html` werden über `output-file` im jeweiligen Notebook erhalten.

Der vom Nutzer deaktivierte Pre-render-Hook bleibt deaktiviert. Für einen
vollständigen lokalen Build zuerst `python scripts/website_assets.py`, danach
`quarto render website` ausführen. Nach einer erneuten Notebook-Ausführung den
Asset-Schritt wiederholen, damit die Downloads denselben Stand haben.
`website/tutorial_website.ipynb` beschreibt diesen Ablauf ausführbar, mit bewusst
getrenntem Build-Schalter. Die ältere Dokumentation unten ist Implementierungshistorie;
bei Widersprüchen gilt dieser Abschnitt.

Die zusätzliche redaktionelle Quelle pro Thema ist eine bewusste Nutzerentscheidung:
Original-Arbeitsnotebooks erhalten, Website-Tutorials auf Deutsch und ohne doppelte
Einstiege anbieten. Die Pflege betrifft Texte, API-Aufrufe und überprüfte Ausgaben;
Berechnungen und Renderer werden wiederverwendet. Der präzisierte Umfang steht in
[der Tutorial-Entscheidung](python_howto_quarto_proposal.md).


## Bestandsaufnahme und minimaler Implementierungsplan

`reporting.materialize(view, chart_name)` liefert bereits Berichtsdictionaries;
`plot.plotly.render(report)` liefert normale Plotly-Figuren. Das Dashboard
verwendet genau diese Pipeline. `electricity_balance` liefert ebenfalls eine
Figur und erwartet bereits aggregierte Daten. Diese Funktionen bleiben unverändert.

Plotlys vorhandene `write_html(include_plotlyjs=True)` und `write_image` reichen
für die Ausgabe aus. Die einzige zusätzliche öffentliche Schnittstelle
`pexl.plot.export.export_figure` ergänzt verpflichtende, sichtbare Herkunft und
eine Kopie der Figur. Direkter Plotly-Export erzwingt diese Angaben nicht.
Es gibt kein neues Datenmodell und keine separate Metadatendatei: ein Mapping
mit Textwerten wird in Plotlys bestehendes `layout.meta` und als Fußnote geschrieben.
Pflegeaufwand: Pflichtfelder/Validierung und Exporttests; ursprüngliche Figuren
und Report-Schnittstellen bleiben kompatibel. Die Funktion akzeptiert HTML,
SVG, PNG und optional PDF als Zieldateiendung.

`scripts/publication_example.py` ist ein ausführbares Beispiel, keine neue
Paket-API. Notebook und Website-Build verwenden dieselben Funktionen. Die
synthetischen Daten werden über `Project`/`Scenario` und das aktive Schema erzeugt.
Sie sind keine Berechnung mit einer Excel-Releaseversion. HTML/SVG/PNG sind
ignorierte, jederzeit neu erzeugbare Build-Artefakte; sie müssen nicht migriert
werden. Bei Schemaänderungen prüfen die Beispieltests deren Kompatibilität.
Quarto-Konfiguration und Seiten sind die einzigen zusätzlichen Website-Quellen.
README und Changelog bleiben maßgeblich für Produkt- und Versionsinformationen.

## Installation und vollständiger Ablauf

Im Repository-Verzeichnis:

```bash
python -m pip install -e ".[publication,dev]"
python scripts/publication_example.py
python -m pytest tests/test_publication.py
quarto render website
```

Quarto CLI separat installieren. Kaleido 1 benötigt Chrome/Chromium; bei fehlendem
Browser nach dessen Installation erneut exportieren. Es gibt keinen stillen
Fallback auf leere oder unvollständige statische Grafiken. Nur HTML benötigt
keinen Exportbrowser: `python scripts/publication_example.py --formats html`.
Die Quarto-Pre-render-Schritte erstellen die konfigurierten realen Ergebnisse,
Lehrmodule, Downloads und synthetischen Beispielgrafiken neu. Der Post-render-Schritt
baut das englische Unterprojekt. Die gesamte Website liegt in `website/_site/`.
Der vollständige Ablauf einschließlich Prüfung und separat freizugebender
Veröffentlichung ist in `notebooks/howto_website.ipynb` ausführbar dokumentiert.
`master` enthält Quellen und erforderliche Eingabedateien; `gh-pages` enthält die
generierte Website. Ein Build allein veröffentlicht nichts.

Ein frischer Build übernimmt keine Altdateien aus `gh-pages`: Die versehentlich
veröffentlichte Quelle `en/index.qmd` und vier unreferenzierte
`assets/results/*.html.table`-Fragmente werden nicht erzeugt. Die Ergebnistabellen
bleiben unter `assets/results/tables.html` und als CSV verfügbar. `.nojekyll`
gehört zum Veröffentlichungsschritt von Quarto. Die bisherigen synthetischen
Grafiken unter `assets/` werden weiterhin mit `publication_example.py` erzeugt,
damit ihre veröffentlichten URLs erhalten bleiben.

Das ausführbare `notebooks/howto_publication.ipynb` umfasst Projekt, Jupyter-Anzeige,
alle Exportformate, Methodenbeispiele und den lokalen Quarto-Build. Für PDF-Dokumente
die SVG- oder PNG-Datei einbinden, beispielsweise `![Bilanz](assets/gwp_ee_detail.png)`.
Statische Dateien enthalten sämtliche Serien, Farben, Vorzeichen, Legenden und
Annotationen. Hover und das Ausblenden von Serien bleiben HTML-Funktionen.
Die sichtbare Herkunft und Achsen ersetzen diese Interaktion beim Druck.

## Eigene Projekte und Herkunft

```python
from pexl import Project, reporting
from pexl.plot import plotly
from pexl.plot.export import export_figure
from pexl.schema.current import SCHEMA_VERSION

project = Project.from_excel("projektexport.xlsx")
report = reporting.materialize(project.view, "primary_energy_balance")
fig = plotly.render(report)
provenance = {
    "source": "projektexport.xlsx; gegebenenfalls SHA-256 ergänzen",
    "scenario": ", ".join(report["frame"]["Variant"]),
    "model_version": "Aus der berechnenden Excel-Arbeitsmappe übernehmen",
    "schema_version": SCHEMA_VERSION,
    "calculated_at": "Aus dem Berechnungsprotokoll übernehmen; sonst unbekannt",
    "convention": "Bedarf/Deckung als positive Beträge; Kontextfaktoren virtuell",
}
export_figure(fig, "bilanz.html", provenance=provenance)
export_figure(fig, "bilanz.svg", provenance=provenance)
export_figure(fig, "bilanz.png", provenance=provenance)
```

Die Pflichtfelder müssen tatsächliche Quellenangaben enthalten. Der Export kann
deren Wahrheit nicht prüfen. Berechnungsstand ist nicht Exportzeitpunkt;
`SCHEMA_VERSION` ist nicht die Modellversion. Stable/Development werden ausschließlich
nach der tatsächlich verwendeten Excel-Arbeitsmappe angegeben. Optional können
Hash, Revision oder konkrete Parameter als zusätzliche Mapping-Einträge erscheinen.

## Methodenprototypen und offene Fragen

### Dichtekontext

`Zielwert.ZQSynergy()` aus `analysis/targets.py` liefert die vorhandenen Parameter
A=38, dx=0.15, EUI=33, fPE=1.63, cutoff=125 mit NGF-Bezug. `target` und
`context_factor` liefern Zielwert und dessen negative virtuelle Gut-/Lastschrift.
Dieser historische Parametersatz wird nicht als aktuell freigegebener
Excel-Referenzparametersatz ausgegeben. Kontext ist **kein realer Energiefluss**.
Die wissenschaftliche Einordnung verweist auf Schneider et al. (2023),
[A Quantitative Positive Energy District Definition with Contextual Targets](https://www.mdpi.com/2075-5309/13/5/1210),
und den in der README verlinkten Hintergrundbericht. Eine numerische Gleichsetzung
dieses historischen Python-Presets mit jeder Modellversion ist nicht belegt.

### Mobilitätsbudget

Das aktive Schema beschreibt `cfm_budget_residential`, `cfm_budget_office`,
`cfm_budget_school`, `cfm_budget_retail` als Eingaben in kWhPE/m²NGFa.
`SCHEMA_META.context_factor_mobility.formula` gewichtet sie mit den jeweiligen
NGF-Flächen und `per_NFA`. `PEI_cf_mobility` multipliziert diesen Wert mit
`mobility_is_included`. Es gibt dafür keine eigenständige numerische Python-
Berechnungsfunktion; das Beispiel führt nur diese einfache Flächengewichtung aus.
Es setzt eingeschlossene Mobilität voraus und verwendet normierte Flächenanteile.
Budget, positiver Bedarf und Budget minus Bedarf stehen getrennt im Diagramm.
Das Notebook erlaubt die Auswahl von Nutzungen und Anteilen als Dictionary.

**Offen:** Nationale Ausgangsstatistik, Bezugsjahr und gültige Zuordnungsparameter
sind aus diesen Schemaeingaben nicht rekonstruierbar. Die Beispielwerte 20/10
sind synthetische Testwerte, keine nationalen Referenzwerte. Für wissenschaftliche
Anwendung die geprüften Eingaben der konkreten Arbeitsmappe und deren Quellen
einsetzen. BGF und NGF sowie End- und Primärenergie dürfen nicht vermischt werden.

### THG-Budget

Der bestehende `gwp_ee_detail`-Report und THG-Renderer zeigen kumulierte Emissionen
und L1/L2/L3-Bänder (0–70 / 70–195 / 195–320). Sie werden wiederverwendet,
nicht als neue Budgets berechnet. Die Renderer-Referenzachse bezeichnet
kg CO2eq/m²BGF und 2025–2075. Bei Reports hat die im Schema angegebene Einheit
Vorrang. Der 50-jährige Bewertungszeitraum ist von einem nationalen Zieljahr
und einem angenommenen Dekarbonisierungspfad zu unterscheiden.

**Offen:** Die Bänder allein dokumentieren weder nationales Zieljahr noch
jährliche Emissionsfaktoren oder Pfadinterpolation. Das Beispiel erfindet keinen
jährlichen Verlauf. Diese Angaben sind vor einer wissenschaftlichen Anwendung
aus der verwendeten Modellversion zu belegen. Die README nennt dafür unter anderem
[Declaration-Ready Climate-Neutral PEDs (2025)](https://doi.org/10.3390/designs9060123).
Die Publikationslinks dienen als Forschungszugang; eine vollständige Prüfung
der Herleitung gegen die aktuelle Arbeitsmappe ist nicht Bestandteil des Prototyps.

## Technische Referenzen

- [Plotly HTML-Export](https://plotly.com/python/interactive-html-export/)
- [Plotly statischer Export](https://plotly.com/python/static-image-export/)
- [Quarto Websites](https://quarto.org/docs/websites/)

HTML bindet Plotly.js lokal in die Datei ein und benötigt beim Betrachten keinen
Python-Server und kein CDN. Die Website bindet diese Dateien per iframe ein.

Die Website verwendet inzwischen den vervollständigten Report `gwp_ee` für bauliche und betriebliche THG-Beiträge. `gwp_ee_detail` bleibt die Detailansicht grauer Emissionen; `district_gwp_ee` bleibt unverändert leer. Der aktuelle Workflow mit realen Exporten ist in `howto_publication.ipynb` dokumentiert.

## Durchgeführte Abnahme

- Gesamte Testsuite: 219 bestanden, einschließlich tatsächlicher SVG-/PNG-Exporte.
- How-to-Notebook vollständig ausgeführt, ohne Zellfehler; Ergebnis unter
  `notebooks/local_exports/howto_publication.executed.ipynb` (ignoriertes Artefakt).
- `quarto render website` erfolgreich; lokale Seitenlinks und Assets geprüft.
- Streamlit-AppTest mit allen Beispielgrafiken erfolgreich; vorhandenes Dashboard
  startet ebenfalls ohne App-Ausnahme. Beim dort gespeicherten Projektpfad meldet
  Streamlit automatische Arrow-Typkorrekturen für gemischte Tabellenwerte.
- Exportierte Primärenergie- und THG-Grafiken visuell geprüft.

In der Windows-Sandbox musste TEMP/TMP auf ein beschreibbares Verzeichnis unter
`notebooks/local_exports/` zeigen. Quarto und die abschließenden Notebook-/Streamlit-
Prüfungen liefen wegen Sandbox-Cache-/Prozessbeschränkungen außerhalb der Sandbox.
Es wurden weder Bilanzmethodik noch Referenzparameter geändert und nichts deployt.


## Erweiterte Anwenderwebsite

Die aktuelle Inhaltsstruktur und Pflege der Lehrmodule sind im
[Website-Umsetzungsplan](website_implementation_plan.md) dokumentiert.
`howto_website.ipynb` führt den gemeinsamen Asset-Build aus. Quarto rendert
nur QMD-Seiten; die freigegebenen Notebooks werden separat als Lesefassung und
Download ohne gespeicherte Ausgaben bereitgestellt. Konkrete neue Projekte und
Stundenexporte sind zurückgestellt; der synthetische Generator bleibt unverändert.

## Python-Batchsimulation

`notebooks/howto_batch_simulate.ipynb` ist die einzige editierbare Quelle des neuen Tutorials. Der bestehende Notebook-Seitenexport wird intern wiederverwendet und erzeugt `website/batch-python.ipynb` sowie einen Download. Das vermeidet eine zweite Code-Implementierung in einer QMD-Datei; die Simulation verwendet weiterhin `RunScenariosAutomated`. Die generierte Seite ist ignoriert, wird bei jedem Asset-Build aktualisiert und benötigt keine Migration oder neue öffentliche API. Pflege: Notebook-Inhalt und Navigation; Prüfung: Notebook-Validierung, Seitenexport und Quarto-Render. Der Website-Build führt keine Excel-Makros aus.

### Abnahme der Tutorial-Reinschriften

- Zwölf deutsche Tutorialquellen direkt in Quarto eingebunden; vier Themenbereiche
  in Übersicht und Seitenleiste. Die Übersicht verlinkt zusätzlich vorhandene
  Excel-Bedienanleitungen und kann um eigenständige Excel-Tutorials ergänzt werden.
- Zehn Tutorials lokal von oben nach unten ausgeführt und mit Ausgaben gespeichert.
  Beim Website-Tutorial bleibt der rekursive Build-Schalter deaktiviert; optionale
  SVG-/PNG-Exporte sind nicht Teil dieses Ausführungslaufs.
- Excel-COM und Baubook nicht live ausgeführt. Der Baubook-Ablauf ist zusätzlich
  mit simulierten API-Antworten ohne Netzwerkzugriff getestet.
- 21 Website-/Tutorialtests erfolgreich. Vollständiger deutscher Quarto-Build:
  45 Seiten. Links, Assets und bytegleiche Notebook-Downloads aller zwölf Tutorials
  geprüft; Downloadkopien sind vom Rendern und Suchindex ausgeschlossen.
- Plotly-Ausgaben als eingebettetes HTML gespeichert, da reine Plotly-MIME-Ausgaben
  in dieser statischen Quarto-Konfiguration nicht dargestellt wurden. Das erhöht
  die Notebookgröße (eingebettete Plotly-Bibliothek), erhält aber die Diagramme
  einschließlich JavaScript in den Downloads ohne separate Inhaltsdateien.
- Interaktive Netzlast-Dauerlinie in der Browser-Vorschau geprüft. Alle 15
  ursprünglichen How-to-Dateien per SHA-256 unverändert bestätigt.
- Englisches Unterprojekt nicht neu gebaut; kein Push und kein Pages-Deployment.
