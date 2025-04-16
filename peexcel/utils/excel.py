import logging
from numpy import NaN
import pandas as pd
import json
from copy import deepcopy
from typing import Optional, List, Dict

logging.basicConfig(level=logging.INFO)
# Migrate PEExcel


def convert(o):
    if isinstance(o, pd.Timestamp):
        return o.isoformat()
    elif hasattr(o, "isoformat"):
        return o.isoformat()
    return str(o)


def parsesheet_in(df) -> dict:
    inputs = {}
    in_header = [
        "Icon",
        "Name",
        "Einheit",
        "Kommentar",
        "Type",
        "var_name",
        "ka",
        "Formel",
    ]
    in_scenarios = [c for c in df.columns if c not in in_header]

    if missing_headers := [col for col in in_header if col not in df.columns]:
        logging.warning(f"Missing columns in OUT sheet: {missing_headers}")

    for _, row in df.iterrows():
        key = row["var_name"] if pd.notna(row.get("var_name")) else row.get("Name")
        if pd.isna(key) or key is NaN:
            continue  # Skip unnamed rows
        inputs[key] = {field: row[field] for field in in_header if field in df.columns}
        inputs[key]["values"] = {scenario: row[scenario] for scenario in in_scenarios}

    return inputs


def parsesheet_out(df) -> dict:
    outputs = {}
    out_header = [
        "ID",
        "Kategorie",
        "Type",
        "Name",
        "Icon",
        "Bereich",
        "var_cat",
        "var_name",
        "Einheit",
        "Formel",
        "Label",
        "Kommentar",
    ]
    out_scenarios = [c for c in df.columns if c not in out_header]

    if missing_headers := [col for col in out_header if col not in df.columns]:
        logging.warning(f"Missing columns in IN sheet: {missing_headers}")

    for _, row in df.iterrows():
        key = row.get("var_name", None)
        if not key:
            continue  # Skip  rows without varname
        outputs[key] = {
            field: row[field] for field in out_header if field in df.columns
        }
        outputs[key]["values"] = {scenario: row[scenario] for scenario in out_scenarios}

    return outputs


class Scenario:
    def __init__(self, name: str, project: "Project"):
        self.name = name
        self.project = project

    def get_input(self, var_name: str, default=None):
        if var_name in self.project.inputs:
            return self.project.inputs[var_name]["values"].get(self.name)
        raise KeyError(f"Variable '{var_name}' not found in inputs.")

    def set_input(self, var_name: str, value):
        if var_name in self.project.inputs:
            self.project.inputs[var_name]["values"][self.name] = value
        else:
            raise KeyError(f"Variable '{var_name}' not found in inputs.")

    def get_output(self, var_name: str):
        if var_name in self.project.outputs:
            return self.project.outputs[var_name]["values"].get(self.name)
        raise KeyError(f"Variable '{var_name}' not found in outputs.")

    def has_inputs(self):
        return any(self.name in v["values"] for v in self.project.inputs.values())

    def has_outputs(self):
        return any(self.name in v["values"] for v in self.project.outputs.values())

    def as_dict(self) -> dict:
        return {
            "name": self.name,
            "inputs": {
                k: v["values"].get(self.name)
                for k, v in self.project.inputs.items()
                if self.name in v["values"]
            },
            "outputs": {
                k: v["values"].get(self.name)
                for k, v in self.project.outputs.items()
                if self.name in v["values"]
            },
        }

    def __repr__(self):
        return f"<Scenario('{self.name}') of Project('{self.project.file_source}')>"


