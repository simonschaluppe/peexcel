"""Adapt annual values to ordinary frames without constructing Scenario objects."""
import logging

import pandas as pd

logger = logging.getLogger(__name__)


def annual_frame(source):
    from pexl.model.project import Project
    from pexl.model.scenario import Scenario
    from pexl.model.view import ProjectView, ScenarioView

    if isinstance(source, pd.DataFrame):
        frame = source.copy()
    else:
        if isinstance(source, Scenario):
            scenarios = (source,)
        elif isinstance(source, ScenarioView):
            scenarios = (source.scenario,)
        elif isinstance(source, (Project, ProjectView)):
            scenarios = source.scenarios
        else:
            raise TypeError("Expected a DataFrame, Project, Scenario, or their views")
        records = []
        for scenario in scenarios:
            values = scenario.to_var_dict()
            for name, value in scenario.legacy.items():
                if name not in values or pd.isna(values[name]):
                    values[name] = value
            records.append({**values, "column_name": scenario.column_name})
        frame = pd.DataFrame(records)

    if not frame.columns.is_unique:
        raise ValueError("Annual values require unique column names")
    if {"batch", "scenario_name"}.issubset(frame.columns):
        identity = pd.MultiIndex.from_frame(frame[["batch", "scenario_name"]])
    elif "scenario_name" in frame:
        identity = pd.Index(frame["scenario_name"], name="scenario_name")
    elif "column_name" in frame:
        identity = pd.Index(frame["column_name"], name="column_name")
    else:
        identity = frame.index
    if not identity.is_unique:
        raise ValueError("Scenario identities must be unique; include batch and scenario_name for multiple runs")
    frame.index = identity
    return frame


def display_names(frame):
    # Include every identity component so repeated names across runs stay visible.
    if isinstance(frame.index, pd.MultiIndex):
        names = [" | ".join(map(str, key)) for key in frame.index]
    else:
        names = frame.index.map(str).tolist()
    if len(set(names)) != len(names):
        logger.warning("Scenario display names collide; showing explicit index representations")
        return [repr(key) for key in frame.index]
    return names


def variable_label(name, language):
    from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META
    from pexl.i18n import PRIMARY_ENERGY_LABELS

    attr = ATTR_NAME_MAP.get(name)
    if attr is None:
        return name
    meta = getattr(SCHEMA_META, attr)
    label = (PRIMARY_ENERGY_LABELS[name].get(language) if name in PRIMARY_ENERGY_LABELS
             else getattr(meta, f"label_{language}", None) or meta.label_de or name)
    return f"{label} [{meta.unit}]" if meta.unit else label
