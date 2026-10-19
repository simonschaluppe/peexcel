# Bewertungsseite erzeugen und in den Hintergrundbericht übernehmen

## Quelle und Erzeugung

Die fachlichen Texte werden ausschließlich in
`notebooks/howto_assessment_explained.ipynb` gepflegt. Die Markdown-Zellen haben
einen `section`-Metadatenschlüssel für ihre Position auf der Seite.
`scripts/assessment_explained.html` enthält Gestaltung und Auswahlsteuerung;
`scripts/assessment_explained.py` erzeugt die Grafiken über die bestehenden
PEExcel-Reports und Plotfunktionen. Die Breite richtet sich nach dem verfügbaren
Platz, unabhängig von der Anzahl ausgewählter Szenarien.

Die Legende wird unter der PE-Grafik als zwei kompakte HTML-Boxen dargestellt;
bei THG ergänzt eine dritte Box die Gesamtbilanz und die L1-/L2-/L3-Bereiche.
Ihre Einträge schalten die entsprechenden Plotly-Reihen gemeinsam ein und aus.
Auf breiten Bildschirmen bleibt die Szenarioauswahl rechts beim Scrollen stehen;
bis 1000 Pixel Fensterbreite wird sie oberhalb des Inhalts angezeigt.
Die HTML-Legenden gehören zur Seite, nicht zum SVG aus Plotlys Bildexport.

Im PEExcel-Projekt ausführen:

```powershell
Set-Location C:\Users\schneids\code\peexcel
python scripts/assessment_explained.py
```

Für einen anderen Projektexport und einen eigenen Ausgabepfad:

```powershell
python scripts/assessment_explained.py --source "C:\Projekte\Export.xlsx" --output "notebooks/local_exports/mein-projekt/index.html"
```

Das ausführbare Beispiel und der Ablauf für beide Bewertungsansichten stehen
in `notebooks/howto_website.ipynb`. Der normale PEExcel-Website-Build erzeugt den
Explorer automatisch mit dem Lehrprojektexport und bindet ihn unter
`assessment-explained.html` ein. Das technische Tutorial bleibt unter
`assessment.html` erreichbar. Beide sind auf der Python-Seite verlinkt.

Alternativ die Codezelle des Notebooks ausführen. Die Ausgabe liegt unter
`notebooks/local_exports/assessment_explained/index.html`. Die Datei enthält
Texte, vorberechnete Diagramme, Auswahlsteuerung und Plotly vollständig und
benötigt keinen Python-Server. Sie ist ein ignoriertes Veröffentlichungsartefakt;
es gibt keine separat zu pflegende Datendatei oder zusätzliche Reportstruktur.

## In peq-higrube einbinden

Die folgenden Schritte werden manuell im Zielprojekt ausgeführt. Das geprüfte
Quarto-Projekt liegt im verschachtelten Verzeichnis
`C:\Users\schneids\code\peq-higrube\peq-higrube` und baut nach `_book`.

```powershell
$target = 'C:\Users\schneids\code\peq-higrube\peq-higrube'
New-Item -ItemType Directory -Force -Path "$target\assets\assessment"
Copy-Item -LiteralPath 'C:\Users\schneids\code\peexcel\notebooks\local_exports\assessment_explained\index.html' -Destination "$target\assets\assessment\index.html"
```

In der vorhandenen `_quarto.yml` unter `project.resources` ergänzen (die
bestehenden Ausschlüsse erhalten):

```yaml
    - "assets/assessment/**"
```

Beispielsweise in `Kapitel/07-anwendung.qmd` an der gewünschten Stelle einfügen:

````markdown
## Bewertung interaktiv nachvollziehen

```{=html}
<iframe src="../assets/assessment/index.html"
        title="Bewertungssystem und Quick Check"
        style="width:100%;height:1400px;border:0;"
        loading="lazy"></iframe>
<p><a href="../assets/assessment/index.html" target="_blank" rel="noopener">
Quick Check in voller Breite öffnen</a></p>
```
````

Der relative Pfad gilt für ein Kapitel unter `Kapitel/`. Bei Einbindung in eine
QMD-Datei im Projektstamm stattdessen `assets/assessment/index.html` verwenden.
Die HTML-Einbettung erscheint nicht im PDF; dafür wäre eine separate statische
Abbildung erforderlich.

## Bauen und veröffentlichen

Nach dem Kopieren und Einbinden:

```powershell
Set-Location C:\Users\schneids\code\peq-higrube\peq-higrube
quarto render --to html
```

Die Ausgabe unter `_book` prüfen; insbesondere
`_book/assets/assessment/index.html` und die einbettende Kapitelseite. Änderungen
an den Quellen einschließlich der übernommenen HTML-Datei im Zielprojekt
committen. Anschließend bewusst veröffentlichen:

```powershell
quarto publish gh-pages --no-render
```

Dieser letzte Befehl pusht die fertige Ausgabe nach `gh-pages`. Er ist kein
lokaler Vorschau-Befehl. Das Zielrepository ist
`https://github.com/simonschaluppe/peq-higrube`.

Bei späteren Änderungen: in PEExcel neu erzeugen, die HTML-Datei erneut kopieren,
den Hintergrundbericht bauen, prüfen und veröffentlichen. Das erzeugte HTML
nicht direkt bearbeiten.
