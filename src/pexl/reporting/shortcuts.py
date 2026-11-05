"""Named annual figures using the same preparation as explicit reporting calls."""
from .analysis import variables
from .materialize import materialize


def primary_energy_scatter_plot(source, *, color=None, symbol=None, size=None,
                                hover_data=(), language="de"):
    """Plot stored virtual primary-energy demand against virtual supply.

    Accepts a scenario-row DataFrame, Project, Scenario or view. The horizontal
    axis is PEI_virtual_demand, the vertical axis PEI_virtual_supply. These are
    exported model totals, including their recorded sign conventions. They can
    differ from magnitude sums of the primary-energy contribution report.
    Optional color/symbol/size/hover_data name source columns. Labels and number
    formatting follow language (de/en). Returns an editable Plotly Figure.
    """
    from pexl.plot import scatter
    names = ["PEI_virtual_demand", "PEI_virtual_supply", color, symbol, size, *hover_data]
    data = variables(source, *(name for name in names if name), language=language)
    return scatter(**data, x="PEI_virtual_demand", y="PEI_virtual_supply",
                   color=color, symbol=symbol, size=size, hover_data=hover_data)


def density_balance_scatter_plot(source, *, color=None, language="de"):
    """Plot FSI against the stored PEI_balance for annual scenario comparisons.

    Accepts DataFrames and model objects supported by reporting.variables.
    ``color`` optionally selects a category column. Uses the exported model
    balance without recomputing it from report contributions. Returns an
    editable Plotly Figure with German/English schema labels.
    """
    from pexl.plot import scatter
    names = ["FSI", "PEI_balance", color]
    data = variables(source, *(name for name in names if name), language=language)
    return scatter(**data, x="FSI", y="PEI_balance", color=color)


def heat_balance_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw annual heat demand and supply using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "heat_balance").
    """
    from pexl.plot.reports import render
    report = materialize(source, "heat_balance", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


def final_energy_balance_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw annual final-energy demand and supply using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "final_energy_balance").
    """
    from pexl.plot.reports import render
    report = materialize(source, "final_energy_balance", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


def primary_energy_balance_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw annual primary-energy demand and supply using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "primary_energy_balance").
    """
    from pexl.plot.reports import render
    report = materialize(source, "primary_energy_balance", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


def gwp_ee_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw lifecycle embodied and operational GWP using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "gwp_ee").
    """
    from pexl.plot.reports import render
    report = materialize(source, "gwp_ee", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


def gwp_ee_detail_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw embodied GWP components using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "gwp_ee_detail").
    """
    from pexl.plot.reports import render
    report = materialize(source, "gwp_ee_detail", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


def gwp_ee_fossil_biogenic_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw fossil and biogenic embodied GWP using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "gwp_ee_fossil_biogenic").
    """
    from pexl.plot.reports import render
    report = materialize(source, "gwp_ee_fossil_biogenic", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


def district_gwp_ee_plot(source, *, language="de", unit=None, annotate=False,
                        budget=None, legend_position="below"):
    """Draw construction, systems, mobility and operational GWP using its schema report.

    ``source`` accepts a scenario-row DataFrame, Project, Scenario or view.
    The report resolves contribution columns, labels, roles and existing
    fallbacks. ``language`` selects German/English labels and fixed chart text.
    ``unit`` optionally converts compatible energy prefixes. ``annotate`` adds
    supported balance annotations; ``budget`` is only supported by the
    two-column gwp_ee chart. ``legend_position`` is "below" or "right".
    Returns an editable Plotly Figure. Inputs are not modified. For editable
    report data use reporting.materialize(source, "district_gwp_ee").
    """
    from pexl.plot.reports import render
    report = materialize(source, "district_gwp_ee", language=language, unit=unit)
    return render(report, annotate=annotate, budget=budget,
                  legend_position=legend_position)


