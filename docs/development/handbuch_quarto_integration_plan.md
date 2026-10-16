# Handbuch in Quarto integrieren: Fachinhalt und Excel-Bedienung

Umsetzungsstand vom 16.10.2026: Navigation und Inhalte lokal in Quarto umgesetzt,
30 Seiten erfolgreich gerendert. Noch nicht veröffentlicht. Die folgenden
Planungsabschnitte dokumentieren die inhaltliche Zuordnung des Handbuchs;
Hinweise auf dessen Abbildungen sind durch die aktuelle Bildauswahl ersetzt.

**Verbindliche Quellenentscheidung:** Ausschließlich die 14 bereitgestellten
PNG-Abbildungen aus `docs/website/` werden für diese Erweiterung verwendet.
Keine Grafiken aus dem alten Handbuch extrahieren. Fachliche Formulierungen
orientieren sich an der Schulungspräsentation vom 14.10.2026. Bestehende
interaktive Schaubilder und Ergebnisplots bleiben erhalten.

**Umgesetzt:** eigene Seiten für Presets, Migration, Blattnavigation, HKLS,
PV-Eingabe, Nutzungsparameter, Variantenverwaltung, Variantenvergleich,
Batch-Simulation und Excel-Dashboard; Ergebnisblatt und Python-Explorer
getrennt, Mobilität und Ökobilanz unter Modellieren. Excel-Orte, Eingabefelder,
Aktionen, Auswahlwerte, Bedienabläufe und Deklarationshinweise sind semantisch
formatiert. `howto_website` und `howto_excel` wurden vollständig ausgeführt.

**Noch benötigte aktuelle Ansichten:** Ergebnisblatt mit den vier Bilanzen;
Scen mit Auswahl und Ausführung; PV-Dachflächenskalierung und Profilimport;
Eco2soft-Import; Projekt-Export/-Import und Variantenverwaltung; HKLS- und
Nutzungsparameter sowie Nachweis-/AUDIT-Ansichten. Diese Stellen sind auf den
Seiten ausdrücklich als Ergänzungsbedarf markiert. Eine tatsächliche Migration
zwischen zwei Excel-Versionen ist damit noch nicht abgenommen.

## Grundlage und Befund

Gelesen: `docs/Handbuch zur Nachweisführung.pdf`, 94 Seiten, Stand Jänner 2026.
Seitenangaben unten sind PDF-Seiten und stimmen hier mit der gedruckten Zählung
überein. Die Seiten 8, 20, 21, 36, 40, 45, 63, 69 und 86 wurden zusätzlich
gerendert und visuell geprüft. Die vorhandenen QMD-Seiten, `styles.css` und
`excel/ribbon/customUI14.xml` wurden abgeglichen. Die Ribbon-Datei belegt die
Bezeichnungen im Repository, noch nicht ihre Übereinstimmung mit der ausgelieferten
Arbeitsmappe. Vor Implementierung der Bedienpfade ist deren Version zu prüfen.

Das Handbuch kombiniert einen Ablauf (S. 7–35) und eine Blattreferenz (S. 36–92).
Die Website hat bereits gute Fachseiten, aber wenig feldgenaue Bedieninformation.
`start.qmd` enthält inzwischen farbige `.excel-menu`-Elemente und einen kurzen
Preset-Hinweis. Diese Arbeit wird weitergeführt. Besonders zu korrigieren ist die
Mehrdeutigkeit von „Dashboard“: `dashboard.qmd` beschreibt derzeit Streamlit,
während das Handbuch damit das Excel-Blatt meint.

## 1. Informationsarchitektur

Zwei Zugänge, eine gemeinsame Beschreibung pro Thema:

- **Aufgabenbezogen:** Einstieg → Projekt und Modell → Anlagen → Auswertung → Nachweis.
- **Nach Excel-Ort:** Blatt-/Ribbon-Navigator → konkreter Abschnitt auf derselben Fachseite.

Kein zweites vollständiges Handbuch neben den Fachseiten. Der Blattnavigator
verlinkt auf stabile Anker und zeigt Blattname, Zweck und Dokumentationsziel.
Auch die Suche soll ältere Namen wie „Erg“, „var“, „Global Warming Potential“
finden. Solche Aliase werden dort einmal erklärt, nicht als parallele Bedienpfade.

Vorgeschlagene Navigation:

| Gruppe | Seiten |
|---|---|
| Tool-Anwendung | `start.qmd` – Einstieg; `presets.qmd` – Schnelleinstieg mit Presets; `excel-navigation.qmd` – Orientierung im Excel-Tool; **`migration.qmd` – Migration auf eine neue Toolversion**; `download.qmd` |
| Modellieren | `model.qmd` – Quartier und Modellaufbau; `envelope.qmd` – Thermische Hülle; `components.qmd` – Bauteilzuordnung; `hvac.qmd` – Heizung, Kühlung, Warmwasser und Lüftung; **`pv.qmd` – PV-Eingabe**; **`systems.qmd` – Speicher und Flexibilität**; `usage.qmd` – Nutzungsparameter; `interfaces.qmd` – Wetter und weitere Datenquellen; `mobility.qmd` – Mobilität; `climate.qmd` – Ökobilanz; **`variants.qmd` – Varianten verwalten** als letzter Eintrag |
| Analysieren und Bewerten | **`results.qmd` – Ergebnisblatt**; **`excel-dashboard.qmd` – Excel-Dashboard**; **`comparison.qmd` – Variantenvergleich**; **`batch.qmd` – Automatische Batch-Simulation (Scen)**; `examples.qmd` – Anwendungsbeispiele; `declaration.qmd` – Nachweisführung einschließlich Qualitätssicherung |
| Dokumentation und Python | `learn.qmd`; `python.qmd`; `dashboard.qmd` mit Titel **Python-Szenarioexplorer**; `glossary.qmd`; `research.qmd`; `about.qmd` |

