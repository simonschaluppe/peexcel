# Umsetzungsplan: PEExcel als Anwender- und Lernwebsite

Stand: 15.10.2026. Anwenderseiten und Lehrmodule lokal implementiert. Die folgenden
Planabschnitte dokumentieren auch die ursprüngliche Ausbauperspektive; der aktuelle
Umfang und die Abnahme stehen am Ende. Konkrete Projektbeispiele einschließlich
Konfigurationsdatei und Stundenexplorer sind auf Nutzerwunsch zurückgestellt.

Abgestimmt: Website und Tutorials auf Deutsch; zusätzlich nur die Startseite auf Englisch.
Die englische Startseite benennt ausdrücklich die deutschsprachige Tooloberfläche
und verlinkt die deutschen Lernwege. README auf kurzen Einstieg kürzen.
Simulierte Zeitreihen bleiben im ersten Umsetzungsschritt ausdrücklich außen vor.
Neue Varianten einschließlich Stundenexporten werden vom Nutzer bereitgestellt.

## Ziel und redaktionelle Verantwortung

Adressaten sind professionelle PEQ-Kompetenzpartner und Studierende, die Quartiere
modellieren, bewerten und zur Deklaration vorbereiten. Die Website übernimmt alle
Informationen der bisherigen README und ergänzt sie um geführte Lernwege und echte
Beispiele. Sie wird die maßgebliche Quelle der Anwenderdokumentation. Die README
wird nach der Migration ein kurzer Repository-Einstieg mit Installationshinweisen
und Website-Link. Diese neue Vorgabe ersetzt die ursprüngliche Anforderung,
Toolinformationen ausschließlich in der README zu pflegen. Der Changelog bleibt
die maßgebliche Versionshistorie.

Leitweg: verstehen → Beispiel erkunden → Tool herunterladen → eigenes Quartier
modellieren → Ergebnisse interpretieren → Nachweis vorbereiten.

## Geprüfter Bestand

- `docs/PEQ Nachweistool 2026-10-14.pptx`: 36 Folien, 97 eingebettete Medien.
  Texte und Gliederung geprüft; PDF-Folien 11 und 13 zusätzlich visuell geprüft.
- Bestehende README: Zielgruppen, drei Bewertungsstufen, Funktionen, Downloads,
  Schnellstart, Python, Dokumentation, Methodik, Repository-Struktur, Publikationen,
  Newsletter, Kontakt, Lizenz/Nutzung und drei eingebundene Bildreferenzen.
- `data/exports/ka_project_backup_v1_13.xlsx` enthält `GNICE | QC Flexibel` sowie
  `GNICE | Quick-Check`, `GNICE | Quick-Check_2`, `GNICE | QC Flex GFZ 2,2` und
  `GNICE | Sanierung Zellulose`.
- Tabellen: IN, OUT, PV-Import und Wetter. Für die Zielvariante liefert der
  bestehende Import keine ScenarioTimeseries. Wetter-/PV-Eingaben sind keine
  simulierten Last-, Speicher- oder Temperaturverläufe dieser Variante.
- Der Section-Renderer liefert SVG mit Element-IDs, data-kind und teilweise
  semantischen IDs. Er stellt schematische Geometrie dar, kein vermessenes Gebäude.
- Die jetzige Website ist ein Exportprototyp; ihre Verweise zur README werden
  durch vollständige, strukturierte Inhalte ersetzt.

## Seitenstruktur und vollständige Inhaltsmigration

| Bereich | Inhalte | Hauptaktion |
|---|---|---|
| Start | Logo/Bilder, Nutzen, Zielgruppen, drei Qualitätsstufen, Funktionsüberblick, GNICE-Vorschau | Beispiel erkunden / Tool starten |
| Loslegen | Systemvoraussetzungen, Stable/Development, Download, Makros, erster Modellierungsablauf | Erstes Quartier bearbeiten |
| Quartiere modellieren | Eingaben, Nutzungen, Flächen, Bauphysik, Technik, PV, Speicher, Mobilität, Presets, Import/Export | Tutorial durchgehen |
| Ergebnisse verstehen | Energieflüsse, Bilanzen, Flexibilität, Mobilität, THG, Kontextfaktoren, Plausibilität/AUDIT | Ergebnis am Beispiel untersuchen |
| Beispiele | GNICE als zusammenhängende Fallstudie, später Vergleich ausgewählter Varianten | Varianten und Zeiträume vergleichen |
| Lernen & Nachschlagen | Geführte Tutorials, HTML-Handbuch, Übungen, Downloads von PDF/PPTX, Suche/Glossar | Passenden Lernweg wählen |
| Python & Forschung | Gerenderte How-tos, Notebook-Downloads, API, Repository-Struktur, Publikationen, Hintergrundbericht | Analyse reproduzieren |
| Über das Tool | FH Technikum Wien, klimaaktiv-Kontext, Entwicklung, Kontakt, Newsletter, Lizenz/Zitieren | Kontakt / Newsletter |

