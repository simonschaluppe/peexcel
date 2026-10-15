"""Explicit cellar lesson; category names come from the existing schema.

Thermal conditions are teaching assumptions, never inferred from a usage name.
No new stored geometry or project classification format is introduced.
"""
import csv
import json
from html import escape
from pathlib import Path
from xml.etree import ElementTree as ET

from pexl.model.scenario import Scenario
from pexl.spatial import render_svg, section_layout_from_scenario

ROOT = Path(__file__).resolve().parents[1]
NS = "http://www.w3.org/2000/svg"


def categories():
    """The twenty construction categories shown in the teaching material."""
    with (ROOT / "data/schemas/1.13.1_dev/IN.csv").open(encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    start = next(i for i, r in enumerate(rows) if r["var_name"] == "COMP_name_wall")
    end = next(i for i, r in enumerate(rows) if r["var_name"] == "COMP_name_balconies")
    return [(r["var_name"], " ".join(r["label_de"].removeprefix("Bauweise").split()))
            for r in rows[start:end + 1]]


def cellar_svg():
    s = Scenario("Referenzmodell: zwei beheizte Geschosse, unbeheizter Keller")
    s.v.NFA_residential, s.v.NFA_other, s.v.NFA_total = 600, 300, 900
    s.v.building_count, s.v.storey_count_avg, s.v.PV_is_used = 1, 2, False
    layout = {"layout_version": 1, "buildings": [{"id": "A",
        "geometry": {"max_floors": 2, "max_basements": 1, "depth_m": 15},
        "allocation": {"usages": ["residential"], "basement_usages": ["other"]}}]}
    section = section_layout_from_scenario(s, layout=layout)
    svg = ET.fromstring(render_svg(section, style="teaching", usage_labels="none"))
    names = dict(categories())
    for n in svg.iter():
        kind, ident = n.get("data-kind"), n.get("id", "")
        key = None
        if kind == "facade":
            key = "wall_ec_unheated" if ":f-1:" in ident else "wall"
        elif kind == "window":
            key = "windows"
        elif kind == "roof":
            key = "roof_flat"
        elif kind == "slab":
            key = {"slab:A:f-1": "basement_floor_unheated", "slab:A:f0": "basement_ceiling",
                   "slab:A:f1": "ceiling"}[ident]
        if key:
            key = "COMP_name_" + key
            n.set("data-category", key)
            n.set("tabindex", "0")
            n.set("role", "button")
            n.set("aria-label", names[key])
        if ident.startswith("A:f-1:s"):
            n.set("fill", "#e5e1d9")
    # Boundary is derived from explicitly chosen heated-envelope elements only.
    nodes = {n.get("id"): n for n in svg.iter() if n.get("id")}
    roof, ceiling = nodes["r0"], nodes["slab:A:f0"]
    x, y = float(roof.get("x"))-8, float(roof.get("y"))-8
    bottom = float(ceiling.get("y")) + float(ceiling.get("height"))
    ET.SubElement(svg, f"{{{NS}}}rect", {"id": "boundary", "x": str(x), "y": str(y),
        "width": str(float(roof.get("width"))+16), "height": str(bottom-y),
        "fill": "none", "stroke": "#b51265", "stroke-width": "3",
        "stroke-dasharray": "7 5", "pointer-events": "none"})
    for text, ypos in [("Beheizte Geschosse", 225), ("Unbeheizter Keller", 375)]:
        ET.SubElement(svg, f"{{{NS}}}text", {"x": "320", "y": str(ypos),
            "text-anchor": "middle", "font-family": "sans-serif", "font-size": "17",
            "fill": "#243746", "pointer-events": "none"}).text = text
    return ET.tostring(svg, encoding="unicode")


def build_catalog(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    names = categories()
    svg = cellar_svg()
    options = "".join(f'<option value="{key}">{escape(label)}</option>' for key, label in names)
    page = TEMPLATE.replace("<!--SVG-->", svg).replace("<!--OPTIONS-->", options)
    page = page.replace("/*NAMES*/{}", json.dumps(dict(names), ensure_ascii=False))
    (output / "index.html").write_text(page, encoding="utf-8")
    (output / "section.svg").write_text(svg, encoding="utf-8")
    return output / "index.html"


TEMPLATE = '''<!doctype html><html lang="de"><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>Bauteile und Keller</title>
<style>*{box-sizing:border-box}body{margin:0;padding:24px;color:#243746;font:17px/1.6 system-ui;background:#f4f7f5}main{max-width:980px;margin:auto}h1{font-size:28px;line-height:1.25}select{font:inherit;max-width:100%;padding:12px;width:100%;background:white;border:1px solid #58776d;border-radius:6px}.canvas{overflow:auto;background:white;border-radius:12px;margin:20px 0}svg{display:block;width:100%;min-width:420px;max-height:440px}#detail{border-left:4px solid #176c5c;padding:14px;background:white;min-height:110px}[data-category]{cursor:pointer}[data-category]:focus-visible,select:focus-visible{outline:3px solid #cb901a}input{width:18px;height:18px}small{display:block}summary{cursor:pointer;font-weight:600}li{margin:7px 0}@media(max-width:500px){body{padding:16px}}@media print{select{display:none}}</style>
<main><h1>Bauteile über und unter der Erde</h1><p>Modellannahme: zwei beheizte Geschosse, gleicher Grundriss, vollständig erdberührter unbeheizter Keller. Keine Projektdaten. Die gestrichelte Hülle endet an der Kellerdecke.</p>
<label for="category">Bauteilkategorie auswählen</label><select id="category"><!--OPTIONS--></select>
<div class="canvas" tabindex="0" role="region" aria-label="Schnitt, horizontal verschiebbar"><!--SVG--></div>
<label><input id="boundary-visible" type="checkbox" checked> Thermische Hülle anzeigen</label>
<p id="detail" aria-live="polite"></p>
<details><summary>Alle Kategorien und ihre Zuordnung</summary><ul id="catalog"></ul></details>
<p>Die 20 Kategorien stammen aus dem Schema 1.13.1_dev. Rahmen und Glas sind weitere Schemafelder; im Schnitt werden Fenster nur als Ganzes dargestellt. Die Originalgrafik auf der Bauteilseite zeigt weitere Situationen.</p>
<small>Farbliche Hervorhebung = Auswahl, gestrichelte Linie = thermische Bilanzgrenze. Unbeheizt ist eine ausdrückliche Modellannahme und wird nicht aus der Nutzung „other“ abgeleitet. Konstruktionsstärken sind schematisch.</small></main>
<script>const names=/*NAMES*/{};const select=document.querySelector('#category');
const descriptions={COMP_name_wall:'Außenwand der beheizten Geschosse gegen Außenluft.',COMP_name_windows:'Fenster als Ganzes, ohne getrennte Rahmen-/Glasgeometrie.',COMP_name_roof_flat:'Flachdach über beheiztem Geschoss.',COMP_name_ceiling:'Innere Geschoßdecke zwischen beheizten Räumen; keine äußere thermische Grenze.',COMP_name_basement_ceiling:'Kellerdecke zwischen beheiztem Erdgeschoss und unbeheiztem Keller: Teil der thermischen Grenze.',COMP_name_wall_ec_unheated:'Erdberührte Kellerwand; hier außerhalb der beheizten Hülle.',COMP_name_basement_floor_unheated:'Erdberührter Fußboden des unbeheizten Kellers; nicht die untere Grenze der beheizten Zone.'};
function draw(){const key=select.value;document.querySelectorAll('[data-category]').forEach(n=>{const on=n.dataset.category===key;n.setAttribute('fill',on?'#167c72':n.dataset.category==='COMP_name_windows'?'#d5edf1':'#697983');n.setAttribute('stroke',on?'#082f34':'none');n.setAttribute('stroke-width',on?'3':'0');n.setAttribute('aria-pressed',on);});document.querySelector('#detail').textContent=names[key]+': '+(descriptions[key]||'Nicht im Schnitt dargestellt. Für diese Kategorie enthält die Referenzgeometrie kein eindeutig zugeordnetes Element. Keine Ersatzzuordnung.');}
select.addEventListener('change',draw);document.querySelectorAll('[data-category]').forEach(n=>{function pick(){select.value=n.dataset.category;draw();}n.addEventListener('click',pick);n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick();}});});document.querySelector('#boundary-visible').addEventListener('change',e=>document.querySelector('#boundary').setAttribute('display',e.target.checked?'inline':'none'));
for(const [key,label] of Object.entries(names)){const li=document.createElement('li');li.textContent=label+' – '+(descriptions[key]||'Nicht im Schnitt dargestellt; Zuordnung am tatsächlichen Bauteil prüfen.');document.querySelector('#catalog').appendChild(li);}draw();</script></html>'''
