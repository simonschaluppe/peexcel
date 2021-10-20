# script to migrate a PEExcel to another Version / File
import logging
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Dict

import xlwings as xw


logging.basicConfig(level=logging.WARNING)
# Migrate PEExcel

## Old book

### Check that it is a valid book

### Parse the excel

# parse_peexcel(book: xw.Book) -> peexcel_data
# check availability, depending
# parse_inputs()
# parse_varianten()
# parse_allkindsofothershit()
# return peexcel_data

### (optional) Save the peexcel_data
# save_csv(peexcel_data) -> csv

### (optional) load from folder
# load_csv(csv) -> peexcel_data

## New book

### Write to new Excel

@dataclass
class Metadata:
    file: str
    extraction_date: datetime = datetime.now()


@dataclass
class Cell:
    value: 'typing.Any'
    formula: str
    sheet: str
    address: str
    name: str = ""


def single_names(book: xw.Book, starts_with:str="") -> Dict[str, Cell]:
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


def parse_peexcel(book: xw.Book):
    di = single_names(book, starts_with="Userinput_")
    results = single_names(book, starts_with="Ergebnis_")
    return dict(
        direct_inputs=di,
        results=results
    )




def migrate():
    path = Path("test_PlusenergieExcel_Performance.xlsx")
    # book = xw.Book(path)

if __name__ == "__main__":
    pass