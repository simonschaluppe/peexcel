"""Notebook-only design proposals; these do not infer or modify scenario inputs."""
from html import escape
from textwrap import wrap
from xml.etree import ElementTree as ET


def mapping(catalog):
    """Explicit review mapping in workbook column order, retaining original names."""
    kinds = {
        "Emission": ["tabs", "underfloor", "radiator", "ceiling_panel", "lt_radiator"],
        "Heating": ["biomass", "gas", "district_heat", "ground_hp", "water_hp", "air_hp", "split"],
        "Cooling": ["freecooling", "district_cold", "air_conditioning", "chiller", "split",
                    "unknown_source_hp", "hybrid_hp", "reversible_hp", "none", "natural",
                    "district_cold", "ground_hp", "ground_freecooling", "water_hp", "chiller", "split", "hybrid_split"],
        "Hot water": ["dhw_gas_local", "dhw_gas_central", "dhw_electric", "dhw_district",
                      "dhw_hp_local", "dhw_hp_central", "dhw_biomass"],
        "Ventilation": ["vent_exhaust", "vent_exhaust_hrv", "vent_balanced_hrv", "vent_balanced"],
    }
    proposals = {
        "tabs": ("Embedded concrete circuit", "Available: heating/cooling='tabs'", "Inside concrete; use heating/cooling colours only for enabled services."),
        "underfloor": ("Pipe above structural slab", "Available: heating='underfloor'", "Straight pipe in screed; cooling is a separate enabled-service choice."),
        "radiator": ("High-temperature radiator", "Available: heating='radiator'", "Below window; stored cooling capacity is not proof of active cooling."),
        "ceiling_panel": ("Suspended cooling panel", "Proposed: ceiling_panel", "Below ceiling, distinct from TABS inside structural concrete."),
        "lt_radiator": ("Low-temperature radiator", "Partial: heating='radiator'", "Add LT label; do not infer a fan coil from NT-WP-Heizkörper."),
        "biomass": ("Boiler + fuel store", "Available: plant=['biomass_boiler']", "Fuel store is a proposed addition; emitter remains unspecified."),
        "gas": ("Gas boiler + flue", "Available: plant=['gas_boiler']", "Show only when thermal slot capacity is positive."),
        "district_heat": ("District heat exchanger", "Available: plant=['district_heating']", "Carrier name plus positive thermal slot capacity; no boiler."),
        "ground_hp": ("Heat pump + ground loop", "Partial: plant=['boreholes']", "Heat-pump cabinet is new; boreholes require evidence, not just 'Erdwärme'."),
        "water_hp": ("Heat pump + groundwater wells", "Partial: plant=['water_well']", "Add HP cabinet and abstraction/return pair; siting is a layout choice."),
        "air_hp": ("Air-source heat pump", "Proposed: outdoor fan + indoor unit", "Source and indoor emitter are independent choices."),
        "split": ("Split indoor + outdoor units", "Partial: usages[usage]['heating'/'cooling']='split'", "Add outdoor condenser and connection; gate by active usage."),
        "freecooling": ("Passive cooling exchanger", "Proposed: exchanger + bypass", "Freecooling alone does not identify air, ground or groundwater source."),
        "district_cold": ("District cooling exchanger", "Proposed: district_cooling", "Keep distinct from district heating; positive QCmax_2th required."),
        "air_conditioning": ("Air treatment + supply ducts", "Proposed: central air cooling unit", "Luft-Luft is not sufficient evidence for a wall split unit."),
        "chiller": ("Central chiller + water circuit", "Proposed: chiller cabinet", "Terminal could be fan coil or surface cooling; ask before selecting."),
        "unknown_source_hp": ("Heat pump, source unresolved", "Proposed: HP + source choice", "Preset explicitly permits groundwater OR ground; keep both alternatives."),
        "hybrid_hp": ("Heat pump + passive bypass", "Proposed: two distinct branches", "Show passive and compressor modes separately; do not infer TABS."),
        "reversible_hp": ("Reversible heat pump", "Proposed: HP with H/C mode label", "Reversibility says nothing about the outdoor source or room emitter."),
        "none": ("No active cooling", "Available: cooling='none'", "Only omit cooling; heating and ventilation remain independent."),
        "natural": ("Window opening + air path", "Available: ventilation='natural'", "No compressor; do not equate all Freecooling presets with windows."),
        "ground_freecooling": ("Ground loop + passive bypass", "Partial: boreholes only if confirmed", "Preset also contains electric cooling capacity: show hybrid possibility."),
        "hybrid_split": ("Window/freecooling + split", "Partial: natural + split", "Keep both paths; verify the freecooling source before automatic mapping."),
        "dhw_gas_local": ("Local gas water heater", "Proposed: wall heater at draw-off", "Do not place a central plant room for a decentral preset."),
        "dhw_gas_central": ("Gas boiler + tank + return", "Partial: gas_boiler", "DHW tank and circulation return are missing from current renderer."),
        "dhw_electric": ("Under-sink electric heater", "Proposed: local electric heater", "Small draw-off appliance, not a room-heating emitter."),
        "dhw_district": ("Heat exchanger + DHW tank", "Partial: district_heating", "DHW branches and storage should be separate from space heating."),
        "dhw_hp_local": ("Local DHW heat pump", "Proposed: local HP + small tank", "Air source is not specified by this preset."),
        "dhw_hp_central": ("Central DHW heat pump + tank", "Proposed: HP + tank + return", "Show central distribution; leave source unresolved."),
        "dhw_biomass": ("Biomass boiler + DHW tank", "Partial: biomass_boiler", "Add storage and a DHW branch; do not duplicate a shared boiler."),
        "vent_exhaust": ("Extract duct + window inlet", "Partial: mechanical", "Current symbol has supply arrows: an exhaust-only variant is needed."),
        "vent_exhaust_hrv": ("Extract air + recovery unit", "Partial: heat_recovery", "Keep exhaust-only topology; WRG does not prove balanced ventilation."),
        "vent_balanced_hrv": ("Supply/extract + heat recovery", "Available: ventilation='heat_recovery'", "Recovery efficiency is a label, not equipment size."),
        "vent_balanced": ("Supply + extract ducts", "Partial: mechanical", "Add return duct; no heat-recovery exchanger."),
    }
    result = []
    for category, category_kinds in kinds.items():
        rows = [r for r in catalog["presets"] if r["category"] == category]
        if len(rows) != len(category_kinds):
            raise ValueError(f"Review mapping after catalogue changes: {category}")
        for row, kind in zip(rows, category_kinds):
            title, support, caution = proposals[kind]
            result.append(dict(row, kind=kind, visual=title, support=support, caution=caution))
    return result


