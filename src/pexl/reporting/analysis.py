"""Prepare annual datasets for free plots and report-balance comparisons."""
import logging

import pandas as pd

from pexl.i18n import chart_text
from ._data import annual_frame, variable_label

logger = logging.getLogger(__name__)


def variables(source, *names, language="de"):
    """Select annual variables and resolve their display labels.

    ``source`` accepts a DataFrame with canonical variable columns, a Project,
    a Scenario or their views. ``names`` lists columns in the desired order;
    omit it to retain all supplied columns. Arbitrary user-created columns are
    accepted and use their column name as label. Schema variables use the
    requested German/English label and unit, with a German/name fallback.

    Returns a dictionary with ``frame``, ``labels`` and ``language`` suitable
    for ``plot.scatter(**data, x=..., y=...)`` and the other free plots.
    A copy is returned with stable scenario identities in its index. Missing
    requested columns are logged and filled with NaN so callers can inspect
    incomplete data. No schema migration or simulation is performed.
    """
    chart_text("value", language)
    frame = annual_frame(source)
    names = list(dict.fromkeys(names or frame.columns))
    missing = [name for name in names if name not in frame]
    if missing:
        logger.warning("Requested annual columns are missing, using NaN: %s", missing)
    return dict(frame=frame.reindex(columns=names).copy(),
                labels={name: variable_label(name, language) for name in names},
                language=language)


def role_total(report, role, *, absolute=False):
    """Sum report contributions for a role, preserving missing values.

    Demand/Bedarf and Supply/Deckung are equivalent semantic role names.
    ``absolute`` implements the magnitude convention used by paired bars.
    This shared calculation is also used by renderer annotations. Returns a
    Series aligned with the report frame; an absent role totals zero.
    """
    aliases = {"demand": "bedarf", "supply": "deckung"}
    role = aliases.get(role.casefold(), role.casefold())
    total = pd.Series(0.0, index=report["frame"].index)
    for series in report["series"]:
        candidate = str(series.get("role") or "").strip().casefold()
        if aliases.get(candidate, candidate) == role:
            values = pd.to_numeric(report["frame"][series["var_name"]], errors="coerce")
            total = total + (values.abs() if absolute else values)
    return total


def balance(source, chart_name, *, include=(), language="de", unit=None):
    """Prepare demand, supply and supply-minus-demand for a paired report.

    The named report determines its contributions and signed/magnitude mode.
    ``include`` selects additional original columns such as FSI or a heating
    preset for scatter axes and grouping. Returned ``frame``, ``labels`` and
    ``language`` can be passed to the generic plots. The derived column names
    ``demand``, ``supply`` and ``balance`` are reserved in ``include``.

    Values follow the displayed report, which can differ from separately
    exported model totals. Missing contributions yield missing sums and a log
    warning. Source row identity/order is preserved, including across batches.
    """
    from .materialize import materialize

    if set(include) & {"demand", "supply", "balance"}:
        raise ValueError("include collides with derived demand/supply/balance columns")
    values = annual_frame(source)
    report = materialize(values, chart_name, language=language, unit=unit)
    if report["chart_type"] != "stacked_bar_comparison":
        raise ValueError("Balance requires a paired demand/supply report")
    result = variables(values, *include, language=language)
    if not include:
        result["frame"] = values.iloc[:, :0].copy()
        result["labels"] = {}
    for column, role in (("demand", "Bedarf"), ("supply", "Deckung")):
        result["frame"][column] = role_total(
            report, role, absolute=report.get("value_mode") == "magnitude"
        ).to_numpy()
    result["frame"]["balance"] = result["frame"]["supply"] - result["frame"]["demand"]
    if result["frame"]["balance"].isna().any():
        logger.warning("Report %s has incomplete balance values", chart_name)
    suffix = f" [{report['unit']}]" if report.get("unit") else ""
    for column, text in (("demand", "demand"), ("supply", "supply"), ("balance", "difference")):
        result["labels"][column] = f"{report['title']}: {chart_text(text, language)}{suffix}"
    return result
