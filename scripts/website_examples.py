"""Configured real exports, shared by publication notebooks and Quarto.

No simulation, inferred channels or replacement results. Plotly remains the
renderer; selected result tables/figures are disposable publication artifacts.
"""
from pathlib import Path
from functools import lru_cache
import hashlib

import numpy as np
import pandas as pd
import yaml

from pexl import Project, reporting
from pexl.analysis.temporal import add_season, SEASONS
from pexl.plot import electricity_balance, electricity_balance_facets
from pexl.plot import plotly
from pexl.plot.export import export_figure
from pexl.schema.current import SCHEMA_VERSION, ATTR_NAME_MAP

ROOT = Path(__file__).resolve().parents[1]
CHARTS = ('heat_balance', 'final_energy_balance', 'primary_energy_balance', 'gwp_ee')
FLOW_POSITIVE = ('E_grid', 'PV_total_direct_use', 'PV_total_flex_use')
FLOW_NEGATIVE = ('PV_to_Egrid',)
FLOW_LABELS = {'E_grid': 'Konventioneller Netzbezug',
               'PV_total_direct_use': 'PV-Direktnutzung',
               'PV_total_flex_use': 'Flexible PV-Nutzung',
               'PV_to_Egrid': 'PV-Netzeinspeisung'}
FLOW_COLORS = {'E_grid': '#950f53', 'PV_total_direct_use': '#43894a',
               'PV_total_flex_use': '#9fc966', 'PV_to_Egrid': '#58a9b8'}
# Investigation checklist, not an alternative simulation schema.
FLOW_GROUPS = {
    'Elektrische Verbraucher': ('E_plugAuxLight', 'Ev_min', 'Eh_min', 'Ec_min', 'Edhw_min', 'Eev_min'),
    'Flexible HKLS-Aufwendungen': ('Eh_flex_1el_final', 'Eh_flex_3el_final', 'Ec_flex_1el_final',
                                 'Ec_flex_3el_final', 'Edhw1_flex_final', 'Edhw2_flex_final'),
    'Signalgesteuerter Netzbezug': ('VRGrid_total_min_use', 'VRGrid_total_flex_use', 'VRGrid_to_Eev_flex'),
    'Speicher und Rückspeisung': ('Batt_to_user', 'Batt_to_HVAC_min', 'Batt_to_Eev_min',
                                'PV_to_Batt', 'VRGrid_to_Batt', 'Eev_to_user', 'Eev_to_HVAC'),
    'PV und konventioneller Netzbezug': ('PV_yield',) + FLOW_POSITIVE + FLOW_NEGATIVE,
}


def configuration(path=None):
    path = Path(path or ROOT / 'website/_examples.yml')
    config = yaml.safe_load(path.read_text(encoding='utf-8'))
    ids = [e['id'] for e in config['examples']]
    if len(set(ids)) != len(ids) or not ids or any(not i for i in ids):
        raise ValueError('Example IDs must be nonempty and unique')
    for entry in [*config['examples'], config['dynamic_example']]:
        file = (ROOT / entry['file']).resolve()
        if not file.is_relative_to(ROOT) or not file.is_file():
            raise ValueError(f'Invalid example file: {entry["file"]}')
        if not entry.get('scenario') or not entry.get('label'):
            raise ValueError('Exact scenario and label are required')
    return config


@lru_cache(maxsize=8)
def _read(file, mtime):
    return Project.from_excel(file)


def load_entry(entry):
    path = ROOT / entry['file']
    project = _read(str(path), path.stat().st_mtime_ns)
    if project.warnings:
        raise ValueError(f'{path.name}: {project.warnings}')
    if project.column_names() != [entry['scenario']]:
        raise ValueError(f'Expected exactly {entry["scenario"]!r}; found {project.column_names()}')
    return project


def load_examples(config=None):
    config = config or configuration()
    project = Project()
    for entry in config['examples']:
        project.add_scenario(load_entry(entry).scenarios[0])
    return project


def numeric_frame(frame, columns):
    missing = set(columns) - set(frame.columns)
    if missing:
        raise ValueError(f'Missing exported channels: {sorted(missing)}')
    values = frame[list(columns)].apply(pd.to_numeric, errors='raise')
    if not np.isfinite(values.to_numpy(dtype=float)).all():
        raise ValueError('Missing or non-finite result values; zero substitution is not permitted')
    return values


def hourly_frame(scenario):
    frame = scenario.timeseries.to_frame().copy()
    index = pd.DatetimeIndex(pd.to_datetime(frame['date']))
    if index.hasnans or index.has_duplicates or not index.is_monotonic_increasing:
        raise ValueError('Invalid hourly time axis')
    if len(index) < 2 or not (index.to_series().diff().dropna() == pd.Timedelta(hours=1)).all():
        raise ValueError('Expected a continuous one-hour timestep')
    frame.index = index
    if not (frame['Monat_nr'].to_numpy() == index.month).all():
        raise ValueError('Month metadata differs from timestamps')
    if not (frame['hour_of_the_day'].to_numpy() == index.hour).all():
        raise ValueError('Hour metadata differs from timestamps')
    return frame


