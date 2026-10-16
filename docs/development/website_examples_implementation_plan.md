# Umsetzungsplan: Projektvergleich und dynamische elektrische Energieflüsse

Stand: 15.10.2026. Umsetzung der Jahresvergleiche und Fachsprache abgeschlossen.
Dynamische Demonstration auf Aspern F7 umgestellt. Die vollständige Erweiterung
der Stundenbilanzen ist separat in `timeseries_plot_extension.md` vorbereitet.
Die folgenden Abschnitte dokumentieren Umfang und Entscheidungen; Monatsansichten
und responsive Facettenlayouts bleiben Teil der späteren Zeitreihenerweiterung.

## Ziel

Die drei neuen Exporte bilden einen zusammenhängenden Variantenvergleich für
Wärmebilanz, Endenergiebilanz, Primärenergiebilanz und THG-Bilanz. Aspern F7 dient separat zur Darstellung vorhandener zeitaufgelöster elektrischer
Teilflüsse. Adressaten sind Energie-, Gebäude- und HKLS-Fachplaner:innen.
Website weiterhin Deutsch, nur Startseite zusätzlich Englisch.

## Geprüfter Datenbestand

| Datei unter `data/exports/` | Importierte Szenarioidentität | Verwendung |
|---|---|---|
| `Bsp_San_6G.xlsx` | `Bsp_San_6G` | Referenz des Variantenvergleichs |
| `Bsp_San_6G_pv.xlsx` | `Bsp_San_6G_pv` | Vergleichsvariante PV |
| `Bsp_San_6G_flex.xlsx` | `Bsp_San_6G_flex` | Vergleichsvariante Flexibilität |

Alle drei Dateien lassen sich mit `Project.from_excel` ohne Importwarnungen
einlesen. Jeweils 8.760 Zeitpunkte vom 01.01.2018 00:00 bis 31.12.2018 23:00,
30 SIM2-Spalten, keine doppelten Zeitstempel. Toolversion `1.13.1_dev`,
NGF 1.175,8 m² und BGF 1.469,75 m². Der Import ordnet IN/STAGE, OUT/Live und
SIM2 einem Szenario mit dem Dateistamm als Identität zu.

Die Stundenexporte enthalten elektrische Energiemengen und Hilfsspalten;
keine zeitaufgelösten thermischen Bilanzglieder oder Raumtemperaturen.
2018 ist zunächst die exportierte Zeitachse, nicht automatisch der
Bewertungsbeginn der Lebenszyklusbilanz oder eine belegte Wetterjahrangabe.

Bestehende Reports `heat_balance`, `final_energy_balance`,
`primary_energy_balance` und `gwp_ee_detail` lassen sich materialisieren.
Bei der Bestandsaufnahme waren `gwp_ee` und `district_gwp_ee` leer.
Inzwischen enthält `gwp_ee` die baulichen und betrieblichen Beiträge sowie
den exportierten Gesamtwert; `district_gwp_ee` bleibt unverändert.
`gwp_ee_detail` ist eine Aufschlüsselung grauer Emissionen und ersetzt daher
keine vollständige THG-Bilanz einschließlich Betrieb und Bewertung.

## 1. Daten- und Bilanzprüfung vor der Veröffentlichung

- Die drei Varianten mit dem bestehenden Mehrdatei-Import gemeinsam laden;
  exakte Identitäten, Schema, Zeitraster, fehlende Werte und Einheiten prüfen.
- Unterschiede der Eingaben dokumentieren: PV-Auslegung, Versorgung,
  Flexibilitätsparameter, Mobilität, Bauteile und Bewertungsannahmen.
  Bezeichnungen wie „nur PV geändert“ erst nach tatsächlichem Eingabevergleich.
- Die verfügbare Ergebnisstruktur gegen IN/OUT und Schemaformeln abgleichen.
  Summen und Komponenten nicht gleichzeitig addieren. NGF/BGF getrennt halten.
- Stundenwerte mit den entsprechenden Jahreswerten abgleichen, sofern
  Bezugsgröße, Bilanzgrenze und Aggregation identisch sind.
