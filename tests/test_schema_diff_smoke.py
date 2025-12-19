from pexl.validate.schema import diff_schema_dirs

def test_schema_diff_runs_on_dev_and_dev2():
    report = diff_schema_dirs("data/schemas/dev", "data/schemas/dev2")
    assert "tables" in report
    assert "IN" in report["tables"]
    assert "OUT" in report["tables"]
