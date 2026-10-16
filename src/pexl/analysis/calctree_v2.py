from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
import json
import math
import re

import networkx as nx
import pandas as pd
import plotly.graph_objects as go


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


def _normalize_source_tag(tags: Iterable[str]) -> str:
    ordered = [tag for tag in ["IN", "SIM", "OUT"] if tag in set(tags)]
    return "+".join(ordered) if ordered else "UNKNOWN"


def _ka_style(ka: Any) -> Dict[str, Any]:
    ka_str = _clean(ka)

    if ka_str == "0":
        return {
            "fillcolor": "white",
            "line": {"color": "red", "width": 1.5},
        }
    if ka_str == "1":
        return {
            "fillcolor": "#eaf7e7",
            "line": {"color": "green", "width": 1.0},
        }
    if ka_str == "2":
        return {
            "fillcolor": "#eaf7e7",
            "line": {"color": "green", "width": 3.0},
        }

    return {
        "fillcolor": "white",
        "line": {"color": "gray", "width": 1.0},
    }


@dataclass
class VariableRecord:
    var_name: str
    source_tags: List[str]
    schema_order: int
    in_schema: bool = False
    sim_schema: bool = False
    out_schema: bool = False
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
    def label(self) -> str:
        return self.label_de or self.var_name

    @property
    def display_layer(self) -> str:
        if self.in_schema:
            return "IN"
        if self.sim_schema:
            return "SIM"
        if self.out_schema:
            return "OUT"
        return "OUT"

    @property
    def merge_key(self) -> str:
        return f"{self.display_layer}|{self.domain}|{self.measure}"

    def to_node_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["source"] = self.source
        data["label"] = self.label
        data["display_layer"] = self.display_layer
        data["merge_key"] = self.merge_key
        data["style"] = (
            _ka_style(self.ka)
            if self.display_layer == "IN"
            else {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}}
        )
        return data


