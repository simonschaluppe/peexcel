# Vorbereitung: vollständige elektrische Stundenbilanzen

Stand 15.10.2026. Die Website zeigt Aspern F7 mit den vorhandenen Teilflüssen.
Die drei Sanierungsvarianten dienen dem Jahresvergleich. Eine vollständige
Stundenbilanz wird erst nach Prüfung und Ergänzung des Exports implementiert.

## Geprüfter Exportbestand

| Bestand | Aspern F7 | Drei Bsp_San_6G-Exporte |
|---|---|---|
| Zeitraster | 8.760 fortlaufende Stunden, 2018 | jeweils identisch |
| SIM2-Spalten einschließlich Zeitangaben | 15 | 30 |
| PV-Ertrag, direkte/flexible Nutzung, Einspeisung | vorhanden | vorhanden |
| Konventioneller Netzbezug und drei Teilaggregate | vorhanden | vorhanden |
| Nutzerstrom, Lüftung, Heizung, Kühlung, Warmwasser, EV-Mindestbedarf | fehlen | vorhanden |
| Sechs flexible elektrische HKLS-Aufwendungen | fehlen | vorhanden |
| `VRGrid_total_min_use`, `VRGrid_total_flex_use` | fehlen | fehlen |
| `VRGrid_to_Eev_flex` | fehlt | vorhanden |
| Batterieladung/-entladung, Vehicle-to-Building | fehlen | fehlen |

Der reproduzierbare Kanalbestand wird von `flow_inventory` in
`scripts/website_examples.py` erzeugt und im Strombilanz-How-to für alle vier
Quellen ausgegeben. Die Website veröffentlicht dazu CSV-Dateien. Nicht exportiert
und exportiert mit ausschließlich Nullwerten bleiben getrennte Zustände.

Im Flex-Export ist `PV_total_flex_use` null, während flexible HKLS-Aufwendungen
und `VRGrid_to_Eev_flex` auftreten. Letzterer ist in 1.539 Stunden ungleich null.
Eine Beschränkung auf PV-Flexibilität würde damit relevante Flüsse auslassen.
`E_grid` summiert laut SIM-Schema ausschließlich `Grid_to_user`,
`Grid_to_HVAC_min` und `Grid_to_Eev_min`; signalgesteuerter Bezug ist darin
nicht enthalten. Aus diesen Exporten lässt sich daher keine vollständige
elektrische Quartiersbilanz belegen.

## Nächster Umsetzungsschritt: Export und Bilanzgrenze

1. SIM-Formeln und tatsächliche Exportauswahl gemeinsam prüfen. Für jeden Kanal
   Quelle, Ziel, Einheit, Flächenbezug, Vorzeichen und Aggregationsbeziehung aus
   dem bestehenden Schema dokumentieren. Einheitenlose Aggregate dürfen erst
   nach Prüfung ihrer Komponenten eine Einheit übernehmen.
2. Für F7 die vorhandenen Verbraucherkanäle des Bsp-Exports übernehmen:
   `E_plugAuxLight`, `Ev_min`, `Eh_min`, `Ec_min`, `Edhw_min`, `Eev_min` sowie
   die sechs finalen flexiblen HKLS-Aufwendungen. EV-Mindestbedarf, flexible
   Ladung und externe Ladung bleiben fachlich getrennt.
3. Den vollständigen signalgesteuerten Bezug über `VRGrid_total_min_use` und
   `VRGrid_total_flex_use` ergänzen. Detailkanäle für Quellenzuordnung optional
   exportieren; Aggregate und enthaltene Teilflüsse niemals gemeinsam summieren.
4. Für aktivierte Batterie-/V2B-Systeme mindestens `PV_to_Batt`,
   `VRGrid_to_Batt`, `Batt_to_user`, `Batt_to_HVAC_min`, `Batt_to_Eev_min`,
   `Eev_to_user` und `Eev_to_HVAC` exportieren. Für Speicherprüfungen zusätzlich
   Ladezustände, Lade-/Entladeenergien und Verluste mit konsistenter Systemgrenze
   aufnehmen. `Batt_total_charge` enthält bereits den Ladewirkungsgrad,
   `Batt_total_discharge` den Entladewirkungsgrad; busseitige und speicherseitige
   Größen dürfen nicht verwechselt werden. V2B-Kanäle sind im Schema negativ
   definiert und erfordern eine explizite Richtungsnormalisierung.
5. Mit vollständigem Export getrennte Prüfgleichungen für PV-Verwendung,
   elektrische Versorgung der Verbraucher und Speicher aufstellen. Eine
   Differenz dient der Diagnose und wird niemals als unbekannter Realfluss
   in die Darstellung eingefügt. Jahresabgleiche nur bei identischem Bezug und
   gleicher Bilanzgrenze; Toleranzen aus Exportpräzision und Größenordnung ableiten.

## Erweiterung der vorhandenen Darstellungen

- `Scenario.timeseries`, `add_season`, `electricity_balance` und
  `electricity_balance_facets` bleiben die Grundlage. Vorzeichen werden vor dem
  Renderer validiert, da dessen Betragsbildung eine falsche Zuordnung verdecken
  könnte. Fehlende erforderliche Kanäle führen zu einer klaren Fehlermeldung.
- PV-Verwendung, Verbrauchsdeckung und Speicherbetrieb als getrennte Ansichten
  derselben Stundenwerte anbieten. Vollständigkeit je Ansicht prüfen, nicht
  pauschal für eine gesamte Datei behaupten. Physische Energie und methodische
  Primärenergie-/THG-Bewertung nicht auf derselben Achse vermischen.
- Saisonprofile zeigen mittlere Leistung, Wochenansichten tatsächliche Stunden,
  Monatsansichten summierte Energie. Wh/m² durch die explizite Stundenlänge
  teilen; andere Zeitraster nicht stillschweigend als Stundenwerte behandeln.
- Für kleine Bildschirme saisonale Facetten wählbar oder in mehreren Zeilen
  darstellen. Erst bestehende Subplot-Möglichkeiten nutzen. Falls ein optionaler
  Layoutparameter erforderlich ist, bisherigen Default unverändert erhalten.
  Nutzen: lesbare Achsen und Legenden ohne eine zweite Plotfamilie. Pflege:
  Regressionstest für Default, gemeinsame Skalen und neue Anordnung.
- Abnahme mit einem vollständigen Referenzexport: stündlicher Bilanzschluss,
  Jahressummen, Speicherverluste, negative V2B-Richtung, Nullkanäle, fehlende
  Kanäle, Zoom und Legendenauswahl; Desktop und Mobilansicht visuell prüfen.

Keine neue persistierte Zeitreihenstruktur und kein separates Schema vorgesehen.
Ein etwaiger Auswahlparameter gehört zur vorhandenen Plot-Schnittstelle und
wird erst im konkreten Implementierungsvorschlag begründet. Kanalinventare sind
reproduzierbare Diagnoseartefakte, keine zweite Quelle für Schemainformationen.
Das ausführbare `notebooks/howto_analyze_electricity_balance.ipynb` dokumentiert
bereits Import, Prüfung, F7-Profile und Kanalinventar; es wird im nächsten Schritt
um dieselben Validierungs- und Darstellungsfunktionen wie die Website ergänzt.
