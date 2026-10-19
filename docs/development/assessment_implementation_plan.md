# Bewertungs-Tutorial: geprüfter Umsetzungsplan

Stand: 19.10.2026. Etappe 1 wurde lokal per Fast-forward in `master`
übernommen (`2ac54d2`). Kein Push, keine Veröffentlichung.

## Datenprüfung vor Etappe 2

Quelle: `data/exports/Klimsta_Abschlussprojekt_Varianten_V3.xlsx`.
Die Prüfung liest den Export; sie führt keine Excel-Simulation aus.

- Blätter: IN (789 Datenzeilen), OUT (563), PV-Import (8.760), Wetter
  (8.760). PV und Wetter sind Eingangszeitreihen, keine vollständigen
  stündlichen Simulationsergebnisse.
- 26 benannte Varianten: Forsthausgasse und 25 Gebäude-/Baualtersvarianten.
  Daneben liegt eine Spalte `Default` vor, die im Tutorial nicht als
  eigenständige Planungsvariante verwendet werden soll.
- Exportierte Toolversion: `1.13.1-dev`; aktives Python-Schema:
  `1_13_1_dev`. Ähnliche Versionsbezeichnung bedeutet hier noch keine
  vollständige Schemakompatibilität.
- `read_project()` scheitert im strengen Modus an unbekannten Variablen.
  IN: `preset_recorded_PV_system`, `preset_recorded_dhw_demand`,
  `preset_recorded_declaration_type`. OUT: `Edhw_th`, `Edhw_1_th`,
  `Edhw_2_th`.
- Ein ausschließlich diagnostischer Import mit `unknown="ignore"` ergibt
  29 Objekte: neben Default und den 26 Varianten werden die OUT-Metadaten
  `color` und `pattern` als Szenarien interpretiert. 52 Namenswarnungen
  betreffen Abweichungen zwischen Spaltenidentität und gespeicherten
  Projekt-/Szenarionamen. Die Originalspaltennamen bleiben maßgeblich.

## Fachliche Befunde

### Primärenergie

Der bestehende Report `primary_energy_balance` stellt Bedarf und Deckung
mit Beträgen dar. Seine Säulendifferenz stimmt bei 13 der 26 benannten
Varianten nicht mit dem exportierten `PEI_balance` überein.

Beispiel: `Geschoßwohnbau 6-Stöckig (Baujahr ab 2020)`:

| Größe | Wert | Fundstelle |
|---|---:|---|
| Differenz der derzeit dargestellten Säulen | +14,093141 kWhPEges./m²NGFa | Diagnose aus Reportserien wie im Renderer |
| Exportierte PE-Bilanz | −8,713075 kWhPEges./m²NGFa | OUT!AN248 |
| Positiver Dichtebeitrag | 22,620319 kWhPEges./m²NGFa | OUT!AN242 |
| Speicherverluste | 0,185897 kWhPEges./m²NGFa | OUT!AN241 |

Die Speicherverluste fehlen in der aktuellen Reportdefinition. Bei diesem
Beispiel entspricht die übrige Differenz dem positiven Dichtebeitrag.
Das erklärt die numerische Abweichung, belegt aber noch nicht, welche
Bewertungsregel im ursprünglichen Excel-Modell beabsichtigt war.
Keine automatische Korrektur des Exports oder der fachlichen Formeln.

Alle 26 exportierten PE-Salden sind negativ (rund −312,780 bis −8,713).
Ein realer positiver Deckungsüberschuss lässt sich mit diesen exportierten
Salden nicht demonstrieren. Grüne Delta-Markierungen können später mit
ausdrücklich synthetischen Renderer-Tests geprüft werden; solche Testwerte
werden nicht als Projektergebnisse im Tutorial verwendet.

### Lebenszyklus-THG

- `gwp_ee` umfasst bauliche und betriebliche Beiträge einschließlich
  Mobilität, negativer Beiträge und `GWP_lc_total`. Bei allen 26 benannten
  Varianten stimmt die Komponentensumme mit dem exportierten Gesamtwert
  innerhalb numerischer Toleranz überein. Dieser Report eignet sich
  grundsätzlich für die Gesamtbilanz, trotz seines verkürzten Namens.
- `gwp_ee_detail` enthält nur graue Emissionen und ist eine Ergänzung,
  kein Ersatz für die Quartiersgesamtbilanz.
- `district_gwp_ee` hat im aktiven Schema keine Serien und ist nicht nutzbar.
- Der Export enthält `GHG_LCA_timeframe_years = 26`, beispielsweise
  IN!AM696. Die Report-/Schema-Beschriftungen nennen dagegen 2025–2075.
  Der tatsächliche Berechnungszeitraum muss geklärt werden, bevor der
  Referenzwert 320 kg CO₂e/m² BGF als belastbarer Budgetvergleich gilt.
