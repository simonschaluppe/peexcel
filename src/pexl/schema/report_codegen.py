from __future__ import annotations

from dataclasses import dataclass
import logging
from pathlib import Path
from typing import Any, Literal

import pandas as pd

from .utils import (
    clean_cell,
    optional_int,
    read_csv_table,
    require_columns,
    write_generated_module,
)


logger = logging.getLogger(__name__)


# Temporary compatibility with the Streamlit prototype / current CHART_types.
# New Excel schemas should preferably use a semantic `chart_type` column directly.
LEGACY_BUILD_FUNCTION_MAP: dict[str, str] = {
    "build_comparison_chart": "comparison",
    "build_gwp_chart": "gwp",
    "build_four_column_gwp_chart": "gwp_four_column",
    "build_multi_grid_chart": "multi_grid",
}


@dataclass(frozen=True)
class ChartRow:
    chart_name: str
    tab_name: str | None
    title: str | None
    chart_type: str
    source_order: int


@dataclass(frozen=True)
class SeriesRow:
    chart_name: str
    label_de: str | None
    var_name: str
    role: str | None
    order: int
    color: str | None
    pattern: str | None


def _renamed_copy(
    df: pd.DataFrame,
    aliases: dict[str, str],
) -> pd.DataFrame:
    """Rename legacy columns only when the canonical column is absent."""
    rename = {
        old: new
        for old, new in aliases.items()
        if old in df.columns and new not in df.columns
    }
    return df.rename(columns=rename).copy()


def normalize_chart_types(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize CHART_types to the codegen contract.

    Canonical columns:
        chart_name, tab_name, title, chart_type

    Legacy compatibility:
        chart -> chart_name
        build_function -> chart_type (mapped to semantic values)
    """
    df = _renamed_copy(df, {"chart": "chart_name"})

    if "chart_type" not in df.columns and "build_function" in df.columns:
        df["chart_type"] = df["build_function"].map(
            lambda value: LEGACY_BUILD_FUNCTION_MAP.get(
                str(clean_cell(value)),
                str(clean_cell(value)),
            )
            if clean_cell(value) is not None
            else None
        )

    require_columns(
        df,
        ["chart_name", "chart_type"],
        table_name="CHART_types",
    )

    if "tab_name" not in df.columns:
        df["tab_name"] = None
    if "title" not in df.columns:
        df["title"] = None

    return df


def normalize_chart_metadata(df: pd.DataFrame) -> pd.DataFrame:
    """
    Normalize CHART_metadata to the new report schema.

    Canonical columns:
        chart_name, label_de, var_name, role, order, color, pattern

    Legacy compatibility:
        chart -> chart_name
        destination -> role
        missing order -> row order within chart (10, 20, 30, ...)
    """
    df = _renamed_copy(
        df,
        {
            "chart": "chart_name",
            "destination": "role",
        },
    )

    require_columns(
        df,
        ["chart_name", "var_name"],
        table_name="CHART_metadata",
    )

    for optional in ["label_de", "role", "color", "pattern"]:
        if optional not in df.columns:
            df[optional] = None

    if "order" not in df.columns:
        # Migration fallback for the previous metadata export. New schemas
        # should contain an explicit order column.
        df["order"] = (
            df.groupby("chart_name", sort=False)
            .cumcount()
            .add(1)
            .mul(10)
        )

    return df


def collect_chart_rows(df: pd.DataFrame) -> list[ChartRow]:
    df = normalize_chart_types(df)
    rows: list[ChartRow] = []

    for source_order, (_, row) in enumerate(df.iterrows()):
        chart_name = clean_cell(row.get("chart_name"))
        chart_type = clean_cell(row.get("chart_type"))
        if chart_name is None:
            continue
        if chart_type is None:
            raise ValueError(
                f"CHART_types row for {chart_name!r} has no chart_type."
            )

        rows.append(
            ChartRow(
                chart_name=str(chart_name),
                tab_name=clean_cell(row.get("tab_name")),
                title=clean_cell(row.get("title")),
                chart_type=str(chart_type),
                source_order=source_order,
            )
        )

    names = [row.chart_name for row in rows]
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        raise ValueError(
            f"CHART_types contains duplicate chart_name values: {duplicates}"
        )

    return rows


def collect_series_rows(df: pd.DataFrame) -> list[SeriesRow]:
    df = normalize_chart_metadata(df)
    rows: list[SeriesRow] = []

    for source_order, (_, row) in enumerate(df.iterrows()):
        chart_name = clean_cell(row.get("chart_name"))
        var_name = clean_cell(row.get("var_name"))
        if chart_name is None or var_name is None:
            continue

        order = optional_int(row.get("order"))
        if order is None:
            # Should only matter for malformed new tables; normalized legacy
            # tables always receive an order above.
            order = (source_order + 1) * 10

        rows.append(
            SeriesRow(
                chart_name=str(chart_name),
                label_de=clean_cell(row.get("label_de")),
                var_name=str(var_name),
                role=clean_cell(row.get("role")),
                order=order,
                color=clean_cell(row.get("color")),
                pattern=clean_cell(row.get("pattern")),
            )
        )

    return rows


def _schema_var_names(
    df_in: pd.DataFrame | None,
    df_out: pd.DataFrame | None,
) -> set[str] | None:
    if df_in is None and df_out is None:
        return None

    result: set[str] = set()
    for table_name, df in (("IN", df_in), ("OUT", df_out)):
        if df is None:
            continue
        require_columns(df, ["var_name"], table_name=table_name)
        for value in df["var_name"]:
            value = clean_cell(value)
            if value is not None:
                result.add(str(value))
    return result


def validate_report_rows(
    charts: list[ChartRow],
    series: list[SeriesRow],
    *,
    schema_var_names: set[str] | None = None,
    unknown_var_policy: Literal["raise", "warn", "ignore"] = "warn",
) -> None:
    chart_names = {chart.chart_name for chart in charts}

    unknown_charts = sorted(
        {row.chart_name for row in series if row.chart_name not in chart_names}
    )
    if unknown_charts:
        raise ValueError(
            "CHART_metadata references chart names not defined in "
            f"CHART_types: {unknown_charts}"
        )

    if schema_var_names is not None:
        unknown_vars = sorted(
            {row.var_name for row in series if row.var_name not in schema_var_names}
        )
        if unknown_vars:
            message = (
                "CHART_metadata references var_name values not present in "
                f"IN/OUT: {unknown_vars}"
            )
            if unknown_var_policy == "raise":
                raise ValueError(message)
            if unknown_var_policy == "warn":
                logger.warning(message)

    exact_rows = [
        (
            row.chart_name,
            row.var_name,
            row.role,
            row.order,
            row.label_de,
            row.color,
            row.pattern,
        )
        for row in series
    ]
    duplicates = sorted(
        {item for item in exact_rows if exact_rows.count(item) > 1},
        key=repr,
    )
    if duplicates:
        logger.warning("Duplicate CHART_metadata rows: %s", duplicates)


def _series_code(row: SeriesRow, indent: str = "            ") -> str:
    return (
        f"{indent}SeriesSpec(\n"
        f"{indent}    var_name={row.var_name!r},\n"
        f"{indent}    label_de={row.label_de!r},\n"
        f"{indent}    role={row.role!r},\n"
        f"{indent}    order={row.order!r},\n"
        f"{indent}    color={row.color!r},\n"
        f"{indent}    pattern={row.pattern!r},\n"
        f"{indent}),"
    )


def generate_report_module_text(
    df_chart_types: pd.DataFrame,
    df_chart_metadata: pd.DataFrame,
    *,
    version: str = "unknown",
    df_in: pd.DataFrame | None = None,
    df_out: pd.DataFrame | None = None,
    unknown_var_policy: Literal["raise", "warn", "ignore"] = "warn",
) -> str:
    charts = collect_chart_rows(df_chart_types)
    series = collect_series_rows(df_chart_metadata)

    validate_report_rows(
        charts,
        series,
        schema_var_names=_schema_var_names(df_in, df_out),
        unknown_var_policy=unknown_var_policy,
    )

    series_by_chart: dict[str, list[SeriesRow]] = {
        chart.chart_name: []
        for chart in charts
    }
    for row in series:
        series_by_chart[row.chart_name].append(row)
    for rows in series_by_chart.values():
        rows.sort(key=lambda row: row.order)

    parts: list[str] = [
        '"""Auto-generated PEExcel chart definitions. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "",
        "from pexl.reporting.spec import ChartSpec, SeriesSpec",
        "",
        f"REPORT_SCHEMA_VERSION = {version!r}",
        "",
        "CHARTS: dict[str, ChartSpec] = {",
    ]

    for chart in sorted(charts, key=lambda row: row.source_order):
        parts.extend(
            [
                f"    {chart.chart_name!r}: ChartSpec(",
                f"        chart_name={chart.chart_name!r},",
                f"        tab_name={chart.tab_name!r},",
                f"        title={chart.title!r},",
                f"        chart_type={chart.chart_type!r},",
                "        series=(",
            ]
        )
        parts.extend(
            _series_code(row)
            for row in series_by_chart[chart.chart_name]
        )
        parts.extend(
            [
                "        ),",
                "    ),",
            ]
        )

    parts.extend(
        [
            "}",
            "",
            "CHART_NAMES: tuple[str, ...] = tuple(CHARTS)",
            "",
            "def get_chart(chart_name: str) -> ChartSpec:",
            "    return CHARTS[chart_name]",
            "",
        ]
    )

    return "\n".join(parts)