Die eigenständigen Seiten folgen konkreten Aufgaben und Excel-Bedienorten.
`systems.qmd` wird ausschließlich als Fachseite **Speicher und Flexibilität**
weiterentwickelt; eine allgemeine Systemübersicht liegt bei `model.qmd`.
`climate.qmd` wird zur Ökobilanzseite. Bestehende URLs bleiben erhalten.
Neue Seiten enthalten redaktionelle Inhalte und nutzen vorhandene Funktionen;
keine zusätzlichen Rechenmodelle oder Parameterdatenbanken entstehen.

Die Ökobilanz ist eine ausdrücklich so benannte, eigenständige Seite unter
Modellieren. Dazu wird `climate.qmd` weiterentwickelt, statt eine zweite Seite
mit denselben Inhalten anzulegen. Ihr Excel-Ort ist das Blatt
**☁ Treibhauspotential** (Handbuch: „Global Warming Potential“); der Navigator
und der Kopf der Seite nennen diesen Zusammenhang. S. 69–71 liefern passende
Inhalte: bauliche Maßnahmen, TGA, Fahrzeugherstellung, Presets, Sammelmaßnahmen,
LCA-Direkteingabe, fossile/biogene Anteile und Lebensdauern. Die Eingabe und
Modellierung stehen hier; THG-Ergebnisanalyse und Nachweiskriterien sind mit
`results.qmd` bzw. `declaration.qmd` verbunden. Für fachlich oder versionsbezogen
noch ungeklärte Teilabschnitte ausdrücklich „In Vorbereitung“ mit benanntem
Excel-Ort vorsehen, keine unbelegten Details ergänzen.

Variantenverwaltung (anlegen, speichern und laden) erhält `variants.qmd` als
eigene Seite am Ende von Modellieren. Einstieg und Presets verlinken dorthin.
Die vergleichende Auswertung erhält `comparison.qmd` als eigene Seite unter
Analysieren und Bewerten: Auswahl der Varianten im Excel-Blatt **Variantenvergleich**,
Diagrammbereiche, identische Bezugsgrößen und Interpretation der Unterschiede.
Die realen Beispielplots werden von dort verlinkt, ersetzen diese Bedienreferenz
aber nicht.

### Migration auf eine neue Toolversion

Eine eigene Seite `migration.qmd` unter Tool-Anwendung, zusätzlich vom Einstieg
und Download verlinkt, beschreibt den Ablauf **Projektexport im alten Tool →
Projektimport im neuen Tool**:

1. Ausgangsdatei und Versionsstand sichern; zu übertragende aktuelle Eingaben
   als Varianten speichern.
2. Im alten Tool das Projekt mit den benötigten Varianten exportieren und die
   Exportdatei getrennt von der Arbeitsmappe ablegen.
3. Die neue Toolversion als eigene Arbeitsdatei öffnen und vorbereiten.
4. Die Projektdatei im neuen Tool importieren. Im Repository-Ribbon heißt der
   Befehl „⬇️ Projekt-Datei importieren“ in der Gruppe „Projekt-Varianten“.
5. Importierte Projekte/Varianten prüfen, Hinweise zu neuen oder geänderten
   Parametern bearbeiten und die Varianten im neuen Tool neu berechnen.
6. Alten und neuen Rechenstand einschließlich Version dokumentieren; Änderungen
   an Methodik, Defaults oder Berechnung können Ergebnisabweichungen verursachen.

Die endgültige Anleitung benennt den verifizierten Exportdialog, Importdialog
und die Auswahl der Varianten, jeweils mit Abbildung und `.excel-path`.
Exportumfang, Übernahme eigener Wetter-/PV-Profile und Behandlung unbekannter
Parameter sind anhand des tatsächlichen Migrationswegs zu prüfen; vollständige
Übernahme oder unveränderte Ergebnisse werden nicht pauschal zugesichert.
Fehlende belegte Details erhalten vorläufig einen klar benannten Platzhalter.
Kein manuelles Kopieren alter Berechnungsblätter als Migrationsverfahren empfehlen.
Für eine anschließende Deklaration führt ein Link zur Qualitätssicherung in der
Nachweisführung; die technische Importkontrolle bleibt Teil der Migration.

### Qualitätssicherung in der Nachweisführung

Der bisherige Abschnitt „Qualitätssicherung“ auf `start.qmd` wird nach
`declaration.qmd#qualitaetssicherung` verschoben. Dort werden Vollständigkeit,
Plausibilität, Deklarationswerte, Datenquellen, Version/Rechenstand und die
Behandlung von AUDIT-Hinweisen zusammen mit der Nachweisdokumentation beschrieben.
Tool-Anwendung und Migration verlinken dorthin. Qualitätssicherung erscheint
nicht als eigenständiger allgemeiner Einstiegsabschnitt.

