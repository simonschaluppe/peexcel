import pytest

from pexl.io.csv_io import read_dataset_dir


def test_load_complete_schema_dataset(tmp_path):
    for name in ("IN", "OUT", "SIM", "CHART_metadata", "CHART_types"):
        (tmp_path / f"{name}.csv").write_text(
            "var_name;Name\nexample;Wärmepumpe\n", encoding="utf-8-sig"
        )
    tables = read_dataset_dir(tmp_path)
    assert set(tables) == {"IN", "OUT", "SIM", "CHART_metadata", "CHART_types"}
    assert tables["IN"].to_dict("records") == [
        {"var_name": "example", "Name": "Wärmepumpe"}
    ]


def test_strict_requires_complete_dataset_but_non_strict_reads_older_schema(tmp_path):
    (tmp_path / "IN.csv").write_text("var_name;Name\nx;Example\n", encoding="utf-8")
    with pytest.raises(FileNotFoundError, match="Missing dataset tables"):
        read_dataset_dir(tmp_path)
    assert list(read_dataset_dir(tmp_path, strict=False)) == ["IN"]


def test_empty_dataset_is_rejected(tmp_path):
    with pytest.raises(FileNotFoundError, match="No CSV tables"):
        read_dataset_dir(tmp_path, strict=False)
