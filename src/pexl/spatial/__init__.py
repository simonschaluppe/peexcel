"""Deterministic, area-preserving schematic projections of PEExcel scenarios.

Layout generation reads the authoritative scenario and returns plain dictionaries.
SVG rendering consumes those dictionaries without changing scientific inputs.
"""

from .layout_spec import normalize_layout

from .section_layout import section_layout_from_scenario, suggest_section_layout
from .svg import render_svg, render_emission_details_svg

section_from_scenario = section_layout_from_scenario

__all__ = [
    "normalize_layout",
    "section_layout_from_scenario",
    "section_from_scenario",
    "suggest_section_layout",
    "render_svg",
    "render_emission_details_svg",
]