## 2. Vollständige Zuordnung des Handbuchs

### Ergänzte Seitenabgrenzung

- **PV-Eingabe (`pv.qmd`):** zwei explizite Arbeitswege. Vereinfacht über
  Dachflächen-Skalierung; detailliert über ein hinterlegtes stündliches
  Erzeugungsprofil. Beide Wege führen zur PV-Konfiguration und Ergebnisprüfung.
  Blatt **PV** und Blatt **PV-Import** getrennt markieren: Profil hinterlegen,
  anschließend auswählen und konfigurieren. Dachfläche, zugrunde liegendes
  Referenzprofil, Skalierung und Verluste erläutern; genaue Feldnamen und
  Umrechnung anhand der aktuellen Arbeitsmappe prüfen. Wetterbezug, Zeitraster
  und Einheiten beim detaillierten Import angeben. Die vollständige Bedienung
  liegt auf dieser Seite; `interfaces.qmd` enthält nur einen Verweis darauf.
- **Speicher und Flexibilität (`systems.qmd`):** eigene Seite mit dem zugehörigen
  Blatt **Flexibilität und Speicher**. PV-Überschussnutzung, externe Signale,
  thermische Gebäudemasse, Warmwasserspeicher und Batterie jeweils mit Eingabeort,
  Freigaben, Parametern und Ergebniskontrolle. PV-Erzeugung nach `pv.qmd`,
  EV-Parameter nach `mobility.qmd` verlinken. F7-Demonstrationsprofile nach
  `examples.qmd` verlagern und von hier sowie vom Excel-Dashboard verlinken.
- **Ökobilanz (`climate.qmd`):** Abschnitt „Verknüpfung mit Eco2soft“ ergänzen.
  Eco2soft als Werkzeug für die vorgelagerte Gebäudeökobilanz einordnen; die
  Übergabe in das Blatt **☁ Treibhauspotential** über passende Bauteil-/
  Sammelmaßnahmen oder LCA-Direkteingaben beschreiben. Bezugsfläche, Module,
  Betrachtungszeitraum und fossile/biogene Beiträge vor der Übernahme abgleichen;
  Doppelzählung von Detail- und Gesamteingaben vermeiden. Eine automatische
  Schnittstelle nur beschreiben, falls tatsächlich belegt; andernfalls die
  konkrete manuelle Übertragung dokumentieren. Offene Feldzuordnungen werden
  als Platzhalter mit dem benötigten Eco2soft-Ergebnis gekennzeichnet.
- **Varianten verwalten (`variants.qmd`):** am Ende von Modellieren. Neue Variante
  anlegen, eindeutig benennen, Projekt zuordnen, Eingaben speichern und vorhandene
  Variante laden; Überschreiben und aktiven Bearbeitungsstand erklären. Verweise
  auf Presets, Migration, Vergleich und Batch-Simulation. Die Auswertung selbst
  bleibt auf den Analyseseiten.
- **Ergebnisblatt (`results.qmd`):** ausschließlich das Blatt **Ergebnisse (Erg)**
  und die dort vorhandenen Diagramme/Tabellen: Projektkennwerte, Wärmebilanz,
  Endenergiebilanz, Flexibilitäts-/Batteriekennwerte, Primärenergie und THG.
  Je Diagramm Excel-Position, dargestellte Größen, Einheiten und Interpretation.
  Keine Dashboard-Bedienung, kein Variantenmanager und keine als Excel-Screenshot
  dargestellten Python-Plots. Diese Funktionen werden nur verlinkt.
- **Excel-Dashboard (`excel-dashboard.qmd`):** eigene Seite für das Blatt
  **Dashboard**. Zuerst Auswahl des Zeitraums und der zeitlichen Auflösung
  einschließlich stündlicher Auswahl für Wochen-/Monatsfenster erläutern, dann
  Pivot-Aktualisierung und die einzelnen dynamischen Diagramme. Je ein Abschnitt
  zu Strombedarf/-nutzung, Stromdeckung, Wärmegewinnen/-verlusten der gekühlten
  und ungekühlten Bereiche sowie Speicherzuständen (Raumtemperatur/Gebäudemasse,
  Warmwasser, EV, Batterie). Abbildungen S. 31–35 und 83–86 gezielt aufteilen und
  mit den aktuellen Diagrammtiteln abgleichen. Zeitfilterwirkung und Aggregation
  ausdrücklich benennen; Energie, Leistung, Temperatur und SOC unterscheiden.
  Weitere tatsächlich vorhandene Dashboard-Diagramme, etwa Monatsverteilungen
  und Absenkpfade, mit ihrem eigenen Zeitbezug ergänzen. F7-Website-Plots separat
  verlinken; deren begrenzter Exportumfang ist keine Einschränkung des Excel-Dashboards.
- **Automatische Batch-Simulation (`batch.qmd`):** eigene Seite unter Analysieren
  und Bewerten mit Excel-Ort **Blatt Scen**. Zweck: große Anzahlen von Varianten
  automatisiert berechnen. Geplanter Ablauf: Varianten vorbereiten/auswählen,
  Batch konfigurieren und starten, Fortschritt und Fehler prüfen, Ergebnisse
  zuordnen und im Variantenvergleich auswerten. Konkrete Spalten, Schaltflächen,
  Speicherung und Exportmöglichkeiten gegen die Arbeitsmappe prüfen. Der bisher
  ausgewertete Handbuchbestand beschreibt diesen Ablauf nicht ausreichend:
  entsprechende Abschnitte und Abbildungen zunächst als „In Vorbereitung“
  anlegen. Keine erfundenen Scen-Befehle oder Garantien zur Wiederaufnahme.

