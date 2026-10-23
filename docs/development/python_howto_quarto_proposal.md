# Python & Automatisierung: Vorschlag zur Vereinheitlichung

Stand: 23.10.2026. Status: **durch die nachfolgende Nutzerentscheidung ersetzt**.

## Verbindliche Präzisierung

Die bestehenden `notebooks/howto_*` bleiben unverändert. Die Website erhält
redaktionell eigenständige deutsche `website/tutorial_*.ipynb`, die Quarto direkt
rendert. Inhaltliche Überschneidungen werden nur im Website-Angebot zusammengeführt.
Gespeicherte Ausgaben und Diagramme gehören zu den Tutorialquellen und Downloads.
Die Übersicht ist offen für weitere Excel-Tutorials. Die frühere Empfehlung,
die How-tos selbst umzuschreiben und generierte Notebook-Seitenkopien zu verwenden,
ist damit ausdrücklich verworfen.

Umgesetzt werden zwölf Themen: Excel-Einstieg, Zeitreihenimport, Baubook, Batch,
Bewertung einschließlich Explorer, elektrische Flussprofile, Netzlast, Sankey,
Gebäudeschnitt einschließlich Lehransicht, Grafikexport, Schema und Website.
Es entsteht kein neuer fachlicher Workflow neben den vorhandenen APIs; die
redaktionelle Website-Fassung wird durch `tutorial_website.ipynb` erklärt.

Nutzen der zusätzlichen gepflegten Notebookdateien: verständliche deutsche
Anleitungen mit ausgewählten Beispielen, ohne die bisherigen Arbeitsnotebooks
und ihre Experimente zu verändern. Die vorhandenen How-tos allein erfüllen diese
vom Nutzer gewünschte Trennung nicht. Pflegeaufwand: Bei API-Änderungen müssen
betroffene Tutorials erneut ausgeführt, Texte und gespeicherte Ergebnisse geprüft
werden; Website-Tests sichern direkte Einbindung und Downloadtreue. Berechnungs-
und Darstellungsfunktionen bleiben im vorhandenen Paket bzw. in vorhandenen Skripten.
Es gibt keinen zusätzlichen Inhaltskatalog und keine neue öffentliche Paket-API.
Die nachfolgenden Abschnitte dokumentieren den ursprünglichen Vorschlag.

## Aktueller Einstieg

Das Batch-How-to liegt in der lokalen Vorschau unter `batch-python.html`.
Verweise stehen in der Seitenleiste unter „Python & Automatisierung“, auf
`python.html`, auf der Startseite und auf `batch.html`. Commit `97b8169`
enthält die Quellen; eine Veröffentlichung auf GitHub Pages erfolgte noch nicht.

## Befund

Alle 15 Dateien `notebooks/howto_*.ipynb` wurden hinsichtlich Zellinhalten,
Abhängigkeiten, Pfaden und bisheriger Einbindung gesichtet. Eine erfolgreiche
Ausführung aller Notebooks ist damit nicht nachgewiesen.

- Zwei Tutorials werden nativ von Quarto gerendert: Bewertung und Batchsimulation.
- Sechs weitere laufen über den separaten `nbconvert`-HTML-Export. Vier davon
  erscheinen in aufklappbaren Iframes, zwei nur als Links. Alle verlieren dabei
  ihre gespeicherten Ausgaben.
- Das Bewertungs-Erklärnotebook liefert Texte für einen gesonderten Explorer.
  Es hat einen Download, aber keine eigene technische Tutorialseite.
- Sechs How-tos fehlen in der bisherigen Notebook-Publikationsauswahl vollständig.
- `python.qmd` wiederholt Links als Tutorial, GitHub-Einstieg und thematischen
  Nachtrag. Die Seitenleiste zeigt nur einen kleinen Teil des Angebots.
- Sprache, Gliederung und Beispielpfade variieren. `howto_excel` und
  `howto_excel_updated` tragen denselben Titel und überschneiden sich stark;
  ersteres enthält zugleich zusätzliche IO-Beispiele und einen Abschnitt zu
  einer „geplanten“ Diagramm-API, die im anderen bereits verwendet wird.
