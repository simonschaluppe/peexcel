# Skizze: Preset-Katalog unter „Nachschlagen“ und spätere Nutzung in pexl

Status: Website-Umsetzung am 28.10.2026 freigegeben. Maßgeblich ist die unten dokumentierte reduzierte Ausbaustufe; frühere weitergehende Vorschläge bleiben zurückgestellt. Die folgenden Entscheidungen sind Vorschläge, soweit nicht ausdrücklich als Nutzeranforderung bezeichnet.

## Ziel

Neben IN-Parametern und OUT-Kennzahlen sollen Anwender die tatsächlich verfügbaren Preset-Kataloge durchsuchen können: Name, Zweck, zugehöriges Blatt, betroffene Eingaben und Werte. Fachseiten wie Heizung oder PV verlinken direkt in den passenden Katalogabschnitt. „Presets anwenden“ bleibt die kurze Bedienanleitung; „Nachschlagen → Presets“ wird die vollständige Referenz.

## Vorhandene Bausteine wiederverwenden

- `scripts/output_catalog.py` erzeugt die durchsuchbaren IN-/OUT-Kataloge aus dem aktiven Schema. `website/output-catalog.js` und die `.schema-catalog`-Formatierung liefern bereits Such-/Filter- und Aufklappmuster. Für Presets die Darstellung wiederverwenden, aber Presets nicht künstlich als IN-/OUT-Variablen deklarieren.
- `src/pexl/schema/current.py` bindet das aktive generierte Schema ein. `SCHEMA_META` und `ATTR_NAME_MAP` liefern Metadaten und die Zuordnung kanonischer `var_name` zu Python-Attributen. Labels und Einheiten daraus beziehen, nicht im Preset-Katalog duplizieren.
- `src/pexl/spatial/data/hvac_presets.json` enthält bereits einen abgegrenzten HVAC-Snapshot mit Kategorie, Namen, Quellbereichen und Werten je `var_name`, außerdem Workbook-Herkunft und Hash. Er beruht auf gecachten Werten und ist kein Nachweis aller aktuellen Excel-Presets.
- `src/pexl/spatial/presets.py` nutzt diesen Bestand für Lehrgrafiken. Die visuellen Zuordnungen sind keine allgemeine Logik zum Anwenden von Szenario-Presets. Sie dürfen dafür nicht stillschweigend wiederverwendet werden.
- `Scenario.v` hält bereits die Szenarioeingaben; die bestehende Schema- und Validierungslogik sowie Excel-Ein-/Ausgabe beibehalten.

## Kleine, überprüfbare Schritte

1. **Inventur:** Tatsächliche Preset-Tabellen der freigegebenen Arbeitsmappe erfassen: Kategorien, Tabellen-/Bereichsnamen, Spaltenbedeutung, `var_name`, Einheiten, Formeln gegenüber gespeicherten Werten und Toolversion. Den vorhandenen HVAC-Snapshot dagegen prüfen. Keine Auswahlmöglichkeiten aus Screenshots oder Namen erraten.
2. **Lesender Katalog:** Zunächst nur bestätigte Kategorien darstellen. Suche über Presetname, Kategorie und betroffene Variablen; Detailansicht mit Wertebelegung und Links zu IN-Einträgen. Herkunft, Toolstand und Vollständigkeit sichtbar machen. Unter „Nachschlagen“ einbinden und aus Fachseiten verlinken. Bedienung und fachliche Erklärung getrennt von vollständigen Wertetabellen pflegen.
3. **Schema-Anbindung:** Erst nach der Inventur entscheiden, ob die vorhandene Preset-Struktur in den Schema-Export übernommen werden kann. Beschlossen: Excel bleibt die verbindliche Quelle. Ein Export erzeugt eine versionierte Ansicht der Werte aus einer konkret identifizierten Arbeitsmappe; keine unabhängige Bearbeitung der Werte im Katalog. Der Website-Katalog und pexl lesen dieselbe Ansicht. Keinen unabhängig editierten JSON-/CSV-Zweitbestand führen.
4. **Szenarien konfigurieren:** Belegte Presetwerte auf die zugehörigen IN-Variablen anwenden; manuelle Vorwerte werden überschrieben. Eine verpflichtende Änderungsvorschau ist nach Entscheidung 5 nicht vorgesehen. Leere Felder bedeuten nicht automatisch null; OUT-Werte nicht überschreiben. Überlappende Presets, fehlende Variablen und inkompatible Toolstände müssen sichtbar behandelt werden. Ein Preset setzt Eingaben; es führt nicht automatisch eine Excel-Simulation aus.

