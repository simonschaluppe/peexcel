from __future__ import annotations

from dataclasses import dataclass
from enum import StrEnum
from typing import TYPE_CHECKING

from pexl.i18n import LocalizedText

if TYPE_CHECKING:
    from pexl.schema.current import VariableMeta
    
class SankeyFlowType(StrEnum):
    """Semantic type of energy represented by a Sankey flow."""

    DEFAULT = "default"
    ELECTRICITY = "electricity"
    THERMAL = "thermal"
    ENVIRONMENTAL_HEAT = "environmental_heat"
    ENVIRONMENTAL_COLD = "environmental_cold"
    USEFUL_HEAT = "useful_heat"
    USEFUL_COLD = "useful_cold"
    LOSS = "loss"

@dataclass(frozen=True)
class SankeyNode:
    """Describe one semantic node in a Sankey diagram."""

    id: str
    label: LocalizedText


@dataclass(frozen=True)
class SankeyFlow:
    """Describe one directed flow backed by one PEExcel variable."""

    source: SankeyNode
    target: SankeyNode
    variable: VariableMeta
    flow_type: SankeyFlowType = SankeyFlowType.DEFAULT
    label: LocalizedText | None = None


@dataclass(frozen=True)
class SankeySpec:
    """Describe the topology and public-facing metadata of a Sankey diagram."""

    name: str
    title: LocalizedText
    flows: tuple[SankeyFlow, ...]