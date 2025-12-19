from typing import Dict, List, Optional
from numpy import NaN
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import re

import excel


class Node:
    def __init__(self, name, parents, label, color, meta):
        self.name = name
        self.label = label
        self.parents = parents
        self.color = color
        self.meta = meta


class CalcTree:
    def __init__(self, project: excel.Project, sim2_path=None):
        self.project = project
        self.sim2_df = (
            pd.read_excel(sim2_path, sheet_name="SIM2") if sim2_path else None
        )
        self.all_vars = self._build_all_variables()

    def _build_all_variables(self) -> Dict[str, Dict]:
        """Build a filtered dictionary of all scoped variables across IN, OUT, and SIM2."""
        all_vars = {}

        def is_valid_var(meta: dict) -> bool:
            var_name = str(meta.get("var_name", "")).strip()
            name = str(meta.get("Name", "")).strip()

            return (
                var_name
                and not var_name.lower().startswith("spalte")
                and not var_name is NaN
                # and var_name == name
            )

        # IN variables
        for var_name, meta in self.project.inputs.items():
            if not is_valid_var(meta):
                continue
            key = f"IN:{var_name}"
            all_vars[key] = meta

        # OUT variables
        for var_name, meta in self.project.outputs.items():
            if not is_valid_var(meta):
                continue
            key = f"OUT:{var_name}"
            all_vars[key] = meta

        # SIM2 (from DataFrame)
        if self.sim2_df is not None:
            for col in self.sim2_df.columns:
                if (
                    not col
                    or str(col).lower() == "h"
                    or str(col).lower().startswith("spalte")
                ):
                    continue
                all_vars[f"SIM2:{col}"] = {
                    "var_name": col,
                    "sheet": "SIM2",
                    "formula": (
                        str(self.sim2_df[col].iloc[0])
                        if str(self.sim2_df[col].iloc[0]).startswith("=")
                        else ""
                    ),
                    "label": col,
                }

        return all_vars


def parse_formula(formula) -> list:
    references = []
    # regex formula
    # match sim name: [@[name]]
    # match


def resolve_formula_refs(
    formula: str, sheet_name: str, in_df=None, all_vars=None
) -> List[str]:
    """
    Extract referenced variable keys from a formula string.
    Returns fully scoped keys like 'IN:Qh', 'SIM2:NFA_total', etc.
    """
    refs = set()

    # 1. Structured reference [@[var_name]]
    structured_refs = re.findall(r"\[\@\[(.*?)\]\]", formula)
    for ref in structured_refs:
        for sheet in ["IN", "SIM2", "OUT"]:
            key = f"{sheet}:{ref}"
            if all_vars and key in all_vars:
                refs.add(key)
                break

    # 2. Excel-style cell refs
    cell_refs = re.findall(r"\b([A-Z]{1,3})(\d{1,5})\b", formula)
    if sheet_name == "IN" and in_df is not None:
        for col_letter, row_str in cell_refs:
            try:
                row_idx = int(row_str) - 2  # adjust for header
                col_idx = col_letter_to_index(col_letter)
                var_name = in_df.iloc[row_idx]["var_name"]
                if pd.notna(var_name):
                    refs.add(f"IN:{str(var_name)}")
            except Exception:
                continue

    # 3. Named variables in all_vars
    if all_vars:
        for full_key in all_vars.keys():
            _, name = full_key.split(":", 1)
            if name in formula:
                refs.add(full_key)

    return list(refs)


def col_letter_to_index(col: str) -> int:
    """Convert Excel column letter to 0-based index (e.g., A -> 0, Z -> 25, AA -> 26)"""
    exp = 0
    col = col.upper()
    col_num = 0
    for char in reversed(col):
        col_num += (ord(char) - ord("A") + 1) * (26**exp)
        exp += 1
    return col_num - 1  # zero-indexed


