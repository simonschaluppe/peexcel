# src/pexl/cli.py
from __future__ import annotations

import argparse
from pathlib import Path

from pexl.validate.schema import diff_schema_dirs, schema_diff_to_markdown


def main() -> None:
    parser = argparse.ArgumentParser(prog="pexl")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_diff = sub.add_parser("schema-diff", help="Diff two schema dataset directories")
    p_diff.add_argument("old", type=Path, help="Old schema")
    p_diff.add_argument("new", type=Path, help="New schema")
    p_diff.add_argument("--md", type=Path, help="Write markdown report to file")
    p_diff.add_argument("--print", action="store_true", help="Print markdown to stdout")
    p_diff.add_argument("--format", choices=["table", "items"], default="items", help="How to render value changes (default: table)")

    args = parser.parse_args()

    if args.cmd == "schema-diff":
        report = diff_schema_dirs(Path("data/schemas" / args.old), Path("data/schemas" / args.new))
        md = schema_diff_to_markdown(report, format=args.format)

        if args.md:
            args.md.write_text(md, encoding="utf-8")

        if args.print or not args.md:
            print(md)

if __name__ == "__main__":
    main()
