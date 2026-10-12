"""Resolved presentation metadata, semantic targets and comparison geometry."""
from copy import deepcopy
import hashlib
import json


def geometry_key(section):
    """Fingerprint actual allocation, not mutable SVG styling or energy inputs."""
    fields = {'buildings': ('id','floor_ids','x_m','width_m','depth_m'),
              'floors': ('id','building_id','index','z_m','height_m','slab_thickness_m','depth_m'),
              'spaces': ('floor_id','usage','area_m2','x_m','width_m'),
              'voids': ('floor_id','kind','area_m2','x_m','width_m')}
    geometry = {kind: [{key: item[key] for key in keys if key in item}
                       for item in section.get(kind, [])] for kind, keys in fields.items()}
    return hashlib.sha256(json.dumps(geometry, sort_keys=True, allow_nan=False).encode()).hexdigest()


def finish_layout(section, normalized, inputs, original, reuse, scenario):
    signature = geometry_key(section)
    if reuse is not None:
        if not isinstance(reuse,dict) or reuse.get('geometry_signature') != signature or geometry_key(reuse) != signature:
            raise ValueError('reuse_geometry: allocation or geometry changed; regenerate and reconcile affected targets')
        # Use detached geometry, retaining current scenario context and presentation.
        for key in ('floors','spaces','voids','adjacency'):
            if key in reuse: section[key] = deepcopy(reuse[key])
    section['geometry_signature'] = signature
    section['geometry_reused'] = reuse is not None
    section['semantic_version'] = 1
    section['provenance'] = {'geometry': {'origin':'explicit' if isinstance(original,dict) else 'assumed',
                                        'scope':'schematic', 'simulation_scope':'scenario'}}
    floors = {f['id']: f for f in section['floors']}
    for index,b in enumerate(section['buildings']):
        b['semantic_id'] = 'building:'+b['id']
        b['circulation'] = {'kind':'elevator' if index%2==0 else 'stairs'}
        if normalized:
            spec = normalized['buildings'][index]
            b['circulation'] = deepcopy(spec['circulation'])
            b['street_side'] = spec['site']['street_side']
            b['courtyard_side'] = 'right' if b['street_side']=='left' else 'left'
            b['envelope'] = deepcopy(spec['envelope'])
            if b['circulation'].get('shaft_width_m',0) >= b['width_m']:
                raise ValueError(f"buildings[{index}].circulation.shaft_width_m must be smaller than the building width")
    counts = {}
    for space in section['spaces']:
        base = f"space:{space['floor_id']}:{space['usage']}"
        count = counts.get(base,0); counts[base] = count+1
        space['semantic_id'] = base+f':{count}'
    space_targets = {s['id']:s['semantic_id'] for s in section['spaces']}
    for f in section['floors']: f['semantic_id'] = 'floor:'+f['id']
    for facade in section['facades']:
        facade['semantic_id'] = 'facade:'+facade['id']
        b = next(b for b in section['buildings'] if b['id']==facade['building_id'])
        exposure = 'street' if facade['side']==b['street_side'] else 'courtyard'
        facade['exposure'] = exposure
        env = b.get('envelope',{})
        facade['facade_style'] = env.get(exposure,{}).get('facade',{}).get('style',b['facade_style'])
        if facade['facade_style'] in ('gruenderzeit','grunderzeit'): facade['facade_style'] = 'gründerzeit'
    counts = {}
    for roof in section['roofs']:
        base = 'roof:'+space_targets.get(roof['space_id'],roof['space_id'])
        count = counts.get(base,0); counts[base]=count+1
        roof['semantic_id'] = base+f':{count}'
    roofs = {r['id']:r for r in section['roofs']}
    for pv in section['pv']['placements']:
        pv['semantic_id'] = 'pv:'+roofs[pv['roof_id']]['semantic_id']
    if normalized:
        section['normalized_layout'] = deepcopy(normalized)
        section['layout_spec'] = deepcopy(normalized)
        section['site'] = deepcopy(normalized['site'])
        records = deepcopy(normalized['systems'].get('plant',[]))
        for record in records:
            record['semantic_id'] = 'equipment:'+record['id']
            record['provenance'] = {'origin':'explicit','scope':'schematic'}
            location = record.get('location')
            if location:
                available = [f for f in section['floors'] if f['building_id']==location['building']]
                level = location['level']
                if level == 'lowest_floor': level = min(f['index'] for f in available)
                if level != 'roof' and level not in [f['index'] for f in available]:
                    raise ValueError(f"systems.plant[{record['id']}].location.level does not exist in the generated building")
                record['resolved_location'] = {**location,'level':level}
        explicit_plant = 'plant' in original.get('systems',{}) or 'plant' in original.get('defaults',{}).get('systems',{}) or any('plant' in b.get('systems',{}) for b in original['buildings'])
        if not explicit_plant:
            from .system_resolution import inferred_plant
            records.extend(inferred_plant(scenario))
        for record in records:
            record.setdefault('semantic_id','equipment:'+record['id'])
            if not record.get('resolved_location'):
                section['assumptions'].append({'code':'unlocated_equipment','description':f"{record['kind']}: physical location and building connections are unknown."})
        section['equipment'] = records
        # A roof setting controls eligibility, never duplicates the scenario PV budget.
        from .section_layout import _place_pv
        eligible = {bid for bid,settings in section.get('systems',{}).get('buildings',{}).items() if 'pv' in settings['roof']}
        section['pv'] = _place_pv(inputs['pv_area'], [r for r in section['roofs'] if r['building_id'] in eligible])
        for pv in section['pv']['placements']:
            pv['semantic_id'] = 'pv:'+roofs[pv['roof_id']]['semantic_id']
        if section['pv']['unplaced_area_m2']:
            section['assumptions'].append({'code':'eligible_roof_overflow','description':'Some PV area does not fit the eligible schematic roofs.'})
