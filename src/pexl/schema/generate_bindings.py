from __future__ import annotations

from pathlib import Path

from .schema_codegen import generate_schema_module_from_csv_dir
from .report_codegen import generate_report_module_from_csv_dir


def generate_bindings(
    *,
    schema_dir: str | Path,
    generated_dir: str | Path,
    version: str,
) -> tuple[Path, Path]:
    """
    Generate both variable/schema and report/chart Python modules.

    Returns
    -------
    (schema_module_path, report_module_path)
    """
    schema_dir = Path(schema_dir)
    generated_dir = Path(generated_dir)

    generated_dir.mkdir(parents=True, exist_ok=True)

    schema_output = generated_dir / f"excel_{version}.py"
    report_output = generated_dir / f"reports_{version}.py"

    generate_schema_module_from_csv_dir(
        schema_dir=schema_dir,
        output_py_path=schema_output,
        version=version,
    )

    generate_report_module_from_csv_dir(
        schema_dir=schema_dir,
        output_py_path=report_output,
        version=version,
    )

    return schema_output, report_output