- Netzlast und Projektzusammenstellung benötigen persönliche OneDrive-/Nextcloud-
  Pfade. Im Netzlasttext steht GFA/BGF, während der Code NFA/NGF verwendet.
  Umbenennung und anschließender Zugriff auf Szenarien müssen gemeinsam geprüft
  werden; einzelne Zellen greifen auf Variablen aus vorherigen Schleifen zurück.
- Das Sankey-Notebook besteht nur aus sechs Codezellen, ohne fachliche Anleitung.
- Baubook enthält eine Ausgabe von Teilen eines API-Schlüssels und gespeicherte
  Ausgaben. Diese dürfen nicht ungeprüft auf die Website übernommen werden.
- Schemawechsel erzeugt Dateien; das Website-Notebook startet selbst einen
  Website-Build. Eine pauschale Ausführung beim Quarto-Build wäre ungeeignet.

## Vorgeschlagene Kapitelstruktur

„Python & Automatisierung“ erhält eine Übersicht mit Ziel, Voraussetzung und
direktem Seitenlink je Tutorial. Kein eingebettetes vollständiges Notebook auf
der Übersicht. Dieselbe Reihenfolge wird in der Seitenleiste verwendet.

| Gruppe | Seiten in Lernreihenfolge |
|---|---|
| Einstieg & Daten | Excel-Projekte lesen und bearbeiten; Zeitreihenexporte zusammenführen; Baubook-Daten importieren |
| Simulieren & analysieren | Batchsimulation; Primärenergie und THG bewerten; elektrische Flussprofile; Netzlast und PV-Einspeisung; Sankey-Diagramme |
| Visualisieren & weitergeben | Gebäudeschnitte; Lehrschnitt und Overlays; Bewertungs-Explorer erzeugen; Grafiken exportieren; vorhandener lokaler Szenarioexplorer (`dashboard.qmd`) |
| Entwicklung & Dokumentation | Schema aktualisieren; Website bauen und veröffentlichen |

Der bestehende Quick-Check bleibt als Fachansicht unter „Analysieren“ erhalten.
Seine technische Anleitung liegt bei „Bewertungs-Explorer erzeugen“; beide
verlinken einander. `dashboard.qmd` bleibt eine Anleitung für die lokale App.

## Entscheidung je Notebook

Die folgenden Namen beziehen sich auf `notebooks/` und enden jeweils auf `.ipynb`.

