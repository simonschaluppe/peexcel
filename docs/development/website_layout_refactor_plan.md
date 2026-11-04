# Plotly und Website: konsolidierter Arbeitsplan

Stand: 29.10.2026. **Einzige maßgebliche Planung für dieses Vorhaben.**
Ersetzt alle früheren Varianten dieses Plans. Der [Skriptaudit](website_scripts_audit.md)
ist eine Bestandsaufnahme mit späteren Prüfkandidaten, kein zweiter Umsetzungsplan.
Status: Die beiden Referenzfälle Primärenergiebericht und Stromprofil sind
implementiert; breitere Migration bleibt nachgelagert. Prüfstand siehe Abschnitt 10.

## 1. Das eigentliche Ziel

PEExcel-Plotfunktionen sollen robuste gewöhnliche Plotly-Figuren liefern, die in
lokalen Notebooks und anschließend in HTML/Website funktionieren. Wiederverwendbare
Analyse-/Plotlogik gehört in die vorhandenen Bibliotheksmodule. Eine Website darf
keine Voraussetzung sein, um diese Funktionen im Notebook zu verwenden.

Die Website soll schnell eine Vorschau vorhandener Inhalte geben. Neuberechnung,
Einlesen neuer Excel-Ergebnisse und Aktualisierung gespeicherter Fachausgaben
sind bewusst gestartete Arbeitsschritte. Preview und Veröffentlichung führen
weder alle Notebooks noch alle Asset-Erzeuger automatisch aus.

## 2. Drei klare Arbeitsschritte

| Schritt | Tätigkeit | Ergebnis |
|---|---|---|
| Arbeiten und ausprobieren | Lokales How-to/Notebook bearbeiten und gezielt ausführen; native `pexl`-Funktionen verwenden | Neue Erkenntnisse, Code und Arbeitsausgaben |
| Dokumentation aktualisieren | Einen ausgewählten Stand prüfen, verständlich erklären und benötigte Outputs/HTML-Dateien gezielt erzeugen | Geprüftes Tutorial oder fertige Fachabbildung |
| Website ansehen/veröffentlichen | QMD und gespeicherte Tutorialausgaben rendern, fertige Assets einbinden | Schnelle lokale Vorschau; nach Abnahme veröffentlichbarer Stand |

„Aus einem Guss“ bedeutet gemeinsame Bibliotheksfunktionen und nachvollziehbare
Beispiele. Es verlangt nicht, dass jede persönliche Experimentierzelle unmittelbar
Bestandteil der veröffentlichten Dokumentation wird.

## 3. Notebook- und Git-Struktur vorerst erhalten

Heute bestehen ursprüngliche `notebooks/howto_*.ipynb` und redaktionell gepflegte
`website/tutorial_*.ipynb`. Letztere enthalten gespeicherte Ausgaben; Quarto führt
sie beim Rendern nicht erneut aus. Diese vorhandene Trennung bleibt für den
Plotly-Refactor bestehen. Die Arbeitsnotebooks bleiben lokal nutzbar.

Es wird jetzt weder die gesamte Notebook-Versionierung abgeschaltet noch ein neuer
HTML-Snapshot-Veröffentlichungsweg eingeführt. Die zwischenzeitlich diskutierten
Varianten „alle Outputs entfernen“, „nur unversioniertes HTML“ und „alles automatisch
im Preview ausführen“ sind keine Implementierungsaufträge dieses Vorhabens.

Ein nur gelegentlich aktualisiertes, geprüftes Website-Tutorial mit Outputs passt
bereits zur bestehenden Struktur. Eine Änderung/Neuausführung einer lokalen Datei
ist nicht automatisch ein Git-Commit oder eine Veröffentlichung. Welche Änderungen
in einen publizierten Stand aufgenommen werden, wird bewusst gewählt; daraus muss
kein monatliches Automatisierungs- oder neues Versionierungssystem entstehen.

Ob später persönliche Experimente in ignorierten Kopien stattfinden oder weitere
ausgewählte Dokumentations-Snapshots angelegt werden, kann gesondert entschieden
werden. Dafür werden jetzt keine Dateien aus Git entfernt und keine Ignore-Regeln
für sämtliche Notebooks geändert.

