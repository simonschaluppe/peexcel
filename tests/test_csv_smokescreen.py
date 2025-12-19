from pathlib import Path
from pexl.io.csv import read_dataset_dir


def test_can_load_schema_dev():
    root = Path("data/schemas/dev")
    tables = read_dataset_dir(root)

    assert "IN" in tables
    assert "OUT" in tables
    assert len(tables["IN"].columns) > 0
    assert len(tables["OUT"].columns) > 0