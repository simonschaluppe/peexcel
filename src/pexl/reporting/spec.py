"""Schema definitions and the materialized-report contract.

A materialized report is an ordinary dictionary with ``frame`` (one row per
scenario, ``Variant`` column), ordered ``series`` metadata (``var_name`` column
key, display ``label``, semantic ``role``, ``unit``, colour/pattern), title and
chart_type. No particular PEExcel column name is required by a renderer: series
explicitly bind metadata to frame columns. ``language`` selects fixed chart text.
``value_mode`` is ``magnitude`` for paired demand/supply reports, or ``signed``
to retain supplied signs. Legacy reports without it retain magnitude behaviour.
Missing/non-finite numeric values are rejected, not replaced by zero. Rendering
never mutates inputs. Calculated annotations describe supplied contributions;
separately stored model totals are not implicitly recomputed after user edits.
"""

from dataclasses import dataclass




@dataclass(frozen=True)
class SeriesSpec:
    var_name: str
    label_de: str | None = None
    role: str | None = None
    order: int = 0
    color: str | None = None
    pattern: str | None = None


@dataclass(frozen=True)
class ChartSpec:
    chart_name: str
    tab_name: str | None
    title: str
    chart_type: str
    series: tuple[SeriesSpec, ...]