- Vorzeichen vor der Plot-Erstellung prüfen: `electricity_balance` verwendet
  Beträge und ordnet Vorzeichen über `positive`/`negative` zu. Das ersetzt
  keine Prüfung der fachlichen Flussrichtung.

**Konkreter Prüfpunkt im Flex-Export:** `PV_total_flex_use` ist über das Jahr
null, während flexible elektrische Aufwendungen für Heizung, Kühlung und
Warmwasser enthalten sind. Daraus folgt nicht, dass die Flexibilität unwirksam
ist: signalgesteuerter Netzbezug ist getrennt zu untersuchen. Laut Schema
umfasst `E_grid` die konventionellen Netzbezugsanteile; flexible Netzkanäle
sind separat definiert, aber in SIM2 nur teilweise vorhanden.

Die Spaltenauswahl des bisherigen Notebooks lässt sich deshalb nicht ungeprüft
als geschlossene Bilanz übernehmen. Zudem steht dort PV-Einspeisung auf der
positiven Seite neben lokal genutzter PV. Zwei Darstellungen sind zu trennen:

1. **PV-Verwendung:** Erzeugung versus direkte Nutzung, flexible Nutzung und
   Einspeisung; Vollständigkeit dieser Zerlegung an den Exporten prüfen.
2. **Elektrische Quartiersbilanz:** Erzeugung, sämtliche Bezugs-/Entladeflüsse
   versus Verbraucher, Ladeflüsse und Einspeisung; nur bei vollständiger
   Flussabdeckung als geschlossene Bilanz ausweisen.

Fehlende Kanäle werden nicht als Null ergänzt oder als vermeintlich gemessener
Restfluss rekonstruiert. Bei unvollständiger Quellenzuordnung können vorhandene
Verbrauchs- und PV-Verwendungsprofile separat veröffentlicht werden; für eine
geschlossene Stundenbilanz sind dann zusätzliche Exportkanäle erforderlich.

## 2. Zentrale Auswahl der Beispiele

`website/_examples.yml` enthält ausschließlich Pfade, exakte Szenarioidentitäten,
Anzeigetitel, Reihenfolge und die für Stundenansichten ausgewählte Variante.

```yaml
examples:
  - id: san-6g
    file: data/exports/Bsp_San_6G.xlsx
    scenario: Bsp_San_6G
    label: Referenz
  - id: san-6g-pv
    file: data/exports/Bsp_San_6G_pv.xlsx
    scenario: Bsp_San_6G_pv
    label: PV-Variante
  - id: san-6g-flex
    file: data/exports/Bsp_San_6G_flex.xlsx
    scenario: Bsp_San_6G_flex
    label: Flexibilitätsvariante
dynamic_example:
  file: data/exports/Aspern PVCheck _ F7.xlsx
  scenario: Aspern PVCheck _ F7
  label: Aspern F7
```

Pfade relativ zum Repository; keine automatische Suche nach ähnlich benannten
Dateien und keine Umbenennung der Szenarioidentitäten. Ein gemeinsamer
Website-Adapter liest die Auswahl, nutzt die bestehenden `Project`-/`Scenario`-
Objekte und erzeugt die Reports. Die Konfiguration enthält keine Ergebniswerte.

Begründung: Die bestehende hartcodierte synthetische Auswahl erlaubt keine
gemeinsame redaktionelle Auswahl realer Dateien. Eine kleine Konfiguration
vermeidet unterschiedliche Zuordnungen je Seite. Pflege: Dateinamen und Labels
bei Änderungen anpassen; Parser, fehlende Dateien, doppelte IDs und falsche
Szenarionamen testen. Kein neues Projekt- oder Zeitreihendatenmodell.

## 3. Vier Bilanzdarstellungen