def scene(kind, category):
    """Original SVG cutaway sketches for reviewing proposed component distinctions."""
    parts = []
    ink, pale = "#71828a", "#e6ebed"
    circuit = "#ba7769" if category in ("Heating", "Hot water") else "#658ba2"
    def node(tag, **attrs):
        parts.append(ET.tostring(ET.Element(tag, {k.replace('_','-'):str(v) for k,v in attrs.items()}), encoding='unicode'))
    def label(t, x, y, size=10):
        parts.append(f'<text x="{x}" y="{y}" font-size="{size}" fill="{ink}">{escape(t)}</text>')
    def line(x1,y1,x2,y2,color=ink,width=1.5):
        node('line',x1=x1,y1=y1,x2=x2,y2=y2,stroke=color,stroke_width=width)
    def box(x,y,w,h,t):
        node('rect',x=x,y=y,width=w,height=h,fill=pale,stroke=ink,stroke_width=1.3)
        label(t,x+5,y+h/2+3)
    def arrow(x,y,up=False):
        d=-1 if up else 1
        line(x,y,x,y+12*d,circuit)
        node('path',d=f'M {x-3},{y+8*d} L {x},{y+12*d} L {x+3},{y+8*d}',fill='none',stroke=circuit)
    node('rect',x=0,y=107,width=316,height=36,fill='#f0eee8')
    node('rect',x=100,y=18,width=208,height=89,fill='#f6f7f6')
    line(98,15,308,15,ink,3);line(98,107,308,107,ink,3)
    line(98,15,98,43);line(98,73,98,107)
    line(98,43,98,73,'#adc0c8',3)
    if kind in {'tabs','underfloor','radiator','ceiling_panel','lt_radiator'}:
        if kind=='tabs':
            node('rect',x=100,y=104,width=208,height=12,fill='#c3cbce')
            line(112,110,291,110,circuit,2)
            label('inside concrete',145,135)
        elif kind=='underfloor':
            node('rect',x=100,y=94,width=208,height=10,fill='#e5e0d5')
            line(112,99,291,99,circuit,2)
            label('screed above slab',145,135)
        elif kind=='ceiling_panel':
            for x in (139,266):line(x,15,x,30)
            box(125,30,156,5,'')
            line(132,33,274,33,'#658ba2',2)
            label('suspended panel',147,73)
        else:
            box(110,81,60,22,'')
            for x in range(117,170,8):line(x,84,x,100,circuit)
            label('LT' if kind=='lt_radiator' else 'HT',179,96)
    elif kind.startswith('vent_') or kind == 'air_conditioning':
        line(110,32,288,32,circuit,3)
        arrow(270,45,up=True)
        box(124,22,37,22,'HR' if 'hrv' in kind else 'AHU')
        if 'balanced' in kind or kind=='air_conditioning':
            line(110,60,288,60,'#9caeb7',2)
            arrow(216,60)
        else:
            line(75,58,118,58,circuit);arrow(180,45,up=True)
            label('window inlet',8,84)
        label('below ceiling',167,93)
    elif kind == 'none':
        label('No cooling equipment',129,66,12)
    elif kind == 'natural':
        line(96,72,81,45,ink,2);line(65,57,148,57,circuit,2)
        node('path',d='M 141,52 L 148,57 L 141,62',fill='none',stroke=circuit)
        label('window air path',139,84)
    elif kind in ('split','hybrid_split'):
        box(110,29,55,17,'indoor');box(34,70,39,30,'fan')
        node('polyline',points='53,70 53,39 110,39',stroke=circuit,fill='none')
        arrow(154,50)
        if kind=='hybrid_split':label('+ passive path',185,83)
    elif kind.startswith('dhw_'):
        local=kind in ('dhw_gas_local','dhw_electric','dhw_hp_local')
        if local:
            line(190,53,275,53,ink,3);box(215,66,32,37,'EL' if kind=='dhw_electric' else 'HP' if 'hp' in kind else 'G')
            node('polyline',points='233,66 233,45 250,45 250,53',fill='none',stroke=circuit,stroke_width=2)
            label('local draw-off',133,125)
        else:
            box(118,71,48,32,'HP' if 'hp' in kind else 'HX' if 'district' in kind else 'B' if 'biomass' in kind else 'G')
            node('rect',x=179,y=46,width=27,height=57,rx=10,fill=pale,stroke=ink)
            node('polyline',points='166,83 179,83 193,83 193,37 278,37',fill='none',stroke=circuit,stroke_width=2)
            node('polyline',points='278,43 202,43 202,95',fill='none',stroke=circuit,stroke_width=1)
            label('tank + circulation',153,125)
    else:
        text='G' if kind=='gas' else 'B' if kind=='biomass' else 'HX' if kind.startswith('district') or 'freecooling' in kind else 'CH' if kind=='chiller' else 'HP'
        box(125,67,47,37,text)
        line(172,78,272,78,circuit,2);line(172,89,272,89,circuit,1)
        label('emitter not specified',178,64,9)
        if kind=='ground_hp' or kind=='ground_freecooling':
            node('polyline',points='125,91 63,91 63,136 72,136 72,96 125,96',fill='none',stroke=circuit,stroke_width=2)
            label('ground source*',4,126)
        elif kind=='water_hp':
            for x in (39,75):
                box(x,112,10,25,'')
                node('polyline',points=f'125,87 {x+5},87 {x+5},131',fill='none',stroke=circuit)
            label('groundwater',7,69)
        elif kind=='air_hp':
            box(27,73,48,30,'fan');line(75,86,125,86,circuit)
            node('circle',cx=63,cy=88,r=7,fill='none',stroke=ink)
        elif kind.startswith('district'):
            line(7,78,125,78,circuit,2);line(7,89,125,89,circuit)
            label('network',19,67)
        elif kind in ('biomass','gas'):
            line(135,67,135,29,ink,3)
            if kind=='biomass':box(36,79,46,25,'fuel');line(82,97,125,97)
            else:line(33,96,125,96);label('gas',37,86)
        elif kind in ('hybrid_hp','freecooling'):
            node('polyline',points='126,69 126,43 244,43 244,78',fill='none',stroke=circuit)
            label('passive bypass',144,34)
        elif kind in ('unknown_source_hp','reversible_hp'):
            label('source ?',13,85);line(76,85,125,85,circuit)
            if kind=='reversible_hp':label('H / C',128,56)
    return ''.join(parts)


