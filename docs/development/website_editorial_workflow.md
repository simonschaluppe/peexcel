# Website-Redaktion

Vereinbart am 28.10.2026. Diese Vereinbarung präzisiert die redaktionellen Vorgaben des Website-Umsetzungsplans.

## Auftrag und Zielgruppe

PEExcel ist eine Wissensplattform für Studierende und PEQ-Kompetenzpartnerinnen und -partner mit Hintergrund in Energietechnik. Sie erleichtert die Handhabung des Tools und macht seine Anwendung attraktiv. Fachwissen darf vorausgesetzt werden, Kenntnisse der konkreten Oberfläche nicht.

Erklären, was eine Funktion leistet, wofür sie nützlich ist, wo sie zu finden ist und wie Ergebnisse zu interpretieren sind. Interessante Grafiken, interaktive Darstellungen und besondere Funktionen des Tools gezielt sichtbar machen, etwa das Zusammenspiel von stündlichen Energieflüssen, Flexibilität, Variantenvergleich und Ökobilanz, soweit tatsächlich implementiert. Keine unbelegten USP-Behauptungen. Beispiele sollen nachvollziehbar sein; fachliche Aussagen und grafische Ergebnisse müssen belegbar bleiben.

## Freigabe vor Umsetzung

1. Der Projektverantwortliche annotiert direkt in Hypothesis, kurz und knapp. Markierter Text liefert den Kontext; ein Anforderungsformular ist nicht erforderlich.
2. Auf Aufforderung im Chat liest der Agent die zugänglichen PEExcel-Annotationen der vereinbarten Gruppe seitenübergreifend ein. Kommentare anderer Projekte ausschließen. Annotation-ID, URL, Originalzitat, Kommentar und Änderungszeit für den Abgleich erhalten.
3. Im Chat eine nummerierte Aktionsliste nach Seiten vorlegen: gewünschtes Ergebnis, konkrete vorgeschlagene Änderung, zugehörige Kommentare, offene fachliche Fragen und erforderliche Screenshots oder Grafiken. Zusammengehörige Kommentare dürfen ein Arbeitspaket bilden. Übergreifende Erweiterungen separat ausweisen.
4. Der Projektverantwortliche gibt die Liste oder einzelne Punkte frei, fordert Konkretisierungen, korrigiert Annahmen oder liefert Bildmaterial. Bis dahin ausschließlich lesen, analysieren und Vorschläge ausarbeiten; die betroffenen Seiten noch nicht ändern. Freigabegrenzen auch bei Teilfreigaben beachten.
5. Erst nach Freigabe umsetzen. Fehlende Abbildungen konkret anfordern oder vorhandene Quellen zur Wiederverwendung vorschlagen. Echte Bedienansichten verwenden; keine erfundenen Screenshots oder Berechnungsergebnisse.
6. Gerenderte Vorschau samt kurzer Zuordnung „Kommentar → Änderung“, Prüfstatus und offenen Punkten im Chat zur Abnahme vorlegen. Änderungen aus dieser Rückmeldung einarbeiten.
7. Abnahme, Veröffentlichung und Löschen sind getrennte Schritte. Standard: abnehmen, im autorisierten Umfang veröffentlichen und prüfen, anschließend die zugehörigen erledigten Annotationen löschen. Eine ausdrücklich anders vereinbarte Reihenfolge ist möglich. Unmittelbar vor dem Löschen IDs und Änderungszeiten mit dem bearbeiteten Stand abgleichen; neue oder geänderte Kommentare erhalten. Löschung prüfen und berichten. Keine Kommentare anderer Seiten oder neuer Bearbeitungsrunden löschen.

## Darstellung und Bildablage

- Ein kurzer grüner PEExcel-Hinweis mit Icon kann am Anfang den Ort im Menüband oder Arbeitsblatt erklären. Grüne Blöcke ansonsten sparsam für kompakte Bedienrezepte, nicht als durchgängiger Hintergrund langer Tutorials.
- Bestehende Klassen wiederverwenden: `excel-operation` für kurze Bedienhinweise, `excel-action` für tatsächliche Klickbefehle, `excel-menu` für Blatt-/Menübezeichnungen. Erklärungen und Abbildungen im normalen Seitenfluss.
- Zusammenhängende Erläuterungen statt Telegrammstil. Technische Begriffe präzise verwenden; notwendige fachliche Rückfragen vor der Umsetzung klären.
- Illustrationen thematisch unter `website/illustrations/<thema>/` ablegen. Vorhandene Ablagen und Ressourcen wiederverwenden; Herkunft, sichtbaren Versionsbezug und Pflegehinweise in `website/illustrations/README.md` festhalten.
- Quellen unterstützen die Erklärung. Die Wissensplattform soll selbst verständlich sein und die Schulungsunterlagen als Lernmedium ablösen; nicht „die Schulung sagt …“ als Argument oder Autorität verwenden. Verweise bei Bedarf als Quellenfußnote.

