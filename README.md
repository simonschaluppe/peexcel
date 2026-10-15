# PEExcel – klimaaktiv Nachweistool für Plus-Energie-Quartiere

PEExcel unterstützt die Modellierung, Bewertung und Dokumentation von Quartieren mit stündlichen Energiebilanzen, erneuerbarer Erzeugung, Mobilität, Lebenszyklus und Flexibilität.

Die **[Anwenderwebsite](website/index.qmd)** enthält Einstieg, Downloads, Methoden, interaktive Lehrschnitte, Tutorials und Forschungsgrundlagen. Deutsch; zusätzlich eine [englische Startseite](website/en/index.qmd). Der Link führt bis zur gesonderten Veröffentlichung auf die Website-Quelle.

- [Excel herunterladen und starten](website/download.qmd)
- [Lernwege für Kompetenzpartner:innen und Studierende](website/learn.qmd)
- [Modellierung und verbindliche Deklarationswerte](website/declaration.qmd)
- [Kontakt, Newsletter und Nutzungshinweise](website/about.qmd)
- [Versionshistorie](CHANGELOG.md)

## Python und lokaler Website-Build

Im geklonten Repository:

```bash
python -m pip install -e ".[publication]"
quarto render website
python -m http.server 8766 --bind 127.0.0.1 --directory website/_site
```

Quarto muss lokal installiert sein. Für die statischen Plotly-Exporte wird Chrome benötigt. Die Vorschau läuft unter `http://127.0.0.1:8766`; mit Strg+C beenden. Die Website kann als statisches Build-Ergebnis veröffentlicht werden; sie führt keine Excel-Simulation im Browser aus.

Ausführbare Einstiege: [Excel/Python](notebooks/howto_excel.ipynb), [Grafikexport](notebooks/howto_publication.ipynb), [Lehrschnitte](notebooks/howto_section_teaching_preview.ipynb), [Website-Workflow](notebooks/howto_website.ipynb). Details zu [Gebäudeschnitten](docs/development/building_sections.md) und [Website-Pflege](docs/development/website_implementation_plan.md).

Für Beiträge gelten die [Projektleitlinien](AGENTS.md). Entwickelt an der FH Technikum Wien, Forschungsgruppe Climate-fit Buildings and Districts. Lizenz- und Nutzungshinweise des Repositorys beachten; bei Verwendung bitte die Quelle angeben.
