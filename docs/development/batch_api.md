# Python-orchestrierte Batchsimulation

## Verantwortlichkeiten und Schnittstellen

`pexl.batch.run_batch()` behält seine bisherige Signatur und liefert `BatchResult`
mit `completed`, `failed`, `exported_files`, `skipped`, `status`. Status ist
`completed` oder `failed`. Vollständig bedeutet: alle angeforderten Exporte
wurden geschrieben und im Checkpoint bestätigt. Callback-Zähler bleiben aus
Kompatibilitätsgründen Capture-Zähler; sie können ungesicherte Ergebnisse enthalten.
Die endgültige Erfolgsmeldung folgt dem Export. Callback-Ausnahmen propagieren
nach bestmöglicher Sicherung.

`Project` und `Scenario` bleiben unverändert. SCEN-Definitionen sind DataFrames,
Ergebnisse normale Project-Exporte. Kein neuer Jobmanager, keine weitere
Ergebnisstruktur, keine zusätzlichen Laufzeitskripte oder Paketabhängigkeiten.

```python
inspect_batch(
    workbook: str | Path,
    *,
    scenarios: str | Path | pd.DataFrame | None = None,
    scenario_filter: Mapping[str, object] | None = None,
    output_dir: str | Path | None = None,
) -> pd.DataFrame
```

Ohne `output_dir` liest und validiert die Funktion die Auswahl ohne Simulation
oder SCEN-Mutation; eine passende offene Arbeitsmappe wird wiederverwendet. Mit einem bestehenden
Batchordner prüft sie Checkpoint, Workbook-Hash, Schema und Ergebnisdateien,
aktualisiert `remaining_scenarios.csv` und liefert die verbleibenden Originalzeilen.
Diese Wiederherstellung öffnet Excel nicht. Ein v2-Checkpoint enthält die
Originalauswahl; die externe Quelldatei ist dafür nicht erforderlich. Bei v1 muss
die ursprüngliche Auswahl über `scenarios` übergeben werden. Beide Betriebsarten
verwenden dieselben Auswahl-/Validierungsfunktionen wie `run_batch`.

Die zusätzliche öffentliche Funktion ist nötig für überprüfbare Auswahl vor dem
Lauf und CSV-Abgleich nach einem Absturz, ohne Simulationsstart oder Hilfsskript.
Pflege: gemeinsame Filtersemantik, Rückgabe eines unveränderten SCEN-DataFrames,
Tests für frische Inspektion und Wiederherstellung ohne Excel.

## Eingaben, Typologien und VBA-Vertrag

`scenarios` akzeptiert DataFrame, CSV oder XLSX; bei None wird SCEN gelesen.
CSV bewahrt Zeichenketten wie `001` und `NA`, Leerzellen, Unicode und Quoting.
XLSX verwendet `Scenarios`, `SCEN` oder das einzige Blatt. Pflichtspalten sind
`Scenario Name` und `Base Scenario`; Namen müssen eindeutig sein. Filter erhalten
die ursprüngliche Zeilenreihenfolge. `Simulieren?` begrenzt die Auswahl nicht.
CSV bewahrt Zellwerte, keine Excel-Formeln/Formatierung oder beliebige pandas-Typen.

Die Entwicklungsmappe `ka_PEQ_Nachweistool_DEV.xlsb` besitzt die IN-Basis `Default`.
Für Typologien vollständige vorhandene SCEN-Zeilen auswählen; Presets und Custom-
Spalten werden nicht aus Namen oder Ergebnisdateien rekonstruiert.
`excel/development/Szenarien_5400.csv` ist eine vorgelagerte Typologieliste und
kein direktes SCEN-Eingabeformat. Das How-to beschreibt Pilot und Vollauswahl.

Der Adapter prüft Basisreferenzen, Presets und Resultatschema vor der Simulation.
Die eingebetteten Module `a_Batch_Simulation.bas` und `a_Presets.bas` der
Entwicklungsmappe wurden für die Implementierung gelesen (nicht verändert):

- Presetwerte entsprechen der Zeile `var_name=dropdown_name` rechts von
  `PRESETS>` in der jeweiligen `Presets_*`-Tabelle. Vergleich ohne Beachtung der
  Groß-/Kleinschreibung, mit entfernten äußeren Leerzeichen.
- `Custom *` referenziert `Preset Name` in der Tabelle `presets`; hier vergleicht
  VBA nach Trim mit Beachtung der Groß-/Kleinschreibung.
- `RunScenariosAutomated(reloadBase)` erhält weiterhin nur einen Boolean.
  Der Adapter wählt genau eine SCEN-Zeile und deaktiviert Save-/Exportflags.
