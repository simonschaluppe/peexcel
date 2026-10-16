# Allgemeine Projektleitlinien

Diese Leitlinien gelten für das gesamte Repository.

## Review- und Wartungsaufwand

- Bestehende Datenstrukturen und Schnittstellen wiederverwenden. Neue Strukturen sowie zusätzlichen Review- und Wartungsaufwand möglichst gering halten.
- Jede neue persistierte Datenstruktur oder öffentliche Schnittstelle im Implementierungsvorschlag nachvollziehbar begründen: konkreter Nutzen, warum vorhandene Alternativen nicht ausreichen und zusätzlicher Pflegeaufwand einschließlich Erzeugung, Aktualisierung, Kompatibilität und Tests. Das gilt auch für automatisch generierte Artefakte.

## Ausführbare How-to-Notebooks

- Für jeden neuen oder erweiterten Arbeitsablauf ein ausführbares `notebooks/howto_*.ipynb` erstellen oder ein passendes bestehendes Notebook aktualisieren.
- Das Notebook erklärt den vollständigen betroffenen Arbeitsablauf und die Erweiterungen mit nachvollziehbaren Beispielen.
- Dieselben Implementierungsfunktionen wie Anwendung, Skript oder CLI verwenden; keine zweite Implementierung im Notebook pflegen.
- Das Notebook ist Teil der Abnahme. Eine README allein genügt nicht.
