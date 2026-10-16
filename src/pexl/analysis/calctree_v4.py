from __future__ import annotations

from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Set, Tuple
from collections import deque
import json
import math
import re

import networkx as nx
import pandas as pd
import plotly.graph_objects as go


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

DEFAULT_LAYER_LAYOUT = {
    "IN": {"y": 0.0, "dx": 3.0, "domain_gap": 2.2, "wave_amp": 0.35, "wave_period": 4.8, "wave_phase": 0.0},
    "SIM": {"y": -7.5, "dx": 2.0, "domain_gap": 1.6, "wave_amp": 0.55, "wave_period": 3.2, "wave_phase": 0.8},
    "OUT": {"y": -14.5, "dx": 3.0, "domain_gap": 2.2, "wave_amp": 0.35, "wave_period": 4.8, "wave_phase": 1.6},
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
        collapse_in: bool = True,
        collapse_sim: bool = False,
        collapse_out: bool = True,
        merge_fields: Tuple[str, ...] = ("domain", "measure"),
        sim_label_mode: str = "var_name",   # "var_name" | "schema"
        sim_annotation_mode: str = "formula",  # "formula" | "var_name_and_formula"
    ) -> nx.DiGraph:
        VG = self.build_variable_graph(include_isolated=include_isolated)
        GG = nx.DiGraph()

        def get_group_key(node_data: Dict[str, Any], var_name: str) -> Tuple[str, ...]:
            layer = _clean(node_data.get("display_layer"))
            collapse = {
                "IN": collapse_in,
                "SIM": collapse_sim,
                "OUT": collapse_out,
            }.get(layer, True)

            if not collapse:
                return (layer, "__VAR__", var_name)

            parts = [layer]
            for field in merge_fields:
                parts.append(_clean(node_data.get(field)))
            return tuple(parts)

        group_members: Dict[Tuple[str, ...], List[str]] = {}
        for var_name, data in VG.nodes(data=True):
            gkey = get_group_key(data, var_name)
            group_members.setdefault(gkey, []).append(var_name)

        for gkey, members in group_members.items():
            members_sorted = sorted(members, key=lambda n: self.records[n].schema_order)
            first = members_sorted[0]
            first_data = VG.nodes[first]

            layer = _clean(first_data.get("display_layer"))
            domain = _clean(first_data.get("domain"))
            measure = _clean(first_data.get("measure"))

            icons: List[str] = []
            for m in members_sorted:
                icon = _clean(VG.nodes[m].get("icon"))
                if icon and icon not in icons:
                    icons.append(icon)

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

            if layer == "SIM":
                if sim_label_mode == "var_name" and len(members_sorted) == 1:
                    label = first
                else:
                    label = " | ".join([part for part in [domain, measure] if part]) or first

                formulas: List[str] = []
                for m in members_sorted:
                    f = _clean(VG.nodes[m].get("formula"))
                    if not f:
                        continue
                    if sim_annotation_mode == "var_name_and_formula" and len(members_sorted) > 1:
                        formulas.append(f"{m}: {f}")
                    else:
                        formulas.append(f)

                annotation = "<br>".join(formulas)
            else:
                label = " | ".join([part for part in [domain, measure] if part]) or first
                annotation = ""

            GG.add_node(
                gkey,
                id="|".join(gkey),
                display_layer=layer,
                domain=domain,
                measure=measure,
                label=label,
                text=display_text,
                style=style,
                source_tags=sorted({_clean(VG.nodes[m].get("source")) for m in members_sorted if _clean(VG.nodes[m].get("source"))}),
                members=members_sorted,
                member_count=len(members_sorted),
                schema_order=min(self.records[m].schema_order for m in members_sorted),
                annotation=annotation,
                icon_text=display_text,
            )

        for src, dst in VG.edges():
            src_g = get_group_key(VG.nodes[src], src)
            dst_g = get_group_key(VG.nodes[dst], dst)
            if src_g != dst_g:
                GG.add_edge(src_g, dst_g)

        return GG

    def apply_domain_node_colors(
        self,
        G: nx.DiGraph,
        domain_colors: Dict[str, str],
        *,
        fallback: str = "#eeeeee",
        color_fill: bool = True,
        color_border: bool = True,
        preserve_in_ka_fill: bool = False,
        preserve_in_ka_border: bool = False,
    ) -> nx.DiGraph:
        for _, data in G.nodes(data=True):
            domain = _clean(data.get("domain"))
            layer = _clean(data.get("display_layer"))
            style = data.get("style", {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}})
            color = domain_colors.get(domain, fallback)

            if color_fill and not (preserve_in_ka_fill and layer == "IN"):
                style["fillcolor"] = color
            if color_border and not (preserve_in_ka_border and layer == "IN"):
                style["line"]["color"] = color

            data["style"] = style

        return G

    def build_layered_positions(
        self,
        G: nx.DiGraph,
        *,
        layout: Optional[Dict[str, Dict[str, float]]] = None,
    ) -> Dict[Any, Tuple[float, float]]:
        cfg = layout or DEFAULT_LAYER_LAYOUT
        buckets: Dict[str, Dict[str, List[Any]]] = {"IN": {}, "SIM": {}, "OUT": {}}

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

        for layer_name in ["IN", "SIM", "OUT"]:
            layer_cfg = cfg[layer_name]
            x = 0.0
            y0 = float(layer_cfg["y"])
            dx = float(layer_cfg["dx"])
            domain_gap = float(layer_cfg["domain_gap"])
            wave_amp = float(layer_cfg["wave_amp"])
            wave_period = float(layer_cfg["wave_period"])
            wave_phase = float(layer_cfg["wave_phase"])

            domains_in_layer = sorted(
                buckets[layer_name].keys(),
                key=lambda d: (self._domain_rank("" if d == "__NO_DOMAIN__" else d), d),
            )

            for domain in domains_in_layer:
                nodes = buckets[layer_name][domain]
                for node in nodes:
                    y = y0 + wave_amp * math.sin((x / wave_period) + wave_phase)
                    pos[node] = (x, y)
                    x += dx
                x += domain_gap

        return pos

    def make_domain_group_shapes(
        self,
        G: nx.DiGraph,
        pos: Dict[Any, Tuple[float, float]],
        *,
        domain_colors: Optional[Dict[str, str]] = None,
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
            color = (domain_colors or {}).get(domain, "#bbbbbb")
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

    def _bfs_with_depth_limit(
        self,
        G: nx.DiGraph,
        start_node: Any,
        *,
        direction: str,
        max_depth: int,
    ) -> Dict[Any, int]:
        visited: Dict[Any, int] = {start_node: 0}
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
    ) -> Tuple[nx.DiGraph, Any]:
        matches = [n for n, d in G.nodes(data=True) if var_name_keyword.lower() in " ".join(d.get("members", [])).lower()]
        if not matches:
            matches = [n for n, d in G.nodes(data=True) if var_name_keyword.lower() in _clean(d.get("label")).lower()]
        if not matches:
            raise KeyError(f"No node found for keyword {var_name_keyword!r}")

        center = matches[0]

        pred_depths = self._bfs_with_depth_limit(G, center, direction="pre", max_depth=pre)
        succ_depths = self._bfs_with_depth_limit(G, center, direction="post", max_depth=post)

        keep = set(pred_depths) | set(succ_depths)
        SG = G.subgraph(keep).copy()

        for n in SG.nodes:
            if n == center:
                SG.nodes[n]["surround_role"] = "center"
                SG.nodes[n]["surround_depth"] = 0
            elif n in pred_depths:
                SG.nodes[n]["surround_role"] = "pre"
                SG.nodes[n]["surround_depth"] = pred_depths[n]
            elif n in succ_depths:
                SG.nodes[n]["surround_role"] = "post"
                SG.nodes[n]["surround_depth"] = succ_depths[n]
            else:
                SG.nodes[n]["surround_role"] = "other"
                SG.nodes[n]["surround_depth"] = 0

        return SG, center

    def surrounding_positions(
        self,
        G: nx.DiGraph,
        *,
        center_node: Any,
        seed: int = 42,
        k: float = 0.9,
        iterations: int = 200,
        pre_y: float = 3.0,
        center_y: float = 0.0,
        post_y: float = -3.0,
        jitter_scale: float = 0.8,
    ) -> Dict[Any, Tuple[float, float]]:
        init_pos: Dict[Any, Tuple[float, float]] = {}

        for i, n in enumerate(G.nodes):
            role = _clean(G.nodes[n].get("surround_role"))
            depth = float(G.nodes[n].get("surround_depth", 0))

            x0 = (i % 7) * jitter_scale
            if role == "pre":
                y0 = pre_y - 0.45 * depth
            elif role == "post":
                y0 = post_y + 0.45 * depth
            else:
                y0 = center_y

            init_pos[n] = (x0, y0)

        spring_pos = nx.spring_layout(
            G,
            pos=init_pos,
            seed=seed,
            k=k,
            iterations=iterations,
        )

        final_pos: Dict[Any, Tuple[float, float]] = {}
        for n, (x, y) in spring_pos.items():
            role = _clean(G.nodes[n].get("surround_role"))
            depth = float(G.nodes[n].get("surround_depth", 0))

            if n == center_node:
                final_pos[n] = (x, center_y)
            elif role == "pre":
                final_pos[n] = (x, abs(y) + pre_y + 0.15 * depth)
            elif role == "post":
                final_pos[n] = (x, -abs(y) + post_y - 0.15 * depth)
            else:
                final_pos[n] = (x, y)

        return final_pos


