"""Rebuild public teaching resources without loading or changing project examples."""
from pathlib import Path
import shutil
import sys
import json

import nbformat
from nbconvert import HTMLExporter

sys.path.insert(0, str(Path(__file__).resolve().parent))
from section_teaching_preview import build_preview
from component_teaching import build_catalog

ROOT = Path(__file__).resolve().parents[1]
DOCUMENTS = {
    "Handbuch zur Nachweisführung.pdf": "handbuch.pdf",
    "PEQ Nachweistool 2026-10-14.pdf": "schulung.pdf",
    "PEQ Nachweistool 2026-10-14.pptx": "schulung.pptx",
    "Broschüre PEQ_klimaaktiv.pdf": "broschuere.pdf",
    "Der klimaaktiv Plus-Energie-Standard im Überblick.pdf": "standard.pdf",
    "Leitfaden PEQ Definition und Operationalisierung_StandJuni2023.pdf": "hintergrund.pdf",
    "klimaaktiv PEQ-Tool Dokumentation.pdf": "tool-dokumentation.pdf",
}
NOTEBOOKS = ("howto_excel", "howto_publication", "howto_section_teaching_preview",
             "howto_website", "howto_analyze_electricity_balance", "howto_visualize_project")


def build(output=None):
    """Copy an explicit public allowlist and render notebooks without execution.

    Stored notebook outputs are removed from both HTML and download copies to
    avoid accidentally publishing local project results. Original notebooks stay
    untouched. Interactive lessons are generated with the shared implementation.
    """
    output = Path(output) if output is not None else ROOT / "website"
    for folder in ("downloads", "media", "tutorials"):
        (output / folder).mkdir(parents=True, exist_ok=True)
    for source, target in DOCUMENTS.items():
        shutil.copyfile(ROOT / "docs" / source, output / "downloads" / target)
    for source, target in (("ComponentTypes.png", "components.png"), ("mobilität.png", "mobility.png")):
        shutil.copyfile(ROOT / "docs" / source, output / "media" / target)
    build_preview(output / "assets/teaching")
    build_catalog(output / "assets/components")
    exporter = HTMLExporter(template_name="basic")
    for name in NOTEBOOKS:
        raw = json.loads((ROOT / "notebooks" / f"{name}.ipynb").read_text(encoding="utf-8"))
        for index, cell in enumerate(raw["cells"]):
            cell.setdefault("id", f"source-cell-{index}")
        notebook = nbformat.reads(json.dumps(raw), as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == "code":
                cell.outputs, cell.execution_count = [], None
        nbformat.write(notebook, output / "downloads" / f"{name}.ipynb")
        body, _ = exporter.from_notebook_node(notebook)
        body = body.replace('href="../docs/development/building_sections.md"',
                            'href="https://github.com/simonschaluppe/peexcel/blob/master/docs/development/building_sections.md"')
        html = ('<!doctype html><html lang="de"><meta charset="utf-8">'
                '<meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{name}</title><style>body{{font:16px/1.6 system-ui;color:#243746;'
                'max-width:900px;margin:auto;padding:24px}}pre{overflow:auto;background:#f1f5f4;'
                'padding:16px}img{max-width:100%}.anchor-link{display:none}</style>'
                '<p>Lesefassung ohne gespeicherte Ausgaben. Für die Ausführung das Notebook '
                'herunterladen und im Repository öffnen.</p>' + body + '</html>')
        (output / "tutorials" / f"{name}.html").write_text(html, encoding="utf-8")
    return output


if __name__ == "__main__":
    build()
    # Existing synthetic examples are unchanged. Bootstrap only absent outputs
    # so a clean checkout can render the pre-existing gallery as before.
    expected = ("primary_energy_balance", "gwp_ee_detail", "electricity", "density", "mobility")
    if not all((ROOT / "website/assets" / f"{name}.{fmt}").exists()
               for name in expected for fmt in ("html", "svg", "png")):
        from publication_example import build as build_existing_examples
        build_existing_examples(ROOT / "website/assets")