def annual_reports(project=None):
    project = project or load_examples()
    # These examples are all-electric. Do not silently mislabel future mixed systems.
    for s in project:
        if str(s.v.tool_version).replace('.', '_') != SCHEMA_VERSION:
            raise ValueError(f'{s.column_name}: unsupported tool/schema version {s.v.tool_version}')
        for key in ('EUI_district_heating', 'EUI_natural_gas', 'EUI_biomass', 'EUI_other', 'GWP_ee_PV'):
            value = getattr(s.v, key)
            if value is None or not np.isfinite(value) or abs(value) > 1e-9:
                raise ValueError(f'{s.column_name}: {key} requires a reviewed publication boundary')
    reports = {name: reporting.materialize(project.view, name) for name in CHARTS}
    for report in reports.values():
        if not report['series']:
            raise ValueError(f'Empty report: {report["chart_name"]}')
        numeric_frame(report['frame'], [s['var_name'] for s in report['series']])
    return reports


def balance_checks(reports):
    rows = []
    for name, report in reports.items():
        frame = report['frame']
        if name == 'gwp_ee':
            parts = [s['var_name'] for s in report['series'] if s['role'] in ('Baulich', 'Betrieblich')]
            residual = frame[parts].sum(axis=1) - frame['GWP_lc_total']
        else:
            pos = [s['var_name'] for s in report['series'] if s['role'] == 'Deckung']
            neg = [s['var_name'] for s in report['series'] if s['role'] == 'Bedarf']
            residual = frame[pos].sum(axis=1) - frame[neg].sum(axis=1)
        for variant, value in zip(frame['Variant'], residual):
            rows.append({'Diagramm': name, 'Variante': variant, 'Differenz': float(value),
                         'Bedeutung': 'Komponentensumme minus Exportgesamtwert' if name == 'gwp_ee'
                         else 'Deckung minus Bedarf (PE: Bewertungsbilanz, kein Schließkriterium)'})
    return pd.DataFrame(rows)


def input_differences(project):
    schema = pd.read_csv(ROOT / 'data/schemas/1.13.1_dev/IN.csv', sep=';')
    rows = []
    for _, row in schema.iterrows():
        key = row['var_name']
        if key not in ATTR_NAME_MAP:
            continue
        values = [getattr(s.v, ATTR_NAME_MAP[key]) for s in project]
        if len({str(v) for v in values}) <= 1:
            continue
        rows.append({'Variable': key, 'Bezeichnung': row['label_de'],
                     **dict(zip(project.column_names(), values))})
    return pd.DataFrame(rows)


def flow_inventory(scenario):
    frame = hourly_frame(scenario)
    rows = []
    for group, keys in FLOW_GROUPS.items():
        for key in keys:
            present = key in frame
            values = numeric_frame(frame, [key])[key] if present else None
            rows.append({'Gruppe': group, 'Kanal': key, 'Exportiert': present,
                         'Stunden ungleich null': int(values.ne(0).sum()) if present else None,
                         'Summe Exportwerte': float(values.sum()) if present else None})
    return pd.DataFrame(rows)


def dynamic_figures(scenario):
    frame = hourly_frame(scenario)
    columns = list(FLOW_POSITIVE + FLOW_NEGATIVE)
    values = numeric_frame(frame, columns)
    if (values < -1e-8).any().any():
        raise ValueError('Directional channels must be nonnegative before signed display')
    # Wh/m² per 1 h interval / 1 h = mean W/m², no energy/power shortcut for other steps.
    prepared = add_season(frame)
    seasonal = prepared.groupby(['season', 'hour_of_the_day'], observed=True)[columns].mean().reset_index()
    kwargs = dict(positive=FLOW_POSITIVE, negative=FLOW_NEGATIVE,
                  labels=FLOW_LABELS, colors=FLOW_COLORS, omit_empty=True)
    facets = electricity_balance_facets(seasonal, facet='season',
        facet_order=[s[0] for s in SEASONS], facet_labels={s[0]:s[1].de for s in SEASONS},
        x='hour_of_the_day', title='Aspern F7 · Saisonale mittlere Tagesprofile',
        x_title='Tagesstunde', y_title='Mittlere Leistung [W/m² NGF]', **kwargs)
    # The data remain hourly; presets only change the visible range.
    hourly = electricity_balance(frame, x='date', title='Aspern F7 · Elektrische Flussprofile',
        x_title='Exportierte Zeitachse', y_title='Mittlere Stundenleistung [W/m² NGF]', **kwargs)
    year = frame.index[0].year
    hourly.update_layout(updatemenus=[{'type':'buttons', 'direction':'right', 'x':0, 'y':1.15,
        'buttons':[{'label':label, 'method':'relayout', 'args':[{'xaxis.range':interval, 'xaxis.autorange':False}]}
            for label, interval in [('Jännerwoche',[f'{year}-01-08', f'{year}-01-15']),
                                    ('Juliwoche',[f'{year}-07-09', f'{year}-07-16'])]] +
        [{'label':'Gesamtjahr','method':'relayout','args':[{'xaxis.autorange':True}]}]}])
    hourly.update_xaxes(range=[f'{year}-07-09', f'{year}-07-16'], rangeslider_visible=True)
    # Reserve independent space for title/presets and slider/provenance.
    hourly.update_layout(margin=dict(l=90, r=260, t=160, b=240),
                         title=dict(y=0.98, x=0.06),
                         xaxis_rangeslider_thickness=0.10)
    return {'f7_seasons':facets, 'f7_hourly':hourly}