In der Hauptnavigation höchstens sechs Einträge; Unterseiten über Seitenleisten.
Download dauerhaft sichtbar. Die ausführliche Struktur oben wird entsprechend
gruppiert, nicht als acht gleichrangige Navigationspunkte ausgespielt.
Eine Migrationscheckliste ordnet jeden README-Abschnitt und jedes Bild einer Zielseite
zu. Bestehende Inhalte werden erst nach dieser Vollständigkeitskontrolle gekürzt.

Sprachen: deutsche Seiten bleiben am bisherigen Ort; eine englische Startseite
unter `website/en/index.qmd` übernimmt Nutzen, PEQ/PED-Einordnung, Funktionsvorschau,
Download und Kontakt. Sprachwechsel nur zwischen den beiden Startseiten.
Verweise von dort auf Tutorials tragen den Hinweis „German“. Keine englische
Doppelpflege von Handbuch, Methoden, Plotlabels und Notebooks. Gemeinsame Assets,
Beispielkonfiguration und Daten für beide Startseiten wiederverwenden.

## Visualität und Vermittlung

- Logo, PEQ-Stufengrafik, vorhandene Illustrationen und verständliche Icons
  übernehmen. Die Symbolfamilie 🏙️ 🧱 🔥 ❄️ 💨 💧 🌞 🔋 🚗 ☁️ bleibt bei ihren Themen.
- Farben für Bauteile und Energieflüsse konsistent zur Präsentation und bestehenden
  Plots verwenden. Icons erhalten Textlabels; Information nie nur über Farbe vermitteln.
- Bilder aus PPTX möglichst als originale Vektor-/Bildassets übernehmen; komplexe
  zusammengesetzte Zeichnungen gezielt exportieren. Quellenfolie im Asset-Kommentar
  dokumentieren. Keine gesamte Schulung als schwer lesbare Folienbilder ablegen.
- Texte als suchbares HTML mit kurzen Erklärungen und anklickbaren Vertiefungen.
  Original-PDF/PPTX zusätzlich anbieten; ausgewählte Originalfolien bei Bedarf
  als vergrößerbare Referenz einbetten.
- Jede Demo beantwortet eine konkrete Frage und endet mit einem passenden Tutorial.
  Beispiel: „Wann hilft Flexibilität?“ → Sommer-/Winterwoche erkunden → Regelung im Tool einstellen.
- Fachlicher Einstieg ohne Python; Code in der Vertiefung aufklappbar. Für Studierende
  Lernziel, Aufgabe und Lösung; für Kompetenzpartner Eingabecheck, Ergebnisdeutung
  und Nachweisbezug auf denselben fachlichen Seiten.

## Umsetzung der Schulungsunterlagen

| Folien | Webdarstellung |
|---|---|
| 1–6 | Toolvorstellung, Einsatzbereich und fachliche Einordnung; DE/EN-Dubletten zusammenführen |
| 7–8, 24–30, 34–35 | Geführtes Tutorial: Eingeben → Presets wählen → Simulieren → Variante speichern → Prüfen |
| 9–10, 15–16 | Energieflussgrafik mit einzeln hervorhebbaren Quellen, Speichern, Verbrauchern und Deckungsreihenfolge |
| 11–12 | Zwei thermisch entkoppelte Zonen; einzeln aktivierbare Wärmeflüsse, klare Trennung von Wärmebilanzgrenze und dargestellter Geometrie |
| 13–14 | Interaktive Bauteilzuordnung: Auswahl in Liste und Schnitt synchron; thermische Hülle als eigene Ebene |
| 17–20 | Mobilität: physische Lade-/Speicherflüsse und verursacherbezogene Bewertungsbilanz getrennt erklären |
| 21 | Flexibilität anhand tatsächlicher Zeitreihen, Konversionsfaktoren und ausgewählter Vergleichsvarianten |
| 22–23 | THG-Systemgrenze, kumulierte Beiträge, Budget und Zeitachse; Zeitraum, Zieljahr und Dekarbonisierungspfad getrennt beschriften |
| 31 | Eigene Tutorials für Energieausweis, Wetter, PV und baubook/Eco2Soft |
| 32–33 | GNICE-Beispiel mit Bilanzplots und später Stundenexplorer |
| 36 | Kontakt und weiterführende Zugänge |

