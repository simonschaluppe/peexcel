"""Check direct Quarto tutorial sources and their publication contract."""
from pathlib import Path
import ast
import re
import sys

import nbformat
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCES = sorted((ROOT / "website").glob("tutorial_*.ipynb"))
EXTERNAL = {"tutorial_batch", "tutorial_baubook"}


def frontmatter(notebook):
    return yaml.safe_load(notebook.cells[0].source.strip().removeprefix("---").removesuffix("---"))


@pytest.mark.parametrize("source", SOURCES, ids=lambda p: p.stem)
def test_tutorial_is_standalone_and_does_not_execute_in_quarto(source):
    notebook = nbformat.read(source, as_version=4)
    nbformat.validate(notebook)
    metadata = frontmatter(notebook)
    assert metadata["lang"] == "de"
    assert metadata["title"] and metadata["description"]
    assert metadata["execute"]["enabled"] is False
    prose = "\n".join(c.source for c in notebook.cells if c.cell_type == "markdown")
    assert "Voraussetzungen" in prose and "## Weiterarbeiten" in prose
    assert f"downloads/{source.name}" in prose
    for cell in notebook.cells:
        if cell.cell_type == "code":
            ast.parse(cell.source)
            assert not re.search(r"[A-Z]:\\Users\\", cell.source)
            assert all(o.output_type != "error" for o in cell.outputs)
            for output in cell.outputs:
                data = output.get("data", {})
                if "application/vnd.plotly.v1+json" in data:
                    assert "text/html" in data, "Static Quarto rendering needs an HTML representation"
    if source.stem in EXTERNAL:
        assert all(not c.get("outputs") for c in notebook.cells)
    else:
        assert all(c.execution_count is not None for c in notebook.cells if c.cell_type == "code")
    if source.stem in {"tutorial_bewertung", "tutorial_excel", "tutorial_grafikexport",
                       "tutorial_netzlast", "tutorial_sankey", "tutorial_stromprofile"}:
        assert any("Plotly.newPlot" in o.get("data", {}).get("text/html", "")
                   for c in notebook.cells for o in c.get("outputs", []))


def test_navigation_and_overview_cover_each_tutorial_once():
    assert SOURCES
    config = yaml.safe_load((ROOT / "website/_quarto.yml").read_text(encoding="utf-8"))
    assert "tutorial_*.ipynb" in config["project"]["render"]
    assert "!downloads/**" in config["project"]["render"]
    assert "assessment.ipynb" not in config["project"]["render"]
    overview = (ROOT / "website/python.qmd").read_text(encoding="utf-8")

    def links(node):
        if isinstance(node, str):
            yield node
        elif isinstance(node, list):
            for item in node:
                yield from links(item)
        elif isinstance(node, dict):
            if "href" in node:
                yield node["href"]
            yield from links(node.get("contents", []))

    navigation = list(links(config["website"]["sidebar"]["contents"]))
    for source in SOURCES:
        assert navigation.count(source.name) == 1
        assert overview.count(f"]({source.name})") == 1
    assert "<iframe" not in overview


def test_tutorial_downloads_keep_outputs_and_build_does_not_rewrite_sources(tmp_path):
    sys.path.insert(0, str(ROOT / "scripts"))
    from website_assets import build
    originals = {p: p.read_bytes() for p in (ROOT / "notebooks").glob("howto_*.ipynb")}
    tutorials = {p: p.read_bytes() for p in SOURCES}
    build(tmp_path)
    for source, content in {**originals, **tutorials}.items():
        assert source.read_bytes() == content
    for source, content in tutorials.items():
        assert (tmp_path / "downloads" / source.name).read_bytes() == content
    assert not list(tmp_path.glob("*.ipynb")), "No generated notebook pages"
    legacy = (tmp_path / "tutorials/howto_excel.html").read_text(encoding="utf-8")
    assert "tutorial_excel.html" in legacy


def test_tutorial_links_have_source_targets():
    for source in SOURCES:
        notebook = nbformat.read(source, as_version=4)
        for cell in notebook.cells:
            if cell.cell_type != "markdown":
                continue
            for target in re.findall(r"\]\(([^)#]+)(?:#[^)]*)?\)", cell.source):
                if target.startswith(("https://", "http://", "downloads/")):
                    continue
                assert (source.parent / target).is_file(), (source.name, target)


def test_baubook_tutorial_handles_keyed_reference_values_without_network(monkeypatch, tmp_path):
    from pexl.io import baubook
    import pandas as pd

    class Session:
        closed = False

        def close(self):
            self.closed = True

    session = Session()
    monkeypatch.setattr(baubook, "load_credentials", lambda path: ("test", "not-a-key"))
    monkeypatch.setattr(baubook, "create_baubook_session", lambda *args: session)
    monkeypatch.setattr(baubook, "get_products", lambda *args, **kwargs: {
        "items": [{"id": "p1", "name": "Beispiel"}]
    })
    monkeypatch.setattr(baubook, "get_categories", lambda *args: {
        "c1": {"Titel": {"de": "Beispielkategorie"}}
    })

    def references(current, reference_type):
        assert current is session and reference_type == "ZG"
        return {"items": {"r1": {"Wert": 1}, "r2": {"Wert": 2}}}

    monkeypatch.setattr(baubook, "get_reference_values", references)
    notebook = nbformat.read(ROOT / "website/tutorial_baubook.ipynb", as_version=4)
    namespace = {}
    for cell in notebook.cells:
        if cell.cell_type == "code":
            exec(compile(cell.source, "tutorial_baubook.ipynb", "exec"), namespace)
            namespace["OUTPUT"] = tmp_path
    assert namespace["referenzen"]["reference_id"].tolist() == ["r1", "r2"]
    assert len(pd.read_excel(tmp_path / "tutorial_baubook_referenzwerte.xlsx")) == 2
    assert session.closed