class SchemaCalcGraph:
    def __init__(self, schema_dir: str | Path):
        self.schema_dir = Path(schema_dir)
        self.df_in = _read_schema_csv(self.schema_dir / "IN.csv")
        self.df_out = _read_schema_csv(self.schema_dir / "OUT.csv")
        self.df_sim = _read_schema_csv(self.schema_dir / "SIM.csv")

        self.domain_order = self._build_domain_order()
        self.records: Dict[str, VariableRecord] = self._build_records()

    def _build_domain_order(self) -> List[str]:
        seen = set()
        ordered: List[str] = []

        for df in (self.df_in, self.df_sim, self.df_out):
            if "domain" not in df.columns:
                continue
            for value in df["domain"]:
                domain = _clean(value)
                if domain and domain not in seen:
                    seen.add(domain)
                    ordered.append(domain)

        return ordered

    def _domain_rank(self, domain: str) -> int:
        domain = _clean(domain)
        try:
            return self.domain_order.index(domain)
        except ValueError:
            return len(self.domain_order)

    def _build_records(self) -> Dict[str, VariableRecord]:
        records: Dict[str, VariableRecord] = {}
        schema_counter = 0

        def ensure_record(var_name: str) -> VariableRecord:
            nonlocal schema_counter
            if var_name not in records:
                records[var_name] = VariableRecord(
                    var_name=var_name,
                    source_tags=[],
                    schema_order=schema_counter,
                )
                schema_counter += 1
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
            rec.in_schema = True
            merge_meta_from_row(rec, row, "IN")

        for _, row in self.df_sim.iterrows():
            var_name = _clean(row.get("var_name"))
            if not var_name:
                continue
            rec = ensure_record(var_name)
            rec.sim_schema = True
            if "SIM" not in rec.source_tags:
                rec.source_tags.append("SIM")

            for field in META_FIELDS:
                if field == "var_name":
                    continue
                row_value = _clean(row.get(field))
                current_value = _clean(getattr(rec, field))
                if row_value and not current_value:
                    setattr(rec, field, row_value)

            sim_formula = _clean(row.get("Formula"))
            if sim_formula:
                rec.formula = sim_formula

        for _, row in self.df_out.iterrows():
            var_name = _clean(row.get("var_name"))
            if not var_name:
                continue
            rec = ensure_record(var_name)
            rec.out_schema = True
            merge_meta_from_row(rec, row, "OUT")

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

    def build_variable_graph(self, include_isolated: bool = True) -> nx.DiGraph:
        G = nx.DiGraph()

        for var_name, record in self.records.items():
            if include_isolated or record.formula:
                G.add_node(var_name, **record.to_node_dict())

        for var_name, record in self.records.items():
            if var_name not in G or not record.formula:
                continue

            for parent_var in self.parse_formula_refs(record.formula):
                if parent_var == var_name:
                    continue
                if parent_var not in G:
                    G.add_node(parent_var, **self.records[parent_var].to_node_dict())
                G.add_edge(parent_var, var_name)

        return G

    def build_group_graph(
        self,
        include_isolated: bool = True,
        merge_by: Tuple[str, ...] = ("display_layer", "domain", "measure"),
    ) -> nx.DiGraph:
        VG = self.build_variable_graph(include_isolated=include_isolated)
        GG = nx.DiGraph()

        group_members: Dict[Tuple[str, ...], List[str]] = {}

        def node_group_key(node_data: Dict[str, Any]) -> Tuple[str, ...]:
            return tuple(_clean(node_data.get(part)) for part in merge_by)

        for var_name, data in VG.nodes(data=True):
            gkey = node_group_key(data)
            group_members.setdefault(gkey, []).append(var_name)

        for gkey, members in group_members.items():
            members_sorted = sorted(members, key=lambda n: self.records[n].schema_order)
            first = members_sorted[0]
            first_data = VG.nodes[first]

            layer = _clean(first_data.get("display_layer"))
            domain = _clean(first_data.get("domain"))
            measure = _clean(first_data.get("measure"))

            icons = []
            for m in members_sorted:
                icon = _clean(VG.nodes[m].get("icon"))
                if icon and icon not in icons:
                    icons.append(icon)

            label_parts = [part for part in [domain, measure] if part]
            display_text = " ".join(icons[:2]) if icons else "•"

            if layer == "IN":
                ka_values = {_clean(VG.nodes[m].get("ka")) for m in members_sorted if _clean(VG.nodes[m].get("ka"))}
                if "2" in ka_values:
                    style = _ka_style("2")
                elif "1" in ka_values:
                    style = _ka_style("1")
                elif "0" in ka_values:
                    style = _ka_style("0")
                else:
                    style = _ka_style("")
            else:
                style = {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}}

            GG.add_node(
                gkey,
                id="|".join(gkey),
                display_layer=layer,
                domain=domain,
                measure=measure,
                label=" | ".join(label_parts) if label_parts else first,
                text=display_text,
                style=style,
                source_tags=sorted({_clean(VG.nodes[m].get("source")) for m in members_sorted if _clean(VG.nodes[m].get("source"))}),
                members=members_sorted,
                member_count=len(members_sorted),
                schema_order=min(self.records[m].schema_order for m in members_sorted),
                annotation=domain+" | "+measure,
            )

        for src, dst in VG.edges():
            src_g = node_group_key(VG.nodes[src])
            dst_g = node_group_key(VG.nodes[dst])
            if src_g != dst_g:
                GG.add_edge(src_g, dst_g)

        return GG

    def layout_positions(
        self,
        G: nx.DiGraph,
        *,
        dx: float = 2.4,
        dy: float = 6.0,
        domain_gap: float = 1.6,
        wave_amp: float = 0.55,
        wave_period: float = 3.5,
        wave_phase_by_layer: Optional[Dict[str, float]] = None,
    ) -> Dict[Any, Tuple[float, float]]:
        buckets: Dict[str, Dict[str, List[Any]]] = {
            "IN": {},
            "SIM": {},
            "OUT": {},
        }

        for node, data in G.nodes(data=True):
            layer = _clean(data.get("display_layer")) or "OUT"
            domain = _clean(data.get("domain")) or "__NO_DOMAIN__"
            buckets.setdefault(layer, {}).setdefault(domain, []).append(node)

        for layer_name in buckets:
            for domain, nodes in buckets[layer_name].items():
                nodes.sort(
                    key=lambda n: (
                        G.nodes[n].get("schema_order", 10**9),
                        _clean(G.nodes[n].get("measure")),
                        _clean(G.nodes[n].get("label")),
                        str(n),
                    )
                )

        pos: Dict[Any, Tuple[float, float]] = {}
        y_map = {
            "IN": 0.0,
            "SIM": -dy,
            "OUT": -2 * dy,
        }
        phase_map = wave_phase_by_layer or {
            "IN": 0.0,
            "SIM": 0.9,
            "OUT": 1.8,
        }

        for layer_name in ["IN", "SIM", "OUT"]:
            x = 0.0

            domains_in_layer = sorted(
                buckets[layer_name].keys(),
                key=lambda d: (
                    self._domain_rank("" if d == "__NO_DOMAIN__" else d),
                    d,
                ),
            )

            for domain in domains_in_layer:
                nodes = buckets[layer_name][domain]
                for i, node in enumerate(nodes):
                    y = y_map[layer_name] + wave_amp * math.sin((x / wave_period) + phase_map.get(layer_name, 0.0))
                    pos[node] = (x, y)
                    x += dx
                x += domain_gap

        return pos

    def apply_domain_colors(
        self,
        G: nx.DiGraph,
        palette: Dict[str, str],
        *,
        fallback: str = "lightgray",
        color_fill: bool = True,
        color_border: bool = True,
        preserve_in_ka_fill: bool = False,
    ) -> nx.DiGraph:
        for _, data in G.nodes(data=True):
            domain = _clean(data.get("domain"))
            layer = _clean(data.get("display_layer"))
            style = data.get("style", {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}})
            color = palette.get(domain, fallback)

            if color_fill and not (preserve_in_ka_fill and layer == "IN"):
                style["fillcolor"] = color
            if color_border:
                style["line"]["color"] = color

            data["style"] = style

        return G

    def make_domain_group_shapes(
        self,
        G: nx.DiGraph,
        pos: Dict[Any, Tuple[float, float]],
        *,
        domain_palette: Optional[Dict[str, str]] = None,
        opacity: float = 0.10,
        pad_x: float = 0.55,
        pad_y: float = 0.85,
    ) -> List[Dict[str, Any]]:
        shapes: List[Dict[str, Any]] = []
        grouped: Dict[Tuple[str, str], List[Any]] = {}

        for node, data in G.nodes(data=True):
            layer = _clean(data.get("display_layer"))
            domain = _clean(data.get("domain"))
            if not layer or not domain or node not in pos:
                continue
            grouped.setdefault((layer, domain), []).append(node)

        for (layer, domain), nodes in grouped.items():
            xs = [pos[n][0] for n in nodes]
            ys = [pos[n][1] for n in nodes]
            color = (domain_palette or {}).get(domain, "#bbbbbb")
            shapes.append(
                dict(
                    type="rect",
                    xref="x",
                    yref="y",
                    x0=min(xs) - pad_x,
                    x1=max(xs) + pad_x,
                    y0=min(ys) - pad_y,
                    y1=max(ys) + pad_y,
                    line=dict(color=color, width=1),
                    fillcolor=color,
                    opacity=opacity,
                    layer="below",
                )
            )
        return shapes


