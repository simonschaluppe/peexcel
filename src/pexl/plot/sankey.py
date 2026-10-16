from __future__ import annotations

from typing import TYPE_CHECKING

import pandas as pd
import plotly.graph_objects as go

from pexl.i18n import Language
from pexl.reporting.sankey import SankeyFlowType, SankeySpec

if TYPE_CHECKING:
    from pexl.model.scenario import Scenario
    from pexl.schema.current import VariableMeta


FLOW_COLORS = {
    SankeyFlowType.DEFAULT: "#166166",
    SankeyFlowType.ELECTRICITY: "#7e1141",
    SankeyFlowType.THERMAL: "#a22110",
    SankeyFlowType.ENVIRONMENTAL_HEAT: "#63C3E6",
    SankeyFlowType.ENVIRONMENTAL_COLD: "#0D7DD9",
    SankeyFlowType.USEFUL_HEAT: "#E1320F",
    SankeyFlowType.USEFUL_COLD: "#00B0F0",
    SankeyFlowType.LOSS: "#767676",
}


def _variable_label(variable: VariableMeta, language: Language) -> str:
    """Return the best available localized label for a schema variable."""
    label = getattr(variable, f"label_{language}", None)
    return label or variable.var_name


def to_frame(
    scenario: Scenario,
    spec: SankeySpec,
    *,
    language: Language = "de",
    drop_zero: bool = True,
) -> pd.DataFrame:
    """Materialize one Sankey specification for one scenario."""
    rows = []

    for flow in spec.flows:
        value = getattr(scenario.v, flow.variable.attr_name)

        if value is None:
            continue

        value = float(value)

        if drop_zero and value == 0:
            continue

        rows.append(
            {
                "source_id": flow.source.id,
                "source": flow.source.label.get(language),
                "target_id": flow.target.id,
                "target": flow.target.label.get(language),
                "value": abs(value),
                "unit": flow.variable.unit or "",
                "formula": flow.variable.formula or "",
                "variable": flow.variable.var_name,
                "label": (
                    flow.label.get(language)
                    if flow.label is not None
                    else _variable_label(flow.variable, language)
                ),
                "flow_type": flow.flow_type,
                "color": FLOW_COLORS.get(
                    flow.flow_type,
                    FLOW_COLORS[SankeyFlowType.DEFAULT],
                ),
            }
        )

    return pd.DataFrame(
        rows,
        columns=[
            "source_id",
            "source",
            "target_id",
            "target",
            "value",
            "unit",
            "formula",
            "variable",
            "label",
            "flow_type",
            "color",
        ],
    )


def render(
    scenario: Scenario,
    spec: SankeySpec,
    *,
    language: Language = "de",
    drop_zero: bool = True,
) -> go.Figure:
    """Render one PEExcel scenario as a localized Plotly Sankey diagram."""
    flows = to_frame(
        scenario,
        spec,
        language=language,
        drop_zero=drop_zero,
    )

    if flows.empty:
        fig = go.Figure()
        fig.update_layout(title=spec.title.get(language))
        return fig

    node_rows = pd.concat(
        [
            flows[["source_id", "source"]].rename(
                columns={"source_id": "id", "source": "label"}
            ),
            flows[["target_id", "target"]].rename(
                columns={"target_id": "id", "target": "label"}
            ),
        ],
        ignore_index=True,
    ).drop_duplicates(subset="id")

    node_ids = node_rows["id"].tolist()
    node_labels = node_rows["label"].tolist()
    node_index = {node_id: i for i, node_id in enumerate(node_ids)}

    fig = go.Figure(
        go.Sankey(
            node={
                "label": node_labels,
                "color": "#808080",
                "line": {
                    "color": "#606060",
                    "width": 1,
                },
            },
            link={
                "source": flows["source_id"].map(node_index),
                "target": flows["target_id"].map(node_index),
                "value": flows["value"],
                "label": flows["label"],
                "customdata": flows[["variable", "unit", "formula"]].to_numpy(),
                "color": flows["color"],
                "arrowlen": 12,
                "hovertemplate": (
                    "%{label}<br>"
                    "%{value:.2f} %{customdata[1]}<br>"
                    "Excel Name: %{customdata[0]}<br>"
                    "Excel Formula: %{customdata[2]}"
                    "<extra></extra>"
                )                          
            },
        )
    )

    fig.update_layout(
        title=f"{scenario.name} – {spec.title.get(language)}",
        font_size=11,
    )

    return fig