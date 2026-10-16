# Codex-Auftrag: PEExcel-Archetypen für Quick-Check-Dashboard

**Ziel (PoC):** Vorhandene PEExcel-Batch-Szenarien als einzelne vollständige XLSX-Exporte (IN, OUT, SIM2) ablegen, mit `pexl.Project.from_files(files)` zusammenführen und für das bestehende Streamlit-Dashboard einen **konsolidierten Jahres-Projektexport** erzeugen. Die stündlichen Daten bleiben in den einzelnen Originaldateien abrufbar. Die Presetauswahl im Dashboard soll mit den aus Excel exportierten Preset-Tabellen kompatibel sein.

**Umfang:** Kleine, durchgängige Implementierung mit Tests und kurzer Gebrauchsanleitung. Keine allgemeine Formatabstraktion, Datenbank, neue Preset-Registry oder umfassende Refaktorierung von PEExcel.

## Gegebene Struktur / bereits vorhandene Bausteine

- Ablage im bestehenden Repository unter `data/exports/archetypes/`.
- Die Batch-Szenariodefinition existiert bereits in PEExcel: Szenariozeilen und anzuwendende Presets. **Nicht neu implementieren.**
- Die Presets werden ausschließlich in Excel-Tabellen `Presets_*` verwaltet: Eingabe-`var_name` als Zeilen, **Preset-ID = Spaltenüberschrift** innerhalb der Tabelle. Keine gesonderte Preset-Registry.
- Ein angewendetes Preset wird als `preset_recorded_<gruppe>` in `IN` gespeichert. Für die kontrollierten Batch-Läufe gilt diese Aufzeichnung vorerst als korrekt; **kein Rückvergleich aller aufgelösten IN-Parameter** (Backlog).
- Einzel-Exporte mit Stundenreihen verwenden derzeit `SIM2` und genau eine `IN`-Szenariospalte `STAGE`; der aktuelle pexl-Importer benennt dieses Szenario nach dem Dateinamen. Normale Projekt-Exporte ohne `SIM2` können mehrere Szenariospalten enthalten.
- `pexl.Project.from_files(files)` existiert und führt mehrere Einzeldateien zu einem `Project` mit individuellen Zeitreihen zusammen. Siehe `notebooks/howto_create_project_from_different_timeseries_files.ipynb`. Szenario-Spaltennamen müssen dabei eindeutig sein.
- Das Dashboard existiert: `apps/dashboard/main.py` (Streamlit). Es verwendet bereits `preset_recorded_*` für Filter und pexl-Reporting für Jahresdiagramme.
- **Achtung:** `src/pexl/io/excel.py::write_project_excel()` schreibt derzeit `IN`/`META`, nicht `OUT`. Es ist aktuell **kein** fertiger Writer für ein konsolidiertes `IN`+`OUT`-Jahresprojekt. Den benötigten kleinen Export ergänzen und im Roundtrip prüfen.
- Der Schema-Konverter (`src/pexl/io/converter.py`) exportiert im Schema-Modus derzeit fest definierte Tabellen (`IN`, `OUT`, `SIM2`, `CHART_*`). Prüfen, **wie die vorhandenen `Presets_*` tatsächlich im Excel-Schemaexport vorliegen**; noch nicht annehmen, dass sie im generierten pexl-Schema systematisch verfügbar sind.

## Artefaktnamen und Ablage

**`ArchetypeBundle`** = logischer Name für den vollständigen Archetypenbestand *einschließlich* der Zeitreihen. Intern kann er bereits durch ein zusammengeführtes `pexl.Project` repräsentiert werden; es muss für den PoC **kein neues Dateiformat** eingeführt werden.

```text
data/exports/archetypes/
  originals/
    <eindeutiger_archetyp_name>.xlsx     # pro Archetyp IN/OUT/SIM2
  catalog.json                           # generierter Index / Preset-Lookup
  annual_project.xlsx                    # konsolidierter IN/OUT-Projektexport ohne SIM
  preset_options.json                    # optionale, generierte Sicht aus dem Schemaexport
```

