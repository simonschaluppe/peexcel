"""Renderer-neutral PEExcel reporting helpers."""

from .materialize import chart_names, materialize, convert_unit

def primary_energy_balance(source, *, language="de", unit=None):
    """Prepare the primary-energy report for a Project or selected ProjectView.

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
