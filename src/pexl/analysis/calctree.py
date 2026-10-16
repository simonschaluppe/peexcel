from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set
import json
import re

import networkx as nx
import pandas as pd
import plotly.graph_objects as go


SOURCE_COLORS = {
    "IN": "cornflowerblue",
    "OUT": "orange",
    "SIM": "lightgreen",
    "IN+SIM": "mediumseagreen",
    "OUT+SIM": "goldenrod",
    "IN+OUT": "mediumpurple",
    "IN+OUT+SIM": "slateblue",
    "UNKNOWN": "gray",
}

META_FIELDS = [
    "icon",
    "domain",
    "measure",
    "spatial_scope",
    "temporal_scope",
    "entity_group",
    "entity_key",
    "var_name",
    "ka",
    "label_de",
    "unit",
    "comment",
]

STRUCTURED_REF_RE = re.compile(r"\[\@\[(.*?)\]\]")
WORD_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")

EXCEL_FUNCTIONS = {
    "IF", "IFS", "AND", "OR", "NOT", "SUM", "MIN", "MAX", "AVERAGE",
    "ABS", "ROUND", "ROUNDUP", "ROUNDDOWN", "INT", "MOD",
    "XLOOKUP", "VLOOKUP", "HLOOKUP", "INDEX", "MATCH", "OFFSET",
    "COUNT", "COUNTA", "COUNTIF", "COUNTIFS", "SUMIF", "SUMIFS",
    "IFNA", "IFERROR", "ISNA", "ISERROR",
    "COS", "SIN", "TAN", "PI",
    "TRUE", "FALSE",
    "NA",
}


def _clean(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    return str(value).strip()


def _read_schema_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, sep=";")


def _first_nonempty(d: Dict[str, Any], keys: Iterable[str], default: Any = "") -> Any:
    for key in keys:
        value = d.get(key)
        if _clean(value) != "":
            return value
    return default


def _normalize_source_tag(tags: Iterable[str]) -> str:
    ordered = [tag for tag in ["IN", "OUT", "SIM"] if tag in set(tags)]
    return "+".join(ordered) if ordered else "UNKNOWN"


@dataclass
class VariableRecord:
    var_name: str
    source_tags: List[str]
    icon: str = ""
    domain: str = ""
    measure: str = ""
    spatial_scope: str = ""
    temporal_scope: str = ""
    entity_group: str = ""
    entity_key: str = ""
    ka: str = ""
    label_de: str = ""
    unit: str = ""
    comment: str = ""
    formula: str = ""

    @property
    def source(self) -> str:
        return _normalize_source_tag(self.source_tags)

    @property
    def color(self) -> str:
        return SOURCE_COLORS.get(self.source, SOURCE_COLORS["UNKNOWN"])

    @property
    def label(self) -> str:
        return self.label_de or self.var_name

    @property
    def group_key(self) -> str:
        return "|".join(
            [
                self.domain,
                self.measure,
                self.spatial_scope,
                self.temporal_scope,
                self.entity_group,
                self.entity_key,
            ]
        )

    def to_node_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["source"] = self.source
        data["color"] = self.color
        data["label"] = self.label
        data["group_key"] = self.group_key
        return data


