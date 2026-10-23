"""Rebuild public teaching resources without loading or changing project examples."""
from pathlib import Path
import shutil
import sys
import json
import filecmp

import nbformat

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


def prepare_assessment(output):
    """Keep the original how-to callable; the Quarto source is now maintained directly.

    Only a download is copied. No generated notebook page is maintained.
    """
    source = ROOT / "website/tutorial_bewertung.ipynb"
    downloads = Path(output) / "downloads"
    downloads.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source, downloads / source.name)
    return source


def build(output=None):
    """Copy an explicit public allowlist and render notebooks without execution.

    German tutorial sources are rendered directly by Quarto and downloaded
    with their saved results. Original how-to downloads remain available without
    outputs for compatibility, including the English site. No code is executed.
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
    from output_catalog import build as build_output_catalog
    for source in ("IN", "OUT"):
        build_output_catalog(output / f"assets/{source.lower()}-catalog.qmd", source=source)
    for name in NOTEBOOKS:
        raw = json.loads((ROOT / "notebooks" / f"{name}.ipynb").read_text(encoding="utf-8"))
        for index, cell in enumerate(raw["cells"]):
            cell.setdefault("id", f"source-cell-{index}")
        notebook = nbformat.reads(json.dumps(raw), as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == "code":
                cell.outputs, cell.execution_count = [], None
        nbformat.write(notebook, output / "downloads" / f"{name}.ipynb")
    # Preserve previously published reading URLs as links to the edited tutorials.
    # This is a compatibility mapping, not another notebook-rendering pipeline.
    destinations = {
        "howto_excel": "tutorial_excel.html",
        "howto_publication": "tutorial_grafikexport.html",
        "howto_section_teaching_preview": "tutorial_gebaeudeschnitt.html",
        "howto_website": "tutorial_website.html",
        "howto_analyze_electricity_balance": "tutorial_stromprofile.html",
        "howto_visualize_project": "tutorial_gebaeudeschnitt.html",
    }
    for name, destination in destinations.items():
        (output / "tutorials" / f"{name}.html").write_text(
            '<!doctype html><html lang="de"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>Tutorial verschoben</title>'
            f'<meta http-equiv="refresh" content="0;url=../{destination}">'
            f'<p><a href="../{destination}">Zum überarbeiteten Tutorial</a></p></html>',
            encoding="utf-8",
        )
    for source in sorted((ROOT / "website").glob("tutorial_*.ipynb")):
        shutil.copyfile(source, output / "downloads" / source.name)
    # Legacy download URLs remain valid for already shared links.
    for name in ("howto_assess", "howto_batch_simulate"):
        notebook = nbformat.read(ROOT / "notebooks" / f"{name}.ipynb", as_version=4)
        for cell in notebook.cells:
            if cell.cell_type == "code":
                cell.outputs, cell.execution_count = [], None
        nbformat.write(notebook, output / "downloads" / f"{name}.ipynb")
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