- Bei Fehlern meldet die aktuelle VBA-Funktion nach `CleanExit` einen spezifischen
  Fehler (`RunScenariosAutomated`, `vbObjectError + 2299`). Nur diese bestätigte
  VBA-Rückmeldung oder ein False-Rückgabewert gilt als bekannter Szenariofehler.
  Andere COM-Fehler während des Makros bedeuten unklaren Ausführungszustand.

`base_reload="always"` lädt vor jeder Variante die Basis. `first_only` lädt am
Sitzungsanfang, bei Basiswechsel und zwingend nach jedem Fehler/Recovery neu.
Die Option setzt sonst vollständige unabhängige Presets voraus.

## Adapter und Wiederherstellung

`PEExcelAdapter(workbook, *, reuse_existing=True)` bleibt allgemein verwendbar.
Direkte Aufrufer können weiter eine passende offene Arbeitsmappe verwenden;
Batch und frische Inspektion verwenden `reuse_existing=True`: eine passende
offene Arbeitsmappe der aktiven Excel-Instanz wird wiederverwendet und bleibt
anschließend offen. Andernfalls wird eine eigene Instanz geöffnet. Gewünschte
Eingabeänderungen vorher speichern; der Checkpoint prüft den Dateistand, nicht
ungespeicherte Änderungen in Excel. Keine automatische Speicherung oder Änderung der Makrosicherheit.

Die private COM-Grenze wiederholt bekannte vorübergehende Ablehnungen nur für
sicher wiederholbare Operationen: höchstens drei Wiederholungen mit 0,25/0,5/1 s
Pause. Makroaufrufe werden niemals blind wiederholt. Ein begrenzter Retry ist
kein Timeout für einen blockierten COM-Aufruf.

Nach bestätigtem Szenariofehler oder sicherem Lese-/Auswahlfehler muss Excel
wieder bereit sein. Danach werden Konfiguration und Basis neu angewandt. Nach
Abbruch der eigenen Excel-Instanz ist höchstens eine Neuverbindung je Lauf
möglich; ein Prozesshandle bestätigt das Ende und schützt vor PID-Wiederverwendung.
Cache-Proxies werden verworfen. Ein noch laufender Prozess mit unklarem Makrostatus
wird nicht ersetzt, verändert oder beendet. Die PID wird zur Prüfung protokolliert.
Fremde Excel-Instanzen werden nie geschlossen; kein Kill nach Prozessname.

## Logging, Fehler und Unterbrechung

Automatische INFO-Ausgabe in Notebook und Terminal sowie appendendes `batch.log`.
Zeitstempel, Phase, Originalindex/Anzahl, Name, Laufzeit und getrennte Capture-/Commit-
Zähler zeigen den Fortschritt. Meldungen erscheinen vor blockierenden Operationen.
Nur laufbezogene Handler für `pexl.batch` und `pexl.io.excel_com`; kein basicConfig
und keine Änderung des Root-Loggers. Handler werden auch bei Fehlern entfernt.

Bekannte Szenariofehler werden bei gesundem Excel übersprungen. Unbehebbare COM-
Probleme stoppen mit `status=failed`. Struktur-/Schema-, Setup- und Exportfehler
propagieren. Die Fehlertexte benennen die Phase. Ein äußerer Abschlussweg versucht
unabhängig Flush, Checkpoint, Retry-CSV und Excel-Cleanup. Sekundäre Fehler
verdecken weder die ursprüngliche Ausnahme noch KeyboardInterrupt.

Ein Interrupt während eines synchronen VBA-Aufrufs kann verzögert sein. Nach
hartem Prozessabbruch gibt es keine garantierte Python-Bereinigung. Einen
verwaisten `.batch.lock` erst entfernen, nachdem Excel nachweislich nicht mehr
rechnet. Kein automatisches Übernehmen fremder Locks.

## Persistenz und Resume

`annual-NNNNN.xlsx` bleibt ein Project-Export mit IN, OUT und META.
Optionale `sim-NNNNN.csv` werden unmittelbar exportiert und aus dem Speicher
entfernt; ein fehlgeschlagener Export lässt den vollständigen Capture für einen
abschließenden Flush erhalten. Batchgröße begrenzt die noch unbestätigten Ergebnisse.

Ergebnisdateien werden über temporäre Dateien ersetzt, anschließend wird eine
Kopie des neuen Manifests atomar geschrieben. Erst danach wird der Speicherstand
als committed aktualisiert. Ein fehlgeschlagener Checkpoint kann keinen zweiten
Eintrag desselben Chunks erzeugen. Ergebnisse ohne Commit sind nicht bestätigt.

Resume überprüft Hashes und Szenarionamen und bildet die Restmenge über Namen.
Erfolgreiche Szenarien müssen kein zusammenhängender Präfix sein. Fehlgeschlagene
werden beim Resume erneut versucht; erfolgreiche werden nicht wieder simuliert.
`completed` bleibt in Chunk-Reihenfolge und passt zu `Project.from_files`.
Resume benötigt weiterhin Jahresergebnisse; reine Zeitreihenläufe unterstützen
portable Retry-CSV und Inspektion, aber kein gewöhnliches Resume.

