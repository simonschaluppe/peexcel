# Gebäudesektor-Quick-Check: POC, 26.10.2026

## Umfang und Wiederverwendung

Gemäß präzisiertem Auftrag hat der technische Durchstich bis zur statisch
veröffentlichbaren Seite Vorrang. Fachliche Auffälligkeiten werden einmal notiert,
ohne Korrekturschleifen oder Nachsimulation. Streamlit bleibt als Referenz erhalten;
seine Stundenanalysen und lokale Dateiauswahl sind kein Teil dieses POC.

| Ergänzung | Nutzen / Lücke vorhandener Funktionen | Pflege und Konsistenz |
|---|---|---|
| `scripts/build_building_sector_results.py` | Project bietet IO, aber keinen Abgleich mit Batch-Hashes, SCEN-Snapshot und Rohspalten. | Orchestriert bestehende APIs; keine Projektklasse. Tests für Checkpoint, Korruption und Roundtrip. |
| `building_sector_project.xlsx` | Gemeinsamer regulärer IN-/OUT-Export für Folgeprojekte. | Generiertes Derivat, Quelle bleiben 217 annual-Dateien. Roundtrip vor Übernahme. |
| `validation.json` im ignorierten Ausgabeverzeichnis | Reproduzierbares Prüfprotokoll mit Quell-/Export-Hashes und Restgrößen. | Wird beim Konsolidieren erneuert; keine zweite fachliche Datenquelle. |
| Kompakte Daten in bestehender HTML-Datei | Vollständige Plotly-Figuren je Szenario skalieren schlecht. | Einmalige Report-Vorlagen, je Szenario benötigte Werte/Filter. Keine Preset-Registry, kein öffentliches Austauschformat. Immer neu generieren. |
| `scenario_scatter` / `scenario_distribution` | Vorhandene Funktionen rendern feste Bilanzreports, keine frei gewählten Szenariovariablen. | Zwei kleine Funktionen auf ProjectView mit Schema-Beschriftung; Tests für Identitäten, Einheiten und Anzahl. |
| `tests/quickcheck_browser.cjs` | HTML-Texttests führen keinen Browser aus. | Playwright mit Chromium, Netzwerkprüfung, Filter-/Kontexttests und reproduzierbarer Messung. |

Die Tabellen-I/O liest Spaltenpaare statt `iterrows` pro Szenario und erzeugt
Exportspalten gemeinsam. Schnittstellen bleiben gleich; bestehende IO-Tests laufen mit.

## Reproduktion und Einbettung

```powershell
python scripts/build_building_sector_results.py
python scripts/assessment_explained.py --output website/assets/assessment-explained/index.html
python -m nbconvert --execute --to notebook --inplace --ExecutePreprocessor.timeout=900 notebooks/howto_building_sector_results.ipynb
```

Das Notebook lädt standardmäßig den geprüften Export; `REBUILD=True` wiederholt
Konsolidierung und Roundtrip. `scripts/website_assets.py` verwendet ausdrücklich diese
Quelle. Fehlt sie, scheitert der Build statt unbemerkt das Lehrprojekt zu verwenden.
Die HTML-Datei enthält Plotly und Daten vollständig und funktioniert direkt im Browser.
Für peq-higrube dieselbe Datei einbetten; Anleitung in `assessment_explained.md`.
Veröffentlichung ist ein gesonderter Schritt. Keine zweite Implementierung im Zielprojekt.

## Technische Prüfung

- 217 Dateien, 5.400 eindeutige Namen in SCEN und Checkpoint; Dateiprüfsummen stimmen.
  Gemeinsame SCEN-Parameter stimmen mit dem eingebetteten Definitions-Snapshot überein.
  Keine fehlgeschlagenen Checkpoint-Einträge.
- 215 Dateien mit 25 Szenarien, eine mit 23 und eine mit 2, jeweils konsistent mit dem Checkpoint.
- Strenger Import ohne ignorierte Variablen; eindeutige, übereinstimmende IN-/OUT-Spalten.
- 6.458.400 vorhandene Werte im Roundtrip verglichen (rtol 1e-12, atol 1e-10),
  gleiche Identitäten/Reihenfolge. Konsolidierung ca. 485 s auf dem ausführenden Desktop.
- PV: `PV_roof_share`, Einheit `ratio`; Browseranzeige in Prozent.
  Das teilweise leere PV-Preset wird nicht als Flächenersatz benutzt.

## Interne fachliche Notizen, keine Fehlerklassifikation

- `PEI_virtual_balance_test`: 1.620 Werte außerhalb 1e-6, maximal absolut 44,1098.
  Das aktuelle Schema addiert den negativen Dichtebeitrag zu `PEI_virtual_demand`,
  der Report zeichnet ihn dagegen betragsmäßig als Bedarf. Die Metadatenformel für
  `PEI_balance` referenziert zudem den alten Namen `PEI_cf_density`. Exporte bleiben unverändert.