## Entscheidung über Datenstruktur und Schnittstelle

Eine neue persistierte Struktur ist nur gerechtfertigt, wenn Excel-Tabellen und der vorhandene HVAC-Snapshot nicht ausreichen, den freigegebenen Bestand reproduzierbar und versionsbezogen bereitzustellen. Konkreter Nutzen wäre dieselbe Auswahl in Website und pexl ohne installierte Excel-Laufzeit. Zusatzaufwand: Exporter pflegen, Quellen-/Versionswechsel erkennen, Formelwerte zuverlässig gewinnen, fehlende Werte erhalten, Kompatibilität prüfen und generierte Dateien reproduzieren. Den bestehenden HVAC-Snapshot bei einer Ablösung migrieren, nicht parallel widersprüchlich weiterpflegen.

Kanonische `var_name` aus dem bestehenden Schema wiederverwenden. Identität eines Presets nicht nur am sichtbaren Namen festmachen: Kategorie, Quelle und Versionsbezug gehören zur Zuordnung. Ob dafür zusätzliche stabile IDs benötigt werden, entscheidet die Inventur; hier wird noch kein Schema festgelegt.

Eine öffentliche `apply_preset`-Schnittstelle ist in dieser Runde nicht erforderlich. Für einen ersten Prototyp reicht eine interne Funktion, die eine geprüfte Belegung vorhandener IN-Variablen zurückgibt. Eine spätere öffentliche Schnittstelle müsste ihren Mehrwert gegenüber vorhandenen Attributzuweisungen belegen: atomare Anwendung, Konfliktbericht, Kompatibilitätsprüfung und klare Regeln für fehlende Werte. Namen und Signatur erst im separaten Implementierungsvorschlag festlegen.

## Abnahme im Folgechat

- Ein realer Heizungs-Preset und ein Preset einer zweiten Kategorie stimmen mit dem freigegebenen Excel-Stand überein.
- Such-/Filterdarstellung verwendet den gleichen bestätigten Bestand wie die Python-Auswahl.
- Übernahme ändert ausschließlich die vorgesehenen IN-Werte; Konflikte, fehlende Werte und Schemaabweichungen werden geprüft. OUT und ursprüngliches Vergleichsszenario bleiben erhalten.
- Ein ausführbares How-to demonstriert Katalogsuche, Änderungsübersicht, gezielte Anwendung und anschließenden bestehenden Simulationsablauf mit denselben Implementierungsfunktionen.
- Erst nach Freigabe der Architektur und Anforderungen entwickeln. Der zugehörige Hypothesis-Kommentar bleibt bis zur vollständigen Umsetzung offen.


## Bestätigte Anforderungen aus der Abnahme

- Zentraler Preset-Bestand für alle Module; bestehende HVAC-Sonderlösungen integrieren.
- Versionierung mit nachvollziehbaren konkreten Werten, besonders für die wiederholt uneinheitlich verwendete Nutzerstromtabelle.
- Bestand auf der Website unter „Nachschlagen“ einsehen und mit Hypothesis kommentieren können. Werte und Erläuterungen sind öffentlich einsehbar; interne Diskussionen finden in der privaten Hypothesis-Gruppe statt.
- Fachseiten bieten aufklappbare Standardfall-Hilfen für Menschen ohne eigene belastbare Eingabewerte. Zweck, passende Situation, Grenzen und Link zum Katalog gehören dazu.
- Website, Excel und pexl sollen auf denselben nachvollziehbaren Stand Bezug nehmen können.

## Vorgeschlagene zentrale Architektur

Eine konkret identifizierte Excel-Arbeitsmappe als verbindliche fachliche Quelle speist einen versionierten Katalog. Derselbe Katalog
wird von der Website-Referenz, den Auswahlhilfen, der Python-Szenariokonfiguration
und den HVAC-Lehrgrafiken gelesen. Er ist kein Bestandteil der räumlichen Visualisierung.
Die bestehende Visualisierung bleibt ein Verbraucher; ihre Darstellungsvorschriften
gehören weiterhin in `spatial`, die fachlichen Presetwerte künftig in den zentralen Bestand.

