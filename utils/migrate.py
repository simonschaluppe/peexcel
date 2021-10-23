# script to migrate a PEExcel to another Version / File
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import xlwings as xw


logging.basicConfig(level=logging.WARNING)
# Migrate PEExcel

## Old book
TEST_PATH = Path("test_PlusenergieExcel_Performance.xlsx")
TEST_SAVE_DIR = Path("test/")
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
class PEExcel:
    file: Path
    extraction_date: datetime = datetime.now()
    version: str = "0.0"
    _inputs: List = field(default_factory=list)
    _results: List = field(default_factory=list)

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


@dataclass
class Cell:
    value: 'typing.Any'
    name: str = ""
    formula: str = ""
    sheet: str = ""
    address: str = ""

    def csv_line(self, delimiter=";"):
        str_vals = [str(v) for v in self.__dict__.values()]
        return delimiter.join(str_vals)

    @classmethod
    def csv_header(cls, delimiter=";"):
        return "value;name;formula;sheet;address"

@dataclass
class Direktinput(Cell):
    pass
@dataclass
class Ergebnis(Cell):
    pass


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



def write_csv(path:Path, list_of_cells:List[Cell], meta_data):
    with open(path, mode="w") as f:
        m = [f"# {k}; {v}\n" for k, v in meta_data.items()]
        f.writelines(m)

        f.write(Cell.csv_header())
        f.write("\n")
        for v in list_of_cells:
            f.write(v.csv_line())
            f.write("\n")




def save_excel_data_as_csvs(directory:Path, peexcel:PEExcel, overwrite=False):
    if directory is None:
        directory = TEST_SAVE_DIR
        overwrite = True
    if directory.is_dir() and not overwrite:
        raise RuntimeError(f"{directory=} ALREADY EXISTS!")

    if not directory.is_dir():
        os.makedirs(directory)

    write_csv(directory / "test_di.csv",
              list_of_cells=peexcel.inputs,
              meta_data=peexcel.info()
              )
    write_csv(directory / "test_results.csv",
              list_of_cells=peexcel.results,
              meta_data=peexcel.info()
              )


def migrate(source_path:Path,
            target_path:Path=None,
            save_csv=True
            ):
    if not target_path and not save_csv:
        raise UserWarning("Either target excel path or save_csv=True required")

    book = xw.Book(source_path)
    peexcel = PEExcel(
        file=source_path,
        _inputs=single_names(book, starts_with="Userinput_").values(),
        _results=single_names(book, starts_with="Ergebnis_").values(),
    )

    if save_csv:
        save_excel_data_as_csvs(
            directory=TEST_SAVE_DIR,
            peexcel=peexcel,
            overwrite=True
        )

    return 0



if __name__ == "__main__":
    migrate(TEST_PATH)