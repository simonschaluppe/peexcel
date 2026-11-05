"""Renderer-neutral PEExcel reporting helpers."""

from .materialize import chart_names, materialize, convert_unit

def primary_energy_balance(source, *, language="de", unit=None):
    """Prepare primary-energy contributions from a DataFrame or model object.

    Uses stored results, preserves scenario order and never runs a simulation.
    ``unit`` may change the energy prefix, but not area/time/energy reference.
    Returns the same editable frame/series dictionary as ``materialize``.
    """
    return materialize(source, 'primary_energy_balance', language=language, unit=unit)


def gwp_ee(source, *, language="de"):
    """District lifecycle GWP: construction, TES, embodied mobility, operation.

    Legacy resolution is recorded in the returned report's ``sources`` mapping.
    """
    return materialize(source, 'gwp_ee', language=language)


def gwp_ee_detail(source, *, language="de"):
    """Embodied construction/TES components; no mobility or operation.

    Uses the distinct coarse legacy breakdown only when current fields are absent.
    """
    return materialize(source, 'gwp_ee_detail', language=language)


def gwp_ee_fossil_biogenic(source, *, language="de"):
    """Signed fossil/biogenic construction/TES contributions and their net total.

    No unsupported fossil/biogenic split is inferred for legacy TES results.
    """
    return materialize(source, 'gwp_ee_fossil_biogenic', language=language)


__all__ = ["chart_names", "materialize", "convert_unit", "primary_energy_balance",
           "gwp_ee", "gwp_ee_detail", "gwp_ee_fossil_biogenic"]

from .analysis import variables, balance
from .shortcuts import (primary_energy_scatter_plot, density_balance_scatter_plot,
    heat_balance_plot, final_energy_balance_plot, primary_energy_balance_plot,
    gwp_ee_plot, gwp_ee_detail_plot, gwp_ee_fossil_biogenic_plot, district_gwp_ee_plot)

__all__ += ["variables", "balance", "primary_energy_scatter_plot", "density_balance_scatter_plot",
    "heat_balance_plot", "final_energy_balance_plot", "primary_energy_balance_plot",
    "gwp_ee_plot", "gwp_ee_detail_plot", "gwp_ee_fossil_biogenic_plot", "district_gwp_ee_plot"]