def gallery_svg(rows, title):
    """Three-column review board; full names and provenance stay in the notebook table."""
    width, cell_w, cell_h = 1140, 370, 322
    height = 88 + ((len(rows)+2)//3)*cell_h
    out=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}" font-family="Arial, sans-serif">',
         f'<rect width="{width}" height="{height}" fill="#f5f6f4"/>',
         f'<text x="24" y="33" font-size="23" fill="#344852">{escape(title)}</text>',
         '<text x="24" y="57" font-size="12" fill="#65747b">Preset-to-drawing proposals · source names preserved · schematic locations, not installation designs</text>']
    for i,row in enumerate(rows):
        x,y=15+(i%3)*cell_w,78+(i//3)*cell_h
        out.append(f'<g transform="translate({x},{y})"><rect width="355" height="307" rx="7" fill="white" stroke="#d9dfe0"/>')
        for j,t in enumerate(wrap(row['name'],40)[:2]):
            out.append(f'<text x="16" y="{24+j*17}" font-size="13" font-weight="bold" fill="#344852">{escape(t)}</text>')
        out.append('<g transform="translate(17,53)">'+scene(row['kind'],row['category'])+'</g>')
        for j,t in enumerate(wrap(row['support'],48)):
            out.append(f'<text x="16" y="{214+j*15}" font-size="11" fill="#4a6773">{escape(t)}</text>')
        for j,t in enumerate(wrap(row['caution'],51)[:3]):
            out.append(f'<text x="16" y="{254+j*14}" font-size="10.5" fill="#697478">{escape(t)}</text>')
        out.append('</g>')
    return ''.join(out)+'</svg>'