- Die Einheitenmetadaten von `gwp_ee` sind nicht einheitlich; `materialize`
  liefert deshalb `unit=None`. Die feste Achsenbeschriftung des Renderers
  darf die ungeklärte Zeitbasis nicht verdecken.

## Nächste Umsetzung nach fachlicher Klärung

1. **Import absichern.** `color` und `pattern` in der vorhandenen
   OUT-Metadatenerkennung berücksichtigen; gezielter Regressionstest.
   Die sechs zusätzlichen Variablen anhand eines maßgeblichen Schemas
   zuordnen oder für das Tutorial explizit als nicht verwendete Zusatzfelder
   prüfen. Kein pauschales, undokumentiertes Ignorieren unbekannter Felder.
   Keine neue öffentliche Import-Signatur nötig. `Default` wird über die
   bestehende Szenarioauswahl ausgeschlossen, nicht global umgedeutet.
2. **Bilanzbasis bestätigen.** PE-Komponenten einschließlich Speicherverlusten
   mit dem maßgeblichen Export abstimmen; Dichtebeitrag nicht erraten.
   THG-Zeitraum und Budgetbezug bestätigen. Falls nötig einen konsistenten
   Export aus der ursprünglichen Excel-Arbeitsmappe verwenden.
3. **`notebooks/howto_assess.ipynb` erstellen.** Deutsche Erläuterungen,
   vollständiger Variantenbestand, transparente Beispielauswahl, Import-
   und Summenprüfungen, Interpretation sowie Export. Unterschiedliche
   Gebäudetypen/Baualtersklassen nicht als isolierte Maßnahmenwirkung
   interpretieren. Bestehende `read_project`, `chart_names`, `materialize`
   und `plotly.render` verwenden. Fehlende Werte nicht als Null darstellen.
4. **Optionale Plot-Erweiterungen vorschlagen und freigeben.** In
   `pexl.plot.plotly.render` deaktivierte Schlüsselwortoptionen für PE-Delta
   und THG-Budgetlinie ergänzen. Bestehende Aufrufe behalten ihr Verhalten.
   Delta zwischen den Säulen, Vorzeichen, Einheit und Rot/Grün; Budgetlinie
   mit lesbarer Beschriftung und bestehenden L1–L3-Bändern. Ungültige oder
   widersprüchliche Bilanzdaten müssen vor der Darstellung auffallen.
5. **Beide Diagramme rendern und zur fachlichen/visuellen Freigabe zeigen.**
   Tests für positive/negative/Null-Deltas, negative THG-Beiträge,
   Summenabgleich und unveränderte Standarddarstellungen. Notebook vollständig
   ausführen; HTML und SVG mit den vorhandenen Exportfunktionen prüfen.
6. **Erst danach Website und Wiederverwendung integrieren.** Eigene Tutorial-
   Seite, sichtbare vorberechnete Plotly-Grafiken, Notebook-Download und
   Szenarioexport. Keine Änderungen an `peq-higrube` oder
   `siedlungs-check-poc`. Commit, Push und Veröffentlichung bleiben eigene
   Freigabepunkte.

## Schnittstellen und Pflegeaufwand

Die vorgeschlagenen optionalen Renderer-Parameter vermeiden eine zweite
Plotimplementierung in Notebook oder Website. Vorhandene Reportdictionaries,
DataFrames und Plotly-Figuren bleiben die Datenstrukturen. Pflegeaufwand:
Parameterprüfung, kurze Dokumentation und Regressionstests; Standardaufrufe
bleiben kompatibel. Die genaue Signatur wird vor Änderung freigegeben.

Ein Szenariomanifest ist erst für die spätere Website-/PoC-Integration
vorgesehen. Nutzen: Varianten, Dateien, Einheiten und Herkunft auffindbar
machen, ohne jede Plotly-Datei einzulesen. Die Metadaten einer einzelnen
Figur ersetzen dieses Verzeichnis nicht. Es soll vollständig aus denselben
Exporten neu erzeugt werden, ohne manuelle zweite Datenpflege. Felder,
Kompatibilitätsregeln und Prüfungen werden vor Einführung festgelegt.
Für die aktuelle Datenprüfung wird kein neues persistiertes Datenmodell
eingeführt.

## Erforderliche Entscheidungen

- Welcher PE-Stand ist maßgeblich, und wie soll der positive Dichtebeitrag
  im gelieferten Export tatsächlich angerechnet werden? Ein konsistenter
  neuer Export wäre der bevorzugte Nachweis; keine stillschweigende
  Anpassung des Python-Ergebnisses an einen Wunschsaldo.
- Welcher THG-Betrachtungszeitraum wurde tatsächlich berechnet, und gilt
  dafür das vorgegebene Budget von 320 kg CO₂e/m² BGF?
- Die im Arbeitsauftrag erwähnten zwei Referenzabbildungen liegen dieser
  Unterhaltung nicht als Bilder vor. Für eine genaue visuelle Angleichung
  werden sie benötigt; die beschriebenen Darstellungsanforderungen sind
  unabhängig davon bekannt.
