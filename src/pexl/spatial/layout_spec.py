"""Versioned JSON layout input; no scientific quantities or simulation state."""
from copy import deepcopy
from math import isfinite
import re
from typing import Literal, TypedDict, NotRequired


class GeometrySpec(TypedDict, total=False):
    relative_length: float
    depth_m: float
    max_floors: int
    max_basements: int


class BuildingLayout(TypedDict):
    id: str
    geometry: NotRequired[GeometrySpec]
    allocation: NotRequired[dict]
    systems: NotRequired[dict]


class LayoutSpec(TypedDict):
    layout_version: Literal[1]
    buildings: list[BuildingLayout]
    defaults: NotRequired[dict]
    site: NotRequired[dict]
    systems: NotRequired[dict]


def _fields(value, allowed, path):
    if not isinstance(value, dict):
        raise ValueError(f"{path} must be a dictionary")
    unknown = set(value) - set(allowed)
    if unknown:
        raise ValueError(f"{path}: unknown fields {sorted(unknown)}")


def _merge(base, override):
    result = deepcopy(base)
    for key, value in override.items():
        result[key] = _merge(result.get(key, {}), value) if isinstance(value, dict) else deepcopy(value)
    return result


def _id(value, path):
    if not isinstance(value, str) or not re.fullmatch(r"[A-Za-z][A-Za-z0-9_-]*", value):
        raise ValueError(f"{path} must start with a letter and contain only letters, digits, '-' or '_'")
    return value


def _number(value, path, *, integer=False, zero=False):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not isfinite(value) or value < 0 or (not zero and value == 0) or (integer and int(value) != value):
        raise ValueError(f"{path} must be a finite {'nonnegative' if zero else 'positive'} {'integer' if integer else 'number'}")


