from collections.abc import Mapping, Sequence

import pandas as pd


def normalize_data(data) -> pd.DataFrame:
    if isinstance(data, pd.Series):
        return data.to_frame(name=data.name or "value")

    if isinstance(data, pd.DataFrame):
        return data

    if isinstance(data, Mapping):
        return pd.DataFrame(data)

    if isinstance(data, Sequence) and not isinstance(data, (str, bytes)):
        series = []
        for i, item in enumerate(data):
            if not isinstance(item, pd.Series):
                raise TypeError("Sequence entries must be pd.Series")
            series.append(item.rename(item.name or f"series_{i + 1}"))
        return pd.concat(series, axis=1)

    raise TypeError(
        "Expected Series, DataFrame, mapping, or sequence of Series"
    )

def normalize_panels(data):
    if isinstance(data, dict) and data:
        first = next(iter(data.values()))

        if isinstance(first, (dict, pd.DataFrame)):
            return {
                name: normalize_data(values)
                for name, values in data.items()
            }

    return {None: normalize_data(data)}