## 4. Was liegt wo – heutige Bedeutung

| Ort | Rolle und maßgeblicher Inhalt |
|---|---|
| `src/pexl/` | Wiederverwendbare Import-, Analyse-, Darstellungs- und Exportfunktionen |
| `notebooks/` | Ausführbare Arbeits-/How-to-Notebooks; kein automatischer Preview-Eingang für alle Dateien |
| `website/*.qmd` | Redaktionelle Fachseiten |
| `website/tutorial_*.ipynb` | Ausgewählte Website-Tutorials mit geprüften gespeicherten Ausgaben |
| `website/illustrations/<thema>/` | Redaktionelle Originale und fertige Abbildungen; dauerhaft gepflegt |
| `website/assets/` | Aktuell ignorierte erzeugte Fachgrafiken, Tabellen, Katalogfragmente und Viewer. Vorhandene Ergebnisse werden eingebunden; nicht pauschal bei jedem Preview erneuert. |
| `website/downloads/` | Bereitstellungskopien für Nutzer, nicht zusätzliche maßgebliche Quelldateien.  |
| `website/_site/` | Gerenderte Website; kann aus Seiten und den vorhandenen Eingaben/Assets neu aufgebaut werden |
| `scripts/` | Momentan Mischung aus Erzeugern, Beispielen und Fachlogik. Nur die für den Plotly-Schritt relevanten Teile werden zuerst bereinigt. |

Wichtig: `assets/` ist heute nicht in Git. Fehlende Assets in einer frischen
Arbeitskopie sind deshalb ein vorhandenes Bereitstellungsthema. Das wird dokumentiert,
aber nicht durch automatische Neuberechnung oder einen beiläufigen Umbau der
Versionierung gelöst. Gespeicherte Notebook-Ausgaben sind davon getrennt zu betrachten.

## 5. Bibliotheksvertrag vor der Umsetzung konkretisieren

Ergänzung nach Architekturgespräch: Der folgende Vertrag leitet die Umsetzung.
Die Referenzfälle setzen ihn bereits um; die übrigen Module werden danach
angeglichen. Keine Website-/Git-Neuorganisation daraus ableiten.

### Zwei Zugänge, dieselbe Darstellung

1. Direkter Weg: vorbereitete Series/DataFrames oder ein materialisierter Report,
   explizite Spalten/Rollen/Einheiten und optionale Labels an den Renderer übergeben.
   Beliebige eigene Spaltennamen und vorherige Skalierung sind erlaubt.
2. Komfortweg: ProjectView -> Reportmaterialisierung -> derselbe Renderer.
   PEExcel-Variablenauswahl und Schemawissen gehören in diese vorgelagerte Stufe.
   `chart(view, chart_name)` und `render(report)` bilden dieses Muster bereits ab.

Ein direkter Renderer liest keine Projektdatei, lädt keine fehlenden Werte nach
und setzt keine konkrete Energieflussvariable voraus. Ein Standardreport darf
dagegen bestimmte Variablen verlangen: Das ist seine ausdrücklich benannte
fachliche Definition. Eigene Daten müssen keinen Standardreport nachahmen.
Einfache Scatter-/Boxplots können weiterhin Plotly Express verwenden; keine
vollständige Parallel-API zu Plotly bauen.

### Datenvertrag und Fachsemantik

"Datenvertrag" bezeichnet Eingabeform, erforderliche Metadaten und Semantik:
Achse/Index, ausgewählte Spalten, Einheit/Bezugsgröße, Vorzeichen, fehlende Werte,
Reihenfolge und Rollen. Vorhandene DataFrames und Reportdictionaries behalten;
Vertrag in `reporting/spec.py` typisieren/dokumentieren und an den Grenzen prüfen,
ohne neue persistierte Struktur oder verpflichtende Wrapperklasse.