def build_dependency_graph(calc_tree: CalcTree) -> nx.DiGraph:
    G = nx.DiGraph()
    all_vars = calc_tree.all_vars
    in_df = calc_tree.project.df_in

    for key, meta in all_vars.items():
        sheet, var_name = key.split(":", 1)
        label = meta.get("Name") or meta.get("label") or var_name
        formula = meta.get("Formel") or meta.get("formula", "")
        color = {"IN": "cornflowerblue", "SIM2": "lightgreen", "OUT": "orange"}.get(
            sheet, "gray"
        )

        G.add_node(key, label=label, color=color, sheet=sheet, meta=meta)

        if isinstance(formula, str) and "=" in formula:
            refs = resolve_formula_refs(formula, sheet, in_df, all_vars)
            for ref in refs:
                if ref in all_vars:
                    G.add_edge(ref, key)

    return G


import json


def export_graph_as_json(G: nx.DiGraph, file_path: str):
    """
    Exportiert das gegebene Netzwerk als JSON im gewünschten Format.
    """
    elements = []
    for i, node in enumerate(G.nodes):
        info = G.nodes[node]
        meta = info.get("meta")
        label = info.get("label", node)
        if not label or label is NaN or "Space" in label:
            continue
        e = meta.get("Einheit", "")
        icon = meta.get("Icon", "")
        element = {
            "id": f"i{i}",
            "Label": meta.get("Name", ""),
            "Sheet": info.get("sheet", "Unknown"),
            "Kategorie": meta.get("Kategorie", ""),
            "Input": meta.get("ka", "No"),
            "Einheit": e if e is not NaN else "",
            "icon": icon if icon is not NaN else "",
        }
        # element["description"] = meta.get("Beschreibung", None) or meta.get(
        #     "Kommentar", None
        # ) must not return NaN
        if var_name := meta.get("var_name", "") is NaN:
            element["var_name"] = ""
        else:
            element["var_name"] = var_name or ""

        # Weitere Felder aus meta hinzufügen (optional)
        # for k, v in info.items():
        #     if k not in element and isinstance(v, (str, int, float)):
        #         element[k] = v

        elements.append(element)

    connections = []
    for src, dst in G.edges():
        connection = {
            "from": G.nodes[src].get("label", src),
            "to": G.nodes[dst].get("label", dst),
            "direction": "directed",
        }
        connections.append(connection)

    data = {
        "elements": elements,
        "connections": connections,
    }

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"✔️ Graph exported to {file_path}")


import plotly.graph_objects as go
import networkx as nx


def draw_dependency_graph_interactive(G: nx.DiGraph):
    pos = nx.spring_layout(G, k=0.3, iterations=100)  # Force-directed layout

    # Extract positions for plotly
    edge_x, edge_y = [], []
    for src, dst in G.edges():
        x0, y0 = pos[src]
        x1, y1 = pos[dst]
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        line=dict(width=0.8, color="#888"),
        hoverinfo="none",
        mode="lines",
    )

    node_x, node_y, node_text, node_color = [], [], [], []
    for node in G.nodes:
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        node_text.append(G.nodes[node].get("label", node))
        node_color.append(G.nodes[node].get("color", "gray"))

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode="markers+text",
        textposition="top center",
        textfont_size=10,
        marker=dict(color=node_color, size=14, line_width=0.5),
        text=node_text,
        hovertext=node_text,
        hoverinfo="text",
    )

    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title="📊 Interactive Excel Calculation Dependency Graph",
            titlefont_size=16,
            showlegend=False,
            hovermode="closest",
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
        ),
    )
    fig.show()


def draw_dependency_graph(G: nx.DiGraph):
    # Group nodes by sheet
    layers = {"IN": [], "SIM2": [], "OUT": [], "OTHER": []}
    for node in G.nodes:
        sheet = G.nodes[node].get("sheet", "OTHER")
        layers.setdefault(sheet, []).append(node)

    # Order layers (left to right)
    sheet_order = ["IN", "SIM2", "OUT", "OTHER"]
    pos = {}
    x_spacing = 5
    y_spacing = 1.2

    for i, sheet in enumerate(sheet_order):
        col_nodes = layers.get(sheet, [])
        for j, node in enumerate(col_nodes):
            pos[node] = (i * x_spacing, -j * y_spacing)

    plt.figure(figsize=(18, 14))
    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=[G.nodes[n]["color"] for n in G.nodes],
        node_size=700,
        alpha=0.9,
    )
    nx.draw_networkx_edges(G, pos, edge_color="gray", arrows=True, alpha=0.4)

    # Optionally trim long labels
    labels = {
        n: (
            G.nodes[n]["label"][:25] + "…"
            if len(G.nodes[n]["label"]) > 30
            else G.nodes[n]["label"]
        )
        for n in G.nodes
    }
    nx.draw_networkx_labels(G, pos, labels, font_size=8)

    plt.title("📊 Excel Calculation Dependency Graph", fontsize=14)
    plt.axis("off")
    plt.tight_layout()
    plt.show()


