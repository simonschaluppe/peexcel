"""Render the English translation using existing assets, without executing cells.

Run from any directory. A previously built German site supplies tutorial pages;
shared assets are copied from the existing website resources, never regenerated.
"""
from pathlib import Path
import shutil
import subprocess
import filecmp

ROOT = Path(__file__).resolve().parents[1]

def build():
    """Render only English prose, preserving existing shared result artifacts."""
    quarto = shutil.which("quarto")
    if quarto is None:
        raise RuntimeError("Quarto executable was not found on PATH.")
    website = ROOT / "website"
    required = ["assets/in-catalog.qmd", "assets/out-catalog.qmd",
                "assets/preset-catalog.qmd", "assets/assessment-explained/index.html",
                "media/logo.png"]
    missing = [name for name in required if not (website / name).is_file()]
    if missing:
        raise FileNotFoundError(
            "Existing website assets are required; no generators were run: "
            + ", ".join(missing)
        )
    subprocess.run([quarto, "render", "--no-execute", "--no-clean"],
                   cwd=website / "en", check=True)
    # Reuse the same public resource locations as the German project. Copy only
    # changed bytes: large self-contained interactive HTML is not recomputed.
    output = website / "_site"
    for name in ("assets", "illustrations", "media", "downloads", "tutorials"):
        for source in (website / name).rglob("*"):
            if not source.is_file():
                continue
            target = output / source.relative_to(website)
            if target.exists() and filecmp.cmp(source, target, shallow=False):
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
    shutil.copy2(website / "output-catalog.js", output / "output-catalog.js")
    _write_tutorial_redirects(output)
    print("English preview ready: quarto preview website --no-render --no-execute --no-watch-inputs")
    print("Open /en/ in the preview. Existing German tutorial pages are reused.")
    return output / "en" / "index.html"


def _write_tutorial_redirects(output):
    """Keep two existing URLs pointing at the maintained tutorial pages."""
    for legacy, current in (("assessment.html", "tutorial_bewertung.html"),
                            ("batch-python.html", "tutorial_batch.html")):
        (output / legacy).write_text(
            '<!doctype html><html lang="de"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>PEXL Tutorial</title>'
            f'<meta http-equiv="refresh" content="0;url={current}">'
            f'<p><a href="{current}">Zum PEXL-Tutorial / Open tutorial</a></p></html>',
            encoding="utf-8",
        )


if __name__ == "__main__":
    build()