class SchemaCalcGraph:
    """
    Build a dependency graph from a schema folder containing:

    - IN.csv
    - OUT.csv
    - SIM.csv

    Expected file formats:
    - IN.csv:  semicolon-separated, includes rich metadata and optional Formel
    - OUT.csv: semicolon-separated, includes rich metadata
    - SIM.csv: semicolon-separated, columns: var_name, Formula
    """

    def __init__(self, schema_dir: str | Path):
        self.schema_dir = Path(schema_dir)
        self.df_in = _read_schema_csv(self.schema_dir / "IN.csv")
        self.df_out = _read_schema_csv(self.schema_dir / "OUT.csv")
        self.df_sim = _read_schema_csv(self.schema_dir / "SIM.csv")

        self.records: Dict[str, VariableRecord] = self._build_records()

    def _build_records(self) -> Dict[str, VariableRecord]:
        records: Dict[str, VariableRecord] = {}

        def ensure_record(var_name: str) -> VariableRecord:
            if var_name not in records:
                records[var_name] = VariableRecord(var_name=var_name, source_tags=[])
            return records[var_name]

        def merge_meta_from_row(record: VariableRecord, row: pd.Series, source_tag: str) -> None:
            if source_tag not in record.source_tags:
                record.source_tags.append(source_tag)

            for field in META_FIELDS:
                if field == "var_name":
                    continue
                row_value = _clean(row.get(field))
                current_value = _clean(getattr(record, field))
                if row_value and not current_value:
                    setattr(record, field, row_value)

            formula_value = _clean(row.get("Formel"))
            if formula_value and not record.formula:
                record.formula = formula_value

        for _, row in self.df_in.iterrows():
            var_name = _clean(row.get("var_name"))
            if not var_name:
                continue
            rec = ensure_record(var_name)
            merge_meta_from_row(rec, row, "IN")

        for _, row in self.df_out.iterrows():
            var_name = _clean(row.get("var_name"))
            if not var_name:
                continue
            rec = ensure_record(var_name)
            merge_meta_from_row(rec, row, "OUT")

        for _, row in self.df_sim.iterrows():
            var_name = _clean(row.get("var_name"))
            if not var_name:
                continue
            rec = ensure_record(var_name)
            if "SIM" not in rec.source_tags:
                rec.source_tags.append("SIM")

            sim_formula = _clean(row.get("Formula"))
            if sim_formula:
                rec.formula = sim_formula

        return records

    @property
    def var_names(self) -> Set[str]:
        return set(self.records.keys())

    def parse_formula_refs(self, formula: str) -> List[str]:
        refs: Set[str] = set()
        if not formula:
            return []

        for ref in STRUCTURED_REF_RE.findall(formula):
            ref = _clean(ref)
            if ref in self.var_names:
                refs.add(ref)

        for token in WORD_RE.findall(formula):
            token = token.strip()
            if token.upper() in EXCEL_FUNCTIONS:
                continue
            if token in self.var_names:
                refs.add(token)

        return sorted(refs)

    def build_graph(self, include_isolated: bool = True) -> nx.DiGraph:
        G = nx.DiGraph()

        for var_name, record in self.records.items():
            if include_isolated or record.formula:
                G.add_node(var_name, **record.to_node_dict())

        for var_name, record in self.records.items():
            if var_name not in G:
                continue
            if not record.formula:
                continue

            for parent_var in self.parse_formula_refs(record.formula):
                if parent_var == var_name:
                    continue
                if parent_var not in G:
                    G.add_node(parent_var, **self.records[parent_var].to_node_dict())
                G.add_edge(parent_var, var_name)

        return G

    def upstream_subgraph(self, target_var: str) -> nx.DiGraph:
        G = self.build_graph(include_isolated=True)
        if target_var not in G:
            raise KeyError(f"{target_var!r} not found")
        keep = {target_var, *nx.ancestors(G, target_var)}
        return G.subgraph(keep).copy()

    def downstream_subgraph(self, source_var: str) -> nx.DiGraph:
        G = self.build_graph(include_isolated=True)
        if source_var not in G:
            raise KeyError(f"{source_var!r} not found")
        keep = {source_var, *nx.descendants(G, source_var)}
        return G.subgraph(keep).copy()

    def filter_graph(
        self,
        G: nx.DiGraph,
        *,
        source: Optional[str] = None,
        domain: Optional[str] = None,
        measure: Optional[str] = None,
        spatial_scope: Optional[str] = None,
        temporal_scope: Optional[str] = None,
        entity_group: Optional[str] = None,
        entity_key: Optional[str] = None,
    ) -> nx.DiGraph:
        keep = []

        for node, data in G.nodes(data=True):
            if source is not None and _clean(data.get("source")).upper() != source.upper():
                continue
            if domain is not None and _clean(data.get("domain")) != domain:
                continue
            if measure is not None and _clean(data.get("measure")) != measure:
                continue
            if spatial_scope is not None and _clean(data.get("spatial_scope")) != spatial_scope:
                continue
            if temporal_scope is not None and _clean(data.get("temporal_scope")) != temporal_scope:
                continue
            if entity_group is not None and _clean(data.get("entity_group")) != entity_group:
                continue
            if entity_key is not None and _clean(data.get("entity_key")) != entity_key:
                continue
            keep.append(node)

        return G.subgraph(keep).copy()