| Darstellung | Inhalt und vorhandene Basis | Notwendige Prüfung/Ergänzung |
|---|---|---|
| Wärmebilanz | `heat_balance`: Transmission, Lüftung, Nachtlüftung, solare und innere Gewinne, Heizwärme- und Kühlbedarf | Vorzeichen-/Rollenkonvention, Bilanzschluss, identischer Flächenbezug; Jahresvergleich aller Varianten |
| Endenergiebilanz | `final_energy_balance`, bestehender gestapelter Vergleich | Registry derzeit vorwiegend elektrisch; weitere Energieträger aus tatsächlicher Versorgung ergänzen, interne Umverteilungen und externe Bezüge getrennt halten |
| Primärenergiebilanz | `primary_energy_balance` | Physische Versorgung und methodische Beiträge getrennt kennzeichnen: PV-Substitution, Flexibilität und Kontextfaktoren; keine Interpretation als zusätzliche Energieerzeugung |
| THG-Bilanz | Bestehende THG-Renderer; `gwp_ee_detail` für Bauteil-/Anlagendetail | Bestehende OUT-Größen für Betrieb, Mobilität, graue Emissionen und Bewertungsbeiträge identifizieren; leere THG-Registry fachlich vervollständigen, statt Bauteildetails als Gesamtbilanz auszugeben |

Jede Darstellung erhält Titel, Einheit, Bezugsfläche, Bilanzgrenze, Zeitraum,
Quellen-/Versionsangabe und eine kurze fachliche Ergebnisinterpretation.
Alle drei Varianten werden nebeneinander dargestellt; Farben und Reihenfolge
der Beiträge bleiben konsistent. Werte und Differenzen sind per Hover sowie
in einer zugänglichen Ergebnistabelle verfügbar.

THG: Klimawirkungskategorie GWP100, Betrachtungszeitraum, Klimazieljahr und
Dekarbonisierungspfad getrennt benennen. Biogene Beiträge und andere negative
Werte nicht durch Betragsbildung verlieren. PV-LCA bleibt modellierbar, wird
aber aus der ka-Bewertung entsprechend der Vorgabe ausgeschlossen. Änderungen
betreffen die Darstellung vorhandener Ergebnisse, keine neue Bewertungsmethode.

## 4. Dynamische Teilflussansichten für Aspern F7

**A. Saisonale mittlere Tagesprofile:** `add_season` und
`pexl.plot.electricity_balance_facets` aus dem bestehenden Notebook wiederverwenden.
Vier Jahreszeiten, gleiche Skala, Tagesstunden 0–23, zentrale Legende.
Stundenenergie in Wh/m² wird erst durch Division durch die geprüfte
Zeitschrittdauer als mittlere Leistung in W/m² dargestellt. Ein saisonaler
Mittelwert ist ausdrücklich kein realer Tagesverlauf.

**B. Chronologische Stundenverläufe:** Bestehenden `electricity_balance`-Renderer
für ein wählbares Zeitfenster nutzen. Monats-/Wochenauswahl, Zoom, Zurücksetzen,
konkrete Winter- und Sommerwochen mit sichtbarem Datum. Vorbelegte Wochen sind
Orientierungsfenster, keine behaupteten statistisch repräsentativen Wochen.
Keine Animation erforderlich; die zeitliche Auflösung und Auswahl tragen den
fachlichen Nutzen.

**C. Monats-/Jahresübersicht:** Energien je Monat summieren; Tagesprofile und
chronologische Wochen bilden ergänzende Ansichten derselben Datenaufbereitung.
Nur tatsächlich vollständige Teilbilanzen gemeinsam darstellen. Fehlende
thermische Stundenkanäle werden nicht aus elektrischen Verbräuchen abgeleitet.

**Interaktion und Layout:** Beiträge über die Legende schalten, technische
Bezeichnungen statt „Flex 1“ ohne Erläuterung, einheitliche Hover-Einheiten,
keine unnötigen Nullserien. Saisonfacetten auf Desktop nebeneinander, mobil
untereinander oder einzeln auswählbar. Die vorhandene Funktion setzt bisher
eine Zeile voraus: zunächst vorhandene Figure-/Subplot-Möglichkeiten nutzen;
nur falls notwendig einen optionalen Layoutparameter mit unverändertem Default
ergänzen. Keine neue Plotfamilie und keine Umgehung des vorhandenen Renderers.

