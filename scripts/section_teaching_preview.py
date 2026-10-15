"""Interactive teaching lesson using existing section geometry, not a simulation.

Run: python scripts/section_teaching_preview.py
The lesson uses the teaching renderer style and explicit fixture overlays. The five component assignments
apply only to the explicitly defined, fully heated two-storey teaching building.
"""
from copy import deepcopy
from pathlib import Path
from xml.etree import ElementTree as ET

from pexl.model.scenario import Scenario
from pexl.spatial import section_layout_from_scenario, render_svg

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def teaching_svg():
    scenario = Scenario("Schematischer Schnitt – vollständig beheizt, ohne Keller")
    scenario.v.NFA_residential = scenario.v.NFA_total = 600
    scenario.v.building_count = 1
    scenario.v.storey_count_avg = 2
    scenario.v.PV_is_used = False
    section = section_layout_from_scenario(scenario)
    source = ET.fromstring(render_svg(section, style="teaching", usage_labels="none"))
    svg = ET.Element(f"{{{NS}}}svg", {
        "viewBox": "0 100 640 340", "role": "img",
        "aria-labelledby": "section-title section-desc",
    })
    ET.SubElement(svg, f"{{{NS}}}title", id="section-title").text = "Schematischer Schematischer Schnitt"
    ET.SubElement(svg, f"{{{NS}}}desc", id="section-desc").text = (
        "Zwei beheizte Geschosse ohne Keller. Geometrie aus dem bestehenden Section-Renderer. "
        "Wärmeflussrichtungen sind qualitative Beispiele, keine Simulation."
    )
    base = ET.SubElement(svg, f"{{{NS}}}g", id="base")
    space_ids = {s["id"] for s in section["spaces"]}
    for original in source.iter():
        kind = original.get("data-kind")
        if original.get("id") not in space_ids and kind not in {"facade", "roof", "slab", "window"}:
            continue
        node = deepcopy(original)
        node.set("fill", "#eef1f3" if original.get("id") in space_ids else "#697983")
        if kind == "window":
            node.set("fill", "#d5edf1")
        component = {"facade": "wall", "roof": "roof", "window": "window"}.get(kind)
        if kind == "slab":
            component = "ground" if original.get("id") == "slab:b0:f0" else "floor"
        if component:
            node.set("data-component", component)
        base.append(node)
    # The contour belongs ONLY to this rectangular, fully heated teaching fixture.
    ET.SubElement(svg, f"{{{NS}}}rect", {
        "id": "hull", "x": "126", "y": "170", "width": "388", "height": "175",
        "rx": "5", "fill": "none", "stroke": "#b51265", "stroke-width": "3",
        "stroke-dasharray": "8 5", "display": "none",
    })
    defs = ET.SubElement(svg, f"{{{NS}}}defs")
    flows = [
        ("solar", "Solare Gewinne", "Qₛ", "#ad7300", (42, 220, 155, 220), (48, 205), "both"),
        ("transmission", "Transmission", "Qₜ", "#a62a65", (490, 210, 600, 210), (527, 195), "both"),
        ("ventilation", "Lüftung", "Qᵥ", "#197c88", (490, 286, 600, 286), (527, 271), "both"),
        ("internal", "Interne Wärmegewinne", "Qᵢ", "#7e458b", (320, 304, 320, 260), (335, 289), "both"),
        ("heating", "Heizung", "Qₕ", "#c03c26", (230, 392, 230, 305), (245, 386), "both"),
        ("cooling", "Kühlung", "Q꜀", "#1769b0", (420, 305, 420, 392), (435, 386), "cooled"),
        ("night", "Nachtlüftung", "Qₙᵥ", "#485a95", (155, 290, 42, 290), (48, 275), "uncooled"),
    ]
    for key, label, symbol, color, coords, text_pos, zone in flows:
        marker = ET.SubElement(defs, f"{{{NS}}}marker", {
            "id": f"arrow-{key}", "viewBox": "0 0 10 10", "refX": "9", "refY": "5",
            "markerWidth": "4", "markerHeight": "4", "orient": "auto-start-reverse",
        })
        ET.SubElement(marker, f"{{{NS}}}path", d="M 0 0 L 10 5 L 0 10 z", fill=color)
        group = ET.SubElement(svg, f"{{{NS}}}g", {"data-flow": key, "data-zone": zone, "display": "none"})
        ET.SubElement(group, f"{{{NS}}}title").text = label
        x1, y1, x2, y2 = coords
        ET.SubElement(group, f"{{{NS}}}line", {
            "x1": str(x1), "y1": str(y1), "x2": str(x2), "y2": str(y2),
            "stroke": color, "stroke-width": "4", "marker-end": f"url(#arrow-{key})",
        })
        ET.SubElement(group, f"{{{NS}}}text", {
            "x": str(text_pos[0]), "y": str(text_pos[1]), "fill": color,
            "font-size": "18", "font-weight": "700", "font-family": "Arial, sans-serif",
        }).text = symbol
    return ET.tostring(svg, encoding="unicode")


