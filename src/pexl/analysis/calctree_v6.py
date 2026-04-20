from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
from collections import deque
import json
import re

import networkx as nx
import pandas as pd
import plotly.graph_objects as go


# ============================================================
# Domain colors
# ============================================================

DEFAULT_DOMAIN_COLORS: Dict[str, str] = {
    "Battery": "#82f19a",
    "Construction": "#e083af",
    "Cooling": "#afa5f0",
    "DHW": "#fb8072",
    "Flexibility": "#b4eb4d",
    "GHG": "#9ad9ec",
    "Heating": "#b3de69",
    "Mobility": "#ffae00",
    "PV": "#28a523",
    "Solar Gains": "#f7ff85",
    "Space Use": "#ccebc5",
    "Thermal Hull": "#ffed6f",
    "Ventilation": "#aec7e8",
    "assessment": "#ffbb78",
    "comfort": "#98df8a",
    "declaration": "#ff9896",
    "district": "#c5b0d5",
    "electricity_dispatch": "#c49c94",
    "electricity_end_use": "#f7b6d2",
    "energy_dispatch": "#dbdb8d",
    "final_energy": "#9edae5",
    "geometry": "#c7c7c7",
    "heat_balance": "#6baed6",
    "lca": "#bdbdbd",
    "mobility": "#9e9ac8",
    "pe_import_export_balance": "#fd8d3c",
    "primary_energy": "#74c476",
    "primary_energy_balance": "#31a354",
    "primray_energy": "#756bb1",
    "project": "#969696",
    "tool": "#17becf",
    "usage": "#e377c2",
    "useful_energy": "#1f77b4",
    "weather": "#7f7f7f",
}


# ============================================================
# One unified anchoring system
# ============================================================

DEFAULT_LAYOUT = {
    "lanes": {
        "IN": (-12.0, 8.0),   # top
        "SIM": (0.0, 0.0),   # center
        "OUT": (12.0, -8.0), # bottom
    },
    "lane_x_span": {
        "IN": 24.0,
        "SIM": 28.0,
        "OUT": 24.0,
    },
    "domain_y_jitter": {
        "IN": 1.0,
        "SIM": 1.0,
        "OUT": 1.0,
    },
    "var_y_jitter": {
        "IN": 0.35,
        "SIM": 0.35,
        "OUT": 0.35,
    },
    "weights": {
        "node_to_var_anchor": 10.0,
        "var_anchor_to_domain_anchor": 14.0,
        "domain_anchor_to_lane_anchor": 22.0,
        "graph_edge": 1.5,
    },
    "spring": {
        "k": 1.2,
        "iterations": 300,
        "seed": 42,
    },
    "domain_shape": {
        "opacity": 0.08,
        "pad_x": 0.9,
        "pad_y": 0.8,
    },
}


# ============================================================
# Parsing helpers
# ============================================================

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
        return {"fillcolor": "white", "line": {"color": "red", "width": 1.5}}
    if ka_str == "1":
        return {"fillcolor": "#eaf7e7", "line": {"color": "green", "width": 1.0}}
    if ka_str == "2":
        return {"fillcolor": "#eaf7e7", "line": {"color": "green", "width": 3.0}}

    return {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}}


# ============================================================
# Model
# ============================================================

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
    def display_layer(self) -> str:
        if self.in_schema:
            return "IN"
        if self.sim_schema:
            return "SIM"
        if self.out_schema:
            return "OUT"
        return "OUT"

    def to_node_dict(self) -> Dict[str, Any]:
        data = asdict(self)
        data["source"] = self.source
        data["display_layer"] = self.display_layer
        data["style"] = (
            _ka_style(self.ka)
            if self.display_layer == "IN"
            else {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}}
        )
        return data


