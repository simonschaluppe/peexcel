import pandas as pd
from pexl.io.csv import normalize_table


def test_normalize_strips_and_sorts():
    df = pd.DataFrame(
        {
            "var_name": [" b ", "a"],
            "value": [" 2 ", "1"],
        }
    )

    norm = normalize_table(df, key_cols=["var_name"])

    assert norm["var_name"].tolist() == ["a", "b"]
    assert norm["value"].tolist() == ["1", "2"]