## Freie Modellierung und klimaaktiv-Deklaration

Fachliche Klarstellung des Toolautors vom 15.10.2026: Das Tool erlaubt auch
Konfigurationen außerhalb der klimaaktiv-Bewertungsmethode. **Deklarationswerte
sind verbindliche Vorgaben für die Deklaration, keine technischen Grenzen des
Modells.** Das Vorhandensein eines Parameters oder Ergebnisses bedeutet nicht,
dass dieser Beitrag in die Deklarationsbewertung eingeht.

| Thema | Freie Modellierung | klimaaktiv-Deklaration |
|---|---|---|
| PV-LCA | Im Tool modellierbar | In der ka-Bewertungsmethode nicht berücksichtigt |
| Stündliche Konversionsfaktoren | Eigene Annahmen modellierbar | Vorgeschriebene Deklarationswerte verwenden |
| Nutzerstrom | Abweichende Annahmen modellierbar | Vorgeschriebene Deklarationswerte verwenden |
| Innere Wärmegewinne | Abweichende Annahmen modellierbar | Vorgeschriebene Deklarationswerte verwenden |

Damit ist die vermeintliche Diskrepanz zur PV-LCA auf Folie 22 aufgelöst.
Keine pauschale Übertragung dieser Aussage auf andere Anlagen oder andere
Bewertungsverfahren. Bei jedem Thema erläutern: Was ist modellierbar? Was ist
für die Deklaration vorgeschrieben? Was geht in die Bewertung ein?

Redaktionelle Darstellung: kurze Kästen „Modellierung“ und „Für die Deklaration“
mit konkretem Versionsbezug, Eingabefeld und Quellenverweis. Ein Modellierungsergebnis
wird nicht ohne Prüfung als Deklarationsnachweis bezeichnet. AUDIT zeigt relevante
Abweichungen; keine selbst erfundene Zulässigkeitsprüfung im Frontend. Zahlenwerte
werden aus den vorhandenen, versionierten Quellen übernommen, nicht hier festgeschrieben.
Auch 2025–2050, 2025–2075 und Klimaziele 2040/2050 behalten getrennte Bezugsrahmen.

## Section-Renderer: Stil, Fachebenen und Interaktion

Die bestehende Geometrie bleibt Grundlage. `architectural`, `hand_drawn` und
`blueprint` bleiben erhalten. Neu geplant ist **ein** Stil `teaching`;
„Wärmeflüsse“, „Bauteile“ oder „thermische Hülle“ werden ausdrücklich keine Stile.

| Ebene | Geplanter Inhalt | Verändert Geometrie oder Berechnung? |
|---|---|---|
| Stil `teaching` | Weißer Hintergrund, ruhige neutrale Raumflächen, kontrastreiche Linien, große Schrift, reduzierte Umgebung und getrennte Legenden | Nein; nur Sichtbarkeit und Darstellung |
| Overlay `components` | Bauteilfarben und Schraffuren gemäß Schulung, anklickbare Zuordnung zur Bauteilliste | Nein |
| Overlay `thermal_boundary` | Hervorgehobene Wärmebilanzgrenze, Legende; innere Decken nicht als Außenhülle markieren | Nein; benötigt belegte Randbedingungen |
| Overlay `thermal_zones` | Gekühlt/ungekühlt, gekennzeichnete Modellzuordnung, thermische Entkopplung | Nein; keine Ableitung aus Nutzung/Farbe |
| Overlay `heat_flows` | Pfeile für Transmission, Lüftung, Nachtlüftung, Solar- und innere Gewinne, Heizung/Kühlung | Nein; zunächst rein qualitativ |
| Bestehende HVAC/PV-/Nutzungsdarstellung | Vorhandene Geräte und Nutzungen bei passendem Lernziel zuschalten | Nein; keine zusätzlichen Anlagen annehmen |
| Auswahl/Fokus | Hervorhebung, Tooltip und Textpanel; Tastatur- und Touchbedienung | Nein; kurzlebiger UI-Zustand |