def normalize_layout(layout: dict) -> dict:
    """Return a detached, versioned specification. Legacy input remains accepted.

    This validates presentation structure. Schema usage names and scientific area
    feasibility are checked by the scenario generator.
    """
    if not isinstance(layout, dict):
        raise ValueError("layout must be a dictionary")
    if 'layout_version' not in layout:
        _fields(layout, {'buildings', 'systems', 'gap_m', 'facade_style'}, 'layout')
        converted = {'layout_version': 1, 'site': {'gap_m': layout.get('gap_m', 20)},
                     'defaults': {'envelope': {'facade': {'style': layout.get('facade_style', 'default')}}}, 'buildings': []}
        if 'systems' in layout:
            converted['defaults']['systems'] = deepcopy(layout['systems'])
        for i, raw in enumerate(layout.get('buildings', [])):
            _fields(raw, {'name','relative_length','depth_m','max_floors','max_basements','basement','usages','basement_usages','usage_shares','systems','gap_after_m','facade_style'}, f'buildings[{i}]')
            b = {'id': f'b{i}', 'geometry': {}, 'allocation': {}}
            for key in ('relative_length','depth_m','max_floors','max_basements'):
                if key in raw: b['geometry'][key] = raw[key]
            if 'basement' in raw:
                if not isinstance(raw['basement'], bool): raise ValueError('basement must be boolean')
                if 'max_basements' in raw and bool(raw['max_basements']) != raw['basement']: raise ValueError('basement and max_basements conflict')
                b['geometry'].setdefault('max_basements', int(raw['basement']))
            for key in ('usages','basement_usages','usage_shares'):
                if key in raw: b['allocation'][key] = deepcopy(raw[key])
            for key in ('name','systems'):
                if key in raw: b[key] = deepcopy(raw[key])
            if 'gap_after_m' in raw: b['site'] = {'gap_after_m': raw['gap_after_m']}
            if 'facade_style' in raw: b['envelope'] = {'facade': {'style': raw['facade_style']}}
            converted['buildings'].append(b)
        layout = converted
    _fields(layout, {'layout_version','site','defaults','buildings','systems'}, 'layout')
    if type(layout['layout_version']) is not int or layout['layout_version'] != 1:
        raise ValueError('layout_version must be 1')
    defaults = layout.get('defaults', {})
    categories = {'geometry','allocation','envelope','circulation','systems','site'}
    _fields(defaults, categories, 'defaults')
    site = deepcopy(layout.get('site', {}))
    _fields(site, {'gap_m','gaps'}, 'site')
    site.setdefault('gap_m', 20)
    _number(site['gap_m'], 'site.gap_m', zero=True)
    raw_buildings = layout.get('buildings')
    if not isinstance(raw_buildings, list) or not raw_buildings: raise ValueError('buildings must be a nonempty list')
    result = {'layout_version': 1, 'site': site, 'buildings': [], 'systems': {}}
    ids = set()
    for i, raw in enumerate(raw_buildings):
        path = f'buildings[{i}]'
        _fields(raw, categories | {'id','name'}, path)
        bid = _id(raw.get('id'), path+'.id')
        if bid in ids: raise ValueError(path+'.id is duplicated')
        ids.add(bid)
        b = _merge(defaults, raw)
        b.setdefault('name', bid)
        geometry = b.setdefault('geometry', {})
        _fields(geometry, {'relative_length','depth_m','max_floors','max_basements'}, path+'.geometry')
        geometry.setdefault('relative_length', 1)
        geometry.setdefault('depth_m', 15)
        geometry.setdefault('max_basements', 0)
        for key in ('relative_length','depth_m','max_floors','max_basements'):
            _number(geometry.get(key), path+'.geometry.'+key, integer=key in ('max_floors','max_basements'), zero=key=='max_basements')
        allocation = b.setdefault('allocation', {})
        _fields(allocation, {'usages','basement_usages','usage_shares'}, path+'.allocation')
        for group in ('allocation','envelope','circulation','site','systems'):
            if group in b and not isinstance(b[group],dict): raise ValueError(path+'.'+group+' must be a dictionary')
        envelope = b.setdefault('envelope', {})
        _fields(envelope, {'facade','street','courtyard'}, path+'.envelope')
        for side in ('street','courtyard'):
            _fields(envelope.get(side,{}), {'facade'}, path+'.envelope.'+side)
        for side, entry in [('facade', envelope.get('facade', {}))] + [(side, envelope.get(side, {}).get('facade', {})) for side in ('street','courtyard')]:
            if side != 'facade': _fields(envelope.get(side, {}), {'facade'}, path+'.envelope.'+side)
            _fields(entry, {'style'}, path+'.envelope.'+side)
            style = entry.get('style', 'default')
            if style not in ('default','gründerzeit','gruenderzeit','grunderzeit'): raise ValueError(path+'.envelope: unsupported facade style')
        circulation = b.setdefault('circulation', {})
        _fields(circulation, {'kind','shaft_width_m'}, path+'.circulation')
        circulation.setdefault('kind', 'elevator' if i % 2 == 0 else 'stairs')
        if circulation['kind'] not in ('elevator','stairs','none'): raise ValueError(path+'.circulation.kind is unsupported')
        if 'shaft_width_m' in circulation: _number(circulation['shaft_width_m'], path+'.circulation.shaft_width_m')
        local_site = b.setdefault('site', {})
        _fields(local_site, {'street_side','gap_after_m'}, path+'.site')
        local_site.setdefault('street_side', 'left' if i % 2 == 0 else 'right')
        local_site.setdefault('gap_after_m', site['gap_m'])
        if local_site['street_side'] not in ('left','right'): raise ValueError(path+'.site.street_side is unsupported')
        _number(local_site['gap_after_m'], path+'.site.gap_after_m', zero=True)
        # Preserve wildcard precedence across scopes before flattening defaults.
        scopes = [defaults.get('systems',{}), raw.get('systems',{})]
        for scope in scopes: _fields(scope, {'usages','plant','roof'}, path+'.systems')
        if any('systems' in obj for obj in (defaults, raw)):
            mappings = [scope.get('usages',{}) for scope in scopes]
            keys = set().union(*(m.keys() for m in mappings))
            b['systems']['usages'] = {key: {} for key in keys}
            for key in keys:
                for mapping in mappings:
                    b['systems']['usages'][key].update(mapping.get('*',{}))
                    b['systems']['usages'][key].update(mapping.get(key,{}))
        result['buildings'].append(b)
    gaps = site.get('gaps', [])
    if not isinstance(gaps,list): raise ValueError('site.gaps must be a list')
    ordered = [b['id'] for b in result['buildings']]
    seen = set()
    for i,gap in enumerate(gaps):
        path = f'site.gaps[{i}]'
        _fields(gap, {'between','width_m','kind'}, path)
        pair = gap.get('between')
        if not isinstance(pair,list) or len(pair)!=2 or any(v not in ids for v in pair): raise ValueError(path+'.between must reference two building IDs')
        indices = sorted(ordered.index(v) for v in pair)
        if indices[1]-indices[0] != 1 or indices[0] in seen: raise ValueError(path+' must reference a unique adjacent pair')
        seen.add(indices[0])
        _number(gap.get('width_m'), path+'.width_m', zero=True)
        if gap.get('kind','courtyard') not in ('courtyard','street'): raise ValueError(path+'.kind is unsupported')
        result['buildings'][indices[0]]['site']['gap_after_m'] = gap['width_m']
    _fields(layout.get('systems',{}), {'plant'}, 'systems')
    records = []
    for b in result['buildings']:
        if 'systems' in b and 'plant' in b['systems']:
            values = b['systems']['plant']
            if not isinstance(values,list): raise ValueError('systems.plant must be a list')
            for j, value in enumerate(values):
                record = {'kind': value} if isinstance(value,str) else deepcopy(value)
                record.setdefault('id', f"{b['id']}-plant-{j}")
                record.setdefault('location', {'building': b['id'], 'level': 'lowest_floor'})
                record.setdefault('serves', [b['id']])
                records.append(record)
    shared = layout.get('systems',{}).get('plant', [])
    if not isinstance(shared,list): raise ValueError('systems.plant must be a list')
    records.extend(deepcopy(shared))
    from .system_resolution import PLANT
    component_ids = set()
    for i,record in enumerate(records):
        path = f'systems.plant[{i}]'
        _fields(record, {'id','kind','source','location','serves'}, path)
        rid = _id(record.get('id'), path+'.id')
        if rid in component_ids: raise ValueError(path+'.id is duplicated')
        component_ids.add(rid)
        if record.get('kind') not in PLANT | {'heat_pump'}: raise ValueError(path+'.kind is unsupported')
        if 'source' in record and (record['kind'] != 'heat_pump' or record['source'] not in ('unknown','groundwater','ground','air')): raise ValueError(path+'.source is unsupported')
        serves = record.get('serves', [])
        if not isinstance(serves,list) or any(v not in ids for v in serves) or len(serves)!=len(set(serves)): raise ValueError(path+'.serves contains invalid building references')
        location = record.get('location')
        if location is not None:
            _fields(location, {'building','level'}, path+'.location')
            if location.get('building') not in ids: raise ValueError(path+'.location.building is unknown')
            level = location.get('level', 'lowest_floor')
            if not (type(level) is int or isinstance(level,str) and level in ('lowest_floor','roof')): raise ValueError(path+'.location.level is invalid')
            location['level'] = level
    if records or 'plant' in layout.get('systems',{}) or 'plant' in defaults.get('systems',{}) or any('plant' in b.get('systems',{}) for b in raw_buildings):
        result['systems']['plant'] = records
    # Local lists are only legacy rendering hints; canonical records live once at root.
    for b in result['buildings']:
        if 'systems' in b: b['systems'].pop('plant', None)
    return result


def allocation_layout(spec):
    """Internal adapter to the established allocator, not a second public format."""
    result = {'gap_m': spec['site']['gap_m'], 'buildings': []}
    for b in spec['buildings']:
        flat = {'id': b['id'], 'name': b['name'], **deepcopy(b['geometry']), **deepcopy(b['allocation']),
                'gap_after_m': b['site']['gap_after_m'], 'facade_style': b['envelope'].get('facade',{}).get('style','default')}
        # Explicit empty plant list prevents duplicating scenario-wide hints.
        flat['systems'] = {**deepcopy(b.get('systems', {})), 'plant': []}
        result['buildings'].append(flat)
    return result
