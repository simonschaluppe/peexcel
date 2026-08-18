# src/pexl/cli.py
from __future__ import annotations

import argparse
from pathlib import Path

from pexl.validate.schema import diff_schema_dirs, schema_diff_to_markdown


def _resolve_schema_dir(value: str) -> Path:
    """Resolve a version name or explicit schema dataset directory."""
    path = Path(value)
    return Path("data/schemas") / path if path.parent == Path(".") else path


def _resolve_schema_file(value: str) -> Path:
    """Resolve a version name or explicit schema workbook path."""
    path = Path(value)

    if path.suffix.lower() in {".xlsx", ".xlsm", ".xlsb"}:
        candidate = Path("data/exports") / path
        return candidate if path.parent == Path(".") and candidate.exists() else path

    return Path("data/exports") / f"schema_{value}.xlsx"


def _version_from_source(path: Path) -> str:
    """Derive the schema version from a directory or workbook name."""
    name = path.name if path.is_dir() else path.stem
    return name.removeprefix("schema_")


def main() -> None:
    """Run PEExcel schema creation and diff commands."""
    parser = argparse.ArgumentParser(prog="pexl")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_dashboard = sub.add_parser(
        "dashboard",
        help="Launch the PEExcel Streamlit dashboard.",
    )

    p_create = sub.add_parser(
        "create-schema",
        help="Generate and validate schema bindings.",
    )
    source = p_create.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "-d", "--dir",
        help="Schema dataset directory or version name.",
    )
    source.add_argument(
        "-f", "--file",
        help="Schema workbook or version name.",
    )
    p_create.add_argument("--dataset-dir", type=Path)
    p_create.add_argument("--generated-dir", type=Path)
    p_create.add_argument("--version")
    p_create.add_argument(
        "--replace",
        action="store_true",
        help="Replace existing exported dataset files.",
    )

    p_diff = sub.add_parser(
        "schema-diff",
        help="Compare two schema datasets.",
    )
    p_diff.add_argument("old")
    p_diff.add_argument("new")
    p_diff.add_argument("--md", type=Path)
    p_diff.add_argument("--print", action="store_true")
    p_diff.add_argument(
        "--format",
        choices=["table", "items"],
        default="items",
    )

    args = parser.parse_args()

    if args.cmd == "dashboard":
        import subprocess
        import sys

        app_path = (
            Path(__file__).resolve().parents[2]
            / "apps"
            / "dashboard"
            / "main.py"
        )

        if not app_path.exists():
            raise FileNotFoundError(
                f"Dashboard app not found: {app_path}"
            )

        subprocess.run(
            [
                sys.executable,
                "-m",
                "streamlit",
                "run",
                str(app_path),
            ],
            check=True,
        )
        return

    elif args.cmd == "create-schema":
        from pexl.schema import create

        if args.dir:
            source_path = _resolve_schema_dir(args.dir)
            version = args.version or _version_from_source(source_path)

            result = create(
                source_path,
                generated_dir=args.generated_dir,
                version=version,
            )
        else:
            source_path = _resolve_schema_file(args.file)
            version = args.version or _version_from_source(source_path)
            dataset_dir = (
                args.dataset_dir
                or Path("data/schemas") / version
            )

            result = create(
                source_path,
                dataset_dir=dataset_dir,
                generated_dir=args.generated_dir,
                version=version,
                replace_files=args.replace,
            )

        print(f"Schema created: {result.version}")
        print(f"  dataset    : {result.dataset_dir}")
        print(f"  schema     : {result.schema_module}")
        print(f"  timeseries : {result.timeseries_module}")
        print(f"  reports    : {result.report_module}")
        return

    if args.cmd == "schema-diff":
        report = diff_schema_dirs(
            _resolve_schema_dir(args.old),
            _resolve_schema_dir(args.new),
        )
        md = schema_diff_to_markdown(
            report,
            value_format=args.format,
        )

        if args.md:
            args.md.write_text(md, encoding="utf-8")

        if args.print or not args.md:
            print(md)


if __name__ == "__main__":
    main()