def export_graph_as_json(G: nx.DiGraph, file_path: str | Path) -> None:
    elements = []
    for node, data in G.nodes(data=True):
        style = data.get("style", {})
        elements.append(
            {
                "id": data.get("id", str(node)),
                "label": data.get("label", str(node)),
                "text": data.get("text", ""),
                "domain": data.get("domain", ""),
                "measure": data.get("measure", ""),
                "display_layer": data.get("display_layer", ""),
                "member_count": data.get("member_count", 1),
                "members": data.get("members", []),
                "annotation": data.get("annotation", ""),
                "fillcolor": style.get("fillcolor", "white"),
                "line_color": style.get("line", {}).get("color", "gray"),
                "line_width": style.get("line", {}).get("width", 1.0),
            }
        )

    connections = []
    for src, dst in G.edges():
        connections.append(
            {
                "from": G.nodes[src].get("id", str(src)),
                "to": G.nodes[dst].get("id", str(dst)),
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
    *,
    pos: Optional[Dict[Any, Tuple[float, float]]] = None,
    title: str = "Calculation dependency graph",
    node_size: float = 46,
    icon_font_size: int = 18,
    show_hover: bool = True,
    show_annotation: bool = True,
    annotation_font_size: int = 10,
    annotation_y_shift: float = -0.9,
    domain_group_shapes: Optional[List[Dict[str, Any]]] = None,
) -> None:
    if len(G.nodes) == 0:
        raise ValueError("Graph is empty")

    if pos is None:
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
        line=dict(width=0.9, color="#888"),
        hoverinfo="none",
    )

    fig = go.Figure(data=[edge_trace])

    for node, data in G.nodes(data=True):
        x, y = pos[node]
        style = data.get("style", {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}})
        text = _clean(data.get("text")) or "•"
        annotation = _clean(data.get("annotation"))

        hover = "<br>".join(
            [
                f"<b>{_clean(data.get('label'))}</b>",
                f"layer: {_clean(data.get('display_layer'))}",
                f"domain: {_clean(data.get('domain'))}",
                f"measure: {_clean(data.get('measure'))}",
                f"members: {annotation}",
            ]
        )

        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text",
                text=[text],
                textposition="middle center",
                textfont=dict(size=icon_font_size),
                hovertext=[hover] if show_hover else None,
                hoverinfo="text" if show_hover else "skip",
                marker=dict(
                    size=node_size,
                    color=style.get("fillcolor", "white"),
                    line=dict(
                        color=style.get("line", {}).get("color", "gray"),
                        width=style.get("line", {}).get("width", 1.0),
                    ),
                ),
                showlegend=False,
            )
        )

        if show_annotation and annotation:
            fig.add_annotation(
                x=x,
                y=y + annotation_y_shift,
                text=annotation,
                showarrow=False,
                font=dict(size=annotation_font_size),
                align="center",
                xanchor="center",
                yanchor="top",
            )

    fig.update_layout(
        title=title,
        showlegend=False,
        hovermode="closest",
        margin=dict(b=20, l=20, r=20, t=40),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        shapes=domain_group_shapes or [],
    )
    fig.show()


