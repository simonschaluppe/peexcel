from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Literal

from .report_codegen import generate_report_module_from_csv_dir
from .schema_codegen import generate_schema_module_from_csv_dir
from .timeseries_codegen import generate_timeseries_module_from_csv_dir


@dataclass(frozen=True)
class GeneratedBindings:
    schema: Path
    timeseries: Path
    reports: Path


def generate_bindings(
    schema_dir: str | Path,
    generated_dir: str | Path,
    *,
    version: str | None = None,
    unknown_chart_var_policy: Literal["raise", "warn", "ignore"] = "warn",
) -> GeneratedBindings:
    '''
    Generate scalar schema, SIM/timeseries schema, and report definitions
    for one PEExcel schema version.
    '''
    schema_dir = Path(schema_dir)
    generated_dir = Path(generated_dir)
    version = version or schema_dir.name

    schema_path = generate_schema_module_from_csv_dir(
        schema_dir=schema_dir,
        output_py_path=generated_dir / f"excel_{version}.py",
        version=version,
    )

    timeseries_path = generate_timeseries_module_from_csv_dir(
        schema_dir=schema_dir,
        output_py_path=generated_dir / f"timeseries_{version}.py",
        version=version,
    )

    reports_path = generate_report_module_from_csv_dir(
        schema_dir=schema_dir,
        output_py_path=generated_dir / f"reports_{version}.py",
        version=version,
        unknown_var_policy=unknown_chart_var_policy,
    )

    return GeneratedBindings(
        schema=schema_path,
        timeseries=timeseries_path,
        reports=reports_path,
    )

