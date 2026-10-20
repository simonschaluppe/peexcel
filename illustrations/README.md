# Stufengrafik

`peq-stufen.png` ist ein Ausschnitt aus Seite 4 von
`docs/PEQ Nachweistool 2026-10-14.pdf`. Die bisherige GitHub-Bildreferenz der README
war bei der visuellen Prüfung nicht erreichbar. Die Originaldarstellung aus der
Schulung erhält Icons, Farben und fachliche Beschriftungen; keine neue Grafiklogik.

Reproduktion mit Poppler aus dem Repository-Verzeichnis:

```powershell
pdftoppm -f 4 -singlefile -scale-to 3200 -x 1440 -y 510 -W 1500 -H 930 -png "docs/PEQ Nachweistool 2026-10-14.pdf" website/illustrations/peq-stufen
```

Die kleine abgeleitete Abbildung wird versioniert, damit normale Website-Builds
keine zusätzliche PDF-Render-Abhängigkeit benötigen. Bei Änderungen an der
Quellfolie den Ausschnitt neu erzeugen, visuell prüfen und gemeinsam aktualisieren.
Die Original-PDF bleibt unverändert und ist auf der Downloadseite verfügbar.


## Forschungsbeispiele und Bediengrafiken

`mobprofiles.png` und `userflexmodel.svg` sind bereitgestellte Originalgrafiken.
`schleife.svg` zeigt den Bearbeitungszyklus. Die drei Deklarationsgrafiken
`deklarationen.svg`, `ihr_weg_zum_peq.svg` und `programmteam.svg` wurden unverändert
aus `docs/website/` übernommen, damit alle Website-Ressourcen im Quarto-Projekt liegen.
Diese Dateien werden als Quellen gepflegt, nicht bei jedem Build neu erzeugt.

Die zwei zusätzlichen PNGs sind feste Ausschnitte aus den vom Autor bereitgestellten
Papern: `flexibility-study.png` aus Schneider et al. (2025), DOI
10.3390/designs9060123, S. 20, Abb. 11; `mobility-results.png` aus Schneider und
Baptista (2025), DOI 10.1109/EEEIC/ICPSEurope64998.2025.11169136, S. 6, Abb. 7.
Sie erhalten Originalachsen und Legenden; deutsche Erläuterungen und Quellenlinks
stehen in den QMD-Seiten. Die Ausschnitte vermeiden unleserliche Ganzseiten und
benötigen keine PDF-Abhängigkeit beim regulären Website-Build. Bei Quellenänderungen
neu ausschneiden, visuell prüfen und Bildunterschriften gemeinsam aktualisieren.
Es gibt kein neues Datenschema und keine aus den Bildern abgeleitete Berechnung.

Reproduktion mit Poppler (PDF-Pfade auf die lokalen Originale setzen):

```powershell
pdftoppm -f 20 -singlefile -scale-to 3000 -x 583 -y 583 -W 1417 -H 817 -png $declarationPdf website/illustrations/flexibility-study
pdftoppm -f 6 -singlefile -scale-to 3000 -x 150 -y 200 -W 1800 -H 1833 -png $mobilityPdf website/illustrations/mobility-results
```