Die neuen Excel-Abläufe für Migration und Batch werden bei der Umsetzung in
`howto_excel.ipynb` dokumentiert; automatisierbare Import-/Auswertungsschritte
nutzen die bestehenden Implementierungsfunktionen. Die tatsächlichen Excel-
Bedienabläufe werden zusätzlich an einer Arbeitsmappe geprüft. Eine erfolgreiche
Notebook-Ausführung allein bestätigt weder Migration noch Scen-Batchbetrieb.

| Handbuch | Ziel in Quarto | Zu übernehmender Inhalt und Abbildungen |
|---|---|---|
| S. 1–3, 6 | `learn.qmd#handbuch`, `download.qmd`, `about.qmd` | Handbuchstand, Quelle, Download, Impressum; Inhaltsverzeichnis als Website-Navigator, keine abfotografierte PDF-Inhaltsseite |
| S. 4–5 | `declaration.qmd#nachweisablauf`, `interfaces.qmd#datenquellen` | Datenerhebung, externe Werkzeuge, Mobilitäts-/PV-/LCA-Nachweise, Auditbericht; Datenquellen als HTML-Tabelle |
| S. 7–10 | `start.qmd#arbeitsdatei`, `#beispiel-laden`, `#berechnen` | Lokale Arbeitsdatei, Makros, Berechnungsmodus, Beispiel laden, Neu berechnen; Ausschnitte aus S. 8–10 für Ribbon, Ladedialog und Berechnung |
| Ergänzung: Versionsmigration (Nutzervorgabe; S. 37 nur allgemeine Import-/Exporthinweise) | `migration.qmd` | Projektexport im alten Tool, Import im neuen Tool, Varianten/Parameter prüfen, neu berechnen; verifizierte Dialogabbildungen ergänzen, offene Exportdetails als Platzhalter |
| Ergänzung: Dachflächen-Skalierung (Nutzervorgabe), S. 29 und 61 | `pv.qmd` | Vereinfachte PV-Eingabe über Dachflächen und detaillierte Eingabe über stündliches Profil; Blatt PV / PV-Import; Bedienreferenz aus interfaces hierher verlagern |
| Ergänzung: Batch-Simulation (Nutzervorgabe) | `batch.qmd` | Blatt Scen; automatisierte Berechnung vieler Varianten; konkrete Bedienung und Abbildungen nach Toolprüfung, bis dahin Platzhalter |
| S. 5 und 69–71 | `climate.qmd#eco2soft` | Eco2soft als vorgelagerte Ökobilanz, Ergebnisübernahme ins THG-Blatt, Systemgrenze und Bezugsgrößen abgleichen; Übertragungsdetails verifizieren |
| S. 10–13, 36–40 | `excel-navigation.qmd` | Blattgruppen, Ribbon, Eingabe-/Default-/Deklarationswerte, berechnete Zellen, ausgeblendete Detailblätter; Ribbon-Abbildung S. 36, Blattregister S. 10/20, Formatierungslegende S. 40 |
| S. 11–14, 41–43 | `model.qmd#quartier-eingeben` | Projekt/Variante, Standort und Wetterauswahl, BGF je Nutzung, NGF/BGF, Raumhöhe, Grundstücksfläche/GFZ, Sanierungsanteil; Screenshots S. 11–13, Tabellen S. 41–43 als durchsuchbare Feldreferenz |
| S. 20–25 | `presets.qmd` und Verweise zu `hvac.qmd` | Presets auf Blatt und im Ribbon, Überschreiben von Parametern, Fernwärme- und Lüftungsbeispiel; S. 21 zeigt beide Zugänge, S. 23–25 die Lüftungskonfigurationen |
| S. 25–27, 37, 87–88 | `variants.qmd`, `comparison.qmd` | Projekt-/Variantenname, speichern, laden, Auswahl im Vergleich, Diagrammbereich; Dialog S. 26, Auswahl S. 27, Vergleich S. 87 |
| S. 28, 44 | `interfaces.qmd#wetter` | Wetterimport versus Auswahl in Quartier; HELIOS-PC, Stundenraster und Eingangsgrößen; Importabbildung S. 28 |
| S. 29, 61–62 | `pv.qmd#profilimport`, `pv.qmd#dachflaechen-skalierung` | Profil einfügen/benennen, kW bzw. kWh je Stundenintervall, 8.760 Werte, Wetterkonsistenz; anschließend Auswahl, Skalierung und Verlustfaktor im Blatt PV; Abbildung S. 29, Feldreferenz S. 61; thermische Erzeugung/Abwärme als gesonderte Detaileingabe S. 62 |
| S. 45–48 | `envelope.qmd#excel-bauphysik` | Opake/transluzente Flächen, Orientierungen, U-/g-Werte, Wärmebrücken, n50, Verschattung, mobiler Sonnenschutz, Speichermasse; Referenzblöcke als HTML; Schnittgrafik jeweils mit zugehörigem Excel-Block verbinden |
| S. 49–51 | `hvac.qmd#heizung` | Solltemperatur, Abgabesystem, vier Erzeugerslots, Energieträger, Leistung, Erzeugungseffizienz, Verteilung/Hilfsstrom, Heizperiode; Detailausschnitt S. 20/21 und Tabellen S. 49/50 |
| S. 52–54 | `hvac.qmd#kuehlung` | Gekühlter NGF-Anteil, Solltemperatur, FreeCooling, drei Erzeugerslots, raumseitige Leistungsgrenze und Kühlperiode; Querverweis auf Nachtlüftung und thermische Zonen |
| S. 55–57 | `hvac.qmd#warmwasser` | Zwei Systeme, nutzungsbezogene Zuweisung, Wirkungsgrade/Verluste, Bedarf und Speicherbemessung; flexible Temperaturanhebung nur verlinken nach `systems.qmd` |
| S. 23–25, 58–60 | `hvac.qmd#lueftung` | Mindestluftwechsel, mechanischer Anteil/Fensterlüftung, WRG Winter/Sommer, Lüfterstrom und Nachtauskühlung; Preset-Abbildungen mit Verweis auf tatsächliche Parameter |
| S. 30, 63–65 | `systems.qmd#excel-flexibilitaet` | PV- und Signalnutzung getrennt, Freigaben je Anwendung, Gebäudemasse, Systemwahl, Temperaturband, Batterie/C-Rate/Wirkungsgrade, WW-Speicherung; Übersicht S. 30 und Referenzfelder S. 63–65 |
| S. 66–68 | `mobility.qmd#excel-mobilitaet` | MIV aktivieren, vereinfachtes/detailliertes Verfahren, Mobilitätstool-Reduktionsfaktor, E-Mobilitätsanteil, Ladepunkte, Wirkungsgrade, interne/externe Mindest-SOC, bidirektionales Laden; Feldtabellen thematisch aufteilen |
| S. 69–71 | **Ökobilanz** unter Modellieren: `climate.qmd#excel-thg`, ergänzend `components.qmd#excel-zuordnung` | Blatt ☁ Treibhauspotential / Global Warming Potential explizit nennen; THG-Systemgrenze und Bewertungszeit; Bauteilkategorien, Vorauswahl, Sammelmaßnahmen, LCA-Direkteingabe, Fossil/Biogen, Lebensdauer; TGA/Mobilitätsherstellung. Bauteilreferenz S. 70 direkt neben Schnitt und Zuordnung, TGA S. 71 bei THG-Eingaben |
| S. 72–73 | `usage.qmd` | Nutzerstrom-Skalierung, interne Wärmegewinne, Allgemeinstrom, Beleuchtung/Tageslichtsteuerung, Nutzungsprofile; editierbare Modellannahmen und Deklarationswerte unterscheiden |
| S. 14–18, 74–82 | `results.qmd#jahresbilanzen` | Ergebnisübersicht, Wärmebilanzen gekühlt/ungekühlt, Heiz-/Kühlperioden, Endenergie-Matrix, Flexibilitäts-/Batteriekennwerte, PE-Bedarf/Deckung und Import/Export, THG; Screenshots S. 14–18 als Orientierung, Ergebnisse S. 75–82 als Feld-/Bilanzreferenz; hier ausschließlich Diagramme und Tabellen des Excel-Ergebnisblatts; reale Website-Plots bleiben auf `examples.qmd` |
| S. 31–35, 83–86 | `excel-dashboard.qmd` | Zeitachse, Aggregation, Pivot-Aktualisierung, thermische/elektrische Verläufe und Speicherzustände; S. 32 für Bedienung, S. 33/34/86 für Diagrammgruppen. F7 als separater Website-Export mit eigener Vollständigkeitsangabe |
| S. 18–19, 89–91 | `declaration.qmd#excel-nachweise` | PEQ, PEQ+M, KN PEQ, Zielwert/Projektwert/Differenz, Übernahme in Auditbericht; Deklarationsblatt S. 18/19, Tabellen S. 90/91 als erläuterte Ergebnisfelder |
| S. 4, 13–14, 40 und bestehender Website-Abschnitt Qualitätssicherung | `declaration.qmd#qualitaetssicherung` | Projektbezogene Daten, verbindliche Deklarationswerte, Plausibilitätsprüfung, AUDIT-Hinweise und Nachweisdokumentation; aus `start.qmd` hierher verlagern |
| S. 92 | `model.qmd#simulationsmodell`, Querverweis `systems.qmd` | Simulationsübersicht als Originalabbildung mit Textalternative; Verknüpfung zum bestehenden interaktiven Systemmodell |
| S. 93–94 | `about.qmd` | Programm-/Kontaktinformationen und Quellenhinweis, nach Aktualitätsprüfung |