class Project:
    """
    Represents a PEExcel project based on an Excel file with structured input/output handling
    and optional scenario management.

    This class acts as a wrapper for Excel files used in the PEExcel framework, which typically
    contain multiple sheets (e.g., 'IN', 'OUT', and optionally 'PV', 'Signals', 'SIM2') representing
    model inputs, outputs, and intermediate results. The class parses and organizes the content of
    these sheets into accessible Python dictionaries and provides utility methods for interacting with
    scenario-based (column) data.

    Parameters
    ----------
    xls_project_path : str
        Path to the Excel file representing the PEExcel project.

    Attributes
    ----------
    file_source : str
        Path to the Excel source file.
    df_in : pandas.DataFrame or None
        Parsed raw content of the 'IN' sheet as a DataFrame, if available.
    df_out : pandas.DataFrame or None
        Parsed raw content of the 'OUT' sheet as a DataFrame, if available.
    inputs : dict or None
        Parsed input variables with metadata and scenario-based values.
    outputs : dict or None
        Parsed output variables with metadata and scenario-based values.
    current_scenario : str or None
        Currently selected scenario, defaulting to the first available scenario.

    Methods
    -------
    taxonomy()
        Returns a dictionary containing all parsed inputs and outputs.
    all_variables()
        Returns a dictionary with fully qualified variable names (e.g. 'IN:var_name').
    scenarios
        Property returning a list of all available scenarios.
    scenario(name=None)
        Returns input values for a specific scenario.
    get(var_name, scenario=None)
        Returns the value of a variable for the given scenario.
    to_json(filepath, section="all")
        Saves project data to a JSON file. Sections: 'inputs', 'outputs', or 'all'.
    variable_description(var_name)
        (Placeholder) Intended to return detailed metadata for a variable.

    Key Features
    ------------
    - Parses 'IN' and 'OUT' sheets (if available) into structured dictionaries with metadata and values.
    - Supports multi-scenario data stored across columns within the sheets.
    - Provides access to variable values per scenario(column).
    - Automatically identifies available scenarios from the 'IN' sheet.
    - Offers methods to export or transform the project data into JSON or DataFrame formats (planned).

    Example
    -------
    >>> project = Project("path/to/Export.xlsx")
    >>> project.scenarios
    ['base', 'scenario1', 'scenario2']
    >>> project.get("NFA_total", scenario="scenario1")
    12450.0
    >>> project.taxonomy()
    {'inputs': {...}, 'outputs': {...}}

    Notes
    -----
    - Missing sheets ('IN' or 'OUT') are handled with warnings.
    - Assumes all scenarios are defined as columns beyond a fixed set of metadata headers.
    """

    def __init__(self, xls_project_path: str):
        self.file_source = xls_project_path

        try:
            self.df_in = pd.read_excel(xls_project_path, sheet_name="IN")
            self.inputs = parsesheet_in(self.df_in)
        except ValueError:
            logging.warning(f"'IN' sheet not found in {xls_project_path}")
            self.df_in = None
            self.inputs = {}

        try:
            self.df_out = pd.read_excel(xls_project_path, sheet_name="OUT")
            self.outputs = parsesheet_out(self.df_out)
        except ValueError:
            logging.warning(f"'OUT' sheet not found in {xls_project_path}")
            self.df_out = None
            self.outputs = {}

        in_scenarios = set()
        for v in self.inputs.values():
            in_scenarios.update(v["values"].keys())

        out_scenarios = set()
        for v in self.outputs.values():
            out_scenarios.update(v["values"].keys())

        all_scenario_names = sorted(in_scenarios.union(out_scenarios))

        self.scenarios: Dict[str, Scenario] = {
            name: Scenario(name, self) for name in all_scenario_names
        }

    # TODO: scenario in - out matching - whats available?

    # TODO: return should just be dataframes
    # project should be able to get a dict repr
    # project should be able to get a json repr
    # project should be able to get a df repr

    # TODO: should be able to write a project
    #       - OUT results?

    def taxonomy(self) -> dict:
        # return dict
        return {"inputs": self.inputs, "outputs": self.outputs}

    def all_variables(self) -> dict:
        """
        Returns a dictionary with keys like 'IN:var', 'SIM2:var', 'OUT:var'
        for unique scoping of variable references.
        """
        all_vars = {}
        for k in self.inputs:
            all_vars[f"IN:{k}"] = self.inputs[k]
        for k in self.outputs:
            all_vars[f"OUT:{k}"] = self.outputs[k]
        return all_vars

    def get_scenario(self, name: str) -> Scenario:
        return self.scenarios[name]

    def to_json(self, filepath: str, section: str = "all"):
        """
        Dumps the parsed project data to a JSON file.

        Parameters:
        -----------
        filepath : str
            The path where the JSON file will be saved.
        section : str
            Which section to export: 'inputs', 'outputs', or 'all'.

        Raises:
        -------
        ValueError:
            If the section argument is invalid.
        """
        if section == "inputs":
            data = self.inputs
        elif section == "outputs":
            data = self.outputs
        elif section == "all":
            data = self.taxonomy()
        else:
            raise ValueError("Section must be 'inputs', 'outputs', or 'all'.")

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=convert)

    def __repr__(self):
        return (
            f"<Project('{self.file_source}') | "
            f"{len(self.inputs)} inputs, {len(self.outputs)} outputs | "
            f"Scenarios: {list(self.scenarios.keys())}>"
        )

    ## read a project
    # hold the json as dataclass?

    # game app needs to come here, get a project
    # and build a district out of it#
    # projectattributes need to findable
    # project is not responsible for ensuring compatability?

    # project will also be used for other tasks
    # formula annotation
    # visualization of calculatio graph, network
    # potentially interactive?

    # should it automatically be like the excel?
    # yes, that means dynamic


if __name__ == "__main__":
    """ import sys
    print(sys.executable)
    #sys.path.append("../")
    print([p for p in sys.path])"""

    import os
    from pathlib import Path
    print(os.getcwd())
    path = Path(os.getcwd()) /  "peexcel\peexcel\Project_Export.xlsx"

    print( path)

    xlp = Project(path)
    # print(xlp)
    # names = nameslist(xw.Book("test_PlusenergieExcel_Performance.xlsx"))
    # excel_paths = [
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Aichinger_211105.xlsb",
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_AmBichl_211105.xlsb",
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Glan_211105.xlsb",
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Gneis_211105.xlsb",
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Graz_211105.xlsb",
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Pilzgasse_211105.xlsb",
    # ]

    # paths = [Path(ep) for ep in excel_paths]

    # aggregation_excel_path = Path(
    #     r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\Quartiersvergleich211108.xlsm"
    # )
    # aggregation_sheet = "PEExcel Import"

    # for path in paths:
    #     append_variations_to_aggregation_sheet(
    #         peexcel_path=path,
    #         agg_book_path=aggregation_excel_path,
    #         agg_sheet_name=aggregation_sheet,
    #         close_peexcel=True,
    #     )