# ============================================================
# Core builder
# ============================================================

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

    def build_graph(self, include_isolated: bool = True) -> nx.DiGraph:
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

    def apply_domain_node_colors(
        self,
        G: nx.DiGraph,
        domain_colors: Dict[str, str],
        *,
        fallback: str = "#eeeeee",
        preserve_in_ka_fill: bool = False,
        preserve_in_ka_border: bool = True,
    ) -> nx.DiGraph:
        for _, data in G.nodes(data=True):
            domain = _clean(data.get("domain"))
            layer = _clean(data.get("display_layer"))
            style = data.get("style", {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}})
            color = domain_colors.get(domain, fallback)

            if not (preserve_in_ka_fill and layer == "IN"):
                style["fillcolor"] = color
            if not (preserve_in_ka_border and layer == "IN"):
                style["line"]["color"] = color

            data["style"] = style

        return G

    # --------------------------------------------------------
    # Surrounding graph
    # --------------------------------------------------------

    def _bfs_with_depth_limit(
        self,
        G: nx.DiGraph,
        start_node: str,
        *,
        direction: str,
        max_depth: int,
    ) -> Dict[str, int]:
        visited: Dict[str, int] = {start_node: 0}
        q = deque([(start_node, 0)])

        while q:
            node, depth = q.popleft()
            if depth >= max_depth:
                continue

            neighbors = G.predecessors(node) if direction == "pre" else G.successors(node)
            for nb in neighbors:
                if nb in visited:
                    continue
                visited[nb] = depth + 1
                q.append((nb, depth + 1))

        return visited

    def surrounding_subgraph(
        self,
        G: nx.DiGraph,
        var_name_keyword: str,
        *,
        pre: int = 5,
        post: int = 10,
    ) -> Tuple[nx.DiGraph, str]:
        matches = [n for n in G.nodes if var_name_keyword.lower() in n.lower()]
        if not matches:
            raise KeyError(f"No node found for keyword {var_name_keyword!r}")

        center = matches[0]

        pred_depths = self._bfs_with_depth_limit(G, center, direction="pre", max_depth=pre)
        succ_depths = self._bfs_with_depth_limit(G, center, direction="post", max_depth=post)

        keep = set(pred_depths) | set(succ_depths)
        SG = G.subgraph(keep).copy()

        for n in SG.nodes:
            if n == center:
                SG.nodes[n]["layout_lane"] = "SIM"
            elif n in pred_depths:
                SG.nodes[n]["layout_lane"] = "IN"
            elif n in succ_depths:
                SG.nodes[n]["layout_lane"] = "OUT"
            else:
                SG.nodes[n]["layout_lane"] = _clean(SG.nodes[n].get("display_layer")) or "OUT"

        return SG, center

    # --------------------------------------------------------
    # One unified anchor builder
    # --------------------------------------------------------

    def build_anchor_targets(
        self,
        G: nx.DiGraph,
        *,
        layout_cfg: Optional[Dict[str, Any]] = None,
    ) -> Tuple[Dict[str, Tuple[float, float]], Dict[str, str], Dict[str, str], Dict[str, str]]:
        cfg = layout_cfg or DEFAULT_LAYOUT

        fixed_anchor_pos: Dict[str, Tuple[float, float]] = {}
        node_to_var_anchor: Dict[str, str] = {}
        var_anchor_to_domain_anchor: Dict[str, str] = {}
        domain_anchor_to_lane_anchor: Dict[str, str] = {}

        lane_nodes: Dict[str, List[str]] = {"IN": [], "SIM": [], "OUT": []}
        for n, data in G.nodes(data=True):
            lane = _clean(data.get("layout_lane")) or _clean(data.get("display_layer")) or "OUT"
            lane_nodes.setdefault(lane, []).append(n)

        for lane in ["IN", "SIM", "OUT"]:
            nodes_here = lane_nodes.get(lane, [])
            if not nodes_here:
                continue

            lane_x, lane_y = cfg["lanes"][lane]
            lane_anchor = f"anchor_lane::{lane}"
            fixed_anchor_pos[lane_anchor] = (lane_x, lane_y)

            domains_here = []
            for n in nodes_here:
                d = _clean(G.nodes[n].get("domain"))
                if d not in domains_here:
                    domains_here.append(d)

            domains_here.sort(key=lambda d: (self._domain_rank(d), d))

            if len(domains_here) == 1:
                domain_xs = {domains_here[0]: lane_x}
            else:
                x0 = lane_x - cfg["lane_x_span"][lane] / 2
                step = cfg["lane_x_span"][lane] / max(len(domains_here) - 1, 1)
                domain_xs = {d: x0 + i * step for i, d in enumerate(domains_here)}

            for d_idx, domain in enumerate(domains_here):
                domain_anchor = f"anchor_domain::{lane}::{domain}"
                dx = domain_xs[domain]
                dy = lane_y + cfg["domain_y_jitter"][lane] * ((d_idx % 3) - 1)
                fixed_anchor_pos[domain_anchor] = (dx, dy)
                domain_anchor_to_lane_anchor[domain_anchor] = lane_anchor

                vars_here = [n for n in nodes_here if _clean(G.nodes[n].get("domain")) == domain]
                vars_here.sort(key=lambda n: (self.records[n].schema_order if n in self.records else 10**9, n))

                if len(vars_here) == 1:
                    var_xs = {vars_here[0]: dx}
                else:
                    var_span = max(1.8, min(12.0, 1.1 * len(vars_here)))
                    vx0 = dx - var_span / 2
                    vstep = var_span / max(len(vars_here) - 1, 1)
                    var_xs = {n: vx0 + i * vstep for i, n in enumerate(vars_here)}

                for v_idx, n in enumerate(vars_here):
                    var_anchor = f"anchor_var::{lane}::{domain}::{n}"
                    vx = var_xs[n]
                    vy = dy + cfg["var_y_jitter"][lane] * ((v_idx % 3) - 1)
                    fixed_anchor_pos[var_anchor] = (vx, vy)
                    var_anchor_to_domain_anchor[var_anchor] = domain_anchor
                    node_to_var_anchor[n] = var_anchor

        return fixed_anchor_pos, node_to_var_anchor, var_anchor_to_domain_anchor, domain_anchor_to_lane_anchor

    def anchored_spring_positions(
        self,
        G: nx.DiGraph,
        *,
        fixed_anchor_pos: Dict[str, Tuple[float, float]],
        node_to_var_anchor: Dict[str, str],
        var_anchor_to_domain_anchor: Dict[str, str],
        domain_anchor_to_lane_anchor: Dict[str, str],
        layout_cfg: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Tuple[float, float]]:
        cfg = layout_cfg or DEFAULT_LAYOUT
        weights = cfg["weights"]
        spring_cfg = cfg["spring"]

        AG = nx.Graph()

        for n, data in G.nodes(data=True):
            AG.add_node(n, **data)

        for src, dst in G.edges():
            AG.add_edge(src, dst, weight=weights["graph_edge"])

        for anchor_name, xy in fixed_anchor_pos.items():
            AG.add_node(anchor_name, is_anchor=True, anchor_pos=xy)

        for n, anchor in node_to_var_anchor.items():
            AG.add_edge(n, anchor, weight=weights["node_to_var_anchor"])

        for var_anchor, domain_anchor in var_anchor_to_domain_anchor.items():
            AG.add_edge(var_anchor, domain_anchor, weight=weights["var_anchor_to_domain_anchor"])

        for domain_anchor, lane_anchor in domain_anchor_to_lane_anchor.items():
            AG.add_edge(domain_anchor, lane_anchor, weight=weights["domain_anchor_to_lane_anchor"])

        pos_init = {name: xy for name, xy in fixed_anchor_pos.items()}
        fixed_nodes = list(fixed_anchor_pos.keys())

        pos = nx.spring_layout(
            AG,
            pos=pos_init,
            fixed=fixed_nodes,
            seed=spring_cfg["seed"],
            k=spring_cfg["k"],
            iterations=spring_cfg["iterations"],
            weight="weight",
        )

        return {n: pos[n] for n in G.nodes if n in pos}

    def make_domain_shapes(
        self,
        G: nx.DiGraph,
        pos: Dict[str, Tuple[float, float]],
        *,
        domain_colors: Optional[Dict[str, str]] = None,
        layout_cfg: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        cfg = layout_cfg or DEFAULT_LAYOUT
        shape_cfg = cfg["domain_shape"]

        grouped: Dict[Tuple[str, str], List[str]] = {}
        for n, data in G.nodes(data=True):
            lane = _clean(data.get("layout_lane")) or _clean(data.get("display_layer")) or "OUT"
            domain = _clean(data.get("domain"))
            grouped.setdefault((lane, domain), []).append(n)

        shapes: List[Dict[str, Any]] = []
        for (_, domain), nodes in grouped.items():
            xs = [pos[n][0] for n in nodes if n in pos]
            ys = [pos[n][1] for n in nodes if n in pos]
            if not xs or not ys:
                continue

            color = (domain_colors or {}).get(domain, "#bbbbbb")
            shapes.append(
                dict(
                    type="rect",
                    xref="x",
                    yref="y",
                    x0=min(xs) - shape_cfg["pad_x"],
                    x1=max(xs) + shape_cfg["pad_x"],
                    y0=min(ys) - shape_cfg["pad_y"],
                    y1=max(ys) + shape_cfg["pad_y"],
                    line=dict(color=color, width=1.0),
                    fillcolor=color,
                    opacity=shape_cfg["opacity"],
                    layer="below",
                )
            )
        return shapes


# ============================================================
# Rendering
# ============================================================

def draw_graph(
    G: nx.DiGraph,
    *,
    pos: Dict[str, Tuple[float, float]],
    domain_colors: Optional[Dict[str, str]] = None,
    title: str = "Calculation graph",
    node_size: float = 28,
    icon_font_size: int = 16,
    show_icons: bool = True,
    show_domain_shapes: bool = True,
    domain_shapes: Optional[List[Dict[str, Any]]] = None,
    edge_color_mode: str = "source_domain",
    edge_default_color: str = "#888888",
    scroll_zoom: bool = True,
) -> None:
    fig = go.Figure()
    arrow_annotations = []

    for src, dst in G.edges():
        x0, y0 = pos[src]
        x1, y1 = pos[dst]

        if edge_color_mode == "source_domain":
            edge_color = (domain_colors or {}).get(_clean(G.nodes[src].get("domain")), edge_default_color)
        elif edge_color_mode == "target_domain":
            edge_color = (domain_colors or {}).get(_clean(G.nodes[dst].get("domain")), edge_default_color)
        else:
            edge_color = edge_default_color

        fig.add_trace(
            go.Scatter(
                x=[x0, x1, None],
                y=[y0, y1, None],
                mode="lines",
                line=dict(width=1.0, color=edge_color),
                hoverinfo="none",
                showlegend=False,
            )
        )
        arrow_annotations.append(
            dict(
                x=x1,
                y=y1,
                ax=x0,
                ay=y0,
                xref="x",
                yref="y",
                axref="x",
                ayref="y",
                showarrow=True,
                arrowhead=2,
                arrowsize=1.2,
                arrowwidth=1.0,
                arrowcolor=edge_color,
                standoff=8,
            )
        )

    for node, data in G.nodes(data=True):
        x, y = pos[node]
        style = data.get("style", {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}})
        icon_text = _clean(data.get("icon")) if show_icons else ""

        hover_lines = [
            f"<b>{node}</b>",
            f"domain: {_clean(data.get('domain'))}",
            f"measure: {_clean(data.get('measure'))}",
            f"layer: {_clean(data.get('display_layer'))}",
            f"source: {_clean(data.get('source'))}",
            f"ka: {_clean(data.get('ka'))}",
            f"label_de: {_clean(data.get('label_de'))}",
            f"unit: {_clean(data.get('unit'))}",
            f"comment: {_clean(data.get('comment'))}",
            f"spatial_scope: {_clean(data.get('spatial_scope'))}",
            f"temporal_scope: {_clean(data.get('temporal_scope'))}",
            f"entity_group: {_clean(data.get('entity_group'))}",
            f"entity_key: {_clean(data.get('entity_key'))}",
            f"formula: {_clean(data.get('formula'))}",
        ]

        fig.add_trace(
            go.Scatter(
                x=[x],
                y=[y],
                mode="markers+text" if show_icons else "markers",
                text=[icon_text] if show_icons else None,
                textposition="middle center",
                textfont=dict(size=icon_font_size),
                hovertext=["<br>".join(hover_lines)],
                hoverinfo="text",
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

    fig.update_layout(
        title=title,
        showlegend=False,
        hovermode="closest",
        margin=dict(b=20, l=20, r=20, t=40),
        xaxis=dict(showgrid=False, zeroline=False, visible=False),
        yaxis=dict(showgrid=False, zeroline=False, visible=False),
        shapes=domain_shapes if show_domain_shapes else [],
        annotations=arrow_annotations,
    )
    fig.show(config={"scrollZoom": scroll_zoom})


# ============================================================
# Export
# ============================================================

def export_graph_as_json(G: nx.DiGraph, file_path: str | Path) -> None:
    elements = []
    for node, data in G.nodes(data=True):
        style = data.get("style", {})
        elements.append(
            {
                "id": node,
                "var_name": node,
                "domain": data.get("domain", data.get("Domain","")),
                "measure": data.get("measure", data.get("Measure","")),
                "display_layer": data.get("display_layer", ""),
                "source": data.get("source", ""),
                "ka": data.get("ka", ""),
                "icon": data.get("icon", ""),
                "label_de": data.get("label_de", ""),
                "unit": data.get("unit", ""),
                "comment": data.get("comment", ""),
                "formula": data.get("formula", ""),
                "fillcolor": style.get("fillcolor", "white"),
                "line_color": style.get("line", {}).get("color", "gray"),
                "line_width": style.get("line", {}).get("width", 1.0),
            }
        )

    connections = [{"from": src, "to": dst, "direction": "directed"} for src, dst in G.edges()]

    payload = {
        "elements": elements,
        "connections": connections,
    }

    Path(file_path).write_text(
        json.dumps(payload, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )


# ============================================================
# Entry points
# ============================================================

def show_all(
    schema_dir: str | Path = "data/schemas/1_11_4",
    *,
    include_isolated: bool = True,
    domain_colors: Optional[Dict[str, str]] = None,
    layout_cfg: Optional[Dict[str, Any]] = None,
    node_size: float = 28,
    icon_font_size: int = 16,
    show_icons: bool = True,
    show_domain_shapes: bool = True,
) -> Tuple[SchemaCalcGraph, nx.DiGraph]:
    calc = SchemaCalcGraph(schema_dir)
    colors = domain_colors or DEFAULT_DOMAIN_COLORS
    cfg = layout_cfg or DEFAULT_LAYOUT

    G = calc.build_graph(include_isolated=include_isolated)
    calc.apply_domain_node_colors(
        G,
        domain_colors=colors,
        preserve_in_ka_fill=False,
        preserve_in_ka_border=True,
    )

    fixed_anchor_pos, node_to_var_anchor, var_anchor_to_domain_anchor, domain_anchor_to_lane_anchor = (
        calc.build_anchor_targets(G, layout_cfg=cfg)
    )

    pos = calc.anchored_spring_positions(
        G,
        fixed_anchor_pos=fixed_anchor_pos,
        node_to_var_anchor=node_to_var_anchor,
        var_anchor_to_domain_anchor=var_anchor_to_domain_anchor,
        domain_anchor_to_lane_anchor=domain_anchor_to_lane_anchor,
        layout_cfg=cfg,
    )

    shapes = calc.make_domain_shapes(G, pos, domain_colors=colors, layout_cfg=cfg)

    draw_graph(
        G,
        pos=pos,
        domain_colors=colors,
        title="Calculation graph",
        node_size=node_size,
        icon_font_size=icon_font_size,
        show_icons=show_icons,
        show_domain_shapes=show_domain_shapes,
        domain_shapes=shapes,
        edge_color_mode="source_domain",
        scroll_zoom=True,
    )

    return calc, G


def show_surrounding(
    schema_dir: str | Path = "data/schemas/1_11_4",
    var_name_keyword: str = "",
    *,
    pre: int = 5,
    post: int = 10,
    include_isolated: bool = True,
    domain_colors: Optional[Dict[str, str]] = None,
    layout_cfg: Optional[Dict[str, Any]] = None,
    node_size: float = 30,
    icon_font_size: int = 16,
    show_icons: bool = True,
    show_domain_shapes: bool = False,
) -> Tuple[SchemaCalcGraph, nx.DiGraph, str]:
    calc = SchemaCalcGraph(schema_dir)
    colors = domain_colors or DEFAULT_DOMAIN_COLORS
    cfg = layout_cfg or DEFAULT_LAYOUT

    G = calc.build_graph(include_isolated=include_isolated)
    calc.apply_domain_node_colors(
        G,
        domain_colors=colors,
        preserve_in_ka_fill=False,
        preserve_in_ka_border=True,
    )

    SG, center = calc.surrounding_subgraph(G, var_name_keyword, pre=pre, post=post)

    fixed_anchor_pos, node_to_var_anchor, var_anchor_to_domain_anchor, domain_anchor_to_lane_anchor = (
        calc.build_anchor_targets(SG, layout_cfg=cfg)
    )

    pos = calc.anchored_spring_positions(
        SG,
        fixed_anchor_pos=fixed_anchor_pos,
        node_to_var_anchor=node_to_var_anchor,
        var_anchor_to_domain_anchor=var_anchor_to_domain_anchor,
        domain_anchor_to_lane_anchor=domain_anchor_to_lane_anchor,
        layout_cfg=cfg,
    )

    shapes = calc.make_domain_shapes(SG, pos, domain_colors=colors, layout_cfg=cfg)

    draw_graph(
        SG,
        pos=pos,
        domain_colors=colors,
        title=f"Surrounding graph for: {var_name_keyword}",
        node_size=node_size,
        icon_font_size=icon_font_size,
        show_icons=show_icons,
        show_domain_shapes=show_domain_shapes,
        domain_shapes=shapes,
        edge_color_mode="source_domain",
        scroll_zoom=True,
    )

    return calc, SG, center


# ============================================================
# Example
# ============================================================

if __name__ == "__main__":
    show_all(
        "data/schemas/v1_11_4",
        include_isolated=True,
        show_icons=True,
        show_domain_shapes=True,
    )

    # show_surrounding(
    #     "data/schemas/v1_11_4",
    #     var_name_keyword="UED_heating",
    #     pre=5,
    #     post=5,
    #     include_isolated=True,
    #     show_icons=True,
    #     show_domain_shapes=False,
    # )