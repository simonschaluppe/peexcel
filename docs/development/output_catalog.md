# Begriffe, Parameter und Kennzahlen nachschlagen

## Umfang und Datenquelle

Nachschlagen ist ein eigener Hauptnavigationspunkt nach Deklarieren und vor Python.
Die Seite enthält Begriffe, Input-Parameter und Output-Kennzahlen. Die Excel-Kapitel
und der separate Bereich Python & Automatisierung bleiben bestehen.

`scripts/output_catalog.py` verwendet ausschließlich die vorhandenen VariableMeta-Objekte
in `pexl.schema.current`. Der Parameter `source` wählt IN oder OUT; andere Quellen werden
abgewiesen. `output_variables()` und `build()` ohne Quellenangabe behalten das bisherige
OUT-Verhalten. Die OUT-Variablenanker bleiben unverändert.

Das aktive Schema `1_13_1_dev` enthält 692 IN-Variablen (691 mit Icon) und 512 OUT-Variablen
(332 mit Icon). Labels, Einheiten, Icons, measure, Entity Group/Key und Bezüge werden
unverändert übernommen und HTML-escaped. Fehlende Felder bleiben sichtbar; fehlende Icons
werden ausgelassen. Icons stehen dezent neben dem Label und sind für Screenreader dekorativ.
Die Domänentitel sind Anzeigeübersetzungen; unbekannte Schlüssel bleiben automatisch sichtbar.

## Wartungsaufwand und Artefakte

Es gibt keine neue gepflegte Datenstruktur oder öffentliche Paket-API. Die vorhandene
Registry reicht aus. Derselbe Renderer erzeugt zwei ignorierte HTML-in-QMD-Fragmente:
`website/assets/in-catalog.qmd` und `out-catalog.qmd`. Das zusätzliche IN-Fragment ermöglicht
die getrennte Einbindung mit eigenen Suchfiltern; das OUT-Fragment allein enthält keine
Input-Definitionen. Beide enthalten ausschließlich die gerenderten Tabellen, keinen
zusätzlichen JSON-Datensatz. Sie werden beim Asset-Build erzeugt, nie manuell bearbeitet.

`website/output-catalog.js` initialisiert jede Tabelle unabhängig, mit getrennten IDs und
Filtern. `in-` und `out-` trennen auch gleichnamige Variablenanker. Es gibt keine zusätzliche
Bibliothek oder Netzwerkanfrage. Native Details bleiben ohne JavaScript nutzbar. CSS ist
auf die Kataloge beschränkt. Schnelleinstiege sind Suchhilfen und keine Schema-Domänen.

Bei Schemaänderungen werden beide Fragmente neu erzeugt. Tests prüfen die Vollständigkeit
beider Quellen, fehlende Angaben, Icon-Ausgabe und HTML-Escaping, eindeutige IDs,
deterministische Ausgabe, alte OUT-Anker und Navigation. Das bestehende ausführbare
`notebooks/howto_output_catalog.ipynb` dokumentiert und prüft beide Kataloge mit denselben
Implementierungsfunktionen. Weitere Notebooks oder gepflegte Metadatenkopien sind unnötig.

## Lokal bauen und prüfen

Der deaktivierte Pre-render-Hook bleibt unverändert. Gezielt aktualisieren:

```powershell
python scripts/output_catalog.py
quarto render website
```

Auch `python scripts/website_assets.py` erzeugt beide Fragmente. `assets/**` und
`downloads/**` bleiben vom eigenständigen Rendern ausgeschlossen.

In der Vorschau beide Kataloge suchen/filtern, unabhängige Filter, leere Ergebnisse,
Zurücksetzen, Metadaten, Icons und Direktlinks prüfen. Ein Schemaeintrag garantiert keinen
Wert in jedem Export und ist keine vollständige Definition zulässiger Eingabewerte.