Renderer verändern Eingaben nicht. Kein stilles NaN->0, keine automatische
Einheitenkonversion und keine Auswahl anderer Projektwerte. Der heutige
Reportrenderer nutzt `fillna(0)`, die Strombilanz `abs()`; beide Regeln müssen
bewusst festgelegt und kompatibel migriert werden. Ein Betragsschema mit getrennten
Bedarf-/Deckungsrollen ist legitim, aber kein universelles Vorzeichenmodell.
Direkte signierte Daten müssen ihre Vorzeichen behalten können. Nur eine eindeutige,
dokumentierte Regel je Eingabemodus, keine unbemerkte Bedeutungsänderung.

Kennwerte, Zielkurven und fachliche Aggregationen gehören in `analysis`/`reporting`.
Darstellungsoperationen wie Dauerliniensortierung oder Facettenbildung dürfen zum
Plot gehören, sofern explizit dokumentiert. Bereits aggregierte Daten dürfen nicht
erneut implizit aggregiert werden. Geänderte Werte erfordern konsistente Einheiten,
Labels und ggf. neu berechnete abgeleitete Kennwerte; Metadaten nicht blind übernehmen.

### Auffindbare Reportnamen

Heute existieren generierte `CHARTS`, `CHART_NAMES`, `get_chart` und öffentlich
`reporting.chart_names()`. Es fehlt ein autovervollständigbarer Zugang.
Gewünschter öffentlicher Zugang: benannte Funktionen wie
`reporting.primary_energy_balance(project_or_view, *, language="de", ...)`.
Ein Project bedeutet alle Szenarien, ein ProjectView genau die ausgewählte Menge
in ihrer Reihenfolge. Project intern einmal auf seine View normalisieren.
Beide Eingaben liefern denselben Reportvertrag, keine automatische Simulation
oder Dateiladung. Weitere Parameter wie Einheiten/Bezugsgröße nur mit klarer
Umrechnungssemantik ergänzen.

Benannte Funktionen sind dünne, dokumentierte Einstiege in den gemeinsamen
Materialisierungskern. `materialize(source, chart_name, ...)` und `chart_names()`
bleiben für dynamische Auswahl und bestehende Aufrufer erhalten. Die zuvor
vorgeschlagene zusätzliche Chart-Enum entfällt. Keine Berechnungsduplikate.

Nutzen der kleinen neuen öffentlichen API: auffindbare Namen und weniger Tippfehler.
Die vorhandene Liste liefert keine einzelnen IDE-Symbole oder Funktionshilfe.
Reine Standardreport-Einstiege aus vorhandenen Schemadefinitionen generieren und
über reporting exportieren, nicht per undurchsichtigem Laufzeit-__getattr__.
Pflege: dokumentierte Signaturen, deterministische Namen/Kollisionsprüfung,
Registry-Parität, gleiche Ergebnisse für Project und dessen View, Schemawechsel
und alte Stringaufrufe testen. Keine eigene Datei pro Report und kein neues
Dateiformat. Generierte Datei nicht manuell bearbeiten. Aktuell aktive
Schemaauswahl dokumentieren; in einem Schema nicht verfügbare Reports klar melden.

### Sprache als Bibliotheksfunktion

Alle öffentlichen Chartwege erhalten einheitlich `language="de"|"en"` sowie
explizite Label-/Titelüberschreibungen. Nutzertexte bleiben unverändert. Schema-
Variablen nutzen vorhandene Sprachmetadaten, feste Charttexte `LocalizedText`.
Ein gemeinsamer Fallback: gewünschte Sprache -> vorhandene deutsche Bezeichnung
-> stabiler Schlüssel. Fehlende Übersetzungen in Tests sichtbar machen.
Keine parallelen `_eng.py`-Implementierungen. Rollen/IDs nicht anhand übersetzter
Anzeigetexte auswerten; alte deutsche Rollen am Reporteingang normalisieren.
Sprachwechsel darf Werte, Rollen, Farben und Reihenfolge nicht ändern.

