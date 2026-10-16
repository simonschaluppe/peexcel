from pathlib import Path
import importlib.util
import xml.etree.ElementTree as ET

import pytest
import plotly.graph_objects as go

from pexl.plot.export import export_figure

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("publication_example", ROOT / "scripts/publication_example.py")
example = importlib.util.module_from_spec(spec)
spec.loader.exec_module(example)


def test_html_preserves_figure_and_provenance(tmp_path):
    figure, convention = example.example_figures()["electricity"]
    figure.add_annotation(text="Original annotation", x=0, y=1)
    figure.update_layout(meta={"keep": "existing"})
    before = figure.to_json()
    path = export_figure(figure, tmp_path / "chart.html", provenance=example.provenance(convention))
    html = path.read_text(encoding="utf-8")
    assert figure.to_json() == before
    assert "plotly.js" in html
    assert '<script src="https://cdn.plot.ly' not in html
    assert "Original annotation" in html
    assert "schema_version" in html and "calculated_at" in html
    assert '"keep":"existing"' in html
    assert list(figure.data[1].y) == [0, 0, -2, -3]


@pytest.mark.parametrize("key", ["source", "scenario", "model_version", "schema_version", "calculated_at", "convention"])
def test_requires_provenance(key, tmp_path):
    provenance = example.provenance("Test")
    del provenance[key]
    with pytest.raises(ValueError, match=key):
        export_figure(go.Figure(), tmp_path / "bad.html", provenance=provenance)
    assert not (tmp_path / "bad.html").exists()


def test_rejects_unsupported_format(tmp_path):
    with pytest.raises(ValueError, match="Expected"):
        export_figure(go.Figure(), tmp_path / "bad.txt", provenance=example.provenance("Test"))


@pytest.mark.parametrize("name", example.CHART_NAMES + ("electricity",))
def test_actual_static_exports(name, tmp_path):
    # Deliberately no skip: publication acceptance requires a working Kaleido/browser.
    figure, convention = example.example_figures()[name]
    assert figure.data, "Publication examples must contain actual data, not placeholders"
    before = figure.to_json()
    provenance = example.provenance(convention)
    svg = export_figure(figure, tmp_path / f"{name}.svg", provenance=provenance)
    text = " ".join(ET.parse(svg).getroot().itertext())
    assert "schema_version" in text and provenance["schema_version"] in text
    assert "calculated_at" in text
    assert figure.layout.title.text in text
    png = export_figure(figure, tmp_path / f"{name}.png", provenance=provenance)
    assert png.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    assert figure.to_json() == before


def test_method_prototypes():
    figure, _ = example.density_figure()
    assert list(figure.data[1].y) == [-v for v in figure.data[0].y]
    fig = example.mobility_figure({"Wohnen": 0.7, "Büro": 0.3},
                                  {"Wohnen": 20, "Büro": 10}, 22)
    assert list(fig.data[0].y) == [17, 22, -5]
    with pytest.raises(ValueError):
        example.mobility_figure({"Wohnen": 0.2}, {"Wohnen": 20}, 22)