Die bestehende Schema-Infrastruktur definiert weiterhin Variablen, Datentypen, Einheiten
und Zuordnungen. Der Preset-Katalog definiert **Wertebelegungen dieser Variablen**.
Katalog und Schema sind verbunden, aber nicht identisch. Ein korrigierter Nutzerstromwert
ändert nicht automatisch die Definition der zugehörigen Eingabevariable.

Die endgültige Datei-/Modulstruktur erst nach Inventur festlegen. Zunächst keine
Datenbank und keine zusätzliche Webanwendung. Die bisherigen IN-/OUT-Kataloge bleiben
unverändert; gemeinsame Darstellungs- und Filterbausteine können wiederverwendet werden.

## Versionierung: Vorschlag zur Entscheidung

1. **Unveränderlicher Katalogstand:** Jeder freigegebene Stand gehört zur jeweiligen
   Toolversion, ohne eigene Katalogversionsnummer. Historische Werte bleiben nachvollziehbar;
   die Website zeigt nur den neuesten Stand (Entscheidung 6).
2. **Inhalt nachprüfbar:** Zu einem Stand gehören konkrete Werte und ein reproduzierbarer
   Inhalts-Hash. Zahlen, Einheiten, Leerwerte und Bezüge müssen deterministisch exportiert
   werden. Ein Hash des gesamten Workbooks reicht nicht: Layoutänderungen würden sonst
   ebenfalls einen neuen vermeintlichen Presetstand erzeugen.
3. **Identität erhalten:** Katalogeinträge brauchen stabile Identität unabhängig vom
   sichtbaren Namen. Vorhandene Schlüssel nach Inventur wiederverwenden; erst bei Bedarf
   zusätzliche IDs einführen. Nicht allein Tabellenposition oder übersetzten Namen verwenden.
4. **Kompatibilität dokumentieren:** Katalogversion mit verwendbarer Schema-/Toolversion
   verknüpfen. Nicht ungeprüft „aktuellen“ Katalog in alte Arbeitsmappen einsetzen.
5. **Bekannter Stand versus lokale Änderungen:** Eine Arbeitsmappe sollte künftig die
   Katalogversion ausweisen. Ein Abgleich ihrer tatsächlichen Werte mit dem Katalog erkennt
   Abweichungen und kennzeichnet sie als lokal verändert. Bei älteren Dateien ohne Kennung
   kann ein tabellenweiser Wertevergleich bekannte Stände identifizieren; sonst „unbekannt“.
6. **Nachvollziehbare Szenarien:** Beim Anwenden eines Presets die verwendete Katalogversion
   und Presetidentität festhalten. Die tatsächlichen Szenarioeingaben bleiben maßgeblich;
   spätere Handänderungen nicht als unverändertes Preset ausgeben. Speicherort und Umfang
   dieser Herkunftsangaben sind eine offene Architekturentscheidung.

Ein Katalog kann nachweisen, welche Werte freigegeben sind und welcher Stand in einer
geprüften Datei steckt. Er erfasst nicht automatisch, wer auf welchem Rechner welche
Datei benutzt. Ein persönliches Nutzungsregister wäre eine zusätzliche, hier nicht
angeforderte Funktion. Vorgeschlagen ist zunächst die Identifizierbarkeit der Dateien.

## Zwei Ansichten aus derselben Quelle

**Nachschlagen:** Den neuesten Toolstand anzeigen, Kategorien und Presets durchsuchen,
konkrete Werte mit Einheiten und Herkunft ansehen. Keine parallele Release-/DEV-Auswahl
oder öffentliche Versionsauswahl vorgesehen. Historische Werte bleiben zur Nachvollziehbarkeit
erhalten; ihre öffentliche Darstellung ist keine Anforderung. Bei der redaktionellen
Bearbeitung den kommentierten Stand festhalten, damit Diskussionen nicht unbemerkt
neueren Werten zugeschrieben werden.

**Thematische Seiten:** Aufklappbarer Einstieg „Noch keine eigenen Werte? Standardfälle
nutzen“. Wenige fachlich beschriebene Situationen statt vollständiger Wertelisten.
Auswahlhilfen verweisen auf den exakt beschriebenen Katalogstand. Eine Empfehlung für
ein konkretes Quartier braucht überprüfbare Kriterien; keine automatische Eignungszusage
allein aus dem Presetnamen. Beschreibungen werden zentral am Preset gepflegt und in die
Fachseite eingebunden; keine Kopien pro Seite.