### Geometrie und Bauteilzuordnung

- `section_layout_from_scenario` und `render_svg` bleiben die einzige Geometrie-
  und Zeichenbasis. Lehrschnitt und Projektschnitt sind klar getrennt.
- Einfache erste Lehrgeometrie: zwei vollständig beheizte Geschosse ohne Keller.
  Fünf belegte Kategorien: Außenwand, Fenster, Dach, Bodenplatte beheizt, innere
  Geschoßdecke. Diese Zuordnung gilt ausdrücklich nur für dieses Lehrmodell.
- Zweite Lehrgeometrie für die vollständige Zuordnung: beheizte/unbeheizte Keller,
  Erdberührung, Rücksprung/Terrasse, Außendecke, Balkon; danach Rahmen/Glas,
  tragende/nichttragende Innenwände und Stützen. Fehlende Geometrieelemente erst
  nach Prüfung der vorhandenen Layout-/Komponentenprimitive ergänzen.
- Alle 20 LCA-Kategorien werden in der Liste erklärt. Nur vorhandene und eindeutig
  zugeordnete Komponenten werden im jeweiligen Schnitt hervorgehoben. „Nicht im
  Schnitt dargestellt“ ist zulässig und besser als eine falsche Zuordnung.
- Kanonische Schema-/Bauteilnamen und vorhandene IDs wiederverwenden. Zusätzliche
  semantische Attribute nur für fehlende Kategorie, thermische Randbedingung und
  Quellenbezug. Keine pauschale Zuordnung aller `slab`-Elemente zur Kellerdecke.
- Thermische Hülle aus belegten Randbedingungen zusammenstellen. Keine allgemeine
  Rechteck-Umrandung für gestufte Gebäude, unbeheizte Räume oder Balkone verwenden.
  Die rechteckige Kontur im Prototyp gilt ausschließlich für dessen einfache Geometrie.

### Wärmefluss-Overlay konkret

| Größe | Symbol | Qualitative Darstellung |
|---|---|---|
| Solare Gewinne | Qₛ | Durch Fenster nach innen |
| Innere Gewinne | Qᵢ | Entstehung innerhalb der Zone; keine Außenquelle suggerieren |
| Transmission | Qₜ | Beispiel Verlustfall nach außen; tatsächliche Richtung zeitabhängig |
| Lüftung | Qᵥ | Beispiel Wärmeabfuhr; keine Luftmengen oder Leistungen ableiten |
| Nachtlüftung | Qₙᵥ | Gemäß Lehrmodell nur in der ungekühlten Zone |
| Heizung | Qₕ | Wärmeeintrag; in beiden Zonen möglich |
| Kühlung | Q꜀ | Wärmeabfuhr; nur in der aktiv gekühlten Zone |

- Zunächst jede Modellzone einzeln umschaltbar, ohne Verbindungspfeil zwischen
  thermisch entkoppelten Zonen. Die Geschosse im Lehrschnitt sind **keine** zwei
  thermischen Zonen. Fachliche Fluss-Semantik gilt unabhängig vom Zeichenstil.
- Pfeile über Außen-/Innenankern positionieren. Außenbeschriftungen reservieren
  eigene Ränder; Zahlen und Texte nicht über Fassaden/Fenster legen.
- Keine Animation zur bloßen Dekoration. Keine erfundenen kW/kWh oder aus der
  Pfeildicke abgeleiteten Mengen. Späterer Datenmodus nur bei vorhandenen, eindeutig
  zugeordneten Zeitreihen; Null, fehlender Wert und Vorzeichenwechsel unterscheidbar.
- Auf Handybreite Bedienelemente untereinander, Text weiterhin mindestens 15–16 px.
  Schnitt darf innerhalb seines Bereichs horizontal verschoben werden, anstatt
  Beschriftungen unlesbar zu verkleinern. Legende und Erklärung bleiben außerhalb
  der Grafik lesbar. Auswahlfarbe plus Kontur/Schraffur verwenden.

### Umsetzung und Wartungsaufwand

