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
