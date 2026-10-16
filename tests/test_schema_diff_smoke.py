from pexl.validate.schema import diff_schema_dirs


def test_schema_diff_reports_changed_added_and_removed_variables(tmp_path):
    old = tmp_path / "old"
    new = tmp_path / "new"
    old.mkdir()
    new.mkdir()
    (old / "IN.csv").write_text(
        "var_name;Name\nkept;Before\nremoved;Old\n", encoding="utf-8"
    )
    (new / "IN.csv").write_text(
        "var_name;Name\nkept;After\nadded;New\n", encoding="utf-8"
    )
    for root in (old, new):
        (root / "OUT.csv").write_text("var_name;Name\nresult;Result\n", encoding="utf-8")
    report = diff_schema_dirs(old, new)
    assert report["tables"]["IN"]["rows"]["var_name_added"] == ["added"]
    assert report["tables"]["IN"]["rows"]["var_name_removed"] == ["removed"]
    assert report["tables"]["IN"]["changes"]["value_change_count"] == 1
    assert report["tables"]["OUT"]["changes"]["value_change_count"] == 0
