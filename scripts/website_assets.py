"""Rebuild public teaching resources without loading or changing project examples."""
from pathlib import Path
import shutil
import sys
import json
import filecmp

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
MANUAL_FIGURES = (
    "excel-overview", "quick-start", "energy-model", "thermal-model", "dispatch",
    "mobility-boundary", "decarbonisation", "operational-emissions",
    "dynamic-assessment", "lifecycle", "tool-workflow", "excel-dashboard",
    "variant-comparison", "presets",
)


def _prepare_notebook_page(output, name, title, page):
    """Prepare a native Quarto page from a saved how-to notebook.

    The notebook remains the only editable content source. The ignored page
    copy retains its outputs; the downloadable copy follows the existing
    output-free download convention. No notebook code is executed here.
    """
    output = Path(output)
    notebook = nbformat.read(ROOT / "notebooks" / f"{name}.ipynb", as_version=4)
    download = nbformat.from_dict(json.loads(nbformat.writes(notebook)))
    for cell in download.cells:
        if cell.cell_type == "code":
            cell.outputs, cell.execution_count = [], None
    (output / "downloads").mkdir(parents=True, exist_ok=True)
    nbformat.write(download, output / "downloads" / f"{name}.ipynb")

    # Quarto supplies the page title; keep all remaining notebook prose intact.
    if notebook.cells and notebook.cells[0].cell_type == "markdown":
        lines = notebook.cells[0].source.splitlines()
        if lines and lines[0].startswith("# "):
            notebook.cells[0].source = "\n".join(lines[1:]).lstrip()
    notebook.cells.insert(0, nbformat.v4.new_raw_cell(
        f'---\ntitle: "{title}"\n'
        'lang: de\nexecute:\n  enabled: false\n'
        'format:\n  html:\n    code-fold: true\n    code-summary: "Python-Code anzeigen"\n'
        '---\n'
    ))
    notebook.cells.insert(1, nbformat.v4.new_markdown_cell(
        f'[Notebook herunterladen](downloads/{name}.ipynb){{.btn .btn-primary}}\n\n'
        '[Zur Notebook-Übersicht](python.qmd)'
    ))
    nbformat.write(notebook, output / page)
    return output / page


def prepare_assessment(output):
    return _prepare_notebook_page(
        output, "howto_assess", "Bewertung von Plus-Energie-Quartieren", "assessment.ipynb"
    )


def build(output=None):
    """Copy an explicit public allowlist and render notebooks without execution.

    Standard reading views and all notebook downloads omit saved outputs.
    The explicitly selected assessment page retains its example outputs for
    native Quarto rendering. Original notebooks stay untouched.
    """
    output = Path(output) if output is not None else ROOT / "website"
    for folder in ("downloads", "media", "tutorials"):
        (output / folder).mkdir(parents=True, exist_ok=True)
    for source, target in DOCUMENTS.items():
        src, dst = ROOT / "docs" / source, output / "downloads" / target
        # Keep identical downloads intact, including PDFs open in a local viewer.
        if not dst.exists() or not filecmp.cmp(src, dst, shallow=False):
            shutil.copyfile(src, dst)
    for source, target in (("ComponentTypes.png", "components.png"), ("mobilität.png", "mobility.png")):
        shutil.copyfile(ROOT / "docs" / source, output / "media" / target)
    shutil.copyfile(ROOT / "docs/website/logo.png", output / "media/logo.png")
    manual = output / "media/manual"
    manual.mkdir(parents=True, exist_ok=True)
    for name in MANUAL_FIGURES:
        source = ROOT / "docs/website" / f"{name}.png"
        shutil.copyfile(source, manual / source.name)
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
    prepare_assessment(output)
    _prepare_notebook_page(
        output, "howto_batch_simulate", "Batchsimulation mit Python", "batch-python.ipynb"
    )
    from assessment_explained import build as build_explorer
    build_explorer(output / "assets/assessment-explained/index.html")
    explained = nbformat.read(ROOT / "notebooks/howto_assessment_explained.ipynb", as_version=4)
    for cell in explained.cells:
        if cell.cell_type == "code":
            cell.outputs, cell.execution_count = [], None
    nbformat.write(explained, output / "downloads/howto_assessment_explained.ipynb")
    return output


if __name__ == "__main__":
    build()
    from website_examples import build as build_examples
    build_examples()