if __name__ == "__main__":
    calc = SchemaCalcGraph("data/schemas/v1_11_4")

    G = calc.build_group_graph(
        include_isolated=True,
        merge_by=("display_layer", "domain", "measure"),
    )

    domain_palette = {
        "tool": "#8dd3c7",
        "declaration": "#ffffb3",
        "weather": "#bebada",
        "usage": "#fb8072",
        "heat_balance": "#80b1d3",
        "solar_gains": "#fdb462",
        "energy_end_use": "#b3de69",
        "energy_supply": "#fccde5",
        "lca": "#d9d9d9",
        "mobility": "#bc80bd",
    }

    calc.apply_domain_colors(
        G,
        palette=domain_palette,
        fallback="#eeeeee",
        color_fill=True,
        color_border=True,
        preserve_in_ka_fill=False,
    )

    pos = calc.layout_positions(
        G,
        dx=2.8,
        dy=7.0,
        domain_gap=2.2,
        wave_amp=0.6,
        wave_period=4.5,
    )

    shapes = calc.make_domain_group_shapes(
        G,
        pos,
        domain_palette=domain_palette,
        opacity=0.10,
        pad_x=0.8,
        pad_y=1.0,
    )

    export_graph_as_json(G, "calctree_grouped.json")
    draw_dependency_graph_interactive(
        G,
        pos=pos,
        title="Schema-based grouped calculation dependency graph",
        node_size=52,
        icon_font_size=18,
        show_annotation=True,
        annotation_font_size=10,
        annotation_y_shift=-1.05,
        domain_group_shapes=shapes,
    )
