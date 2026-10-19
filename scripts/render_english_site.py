"""Build the English Quarto subsite into the main website output directory."""
from pathlib import Path
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
QUARTO = shutil.which("quarto")
if QUARTO is None:
    print("Quarto executable was not found on PATH; cannot render the English site.", file=sys.stderr)
    raise SystemExit(1)

english_project = ROOT / "website" / "en"
subprocess.run([QUARTO, "render"], cwd=english_project, check=True)
