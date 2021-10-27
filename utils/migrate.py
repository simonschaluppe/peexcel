# script to migrate a PEExcel to another Version / File
import csv
import logging
import os
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import xlwings as xw

from utils import excel

logging.basicConfig(level=logging.ERROR)
# Migrate PEExcel

## Old book
TEST_PATH = Path("test/test_PlusenergieExcel_Performance.xlsx")
TEST_SAVE_DIR = Path("test/")

from utils.excel import PEExcel
from utils.csv_handler import save_excel_data_to_dir
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




def migrate(source_path: Path,
            target_path: Path = None,
            save_csv=True
            ):
    if not target_path and not save_csv:
        raise UserWarning("Either target excel path or save_csv=True required")



    peexcel = PEExcel.parse(path=source_path)

    # TODO: write a report of
    if save_csv:
        save_excel_data_to_dir(
            directory=TEST_SAVE_DIR,
            peexcel=peexcel,
            overwrite=True
        )

    return 0


if __name__ == "__main__":
    migrate(TEST_PATH)
