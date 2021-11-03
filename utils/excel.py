import csv
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import xlwings as xw

logging.basicConfig(level=logging.INFO)
# Migrate PEExcel

## Old book
# TEST_PATH = Path("test_PlusenergieExcel_Performance.xlsx")
# TEST_SAVE_DIR = Path("test/")


def nameslist(book):
    result = list()
    for name in book.names:
        try:
            range = name.refers_to_range
            if range.size == 1:
                val = range.value
                formula = range.formula
            else:
                val = "#Range"
                formula = "#Range"

            cell = Cell(
                name=name.name,
                sheet=range.sheet.name,
                address=range.address,
                # refers_to_range=str(range),
                # refes_to=str(name.refers_to),
                value=val,
                formula=formula
            )
        except:
            # Except What?
            # some names have an error in their refers_to_range, when xlwings cannot resolve it.
            # that is all names pointing to an external file
            cell = Cell(name=name.name,
                        refers_to=str(name.refers_to),
                        broken=True,
                        value="#REF")
        result.append(cell)
    return result


@dataclass
class PEExcel:
    file: Path
    extraction_date: datetime = datetime.now()
    version: str = "0.0"
    _inputs: List = field(default_factory=list)
    _results: List = field(default_factory=list)
    _variations: List = field(default_factory=list)

    @property
    def results(self):
        return self._results

    @property
    def inputs(self):
        return self._inputs

    def info(self):
        return dict(
            file=self.file,
            date=self.extraction_date,
            version=self.version
        )

    @classmethod
    def parse(cls, path):
        logging.warn(path)
        book = xw.Book(path)
        return cls(file=path,
                   _inputs=single_names(book, starts_with="Userinput_").values(),
                   _results=single_names(book, starts_with="Ergebnis_").values(),
                   )

    def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=",", debug=True):
        """
        Parse a CSV file into a list of records
        """

        if select and not has_headers:
            raise RuntimeError(f"arguments select and has_headers can't both be true or false at the same time.")

        rows = csv.reader(lines, delimiter=delimiter)

        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(name) for name in select]
                headers = [headers[i] for i in indices]
        else:
            select = None

        records = []
        for i, row in enumerate(rows):
            if not row:
                continue

            if select:
                row = [row[i] for i in indices]
            if types:
                try:
                    row = [func(val) for func, val in zip(types, row)]
                except ValueError as e:
                    if debug:
                        logging.WARNING(f"Row {i}: ValueError parsing {row} - skipping row...")
                        logging.DEBUG(f"Row {i}: Type mismatch: {e}")
                    continue
            if has_headers:
                record = dict(zip(headers, row))
            else:
                record = tuple(row)
            records.append(record)

        return records


@dataclass
class Cell:
    value: 'typing.Any'
    name: str = ""
    formula: str = ""
    sheet: str = ""
    address: str = ""
    refers_to_range: str = ""
    refers_to: str = "",
    broken: bool = False

    def csv_line(self, delimiter=";"):
        str_vals = [str(v) for v in self.__dict__.values()]
        return delimiter.join(str_vals)

    @classmethod
    def csv_header(cls, delimiter=";"):
        return "value;name;formula;sheet;address;refers_to_range;refers_to"

@dataclass
class Variation:
    name: str


def single_names(book: xw.Book, starts_with: str = "") -> Dict[str, Cell]:
    di = dict()
    for name in book.names:
        if starts_with:
            if not name.name.startswith(starts_with):
                # logging.debug(f"Ignoring {name.name=}")
                continue

        try:
            range = name.refers_to_range
        except:
            logging.warning(f"REFERENCE Broken: '{name.name}': {name.refers_to} ")
            continue

        size = range.size

        if size != 1:
            logging.info(f"Ignoring {name.name=} range of size ")

        di[name.name] = Cell(
            name=name.name,
            sheet=range.sheet.name,
            address=range.address,
            value=range.value,
            formula=range.formula
        )
    return di

def variations(book: xw.Book):
    """returns the named range 'Varianten___'"""
    vars1 = book.names["Varianten____"].refers_to_range
    cols = len(vars1.columns)
    headers = book.sheets["Varianten"][1,:cols]

    if len(headers.columns) != len(vars1.columns):
        raise KeyError(f"Mismatching number of header and variation body columns")

    return headers, vars1


def append_variations_to_aggregation_sheet(
        peexcel_path: Path,
        agg_book_path: Path,
        agg_sheet_name: str,
        close_peexcel: bool=True,
):
    compare_book = xw.Book(agg_book_path)

    aggregation_sheet_name = agg_sheet_name
    sheetnames = [s.name for s in compare_book.sheets]
    if aggregation_sheet_name not in sheetnames:
        raise IndexError

    aggregation_sheet = compare_book.sheets[aggregation_sheet_name]

    logging.info(f"Opening {peexcel_path}")
    peexcel = xw.Book(peexcel_path)
    headers, databody = variations(peexcel)

    #TODO: extract method append_to_bottom(aggregation_sheet, databody)
    firstrow = aggregation_sheet["A4"].end("down").row
    lastrow = firstrow + len(databody.rows)
    firstcol, lastcol = 0, len(databody.columns)

    logging.info(f"inserting {lastrow-firstrow} variants at sheet {agg_sheet_name} from row{firstrow}-col{firstcol} to row{lastrow}-{lastcol}")

    insert_range = aggregation_sheet[firstrow:lastrow, firstcol:lastcol]
    insert_range.value = databody.value

    lastrow_new = aggregation_sheet["A4"].end("down").row
    insert_range = aggregation_sheet[firstrow:lastrow_new, firstcol:lastcol]
    insert_range.columns[5].value = str(peexcel_path)
    insert_range.columns[6].value = peexcel.name.split("_")[1]
    sht = compare_book.sheets[aggregation_sheet_name]

    if close_peexcel:
        logging.info(f"Closing {peexcel.name}")
        peexcel.close()

def end(range:xw.Range):
    """
    end() works exactly like ctrl_arrow movement.
    will stop at any empty cell encountered
    """
    lastrow = range.end("down")
    lastcol = lastrow.end("right")
    return (lastrow.row, lastcol.column)

def append_to_bottom(aggregation_sheet: xw.Sheet, databody: xw.Range):
    pass



if __name__ == "__main__":
    # names = nameslist(xw.Book("test_PlusenergieExcel_Performance.xlsx"))
    excel_paths = [
        # r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Aichinger_211021.xlsb",
        # r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_AmBichl_211022.xlsb",
        # r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Glan_211022.xlsb",
        # r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Gneis_211022.xlsb",
        # r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Graz_211022.xlsb",
        # r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Pilzgasse_211022.xlsb",
        r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\PlusenergieExcel_Pilzgasse_211022_ms.xlsb",
    ]

    paths = [Path(ep) for ep in excel_paths]

    aggregation_excel_path = Path(
        r"C:\Users\Simon Schneider\Nextcloud\EE\1_Forschung\2_Laufend\ZQ Austria\Quartiersdaten\Quartiersvergleich211027.xlsm")
    aggregation_sheet = "PEExcel Import"

    for path in paths:
        append_variations_to_aggregation_sheet(
            peexcel_path=path,
            agg_book_path=aggregation_excel_path,
            agg_sheet_name=aggregation_sheet,
            close_peexcel=False
        )