## 5. Integration und Fachsprache

- `examples.qmd`: zentraler Variantenvergleich mit Projektkennwerten, Eingabe-
  unterschieden und den vier Bilanzen. Reale Ergebnisse ersetzen die synthetischen
  Beispiele als primären Anwendungsnachweis; synthetische Methodentests bleiben
  bei Bedarf in der technischen Dokumentation.
- `systems.qmd`: ausgewählte elektrische Flussprofile von Aspern F7.
- `results.qmd`, `climate.qmd`: fachliche Einordnung der realen Ergebnisse und
  Links auf Detailansichten; keine ungesicherten Kausalaussagen zur Flexwirkung.
- Startseite: kompakter realer Variantenvergleich als Funktionsnachweis;
  Verweise auf technische Dokumentation und Anwendungsabläufe.
- Fachseiten durchgehend redaktionell überarbeiten, einschließlich Navigation,
  Buttons, Diagrammtexte und Notebook-Einführungen. Direkte Aufforderungen wie
  „Erkunde“, „Selbst ausprobieren“, „Lernziel“, „Aufgabe“ und „Lösungshinweis“
  durch „Systemgrenze“, „Modellannahmen“, „Eingangsdaten“, „Auswertung“,
  „Ergebnisinterpretation“ und „Prüfschritte“ ersetzen.
- Beispiele: „Innere Wärmen“ → „Interne Wärmegewinne“;
  „Lüften“ → „Elektrischer Energiebedarf der Lüftung“;
  „Lehrschnitt“ → „Schematischer Gebäudeschnitt“;
  „Lernen“ → „Dokumentation und Arbeitsabläufe“.
- Kein informelles Du, weniger dekorative Emojis; vorhandene technische
  Symbolik und informative Grafiken erhalten. Fachbegriffe präzise verwenden:
  Wärmebedarf, elektrische Endenergie, Leistung und Primärenergie nicht vermischen.
- Modellannahmen und verbindliche Deklarationswerte bleiben sichtbar getrennt.
  Der bestehende API-Wert `style="teaching"` bleibt aus Kompatibilitätsgründen;
  benutzerseitig wird „reduzierte Schnittdarstellung“ verwendet.

## 6. Build, Wiederverwendung und Artefakte

Import → bestehende Scenario-Zeitreihen → gemeinsame Aggregation/Validierung →
Report/Plot → `export_figure` → Quarto. Notebook und Website verwenden dieselben
Funktionen. Keine Berechnungslogik in JavaScript oder QMD duplizieren.

Vorbereitete Plotly-HTML-Dateien und SVG/PNG-Ansichten bleiben unter dem
ignorierten `website/assets/`. Nur ausgewählte Kanäle werden eingebettet;
keine automatische Veröffentlichung vollständiger Arbeitsmappen. Monats- und
Saisonansichten sind kompakt, Stundenansicht wird bei Bedarf geladen.

Die realen Beispielartefakte werden bei jedem Build aus der Konfiguration
erneuert; der bisherige „nur erzeugen, wenn fehlend“-Mechanismus ist hierfür
ungeeignet. Herkunft im vorhandenen Provenienzformat inklusive Dateiname,
Szenario, Tool-/Schemaversion und Zeitbasis. Kein zusätzliches persistiertes
Zwischenformat oder eigener Cache notwendig. Wartungsaufwand bleibt bei
Quellenwahl, Schema-Mappings, Aggregationstests und visueller Prüfung.

Notwendige THG-/Endenergie-Serien werden in der vorhandenen Registry ergänzt,
nicht in einer parallelen Website-Tabelle gepflegt. Auswirkungen auf bestehende
Reports und Renderer durch Regressionstests prüfen. Technische Labels möglichst
an ihrer bestehenden zentralen Quelle berichtigen.

## 7. Ausführbare How-tos und Abnahme

