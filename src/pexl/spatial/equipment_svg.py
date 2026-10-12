"""Draw resolved equipment records once, with explicit location and service links."""
from xml.etree import ElementTree as ET


def draw_equipment(section, element, text, x, y, yscale):
    buildings = {b['id']:b for b in section['buildings']}
    occupied = {}
    for record in section.get('equipment',[]):
        location = record.get('resolved_location')
        if not location:
            continue  # Listed as unlocated in assumptions; no invented physical position.
        b = buildings[location['building']]
        level = location['level']
        if level == 'roof':
            z = max(r['z_m'] for r in section['roofs'] if r['building_id']==b['id'])
        else:
            f = next(f for f in section['floors'] if f['building_id']==b['id'] and f['index']==level)
            z = f['z_m']
        key = (b['id'],level)
        index = occupied.get(key,0); occupied[key]=index+1
        # Compact cabinets stay within a building; additional records stack in rows.
        width = max(8, min(32,(x(b['x_m']+b['width_m'])-x(b['x_m']))/4))
        px = x(b['x_m'])+5+(index%2)*(width+4)
        py = y(z)-5-24*(index//2)
        g = element('g',data_kind='equipment',data_system=record['kind'],
                    data_semantic_id=record['semantic_id'],data_building=b['id'])
        ET.SubElement(g,'title').text = record['kind'].replace('_',' ')+'; serves '+', '.join(record.get('serves',[]))+' (schematic)'
        ET.SubElement(g,'rect',{'x':str(px),'y':str(py-20),'width':str(width),'height':'20',
                               'fill':'#c9d4d7','stroke':'#586f78','stroke-width':'1'})
        label = {'heat_pump':'HP','district_heating':'DH','gas_boiler':'G','oil_boiler':'O','biomass_boiler':'B'}.get(record['kind'],'SYS')
        t=ET.SubElement(g,'text',{'x':str(px+width/2),'y':str(py-7),'text-anchor':'middle','font-family':'sans-serif','font-size':'9','fill':'#435963'});t.text=label
        for target in record.get('serves',[]):
            if target==b['id']: continue
            other=buildings[target];tx=x(other['x_m']+other['width_m']/2)
            element('path',data_kind='service-connection',data_equipment=record['id'],data_serves=target,
                    data_semantic_id=record['semantic_id'],d=f'M {px+width/2} {py} V {y(0)+12} H {tx} V {y(0)}',
                    fill='none',stroke='#8a9ca2',stroke_width=1,stroke_dasharray='4 3')


def attach_semantic_targets(root, section):
    targets = {}
    for category in ('spaces','floors','facades','roofs'):
        for item in section.get(category,[]):
            if 'semantic_id' in item: targets[item['id']]=item['semantic_id']
    for i,pv in enumerate(section['pv']['placements']):
        targets[f'pv{i}']=pv.get('semantic_id','pv:'+str(i))
    for node in root.iter():
        key=node.get('id','')
        owner=node.get('data-facade')
        if key.startswith(('insulation:','window:','slab:')): owner=key.split(':',1)[1]
        target=targets.get(key) or targets.get(owner)
        if target: node.set('data-semantic-id',target)
