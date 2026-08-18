from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import re
import sys

from pexl.io.converter import xlsx_to_dataset_dir

from .generate_bindings import generate_bindings


@dataclass(frozen=True)
class SchemaBuildResult:
    source_path: Path
    dataset_dir: Path
    generated_dir: Path
    schema_module: Path
    timeseries_module: Path
    report_module: Path
    version: str


def _normalize_version_name(value: str) -> str:
    """
    Make a safe Python module suffix from a file/folder name.

    Example
    -------
    "schema_1.13.1-dev_8" -> "schema_1_13_1_dev_8"
    "v1.13.1"             -> "v1_13_1"
    """
    value = str(value).strip()
    value = re.sub(r"[^0-9A-Za-z_]+", "_", value)
    value = re.sub(r"_+", "_", value)
    value = value.strip("_")

    if not value:
        raise ValueError("Could not derive a valid version name.")

    return value


def _default_dataset_dir_for_xlsx(xlsx_path: Path) -> Path:
    """
    Default persistent dataset directory created next to the XLSX.
    """
    return xlsx_path.parent / f"{xlsx_path.stem}__schema"

def _validate_generated_module(
    path: Path,
    module_name: str,
) -> None:
    code = path.read_text(encoding="utf-8")

    # Syntax validation
    compile(
        code,
        str(path),
        "exec",
    )

    # Runtime/import validation
    spec = importlib.util.spec_from_file_location(
        module_name,
        path,
    )

    if spec is None or spec.loader is None:
        raise ImportError(
            f"Cannot create import spec for {path}"
        )

    module = importlib.util.module_from_spec(spec)

    previous = sys.modules.get(module_name)
    sys.modules[module_name] = module

    try:
        spec.loader.exec_module(module)
    finally:
        if previous is None:
            sys.modules.pop(module_name, None)
        else:
            sys.modules[module_name] = previous

def create(
    path: str | Path,
    *,
    dataset_dir: str | Path | None = None,
    generated_dir: str | Path | None = None,
    version: str | None = None,
    replace_files: bool = False,
) -> SchemaBuildResult:
    """
    Generate PEExcel Python bindings from either:

    - a schema dataset directory, or
    - a schema workbook (.xlsx / .xlsm / .xlsb) directly

    The function generates:
    - variable/schema bindings
    - timeseries/SIM bindings
    - chart/report bindings

    Parameters
    ----------
    ...
    replace_files:
        Passed to `xlsx_to_dataset_dir(...)` when `path` is a workbook.
    """
    source_path = Path(path)

    if generated_dir is None:
        generated_dir = Path(__file__).parent / "generated"
    else:
        generated_dir = Path(generated_dir)

    if source_path.is_dir():
        schema_dir = source_path

    elif source_path.is_file() and source_path.suffix.lower() in {
        ".xlsx",
        ".xlsm",
        ".xlsb",
    }:
        if dataset_dir is None:
            schema_dir = _default_dataset_dir_for_xlsx(source_path)
        else:
            schema_dir = Path(dataset_dir)

        xlsx_to_dataset_dir(
            xlsx_path=source_path,
            out_dir=schema_dir,
            mode="schema",
            replace_files=replace_files,
        )

    else:
        raise ValueError(
            f"Expected schema directory or Excel file, got: {source_path}"
        )

    module_version = _normalize_version_name(
        version if version is not None else schema_dir.name
    )

    bindings = generate_bindings(
        schema_dir=schema_dir,
        generated_dir=generated_dir,
        version=module_version,
    )

    for module_name, module_path in (
        ("_pexl_generated_schema_check", bindings.schema),
        ("_pexl_generated_timeseries_check", bindings.timeseries),
        ("_pexl_generated_reports_check", bindings.reports),
    ):
        _validate_generated_module(
            module_path,
            module_name,
        )

    return SchemaBuildResult(
        source_path=source_path,
        dataset_dir=schema_dir,
        generated_dir=generated_dir,
        schema_module=bindings.schema,
        timeseries_module=bindings.timeseries,
        report_module=bindings.reports,
        version=module_version,
    )