def draw_dependency_graph_interactive(
    G: nx.DiGraph,
    *,
    pos: Optional[Dict[Any, Tuple[float, float]]] = None,
    title: str = "Calculation dependency graph",
    node_size: float = 46,
    icon_font_size: int = 18,
    show_hover: bool = True,
    show_annotation: bool = False,
    annotation_font_size: int = 10,
    annotation_y_shift: float = -1.1,
    show_icons: bool = True,
    show_labels: bool = False,
    label_font_size: int = 10,
    label_y_shift: float = 0.95,
    domain_group_shapes: Optional[List[Dict[str, Any]]] = None,
    edge_color_mode: str = "source_domain",
    edge_default_color: str = "#888888",
    domain_colors: Optional[Dict[str, str]] = None,
    scroll_zoom: bool = True,
) -> None:
    if len(G.nodes) == 0:
        raise ValueError("Graph is empty")

    if pos is None:
        pos = nx.spring_layout(G, k=0.35, iterations=100, seed=42)

    fig = go.Figure()

    for src, dst in G.edges():
        x0, y0 = pos[src]
        x1, y1 = pos[dst]

        if edge_color_mode == "source_domain":
            src_domain = _clean(G.nodes[src].get("domain"))
            edge_color = (domain_colors or {}).get(src_domain, edge_default_color)
        elif edge_color_mode == "target_domain":
            dst_domain = _clean(G.nodes[dst].get("domain"))
            edge_color = (domain_colors or {}).get(dst_domain, edge_default_color)
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

    for node, data in G.nodes(data=True):
        x, y = pos[node]
        style = data.get("style", {"fillcolor": "white", "line": {"color": "gray", "width": 1.0}})
        icon_text = _clean(data.get("icon_text")) or _clean(data.get("text")) or "•"
        annotation = _clean(data.get("annotation"))
        label = _clean(data.get("label"))

        hover = "<br>".join(
            [
                f"<b>{label}</b>",
                f"layer: {_clean(data.get('display_layer'))}",
                f"domain: {_clean(data.get('domain'))}",
                f"measure: {_clean(data.get('measure'))}",
                f"members: {', '.join(data.get('members', []))}",
            ]
        )

        trace_kwargs = dict(
            x=[x],
            y=[y],
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

        if show_icons:
            fig.add_trace(
                go.Scatter(
                    mode="markers+text",
                    text=[icon_text],
                    textposition="middle center",
                    textfont=dict(size=icon_font_size),
                    **trace_kwargs,
                )
            )
        else:
            fig.add_trace(go.Scatter(mode="markers", **trace_kwargs))

        if show_labels and label:
            fig.add_annotation(
                x=x,
                y=y + label_y_shift,
                text=label,
                showarrow=False,
                font=dict(size=label_font_size),
                align="center",
                xanchor="center",
                yanchor="bottom",
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
    fig.show(config={"scrollZoom": scroll_zoom})


def export_graph_as_json(G: nx.DiGraph, file_path: str | Path) -> None:
    elements = []
    for node, data in G.nodes(data=True):
        style = data.get("style", {})
        elements.append(
            {
                "id": data.get("id", str(node)),
                "label": data.get("label", str(node)),
                "text": data.get("text", ""),
                "icon_text": data.get("icon_text", ""),
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


def show_all(
    schema_dir: str | Path,
    *,
    include_isolated: bool = True,
    collapse_in: bool = True,
    collapse_sim: bool = False,
    collapse_out: bool = True,
    sim_label_mode: str = "var_name",
    sim_annotation_mode: str = "formula",
    domain_colors: Optional[Dict[str, str]] = None,
    layer_layout: Optional[Dict[str, Dict[str, float]]] = None,
    node_size: float = 30,
    icon_font_size: int = 18,
    show_icons: bool = True,
    show_labels: bool = True,
    show_annotation: bool = True,
) -> Tuple[SchemaCalcGraph, nx.DiGraph]:
    calc = SchemaCalcGraph(schema_dir)
    colors = domain_colors or DEFAULT_DOMAIN_COLORS

    G = calc.build_group_graph(
        include_isolated=include_isolated,
        collapse_in=collapse_in,
        collapse_sim=collapse_sim,
        collapse_out=collapse_out,
        merge_fields=("domain", "measure"),
        sim_label_mode=sim_label_mode,
        sim_annotation_mode=sim_annotation_mode,
    )

    calc.apply_domain_node_colors(
        G,
        domain_colors=colors,
        fallback="#eeeeee",
        color_fill=True,
        color_border=True,
        preserve_in_ka_fill=False,
        preserve_in_ka_border=False,
    )

    pos = calc.build_layered_positions(G, layout=layer_layout or DEFAULT_LAYER_LAYOUT)
    shapes = calc.make_domain_group_shapes(G, pos, domain_colors=colors, opacity=0.10, pad_x=0.75, pad_y=0.95)

    draw_dependency_graph_interactive(
        G,
        pos=pos,
        title="Schema-based grouped calculation dependency graph",
        node_size=node_size,
        icon_font_size=icon_font_size,
        show_icons=show_icons,
        show_labels=show_labels,
        show_annotation=show_annotation,
        annotation_font_size=9,
        annotation_y_shift=-1.1,
        label_font_size=10,
        label_y_shift=0.95,
        domain_group_shapes=shapes,
        edge_color_mode="source_domain",
        edge_default_color="#999999",
        domain_colors=colors,
        scroll_zoom=True,
    )

    return calc, G


def show_surrounding(
    schema_dir: str | Path,
    var_name_keyword: str,
    *,
    pre: int = 5,
    post: int = 10,
    include_isolated: bool = True,
    collapse_in: bool = True,
    collapse_sim: bool = False,
    collapse_out: bool = True,
    sim_label_mode: str = "var_name",
    sim_annotation_mode: str = "formula",
    domain_colors: Optional[Dict[str, str]] = None,
    node_size: float = 34,
    icon_font_size: int = 18,
    show_icons: bool = True,
    show_labels: bool = True,
    show_annotation: bool = False,
) -> Tuple[SchemaCalcGraph, nx.DiGraph, Any]:
    calc = SchemaCalcGraph(schema_dir)
    colors = domain_colors or DEFAULT_DOMAIN_COLORS

    G = calc.build_group_graph(
        include_isolated=include_isolated,
        collapse_in=collapse_in,
        collapse_sim=collapse_sim,
        collapse_out=collapse_out,
        merge_fields=("domain", "measure"),
        sim_label_mode=sim_label_mode,
        sim_annotation_mode=sim_annotation_mode,
    )

    calc.apply_domain_node_colors(
        G,
        domain_colors=colors,
        fallback="#eeeeee",
        color_fill=True,
        color_border=True,
        preserve_in_ka_fill=False,
        preserve_in_ka_border=False,
    )

    SG, center = calc.surrounding_subgraph(G, var_name_keyword, pre=pre, post=post)
    pos = calc.surrounding_positions(
        SG,
        center_node=center,
        seed=42,
        k=0.95,
        iterations=250,
        pre_y=3.8,
        center_y=0.0,
        post_y=-3.8,
        jitter_scale=0.9,
    )

    draw_dependency_graph_interactive(
        SG,
        pos=pos,
        title=f"Surrounding graph for: {var_name_keyword}",
        node_size=node_size,
        icon_font_size=icon_font_size,
        show_icons=show_icons,
        show_labels=show_labels,
        show_annotation=show_annotation,
        annotation_font_size=9,
        annotation_y_shift=-1.1,
        label_font_size=10,
        label_y_shift=0.95,
        domain_group_shapes=None,
        edge_color_mode="source_domain",
        edge_default_color="#999999",
        domain_colors=colors,
        scroll_zoom=True,
    )

    return calc, SG, center


if __name__ == "__main__":
    # show_all(
    #     "data/schemas/v1_11_4",
    #     collapse_in=True,
    #     collapse_sim=False,
    #     collapse_out=True,
    #     sim_label_mode="var_name",
    #     sim_annotation_mode="formula",
    #     show_icons=True,
    #     show_labels=True,
    #     show_annotation=True,
    # )

    #example:
    show_surrounding(
        "data/schemas/v1_11_4",
        var_name_keyword="UED_heating",
        pre=15,
        post=10,
        collapse_in=False,
        collapse_sim=False,
        collapse_out=False,
        sim_label_mode="var_name",
        sim_annotation_mode="formula",
    )