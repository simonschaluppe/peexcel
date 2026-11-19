"""Shared Plotly primitives for annual reports."""
import math

import pandas as pd
import plotly.graph_objects as go


def darken_color(hex_color: str, factor: float = 0.7) -> str:
    """Return a darker hex color for Plotly pattern foregrounds."""
    value = (hex_color or "").strip().lstrip("#")

    if len(value) == 3:
        value = "".join(c * 2 for c in value)

    if len(value) != 6:
        return "#000000"

    try:
        r, g, b = (int(value[i:i + 2], 16) for i in (0, 2, 4))
    except ValueError:
        return "#000000"

    r, g, b = (max(0, int(v * factor)) for v in (r, g, b))
    return f"#{r:02x}{g:02x}{b:02x}"


def _marker(series: dict, *, replace_pattern: bool = False) -> dict:
    """Build a Plotly marker dictionary from materialized series metadata."""
    color = series.get("color") or "#cccccc"
    pattern = series.get("pattern") or ""
    marker = {"color": color}

    if color.lower() == "#ffffff":
        marker["line"] = {"color": "gray", "width": 1}

    if pattern:
        marker["pattern"] = {
            "shape": pattern,
            "fgcolor": darken_color(color),
            "bgcolor": color,
            **({"fillmode": "replace"} if replace_pattern else {}),
        }

    return marker


def _role(series: dict) -> str:
    """Return the normalized semantic role of a materialized series."""
    role = str(series.get("role") or "").strip().casefold()
    return {'demand': 'bedarf', 'supply': 'deckung'}.get(role, role)


def _series_for_role(report: dict, role: str) -> list[dict]:
    """Return report series matching one semantic chart role."""
    role = _role({'role': role})
    return [series for series in report["series"] if _role(series) == role]


def _values(report: dict, series: dict, *, absolute: bool = False) -> list[float]:
    """Return numeric values for one materialized report series."""
    values = pd.to_numeric(
        report["frame"][series["var_name"]],
        errors="raise",
    )
    if not values.map(lambda value: pd.notna(value) and math.isfinite(value)).all():
        raise ValueError(f"Missing or non-finite report values: {series['var_name']}")

    if absolute:
        values = values.abs()

    return values.tolist()


def _number(value: float, *, signed: bool = False, language="de") -> str:
    # Avoid a misleading negative zero in rounded labels.
    value = 0.0 if abs(value) < 0.05 else value
    text = format(value, "+.1f" if signed else ".1f")
    return text.replace(".", ",") if language == "de" else text


def _difference_bracket(fig: go.Figure, x: float, start: float, end: float, color: str) -> None:
    """Draw a difference at a numeric position on the chart's x axis."""
    for x0, x1, y0, y1 in (
        (x, x, start, end),
        (x - 0.12, x + 0.12, start, start),
        (x - 0.12, x + 0.12, end, end),
    ):
        fig.add_shape(type="line", xref="x", yref="y", x0=x0, x1=x1,
                      y0=y0, y1=y1, line={"color": color, "width": 2.5})