## Erforderliche zusätzliche Pflege, falls freigegeben

- Versionierte Wertestände: notwendig für reproduzierbare Nutzerstrom- und andere
  Presettabellen. Pflege umfasst Erzeugung, fachliche Freigabe, Vergleich und Archivierung.
  Der vorhandene HVAC-Snapshot deckt diese vollständige Historie nicht ab und soll bei
  Migration ersetzt oder aus derselben zentralen Quelle erzeugt werden.
- Herkunftsangaben in Arbeitsmappen/Szenarien: Nutzen ist die eindeutige Standzuordnung.
  Vorhandene Projekt-/Szenariometadaten zuerst prüfen; nur fehlende Informationen ergänzen.
  Aufwand umfasst Excel-Export/Import, Rückwärtskompatibilität und Tests für lokale Änderungen.
- Stabiler Zugriff für Verbraucher: Zunächst interne Katalog-/Validierungsfunktionen;
  öffentliche API erst bei konkretem Bedarf. Eine gemeinsame Auflösung von IDs, Versionen
  und Wertebelegungen verhindert unterschiedliche Regeln in Website, HVAC und Szenarien.
- Prüfung: Export eines realen Nutzerstrom- und HVAC-Katalogs gegen Excel, Unterschiede
  zwischen Versionen, unveränderte historische Stände, kompatible Variablen/Einheiten,
  Leerwertbehandlung, Konflikte überlappender Presets und Herkunft nach manuellen Änderungen.
  Beispiele verwenden dieselben Funktionen im ausführbaren How-to.

## Entscheidungsfolge für die Anforderungsgespräche

1. Pflegequelle, unabhängige Katalogversionen und Sichtbarkeit/Zugriffsschutz.
2. Katalogumfang: nur Preset-Auswahl oder auch feste Referenz-/Nutzerstromtabellen;
   priorisierte erste Kategorien und Beispielarbeitsmappen.
3. Standzuordnung: Version anzeigen, Abweichungen erkennen, Update-Hinweise oder
   explizite Synchronisation; Umgang mit lokalen Anpassungen und Altdaten.
4. Freigabeprozess: wer bearbeitet, wer prüft, Entwurf versus freigegeben, Anlass und
   Benennung neuer Versionen, fachliche Quellen und Änderungsbegründungen.
5. Benutzerführung: Standardfall-Kriterien, Detailtiefe, Katalogsuche, Versionsvergleich
   und Zuordnung von Hypothesis-Diskussionen.
6. Anwendung in pexl und Excel: einzelne Presets versus Kombinationen, Überschreibungs-
   regeln, nutzungsspezifische Werte, Formeln/Abhängigkeiten und erforderliche Historie.
7. Migration des HVAC-Bestands, erster vertikaler Durchstich und konkrete Abnahmekriterien.

Die Antworten werden hier fortgeschrieben. Bis zur Freigabe keine Katalogmigration
oder neue persistierte Laufzeitstruktur implementieren.


## Entscheidung 1: Excel bleibt autoritativ

Vom Projektverantwortlichen bestätigt: Maßgeblich sind die Werte in der herunterladbaren
Excel-Arbeitsmappe. Der zentrale Katalog, die Website und Python-Verbraucher bilden diesen
Stand ab. Solange keine verlässliche automatische Übernahme zentral gepflegter Werte nach
Excel existiert, gibt es keine zweite führende Pflegequelle im Repository.

Konsequenzen für den Entwurf:

- Fachliche Werte in Excel ändern und dort prüfen; danach den Katalog daraus exportieren.
- Jeden exportierten Katalogstand einer konkreten Quellarbeitsmappe und deren Inhalt zuordnen.
- Nicht den alten Katalog bei jedem Website-Build stillschweigend mit einer beliebigen
  lokalen Entwicklungsdatei überschreiben. Auswahl der Quellarbeitsmappe und Freigabestatus
  müssen ausdrücklich feststehen.
- Korrekturen im Katalog oder Hypothesis-Kommentare sind Änderungsvorschläge. Verbindliche
  Wertänderungen müssen zunächst in Excel umgesetzt werden.
- Historische Katalogstände bleiben Nachweise ihrer jeweiligen Excel-Quelle; sie werden
  nicht nachträglich mit neueren Werten überschrieben.
- pexl und Visualisierungen können diese exportierten Stände zentral lesen, ohne eine
  konkurrierende fachliche Datenquelle zu bilden.