def compute_self_reference_depths(G: nx.DiGraph) -> dict:
    """
    Computes the max self-referencing depth per node, scoped per sheet.
    Returns a dict of node -> depth (starting from 0).
    """
    depth_map = {}

    def dfs(node, visited):
        if node in depth_map:
            return depth_map[node]
        if node in visited:
            return 0  # prevent cycles
        visited.add(node)

        sheet = G.nodes[node].get("sheet", "")
        max_depth = 0
        for pred in G.predecessors(node):
            if G.nodes[pred].get("sheet", "") == sheet:
                max_depth = max(max_depth, 1 + dfs(pred, visited))

        visited.remove(node)
        depth_map[node] = max_depth
        return max_depth

    for node in G.nodes:
        dfs(node, set())

    return depth_map


def draw_dependency_graph_force_xlayered(G: nx.DiGraph):
    # Define layout configuration

    dx = 3  # spacing between levels
    base_x = {"IN": -15, "SIM2": 0, "OUT": 15}  # left-mid-right

    depth_map = compute_self_reference_depths(G)
    fixed_x = {}

    for node in G.nodes:
        sheet = G.nodes[node].get("sheet", "OTHER")
        ka_val = G.nodes[node].get("ka", None)
        depth = depth_map.get(node, 0)

        # Color tweak for IN:ka=2
        if sheet == "IN" and ka_val == 2:
            G.nodes[node]["color"] = "darkgreen"

        # Fallback if unknown sheet
        if sheet not in base_x:
            sheet = "SIM2"

        fixed_x[node] = base_x[sheet] + dx * depth

    # Only y gravity
    pos_y = nx.spring_layout(G, seed=42)

    pos = {node: (fixed_x[node], pos_y[node][1]) for node in G.nodes}

    # Edges
    edge_traces = []
    for src, dst in G.edges():
        x0, y0 = pos[src]
        x1, y1 = pos[dst]

        parent_color = G.nodes[src].get(
            "color", "#888"
        )  # or use dst for child-based coloring

        edge_traces.append(
            go.Scatter(
                x=[x0, x1, None],
                y=[y0, y1, None],
                line=dict(width=1, color=parent_color),
                hoverinfo="none",
                mode="lines",
            )
        )

    # Nodes
    node_trace = go.Scatter(
        x=[pos[n][0] for n in G.nodes],
        y=[pos[n][1] for n in G.nodes],
        mode="markers+text",
        text=[G.nodes[n]["label"] for n in G.nodes],
        hovertext=[n for n in G.nodes],
        textposition="top center",
        marker=dict(
            size=12,
            color=[G.nodes[n]["color"] for n in G.nodes],
            line=dict(width=1, color="black"),
        ),
    )

    fig = go.Figure(data=[edge_traces, node_trace])
    fig.update_layout(
        showlegend=False,
        title="📊 Layered Excel Dependency Graph",
        margin=dict(l=0, r=0, t=40, b=0),
        plot_bgcolor="white",
    )
    fig.show()


if __name__ == "__main__":
    p = excel.Project("../Project_Export.xlsx")
    # tax = p.taxonomy()
    # dfsim = pd.read_excel("../Taxonomy.xlsx", sheet_name="SIM2")
    # tax["SIM2"] = {k: dfsim[k].loc[0] for k in dfsim.columns}

    c = CalcTree(p, sim2_path="../Taxonomy.xlsx")
    graph = build_dependency_graph(c)
    export_graph_as_json(graph, "calctree.json")
    # draw_dependency_graph(graph)
    # draw_dependency_graph_interactive(graph)
    # draw_dependency_graph_force_xlayered(graph)

#   https://kumu.io/simonschaluppe/sandbox#peexcel
