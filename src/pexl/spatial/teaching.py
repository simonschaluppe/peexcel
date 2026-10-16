"""Neutral teaching appearance; scientific geometry remains authoritative.

No component classifications or thermal boundaries are inferred here. The
interactive teaching lesson supplies those explicitly for its named fixtures.
"""
from copy import deepcopy
from xml.etree import ElementTree as ET


def simplify_section(svg: str, section: dict) -> str:
    """Keep semantic section geometry, remove context and retain accessible labels."""
    ns = "http://www.w3.org/2000/svg"
    ET.register_namespace("", ns)
    source = ET.fromstring(svg)
    root = ET.Element(f"{{{ns}}}svg", dict(source.attrib))
    root.set("data-style", "teaching")
    root.set("aria-label", "Schematischer Gebäudeschnitt; neutrale Lehrdarstellung")
    for node in source:
        if node.tag.rsplit("}", 1)[-1] in {"title", "desc", "defs"}:
            root.append(deepcopy(node))
    spaces = {space["id"] for space in section["spaces"]}
    kinds = {"facade", "roof", "slab", "window"}
    bounds = []
    for node in source.iter():
        if node.get("id") not in spaces and node.get("data-kind") not in kinds:
            continue
        clone = deepcopy(node)
        clone.set("fill", "#edf1f3" if node.get("id") in spaces else "#697983")
        if node.get("data-kind") == "window":
            clone.set("fill", "#d5edf1")
        root.append(clone)
        if all(key in node.attrib for key in ("x", "y", "width", "height")):
            x, y, w, h = (float(node.get(k)) for k in ("x", "y", "width", "height"))
            bounds.append((x, y, x + w, y + h))
    if bounds:
        x0 = min(b[0] for b in bounds) - 35
        y0 = min(b[1] for b in bounds) - 35
        w = max(b[2] for b in bounds) - x0 + 35
        h = max(b[3] for b in bounds) - y0 + 35
        root.set("viewBox", f"{x0:g} {y0:g} {w:g} {h:g}")
        root.set("width", f"{w:g}")
        root.set("height", f"{h:g}")
    return ET.tostring(root, encoding="unicode")