| Notebook | Geplante Überarbeitung |
|---|---|
| `howto_excel` | Maßgeblichen Einstieg daraus machen: Import, Szenarien, Glossar/Selektion, Änderung, Export. Aktuelle Inhalte aus `_updated` übernehmen, zusätzliche IO-Beispiele erhalten, veraltete Planungstexte entfernen. |
| `howto_excel_updated` | Nach Abgleich aller Inhalte durch ein kurzes, Quarto-kompatibles Verweisnotebook auf `howto_excel` ersetzen. Keine zweite Implementierung und kein zweiter gleichnamiger Navigationseintrag. |
| `howto_create_project_from_different_timeseries_files` | Deutsche Anleitung, vorhandenes `Project.from_files`, explizite Eingabedateien aus dem Repository und Ausgaben unter `local_exports`. Pickle als optionalen lokalen Zwischenspeicher erklären, nicht als Voraussetzung des nächsten Tutorials. |
| `howto_baubook_io` | Deutsch vereinheitlichen, Nummerierung reparieren, Zugangsdaten-Ausgabe entfernen und gespeicherte Ausgaben bereinigen. Bestehende `pexl.io.baubook`-Funktionen verwenden; API-Zugriff ausdrücklich als lokale Voraussetzung kennzeichnen. |
| `howto_batch_simulate` | Einheitliche Projektwurzel/Pfadkonfiguration, Voraussetzungen und Ergebnisprüfung; Szenarionamen und Exportdateinamen konsistent behandeln. VBA-Einstiegspunkt beibehalten. Keine Excel-Simulation im Website-Build. |
| `howto_assess` | Als Vorbild für nachvollziehbare Schritte verwenden; Metadaten und Linkkonventionen angleichen, geprüfte Diagrammausgaben erhalten. Bestehende URL `assessment.html` behalten. |
| `howto_analyze_electricity_balance` | Bestehenden Ablauf beibehalten, native Quarto-Seite mit geprüften Beispieldiagrammen. Titel und Grenzen als Teilflussanalyse korrekt ausweisen. |
| `howto_analyze_gridload` | Deutsche, von oben nach unten ausführbare Anleitung; persönliche Pfade, Debugzellen und auskommentierte Versuche entfernen. Flächenbezug gegen Schema prüfen, konsistent beschriften; explizite Szenarioauswahl und optionale Gruppierung. |
| `howto_sankey` | Ziel, Voraussetzungen, vorhandene Beispielquelle, Warmwasser/Heizung/Kühlung sowie Interpretation und Grenzen ergänzen. Vorhandene Sankey-Renderer verwenden. |
| `howto_visualize_project` | Deutsche Schrittfolge, Parameter und Annahmen bündeln; vorhandene räumliche Funktionen und Beispiele erhalten, SVG-Ausgaben in Quarto prüfen. |
| `howto_section_teaching_preview` | Vom allgemeinen Gebäudeschnitt abgrenzen: Lehrstil, Overlays und Prüfung. Bestehende interaktive Module weiterverwenden; deren gezielte Einbettung bleibt möglich. |
| `howto_assessment_explained` | Fachtexte als Quelle des bestehenden Explorers erhalten; technischen Ablauf mit Quelle, Erzeugung und Ergebnis ergänzen. Vorher prüfen, welche Markdownzellen der Explorer übernimmt, damit technische Anleitung nicht in der Fachansicht landet. |
| `howto_publication` | Fokus auf Grafikexport und Datenherkunft. Entwicklungsabschnitt zur Report-Codegenerierung mit dem Schema-How-to abgleichen und dort bündeln. |
| `howto_schema_transition` | Deutsches Entwickler-Tutorial mit Parametern, Vergleich, Prüfung und separater Aktivierung; Dateierzeugung in einem isolierten Beispiel prüfen. Vorhandene Schema-API beibehalten. |
| `howto_website` | Gemeinsamen Publikationsweg aller How-tos ausführbar dokumentieren. Historische Sonderfälle bereinigen; Vorschau, Notebook-Prüfung, Sprachfassungen und Veröffentlichung klar trennen. |

## Einheitlicher Aufbau und technische Umsetzung

Jedes vollständige Tutorial erhält Titel und Kurzbeschreibung, Lernziel,
Voraussetzungen/Datenquelle, einen Konfigurationsblock, nummerierte Schritte,
sichtbares Ergebnis mit Interpretation sowie weiterführende Links. Texte werden
Deutsch; API-Namen bleiben unverändert. Notebookcode verwendet die vorhandenen
Paket- und Skriptfunktionen. Die Quarto-Darstellung zeigt Code aufklappbar.

Die Notebooks bleiben die **einzige editierbare Quelle** für Tutorialtext und
Code. Der vorhandene private Helfer `_prepare_notebook_page` wird vereinheitlicht
und für alle How-tos verwendet. Der separate HTMLExporter-Weg entfällt.
Notebook-Metadaten erhalten die benötigten Quarto-Seitenangaben; es gibt keine
zusätzliche Inhaltskopie in QMD und keinen neuen Katalog in JSON oder YAML.
Die Navigation bleibt in der vorhandenen `_quarto.yml`.

