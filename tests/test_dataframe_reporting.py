"""Regressions at the annual storage/reporting boundary."""
import json

import pandas as pd
import pytest

from pexl import Project, reporting, plot
from pexl.model.scenario import Scenario
from pexl.schema.current import CHARTS, ATTR_NAME_MAP


def test_dataframe_and_project_share_heat_report_and_balance():
    project = Project()
    for number in range(2):
        scenario = Scenario(f"s{number}")
        for series in CHARTS["heat_balance"].series:
            setattr(scenario.v, ATTR_NAME_MAP[series.var_name], number + 2.0)
        project.add_scenario(scenario)
    frame = project.view.to_frame()
    expected = reporting.materialize(project, "heat_balance")
    actual = reporting.materialize(frame, "heat_balance")
    pd.testing.assert_frame_equal(actual["frame"], expected["frame"])
    before = frame.copy(deep=True)
    data = reporting.balance(frame.iloc[::-1], "heat_balance")
    assert data["frame"].index.tolist() == ["s1", "s0"]
    pd.testing.assert_frame_equal(frame, before)


def test_repeated_names_across_batches_remain_distinct():
    frame = pd.DataFrame({"batch": ["b", "a"], "scenario_name": ["same", "same"],
                          "FSI": [2, 1], "PEI_balance": [-4, 5]})
    data = reporting.variables(frame, "FSI", "PEI_balance", language="en")
    assert data["frame"].index.tolist() == [("b", "same"), ("a", "same")]
    figure = plot.scatter(**data, x="FSI", y="PEI_balance")
    assert list(figure.data[0].y) == [-4, 5]
    assert figure.layout.separators == ".,"
    assert len(set(figure.data[0].hovertext)) == 2


def test_missing_selection_warns_and_keeps_unknown_user_columns(caplog):
    frame = pd.DataFrame({"custom": [3]})
    data = reporting.variables(frame, "custom", "missing")
    assert data["labels"]["custom"] == "custom"
    assert data["frame"]["missing"].isna().all()
    assert "missing" in caplog.text
    assert "missing" not in frame


def test_localized_title_and_histogram():
    frame = pd.DataFrame({s.var_name: [1.0] for s in CHARTS["heat_balance"].series})
    de = reporting.materialize(frame, "heat_balance", language="de")
    en = reporting.materialize(frame, "heat_balance", language="en")
    pd.testing.assert_frame_equal(de["frame"], en["frame"])
    assert de["title"] == "Wärmebilanz"
    assert en["title"] == "Heat balance"
    assert plot.histogram(pd.DataFrame({"x": [1, 2]}), "x", language="en").layout.yaxis.title.text == "Frequency"


def test_streaming_conversion_preserves_values_and_previous_output(tmp_path):
    from openpyxl import Workbook
    from pexl.io.parquet import export_annual_batch
    import pyarrow.parquet as pq

    source = tmp_path / "run"
    source.mkdir()
    book = Workbook()
    book.remove(book.active)
    for sheet, variable in (("IN", "FSI"), ("OUT", "QH")):
        ws = book.create_sheet(sheet)
        ws.append(["var_name", "Name", "one", "two"])
        ws.append([variable, "label", 1.25, None])
    book.save(source / "annual-00001.xlsx")
    manifest = {"identity": {"schema": "1_13_1_dev"}, "failed": {},
                "chunks": [{"annual": "annual-00001.xlsx", "scenarios": ["one", "two"]}]}
    (source / "batch.json").write_text(json.dumps(manifest), encoding="utf8")
    output = export_annual_batch(source, tmp_path / "result", files_per_row_group=1)
    df = pd.read_parquet(output)
    assert df["scenario_name"].tolist() == ["one", "two"]
    assert df["QH"][0] == 1.25 and pd.isna(df["QH"][1])
    metadata = json.loads(pq.ParquetFile(output).schema_arrow.metadata[b"pexl.batch"])
    assert metadata["schema"] == "1_13_1_dev"
    original = output.read_bytes()
    # Duplicate names prevent publishing an ambiguous replacement.
    manifest["chunks"][0]["scenarios"] = ["one", "one"]
    (source / "batch.json").write_text(json.dumps(manifest), encoding="utf8")
    with pytest.raises(ValueError):
        export_annual_batch(source, output.parent)
    assert output.read_bytes() == original