## 3. Einheitlicher Aufbau jeder Fachseite

1. **Kurzbeschreibung und Excel-Ort:** Aufgabenstellung und direkt sichtbarer Pfad
   zum Blatt/Abschnitt; kein Aufklappen nötig, um den Ort zu finden.
2. **Fachlicher Zusammenhang:** Systemgrenze, Größen, Einheiten und Modellwirkung;
   vorhandene Schnittgrafiken/Plots hier beibehalten.
3. **Im Excel-Tool:** konkrete Schritte, Originalbezeichnungen, Eingabefelder,
   zugeschnittener Screenshot und erwartete Änderung.
4. **Eingaben im Detail:** HTML-Tabelle mit Feld, Einheit/Bezug, Bedeutung,
   Eingabeart und Deklarationsbindung. Lange Referenzen optional aufklappbar.
5. **Ergebnis prüfen:** zuständiges Ergebnisblatt und Diagramm/Tabellenblock,
   z. B. Änderung der Lüftung → Wärmebilanz UND elektrischer Lüftungsbedarf.
6. **Für die Deklaration:** nur die zusätzlich verbindlichen Bedingungen;
   weiterführende methodische Quellen und Handbuchseite am Ende.

Nicht jedes Thema braucht sechs sichtbare Großkapitel. Kurze Bedienblöcke stehen
direkt beim zugehörigen Fachabschnitt. Ein Bedienhinweis soll immer einen
vollständigen Weg aus Ort, Handlung und Ergebnisprüfung enthalten.

