"""Catalog merging must preserve identity and reconcile run-local inference."""
import json

import pyarrow as pa
import pyarrow.parquet as pq
import pytest

from pexl.io.parquet import combine_annual_batches


def write_run(path, batch, **columns):
    pq.write_table(pa.table({"batch": [batch], "scenario_name": ["same"],
                            "source_file": ["annual-00001.xlsx"], **columns}), path)


def test_catalog_promotes_types_and_retains_both_identities(tmp_path):
    first, second = tmp_path / "first.parquet", tmp_path / "second.parquet"
    write_run(first, "pv", QH=[1.5], unused=pa.array([None], type=pa.string()))
    write_run(second, "noPV", QH=[0], unused=[3.0], additional=[4])
    output = combine_annual_batches([first, second], tmp_path / "catalog", rows_per_batch=1)
    table = pq.read_table(output)
    assert table["batch"].to_pylist() == ["pv", "noPV"]
    assert table["QH"].to_pylist() == [1.5, 0.0]
    assert table["unused"].to_pylist() == [None, 3.0]
    assert table["additional"].to_pylist() == [None, 4]
    assert json.loads(table.schema.metadata[b"pexl.catalog"])["scenario_count"] == 2
    # Rebuilding replaces the catalog instead of appending duplicates.
    combine_annual_batches([first, second], output.parent)
    assert pq.read_metadata(output).num_rows == 2


def test_duplicate_identity_leaves_previous_catalog_intact(tmp_path):
    first, second = tmp_path / "first.parquet", tmp_path / "second.parquet"
    write_run(first, "run", QH=[1])
    output = combine_annual_batches([first], tmp_path / "catalog")
    original = output.read_bytes()
    write_run(second, "run", QH=[2])
    with pytest.raises(ValueError, match="Duplicate"):
        combine_annual_batches([first, second], output.parent)
    assert output.read_bytes() == original


def test_incompatible_non_null_types_are_not_silently_coerced(tmp_path):
    first, second = tmp_path / "first.parquet", tmp_path / "second.parquet"
    write_run(first, "one", QH=[1.0])
    write_run(second, "two", QH=["error"])
    with pytest.raises(pa.ArrowTypeError):
        combine_annual_batches([first, second], tmp_path / "catalog")