Die bisherige pauschale Verschiebung aller Übersetzungsthemen gilt hier nicht mehr:
Chart-i18n ist nun Teil des Bibliotheksziels. Die englische Website mit Navigation,
Seitenübersetzung und Deployment bleibt ausdrücklich zurückgestellt. Zahlen-/
Datumslocale und Plotly-Bedienelemente auch beim HTML-Export berücksichtigen.

### Zuschnitt je Datei

| Datei | Geplanter Zuschnitt |
|---|---|
| `reporting/spec.py`, `materialize.py` | Bestehenden Reportvertrag präzisieren, validieren; Schemaauswahl, Rollen, Labels und benötigte fachliche Ableitungen vor dem Rendern aufbereiten. |
| `schema/report_codegen.py`, generierte Reports, `reporting/__init__.py` | Auffindbare Reportnamen aus bestehender Quelle generieren/exportieren; Strings erhalten. |
| `plot/plotly.py` -> `plot/reports.py` | Auf Nutzerwunsch nach Aufgabe benennen: Reportrenderer samt dünnem `chart`-Komfortzugang. Andere Plotmodule verwenden ebenfalls Plotly. Aufrufer/Imports gemeinsam migrieren; bei benötigter Abwärtskompatibilität alter Pfad nur als befristete Weiterleitung, keine zweite Implementierung. Projektbezogene Scatter-/Verteilungshelfer vor dem Umzug auf ihre Zuständigkeit prüfen. |
| `plot/electricity_balance.py` | Direkter expliziter Daten-/Spaltenvertrag; Standardprofil-Auswahl vorgelagert. Gemeinsame Renderer für eigene und Standarddaten. |
| `analysis/temporal.py`, `analysis/targets.py` | Zeitprofilaufbereitung bzw. Zielwertberechnung. Der Plot erhält ausgewählte Ergebnisse, keine intern erzwungene Zielwertfamilie. |
| `plot/typical_day.py`, Dauerlinien, Heatmap, Sankey | Bestehende spezialisierte Funktionen behalten; Eingabe-, Sprach- und Layoutregeln angleichen, keine erzwungene Einheits-Reportstruktur. |
| `plot/plotting.py`, `plot/plotting_eng.py` | Aufrufer prüfen. `target_of_gfz`/Kontextkurven und `xy_balance_plot` in ein gemeinsames fachlich benanntes `plot/targets.py` bündeln; alte Imports bei Bedarf befristet weiterleiten. Beispiele in How-to, überlappende Bilanzhelfer mit bestehenden Renderern abgleichen. |
| `plot/targets.py` (ersetzt Altmodul-Funktionalität) | Reine Darstellung expliziter Kurven/Punkte/Referenzlinien, keine interne Auswahl von `ZQSynergy`. Ein gemeinsamer Ort statt zweier Sprachkopien; Matplotlib-Aufrufer nicht still auf Plotly umstellen. Backend-Parität nur bei tatsächlichem Bedarf. |
| `i18n.py`, `plot/styles.py`, `plot/export.py`, `plot/__init__.py` | Gemeinsame Sprachregeln, semantisch stabile Farben, Darstellung/Export und kuratierte öffentliche Imports. Keine Website-Abhängigkeit. |

Ein neues `plot/targets.py` hat einen eng begrenzten Nutzen: die noch benötigten
Zielkurvendarstellungen ersetzen zwei vermischte Altmodule. Pflege umfasst deren
Aufrufer, nichtmutierende Eingaben, Labels, Referenzlinien und vorhandene Backends;
keine neue Zielwertberechnung. Löschung erst nach Migration tatsächlicher Aufrufer.

Abnahme zusätzlich: gleiche Figure-Daten über direkten und Komfortweg; beliebige
Spaltennamen; skalierte Eingaben; Eingaben unverändert; fehlende Werte/Vorzeichen
geprüft; DE/EN identische Fachwerte; vorhandene Reportnamen kompatibel. Breite
Migration schrittweise, zuerst Stromprofil und ein materialisierter Report.

## 6. Begrenzter erster Umsetzungsschritt

**Referenzfall: Stromprofil-Tutorial.** Es soll mit expliziter Datei-/Szenarioauswahl
und installierter Bibliothek ausführbar sein, ohne `website_examples` zu importieren.
Saisonmittel, Stundenverlauf, Zeitraumwahl und Slider müssen im Notebook funktionieren.

