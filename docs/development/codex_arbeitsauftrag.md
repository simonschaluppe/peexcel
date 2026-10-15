# Codex-Auftrag: PEExcel – Wiederverwendbare Visualisierungen und Quarto-Toolwebsite

**Repository:** `simonschaluppe/peexcel`

## Ziel

Die bereits vorhandenen PEExcel-Auswertungs- und Plotly-Funktionen sollen neben dem Streamlit-Dashboard auch in statischen Quarto-Webseiten, Praxisbeispielen und wissenschaftlichen Publikationen verwendet werden können.

Zusätzlich soll im Repository eine einfache Quarto-Toolwebsite entstehen, mit Toolvorstellung, Downloads, Versionsinformationen, Dokumentationszugängen und einem Einstieg zum Szenarioexplorer.

**Wichtig:** Vorhandene Funktionen wiederverwenden. Keine neue Plotting-Architektur oder umfangreiche Refaktorierung.

## Bestehende Komponenten prüfen

- `src/pexl/plot/plotly.py`
- `src/pexl/plot/electricity_balance.py`
- `src/pexl/analysis/targets.py`
- `src/pexl/reporting/materialize.py`
- `apps/dashboard/main.py`
- `README.md`, `CHANGELOG.md`, `AGENTS.md`
- Bestehende How-to-Notebooks und Tests

Die Reporting-Pipeline `reporting.materialize(view, chart_name)` → `plotly.render(report)` soll möglichst unverändert bleiben.

## Arbeitspaket A – Plotly für Quarto nutzbar machen (Priorität 1)

1. Eine minimale, dokumentierte Möglichkeit schaffen, vorhandene Plotly-Abbildungen aus PEExcel-Projekten als eigenständige HTML-Grafiken und statische SVG-/PNG-Versionen zu exportieren.
2. Unterstützt werden zunächst die bestehenden Primärenergie- und THG-Bilanzdiagramme sowie ausgewählte Stromflussdiagramme.
3. Titel, Einheiten, Legenden, Tooltips, Annotationen, positive/negative Flussrichtungen und verwendete Bilanzkonventionen erhalten.
4. Diagramme müssen in einer statischen Quarto-Website ohne Streamlit-Server interaktiv funktionieren.
5. Bei statischen Exporten eine äquivalente PDF-taugliche Darstellung erzeugen.
6. Jedes Diagramm erhält nachvollziehbare Angaben zu Datenquelle, Szenario, Modell-/Schemaversion und Berechnungsstand.

Zunächst bestehende Exportmöglichkeiten von Plotly prüfen, bevor neue Schnittstellen eingeführt werden.

## Arbeitspaket C – Wiederverwendbare Methodenvisualisierungen (Priorität 3)

Prototypen für folgende Darstellungen vorbereiten:

**Dichtekontextfaktor**
- GFZ als Eingangsgröße
- Dichteabhängiger Zielwert und äquivalente virtuelle Gut-/Lastschrift
- Parameter der verwendeten Modellversion
- Klarer Hinweis: Kontextfaktor ist kein realer Energiefluss

**Mobilitätsbudget**
- Auswahl von Nutzung und Flächenanteilen
- Berechnung des national zugeordneten Mobilitätsbudgets pro m² NGF
- Darstellung von Budget, tatsächlichem Mobilitätsbedarf und daraus resultierendem Bilanzbeitrag als getrennte Größen

**THG-Budget**
- L1/L2/L3-Budgetvarianten
- Kumulierte Emissionen und Budgetgrenze
- Unterscheidung von 50-jährigem Bewertungszeitraum, nationalem Zieljahr und angenommenem Dekarbonisierungspfad

Methodische Werte nicht neu erfinden. Existierende Implementierungen und die wissenschaftliche Herleitung identifizieren; fehlende Daten oder Unklarheiten dokumentieren.

## Arbeitspaket B – Toolwebsite (Priorität 2)

Eine kleine Quarto-Website innerhalb des PEExcel-Repositories vorbereiten, beispielsweise unter `website/`, ohne die bisherige Dokumentation oder Repository-Struktur zu beschädigen.

Vorgesehene Inhalte:

- PEExcel – Überblick
- Download und aktuelle Releases
- Schnellstart und Handbuch
- Ergebnisinterpretation und Beispiele
- Python-Schnittstelle und Notebooks
- Dashboard / Szenarioexplorer
- Verlinkung zum wissenschaftlichen Hintergrundbericht

README und Changelog sollen die maßgeblichen Quellen für Toolinformationen bleiben. Keine umfangreichen manuell duplizierten Inhalte.

## Streamlit und Hosting

Die vorhandene Streamlit-App soll vorerst weiter lokal funktionieren.


## Technische Anforderungen

- `AGENTS.md` beachten.
- Vorhandene Python-Funktionen und Datenstrukturen bevorzugen.
- Keine Änderungen der Bilanzmethodik oder Referenzparameter.
- Für den neuen Workflow ein ausführbares `notebooks/howto_*.ipynb` erstellen oder erweitern.
- Einen kleinen, freigegebenen beziehungsweise synthetischen Beispieldatensatz verwenden.
- Tests für Export und Nachvollziehbarkeit ergänzen.
- Stable-, Development- und Schema-Version nicht vermischen.

## Abnahme

Das Arbeitspaket ist erfolgreich, wenn eine existierende PEExcel-Ergebnisgrafik

1. im bestehenden Streamlit-Dashboard weiterhin funktioniert,
2. in Jupyter angezeigt werden kann,
3. als interaktives HTML ohne Python-Server dargestellt werden kann,
4. als statische SVG-/PNG-Abbildung verfügbar ist.

**Arbeitsmodus:** Zunächst Bestandsaufnahme und minimalen Implementierungsplan vorlegen. Danach den kleinsten durchgängigen Prototyp umsetzen. Keine großflächigen Refaktorierungen und keine Deployment-Einrichtung ohne Freigabe.