"""Publication export of existing figures; no calculation or rendering changes."""
from __future__ import annotations

from html import escape
from pathlib import Path
from textwrap import wrap
from collections.abc import Mapping

import plotly.graph_objects as go


def export_figure(
    figure: go.Figure,
    path: str | Path,
    *,
    provenance: Mapping[str, str],
    width: int = 1400,
    height: int = 900,
) -> Path:
    """Export HTML (offline), SVG, PNG or PDF with visible provenance.

    Required keys: source, scenario, model_version, schema_version,
    calculated_at and convention. Values describe the *data*, not export time
    or the package version. Unknown calculation dates must be stated explicitly.
    Extra entries (e.g. source hash or code revision) are included too.
    Static formats require the optional ``publication`` dependencies and Chrome.
    The original figure, including its traces and annotations, is not modified.
    Static plots retain all traces; interactive hover/legend actions only exist
    in HTML. Use axis titles and the convention field to explain printed plots.
    """
    required = ("source", "scenario", "model_version", "schema_version",
                "calculated_at", "convention")
    for key in required:
        if not isinstance(provenance.get(key), str) or not provenance[key].strip():
            raise ValueError(f"provenance requires a non-empty {key!r}")
    if any(not isinstance(k, str) or not isinstance(v, str)
           for k, v in provenance.items()):
        raise ValueError("provenance keys and values must be strings")
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix not in {".html", ".svg", ".png", ".pdf"}:
        raise ValueError("Expected .html, .svg, .png or .pdf")
    if width < 600 or height < 500:
        raise ValueError("Publication export requires width >= 600, height >= 500")

    result = go.Figure(figure)
    lines = []
    for key, value in provenance.items():
        lines.extend(wrap(f"{key}: {value}", width=max(35, (width - 100) // 7)))
    footer_height = 18 * len(lines) + 30
    # Keep the original plotting area and reserve a separate footer below it.
    bottom = result.layout.margin.b or 80
    result.update_layout(paper_bgcolor="white", plot_bgcolor="white",
                         width=width, height=height + footer_height,
                         margin_b=bottom + footer_height)
    result.add_annotation(
        text="<br>".join(escape(line) for line in lines),
        x=0, xref="paper", xanchor="left", y=0, yref="paper",
        yanchor="top", yshift=-bottom, showarrow=False, align="left",
        font={"size": 12, "color": "#333333"},
    )
    # Preserve arbitrary existing metadata instead of replacing it.
    result.update_layout(meta={"original": figure.layout.meta,
                               "provenance": dict(provenance)})
    path.parent.mkdir(parents=True, exist_ok=True)
    if suffix == ".html":
        result.write_html(path, include_plotlyjs=True, full_html=True,
                          config={"responsive": True}, auto_open=False)
    else:
        result.write_image(path, format=suffix[1:], scale=2 if suffix == ".png" else 1)
    return path