## 4. Formatierung: Ort, Bedienung und fachlicher Inhalt

Die vorhandene `.excel-menu` bleibt die Basis für **Blattmarkierungen** mit
Excel-Farben/Icons. Sie wird nicht auf beliebige Fachbegriffe oder alle Klicks
angewendet. Farbe kennzeichnet den Bereich, die sichtbare Beschriftung den Typ.

| Element | Gestaltung / vorgeschlagene Klasse | Beispiel |
|---|---|---|
| Tabellenblatt | `.excel-menu` plus bestehende Farbklasse; kompakter rechteckiger Tab, vorangestellt „Blatt“ | Blatt **🔥 Heizung** |
| Menübandpfad | `.excel-path`: heller neutraler Hintergrund, umbruchfähige Folge; „Menüband“ als Klartext | Menüband: klimaaktiv PEQ → Heizung → Auswahl Heizsystem |
| Abschnitt im Blatt | `.excel-section`: dunkle Schrift, dezente untere Linie, keine Button-Anmutung | Abschnitt **Heizsysteme** |
| Tatsächliche Excel-Aktion | `.excel-action`: umrandete, kompakte Textmarke, mit „Befehl“/Handlungsverb im Satz | Befehl **Aktuelle Eingabe speichern** |
| Eingabefeld | `.excel-field`: hellgrün/dunkelgrün, eckiger Rahmen; exakte Feldbezeichnung | Feld **Maximale Heizleistung** |
| Auswahleintrag / Preset | `.excel-value`: neutral hinterlegter Wert in Anführungszeichen | Preset **„Fernwärme“** |
| Tastatur | natives `<kbd>` | F9 |
| Bedienabschnitt | `.excel-operation`: dezente getönte Fläche, linke Linie, Titel „Im Excel-Tool“ | Ort + nummerierte Schritte + Screenshot + Kontrolle |
| Methodische Erläuterung | normaler Satzspiegel, Titel „Fachlicher Zusammenhang“; optional `.method-note` für Vertiefung | Kaskade der Heizsysteme |
| Deklarationsbindung | `.declaration-note`: beschrifteter Hinweis „Für die Deklaration“, separate Textmarke | Deklarationswert; Modellvariation möglich |

Wichtig: **Eingabeart und Verbindlichkeit sind zwei verschiedene Eigenschaften.**
Ein grünes Eingabefeld kann zugleich einen Deklarationswert enthalten. Deshalb
separate Kennzeichnung „Eingabe“, „Default“ oder „berechnet“ und zusätzlich
„Deklarationswert“. Kein Schloss-Symbol für Werte, die technisch veränderbar sind.
Erklärung: „Im Modell variierbar; für die Deklaration den vorgegebenen Wert verwenden.“
PV-LCA erhält stattdessen „Modellierbar; in der ka-Bewertung nicht berücksichtigt“.

Die Stilklassen stellen nur Dokumentation dar. Sie lösen keine Excel-Aktion aus.
Nur echte Website-Verweise erhalten Linkverhalten; keine Scheinschaltflächen,
Hover-Effekte oder Hand-Cursor bei reinen Beschriftungen. Icons dekorativ ergänzen,
Bezeichnungen auch ohne Farbe und Symbol verständlich halten.

### Beispiel für Quarto-Markup

```markdown
## Heizung konfigurieren {#heizung}

**Excel-Ort:** Blatt [🔥 Heizung]{.excel-menu .darkred} →
Abschnitt [Heizsysteme]{.excel-section}

### Fachlicher Zusammenhang

Die Erzeuger werden entsprechend ihrer Priorität und Leistungsgrenze eingesetzt.

::: {.excel-operation}
### Im Excel-Tool

::: {.excel-path}
**Menüband:** klimaaktiv PEQ → Heizung → Auswahl Heizsystem
:::

1. Ausgangsstand mit [Aktuelle Eingabe speichern]{.excel-action} sichern.
2. Preset [„Fernwärme“]{.excel-value} auswählen.
3. Die übernommenen Felder, insbesondere [Maximale Heizleistung]{.excel-field},
   Energieträger und Effizienz, anhand der Projektkonfiguration prüfen.
4. Über **Formeln → Berechnung → Neu berechnen** neu berechnen.

**Kontrolle:** Blatt [Ergebnisse]{.excel-menu .red} → Endenergiebilanz.
:::
```

