"""Portable annual assessment reader using shared PEExcel report templates."""
from pathlib import Path
import gzip
import json
import math
import hashlib
from html import escape

import nbformat
from nbconvert.filters.markdown import markdown2html
from plotly.offline import get_plotlyjs
from plotly.utils import PlotlyJSONEncoder

from pexl import Project, reporting
from pexl.plot import plotly
from pexl.schema.current import SCHEMA_VERSION, SCHEMA_META
from pexl.analysis.targets import target

ROOT = Path(__file__).resolve().parents[1]
SECTOR = ROOT / 'data/exports/typologies/building_sector/building_sector_project.xlsx'
FILTERS = [('geometry', 'Geometrie', 'preset_recorded_geometry'),
           ('hulls', 'Baualter / Hülle', 'preset_recorded_hulls'),
           ('pv', 'PV-Dachflächenanteil', 'PV_roof_share'),
           ('flexibility', 'Flexibilität', 'preset_recorded_flexibility_system'),
           ('family', 'Heizungsfamilie', None),
           ('heating', 'Heizung im Detail', 'preset_recorded_heating_system')]
CONTEXT = ('cfd_fPE', 'cfd_A', 'cfd_dx', 'cfd_EUI', 'cfd_cutoff', 'cfr_budget',
           'FSI', 'renovation_share', 'GFA_total', 'NFA_total',
           'context_factor_density', 'context_factor_renovation', 'PEI_cf_density_pos',
           'PEI_cf_density_neg', 'PEI_cf_renovation', 'PEI_virtual_demand',
           'PEI_virtual_supply', 'PEI_balance')
ANALYSIS = ('QH', 'QC', 'preset_recorded_hulls', 'preset_recorded_geometry',
            'preset_recorded_heating_system', 'PV_roof_share')


def _analysis_templates(view, names, columns):
    """Reuse Python plotting functions, keeping only style and scenario bindings.

    Numeric vectors reference the shared annual value matrix. The one derived
    final-energy report balance stays in its trace; it has no simulated alias.
    """
    heating = 'preset_recorded_heating_system'
    plots = [
        ('pe_scatter', 'PE-Bedarf versus PE-Deckung', 'PEI_virtual_demand', 'PEI_virtual_supply',
         plotly.scenario_scatter(view, 'PEI_virtual_demand', 'PEI_virtual_supply',
            color=heating, symbol='preset_recorded_geometry', size='GFA_total')),
        ('heating_distribution', 'Heizwärmebedarf nach Hülle', 'preset_recorded_hulls', 'QH',
         plotly.scenario_distribution(view, 'QH', by='preset_recorded_hulls')),
        ('cooling_distribution', 'Kühlbedarf nach Geometrie', 'preset_recorded_geometry', 'QC',
         plotly.scenario_distribution(view, 'QC', by='preset_recorded_geometry', kind='violin')),
        ('pe_gfz', 'Primärenergiesaldo gegenüber GFZ', 'FSI', 'PEI_balance',
         plotly.scenario_scatter(view, 'FSI', 'PEI_balance', color=heating)),
        ('ee_gfz', 'Endenergie-Reportsaldo gegenüber GFZ', 'FSI', None,
         plotly.report_balance_scatter(view, 'final_energy_balance', 'FSI', color=heating)),
    ]
    ids = {name: i for i, name in enumerate(names)}
    result = {}
    for key, title, x, y, fig in plots:
        traces = []
        for trace in fig.data:
            item = trace.to_plotly_json()
            item['meta'] = dict(ids=[ids[n] for n in trace.hovertext], x=columns[x],
                                y=columns[y] if y else None,
                                size=columns['GFA_total'] if key == 'pe_scatter' else None)
            if y is None:
                item['meta']['derived_y'] = list(trace.y)
            for field in ('x', 'y', 'hovertext', 'customdata'):
                item.pop(field, None)
            item.get('marker', {}).pop('size', None)
            item['hovertemplate'] = '%{hovertext}<br>%{x}<br>%{y:.2f}<extra>%{fullData.name}</extra>'
            traces.append(item)
        result[key] = dict(title=title, data=traces, layout=fig.layout.to_plotly_json())
    return result


