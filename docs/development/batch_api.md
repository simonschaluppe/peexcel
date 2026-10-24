# Python-orchestrierte Batchsimulation

## Entscheidung und Schnittstellen

`pexl.batch.run_batch` kapselt Szenarioauswahl, den synchronen VBA-Aufruf und die
sofortige Ergebnissicherung. `BatchResult` enthält `completed`, `failed`,
`exported_files`, `skipped` und `status`. Diese kleine öffentliche Schnittstelle
ersetzt die COM-Schleifen in den Notebooks; Project/Scenario allein können keine
Excel-Berechnung starten. Es entsteht kein zweites Simulationsmodell, keine
Konfigurationshierarchie und keine zusätzliche Schemaabbildung.

`pexl.io.excel_com.PEExcelAdapter` ist der allgemeine PEExcel-COM-Adapter und die
interne Windows-Grenze. Verbindung, Besitz der Excel-Instanz, Tabellenzugriff und
Aufräumen bilden die gemeinsame Infrastruktur. Beim Öffnen wird keine SCEN-Tabelle
vorausgesetzt; Tabellen werden erst bei der jeweiligen Operation aufgelöst.
Szenariokonfiguration und -ausführung sind die ersten konkreten Operationen dieses
Adapters, keine Einschränkung auf Batch-Aufträge. `capture_scenario` kann aktuelle
Ergebnisse auch ohne vorherige SCEN-Konfiguration oder Simulation übernehmen.

Die Methoden `read_scenarios`, `configure_scenarios`, `run_scenario` und
`capture_scenario` benennen ihre konkrete Aufgabe. Weitere PEExcel-Funktionen
können später dieselbe Verbindung und Tabelleninfrastruktur nutzen. Dafür werden
jetzt weder leere Methoden noch eine zusätzliche Basisklasse oder Adapterhierarchie
eingeführt. Reihenfolge, Chunking, Resume und Dateiexport bleiben in `pexl.batch`.
Nur im Adapter werden COM-Objekte verwendet. `load_scenario_values` überträgt IN/STAGE und
OUT/Live nach `Project.get_or_create_scenario`. `write_project_excel` verwendet
die bestehenden `build_project_table`-Funktionen; `read_project` prüft fortgesetzte
Exporte. Optionales SIM wird über `Scenario.set_timeseries` aufgenommen und als
CSV ausgegeben. Anschließend wird der Stunden-Datenrahmen freigegeben.

## Eingaben und Excel-Lebenszyklus

Ohne `scenarios` wird die vorhandene SCEN-Tabelle `Scenarios` verwendet.
Alternativ akzeptiert `scenarios` einen DataFrame, CSV oder XLSX. Excel-Dateien
verwenden das Blatt `Scenarios`, ersatzweise `SCEN`, oder das einzige Blatt.
Die erste Zeile enthält die originalen SCEN-Spaltennamen. `Scenario Name` und
`Base Scenario` sind Pflicht; Namen müssen eindeutig sein. Unbekannte Spalten
werden vor dem ersten Rechenlauf abgewiesen. CSV-Trennzeichen werden erkannt.
Fehlende optionale Spalten bleiben bei externer Konfiguration leer.

Eine externe Liste ersetzt temporär den SCEN-Tabelleninhalt. Ursprüngliche Größe
und Formeln werden bei normalem Ende und Python-Ausnahmen wiederhergestellt.
Bei nativer Konfiguration werden die ursprünglichen Steuerfelder (Auswahl, Reload, Save/Export) restauriert;
die VBA-Statusinformationen bleiben sichtbar. Excel darf während eines Auftrags
nicht manuell bearbeitet werden. Nach einem Prozessabsturz kann Python keine
Wiederherstellung garantieren; dafür eine gespeicherte Arbeitskopie verwenden.

Eine passende Arbeitsmappe der aktiven Excel-Instanz wird wiederverwendet. Sonst
wird eine separate Instanz geöffnet. Fremde Arbeitsmappen/Instanzen werden weder
gespeichert noch geschlossen; selbst geöffnete werden ohne Speichern geschlossen.
Makrosicherheit wird nicht verändert. Andere, nicht aktive Excel-Instanzen werden
nicht automatisch durchsucht. Die Arbeitsmappe muss den vereinbarten VBA-Vertrag
bereits implementieren; diese Änderung verändert kein VBA und keine XLSB-Datei.

Die API setzt vorhandene Save-/Exportflags auf False und gleicht `Skip base reload?`
mit dem Reload-Argument ab. Diese Steuerfelder einer externen Liste sind daher nicht
maßgeblich; die API-Optionen gelten. Pro Aufruf wird genau eine Zeile per Bulk ausgewählt:
`RunScenariosAutomated(reloadBase)` erhält ausschließlich einen Boolean.
VBA lädt optional die Basis, wendet Presets an, rechnet und aktualisiert den Status.
VBA speichert/exportiert in diesem Modus nicht. Python liest Ergebnisse vor dem
nächsten Aufruf. IN, OUT und optional SIM müssen strukturierte Tabellen mit diesen
Namen sein (Groß-/Kleinschreibung wird ignoriert). In der aktuellen Arbeitsmappe liegt
`sim` auf dem Blatt `SIM2`; die Suche hängt nicht vom Blattnamen ab. IN benötigt `var_name`/`STAGE`, OUT `var_name`/`Live`; SIM hat die
kanonischen Stundenvariablen als Spalten. Ein anderes SIM-Layout muss explizit im
Adapter ergänzt werden, nicht durch eine zweite Konvertierung im Notebook.