1. Stil in den vorhandenen Style-Tokens ergänzen; für alle Stile dieselben
   semantischen Geometrieelemente behalten. Lehrstil blendet störende Umgebung,
   unnötige Maßketten und Dekoration aus; die bisherigen Stile ändern sich nicht.
2. Fachliche Zuordnung von der Farbgebung trennen. Bestehende Section-Dictionaries
   erweitern nur dann, wenn Randbedingungen nicht anders belegbar sind; zusätzliche
   persistierte Felder vor Einführung separat begründen. Erste Lehrmodelle enthalten
   explizite Annahmen, keine scheinbar aus GNICE berechneten Kategorien.
3. Ein gemeinsamer Overlay-Zeichner verwendet vorhandene SVG-Anker/IDs; Notebook
   und Website teilen ihn. Für die spätere Paket-API ein optionaler `overlays`-
   Parameter an `render_svg` prüfen, Standard leer. Noch keine öffentliche API im Prototyp.
4. Kleine HTML/JavaScript-Bedienung steuert nur Sichtbarkeit, Auswahl und Erklärungen;
   Berechnungen bleiben Python/Excel. Statischer Export des gewählten Zustands muss
   dieselben Farben, Pfeile, Legende und Hinweise enthalten.
5. Tests: unveränderte Geometrie/Werte, eindeutige IDs, korrekte Bauteilzuordnung,
   Kühlung/Nachtlüftung je Zone, fehlende Daten, Druckdarstellung, Lesbarkeit und
   Tastaturbedienung. Ausführbares How-to gehört zur Abnahme.

Die optionale Overlay-Schnittstelle wäre nötig, weil vorhandene `annotations` nur
Beschriftungen und vorhandene HVAC-Darstellungen Geräte darstellen, jedoch keine
Wärmebilanzflüsse. Pflegeumfang: ein Satz semantischer Anker, ein gemeinsamer Zeichner,
Zuordnungs-/Darstellungstests. Keine neue Plotting- oder Simulationsarchitektur.

### Bereits ausführbarer Prüfprototyp

`scripts/section_teaching_preview.py` erzeugt aus dem bestehenden Renderer eine
reduzierte Schnittansicht mit drei Ansichten: Bauteile, Hülle, Wärmeflüsse. Dabei
werden vorhandene SVG-Primitive kopiert; ihre Koordinaten werden nicht neu berechnet.
Die Zuordnung/Anker sind bewusst auf das dokumentierte Lehrmodell beschränkt.
Der Prototyp ist ein Review-Hilfsmittel, keine allgemeine Paketfunktion.

Start: `python scripts/section_teaching_preview.py`. Ergebnis:
`notebooks/local_exports/section_teaching/index.html`. Das begleitende
`notebooks/howto_section_teaching_preview.ipynb` verwendet dieselbe Funktion.
Generierte HTML/SVG/Bilder bleiben ignorierte und reproduzierbare Prüfartefakte.

Prüfung vom 15.10.2026:

- 49 Tests bestanden: neuer Lehrschnitt-Prototyp sowie bestehende SVG-/Stiltests.
  Übernommene Geometriekoordinaten sind unverändert; innere Decke und Bodenplatte
  sind unterschiedlich zugeordnet; SVG-IDs sind eindeutig.
- How-to-Notebook vollständig mit Jupyter ausgeführt, ohne Zellfehler.
- Browser-Sichtprüfung: Bauteile, Hülle und Wärmeflüsse auf Desktop; Mobilansicht
  bei 390 px Breite. Gefundenen Seitenüberlauf korrigiert: nur die Grafik scrollt
  horizontal, Text/Bedienelemente bleiben innerhalb der Seite. Die Vergleichstabelle
  wird mobil zu untereinander angeordneten Einträgen.
- Browser-Funktionstest: gekühlt zeigt Kühlung ohne Nachtlüftung; ungekühlt zeigt
  Nachtlüftung ohne Kühlung; Ausblenden entfernt sämtliche Flusspfeile; innere
  Geschoßdecke per Enter auswählbar, mit sichtbarem Fokus und Erklärung.
- Screenshots: `notebooks/local_exports/section_teaching/desktop-flows.png`,
  `desktop-hull.png` und `mobile-flows.png` im selben Verzeichnis.
