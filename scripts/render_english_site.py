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
    print("English preview ready: quarto preview website --no-render --no-execute --no-watch-inputs")
    print("Open /en/ in the preview. Existing German tutorial pages are reused.")
    return output / "en" / "index.html"


if __name__ == "__main__":
    build()
