<img src="https://github.com/simonschaluppe/peexcel/assets/22156735/2856e7d9-54d9-4ea9-a894-1128f435c139" height="300">

# PEExcel – klimaaktiv Nachweistool für Plus-Energie-Quartiere

PEExcel ist ein Excel-basiertes Nachweistool für die klimaaktiv Deklaration **„Plus-Energie-Quartiere“**.  
Es unterstützt die Bewertung und Deklaration von Quartieren auf Basis stündlicher Energiebilanzen, erneuerbarer Energieerzeugung, Mobilität, grauer Emissionen und Flexibilitätsmaßnahmen.

Das Tool wurde von der Forschungsgruppe **[Climate-fit Buildings and Districts](https://www.technikum-wien.at/forschungsschwerpunkt-renewable-energy-systems/)** der  an der [Fachhochschule Technikum Wien](https://www.technikum-wien.at/) im Rahmen der Entwicklung des klimaaktiv Qualitätsstandards für Plus-Energie-Quartiere erarbeitet.

## 🎯 Wofür ist PEExcel gedacht?

PEExcel dient der strukturierten Modellierung, Bewertung und Dokumentation von Quartiersprojekten im Sinne des klimaaktiv Standards **Plus-Energie-Quartiere**. 

Das Tool unterstützt insbesondere:

- die energetische und THG-Bewertung von Quartiersvarianten
- die Vorbereitung von Planungsdeklarationen
- die Qualitätssicherung im Planungsprozess
- die nachvollziehbare Dokumentation zentraler Eingaben und Ergebnisse
- den Vergleich von Szenarien und Maßnahmenpaketen

## 👥 Zielgruppen

PEExcel richtet sich an:

- klimaaktiv PEQ Kompetenzpartner:innen
- Energie- und Gebäudeexpert:innen
- Planer:innen und Konsulent:innen
- Forschungseinrichtungen und Ausbildung

## Bewertungsrahmen

Das Tool bildet die drei Qualitätsstufen des [klimaaktiv Standards für Plus-Energie-Quartiere](https://www.klimaaktiv.at/publikationen/plus-energie-quartiere) ab:

1. **Plus-Energie-Quartier**  
   Bewertung der Betriebsenergie von Gebäuden und quartiersbezogener Energieversorgung.

2. **Plus-Energie-Quartier mit Mobilität**  
   Ergänzung der Bilanz um den Energiebedarf des motorisierten Individualverkehrs.

3. **Klimaneutrales Plus-Energie-Quartier**  
   Erweiterung um Lebenszyklus-Treibhausgasemissionen, insbesondere graue Emissionen der Gebäude.
<img width="1228" height="467" alt="image" src="https://github.com/user-attachments/assets/095a8e31-2daf-47f3-8174-8890566f9fb6" />

## ⚙️ Zentrale Funktionen

PEExcel umfasst unter anderem:

- stündliche Energiebilanzierung auf Quartiersebene
- Bewertung von Wärme, Kälte, Strom, Warmwasser, Lüftung und Hilfsenergie
- Abbildung von Photovoltaik, Eigenverbrauch und Einspeisung
- Berücksichtigung von Speichern und Flexibilitätsoptionen
- Integration standortbezogener Mobilitätsbewertung
- Bewertung grauer Emissionen über den Lebenszyklus
- Berücksichtigung von THG-Absenkpfaden des nationalen Energiesystems bis 2075
- Szenarien- und Variantenvergleich
- strukturierte Eingabe-, Ergebnis- und Exporttabellen
- deklarationsorientierte Ergebnisdarstellung
- Python-Paket `pexl` für automatisierten Datenimport/-export, Schema-Validierung, Ergebnisanalyse und Visualisierung

## 📥 Download

| Version | Status | Beschreibung | Link |
|---|---|---|---|
| v1.10 | Stable Release | Empfohlene Version für reguläre Anwendung und Tests | [🧰 Excel Tool (v1.10 Stable Release](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/excel/tool/ka_PEQ_Nachweistool.xlsb)  |
| v1.12.x | Development Version | Entwicklungsstand mit neuen Funktionen und laufenden Anpassungen | [🧰 Excel Tool (v1.12.7)](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/excel/development/ka_PEQ_Nachweistool_DEV.xlsb)  |

> Hinweis: PEExcel benötigt Microsoft Excel / Office 365 mit aktivierten Makros.  
> Nach dem Download muss die Datei gegebenenfalls in den Dateieigenschaften entsperrt werden, damit Makros ausgeführt werden können.

## 🚀 Schnellstart

1. Aktuelle Stable-Version herunterladen.
2. Datei lokal speichern.
3. Falls Windows die Datei blockiert: Rechtsklick auf die Datei → **Eigenschaften** → **Zulassen** / **Entsperren**.
4. Datei in Excel öffnen.
5. Makros aktivieren.
6. Mit dem Handbuch oder Quick-Start-Guide die erste Beispieldeklaration durchgehen.
   
## 🐍 Python-Schnittstelle

Neben der interaktiven Nutzung in Excel enthält das Repository auch das Python-Paket `pexl`. Es unterstützt automatisierte Workflows rund um PEExcel, etwa Import und Export von Daten, Validierung von Schemas, Analyse von Ergebnissen und Visualisierung.

Ein Einstieg ist im Notebook [`notebooks/howto_excel.ipynb`](notebooks/howto_excel.ipynb) dokumentiert. Dieses zeigt beispielhaft, wie PEExcel-Projekte aus Python heraus angesprochen werden kann.

## 📚 Dokumentation

| Dokument | Inhalt | Link |
|---|---|---|
| Handbuch zur Nachweisführung | Einstieg, Toolstruktur, zentrale Abläufe und Quick-Start | [📖 Handbuch herunterladen](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/docs/Handbuch%20zur%20Nachweisf%C3%BChrung.pdf)
| klimaaktiv Broschüre Plus-Energie-Quartiere | Überblick über Standard, Qualitätsstufen und Bewertungslogik | [📜Broschüre Klimaaktiv Plus-Energie-Standard](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/docs/Brosch%C3%BCre%20PEQ_klimaaktiv.pdf) |
| Hintergrundbericht | Methodische Grundlagen der PEQ-Definition und Operationalisierung | [📚 Hintergrund-Bericht PEQ Definition und Operationalisierung](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/docs/Leitfaden%20PEQ%20Definition%20und%20Operationalisierung_StandJuni2023.pdf)|
| Präsentation zum Nachweistool | Kurzüberblick über Aufbau und Anwendung | [💡Präsentation herunterladen](https://github.com/simonschaluppe/peexcel/raw/refs/heads/master/docs/klimaaktiv%20PEQ-Tool%20Dokumentation.pdf) |

## 🧮 Methodischer Überblick

PEExcel kombiniert mehrere Bewertungsbausteine zu einem deklarationsfähigen Quartiersmodell:

- Energiebedarf und Energieerzeugung im Gebäudebetrieb
- zeitlich aufgelöste Import- und Exportbilanz
- erneuerbare Energieerzeugung am Standort
- Mobilitätsenergie in Abhängigkeit von Standortqualität und Mobilitätskonzept
- graue Emissionen der Gebäude über den Lebenszyklus
- Kontextfaktoren wie Dichte, Bestand und Flexibilität

Die Bilanzierung erfolgt mit stündlicher Auflösung und erlaubt damit eine differenzierte Bewertung von Eigenverbrauch, Netzinteraktion, Speichern und zeitlicher Verfügbarkeit erneuerbarer Energie.

## 🗂️ Repository-Struktur

```text
peexcel/
├── excel/
│   ├── tool/              # aktuelle stabile Tool-Versionen
│   └── development/       # Entwicklungsversionen
├── src/
│   └── pexl/              # Python-Paket für Import, Export, Validierung, Analyse und Visualisierung
├── notebooks/             # How-to- und Analyse-Notebooks
│   ├── howto_excel.ipynb  # Beispiel: PEExcel aus Python ansteuern
│   ├── howto_schema.ipynb # Arbeit mit Export- und Eingabeschemata
│   └── validate.ipynb     # Validierung von Daten und Exporten
├── data/
│   ├── schemas/           # CSV- und Exportschemata
│   └── examples/          # Beispiel- und Testdaten
├── docs/                  # Dokumentation, Berichte und Präsentationen
├── tests/                 # Tests für Python-Komponenten
├── pyproject.toml         # Python-Projektkonfiguration
└── README.md
```

## 📝 Publikationen und Hintergrund

Die methodischen Grundlagen des Tools wurden im Rahmen mehrerer Forschungs- und Entwicklungsarbeiten zu Positive Energy Districts, klimaneutralen Quartieren und deklarationsfähigen Bewertungsmethoden erarbeitet.

Relevante Publikationen:
Ausgewählte Publikationen:

| Jahr | Publikation | Thema |
|---|---|---|
| 2023 | Schneider et al. – [A Quantitative Positive Energy District Definition with Contextual Targets](https://www.mdpi.com/2075-5309/13/5/1210) | PEQ-Definition und kontextbezogene Zielwerte je baulicher Dichte und Quartiersstandort |
| 2024 | Schneider et al. – [PEExcel: A Fast One-Stop-Shop Assessment and Simulation Framework for Positive Energy Districts](https://doi.org/10.26868/29761662.2024.11) | PEExcel-Framework und Anwendung |
| 2024 | Schneider et al. – [Can Urban Retrofitting Achieve a Positive Energy Balance?](https://doi.org/10.1109/i-COSTE63786.2024.11024809) | Fallstudien zu urbanem Bestand |
| 2025 | Bruckner et al. – [Lessons Learned from Four Real-Life Case Studies](https://doi.org/10.3390/en18030560) | Energiebilanzierung realer PED-Fallstudien |
| 2025 | Schneider & Baptista – [Annual Hourly E-Mobility Modelling and Assessment in Climate Neutral Positive Energy Districts](https://doi.org/10.1109/EEEIC/ICPSEurope64998.2025.11169136) | Stündliche E-Mobilitätsmodellierung im Quartier|
| 2025 | Schneider et al. – [Declaration-Ready Climate-Neutral PEDs](https://doi.org/10.3390/designs9060123) | Deklarationsfähige klimaneutrale PEQ-Bewertung mit Fallbeispielen |

Weitere Literatur, Hintergrundberichte und methodische Dokumente sind in der Dokumentation verlinkt.

## 📩 Newsletter

Aktuelle Informationen zu Tool-Updates, Veranstaltungen, Schulungen und Weiterentwicklungen der klimaaktiv Deklaration **„Plus-Energie-Quartiere“** erhalten Sie über den klimaaktiv PEQ Kompetenzpartner Newsletter.

 [zum Newsletter anmelden](https://flow.cleverreach.com/fl/e24548f3-b4ae-4851-a0c2-bff4d05092ef/)
 
## 💬 Kontakt
Simon Schneider
FH Technikum Wien  
Forschungsgruppe Climate-fit Buildings and Districts

Technische Fragen, Fehlerberichte und Verbesserungsvorschläge bitte über die
[GitHub Issues](../../issues) einbringen.

Für fachliche Fragen zur klimaaktiv Deklaration **„Plus-Energie-Quartiere“**
verweisen wir auf die offiziellen Kontaktstellen in der Dokumentation und auf
die Informationsangebote des klimaaktiv Programms.
  
## 📄 Lizenz und Nutzung

Bitte beachten Sie die im Repository angeführten Lizenz- und Nutzungshinweise.  
Bei Verwendung des Tools in Projekten, Publikationen oder Lehrveranstaltungen wird um entsprechende Quellenangabe gebeten.



![image](https://github.com/user-attachments/assets/696c5440-e451-46fd-823e-d94ec4e45ea5)