## Technischer Abruf und Pflege

`scripts/collect_website_annotations.ps1` liest ausschließlich über die bestehende Hypothesis-Such-API. Es verwendet den lokal mit Windows DPAPI verschlüsselten Token unter `~/.hypothesis-token.dpapi`, gibt ihn nicht aus und schreibt oder löscht keine Annotationen. Die vereinbarte Gruppe ist `Q4qRzANo`; gefiltert wird auf die veröffentlichte PEExcel-Website. Andere Gruppen oder Vorschau-URLs nur bei vereinbartem Bedarf ergänzen.

Das ausführbare `notebooks/howto_website_editorial.ipynb` ruft dasselbe Skript auf und zeigt die Kommentare zur redaktionellen Auswertung. Der Abruf verwendet die unveränderten API-Annotationen statt eines neuen Datenschemas. Eine optionale lokale Momentaufnahme im bereits ignorierten `notebooks/local_exports/` bewahrt IDs und Änderungszeiten für eine Abnahme über mehrere Sitzungen. Sie enthält private Kommentare, gehört nicht in Git oder öffentliche Website-Downloads und wird pro Redaktionsrunde neu erzeugt. Vor Löschungen den aktuellen Serverstand erneut lesen. Keine neue Datenbank, kein automatischer Löschjob und keine zusätzliche öffentliche Schnittstelle.

Pflege: Bei API-Änderungen das interne Abrufskript und Notebook gemeinsam aktualisieren. Pagination, Gruppeneinschränkung und URL-Filter bei Änderungen prüfen. Der Token bleibt ausschließlich lokal; bei fehlendem oder ungültigem Zugang abbrechen, ohne ihn in Fehlermeldungen auszugeben.

## Verbindlicher Stil für weitere PEExcel-Erklärungsseiten

Am 28.10.2026 vom Projektverantwortlichen abgenommen: Die Seiten zu PV, Haustechnik,
Modellübersicht und thermischer Hülle sind das redaktionelle Muster für weitere
Erklärungsseiten. Reale Screenshots auf relevante Bereiche zuschneiden, Eingaben
mit erklärenden Rahmen und Nummern markieren und die Nummern unmittelbar darunter
erläutern. Originalwerte erhalten, Abbildungen vergrößerbar machen und pro Thema ablegen.

Für wichtige Einschübe diese vier Bezeichnungen und Bedeutungen einheitlich verwenden:

| Kategorie | Zweck | Darstellung mit vorhandenen Mitteln |
|---|---|---|
| **Wo im PEExcel?** | Orientierung: Menüband, Gruppe, Blatt und konkrete Befehle | Kurzer grüner `excel-operation`-Block mit PEExcel-Icon, üblicherweise einmal am Anfang |
| **Deklaration** | Anforderungen oder Abweichungen für den Nachweis; Modellierbarkeit und Nachweisregeln trennen | `declaration-note` mit deutlich sichtbarem Titel „Deklaration“ |
| **Forschung / Experte** | Vertiefung zu Modellannahmen, Methodik, Daten oder weitergehenden Analysen | Quarto `callout-note`, Titel „Forschung / Experte“, bei längeren Vertiefungen `collapse=true` |
| **Achtung** | Konkrete Fehlbedienung, unzulässige Kombination oder wichtige Interpretationsgrenze | Quarto `callout-warning`, Titel „Achtung“; die konkrete Konsequenz im Text nennen |

Keine neuen Farben oder Varianten je Seite erfinden; Kategorien müssen auch anhand
des Titels erkennbar sein. Laufende Tutorials nicht vollständig in Einschübe setzen.
Bestehende Seiten bei der nächsten redaktionellen Bearbeitung an diese Benennung
angleichen; die Vereinbarung allein löst keinen ungeprüften websiteweiten Umbau aus.

Für Anfänger auf Fachseiten aufklappbare Auswahlhilfen vorsehen: **„Noch keine eigenen
Werte? Standardfälle nutzen“**. Beschreiben, für welche Situation ein vorhandenes Preset
gedacht ist, z. B. „Wenn dein Quartier …, beginne mit …“, und in den zentralen
versionsbezogenen Katalog unter „Nachschlagen“ verlinken. Dies ist eine Anforderung
an die geplante Preset-Erweiterung, noch keine Bestätigung bereits implementierter
Kataloge oder fachlicher Eignung einzelner Standardfälle.