Die nachfolgenden Entscheidungen legen Versionsbindung und Sichtbarkeit fest. Ein Inhalts-Hash dient nur der technischen Prüfung; er begründet keine unabhängige Veröffentlichung von Presets.


## Entscheidungen 2 und 3: Versionsbindung und Sichtbarkeit

Vom Projektverantwortlichen ausdrücklich bestätigt:

- Jeder freigegebene Preset-Stand gehört fest zu einer Excel-Toolversion. Keine unabhängigen Preset-Releases.
- Preset-Werte und Erläuterungen sind auf der Website öffentlich einsehbar.
- Interne Diskussionen finden in der bestehenden privaten Hypothesis-Gruppe statt. Die private Gruppe schützt die Kommentare, nicht die öffentlich dokumentierten Werte.

Folgerungen für die vorgeschlagene Umsetzung:

- Die Toolversion kennzeichnet den Katalogstand. Keine zusätzliche fachliche Katalogversionsnummer erforderlich; die Website zeigt gemäß Entscheidung 6 nur den neuesten Stand.
- Ein technischer Hash der exportierten Tabelleninhalte kann prüfen, ob eine Datei tatsächlich dem freigegebenen Stand entspricht. Unterschiedliche Werte bei gleicher Toolversionsnummer gelten als Abweichung oder Entwicklungsstand, nicht als zweiter freigegebener Katalog.
- Änderungen an freigegebenen Preset-Werten erfordern eine neue Toolversion. Der aktuelle Entwicklungsstand heißt 1.13.1-Dev; siehe Entscheidung 6.
- Historische Toolversionen behalten ihre unveränderten Werte als Nachweis. Die Website zeigt den neuesten Stand.
- Keine neue Anmeldung oder Zugriffsschutz-Infrastruktur für den Katalog nötig. Interne Kommentare in der privaten Hypothesis-Gruppe führen.

Geklärt: Auch Referenz- und Standardwerttabellen sind technisch Presets. Alle sind benannte Pakete zusammengehöriger Variablenwerte, die gemeinsam gesetzt werden. Die inhaltliche Unterscheidung begründet keine unterschiedlichen technischen Typen oder Anwendungspfade. Der Umfang der ersten Ausbaustufe bleibt offen.


## Entscheidung 4: Einheitlicher technischer Preset-Begriff

Vom Projektverantwortlichen erläutert: Referenz- und Standardwerttabellen werden in Excel
bereits mit derselben Preset-Mechanik verwendet. Ein Preset fasst mehrere Variablenwerte
unter einem Namen zusammen und setzt sie gemeinsam. Beispiele sind Nutzerstromwerte
nach einer Deklarationsvorgabe oder nach einer bestimmten Ausgabe der OIB-Richtlinie.
Die konkrete Ausgabe und fachliche Gültigkeit müssen aus der Quelle ermittelt werden;
es wird hier kein bestimmter OIB-Stand behauptet.

Folgerungen:

- Ein gemeinsames technisches Datenmodell und ein gemeinsamer Anwendungspfad für alle
  Presets. Keine parallelen Klassen oder Importer für „Referenztabelle“ versus „Standardfall“.
- Dieselben zentralen Presetwerte versorgen Excel-Abgleich, Website, pexl und HVAC-Ansichten.
- Unterschiede in Zweck, fachlicher Quelle und Eignung redaktionell erklären: etwa
  typische Anlagenkonfiguration, Referenzwerte oder Deklarationsvorgaben. Diese Einordnung
  steuert Darstellung und Auswahlhilfe, nicht die technische Werteübernahme.
- Kategorien nicht vorschnell als gegenseitig ausschließende Typen festschreiben. Ein
  Preset kann mehrere fachliche Bezüge haben. Ob dafür neue Metadaten erforderlich sind
  oder vorhandene Bezeichnungen/Beschreibungen genügen, erst bei der Inventur entscheiden.
- Deklarationsbezug ist keine automatische Bestätigung der Zulässigkeit jedes mit dem
  Preset erzeugten Szenarios. Quelle, Ausgabe und zugehöriger Toolstand bleiben sichtbar.

Nächste Frage: Wie verhält sich das heutige Excel beim Anwenden auf bereits bearbeitete
Eingaben? Vollständiges Überschreiben aller zum Preset gehörenden Variablen, Umgang mit
leeren Zellen und mögliche Abhängigkeiten müssen erfasst werden. pexl soll diese Semantik
nachbilden, nicht eine konkurrierende Preset-Logik einführen.


