"""Compatibility import; use :mod:`pexl.plot.reports` for report rendering."""
from .reports import chart, render, scenario_scatter, scenario_distribution, report_balance_scatter
from . import reports as _reports


def __getattr__(name):
    # Preserve historical helper imports while callers migrate.
    return getattr(_reports, name)