Manifest v2 erweitert das bestehende `batch.json` um die vollständige ausgewählte
SCEN-Tabelle (`selected`, split-Format) und kompakte Laufzeitumgebungsinformation (Python, Paket, Excel). Erfolgreiche
Chunks halten zusätzlich die gemessenen Simulations-/Capture-Sekunden pro Szenario.
Die bisherige `identity` bleibt kompatibel. Ihre Arbeitsmappen-/Schema-/Options-
und Definitionsprüfung gilt weiter. Die vollständige Tabelle ist zusätzlich nötig,
weil die bisherige Identität Steuer-/Statusspalten bewusst auslässt und ohne sie
keine originale Retry-CSV rekonstruierbar wäre. Kein Duplikat der Ergebnisdaten.
V1 wird erst nach erfolgreicher Prüfung mit aktuellen passenden Eingaben ergänzt;
unbekannte Versionen werden abgewiesen. Pflege: serialisieren, prüfen, gezielter
V1-Upgrade, Datentyp-/Werte- und Fehlergrenzentests.

`remaining_scenarios.csv` ist stets eine geordnete Teilmenge der Originalauswahl:
alle Zeilen ohne bestätigte vollständige Ergebnisse. Sie wird vor Simulation,
bei Checkpoints und bei Fehlern/Interrupts aktualisiert. Vollständiger Erfolg
hinterlässt eine Datei nur mit Kopfzeile. Kein eigenes Retry-Schema.

JSON und CSV sind zwei Dateien und nicht zusammen atomar: ein harter Absturz
kann eine ältere CSV hinterlassen. Vor portabler Wiederholung mit `inspect_batch`
abgleichen; `batch.json` bleibt maßgeblich. Gewöhnliches Resume gleicht ebenfalls
ab. Bei unlesbaren Eingaben oder nicht beschreibbarem Datenträger kann kein
Recovery-Artefakt garantiert werden; Fehler werden explizit protokolliert.
Die CSV ersetzt nicht die passende Modellversion mit ihren Basis-/Presetdaten.

## Plausibilität, Betrieb und Abnahme

Nach Capture wird `PEI_balance` aus OUT samt Schemaeinheit angezeigt. Fehlende,
nichtnumerische und nichtendliche Werte erzeugen Warnungen. Der Wert wird bereits
im normalen OUT-Export persistiert; kein separates Metrikformat. Keine neue
Energiebilanz, kein erfundener Schwellenwert; ein negativer Saldo ist kein
allgemeiner Fehler. Fachliche Plausibilitätsgrenzen bleiben modellabhängig.

Python und Excel laufen lokal in der interaktiven Windows-Sitzung des
Simulationsrechners; RDP dient zur Bedienung. Hängende VBA-Aufrufe benötigen
manuelle Prüfung. Prozessüberwachung/harte Timeouts und CLI-Erweiterung sind
nicht Bestandteil dieser Implementierung.

`notebooks/howto_batch_simulate.ipynb` ist das ausführbare How-to; das bestehende
`website/tutorial_batch.ipynb` bleibt synchron. Tests verwenden die echten
Project-Exporte und simulierte COM-Grenzen. Abnahme umfasst Notebook-/Skriptpfad,
Logging, fehlgeschlagene Exporte/Checkpoints, Unterbrechung, CSV-Roundtrip,
nichtzusammenhängendes Resume, Ownership, Reconnection und VBA-Fehlerklassifikation.
Ein realer Excel-Pilot plus RDP-Trennen/Wiederverbinden bleibt eine separate
Prüfung auf dem Simulationsrechner; Mock-Tests bestätigen keine Excel-Berechnung.

Der optionale Live-Test ist standardmäßig übersprungen. Für eine gespeicherte,
geschlossene Arbeitskopie und genau eine benannte Default-Typologie bewusst
`PEEXCEL_LIVE_WORKBOOK` und `PEEXCEL_LIVE_SCENARIO` setzen und
`python -m pytest tests/test_batch.py -k live_default_typology_pilot` ausführen.
Dieser Test startet eine echte Simulation und prüft danach Resume. Ein RDP-
Verbindungstest muss direkt auf dem Zielrechner erfolgen.

## Debug-Neustart

`run_batch(..., overwrite=True)` löscht nur die reservierten Batch-Ausgabedateien
im Ausgabeordner, unter dem bestehenden exklusiven Lock. Andere Dateien und
Unterordner bleiben erhalten. Nicht mit `resume=True` kombinierbar. Das optionale
Argument ermöglicht wiederholte Prototyp-Läufe ohne manuelles Löschen; keine neue
persistierte Struktur. Tests prüfen Neustart, Erhalt anderer Dateien und Locks.
