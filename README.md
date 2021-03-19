# Plus-Energie-Quartier-Excel ("PE-Excel")
## Konzeptpapier 
### Starting Point: Positive Energy District Simulation with Excel
**History**
The PE-Excel has been developed by the research group [sustainable buildings and cities](https://res.technikum-wien.at/sbc/) at the University of Applied Science Vienna. The initial goal was to create a efficient yet flexible platform for simulating PEDs with an hourly energy balance resolution. It combines three different models and simulations into a comprehensive evaluation framework for the performance of PEDs. The three main parts integrated in this framework are
* Hourly PV Simulation Results 
* LCA results in up to 5 Variants (manually imported from eco2soft LCA calculator)  
* Hourly energy balance including determined DSM strategies for onsite PV excess and offsite Wind Peak Shaving used in TABS, DHW, Batteries and Ecars

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

 ### Solve Unwieldy filesize, crashes.
We have 2 areas of improvement here
1. Reduce File Size to improve Handling
2. Reduce Calculation and Update Time

**Reduce File Size to improve Handling**
Target range: <= 10 MB would be ideal  because emailable, but probably unfeasible
Initial size: 40-50 MB
Current Size 11/2020 (.xlsb): 25 MB

To reduce file size it is first neccessary to identify their main causes:
* Pictures, especially uncompressed: This is a tradeoff between the documentation and visualization pictures typcally provide. If compressed and used sparinggly, this shouldnt be an issue. 
* widespread formatting over entire columns and rows: Storing formatting requires much more space than just the formulas and values. use formatting primaarily to distinguish between different cell types: Different sorts of User Input, Calculations and Logic, Links, Default Values, etc. Some formatting information such as colors can be used to find cells of certain type for targetted testing, saving and loading. In any way, make sure to restrict formatting to used cells only. 
* long chains of formula logic: For Excel to carry out all calculations in a workbook it first needs to resolve all internal (and external) references between cells. To this end Excel creates a so called "calculation chain". This is basically a directed graph whose nodes are batches of independent thus parallel calculations connected by arrows of dependency. For large sets of calculations, this dependency chain can become so long that it amounts for a significant part of the file size: In the case of the PE-Excel the calculation chain initially amounted to upwards of 50% of space. Unfortunately this can only be addressed indirectly: Reduce lookups and references in general, most importantly between worksheets.   

### Enable Variations
Problem: No easy way to calculate and store variations
This is important because it 
* facilitates semi-automatic and automatic testing: Test-cases can be defined as fixed Variations of a base Variant
* reduces the number of Excel files required to store relevant input sets

### Flexibility to change calculation / simulation / algorithm
This is an important and rather complex topic.
First, there is a distinction between technical programmability and content of the simulation.

### Enable Updateability
There are now git systems that can log, diff and merge Excel files. I tried xltrails and it didnt work for the Workbooks of our size. 
In the current PE-Excel, you can save and load the content and address of all cells of a specifiable formatting set, namely their background colors. This has some obvious flaws but if the structure and positition of the inputs stays relatively constant and is backed with default values, this can be used to transfer project specific information between PE-Excels of different version.

# pyped  
## Concept for transitioning from Excel to Python

pyped stands for **python positive energy district** and is designed for the
following tasks:
1. Wrapping (quasi-)dynamic peb simulation methods
    * PE-Excel
        * Map xls variables to python datastructs
    * Casaclima excel?
    * Classes?
* Perform time series calculation
* flexible /optional sub-energy models. Sub-model agnostic?
* comprehensive model representation
    (eco, lca, comfort)
3. (Visual representation)
    * Plots
4. User interfaces
    * simtower
        * Modelling / Learning tool

Möglicherweise eigene Projekte, vielleicht hier als feature dabei:
* Meta-Wrapper? bzw API
    * city gml > all data (energy ADE)
    * cityJSON > same but less and less maintained. more lightweight and native
    * BIM / IFC > gibts sicher schon einiges, um die Therm. Hülle und HLKS zu bekommen
    * Open IFC vomBednar? Integral? wieh hat das geheißen?

* Git-style version control system for Variant Exploration and documentation

Ziele Was ist das Ziel von pyped
Zu 1. Mai
