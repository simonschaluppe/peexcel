# Allgemeine Projektleitlinien

Diese Leitlinien gelten für das gesamte Repository.

## Website: Redaktion und Zielgruppe

- Die Website ist eine Wissensplattform für Studierende und PEQ-Kompetenzpartnerinnen und -partner mit energietechnischem Hintergrund. Sie soll die Handhabung von PEExcel erleichtern und zum Erkunden seiner Möglichkeiten motivieren.
- Stil der abgenommenen Erklärungsseiten fortführen: zugeschnittene Original-Screenshots mit Rahmen, Nummern und zugehörigen Erläuterungen. Einschübe einheitlich als „Wo im PEExcel?“, „Deklaration“, „Forschung / Experte“ und „Achtung“ kennzeichnen; Zuordnung und Gestaltung stehen im Redaktionsablauf.
- Verständliche Tutorials, aussagekräftige Grafiken, echte Bedienansichten und fachlich belegte besondere Funktionen des Tools hervorheben. Keine unbelegten Alleinstellungsversprechen; technische Zusammenhänge direkt erklären.
- Verbindlicher Redaktionsablauf: [Website-Redaktion](docs/development/website_editorial_workflow.md). Hypothesis-Kommentare auf Aufforderung sammeln, konkrete Aktionen und Materialbedarf hier im Chat vorlegen und erst nach ausdrücklicher Freigabe umsetzen. Kurze Annotationen sind ausreichend; Unklarheiten nicht stillschweigend als freigegeben behandeln.

## Review- und Wartungsaufwand

- Bestehende Datenstrukturen und Schnittstellen wiederverwenden. Neue Strukturen sowie zusätzlichen Review- und Wartungsaufwand möglichst gering halten.
- Jede neue persistierte Datenstruktur oder öffentliche Schnittstelle im Implementierungsvorschlag nachvollziehbar begründen: konkreter Nutzen, warum vorhandene Alternativen nicht ausreichen und zusätzlicher Pflegeaufwand einschließlich Erzeugung, Aktualisierung, Kompatibilität und Tests. Das gilt auch für automatisch generierte Artefakte.

## Ausführbare How-to-Notebooks

- Für jeden neuen oder erweiterten Arbeitsablauf ein ausführbares `notebooks/howto_*.ipynb` erstellen oder ein passendes bestehendes Notebook aktualisieren.
- Das Notebook erklärt den vollständigen betroffenen Arbeitsablauf und die Erweiterungen mit nachvollziehbaren Beispielen.
- Dieselben Implementierungsfunktionen wie Anwendung, Skript oder CLI verwenden; keine zweite Implementierung im Notebook pflegen.
- Das Notebook ist Teil der Abnahme. Eine README allein genügt nicht.