- Grenzen: fünf Bauteilkategorien, feste Lehrgeometrie, qualitative Flüsse;
  noch kein generischer Lehrstil in der Paket-API, kein Export des gewählten
  Overlay-Zustands und keine vollständige 20-Kategorien-Zuordnung.

## Konfiguration der echten Beispiele

Empfehlung: eine kleine zentrale `website/_examples.yml`; jede Seite referenziert
den Eintrag über eine ID. Das verhindert unterschiedliche Dateipfade und
Variantenschreibweisen zwischen Jahresbilanz, Schnitt und Tutorial. Quarto erlaubt
auch Dokument-Metadaten; direkte Seitenkonfiguration bleibt eine mögliche spätere
Alternative. In der ersten Version nur einen zentralen Ladeweg implementieren.

Vorgeschlagenes Format (noch kein implementierter Vertrag):

```yaml
examples:
  gnice-flex:
    title: "GNICE – flexible Versorgung"
    project_file: "data/exports/ka_project_backup_v1_13.xlsx"
    variants:
      - "GNICE | QC Flexibel"
    timeseries_files: {}  # später: exakter Variantenname → SIM2-Exportpfad
```

Pfade relativ zum Repository, Varianten exakt wie die Excel-Spaltennamen.
Seitenauswahl z. B. `example: gnice-flex` im YAML-Frontmatter; der kleine Website-
Build-Adapter liest diesen Verweis. Quarto lädt dadurch nicht automatisch Excel.

Build-Ablauf: Konfiguration prüfen → `Project.from_excel` → exakte Auswahl →
vorhandene Reporting-/Plot-/Section-Funktionen → nur ausgewählte Ergebnisse ausgeben.
SIM2-Dateien werden über den vorhandenen Import geladen und ausdrücklich der Variante
zugeordnet. Keine automatische Zuordnung allein über ähnlich klingende Dateinamen.
Fehlende Variante: verständlicher Fehler mit vorhandenen Namen. Fehlende Stundenwerte:
klarer Hinweis und kein erfundener Zeitverlauf. Fehlende Bilanzserien/Einheiten:
sichtbar melden, keine plausibel aussehende Nullbilanz erzeugen.

Begründung der neuen Konfigurationsdatei: bisher hartcodiertes synthetisches Beispiel
erlaubt keine redaktionelle Auswahl. Persistiert werden nur Pfade, Namen und
Darstellungsoptionen, keine zweite Kopie von Ergebnisdaten. Pflegeaufwand: Einträge
bei umbenannten Dateien/Varianten ändern; Parser und Validierung testen. Generierte
Assets werden bei jedem Build ersetzt und bleiben ignoriert. Notebook und Website
verwenden dieselbe Lade-/Auswahlfunktion.

## Dynamische Zeitreihen und Notebook-Einbettung

Nach Rückmeldung des Nutzers zurückgestellt: zunächst keine Zeitreihen-Demo und
keine Ersatzdaten. Die folgenden Punkte beschreiben ausschließlich den späteren Ausbau.

Erster Stundenexplorer nach Lieferung eines passenden SIM2-Exports: Zeitfenster
wählen/zoomen, Sommer-/Winterwoche, Strombedarf, PV, Bezug/Einspeisung und vorhandene
Speichergrößen. Danach Temperatur-/Wärmeflussansicht und Variantenvergleich.
Einheiten, Leistung versus Energie, Aggregation, Zeitzone und Datenlücken prüfen.
8760-Stunden-Daten nur für benötigte Kanäle publizieren; umfangreiche Abbildungen
bei Bedarf laden. Browserinteraktion funktioniert mit vorberechneten Daten auf
GitHub Pages. Neue Excel-Simulationen werden dort nicht ausgeführt.

How-tos als lesbare HTML-Tutorials darstellen, mit ausgewählten eingebetteten
Notebook-Ausgaben und Download des ausführbaren Originals. Bestehende Analyse-
Notebooks wiederverwenden, keine Berechnungen in QMD/JavaScript nachbauen.
`howto_publication.ipynb` für Konfiguration und echte Varianten erweitern;
`howto_visualize_project.ipynb` für neue Schnittinteraktionen erweitern.

Quarto-Referenzen:
- https://quarto.org/docs/projects/quarto-projects.html
- https://quarto.org/docs/authoring/notebook-embed.html

## Reihenfolge und Abnahme