def _clean(value):
    if value is None or isinstance(value, float) and not math.isfinite(value):
        return None
    return value


def context_values(values, *, bgf=None, gf=None, renovation=None):
    """Assessment overlay following stored schema signs; originals stay intact.

    Renovation is the NFA-weighted overall percentage. No energy flows change.
    Omitted parameters preserve the corresponding exported assessment.
    """
    result = dict(values)
    if bgf is not None or gf is not None:
        if bgf is None or gf is None or not all(math.isfinite(x) and x > 0 for x in (bgf, gf)):
            raise ValueError('BGF and GF must both be finite and positive')
        result['FSI'] = bgf / gf
        if result['FSI'] + values['cfd_dx'] <= 0:
            raise ValueError('Invalid density denominator')
        density = -float(target(result['FSI'], A=values['cfd_A'], dx=values['cfd_dx'],
                                EUI=values['cfd_EUI'], fPE=values['cfd_fPE'], cutoff=values['cfd_cutoff']))
        result.update(context_factor_density=density, PEI_cf_density_pos=max(density, 0),
                      PEI_cf_density_neg=min(density, 0))
    if renovation is not None:
        if not math.isfinite(renovation) or not 0 <= renovation <= 100:
            raise ValueError('Renovation must be between 0 and 100 percent')
        result['renovation_share'] = renovation / 100
        result['context_factor_renovation'] = result['PEI_cf_renovation'] = values['cfr_budget'] * renovation / 100
    dn = result['PEI_cf_density_neg'] - values['PEI_cf_density_neg']
    dp = result['PEI_cf_density_pos'] - values['PEI_cf_density_pos']
    dr = result['PEI_cf_renovation'] - values['PEI_cf_renovation']
    result['PEI_virtual_demand'] = values['PEI_virtual_demand'] + dn
    result['PEI_virtual_supply'] = values['PEI_virtual_supply'] + dp + dr
    result['PEI_balance'] = values['PEI_balance'] + dn + dp + dr
    return result


def browser_data(project):
    """Page payload: existing report frames plus shared render templates."""
    names = [n for n in project.column_names() if n not in {'Default', 'color', 'pattern'}]
    if not names:
        raise ValueError('Der Projektexport enthält keine auswählbaren Szenarien.')
    selected = Project()
    for name in names:
        selected.add_scenario(project[name])
    reports = {key: reporting.materialize(selected.view, chart) for key, chart in
               [('pe', 'primary_energy_balance'), ('thg', 'gwp_ee')]}
    variables = list(dict.fromkeys([s['var_name'] for r in reports.values() for s in r['series']] + list(CONTEXT) + list(ANALYSIS)))
    columns = {key: i for i, key in enumerate(variables)}
    templates = {}
    for key, report in reports.items():
        sample = dict(report, frame=report['frame'].iloc[:1].copy())
        sample['frame']['Variant'] = 'Szenario'
        figure = plotly.render(sample, **({'budget': 320} if key == 'thg' else {})).to_dict()
        labels = {s['label']: s for s in report['series']}
        for trace in figure['data']:
            series = labels.get(trace['name'])
            if series:
                trace['meta'] = dict(column=columns[series['var_name']], role=series['role'])
                trace['legendgroup'] = series['role']
            trace['y'] = [None] * len(trace.get('y', []))
            trace.pop('text', None)
        templates[key] = figure
    scenarios = []
    for i, scenario in enumerate(selected):
        attrs = {}
        for key, label, variable in FILTERS:
            if variable:
                value = _clean(getattr(scenario.v, variable, None))
                attrs[key] = (f'{100 * value:g} %' if key == 'pv' and value is not None else str(value)) if value is not None else 'Nicht aufgezeichnet'
        # Group from recorded IN label; retain detail verbatim, no preset list.
        attrs['family'] = attrs['heating'].split(' (', 1)[0]
        values = [_clean(getattr(scenario.v, v, None)) for v in variables]
        scenarios.append(dict(id=i, name=scenario.column_name, filters=attrs, values=values))
    defaults = [i for i, name in enumerate(names) if '6-Stöckig' in name and
                any(age in name for age in ('bis 1944', '1990-1999', 'ab 2020'))]
    return dict(scenarios=scenarios, defaults=defaults or list(range(min(3, len(names)))),
                columns=columns, templates=templates, schema=SCHEMA_VERSION,
                analysis=_analysis_templates(selected.view, names, columns),
                filters=[dict(key=k, label=l, source=v) for k, l, v in FILTERS],
                units={v: getattr(SCHEMA_META, v).unit for v in variables})


