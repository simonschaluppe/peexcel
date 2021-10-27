import logging
from pathlib import Path
from unittest import TestCase

import pytest
import xlwings

from .. import migrate as m
from .. import excel





@pytest.fixture
def testbook_path():
    return Path("test_PlusenergieExcel_Performance.xlsx")

@pytest.fixture
def testbook(testbook_path):
    logging.debug(testbook_path)
    book = xlwings.Book(testbook_path)
    # assert type(book) is xlwings.Book
    return book


def test_migrate(testbook_path):
    assert 0 == m.migrate(source_path=testbook_path,
                     target_path=testbook_path,
                     save_csv=False
                     )



def test_single_names(testbook):
    result = excel.single_names(testbook, starts_with="Userinput_")
    assert result["Userinput_test1"] is not None
    assert result["Userinput_test1"].value == "testinput"
    assert result["Userinput_test2"].formula == "=A1"

    result = excel.single_names(testbook, starts_with="Ergebnis_")
    assert result["Ergebnis_1"].value == 3
    # testing formulas is tricky, as xlwings saves the english translation
    assert result["Ergebnis_1"].formula != "=WURZEL(9)"
    assert result["Ergebnis_1"].formula == "=SQRT(9)"