def export_graph_as_json(G: nx.DiGraph, file_path: str | Path) -> None:
    elements = []
    for node, data in G.nodes(data=True):
        elements.append(
            {
                "id": node,
                "label": data.get("label", node),
                "var_name": node,
                "source": data.get("source", ""),
                "domain": data.get("domain", ""),
                "measure": data.get("measure", ""),
                "spatial_scope": data.get("spatial_scope", ""),
                "temporal_scope": data.get("temporal_scope", ""),
                "entity_group": data.get("entity_group", ""),
                "entity_key": data.get("entity_key", ""),
                "unit": data.get("unit", ""),
                "icon": data.get("icon", ""),
                "comment": data.get("comment", ""),
                "ka": data.get("ka", ""),
                "group_key": data.get("group_key", ""),
                "formula": data.get("formula", ""),
            }
        )

    connections = []
    for src, dst in G.edges():
        connections.append(
            {
                "from": src,
                "to": dst,
                "direction": "directed",
            }
        )

    payload = {
        "elements": elements,
        "connections": connections,
    }

    Path(file_path).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


def draw_dependency_graph_interactive(
    G: nx.DiGraph,
    title: str = "Calculation dependency graph",
) -> None:
    if len(G.nodes) == 0:
        raise ValueError("Graph is empty")

    pos = nx.spring_layout(G, k=0.35, iterations=100, seed=42)

    edge_x = []
    edge_y = []
    for src, dst in G.edges():
        x0, y0 = pos[src]
        x1, y1 = pos[dst]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode="lines",
        line=dict(width=0.8, color="#888"),
        hoverinfo="none",
    )

    node_x = []
    node_y = []
    node_text = []
    node_hover = []
    node_color = []

    for node, data in G.nodes(data=True):
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(data.get("label", node))
        node_color.append(data.get("color", "gray"))

        hover = "<br>".join(
            [
                f"<b>{data.get('label', node)}</b>",
                f"var_name: {node}",
                f"source: {_clean(data.get('source'))}",
                f"domain: {_clean(data.get('domain'))}",
                f"measure: {_clean(data.get('measure'))}",
                f"spatial_scope: {_clean(data.get('spatial_scope'))}",
                f"temporal_scope: {_clean(data.get('temporal_scope'))}",
                f"entity_group: {_clean(data.get('entity_group'))}",
                f"entity_key: {_clean(data.get('entity_key'))}",
                f"unit: {_clean(data.get('unit'))}",
                f"ka: {_clean(data.get('ka'))}",
            ]
        )
        node_hover.append(hover)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        text=node_text,
        textposition="top center",
        hovertext=node_hover,
        hoverinfo="text",
        marker=dict(
            size=14,
            color=node_color,
            line=dict(width=0.6, color="black"),
        ),
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=title,
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=20, r=20, t=40),
            xaxis=dict(showgrid=False, zeroline=False, visible=False),
            yaxis=dict(showgrid=False, zeroline=False, visible=False),
        ),
    )
    fig.show()


if __name__ == "__main__":
    calc = SchemaCalcGraph("data/schemas/v1_11_4")

    G = calc.build_graph(include_isolated=False)

    # Example:
    # G = calc.upstream_subgraph("QH_fPE_weighted_annual")
    # G = calc.filter_graph(G, domain="heat_balance", temporal_scope="annual")

    export_graph_as_json(G, "calctree.json")
    draw_dependency_graph_interactive(G, title="Schema-based calculation dependency graph")