## Entscheidung 5: Überschreiben und leere Zellen

Vom Projektverantwortlichen für den Entwurf festgelegt:

- Beim Anwenden überschreiben belegte Presetwerte die zugehörigen Eingaben, auch wenn
  diese zuvor manuell angepasst wurden. Kein zusätzlicher Schutz oder verpflichtender
  Bestätigungsdialog speziell für manuelle Anpassungen vorgesehen.
- Leere Presetzellen bedeuten „nicht setzen“: Der bisherige Szenariowert bleibt erhalten.
  Insbesondere sind leere Zellen nicht mit null gleichzusetzen; eine explizite numerische
  Null ist ein zu übernehmender Wert.
- Nachträgliche manuelle Anpassungen sind zulässig. Die tatsächlichen Eingabewerte sind
  für die Auswertung maßgeblich. Abweichungen von Deklarationsvorgaben gehören in den
  Audit-Ablauf, nicht in eine zusätzliche Schutzlogik des Preset-Katalogs.
- Daraus folgt keine Behauptung, dass der bestehende Audit bereits jede denkbare manuelle
  Änderung erkennt. Keine neue Audit-Funktion in diesem Architekturgespräch zugesagt.
- Die Aussage zu leeren Zellen ist die vereinbarte Zielsemantik. Den tatsächlichen
  Excel-Code bei späterer Implementierung dagegen prüfen; die Untersuchung ist derzeit
  ausdrücklich nicht dringend. Abweichungen dann vor einer Änderung vorlegen.

Die zuvor vorgeschlagene verpflichtende Änderungsvorschau ist damit keine Anforderung.
Ein Versionsvergleich im Nachschlagekatalog bleibt davon unabhängig sinnvoll. Beim
späteren Anwenden mehrerer Presets muss die Reihenfolge explizit sein; wie diese fachlich
kombiniert werden, ist noch im jeweiligen Ablauf festzulegen.

## Entscheidung 6: Website zeigt den neuesten Stand

Vom Projektverantwortlichen bestätigt:

- Auf der Website soll nur der neueste Stand dargestellt werden, aktuell **1.13.1-Dev**.
- Keine parallele Darstellung eines älteren Releases und eines separaten DEV-Katalogs.
- Ziel bis zum Ende des laufenden Redaktionszyklus: diesen Toolstand veröffentlichen
  und als Release freigeben. Bis zur tatsächlichen Freigabe bleibt er als DEV gekennzeichnet.
- Die versionsbezogene Nachvollziehbarkeit der Presetwerte bleibt erforderlich;
  daraus folgt keine öffentliche Archivansicht oder Versionsauswahl auf der Website.

Diese Entscheidung beschreibt das Release-Ziel, bestätigt aber noch keine erfolgte
Veröffentlichung und gibt die bisher nur skizzierte Katalogimplementierung nicht frei.

## Konkreter Ablagevorschlag zur Freigabe

Vorgeschlagene neue Dateien, noch nicht implementiert:

- `src/pexl/schema/generated/presets_1_13_1_dev.json`: ein zentraler, aus Excel
  erzeugter Wertebestand je Toolversion. Bestehende HVAC-JSON-Struktur als Ausgangspunkt
  verwenden (Quelle, Kategorien, Namen, Belegungen nach var_name). Quellbereiche,
  Toolversion und Inhaltskennung nachvollziehbar halten. Labels und Einheiten aus dem
  passenden Schema beziehen. Keine zusätzliche Kopie unter Website oder spatial.
- `src/pexl/schema/presets.py`: interner gemeinsamer Leser und Prüfung gegen das
  zugehörige Schema. Die aktive Auswahl an die vorhandene Schema-Version koppeln;
  keine zweite unabhängig gepflegte CURRENT-Version. Website, spatial und später
  Szenarioanwendung benutzen diesen Leser.
- `scripts/export_presets.py`: expliziter Export aus einer ausgewählten Excel-Datei,
  keine automatische Auslesung beliebiger DEV-Dateien beim Website-Build. Extraktion
  nach Inventur an vorhandene Excel-/Schema-Hilfen anbinden. Keine zweite Extraktion
  im Notebook. Formelwerte nur aus zuverlässig berechnetem und gespeichertem Stand.