Die genaue Beschriftung und Verfügbarkeit dieses Pfads werden gegen die
ausgelieferte Arbeitsmappe geprüft. S. 21 zeigt Blatt-Dropdown und Ribbon als
Alternativen; die Webdarstellung darf sie nicht zu einer Klickfolge vermischen.

### CSS-Anpassungen

- Die aktuelle globale `min-width: 190px` der `.excel-menu` für Inline-Pfade
  aufheben; feste Breite nur im Blattnavigator verwenden.
- `white-space: nowrap` nicht auf ganze Pfadketten übertragen. Einzelne Marken
  bei Bedarf umbrechen lassen; Container mit `display:flex; flex-wrap:wrap`.
- Farben `.darkred`, `.red`, `.orange`, `.teal` beibehalten und Kontrast prüfen.
  Die Zuordnung wird aus Excel übernommen, nicht nach methodischen Themen erfunden.
- Feld-, Aktions- und Methodenformate unterscheiden sich zusätzlich durch Rahmen,
  Form und sichtbare Labels. Kein ausschließlich farbbasierter Status.
- Quarto-Fenced-Divs statt eingerückter Markdown-Spans innerhalb roher
  `<details>`-Blöcke nutzen; die vorhandene Startseite darauf prüfen.
- Screenshots responsiv, Vergrößerung über Quarto-Lightbox, Tabellen horizontal
  scrollbar, Bedienpfade und Hinweistexte ohne horizontales Seitenscrollen.
- Druckansicht mit lesbaren Rahmen/Labels und vollständigen Quellenangaben.

## 5. Presets als schneller Einstieg

`start.qmd` erhält unmittelbar nach der Dateivorbereitung zwei Wege:
**Vorhandenes Beispiel laden** und **Projekt mit Presets konfigurieren**.
Beide führen zum selben Ablauf; Presets werden nicht als Voraussetzung für
projektspezifische Eingaben dargestellt.

1. Beispiel laden oder Projekt-/Flächendaten eingeben; Ausgangsvariante unter
   eindeutigem Namen speichern.
2. In der Quick-Start-Ansicht die grundlegenden Presets wählen, soweit dort in
   der aktuellen Toolversion angeboten. Fachblätter und Ribbon bleiben direkte
   Alternativen. „Quick-Start“/„Start“/„Überblick“ vorab eindeutig zuordnen.
3. Eine kurze Preset-Matrix verlinkt zur jeweiligen Feldreferenz:
   Hülle/U-Werte und Luftdichtheit; Heizung/Abgabe/Bauweise; Kühlung; Lüftung;
   Warmwasser; PV-Auswahl; Flexibilität/Batterie; Mobilität; bauliche/TGA-LCA;
   Nutzerstrom. Diese Menügruppen sind in `customUI14.xml` vorhanden.
4. Vor dem Anwenden erläutern: Ein Preset übernimmt ein Parameterpaket und kann
   bestehende Eingaben ersetzen. Ausgangsstand sichern; nicht auf Excel-Undo
   vertrauen. Kein pauschales „alle Rückfragen mit Ja bestätigen“ übernehmen.
5. Übernommene Parameter sichtbar kontrollieren: Systemanteile/-leistungen,
   Sollwerte, Verluste und Aktivierungsschalter. Preset-Titel allein belegt keine
   aktive Konfiguration; das zeigt bereits der aktuelle Sanierungsvergleich.
6. Neu berechnen; Ergebnisblatt und bei Bedarf Excel-Pivot-Dashboard aktualisieren.
7. Als neue Variante speichern, Vergleich auswählen, fachliche Wirkung prüfen.
8. Für den Nachweis Schätzungen/Beispieldaten durch Projektangaben ersetzen und
   die verbindlichen Deklarationswerte beibehalten bzw. wiederherstellen.

Durchgehendes Beispiel: bestehendes Quartier → Heizungs-Preset „Fernwärme“ →
Parameterkontrolle → neue Variante → Endenergie-/PE-Vergleich. Ergänzend
Lüftungs-Presets mit/ohne WRG zur Wirkung auf Wärmebedarf und Ventilatorstrom.
Keine universellen Wirkungsgrade aus einem Beispiel ableiten; S. 24 nennt 100 %
WRG, was nicht als allgemeine Anlagenempfehlung übernommen wird.

## 6. Aktuelle Abbildungen einbetten

Unveränderte Quelldateien liegen unter `docs/website/`; der vorhandene
Asset-Build kopiert sie nach `website/media/manual/`. Die QMD-Seiten enthalten
Alt-Texte, Bildunterschriften und Quellenhinweise. Transparente Diagramme stehen
auf weißem Hintergrund und können über die Lightbox vergrößert werden.

| Abbildung | Ziel |
|---|---|
| quick-start, presets | Einstieg und Presets |
| tool-workflow, excel-overview | Blattnavigation |
| energy-model | Quartier und Modell |
| thermal-model | Thermische Hülle, Excel-Dashboard |
| dispatch, dynamic-assessment | Speicher und Flexibilität |
| mobility-boundary | Mobilität |
| decarbonisation, operational-emissions, lifecycle | Ökobilanz |
| excel-dashboard | Excel-Dashboard |
| variant-comparison | Variantenvergleich |