1. `howto_analyze_electricity_balance.ipynb`: konfigurierter Aspern-F7-Export statt lokalem
   Nextcloud-Pickle; saisonale Profile, Stundenfenster, Einheiten und Bilanzprüfung.
2. `howto_publication.ipynb`: Auswahl über zentrale Konfiguration, vier reale
   Bilanzberichte, Provenienz und Export.
3. `howto_website.ipynb`: Build der ausgewählten Beispiele und Einbettung.
4. Tests: Import/Identitäten, Lücken und Zeitraster, Aggregationen,
   Einheiten/Bezugsflächen, keine Doppelzählung, THG-Grenzen und negative Werte,
   Fehler bei fehlenden Daten, unveränderte Defaults der vorhandenen Renderer.
5. Notebooks ausführen, Quarto bauen, lokale Links prüfen, Desktop/Mobilansicht
   sowie Legendensteuerung, Zeitfenster und Tastaturbedienung visuell abnehmen.

Reihenfolge: Bilanzprüfung → Konfiguration und gemeinsame Aufbereitung → vier
Jahresbilanzen → dynamische Ansichten → fachsprachliche Überarbeitung → Abnahme.
Der erste Prüfschritt entscheidet, ob für eine vollständige dynamische
Quartiersbilanz zusätzliche SIM2-Kanäle benötigt werden. Vorhandene Profile
und Jahresergebnisse können unabhängig davon genutzt werden.

## Umgesetzte Bilanzabgrenzungen und Pflege

- Alle drei Varianten enthalten bereits PV. Der IN-Vergleich zeigt ausschließlich
  Unterschiede in Flexibilitäts-Preset, `FLEX_PV_is_used` und `FLEX_is_used`.
  Die verbindlichen aktuellen Anzeigetitel stehen in `_examples.yml`.
- Lokale elektrische Endenergiebilanz: Einspeisung und externe EV-Ladung sind
  keine lokale Deckung; direkte elektrische Warmwasserbereitung gehört zum Bedarf.
- Wärme- und Endenergiebilanz schließen numerisch. Die THG-Komponentensumme
  entspricht dem exportierten Gesamtwert. Die Primärenergiedifferenz ist ein
  Bewertungsergebnis, kein physisches Schließkriterium.
- Schemaänderungen erfolgen in `CHART_metadata.csv`; das vorhandene Python-Modul
  wird daraus regeneriert. Keine neue öffentliche Plot-Schnittstelle.
- Die einzige neue handgepflegte Struktur ist `_examples.yml` zur gemeinsamen
  Quellenauswahl. PyYAML wird im bestehenden Publication-Extra benötigt.
- Zusätzliche CSV-Tabellen enthalten ausschließlich reproduzierbare Reportwerte,
  IN-Unterschiede, Bilanzprüfungen und Kanalverfügbarkeit. Sie ermöglichen Download
  und nachvollziehbare Prüfung; Plot-HTML allein bietet keinen tabellarischen
  Zugriff darauf. Sie werden zusammen mit HTML/SVG/PNG bei jedem Build erneuert,
  bleiben ignorierte Artefakte und sind kein Importformat oder dauerhaftes API.
  Pflege und Tests liegen bei den gemeinsamen Funktionen in `website_examples.py`.
- Drei aktualisierte How-tos verwenden dieselben Funktionen wie der Website-Build.

## Abnahme am 15.10.2026

230 Tests bestanden; nach der visuellen Layoutkorrektur zusätzlich alle fünf
Beispieltests erneut bestanden. Alle drei aktualisierten How-tos erfolgreich
ausgeführt. Quarto: 20 Seiten; 1.018 lokale Link-/Assetziele ohne fehlende Datei.
THG- und Primärenergiedarstellungen visuell geprüft; F7-Zeitfenster im Browser
umgeschaltet und Überlappungen von Titel, Auswahl, Slider und Provenienz behoben.
Mobile Seite geprüft: breite Diagramme bleiben horizontal scrollbar; die
kompakte Facettenanordnung ist Teil der geplanten Zeitreihenerweiterung.
