# Signallabor – Netzdienlichkeitssignale (PEXL)

## Start

1. ZIP vollständig entpacken; beide Notebooks, `signallabor_data.csv` und `assets/` im gleichen Ordner belassen.
2. Python und JupyterLab oder VS Code mit den Erweiterungen Python und Jupyter einrichten. [Jupyter-Installation](https://jupyter.org/install) · [Jupyter in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks).
3. Notebook 01 öffnen, Python-Kernel auswählen. Falls nötig die Installationszelle aktivieren (`%pip install pandas numpy matplotlib`), anschließend alle Zellen ausführen. Bei Bedarf Kernel neu starten.
4. Die mit EXPERIMENT gekennzeichneten Parameter ändern, Zellen erneut ausführen und Leitfragen in Markdown beantworten.
5. Notebook 02 mit den Kennwerten aus der eigenen PEExcel-Variante bearbeiten. Es ist unabhängig von Notebook 01 ausführbar.

## Inhalt

- `01_signallabor_AB.ipynb`: Signalherkunft, Schwellenwerte, rollierende Quantile, Aktivierungsfunktionen.
- `02_signallabor_gebaeude.ipynb`: Thermische Gebäudecharakteristik, PEExcel-Zuordnung, Lade-/Entladezeiten, zeitliche Filter und Look-ahead.
- `signallabor_data.csv`: unveränderte, vorbereitete historische Übungsdaten (2021/2022, jeweils 8760 Stunden). Herkunft und Einschränkungen siehe Notebooks.
- `assets/`: neun statische Konzeptgrafiken als SVG, relativ aus Markdown referenziert; für die Wissensplattform wiederverwendbar. Dynamische Experimentgrafiken werden im Notebook berechnet.
- `output/`: wird bei Ausführung erzeugt; enthält das jeweils ausgewählte Signal, die dokumentierte Zeitreihe und Parameter.

Keine PEXL-Installation für diese beiden Notebooks erforderlich. `QHmax_total_m2` wird im zweiten Notebook aus IN übernommen. Die Beispiel-Heizleistung und Komforttemperaturen sind illustrative Annahmen und durch eigene Werte zu ersetzen.

Vor der PEExcel-Anwendung sind Importformat, konkrete Signalzuordnung und die zeitliche Synchronisation der historischen Daten mit der Simulationszeitachse zu prüfen. Vor öffentlicher Weiterverteilung der historischen Daten sind die Nutzungsbedingungen der jeweiligen Datenquellen zu prüfen.

[PEExcel-Wissensplattform](https://simonschaluppe.github.io/peexcel/)