| Datei/Bereich | Konkrete Aufgabe |
|---|---|
| `scripts/website_examples.py` | Wiederverwendbare Stundenachsen-/Kanalprüfung und Profil-/Plotlogik herauslösen. Website-Auswahl/Assetpfade dürfen als dünnes Rezept bleiben. Keine zweite Fachimplementierung behalten. |
| `src/pexl/analysis/temporal.py` | Stundenachsenprüfung und wiederverwendbare Kanalbestandsprüfung aus vorhandenem Code aufnehmen, vorhandene DataFrames nutzen. |
| `src/pexl/plot/electricity_balance.py` | Profilfunktion mit vorhandenen Renderern bündeln; explizite Daten/Parameter statt Website-Konfiguration. Zeitnavigation als Bestandteil der normalen Plotly-Figuren. |
| `src/pexl/plot/typical_day.py`, `_duration_curve_plotly.py` | Feste Breiten kontrollierbar machen; für Facetten eine nachvollziehbare wählbare Anordnung ermöglichen. Gewöhnliche Notebook-Nutzung bleibt unabhängig von Website-Einstellungen. |
| `src/pexl/plot/export.py` | Soweit für diesen Referenzfall nötig, responsiven HTML-Export und lesbare Herkunft ermöglichen; bestehende statische Exporte erhalten. |
| `website/styles.css` | 900-px-Mindestbreite und erzwungenen Diagrammüberlauf beheben. Diagramme nicht durch Abschneiden scheinbar passend machen. |
| `website/tutorial_stromprofile.ipynb` | Explizite Eingaben und native API zeigen, einmal gezielt ausführen, gespeicherte Ergebnisse abnehmen. |
| Passendes `notebooks/howto_*.ipynb` | Dieselbe native Funktion ausführbar erklären; betroffene alte Skriptimporte migrieren, persönliche Inhalte nicht pauschal umschreiben. |
| Relevante Plot-/Website-/Tutorialtests | Datenwerte und Vorzeichen, originale Figure-Eigenschaften, Facetten, Notebook-Ausführung und schmale gerenderte Darstellung prüfen. |

Gemeinsame API nur ergänzen, wo vorhandene Funktionen nicht genügen. Nutzen:
Notebook und HTML verwenden eine Implementierung. Keine neue Figure-Hülle, kein
Website-Adapter, kein allgemeines Layout-/Registry-Framework und keine zusätzliche
persistierte Datenstruktur. API-Kompatibilität und fachliche Ergebnisse prüfen.

Nach diesem Referenzfall betroffene weitere Plotly-Tutorials gezielt angleichen.
Keine Gesamtmigration sämtlicher Skripte als Voraussetzung dieses ersten Ergebnisses.

## 7. Preview, Aktualisierung und Redaktion

- Preview rendert vorhandene Seiten und gespeicherte Outputs. Bei reinem Text-/
  CSS-Edit ist keine Notebookausführung oder erneutes Einlesen großer Exceldateien nötig.
- Benötigt eine Änderung neue Ergebnisse, gezielt Notebook bzw. bestehenden Erzeuger
  aufrufen, Ergebnis prüfen und anschließend die Vorschau aktualisieren.
- Interaktion mit einem fertigen Plotly-Diagramm oder Viewer ist Browserlaufzeit;
  dafür muss der Website-Build keine Python-Berechnung starten.
- `website_assets.py` wird nicht ungefragt zum universellen Build-Orchestrator
  ausgebaut. Seine teuren Erzeugungsschritte sind kein normaler Preview-Schritt.
  Der spätere Zuschnitt wird nach dem funktionierenden Plotly-Referenzfall entschieden.
- Original und fertige annotierte Screenshots behalten. Einmalige redaktionelle
  Erzeugungsskripte nicht als dauerhaftes Produkt aufbauen. Bestehende Hilfsskripte
  erst nach Prüfung ihrer Aufrufer entfernen; kein Bilderneubau bei Preview.
