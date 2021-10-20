import logging
from pathlib import Path
from unittest import TestCase

import pytest
import xlwings

import utils.migrate as m

@pytest.fixture(scope="module")
def testbook():
    path = Path("test_PlusenergieExcel_Performance.xlsx")
    book = xlwings.Book(path)
    # assert type(book) is xlwings.Book
    return book

def test_migrate():
    assert m.migrate()

def test_parse_peexcel(testbook):
    pee = m.parse_peexcel(testbook)
    assert "direct_inputs" in pee.keys()
    assert "results" in pee.keys()
    assert pee["results"]["Ergebnis_1"].value == 3
    # testing formulas is tricky, as xlwings saves the english translation
    assert pee["results"]["Ergebnis_1"].formula != "=WURZEL(9)"
    assert pee["results"]["Ergebnis_1"].formula == "=SQRT(9)"


def test_single_names(testbook):
    result = m.single_names(testbook, starts_with="Userinput_")
    assert result["Userinput_test1"] is not None
    assert result["Userinput_test1"].value == "testinput"
    assert result["Userinput_test2"].formula == "=A1"