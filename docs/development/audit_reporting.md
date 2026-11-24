# Interne Auditberichte

`notebooks/howto_auditbericht.ipynb` ist die ausführbare, kopierbare Berichtsquelle.
Das Beispiel verwendet die lokale `Klimagemeinschaften_typen.xlsx` und `Hol_PHniv`.
Die Datei enthält keine Variante `AW Holz`; es erfolgt kein stiller Namensersatz.
Das Notebook prüft zusätzlich alle Typen der eingestellten Datei. Private Eingaben
und erzeugte Berichte werden nicht mit Git versioniert.

## Projektablage und Bedienung

Das Notebook als `auditbericht.ipynb` neben die Projektdatei kopieren. Projektpfad
und exakten Variantennamen einstellen, Markdown-Texte bearbeiten, speichern und
alle Zellen ausführen. Die letzte Zelle schreibt `report/auditbericht.html` und
`report/auditbericht.docx`. Ein erneuter Export ersetzt diese Ausgaben; das
Quellnotebook bleibt unverändert. Änderungen im fertigen Word-Dokument werden
nicht zurückgeführt. Quarto wird in einem isolierten temporären Projekt gestartet,
damit eine umgebende Website-Konfiguration keine Veröffentlichung auslöst.

Voraussetzungen: `pip install -e ".[publication]"`, Quarto auf PATH und ein von
Kaleido unterstütztes Chrome für die statischen Word-Abbildungen. Es wird keine
Software automatisch installiert. HTML lässt sich auch allein mit
`render_notebook(path, formats=("html",))` erzeugen.

Der Renderer führt gewöhnliche Python/IPython-Zellen in einem frischen Prozess
mit dem aufrufenden Interpreter im Projektverzeichnis aus. Das benötigt keinen
registrierten Jupyter-Kernel oder Netzwerkport. Interaktive Widgets, Hintergrund-
und asynchrone Zellen sind nicht Teil dieses Berichtsformats. Nur vertrauenswürdige
Notebooks ausführen. `audit-help` und `audit-control` entfernen Anleitung,
Typenprüfung und Exportaufruf aus dem Bericht und verhindern Exportrekursion.

## Fachliche Grundlage und Grenzen

Die Kapitel und Unterkapitel folgen dem Auditbericht Campo Breitenlee, Planung,
11.11.2026. Die Tabellen sind als native, einheitliche Parameter/Wert/Einheit-
Tabellen umgesetzt; die Word-Gestaltung ist keine pixelgenaue Kopie des Originals.
Projekttexte, Bildrechte, Pläne, Prüfstatus, Beteiligte, Ausschussentscheidungen
und fachliche Schlussfolgerungen bleiben ausdrücklich manuell zu ergänzen.
Die Beispielvorlage enthält die fünf Hauptkapitel und den technischen Anhang.
Sommer-/Winterwochen bleiben Bildplatzhalter, weil Jahreswerte keine Zeitreihen
ersetzen. Die Vorlage erteilt keine automatische Deklarationsfreigabe.

Die Tabellen behalten gespeicherte Werte und Schemaeinheiten bei (z.B. ratio =
dimensionsloser Faktor, nicht Prozent). Einzig PV-Jahresertrag und spezifischer
PV-Ertrag werden transparent aus PV_total, NFA_total und PV_kWp abgeleitet.
Import/Export-Saldo und Zielwertdifferenz werden auf endliche Zahlen und Konsistenz
geprüft (absolute Toleranz 0,05 kWhPE/(m²NGF a)). Die Zuordnung des gespeicherten
Zielwerts zum beantragten Deklarationsumfang bleibt eine fachliche Prüfung.
Fehlende optionale Werte werden nicht als Null ersetzt. Tool-/Schemaabweichungen
erscheinen sichtbar im Bericht; weder Importer noch Schema werden dabei migriert.

## Schnittstellen und Pflege

- `reporting.audit.select_scenario`, `table`, `chart`, `data_notes`: vorhandene
  annual_frame-/materialize-/Plotly-Verträge für Project, Scenario, Views und
  DataFrames. Die einzige neue fachliche Definition ist die explizite Zuordnung
  der Audit-Tabellen zu Variablen. Anforderungen werden je Tabelle ausgewertet.
  Keine neue Datenklasse, Datenbank oder persistierte Zwischenstruktur.
- `reporting.document.display_table`, `display_chart`, `render_notebook`:
  gemeinsame Anzeige und Dokumentausgabe. Der vorhandene Einzelgrafikexport
  reicht für ein Dokument aus Markdown, Tabellen und mehreren Plots nicht aus;
  seine statische Bildausgabe wird wiederverwendet. Ausgabe sind gewöhnliche
  HTML-/DOCX-Dateien, keine neue interne Austauschstruktur.
- `assets/audit-reference.docx`: paketierte Word-Formatvorlage auf Basis der
  Quarto/Pandoc-Referenz, A4 mit 20-mm-Rändern und schwarzen Calibri-Überschriften.
  Bei Layoutänderungen in Word bearbeiten und beide Ausgabeformate prüfen.
  Die Notebook-Kapitel sind die einzige Vorlage für Berichtsinhalte; keine zweite
  QMD-Vorlage. Bestehende Projektkopien werden nicht automatisch überschrieben.

Neue Variablenzuordnungen und Layoutänderungen verursachen Pflege in den jeweiligen
Tabellen bzw. der Referenzdatei und erfordern Regressionstests sowie einen realen
Renderdurchlauf. Testabdeckung: exakte Auswahl, fehlende/inkonsistente Bilanzen,
DataFrame-/Objekt-Parität, optionale Daten, Vorlagennamen, gespeicherte Freitexte,
Export ohne Rekursion und (wenn lokal vorhanden) sämtliche Beispieldatei-Typen.

Ausführung: `python -m pytest tests/test_audit.py -q`.

## Verifikation am 16.11.2026

Mit der lokalen Typendatei wurden alle 21 Varianten über die Tabellen und fünf
Diagrammtypen geprüft. Das How-to wurde einschließlich dieser Prüfung ausgeführt;
die Projektkopie enthält die Ausgaben. Die HTML-Ausgabe verwendet `Hol_PHniv`.
Ein kleiner Quarto-Integrationstest bestätigt die HTML-/DOCX-Ausgabe inklusive
neu ausgeführter Zellen und unverändertem Quellnotebook. Der vollständige DOCX-
Durchlauf mit Diagrammen blieb in der eingeschränkten Ausführungsumgebung beim
Kaleido-Start blockiert (Windows asyncio/socketpair). Ein separater Prozess
begrenzt diesen Schritt auf maximal 60 Sekunden. Der vollständige Word-Bericht
mit Bildern und dessen visuelle Abnahme sind daher noch offen; keine erfolgreiche
Prüfung des kompletten Word-Layouts behaupten. Auch die lokale HTML-Browservorschau
war in dieser Umgebung nicht erlaubt; HTML wurde strukturell geprüft.