- **Original-XLSX sind die maßgeblichen Simulationsergebnisse.** Keine Pflicht-Konvertierung in CSV/Parquet.
- `catalog.json`, `annual_project.xlsx` und ggf. `preset_options.json` sind **reproduzierbar generierte** Artefakte, nicht manuell zu pflegen.
- Optionaler lokaler Cache `archetype_bundle.pkl` für das vollständige pexl-`Project` (siehe Notebook) ist erlaubt, aber **nicht** als dauerhaftes Austauschformat oder als Uploadformat verwenden (Python-/Schemakompatibilität; Pickle nur für vertrauenswürdige Dateien).
- Vor dem Commit der vollständigen Originaldateien Größe prüfen; bei Bedarf Git LFS, statt unbemerkt große Binärdateien in normales Git aufzunehmen.

## Meilenstein 1: Originale einlesen und katalogisieren

1. Kleine repräsentative Menge vorhandener vollständiger SIM2-XLSX unter `originals/` bereitstellen bzw. mit den echten PEExcel-Exporten testen. Keine fiktiven Produktionsdaten erzeugen.
2. Ein schmales CLI oder Skript implementieren, das Dateien deterministisch sortiert und mit `pexl.Project.from_files(files)` einliest. Bestehende pexl-Methoden nutzen; kein zweiter XLSX-Parser für Projekte.
3. Pro `Scenario` alle vorhandenen, nichtleeren `preset_recorded_*`-Werte mittels `scenario.to_var_dict()` extrahieren.
4. Index erzeugen: Szenarioname/Datei, `preset_recorded_*`-Werte, optional Modell-/Schema-Version, Prüfsumme der Quelldatei, ob SIM vorhanden ist, Anzahl Zeitschritte, Validierungswarnungen. Den **Originaldateipfad** erhalten, damit die Stundenreihen später gezielt geladen werden können.
5. Duplikate behandeln: gleiche Szenarionamen sind Fehler (wie `Project.from_files()`); **gleiche Preset-Kombinationen sind nicht zwingend identische Simulationen**. Mehrfachtreffer nicht stillschweigend überschreiben: Name/weitere IN-Werte können abweichen. Dashboard muss dann beide anzeigen oder explizit auswählen lassen.

Minimale Struktur (Beispiel, keine zusätzlichen manuell gepflegten IDs):

```json
{
  "schema_version": "<aus Quellschema>",
  "items": [
    {
      "scenario": "MFH_WP_01",
      "file": "originals/MFH_WP_01.xlsx",
      "presets": {
        "preset_recorded_geometry": "MFH kompakt",
        "preset_recorded_heating_system": "Wärmepumpe"
      },
      "timeseries_available": true,
      "time_steps": 8760,
      "warnings": []
    }
  ]
}
```

Die Key-Felder sind bereits durch die `preset_recorded_*`-`var_name`s eindeutig. Datei- und Anzeigeidentitäten nicht durch fragile zusammengeklebte Preset-Namen ersetzen.

## Meilenstein 2: Ein Jahresprojekt für das Dashboard

- Aus demselben zusammengeführten `Project` einen **gültigen regulären PEExcel-Projektexport ohne SIM** schreiben: mindestens Blätter `IN` und `OUT`, mit *allen* Szenarien als Spalten, `var_name` als Zeilenbezeichner und den vorhandenen Werten.
- Bestehenden `build_project_in_dataframe()` verwenden; für `OUT` analog eine möglichst kleine Ergänzung entwickeln. Den bisherigen `write_project_excel()`-Vertrag nicht unbemerkt ändern; ggf. dedizierte Funktion `write_annual_project_excel()` ergänzen.
- **Roundtrip:** `pexl.Project.from_excel("annual_project.xlsx")` muss alle Szenarien und ihre IN/OUT-Jahreswerte wieder korrekt laden können. `SIM2` darf darin fehlen.
- Dies ist für den PoC einfacher als ein zweites JSON-Modell für sämtliche Jahreswerte: Das bestehende Dashboard kann diesen Export bereits über `Project.from_excel()` lesen.
- SIM bleibt ausschließlich in den Originalen und wird standardmäßig **nicht** ins Dashboard geladen.

Konzeptioneller Ablauf (konkrete API nach Codeinspektion wählen):

```python
files = sorted(Path("data/exports/archetypes/originals").glob("*.xlsx"))
project = pexl.Project.from_files(files)  # existiert; IN + OUT + SIM je Scenario

# neu/ergänzt: Index aus recorded-Presets sowie Jahresprojekt IN+OUT schreiben
build_archetype_catalog(project, files, target="data/exports/archetypes/catalog.json")
write_annual_project_excel(project, "data/exports/archetypes/annual_project.xlsx")
```