- QMD/Notebook und Hypothesis bleiben die Bearbeitungswege. Der bestehende
  Redaktionsablauf regelt Freigabe, echte Screenshots und gerenderte Abnahme.
- Englische Website bleibt zurückgestellt; Chart-i18n folgt Abschnitt 5.

## 8. Spätere Themen – ausdrücklich außerhalb des ersten Schritts

Quick-Check/Bewertungsviewer, Batch-Konsolidierung, Preset-/Katalogimport,
Lehrschnitte und allgemeine Skriptlöschungen werden getrennt betrachtet.
Der Audit erklärt ihre heutigen Funktionen und die möglichen Zielorte.
Keine dort vorgeschlagene neue API oder Löschung ist Voraussetzung der Plotly-Korrektur.

Für Quick-Check später konkret klären: Datenimport/Erzeugung bewusst starten,
vorhandene Daten/UI schnell lokal testen, welche Fachlogik wirklich nativ verfügbar
sein muss und welche Browserlogik gerechtfertigt ist. Keine neue Viewerarchitektur
allein aufgrund eines Skriptnamens oder einer angestrebten Dateianzahl einführen.

## 9. Abnahme des ersten Schritts

1. Stromprofil-Notebook läuft ohne Website-Helfer mit dokumentierten Eingaben.
2. Dieselben Plotfunktionen liefern im Notebook und gespeicherten HTML die
   vorgesehenen Werte und Interaktionen; schmale Darstellung wird visuell geprüft.
3. Textänderung und Preview führen weder Notebookzellen noch Asset-Neuberechnung aus.
4. Betroffene How-to-/Tutorialausgaben werden genau einmal bewusst aktualisiert
   und geprüft; bestehende Versionierungs-/Veröffentlichungsstruktur funktioniert weiter.
5. Entfernte Duplikate und verbleibende Skriptaufgaben werden im Diff nachvollziehbar.
   Keine Veröffentlichung oder breite Dateilöschung als Nebenwirkung.

## 10. Umgesetzter Referenzschritt und Grenzen

- `plot/reports.py` ersetzt die Implementierung in `plot/plotly.py`; letzteres
  bleibt als kleiner Importadapter. Vorhandene lokale Änderungen an den
  Annotationsdefaults wurden übernommen. Eigene Python-/Notebook-Aufrufer migriert.
- `reporting.primary_energy_balance(Project|ProjectView, language=..., unit=...)`
  verwendet denselben Materialisierungskern wie dynamische Stringauswahl.
  Zunächst genau ein expliziter benannter Einstieg für den Referenzfall; die
  Generierung weiterer Standardreportfunktionen ist noch nicht umgesetzt.
  Das vermeidet einen Generatorumbau vor Abnahme des ersten Funktionsvertrags.
- `reporting.convert_unit` kopiert Werte und Metadaten gemeinsam. Bewusst nur
  Wh/kWh/MWh-Präfixe bei identischer Bezugsgröße. Keine implizite Flächen-, Zeit-
  oder Primärenergiefaktorumrechnung. Modellversion gegen aktives Schema prüfen.
- Primärenergiebericht: DE/EN-Texte, vorhandene Rollen plus demand/supply-Aliasse,
  explizites value_mode und strenge Prüfung fehlender/nichtendlicher Zahlen.
  Berichtsdictionaries bleiben editierbar, kein neues Persistenzformat.
- `analysis.temporal` enthält die aus dem Skript übernommene Stundenachsenprüfung,
  numerische Prüfung, Kanalbestand und explizite saisonale Stundenmittel.
- Strombilanz: eigene Spalten, magnitude/signed, native Zeitraumwahl/Slider,
  mehrzeilige Facetten, horizontale Legenden; keine Website-Abhängigkeit.
  Die fachliche Beispielauswahl bleibt ein kurzes Rezept im Skript/Notebook.
- HTML-Export nutzt verfügbare Breite und separat umbrechende Herkunftsangaben;
  SVG/PNG behalten feste Exportabmessungen. Website-Mindestbreite entfernt.
