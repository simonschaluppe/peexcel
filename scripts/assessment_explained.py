"""Build the portable assessment reader from notebook prose and existing plots.

The generated HTML is disposable: no new report schema or saved data model.
Browser code only selects and joins already rendered Plotly figures.
"""
from pathlib import Path
import json
from html import escape

import nbformat
from nbconvert.filters.markdown import markdown2html
from plotly.offline import get_plotlyjs
from plotly.utils import PlotlyJSONEncoder

from pexl import Project, reporting
from pexl.io.excel import read_project
from pexl.plot import plotly

ROOT = Path(__file__).resolve().parents[1]


def build(output=None, *, source=None):
    """Render an existing project export; source defaults to the teaching example.

    A keyword-only source reuses the existing Excel reader and figure pipeline,
    without a second data format or per-project configuration file.
    """
    output = Path(output or ROOT / 'notebooks/local_exports/assessment_explained/index.html')
    source = Path(source) if source is not None else ROOT / 'data/exports/Klimsta_Abschlussprojekt_Varianten_V3.xlsx'
    project = read_project(source, unknown='ignore')
    names = [n for n in project.column_names() if n not in {'Default', 'color', 'pattern'}]
    if not names:
        raise ValueError('Der Projektexport enthält keine auswählbaren Szenarien.')
    figures = []
    for index, name in enumerate(names):
        selected = Project()
        selected.add_scenario(project[name])
        item = {'name': name, 'id': index, 'plots': {}}
        for key, chart_name in [('pe', 'primary_energy_balance'), ('thg', 'gwp_ee')]:
            report = reporting.materialize(selected.view, chart_name)
            report['frame'] = report['frame'].copy()
            report['frame']['Variant'] = name
            fig = plotly.render(report, annotate=True, **({'budget': 320} if key == 'thg' else {}))
            roles = {series['label']: series.get('role', '') for series in report['series']}
            for trace in fig.data:
                trace.legendgroup = roles.get(trace.name, 'Orientierung')
            item['plots'][key] = fig.to_dict()
        figures.append(item)
    defaults = [i for i, name in enumerate(names) if '6-Stöckig' in name and
                any(age in name for age in ('bis 1944', '1990-1999', 'ab 2020'))]
    notebook = nbformat.read(ROOT / 'notebooks/howto_assessment_explained.ipynb', as_version=4)
    prose = {c.metadata['section']: markdown2html(c.source) for c in notebook.cells
             if c.cell_type == 'markdown' and 'section' in c.metadata}
    prose['source'] = '<p><strong>Datengrundlage:</strong> ' + escape(source.name) + '</p>' + prose['source']
    template = (ROOT / 'scripts/assessment_explained.html').read_text(encoding='utf-8')
    for key, value in prose.items():
        template = template.replace('{{' + key + '}}', value)
    payload = json.dumps({'scenarios': figures, 'defaults': defaults or list(range(min(3, len(names))))},
                         cls=PlotlyJSONEncoder, ensure_ascii=False).replace('<', '\\u003c')
    template = template.replace('{{DATA}}', payload).replace('{{PLOTLY}}', get_plotlyjs())
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(template, encoding='utf-8')
    return output


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Projekt-Varianten-Explorer aus einem PEExcel-Export erzeugen')
    parser.add_argument('--source', type=Path, help='Projektexport (.xlsx)')
    parser.add_argument('--output', type=Path, help='Ziel-HTML-Datei')
    args = parser.parse_args()
    print(build(args.output, source=args.source))