## Meilenstein 3: Preset-Optionen leichtgewichtig aus dem Schema

**Konzept:** Zwei Ebenen sauber trennen, ohne neue manuell gepflegte Strukturen:

1. **Taxonomisches Schema** (`IN`, `OUT`, `SIM`, `VariableMeta`): beschreibt Variablen und Bedeutungen. `preset_recorded_*` gehört hierher als normale IN-Variable.
2. **Preset-Referenzdaten** (`Presets_*` in Excel): definieren verfügbare Preset-IDs (= Spaltennamen) und die zugehörigen IN-Parameterwerte. Sie gehören zum *versionierten Schema-Snapshot*, aber **nicht als zusätzliche Felder zu `VariableMeta`**.

**Jetzt (PoC):**

- Vorhandenen Excel-Schemaexport auf `Presets_*` prüfen. Wenn die Tabellen darin zugänglich sind, deren **Spaltenüberschriften** als `preset_options.json` exportieren – vollständig abgeleitet, keine neue Registry in Excel.
- Gruppe zunächst per Namenskonvention verbinden: `preset_recorded_<suffix>` ↔ `Presets_<suffix>`. Sonderfälle nur bei tatsächlichem Bedarf als kleine dokumentierte Zuordnung behandeln; keine große allgemeine Metadaten-Infrastruktur.
- Beim Verarbeiten eines Archetyps zwei *leichte* Prüfungen:
  - Existiert das `preset_recorded_*`-Feld im IN-Schema und seine zugehörige Preset-Tabelle bzw. Optionsgruppe im Schema-Snapshot?
  - Entspricht der nichtleere aufgezeichnete Wert **exakt einem Spaltennamen** dieser Gruppe?
- Fehlende Gruppen/Optionen für den PoC als **strukturierte Warnung** erfassen (nicht stillschweigend korrigieren oder wegen alter Exporte den gesamten Build abbrechen). Ein späterer Strict-Modus kann daraus Fehler machen.
- **Nicht** prüfen, ob alle von der Preset-Spalte festgelegten IN-Einzelparameter mit dem Szenario übereinstimmen. Das ist ausdrücklich Backlog.
- Wenn die Preset-Tabellen *nicht* im aktuellen Schemaexport lesbar sind: zuerst minimal die bestehende Schemaexport-/Konverterpipeline erweitern; nicht im Dashboard Presetlisten manuell duplizieren. Als Übergang dürfen vorhandene `preset_recorded_*`-Werte nur die **bereits simulierten** Optionen anzeigen, nicht fälschlich alle grundsätzlich auswählbaren Presets.

Beispiel einer **generierten** Sicht:

```json
{
  "source_schema": "<version/hash>",
  "groups": {
    "preset_recorded_heating_system": {
      "table": "Presets_heating_system",
      "options": ["Wärmepumpe", "Fernwärme"]
    }
  }
}
```

**Später (Backlog):** `pexl.schema.presets` als eigenständige read-only Schnittstelle auf diese *bestehenden* Preset-Tabellen, optional inkl. Parameterbelegung je Spalte, Quellen-/Versionshash und Validierung der effektiven IN-Werte. **Keine zweite Quelle der Wahrheit.**

## Meilenstein 4: Dashboard-PoC

- In `apps/dashboard/main.py` die Datenquelle **vorkonfiguriertes `annual_project.xlsx`** ergänzen, ohne die bisherige Auswahl eines eigenen Projekt-Exports zu entfernen.
- Bestehende Jahresdiagramme/Reports wiederverwenden. Standardmäßig **keine Zeitreihendiagramme** und **kein SIM-Laden** für die Webansicht.
- Preset-Filter möglichst aus `preset_options.json` aufbauen; unterschiedliche Zustände eindeutig darstellen: *Option prinzipiell vorhanden*, *diese Kombination bereits berechnet*, *nicht berechnet*. Für den ersten Schritt genügt auch die Filterung nur tatsächlich vorhandener Varianten, sofern die Einschränkung sichtbar ist.
- Eigene Projekt-Export-XLSX müssen weiterhin über denselben pexl-Import und dieselben Jahresdiagramme angezeigt werden können. Für echte Browsernutzung `st.file_uploader` statt ausschließlich lokaler `tkinter`-Dateiauswahl prüfen; nicht automatisch ein allgemeines Upload-/Formatframework bauen.
- Das Nachladen einzelner stündlicher Ergebnisse über `catalog.json -> originals/<file>.xlsx` nur vorbereiten; UI hierfür ist **nicht** Teil des PoC.