1. Inhalte/Assets zuordnen, README-Migrationsliste und fachliche offene Punkte klären.
2. Navigation, Start, Download, erster Lernweg; vorhandene Bilder und Icons übernehmen.
3. Zentral konfiguriertes GNICE-Beispiel mit Jahresbilanz, nachvollziehbarer Herkunft
   und geeignetem schematischen Schnitt. Projektwerte vor Interpretation prüfen.
4. Thermische Hülle/Bauteilzuordnung aus Folien 11–14 als interaktives Lehrmodul.
5. Später, nach Bereitstellung neuer Varianten: passenden Stundenexport anbinden,
   Flexibilitätsdemo und Vergleich ergänzen. Kein Hindernis für die erste Website.
6. Weitere Methodik-/Tutorialseiten, Publikationen, Kontakt, Newsletter und Lizenz
   migrieren; README kürzen; Veröffentlichung gesondert behandeln.

Abnahme: alle README-Inhalte zugeordnet; GNICE gezielt geladen; Variantenwechsel
ohne Codeänderung; keine Null-/Synthetic-Fallbacks bei fehlenden Daten; Darstellung
auf Desktop und Mobilgeräten geprüft; Bedienung per Tastatur; lokale Links korrekt;
Quarto-Build erfolgreich; relevante Tests und beide How-tos ausführbar; Grafiken
und Tutorials verwenden die vorhandenen Implementierungsfunktionen.

Abgestimmt: Deutsch als Website-/Toolsprache, nur Startseite zusätzlich Englisch;
README kürzen; Zeitreihen vorerst zurückstellen. PV-LCA ist fachlich geklärt:
modellierbar, aber nicht Teil der ka-Bewertungsmethode. Deklarationswerte sind für
die Deklaration verbindlich; frei modellierte Varianten werden entsprechend bezeichnet.


## Umsetzung der Anwenderwebsite (15.10.2026)

Umgesetzt: deutsche Fach- und Lernseiten, nur englische Startseite, Navigation und
Suche, README-Migration, öffentliche Downloadauswahl, Notebook-Lesefassungen,
Lehrstil `teaching`, interaktive Hüllen-/Wärmeflusslektion und zweiter Kellerfall.
Konkrete Projekte, neue Varianten, `_examples.yml` und Stundenexplorer bleiben
zurückgestellt. Der vorhandene synthetische Beispielinhalt bleibt unverändert.
Eine Veröffentlichung gehört nicht zu diesem lokalen Umsetzungsschritt.

### README-Migration

| Bisheriger Inhalt | Neue Quelle |
|---|---|
| Zweck, Zielgruppen, Logo, Funktionen, drei Stufen und Stufengrafik | `index.qmd`, `model.qmd` |
| Downloads, Versionen, Voraussetzungen und Schnellstart | `download.qmd`, `start.qmd` |
| Python, Gebäudeschnitte, Publikationsworkflow und Notebooks | `python.qmd`, `envelope.qmd` |
| Handbuch, Broschüre, Hintergrundbericht und Präsentation | `download.qmd`, `learn.qmd` |
| Methodischer Überblick | `results.qmd`, `mobility.qmd`, `climate.qmd`, `declaration.qmd` |
| Repository-Struktur und Projektleitlinien | `about.qmd` |
| Sechs Publikationen und bisherige Schlussillustration | `research.qmd` |
| Newsletter, Kontakt, Lizenz und Nutzung | `about.qmd` |

Die drei bisherigen README-Bildreferenzen bleiben erhalten. Bauteil- und
Mobilitätsgrafik werden aus `docs/` kopiert. Original-PDF/PPTX bleiben unverändert.

### Schnittstellen, Artefakte und Pflegeaufwand

- `render_svg(..., style="teaching")` ist die einzige neue öffentliche Option.
  Nutzen: dieselbe neutrale Strukturansicht in Website, Notebook und Python.
  Die bestehenden Stile enthalten Umgebung, Haustechnik und Beschriftungen, die
  für die Lehrüberlagerungen stören. Der Stil übernimmt bestehende Geometrie und
  IDs; keine neue Geometriestruktur. Er blendet Annotationen, Anlagen, dekorative
  Innenwände/Schächte und Nutzungslabels aus; `annotations=True` wird abgewiesen.
  Pflege: Anpassungen an semantische Renderer-Elemente prüfen, Geometrieerhalt
  und bestehende Stile testen. Fachebenen sind keine weiteren Stilnamen.