Generierte Seitenkopien liegen wie bisher unter `website/`, Downloads unter
`website/downloads/`. Sie bleiben ignorierte Build-Artefakte. Ihr Nutzen ist die
Einbindung der außerhalb des Website-Verzeichnisses liegenden Quellen in dessen
Navigation, Suche und Gestaltung. Direkte vorhandene Notebook-Dateien reichen
für diese Projektstruktur nicht ohne Anpassung des Build-Schritts aus. Die
Erzeugung erfolgt bei jedem Build; Handpflege und Migration der Kopien entfallen.
Pflegeaufwand: ein Exporthelfer, vorhandene Navigation und Tests für Linkziele,
Quelltreue und Ausgaben. Keine neue öffentliche Paket-API vorgesehen.

Bestehende URLs `assessment.html`, `batch-python.html` und die sechs bisherigen
`tutorials/howto_*.html` sollen erhalten bleiben. Neue Tutorials bekommen ebenfalls
sprechende Seitenadressen; interne Links werden angepasst. Pfade zu Downloads,
Grafiken und anderen Tutorials müssen für Seiten im Unterverzeichnis korrekt
aufgelöst werden. Das wird vor der vollständigen Umstellung an einer Seite
geprüft. Der `_updated`-Verweis bleibt aus Gründen der Auffindbarkeit erhalten.

## Ausführung und sichtbare Ergebnisse

- **Website-Build:** rendert die vorbereiteten Notebooks ohne deren Code erneut
  auszuführen. Damit startet er weder Excel noch API-Abfragen, Schemawechsel oder
  rekursiv den im Website-Notebook beschriebenen Build.
- **Lokale Abnahme:** Analyse- und Visualisierungsnotebooks werden vorher mit
  versionierten Beispieldaten von oben nach unten ausgeführt. Geprüfte Ausgaben
  werden für die Website übernommen; Downloads bleiben ohne Ausgaben.
- **Externe Voraussetzungen:** Excel/COM und Baubook werden ausdrücklich als
  lokale Abläufe ausgewiesen. Ohne erforderliche Umgebung wird nur die geprüfte
  Anleitung veröffentlicht und die fehlende Ausführungsabnahme benannt. Keine
  erfundenen Simulationsergebnisse oder automatischen API-Aufrufe.
- **Dateiändernde Beispiele:** Ausgaben grundsätzlich in `notebooks/local_exports`;
  Schemaaktivierung und Veröffentlichung bleiben bewusste, getrennte Schritte.
- **Gespeicherte Ausgaben:** vor Übernahme auf persönliche Pfade, Zugangsdaten,
  veraltete Fehler und Datenquellen prüfen. Baubook-Ausgaben zunächst entfernen.

## Umsetzung und Abnahme nach Freigabe

1. Exportweg und einheitliche Seitengestaltung an Excel-Einstieg, Batch und einem
   Diagramm-Tutorial umsetzen; native Darstellung und bestehende URLs prüfen.
2. Alle 15 Quellen gemäß Tabelle bearbeiten; Excel-Doppelung zusammenführen,
   Datenpfade und Tutorialverweise vereinheitlichen.
3. Ausführbare lokale Abläufe prüfen, erforderliche externe Prüfungen getrennt
   protokollieren. Keine globale Zusage „alle ausführbar“ ohne diese Nachweise.
4. `howto_website` als ausführbare Dokumentation der neuen Publikationskette
   aktualisieren; `publication.md` auf den aktuellen technischen Stand bringen.
5. Gesamten Quarto-Build und vorhandene Website-Tests ausführen. Abdeckung aller
   15 Quellen, funktionierende Downloads, interne Links, Suche, Quelltreue und
   unveränderte Originalnotebooks durch den Build prüfen. Desktop- und schmale
   Vorschau einschließlich Tabellen und interaktiver Diagramme kontrollieren.

**Zur Freigabe:** diese Struktur und vollständige Überarbeitung, einschließlich
Zusammenführung der Excel-Einstiege und deutscher Redaktion. Anschließend lokale
Vorschau zur Abnahme; Commit/Veröffentlichung nach dem dafür vereinbarten Auftrag.
Dieser Vorschlag selbst ändert weder Notebooks noch Website oder Excel-Dateien.