- `howto_report_plots`, `howto_analyze_electricity_balance` und
  `tutorial_stromprofile` gezielt ausgeführt; gespeicherte Outputs bleiben erhalten.
  Tutorialdownload bewusst kopiert, Quarto mit deaktivierter Ausführung gerendert.

Nicht als bereits umgesetzt verstehen: vollständige Chart-i18n (insbesondere
Plotly-eigene Toolbar-Locale und weitere Reporttypen), Zielkurven-Altmodule,
sämtliche typischen Tages-/Dauerlinienlayouts, allgemeine Einheiten-/Bezugsrechnung,
automatische Schemaauswahl sowie Quick-Check-/Batch-/Preset-Umbauten.

Prüfung: 54 Tests erfolgreich (Verträge, Annotationen, Publikation mit echtem
HTML/SVG/PNG, Gebäudesektor, Tutorialquellen und unverändernde Downloadbereitstellung).
Drei bekannte Bestandsfehler im abschließenden Lauf ausgenommen, nicht gelöscht
oder abgeschwächt. Drei Referenznotebooks ausgeführt; Browserdarstellung bei
600 und 390 Pixeln geprüft. Separat festgestellte bestehende Daten/Testabweichungen:
Endenergiebilanz der drei Website-Beispiele schließt nicht (ca. 21–32 Einheiten),
und GWP-Beispiele enthalten keine vom Test erwarteten negativen Beiträge.
Mit unverändertem Materialisierungs-/Rendercode aus Git HEAD reproduziert;
Frames aller vier bisherigen Jahresberichte stimmen vor/nach Änderung überein.
Diese fachlichen Befunde wurden nicht durch geänderte Werte oder abgeschwächte
Tests kaschiert. Zusätzlich enthält `tutorial_gebaeudeschnitt.ipynb` bereits in
Git HEAD eine nicht ausgeführte Codezelle; der entsprechende Bestandstest bleibt
rot. Keine Neuausführung dieses unbeteiligten Tutorials als Nebenwirkung.

### Nachtrag: GWP-Berichte korrigiert

Die GWP-Definitionen verwenden jetzt die aktuellen Komponenten und Summen aus
`CHART_metadata.csv`; das generierte Register wird daraus erzeugt. Die neue
fachliche Auflösung in `reporting/gwp.py` behandelt ausschließlich die Auswahl
aktueller oder grober Legacy-Lebenszykluswerte und dokumentiert deren Herkunft
im vorhandenen Report-Dictionary (`sources`). Keine neue persistierte Datenstruktur.
Die dünnen Funktionen `reporting.gwp_ee`, `gwp_ee_detail` und
`gwp_ee_fossil_biogenic` ermöglichen einen auffindbaren Zugriff ohne Stringnamen;
sie verwenden denselben Materialisierungspfad und benötigen keine zweite Implementierung.

Aktuelle Nullwerte sind gültig. Unvollständige aktuelle Ergebnisse werden nicht
mit Legacy-Werten ergänzt. Legacy-Detailgruppen bleiben grob; eine vollständige
fossile/biogene TES-Aufteilung wird aus ihnen nicht erfunden. Die Detailbilanz
umfasst Baukonstruktion und technische Systeme, die Quartiersbilanz zusätzlich
Mobilitätsherstellung und Betrieb. Summen erscheinen als Marker statt erneut
als gestapelte Beiträge. Quick-Check verwendet die aufgelösten Reportwerte.

Der oben dokumentierte negative-GWP-Testbefund ist damit behoben: Negative
Beiträge existieren im Detailbericht, müssen aber nicht in aggregierten
Quartierssummen auftreten. Der Test prüft jetzt diese fachliche Grenze und den
Summenschluss. 48 gezielte Tests bestanden, einschließlich Browser-JavaScript-
Parität und Bildexport. Drei betroffene Notebooks wurden explizit ausgeführt
und ihre Ausgaben gespeichert. Die unabhängige Endenergiebilanzabweichung bleibt
offen. Website-Preview und Build führen weiterhin keine Fachberechnungen aus.