def provenance(entries, convention):
    return {'source': '; '.join(e['file'] for e in entries),
            'scenario': '; '.join(e['scenario'] for e in entries),
            'model_version': '; '.join(str(load_entry(e).scenarios[0].v.tool_version) for e in entries),
            'schema_version': SCHEMA_VERSION,
            'calculated_at': 'Gespeicherte Exportergebnisse; Berechnungszeitpunkt nicht belegt',
            'convention': convention,
            'sha256_prefix': '; '.join(hashlib.sha256((ROOT/e['file']).read_bytes()).hexdigest()[:16] for e in entries)}


def build(output=None, formats=('html','svg','png')):
    output = Path(output or ROOT/'website/assets/results')
    output.mkdir(parents=True, exist_ok=True)
    config = configuration()
    project = load_examples(config)
    reports = annual_reports(project)
    checks = balance_checks(reports)
    closure = checks.loc[checks['Diagramm'] != 'primary_energy_balance', 'Differenz']
    if closure.abs().gt(1e-6).any():
        raise ValueError('Annual heat/end-energy or GHG component reconciliation failed')
    labels = {e['scenario']: e['label'] for e in config['examples']}
    for name, report in reports.items():
        shown = dict(report)
        shown['frame'] = report['frame'].copy()
        shown['frame']['Variant'] = shown['frame']['Variant'].map(labels)
        shown['series'] = [s for s in report['series'] if report['frame'][s['var_name']].abs().gt(1e-10).any()]
        fig = plotly.render(shown)
        convention = 'Jahreswerte; NGF-Bezug. Bedarf und Deckung in getrennten Säulen, positive Beträge.'
        if name == 'gwp_ee':
            convention = 'Exportierte THG-Modellbilanz 2025–2075; kg CO₂eq/m² BGF; EE=Herstellung, OE=Betrieb; negative Beiträge bleiben erhalten. PV-LCA in diesen Exporten null.'
        if name == 'final_energy_balance':
            convention += ' Elektrische lokale Nutzung; ohne Einspeisung und externe EV-Ladung. Übrige Energieträger in diesen Varianten null.'
        for fmt in formats:
            export_figure(fig, output/f'{name}.{fmt}', provenance=provenance(config['examples'], convention), width=1500)
        table = report['frame'].rename(columns={s['var_name']:s['label'] for s in report['series']})
        table.to_csv(output/f'{name}.csv',index=False,encoding='utf-8-sig')
    differences = input_differences(project)
    differences.to_csv(output/'input_differences.csv',index=False,encoding='utf-8-sig')
    checks.to_csv(output/'balance_checks.csv',index=False,encoding='utf-8-sig')
    dynamic = load_entry(config['dynamic_example']).scenarios[0]
    for name, fig in dynamic_figures(dynamic).items():
        for fmt in formats:
            if name == 'f7_hourly' and fmt != 'html':
                continue
            export_figure(fig,output/f'{name}.{fmt}',width=1500,
                height=1100 if name == 'f7_hourly' else 900,
                provenance=provenance([config['dynamic_example']],
                    'Teilflussdarstellung, keine geschlossene Verbrauchsbilanz. PV-Nutzung und konventioneller Netzbezug positiv; Einspeisung negativ. Wh/m² je 1 h / 1 h = W/m² NGF.'))
    for s in [*project.scenarios, dynamic]:
        flow_inventory(s).to_csv(output/f'channels-{s.column_name}.csv',index=False,encoding='utf-8-sig')
    # Accessible tables use the same report data, not a second calculation.
    sections = ['<!doctype html><html lang="de"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ergebnistabellen</title><style>body{font:16px/1.5 system-ui;padding:20px;color:#243746}table{border-collapse:collapse}td,th{padding:8px;border:1px solid #ccd6d8}section{overflow:auto}h2{font-size:22px}</style>']
    for name, report in reports.items():
        sections.append(f'<h2>{report["title"]} · {report["unit"]}</h2><section>'+report['frame'].to_html(index=False,float_format=lambda x:f'{x:.3f}')+'</section>')
    sections += ['<h2>Abweichende IN-Werte</h2><p>Exportierte Eingaben einschließlich abgeleiteter IN-Werte; keine Aussage über alleinige Maßnahmenursachen.</p><section>'+differences.to_html(index=False)+'</section>',
                 '<h2>Bilanzdifferenzen</h2><section>'+checks.to_html(index=False,float_format=lambda x:f'{x:.6f}')+'</section></html>']
    (output/'tables.html').write_text(''.join(sections),encoding='utf-8')
    return reports, checks


if __name__ == '__main__':
    build()