## Abnahme / Tests

- [ ] Mehrere reale SIM2-Einzelexporte lassen sich mit `Project.from_files()` zusammenführen; jedem Szenario bleiben seine Zeitreihen zugeordnet.
- [ ] `catalog.json` referenziert jede Quelldatei eindeutig und enthält ihre `preset_recorded_*`-Werte.
- [ ] Preset-Abgleich prüft nur **Gruppenexistenz + Optionsnamen** und meldet Nichtübereinstimmungen nachvollziehbar.
- [ ] `annual_project.xlsx` enthält `IN` + `OUT` für alle Archetypen; Read-Write-Read-Roundtrip bewahrt Szenarioanzahl, Namen und exemplarische Jahreswerte.
- [ ] Das bestehende Dashboard kann den konsolidierten Export laden und danach über Presets navigieren und Jahresdiagramme darstellen.
- [ ] Eine eigene reguläre Projekt-Export-XLSX kann nach wie vor geladen werden; kein SIM erforderlich.
- [ ] Dieselben Eingabedateien erzeugen einen deterministischen Katalog (keine zufälligen IDs/unstabilen Ordnungen).
- [ ] Fehlende, leere oder unbekannte Presetwerte lösen Warnungen aus, ohne erfolgreiche andere Szenarien zu verlieren.
- [ ] Kurze README mit einem ausführbaren Aufruf, Eingabeverzeichnis und erzeugten Dateien.
- [ ] Ein ausführbares `notebooks/howto_archetypes.ipynb` erklärt den vollständigen Arbeitsablauf und jede Erweiterung davon. Es verwendet dieselben Implementierungsfunktionen wie Skript/CLI, ohne die Logik zu duplizieren.
- [ ] Jede neue persistierte Datenstruktur oder öffentliche Schnittstelle ist gemäß der folgenden Regel begründet.

## Verbindliche Regel für Review- und Wartungsaufwand

Es gelten die [allgemeinen Projektleitlinien](../../AGENTS.md) für das gesamte Repository; die folgenden Anforderungen konkretisieren sie für diesen Plan.

Bestehende Datenstrukturen und Schnittstellen wiederverwenden und den zusätzlichen Review- und Wartungsaufwand möglichst gering halten. Jede neue persistierte Datenstruktur oder öffentliche Schnittstelle muss im Implementierungsvorschlag nachvollziehbar begründen:

- welchen konkreten Nutzen sie für den vorgesehenen Arbeitsablauf hat,
- warum die vorhandenen Strukturen oder Schnittstellen dafür nicht ausreichen,
- welchen zusätzlichen Pflegeaufwand sie verursacht, einschließlich Erzeugung, Aktualisierung, Kompatibilität und Tests.

Diese Begründung gilt auch für automatisch generierte Artefakte wie `catalog.json` und `preset_options.json`; ihre Nennung in diesem Plan ersetzt die Begründung nicht. Jede Erweiterung des Arbeitsablaufs muss im ausführbaren How-to-Notebook nachvollziehbar sein. Das Notebook ist Teil der Abnahme, eine README allein genügt nicht.

## Nicht jetzt

Keine neue Preset-Registry; keine neue Archetype-Klasse; keine Excel-/CSV-/Parquet-Adapterfamilie; keine automatische Simulation aus dem Web; keine Quick-Check-Rückübertragung in eine `.xlsb`; keine aufwendige Preset-Parameter-Konsistenzprüfung; keine Datenbank; keine großflächigen Änderungen an VBA.

**Arbeitsweise für Codex:** Erst existierende Import-/Exportfunktionen, Schema-Dataset, Notebook und Dashboard inspizieren. Den kleinsten funktionsfähigen Patch implementieren, passende Tests ausführen und verbleibende Unklarheiten (insbesondere tatsächliche Preset-Tabellen im Excel-Schemaexport) konkret im Ergebnis dokumentieren. Keine Annahmen über nicht inspizierte Workbook-Strukturen als Fakten behandeln.