def build_preview(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    svg = teaching_svg()
    (output / "section.svg").write_text(svg, encoding="utf-8")
    html = TEMPLATE.replace("<!--SECTION-->", svg)
    path = output / "index.html"
    path.write_text(html, encoding="utf-8")
    return path


TEMPLATE = '''<!doctype html><html lang="de"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PEExcel · Thermische Hülle und Wärmeflüsse</title>
<style>
*{box-sizing:border-box}[hidden]{display:none!important}body{margin:0;background:#f4f6f7;color:#243746;font:17px/1.55 system-ui,sans-serif}
main{max-width:1180px;margin:auto;padding:32px 24px}h1{font-size:32px;line-height:1.2;margin:10px 0}h2{font-size:21px;margin:0 0 12px}
.eyebrow{color:#37695e;font-weight:700;font-size:14px}.intro{max-width:850px;margin:12px 0 24px}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 290px;gap:20px}.card{min-width:0;background:white;border:1px solid #d8e1e5;border-radius:12px;padding:22px}
button,select{font:inherit;border:1px solid #8c9da8;border-radius:6px;background:white;padding:9px 12px;color:inherit;cursor:pointer}
button[aria-pressed=true]{background:#164f60;color:white;border-color:#164f60}button:focus-visible,select:focus-visible,input:focus-visible{outline:3px solid #e7a51e;outline-offset:3px}
.toolbar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:20px}.component-list{display:grid;gap:7px}.component-list button{text-align:left}
label{display:block;margin:10px 0}input{width:18px;height:18px;vertical-align:middle}select{max-width:100%;width:100%}
svg{width:100%;height:auto;display:block}.canvas{overflow-x:auto}.hint{font-size:15px;color:#506470;margin:12px 0}.notice{border-left:4px solid #b51265;padding:8px 14px;background:#faf0f5;font-size:15px}
.legend{display:flex;flex-wrap:wrap;gap:8px 16px;font-size:16px}.legend span{white-space:nowrap}.result{min-height:95px;background:#f1f5f7;padding:12px;border-radius:6px;margin-top:15px}
.rules{margin-top:22px}table{width:100%;border-collapse:collapse}th,td{text-align:left;vertical-align:top;padding:12px;border-bottom:1px solid #dce4e8}th{font-size:15px}small{font-size:14px}
[data-component]{cursor:pointer}[data-component]:focus-visible{outline:3px solid #e7a51e}[data-component].selected{stroke:#142d3d;stroke-width:4;paint-order:stroke fill}
@media(max-width:760px){main{padding:20px 12px}h1{font-size:27px}.layout{grid-template-columns:1fr}.card{padding:16px}.canvas svg{min-width:590px}.canvas{border-bottom:1px solid #dce4e8}.result{min-height:0}table{font-size:15px}thead{display:none}tbody,tr,td{display:block}tr{padding:8px 0;border-bottom:1px solid #dce4e8}td{padding:5px 0;border:0}td:first-child{font-weight:700}td:nth-child(2)::before{content:"Modellierung: ";font-weight:600}td:nth-child(3)::before{content:"Deklaration: ";font-weight:600}.hint{font-size:15px}}
@media print{body{background:white}.toolbar,aside,.rules{display:none}.layout{display:block}.card{border:0}.canvas svg{min-width:0}.hint{font-size:12px}}
</style>
<main><div class="eyebrow">PEExcel · THERMISCHE MODELLGRENZEN</div>
<h1>Thermische Bilanzgrenze und Wärmeflüsse</h1>
<p class="intro">Bauteilzuordnung, Wärmebilanzgrenze und qualitative Wärmeflüsse am schematischen Gebäudeschnitt. Das Referenzmodell zeigt zwei vollständig beheizte Geschosse ohne Keller. Die Geometrie ist schematisch und nicht aus einem Projekt abgeleitet.</p>
<div class="toolbar" aria-label="Darstellung">
<button data-mode="components" aria-pressed="true">1 · Bauteile</button>
<button data-mode="hull" aria-pressed="false">2 · Thermische Hülle</button>
<button data-mode="flows" aria-pressed="false">3 · Wärmeflüsse</button><button id="save-svg">Ansicht als SVG speichern</button><button id="print-view">Drucken</button></div>
<div class="layout"><section class="card"><h2 id="mode-title">Bauteile zuordnen</h2>
<div class="canvas" tabindex="0" role="region" aria-label="Schnittansicht, auf schmalen Bildschirmen horizontal verschiebbar"><!--SECTION--></div>
<div class="legend" id="legend"></div>
<p class="hint">Schematische Geometrie aus dem bestehenden Section-Renderer. Auf schmalen Displays ist der Schnitt horizontal verschiebbar; Beschriftungen bleiben lesbar.</p>
<div class="notice" id="context">Bauteilfarben sind eine fachliche Ebene über dem neutralen Lehrstil.</div></section>
<aside class="card"><h2>Darstellungsoptionen</h2>
<div id="component-controls" class="component-list">
<button data-pick="wall">Außenwand</button><button data-pick="window">Fenster</button>
<button data-pick="roof">Dach</button><button data-pick="ground">Bodenplatte, beheizt</button>
<button data-pick="floor">Innere Geschoßdecke</button></div>
<div id="flow-controls" hidden><label for="zone">Thermische Modellzone</label>
<select id="zone"><option value="uncooled">Ohne aktive Kühlung</option><option value="cooled">Mit aktiver Kühlung</option></select>
<label><input id="flow-visible" type="checkbox" checked> Wärmeflüsse zeigen</label>
<div id="individual-flows"></div><p class="hint">Beide Modellzonen sind thermisch entkoppelt. Der Wechsel zeigt jede Zone einzeln; zwischen ihnen wird kein Wärmeaustausch gezeichnet.</p></div>
<label><input id="show-hull" type="checkbox"> Thermische Hülle markieren</label>
<p class="result" id="detail" aria-live="polite">Bauteiltyp für die Detailzuordnung auswählen. Eine innere Geschoßdecke gehört hier zur Konstruktion, aber nicht zur äußeren Wärmebilanzgrenze.</p>
</aside></div>
<section class="card rules"><h2>Modellieren und deklarieren</h2>
<p>Das Tool erlaubt freie Modellierung. Für eine klimaaktiv-Deklaration sind die jeweils ausgewiesenen Deklarationswerte und Bewertungsregeln einzuhalten.</p>
<table><thead><tr><th>Beispiel</th><th>Freie Modellierung</th><th>klimaaktiv-Deklaration</th></tr></thead><tbody>
<tr><td>PV-LCA</td><td>Kann im Modell berücksichtigt werden.</td><td>Wird in der Bewertungsmethode nicht berücksichtigt.</td></tr>
<tr><td>Konversionsfaktoren, Nutzerstrom, interne Wärmegewinne</td><td>Eigene Annahmen sind modellierbar.</td><td>Die vorgegebenen Deklarationswerte der jeweiligen Version sind zu verwenden.</td></tr></tbody></table>
<p class="hint">Fachliche Einordnung nach Vorgabe des Toolautors. Diese Vorschau prüft keine Deklarationskonformität und enthält keine berechneten Wärmeflusswerte.</p></section></main>
<script>
const colors={wall:'#ce699d',window:'#39849b',roof:'#548d4c',ground:'#825f3d',floor:'#52665b'};
const labels={wall:'Außenwand',window:'Fenster',roof:'Dach',ground:'Bodenplatte',floor:'Innere Decke'};
const details={wall:'Außenwand: trennt den beheizten Innenraum von der Außenluft.',window:'Fenster: Teil der thermischen Hülle; solare Gewinne und Transmission getrennt betrachten.',roof:'Dach: obere Begrenzung des beheizten Referenzgebäudes.',ground:'Bodenplatte: untere Wärmebilanzgrenze dieses Referenzmodells ohne Keller.',floor:'Innere Geschoßdecke: zwischen beheizten Geschossen; hier kein Teil der äußeren thermischen Hülle.'};
let mode='components';let selected=null;
const flowNames={solar:'Solare Gewinne',internal:'Interne Wärmegewinne',transmission:'Transmission',ventilation:'Lüftung',heating:'Heizung',cooling:'Kühlung',night:'Nachtlüftung'};
for(const [key,label] of Object.entries(flowNames)){const row=document.createElement('label');row.dataset.flowControl=key;const box=document.createElement('input');box.type='checkbox';box.checked=true;box.dataset.toggleFlow=key;row.append(box,document.createTextNode(' '+label));document.querySelector('#individual-flows').appendChild(row);}

function draw(){
document.querySelectorAll('[data-mode]').forEach(b=>b.setAttribute('aria-pressed',b.dataset.mode===mode));
document.querySelectorAll('[data-component]').forEach(n=>{n.setAttribute('fill',mode==='components'?colors[n.dataset.component]:n.dataset.component==='window'?'#d5edf1':'#697983');n.classList.toggle('selected',selected===n.dataset.component);});
document.querySelectorAll('[data-pick]').forEach(b=>b.setAttribute('aria-pressed',selected===b.dataset.pick));
document.querySelector('#hull').setAttribute('display',document.querySelector('#show-hull').checked?'inline':'none');
const zone=document.querySelector('#zone').value;
document.querySelector('[data-flow-control=cooling]').hidden=zone!=='cooled';document.querySelector('[data-flow-control=night]').hidden=zone!=='uncooled';
document.querySelectorAll('[data-flow]').forEach(g=>g.setAttribute('display',mode==='flows'&&document.querySelector('#flow-visible').checked&&document.querySelector('[data-toggle-flow='+g.dataset.flow+']').checked&&(g.dataset.zone==='both'||g.dataset.zone===zone)?'inline':'none'));
document.querySelector('#component-controls').hidden=mode==='flows';document.querySelector('#flow-controls').hidden=mode!=='flows';
document.querySelector('#mode-title').textContent={components:'Bauteile zuordnen',hull:'Die Wärmebilanzgrenze erkennen',flows:'Wärmeflüsse · '+(zone==='cooled'?'mit aktiver Kühlung':'ohne aktive Kühlung')}[mode];
document.querySelector('#context').textContent=mode==='flows'?'Qualitative Richtungen: Wärmegewinne nach innen, Wärmeabfuhr nach außen. Die gezeigte Transmission ist ein Verlustfall; reale Vorzeichen sind zeitabhängig. Pfeildicken kodieren keine Leistung.':mode==='hull'?'Die gestrichelte Linie umschließt beide beheizten Geschosse. Die innere Geschoßdecke liegt innerhalb der Bilanzgrenze.':'Bauteilfarben sind eine fachliche Ebene über dem neutralen Lehrstil.';
document.querySelector('#legend').innerHTML=mode==='hull'?'<span>Gestrichelt: thermische Hülle</span><span>Innere Decke: innerhalb der Bilanzgrenze</span>':mode==='flows'?['Qₛ Solare Gewinne','Qₜ Transmission','Qᵥ Lüftung','Qᵢ Interne Wärmegewinne','Qₕ Heizung',zone==='cooled'?'Q꜀ Kühlung':'Qₙᵥ Nachtlüftung'].map(x=>'<span>'+x+'</span>').join(''):Object.keys(labels).map(k=>'<span style="border-left:5px solid '+colors[k]+';padding-left:6px">'+labels[k]+'</span>').join('');
document.querySelector('#detail').textContent=mode==='flows'?'Heizung ist in beiden Zonen möglich. Aktive Kühlung wird nur in der gekühlten Zone, Nachtlüftung hier nur in der ungekühlten Zone gezeigt.':selected?details[selected]:'Bauteiltyp für die Detailzuordnung auswählen. Die innere Decke liegt innerhalb der Wärmebilanzgrenze.';
}
document.querySelectorAll('[data-mode]').forEach(b=>b.addEventListener('click',()=>{mode=b.dataset.mode;selected=null;document.querySelector('#show-hull').checked=mode==='hull';draw();}));
document.querySelectorAll('[data-pick]').forEach(b=>b.addEventListener('click',()=>{selected=b.dataset.pick;draw();}));
document.querySelectorAll('input,select').forEach(n=>n.addEventListener('change',draw));
document.querySelectorAll('[data-component]').forEach(n=>{
n.setAttribute('tabindex','0');n.setAttribute('role','button');n.setAttribute('aria-label',labels[n.dataset.component]);
const pick=()=>{selected=n.dataset.component;draw();};n.addEventListener('click',pick);
n.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){e.preventDefault();pick();}});
});
document.querySelector('#print-view').addEventListener('click',()=>window.print());
document.querySelector('#save-svg').addEventListener('click',()=>{
const clone=document.querySelector('.canvas svg').cloneNode(true),ns='http://www.w3.org/2000/svg';
clone.setAttribute('xmlns',ns);clone.setAttribute('viewBox','0 70 640 510');clone.setAttribute('width','1280');clone.setAttribute('height','1020');
const bg=document.createElementNS(ns,'rect');for(const [k,v] of Object.entries({x:0,y:70,width:640,height:510,fill:'white'}))bg.setAttribute(k,v);clone.insertBefore(bg,clone.firstChild);
clone.querySelectorAll('.selected').forEach(n=>{n.setAttribute('stroke','#142d3d');n.setAttribute('stroke-width','4');});
const lines=[document.querySelector('#mode-title').textContent,...Array.from(document.querySelectorAll('#legend span')).map(n=>n.textContent),'Referenzmodell: 2 beheizte Geschosse, kein Keller. Keine Simulation.', 'Qualitative Wärmeflüsse; Pfeildicken sind keine Leistungen.'];
let y=432;lines.forEach((line,i)=>{const t=document.createElementNS(ns,'text');t.setAttribute('x','20');t.setAttribute('y',i===0?'95':String(y));t.setAttribute('font-size',i===0?'18':'12');t.setAttribute('font-family','sans-serif');t.setAttribute('fill','#243746');t.textContent=line;clone.appendChild(t);if(i>0)y+=16;});
const blob=new Blob([new XMLSerializer().serializeToString(clone)],{type:'image/svg+xml'});const url=URL.createObjectURL(blob);const a=document.createElement('a');a.href=url;a.download='peexcel-lehrschnitt.svg';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
});draw();
</script></html>'''


if __name__ == "__main__":
    print(build_preview(Path(__file__).resolve().parents[1] / "notebooks/local_exports/section_teaching"))