- `test_heat_balance`: 531 Werte außerhalb 1e-6, maximal absolut 2,45225.
  Saisonale Restgrößen sind ebenfalls vorhanden. 1e-6 ist nur eine Sichtungsschwelle,
  keine bestätigte fachliche Abnahmetoleranz. `test_EUI_balance` und
  `PEI_importexport_balance_test` sind innerhalb dieser Schwelle null.
- 14 Variablen enthalten fehlende Werte. Nicht benötigte Kennwerte enthalten teilweise
  numerische COM-Fehlercodes, etwa `GWP_emInt_batt_charge` und Kühlperiodenkennwerte.
  Sie bleiben erhalten; vollständige Häufigkeiten stehen in `validation.json`.
- `first_only`: Jahreswerte erlauben keinen sicheren Ausschluss von Zustandsüberträgen.
  Identische Ergebnisse sind kein Beweis dafür. Keine Nachsimulation.
- `gwp_ee` hat im Schema 1_13_1_dev keine Serien. Ein begrenzter Kompatibilitätszweig
  in `reporting.materialize` verwendet dann die exportierten Lebenszyklus-Summen
  `GWP_lc_EE_total`, `GWP_lc_OE_total`, `GWP_lc_total`. Python und Browser teilen damit
  Größen, Labels und Einheiten. Sobald die Schemaquelle Serien liefert, greift der Zweig nicht.

## Kontext und Auswahl

BGF/GF setzt ausschließlich GFZ. Keine Skalierung der simulierten Energieflüsse oder THG.
Der Sanierungsanteil ist NFA-gewichtet gemäß `SUMMENPRODUKT(Renovation_shares;NFA_shares)`;
die Kontextgröße ist deshalb `cfr_budget * Anteil`. Der Dichtehelfer berücksichtigt
`cutoff=0` als echte MIN-Grenze; nur `None` bedeutet keine Begrenzung.

Virtuelle Exportgrößen und Export-Saldo werden jeweils um ihre eigenen Kontextdifferenzen
fortgeschrieben. Die bekannte Differenz zur Reportdarstellung wird nicht bereinigt.
Original, Anpassung und Differenz sind sichtbar; leere Eingaben erhalten das Original.

ODER innerhalb, UND zwischen Filtern. Keine Markierung bedeutet alle Werte.
Filter verändern keine Auswahl. Auf Nutzerwunsch entfällt die ursprüngliche Grenze von 20.
Treffer-, Auswahl- und Detailansichten verwenden 80 Einträge pro Seite.
Über 100 ausgewählte Szenarien werden mit WebGL-Liniensegmenten statt SVG-Balken
gezeichnet; jedes einzelne Szenario und jeder Reportbeitrag bleibt enthalten.
Ausgefilterte ausgewählte Szenarien bleiben in der separaten Auswahlliste erreichbar.

## Erweiterung: Analysen und Notebook online

Die fünf Analyseansichten verwenden dieselben Python-Plottingfunktionen wie das
Notebook. Gemeinsame Vorlagen speichern Stil und Szenario-IDs; Jahreswerte werden
aus der vorhandenen Matrix referenziert. Nur der Endenergie-Reportsaldo benötigt
einen zusätzlichen abgeleiteten Vektor. `report_balance_scatter()` schließt die
Lücke zwischen Report und generischem Scatter: Deckung minus Bedarf wird mit
derselben Rollen-Summierung wie im bestehenden Bilanzrenderer gebildet. Dies ist
keine neue simulierte Variable. Die Browseransichten unterstützen Filtertreffer
oder Auswahl und aktualisieren Kontextgrößen mit der bestehenden Overlayfunktion.

`publish_notebook()` im bestehenden Generator veröffentlicht das ausgeführte
Notebook als Download und HTML mit eingebetteten Plotly-Ausgaben. Ein gewöhnlicher
HTML-Export zeigt die vorhandenen Plotly-MIME-Ausgaben nicht zuverlässig; deshalb
werden diese mit Plotlys HTML-Exporter umgesetzt. Pflegeaufwand: bei Änderungen
Notebook erneut ausführen und beide abgeleiteten Dateien erzeugen, keine manuell
gepflegten Daten. Tests prüfen vollständige Szenariobindungen, Reportwerte,
Auswahl ohne Obergrenze und Browserrendering sämtlicher Analyseansichten.

## Browsermessung

Erster vollständiger Lauf: Chromium 156, lokale HTML-Datei, drei Wiederholungen je
Diagrammgröße, keine externen Netzwerkanfragen. Rohdaten/Browserkennung unter
`notebooks/local_exports/building_sector/browser/browser-performance.json`.