- `scripts/preset_catalog.py`: erzeugt Quarto-Fragmente aus zentralem Katalog und
  redaktionellen Erläuterungen; Such-/Aufklappgestaltung von output_catalog wiederverwenden.
- `website/preset-catalog.qmd`: neue öffentliche Referenz unter Nachschlagen.
  `website/presets.qmd` bleibt die bestehende Bedienanleitung unter Starten.
- `website/_preset-notes.yml`: ausschließlich redaktionelle Hinweise pro bestätigtem
  Presetschlüssel: geeignete Situation, Erklärung, Grenzen, Themenzuordnung. Keine
  Zahlenwerte oder separat gepflegten Einheiten. Quelle für Katalogtexte und aufklappbare
  Hilfen auf HVAC-/PV-/Nutzungsseiten. Bereits geeignete Excel-Beschreibungen übernehmen,
  nur fehlende didaktische Texte hier ergänzen.
- `notebooks/howto_preset_catalog.ipynb`: ausführbarer Nachweis von Export, Prüfung,
  Katalogerzeugung und gemeinsamer Nutzung; später um Szenarioanwendung erweitern.

Der bestehende `spatial/data/hvac_presets.json` wird nach einem Werteabgleich abgelöst;
die grafischen Rezepte in `spatial/presets.py` bleiben dort und lesen zentral.
Die vorhandene Schema-Codegenerierung muss für den ersten JSON-Katalog keine neue
öffentliche Rückgabestruktur erhalten. Gemeinsame Export-Orchestrierung erst bei Bedarf.

Zusatzaufwand begrenzen und begründen:

- Versioniertes JSON ersetzt den fachlich zu eng abgelegten HVAC-Snapshot und ermöglicht
  Nutzung ohne Excel. Export/Update erfolgen bewusst pro Toolstand; freigegebene Stände
  bleiben unverändert. Tests prüfen reale Werte, fehlende Werte versus null sowie die
  Schema-Zuordnung und den Übergang der HVAC-Verbraucher. Paketierung der JSON-Dateien
  beim Python-Build mitprüfen.
- Redaktionelle YAML-Datei vermeidet mehrfach gepflegte Empfehlungen auf Fachseiten.
  Pflege nur bei geänderten Erklärungen oder Presets; verwaiste Schlüssel beim Build
  melden. Sie ist keine zweite fachliche Wertequelle und benötigt keine eigene Version.
- Website-Fragmente sind reine Build-Ergebnisse. Der vorhandenen Include-Konvention
  folgen; keine zusätzliche persistierte Website-Datenbank oder JSON-Wertekopie.

Öffentliche Darstellung: nur aktueller Stand unter `preset-catalog.html`, mit Toolversion
und DEV-/Release-Status. Kategorien durchsuchen, Presets aufklappen, Werte/Einheiten und
Quelle einsehen sowie zu IN-Definitionen springen. Stabile Presetanker für Hypothesis;
vor Änderungen kommentierten Stand im Redaktionsprotokoll sichern. Historische Nachweise
im Repository, keine öffentliche Versionsauswahl. Beim Release erneut aus der finalen
Excel exportieren und prüfen, erst dann Website und Download auf denselben Stand setzen.

## Freigegebene reduzierte Website-Ausbaustufe

Nur ein explizit ausgewählter JSON-Snapshot in schema/generated; Website-Erzeugung und lesender Export im bestehenden scripts/output_catalog.py. Kein schema/presets.py, keine zusätzliche CLI, keine Szenarioanwendung und keine HVAC-Migration. Namen gelten innerhalb des Snapshots, nicht als unveränderliche IDs. Quellpfad tatsächlich data/exports/schemas/schema_1.13.1_dev.xlsx. Metadaten aus dessen IN-Blatt werden mit exportiert, damit ein späterer Wechsel von current.py die Snapshotanzeige nicht verändert.

Redaktionelle Gruppentexte in website/_preset-notes.yml, daraus Katalog und Fachseitenhilfen. JSON erlaubt Build ohne Excel; generierte QMD-Fragmente unter assets sind wegwerfbar. Pflege: bewusster Neu-Export, Vergleich und Prüfung von Namen/Links/Notizen. Neuer oder fehlender Tabellenname bricht den Build zur redaktionellen Klärung ab. Ausführbare Abnahme: notebooks/howto_preset_catalog.ipynb.
