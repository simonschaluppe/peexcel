"""Plot ordinary scenario-row DataFrames without schema or model dependencies."""
import logging

import plotly.express as px

from pexl.i18n import chart_text

logger = logging.getLogger(__name__)


def _prepare(frame, names, language):
    chart_text("value", language)
    missing = [name for name in names if name is not None and name not in frame]
    if missing:
        raise ValueError(f"Plot requires columns {missing}")
    if frame.empty:
        logger.warning("Plot received an empty scenario selection")
    return frame


def _finish(figure, language):
    figure.update_layout(separators=",." if language == "de" else ".,")
    return figure


def scatter(frame, x, y, *, color=None, symbol=None, size=None,
            hover_name=None, hover_data=(), labels=None, language="de"):
    """Draw an XY scatter from explicitly named DataFrame columns.

    ``x``/``y`` are column names; ``color``, ``symbol`` and ``size`` optionally
    encode other columns. ``hover_name`` names a display column and
    ``hover_data`` lists additional columns. With no hover_name, the row index
    is shown, including all levels of a MultiIndex. ``labels`` maps column
    names to display text and can come from ``reporting.variables``.
    ``language`` controls fixed text and number formatting, not source values.

    Returns an editable Plotly Figure. Inputs are never mutated. Missing
    columns raise a descriptive ValueError; empty selections log a warning.
    """
    frame = _prepare(frame, [x, y, color, symbol, size, hover_name, *hover_data], language)
    hover = frame[hover_name] if hover_name else frame.index.map(str)
    figure = px.scatter(frame, x=x, y=y, color=color, symbol=symbol, size=size,
                        hover_name=hover, hover_data=list(hover_data), labels=labels)
    return _finish(figure, language)


def distribution(frame, variable, *, by=None, color=None, kind="box",
                 hover_name=None, labels=None, language="de"):
    """Draw a box or violin distribution of annual scenario values.

    ``variable`` selects the numeric column. ``by`` optionally creates groups
    and ``color`` optionally distinguishes another category. ``kind`` is
    ``box`` or ``violin``. Labels may be supplied by reporting.variables.
    ``hover_name`` selects a scenario-label column; otherwise the index is used.
    Distributions are unweighted simulated variants, not stock estimates.
    Returns an editable Plotly Figure without modifying the frame.
    """
    if kind not in ("box", "violin"):
        raise ValueError("kind must be 'box' or 'violin'")
    frame = _prepare(frame, [variable, by, color, hover_name], language)
    hover = frame[hover_name] if hover_name else frame.index.map(str)
    figure = getattr(px, kind)(frame, x=by, y=variable, color=color,
                              hover_name=hover, labels=labels, points=False)
    return _finish(figure, language)


def histogram(frame, variable, *, color=None, bins=None, labels=None, language="de"):
    """Count simulated variants in bins of a DataFrame variable.

    ``variable`` selects the horizontal-axis column; ``color`` optionally
    groups observations. ``bins`` is Plotly's desired maximum bin count.
    Counts are unweighted. Use ``labels`` for translated variable labels,
    usually supplied by reporting.variables. Returns an editable Plotly Figure.
    The frequency axis and number formatting follow ``language``.
    """
    frame = _prepare(frame, [variable, color], language)
    figure = px.histogram(frame, x=variable, color=color, nbins=bins, labels=labels)
    figure.update_yaxes(title=chart_text("frequency", language))
    return _finish(figure, language)