- Lehrüberlagerungen bleiben in `scripts/section_teaching_preview.py` und
  `scripts/component_teaching.py` als ausdrücklich definierte Lehrannahmen.
  Keine generische automatische Projektklassifikation und kein neues Layoutschema.
  Der Kellerfall zeigt 7 eindeutig zugeordnete Kategorien; alle 20 Kategorien
  aus dem versionierten Schema stehen zur Auswahl. Terrassen, Balkone, tragende
  Innenwände, Stützen und weitere fehlende Elemente werden als nicht dargestellt
  bezeichnet. Rahmen/Glas bleiben zusätzliche Schemafelder ohne eigene Geometrie.
  Die Erweiterung beliebiger Projektschnitte um solche Elemente bleibt ein
  gesonderter Geometrieausbau; hierfür wurde keine fiktive Geometrie ergänzt.
- `scripts/website_assets.py` erzeugt ignorierte `media/`, `downloads/`,
  `tutorials/` und Lehrmodule unter `assets/`. Nutzen: portable relative Links,
  Originalquellen bleiben maßgeblich. Bestehende Markdown-Links allein betten
  weder lokal verfügbare Unterlagen noch Notebook-Inhalte in den Build ein.
  Eine explizite öffentliche Dateiauswahl verhindert pauschales Kopieren von
  `docs/` oder Projektdateien. Pflege: Auswahl bei neuen Quellen aktualisieren;
  fehlende Quellen brechen den Build ab. Keine zweite Ergebnisdatenablage.
- Notebook-Lesefassungen und Downloadkopien entfernen gespeicherte Ausgaben.
  Sie werden nicht beim Seitenbuild ausgeführt. Abnahme führt die betroffenen
  How-tos separat aus; Implementierungsfunktionen sind dieselben wie im Build.
- Der Pre-Render-Schritt erzeugt fehlende bisherige synthetische Grafikartefakte
  mit dem unveränderten Generator für frische Checkouts. Vorhandene vollständige
  Artefakte werden nicht aktualisiert. Reale Excel-Projekte werden nicht geladen.

### Lokaler Ablauf

`python -m pip install -e ".[publication]"`, Quarto und Chrome bereitstellen;
`quarto render website`. Details und ein ausführbarer Build in
`notebooks/howto_website.ipynb`. Die neue Rendereroption sowie beide Lehrmodule
sind in `notebooks/howto_section_teaching_preview.ipynb` nachvollziehbar.


### Abnahme des lokalen Website-Standes

- Gesamte Testsuite: 225 bestanden. Nach der abschließenden Notebook-Normalisierung
  zusätzlich alle sechs Website-/Lehrmodultests erneut erfolgreich.
- Beide How-tos vollständig mit Jupyter ausgeführt; `howto_website` nach der
  Exportkorrektur nochmals. Ausgaben unter `notebooks/local_exports/`.
- Quarto rendert ausschließlich die 20 QMD-Seiten; Notebook-Downloads werden
  bewusst nicht als weitere Quarto-Seiten entdeckt oder ausgeführt.
- Browser: Wärmefluss-Zonenwechsel, Einzelfluss-Schalter, SVG-Download,
  Kellerdecken-Auswahl und fehlende Kategorien geprüft. Desktop 1280 px und
  Mobilansicht 390 px: kein Seitenüberlauf, Diagramme scrollen intern.
- Exportiertes SVG als XML eingelesen; gewählte Zone, Legende und Lehrannahmen
  enthalten. Das SVG ist ein aktueller Darstellungszustand, keine Simulation.
- Die Stufengrafik wird als lokaler, nachvollziehbar reproduzierter PDF-Ausschnitt
  eingebettet. Reproduktion und Pflege stehen in `website/illustrations/README.md`.
  Die übrigen früheren README-Bildreferenzen bleiben erhalten; externe GitHub-
  Bilder werden als HTML eingebunden, damit Quarto ihre URLs nicht umschreibt.

Keine neue Projektvariante, kein neuer Stundenexport, keine Veröffentlichung.

Abschließender Linkcheck: 1.026 lokale Link-, Bild- und iframe-Ziele geprüft,
keine fehlenden Dateien. Screenshots: `notebooks/local_exports/website_review/`.
Der lokale Prüfserver wurde anschließend beendet.
