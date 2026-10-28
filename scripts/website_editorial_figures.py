"""SVG viewport crops and vector callouts over unchanged editorial screenshots.

Original pixels remain embedded verbatim. Regenerate with this script or the
editorial preview notebook; no image model or raster retouching is involved.
"""
from base64 import b64encode
from html import escape
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]

# Crop and rectangle coordinates refer to the original screenshot pixels.
# These are presentation settings, not a second model of Excel parameters.
FIGURES = (
    ("pv/skalierung", (100, 674, 1120, 357), "PV: Modus, Dimensionierung und Presets",
     ((455, 674, 150, 50), (455, 873, 255, 144), (953, 725, 263, 305))),
    ("pv/profile", (0, 163, 1607, 360), "PV-Import: Standardprofile und eigene Stundenprofile",
     ((83, 206, 575, 66), (789, 163, 816, 109), (789, 273, 816, 248))),
    ("hvac/heizung", (8, 0, 578, 813), "Heizung: Erzeuger, Leistungsgrenzen und Raumtemperatur",
     ((49, 31, 337, 104), (279, 189, 107, 374), (279, 749, 107, 63))),
    ("hvac/kuehlung", (0, 0, 552, 779), "Kühlung: FreeCooling, Erzeuger und raumseitige Grenze",
     ((8, 7, 543, 112), (245, 175, 110, 359), (245, 736, 110, 42))),
    ("hvac/lueftung", (0, 0, 619, 789), "Lüftung: Anteile, Wärmerückgewinnung und Nachtlüftung",
     ((300, 4, 292, 174), (300, 315, 292, 159), (300, 634, 292, 152))),
)


def build(root=ROOT):
    """Write self-contained SVGs, returning their paths for notebook display."""
    output = []
    for name, crop, title, boxes in FIGURES:
        source = Path(root) / "website/illustrations" / f"{name}-original.png"
        payload = source.read_bytes()
        if payload[:8] != b"\x89PNG\r\n\x1a\n":
            raise ValueError(f"Expected PNG: {source}")
        width, height = struct.unpack(">II", payload[16:24])
        x, y, w, h = crop
        if not (0 <= x < x+w <= width and 0 <= y < y+h <= height):
            raise ValueError(f"Crop outside source: {source}")
        # A separate right gutter keeps numbered markers off spreadsheet text.
        parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w+52}" height="{h}" viewBox="0 0 {w+52} {h}" role="img" aria-labelledby="title">',
                 f'<title id="title">{escape(title)}. Markierungen 1 bis 3 werden im Begleittext erläutert.</title>',
                 '<rect width="100%" height="100%" fill="white"/>',
                 f'<svg width="{w}" height="{h}" viewBox="{x} {y} {w} {h}" overflow="hidden">',
                 f'<image width="{width}" height="{height}" href="data:image/png;base64,{b64encode(payload).decode()}"/>',
                 '</svg>']
        for index, (bx, by, bw, bh) in enumerate(boxes, 1):
            left, top = bx-x, by-y
            cy = max(18, min(h-18, top+bh/2))
            color = ("#125d78", "#995200", "#71478c")[index-1]
            parts.extend((
                f'<rect x="{left}" y="{top}" width="{bw}" height="{bh}" rx="3" fill="none" stroke="{color}" stroke-width="2.5"/>',
                f'<circle cx="{w+28}" cy="{cy}" r="17" fill="{color}" stroke="white" stroke-width="2"/>',
                f'<text x="{w+28}" y="{cy+6}" text-anchor="middle" font-family="Arial,sans-serif" font-size="19" font-weight="bold" fill="white">{index}</text>',
            ))
        parts.append('</svg>')
        target = source.with_name(source.name.replace('-original.png', '.svg'))
        target.write_text('\n'.join(parts), encoding='utf-8')
        output.append(target)
    return output


if __name__ == '__main__':
    for path in build():
        print(path.relative_to(ROOT))