| Messgröße | Desktop | Mobiler Viewport 390 × 844, Desktop-CPU |
|---|---:|---:|
| Laden bis initiale Diagramme | 2,98 s | 2,44 s |
| JS-Initialisierung | 431 ms | 456 ms |
| Kombinierter Filter, Median / P95 | 11,3 / 15,0 ms | 5,5 / 9,5 ms |
| Diagramme, 1 Szenario, Median | 89,5 ms | 72,5 ms |
| Diagramme, 5 Szenarien, Median | 105,6 ms | 102,8 ms |
| Diagramme, 10 Szenarien, Median | 151,2 ms | 126,3 ms |
| Diagramme, 20 Szenarien, Median | 204,8 ms | 756,5 ms |
| Verwendeter JS-Heap, ungefähr | 39,6 MB | 35,1 MB |

Browserdaten: 2.773.517 Bytes roh / 252.808 Bytes gzip. Gesamte HTML-Datei mit Plotly:
7.653.850 Bytes roh / 1.726.414 Bytes gzip. Gzip wurde lokal berechnet; tatsächliche
Transferkompression hängt vom Hosting ab. Nach Text-/Layoutänderungen nennt die
Build-Ausgabe aktuelle Größen.

Der POC ist auf dem getesteten Desktop praktikabel. Physische Mobilgeräte und das
spätere Hosting sind noch nicht gemessen. Emulation und JS-Heap sind keine vollständige
Gerätespeicher-/Netzwerkmessung. Wissenschaftliche Freigabe und echte Mobilgeräte-Abnahme
werden mit diesem POC nicht behauptet.

## Abschlusstest und Veröffentlichung

39 fokussierte Python-Tests bestanden (Gebäudesektor, bestehende Excel-I/O,
Plot-Annotationen und explizite Quick-Check-Quelle). Das neue How-to-Notebook wurde
vollständig ausgeführt. Die einzelne Quarto-Seite wurde erfolgreich gerendert.
Die umfassenderen Website-Tests finden drei bestehende Fehler in der schematischen
Gebäudeschnitt-Darstellung (`PV_roof_area_percentage` statt aktuellem Schemafeld).
Diese außerhalb des POC liegenden Funktionen wurden nicht umgebaut.

Der abschließende Browserlauf nach Verbesserung der mobilen Achsenbeschriftung
liegt unter `browser-final`: Desktop Laden 1,53 s, Filtermedian 4,1 ms,
20 Szenarien Median 71,7 ms; mobiler Viewport Laden 1,27 s, Filtermedian 3,8 ms,
20 Szenarien Median 73,8 ms. Die Hostauslastung unterscheidet sich vom ersten Lauf.
Benötigte Browserkennwerte enthalten im vollständigen Bestand keine fehlenden Werte
oder numerischen COM-Fehlercodes.

Nach ausdrücklicher Nutzerfreigabe wurden ausschließlich `assessment-explained.html`
und `assets/assessment-explained/index.html` auf dem bestehenden `gh-pages`-Branch
aktualisiert (Commit `c412993`). Der übrige Website-Bestand bleibt erhalten.
Die lokale Implementierung auf dem Arbeitsbranch wurde nicht automatisch committed.

GitHub-Pages-Deployment erfolgreich; öffentliche Seite und eingebettete Anwendung
antworten HTTP 200. Der ausgelieferte Inhalt stimmt (nach Zeilenendennormalisierung)
mit dem lokal geprüften Artefakt überein und enthält 5.400 Szenarien.
Der Browser-Abnahmetest wurde zusätzlich gegen die Live-URL ausgeführt und bestand
für Desktop und mobilen Viewport ohne zusätzliche Berechnungs-/Datenanfragen.
Messung `browser-live`: Laden Desktop 2,46 s / mobil emuliert 2,16 s,
Filtermedian jeweils 3,9 ms, 20 Szenarien Median 86,2 / 98,8 ms.

Öffentliche Anwendung: https://simonschaluppe.github.io/peexcel/assets/assessment-explained/index.html

Einbettende Seite: https://simonschaluppe.github.io/peexcel/assessment-explained.html


### Abnahme ohne Auswahlgrenze

Alle 5.400 Szenarien erfolgreich ausgewählt und alle fünf Analyseansichten gerendert.
Chromium 156: Laden lokal 1,86 / 1,78 s (Desktop / mobiler Viewport),
Filtermedian 4,1 / 4,4 ms, Aktualisierung aller 5.400 Szenarien 534 / 427 ms.
JS-Heap nach Test 81,4 MB. Mobile Messung emuliert den Viewport auf Desktop-CPU;
kein Nachweis auf physischer Mobilhardware. HTML: 8330082 Bytes, gzip: 1839141 Bytes.
Notebook vollständig ausgeführt; neun Plotly-Diagramme in der HTML-Leseansicht
im Browser ohne JavaScript-Fehler überprüft. Rohdaten: browser/browser-performance.json.
