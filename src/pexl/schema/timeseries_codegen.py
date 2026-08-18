from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import pandas as pd

from .schema_codegen import unique_name_map
from .utils import (
    as_python_literal,
    clean_cell,
    read_csv_table,
    require_columns,
    write_generated_module,
)


@dataclass(frozen=True)
class TimeseriesMetaRow:
    var_name: str
    attr_name: str
    domain: str | None = None
    measure: str | None = None
    unit: str | None = None
    formula: str | None = None


def normalize_timeseries_schema(df: pd.DataFrame) -> pd.DataFrame:
    '''
    Normalize SIM schema columns to the Python/codegen contract.

    Expected PEExcel export columns:
        var_name, Domain, Measure, Unit, Formula
    '''
    aliases = {
        "Domain": "domain",
        "Measure": "measure",
        "Unit": "unit",
        "Formula": "formula",
    }

    rename = {
        old: new
        for old, new in aliases.items()
        if old in df.columns and new not in df.columns
    }

    df = df.rename(columns=rename).copy()

    require_columns(
        df,
        ["var_name"],
        table_name="SIM",
    )

    for optional in ("domain", "measure", "unit", "formula"):
        if optional not in df.columns:
            df[optional] = None

    return df


def collect_timeseries_rows(
    df: pd.DataFrame,
) -> list[TimeseriesMetaRow]:
    df = normalize_timeseries_schema(df)

    raw_rows: list[dict[str, Any]] = []

    for _, row in df.iterrows():
        var_name = clean_cell(row.get("var_name"))

        if var_name is None:
            continue

        raw_rows.append(
            {
                "var_name": str(var_name),
                "domain": clean_cell(row.get("domain")),
                "measure": clean_cell(row.get("measure")),
                "unit": clean_cell(row.get("unit")),
                "formula": clean_cell(row.get("formula")),
            }
        )

    var_names = [row["var_name"] for row in raw_rows]

    if len(var_names) != len(set(var_names)):
        duplicates = sorted(
            {
                name
                for name in var_names
                if var_names.count(name) > 1
            }
        )
        raise ValueError(
            f"SIM contains duplicate var_name values: {duplicates}"
        )

    name_map = unique_name_map(var_names)

    return [
        TimeseriesMetaRow(
            var_name=row["var_name"],
            attr_name=name_map[row["var_name"]],
            domain=row["domain"],
            measure=row["measure"],
            unit=row["unit"],
            formula=row["formula"],
        )
        for row in raw_rows
    ]


def build_timeseries_meta_dataclass_code() -> str:
    return '''@dataclass(frozen=True)
class TimeseriesMeta:
    var_name: str
    attr_name: str
    domain: str | None = None
    measure: str | None = None
    unit: str | None = None
    formula: str | None = None

    def __repr__(self) -> str:
        parts = [self.var_name]

        if self.unit:
            parts.append(f"[{self.unit}]")

        return "<TimeseriesMeta " + " ".join(parts) + ">"
'''

def build_timeseries_meta_registry_code(
    rows: list[TimeseriesMetaRow],
) -> str:
    lines = [
        "class TimeseriesMetaRegistry:",
        "    def __init__(self):",
    ]

    if not rows:
        lines.append("        pass")
        return "\n".join(lines)

    for row in rows:
        lines.append(
            f"        self.{row.attr_name} = TimeseriesMeta(\n"
            f"            var_name={row.var_name!r},\n"
            f"            attr_name={row.attr_name!r},\n"
            f"            domain={as_python_literal(row.domain)},\n"
            f"            measure={as_python_literal(row.measure)},\n"
            f"            unit={as_python_literal(row.unit)},\n"
            f"            formula={as_python_literal(row.formula)},\n"
            f"        )"
        )

    return "\n".join(lines)


def build_timeseries_attr_map_code(
    rows: list[TimeseriesMetaRow],
) -> str:
    lines = [
        "TIMESERIES_ATTR_NAME_MAP: dict[str, str] = {"
    ]

    for row in rows:
        lines.append(
            f"    {row.var_name!r}: {row.attr_name!r},"
        )

    lines.append("}")
    return "\n".join(lines)


def generate_timeseries_module_text(
    df_sim: pd.DataFrame,
    version: str = "unknown",
) -> str:
    rows = collect_timeseries_rows(df_sim)

    parts = [
        '"""Auto-generated SIM/timeseries schema bindings. Do not edit manually."""',
        "",
        "from __future__ import annotations",
        "from dataclasses import dataclass",
        "",
        f"TIMESERIES_SCHEMA_VERSION = {version!r}",
        "",
        build_timeseries_meta_dataclass_code(),
        "",
        build_timeseries_meta_registry_code(rows),
        "",
        "TIMESERIES_META = TimeseriesMetaRegistry()",
        "",
        build_timeseries_attr_map_code(rows),
        "",
    ]

    return "\n".join(parts)

def generate_timeseries_module_from_csv_dir(
    schema_dir: str | Path,
    output_py_path: str | Path,
    version: str | None = None,
) -> Path:
    schema_dir = Path(schema_dir)
    version = version or schema_dir.name

    code = generate_timeseries_module_text(
        df_sim=read_csv_table(schema_dir / "SIM.csv"),
        version=version,
    )

    return write_generated_module(
        output_py_path,
        code,
    )


def generate_timeseries_module_from_excel(
    excel_path: str | Path,
    output_py_path: str | Path,
    version: str | None = None,
    *,
    sheet_name: str = "SIM2",
) -> Path:
    excel_path = Path(excel_path)
    version = version or excel_path.stem

    code = generate_timeseries_module_text(
        df_sim=pd.read_excel(
            excel_path,
            sheet_name=sheet_name,
        ),
        version=version,
    )

    return write_generated_module(
        output_py_path,
        code,
    )