def generate_report_module_from_csv_dir(
    schema_dir: str | Path,
    output_py_path: str | Path,
    version: str | None = None,
    *,
    unknown_var_policy: Literal["raise", "warn", "ignore"] = "warn",
) -> Path:
    schema_dir = Path(schema_dir)
    version = version or schema_dir.name

    df_in = read_csv_table(schema_dir / "IN.csv")
    df_out = read_csv_table(schema_dir / "OUT.csv")

    code = generate_report_module_text(
        df_chart_types=read_csv_table(schema_dir / "CHART_types.csv"),
        df_chart_metadata=read_csv_table(schema_dir / "CHART_metadata.csv"),
        df_in=df_in,
        df_out=df_out,
        version=version,
        unknown_var_policy=unknown_var_policy,
    )
    return write_generated_module(output_py_path, code)


def generate_report_module_from_excel(
    excel_path: str | Path,
    output_py_path: str | Path,
    version: str | None = None,
    *,
    unknown_var_policy: Literal["raise", "warn", "ignore"] = "warn",
) -> Path:
    excel_path = Path(excel_path)
    version = version or excel_path.stem

    code = generate_report_module_text(
        df_chart_types=pd.read_excel(excel_path, sheet_name="CHART_types"),
        df_chart_metadata=pd.read_excel(excel_path, sheet_name="CHART_metadata"),
        df_in=pd.read_excel(excel_path, sheet_name="IN"),
        df_out=pd.read_excel(excel_path, sheet_name="OUT"),
        version=version,
        unknown_var_policy=unknown_var_policy,
    )
    return write_generated_module(output_py_path, code)