## Reload und Fehler

Standard `always` lädt für jedes Szenario die Basis neu. `first_only` lädt beim
ersten tatsächlich ausgeführten Szenario jeder Sitzung und beim Wechsel von
`Base Scenario`. Das gilt insbesondere nach Resume. Es ist nur für vollständige,
unabhängige Presets geeignet: ausgelassene Eingaben können sonst aus dem vorherigen
Szenario fortbestehen. Chunk-Grenzen allein ändern den Reload-Zustand nicht.

Beim ersten VBA- oder Capture-Fehler stoppt der Lauf mit `status='failed'`. Zuvor
vollständig erfasste Szenarien werden gesichert. Setup- und Exportfehler werden
als Exceptions weitergegeben. Bei KeyboardInterrupt werden bereits erfasste
Szenarien gesichert, soweit Python noch ausgeführt werden kann; laufende synchrone
COM-Aufrufe können nicht zuverlässig abgebrochen oder mit Timeout beendet werden.

## Persistenz, Resume und Pflegeaufwand

`annual-00001.xlsx` usw. sind normale Projektdateien mit IN, OUT, META und bis zu
`batch_size` Szenarien. Für ca. 5.000 Szenarien bei 25 entstehen ca. 200 Dateien.
Kein eigenes Ergebnisformat: sie lassen sich mit `Project.from_files` konsolidieren.
`sim-00001.csv` usw. enthalten optionale Stundenwerte, zugeordnet über `batch.json`.

Ein neues, versioniertes `batch.json` ist erforderlich, weil normale Projektdateien
weder Workbook-/Konfigurationsidentität noch atomaren Fortschritt oder Dateihashes
enthalten. Es enthält keine Kopie der Ergebnisse: nur Eingabeidentität, Schema,
Optionen, erfolgreiche Chunks und den letzten Fehler. Die Identität umfasst den
Workbook-Dateihash und die gewählten SCEN-Zeilen einschließlich Presets; Auswahl-
und Statusfelder einschließlich `Zeitpunkt` sowie die von Python gesteuerten
Reload-/Save-/Exportfelder werden aus der Zeilenidentität ausgeschlossen. Andere ungespeicherte
Workbook-Änderungen sind nicht durch den Dateihash erfasst: vor einem Auftrag den
gewünschten Basisstand speichern und währenddessen unverändert lassen.

Ergebnisdateien werden zuerst über temporäre Dateien ersetzt, danach wird das
Manifest atomar ersetzt. Resume akzeptiert nur identische Eingaben und überprüfte
Dateihashes und Szenarionamen. Ein nicht abgeschlossener Chunk wird erneut gerechnet;
nach einem harten Abbruch bleiben höchstens `batch_size-1` noch nicht bestätigte
Szenarien. Verwaiste Dateien eines solchen Chunks sind keine bestätigten Ergebnisse.
Resume benötigt Jahresergebnisse; reine Zeitreihenläufe sind ohne Resume möglich.

Ein exklusiv angelegtes `.batch.lock` verhindert parallele Schreibzugriffe. Nach
einem harten Prozessabbruch erst sicherstellen, dass Excel nicht mehr rechnet, dann
den verwaisten Lock entfernen. Keine automatische Übernahme eines fremden Locks.

Pflege: Manifestversion bei inkompatiblen Änderungen erhöhen; keine automatische
Migration, sondern neuer Ausgabeordner. Tests prüfen echte Project-Roundtrips,
Resume, Fehler, Hashprüfung, externe Listen, Auswahl und Makroargumente am Fake-COM.
Keine neuen Abhängigkeiten im Kernpaket: das optionale Extra `[batch]` ergänzt
pywin32 unter Windows und openpyxl. Ein Live-Test benötigt Windows/Excel und eine
Arbeitskopie mit dem neuen VBA-Vertrag; Mock-Tests bestätigen keine Excel-Berechnung.

## Tutorials

`notebooks/howto_batch_simulate.ipynb` ist das vorhandene ausführbare How-to;
eine Datei `howto_batch_simulation_with_python.ipynb` existiert im Repository nicht.
`website/tutorial_batch.ipynb` bleibt die deutsche Quarto-Reinschrift unter der
bisherigen URL `batch-python.html`. Beide verwenden ausschließlich die öffentliche
Batch-API und bestehende Project-Analyse. Der Live-Aufruf ist explizit einschaltbar.
