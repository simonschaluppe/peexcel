# Deutsch
### Startpunkt: Plusenergie-Quartier Simulation mit Excel
Das PE-Excel wurde von der Forschungsgruppe [Nachhaltige Gebäude und Städte](https://res.technikum-wien.at/sbc/) an der Fachhochschule Technikum Wien entwickelt. Das ursprüngliche Ziel war es, eine effiziente und dennoch flexible Plattform für die Simulation von PEQs mit einer stündlichen Energiebilanzauflösung zu schaffen. Es kombiniert drei verschiedene Modelle und Simulationen zu einem umfassenden Bewertungsrahmen für die Leistung von PEQs. Die drei Hauptteile, die in diesem Rahmenwerk integriert sind, sind
* Stündliche PV-Simulationsergebnisse 
* LCA-Ergebnisse in bis zu 5 Varianten (manuell importiert vom eco2soft LCA-Rechner)  
* Stündliche Energiebilanz einschließlich ermittelter DSM-Strategien für den PV-Überschuss vor Ort und das Offsite-Wind-Peak-Shaving, die in TABS, DHW, Batterien und Ecars verwendet werden

![grafik](https://user-images.githubusercontent.com/80957185/112003855-9088d400-8b21-11eb-91b0-c3f231016cc3.png)

## Was sind die Vorteile?
Ausgehend von diesem wenig bekannten "Plusenergieexcel". Hat es einige große Vorzüge neben einigen sehr schmerzhaften Fehlern:
**Das Gute:**
* Dynamisch: Es hat eine stündliche Auflösung: Energiebilanz, Lastprofile, PV-Erzeugung, alles war für alle 8760 h des Jahres bekannt war konnte mit einem vernünftigen Algorithmus verwendet werden, der versuchte, den Eigenverbrauch, CO2-Emissionen usw. zu optimieren
* Voreinstellungen: Es sind bereits alle Voreinstellungen vorhanden: Steckdosen verschiedener Nutzungen (Wohnen, Büro, etc.), Wirkungsgrade der Umwandlungssysteme
* Einfach zu bedienen: Es ist ein fahrfertiges Auto: Alle Komponenten sind bereits ineinander verzahnt, man muss nur noch ein paar Grundflächen angeben und erhält sofort Ergebnisse
* Nachvollziehbar: Es ist ... relativ ... klar, wie die Simulation abläuft: jeder Zeitschritt eine Zeile, jede Berechnung eine Spalte
* Es ist ein One-Stop-Shop: Man hat alle notwendigen Eingabedaten, Simulationslogik, Ergebnisse und Visualisierungen übersichtlich in einer Datei
* leicht anpassbar und erweiterbar: Einfach ein paar Formeln draufklatschen
	
**Das Schlechte:**
* Keine Versionskontrolle: Jede Simulationseingabe und -ausgabe war eine einzige Datei. Neue Variante bedeutet -> neue Datei. Sobald Sie getrennte Dateien haben, haben Sie keine Möglichkeit zu wissen, welche Eingaben gleich sind und welche sich unterscheiden (außer durch Dateinamenprosa und Speicher, die beide nicht sehr gut kommunizierbar sind). An diesem Punkt müssen Sie darauf vertrauen, dass Sie (und Ihre Mitarbeiter) ab diesem Punkt keine Fehler mehr machen, oder Sie riskieren, eine Menge Arbeit zu verlieren
* Keine Eingabeprüfung: Es gibt im Grunde keine Möglichkeit, die Eingaben auf Fehler zu prüfen oder zu validieren, außer dass man jede einzelne Zelle überprüft, "nachschaut" und "plausibilisiert"
	
**Das Hässliche:**
* Unhandlich: Die Datei ist über 35 MB groß. Das ist nicht verschickbar. Das wird sehr schnell langweilig.
* Unstabil: Die Berechnung dauert sehr lange und ist instabil. Viele Laptops kommen mit den Anforderungen, all diese Daten im Speicher zu halten, nicht zurecht und stürzen ab... und lassen den Benutzer oft auch nicht richtig speichern. Dann viel Spaß beim Wiederherstellen Ihrer Arbeit und beim Überprüfen aller Änderungen, die Sie zuvor vorgenommen haben. Welche haben es geschafft und welche nicht. Können Sie sich an alle erinnern? 
* Nicht aktualisierbar: Das Ändern der Berechnung bedeutet das Ändern der gesamten Datei. Da Eingaben nicht ohne weiteres zwischen Dateien übertragbar sind, bedeutet dies, dass Sie nicht gegen andere Projekte prüfen können. Ich wiederhole: Sie können ältere Projekteingabedaten nicht mit neueren Dateien verwenden.
	
Die Hauptschmerzpunkte sind hier also:
1. Unhandliche Dateigröße, Abstürze.
2. Keine flexible Möglichkeit, Berechnung / Simulation / Algorithmus zu ändern
3. Keine einfache Möglichkeit zur Berechnung und Speicherung von Variationen
4. Aktualisierbarkeit

# English
### Starting Point: Positive Energy District Simulation with Excel
The PE-Excel has been developed by the research group [sustainable buildings and cities](https://res.technikum-wien.at/sbc/) at the University of Applied Science Vienna. The initial goal was to create a efficient yet flexible platform for simulating PEDs with an hourly energy balance resolution. It combines three different models and simulations into a comprehensive evaluation framework for the performance of PEDs. The three main parts integrated in this framework are
* Hourly PV Simulation Results 
* LCA results in up to 5 Variants (manually imported from eco2soft LCA calculator)  
* Hourly energy balance including determined DSM strategies for onsite PV excess and offsite Wind Peak Shaving used in TABS, DHW, Batteries and Ecars

![grafik](https://user-images.githubusercontent.com/80957185/112003855-9088d400-8b21-11eb-91b0-c3f231016cc3.png)

## What are the Benefits?
Starting from this infamous "Plusenergieexcel". It has some great merits alongside some very painful flaws:
**The Good:**
* Dynamic: It had hourly resolution: Energy balance, load profiles, PV generation, everything was known for each 8760 h of the year and could be used with a sensible algorithm trying to optimize for own consumption, CO2 emission, etc
* Defaults: It had all defaults already set up: Plugloads of different usages (residential, office, etc), efficiencies of conversion systems
* Easy to use: It was a car ready to drive: all components already interlocked, just give us some floor areas and we have results immediately
* Comprehensible: It was … relatively .. clear how the simulation was carried out: each timestep one row, each calculation one column
* It was a One-Stop-Shop: you had all your neccessary input data, simulation logic, results and visualisations neatly organized in one file
* easily customizeable and extendable: Just slap some formulas on
	
**The Bad:**
* No Version Control: each Simulation input and output was one single file. New variant means -> new file. Once you have separated files, you have no way of knowing which inputs are the same and which differ (except by filename prose and memory, which are both not very well communicatable). At this point you have to trust that you (and your collaborators) dont do any mistakes from this point onwards anymore or risk binning alot of work
* No Input-check: There is basically no way to check for errors or validate the inputs except checking every single cell, "glancing" and "plausibility"
	
**The Ugly:**
* Unwieldy: The file is upwards of 35 MB. That is not emailable. This gets old real fast.
* Unstable: The calculation takes a long time and is unstable. Many Laptops cant handle the requirements to keep all that data in memory and crash… often not letting the user save properly either. Then have fun restoring your work and checking for all the changes you made previously. Which ones made it and which didnt. Do you remember all of them? 
* Not updateable: Changing the calculation means changing the whole file. Since inputs are not readily transferrable between files, this means that you cannot check against other projects. I repeat: You cannot use older project input data with newer files.
	
So the main pain points here are:
1. Unwieldy filesize, crashes.
2. No flexible way to change calculation / simulation / algorithm
3. No easy way to calculate and store variations
4. Updateability