def build(output=None, *, source=None, project=None):
    output = Path(output or ROOT / 'notebooks/local_exports/assessment_explained/index.html')
    source = Path(source) if source is not None else SECTOR
    project = project if project is not None else Project.from_excel(source, unknown='raise' if source == SECTOR else 'ignore')
    data = browser_data(project)
    data['source'] = {'file': source.name, 'sha256': hashlib.sha256(source.read_bytes()).hexdigest() if source.exists() else None}
    notebook = nbformat.read(ROOT / 'notebooks/howto_assessment_explained.ipynb', as_version=4)
    prose = {c.metadata['section']: markdown2html(c.source) for c in notebook.cells
             if c.cell_type == 'markdown' and 'section' in c.metadata}
    prose['source'] = '<p><strong>Datengrundlage:</strong> ' + escape(source.name) + '</p>' + prose['source']
    template = (ROOT / 'scripts/assessment_explained.html').read_text(encoding='utf-8')
    for key, value in prose.items():
        template = template.replace('{{' + key + '}}', value)
    payload = json.dumps(data, cls=PlotlyJSONEncoder, ensure_ascii=False, allow_nan=False, separators=(',', ':')).replace('<', '\\u003c')
    template = template.replace('{{DATA}}', payload).replace('{{PLOTLY}}', get_plotlyjs())
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template, encoding='utf-8')
    metrics = dict(scenarios=len(data['scenarios']), payload_bytes=len(payload.encode()),
                   payload_gzip_bytes=len(gzip.compress(payload.encode(), mtime=0)),
                   html_bytes=output.stat().st_size,
                   html_gzip_bytes=len(gzip.compress(template.encode(), mtime=0)))
    print(json.dumps(metrics))
    return output


def publish_notebook(output_root):
    """Publish the executed workflow and its Plotly outputs without rerunning it."""
    from nbconvert import HTMLExporter
    import plotly.io as pio
    output_root = Path(output_root)
    notebook = nbformat.read(ROOT / 'notebooks/howto_building_sector_results.ipynb', as_version=4)
    download = output_root / 'downloads/howto_building_sector_results.ipynb'
    download.parent.mkdir(parents=True, exist_ok=True)
    nbformat.write(notebook, download)
    for cell in notebook.cells:
        for output in cell.get('outputs', []):
            data = output.get('data', {})
            if 'application/vnd.plotly.v1+json' in data:
                data['text/html'] = pio.to_html(data.pop('application/vnd.plotly.v1+json'), full_html=False, include_plotlyjs=False)
            if 'text/html' in data:
                data['text/html'] = data['text/html'].replace('local_exports/building_sector/quickcheck.html', '../assets/assessment-explained/index.html')
    html, _ = HTMLExporter().from_notebook_node(notebook)
    html = html.replace('</head>', '<script>' + get_plotlyjs() + '</script></head>')
    reading = output_root / 'tutorials/building_sector_results.html'
    reading.parent.mkdir(parents=True, exist_ok=True)
    reading.write_text(html, encoding='utf-8')
    return reading


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Statischen PEExcel Quick-Check erzeugen')
    parser.add_argument('--source', type=Path, help='Projektexport (.xlsx)')
    parser.add_argument('--output', type=Path, help='Ziel-HTML-Datei')
    args = parser.parse_args()
    print(build(args.output, source=args.source))