Bildunterschriften unterscheiden „Excel-Bedienung“ und „Modell/Bilanz“.
Die Schulungsabbildungen sind keine Ergebnisse der drei Bsp-Exporte.
Fehlende aktuelle Bedienabbildungen werden angefragt, nicht aus dem alten
Handbuch ersetzt.

## 7. Vor der Übernahme redaktionell klären

Diese Punkte blockieren die Strukturentscheidung nicht, benötigen aber fachlichen
Abgleich für die konkreten Inhalte:

- S. 41 zeigt v1.08, die neuen Beispiele verwenden 1.13.1_dev; Namen, Presets,
  Einfügezeilen und ausgeblendete Blätter versionsbezogen prüfen. Zeile 25 beim
  PV-Import nur mit verifiziertem Toolstand nennen.
- Warmwasser S. 55 beschreibt zunächst eine Priorität, dann komplementäre
  Nutzungsanteile. Die aktuelle Implementierung entscheidet über die Erklärung.
- S. 5 nennt andere LCA-Grenzen/Zeiträume als S. 69. Dort stehen außerdem
  „pro Jahr“ und kumuliertes Budget nebeneinander. Mit aktuellem Schema und
  Methodik abgleichen, keine widersprüchlichen Angaben übernehmen.
- PV-LCA und alle Deklarationswerte gemäß der vereinbarten Unterscheidung:
  Modellierung frei möglich, ka-Nachweis mit festgelegter Bewertung.
- Angaben wie „sechs Nutzungen“ trotz zusätzlicher sonstiger Nutzung,
  „JSON/XML je nach Implementierung“ und pauschale Sicherheitsversprechen des
  Handbuchs nicht als zugesicherte aktuelle Funktion übernehmen.
- Ergebnisbeispiele des Handbuchs und die drei Bsp-Varianten sind verschiedene
  Datensätze. Screenshots erklären Bedienorte, die neuen Plots zeigen ihre
  jeweiligen Exportergebnisse; Zahlen nicht vermischen.

## 8. Umsetzung und Abnahme

1. UI-Bezeichnungen mit der ausgewählten aktuellen Arbeitsmappe abgleichen;
   Pilotseiten Presets und Heizung sowie Formatierungslegende erstellen.
2. `.excel-menu` kompatibel erweitern und die wenigen oben genannten
   semantischen Klassen in `styles.css` ergänzen. Desktop/Mobil/Druck prüfen.
3. Blattnavigator, Einstieg, eigene Migrationsseite und Preset-Ablauf; danach HKLS,
   eigenständige PV-Eingabe, Speicher und Flexibilität, Nutzungsparameter, Mobilität,
   Ökobilanz mit Eco2soft-Bezug und abschließend Variantenverwaltung.
4. Fachseiten gemäß Zuordnung ergänzen, Abbildungen einbetten, Excel-Ergebnisse
   und Python-Szenarioexplorer klar trennen. Bestehende Seiten untereinander
   bis zum konkreten Eingabe-/Ausgabeabschnitt verlinken.
   „Analysieren und Bewerten“ mit getrennten Seiten für Ergebnisblatt,
   Excel-Dashboard, Variantenvergleich und Batch-Simulation (Scen) einrichten;
   Qualitätssicherung in die Nachweisführung verschieben.
5. `howto_website.ipynb` um Aufbau der Bedienblöcke, Bilderzeugung und lokalen
   Build erweitern; dieselbe Asset-Funktion wie im Website-Build nutzen und ausführen.
6. Abnahme: jede Handbuchgruppe hat ein Ziel; jeder Bedienabschnitt hat Ort,
   Handlung und Ergebniskontrolle; Preset-Überschreiben wird vorher erläutert;
   Methoden-/Bedien-/Deklarationshinweise sind ohne Farben unterscheidbar.
   Quarto-/Linkprüfung plus visuelle Kontrolle bei Desktop und 390 px Breite;
   keine unbelegten Schaltflächen, Zelladressen oder Modellbehauptungen.
   Migration anhand eines alten Projektexports und einer neuen Toolversion
   nachvollziehen; nicht geprüfte Übernahmedetails sichtbar offenlassen.

### Pflegeaufwand und Datenstrukturen

Kein neues öffentliches API, keine zweite Parameterdatenbank und kein neues
Navigationsschema. QMD-Anker, Quarto-Navigation und vorhandene CSS reichen aus.
Die zusätzlichen Inhaltsseiten pflegen redaktionelle Inhalte, keine Rechenlogik.

Die 14 freigegebenen Originalbilder werden als stabile Quelldateien versioniert.
Eine explizite Dateiliste in der bestehenden `website_assets.py` stellt sicher,
dass nur diese Bilder kopiert werden und fehlende Quellen den Build abbrechen.
Nutzen: reproduzierbare Veröffentlichung ohne Abhängigkeit von temporären
Chat-Anhängen; vorhandene PDF-Ausschnitte sind gemäß Nutzervorgabe ungeeignet.
Pflege: Ersatzbilder unter demselben Namen austauschen und Bildunterschrift
sowie Lesbarkeit prüfen; bei neuen Motiven Liste und QMD-Verwendung ergänzen.
Generierte Kopien bleiben ignoriert. Keine neue öffentliche Schnittstelle,
kein PDF-Renderer und kein zusätzliches fachliches Datenmodell. Der vorhandene
Build-Test prüft die bytegleiche Veröffentlichung aller 14 Bilder.
