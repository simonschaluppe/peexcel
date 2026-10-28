"""Render active IN/OUT metadata as searchable Quarto fragments, without project values."""
from collections import defaultdict
from html import escape
from pathlib import Path
import hashlib
import json

from pexl.schema import current

ROOT = Path(__file__).resolve().parents[1]
# Explicit website snapshot selection, independent of future Python preset APIs.
PRESET_SNAPSHOT = ROOT / 'src/pexl/schema/generated/presets_1_13_1_dev.json'


def export_preset_snapshot(workbook, output=PRESET_SNAPSHOT):
    """Read exported tables; never open Excel, run macros or change the workbook."""
    import openpyxl
    path = Path(workbook)
    wb = openpyxl.load_workbook(path, read_only=True, data_only=False)
    try:
        meta = dict(list(wb['META'].values)[1:])
        rows = list(wb['IN'].values)
        fields = rows[0]
        variables = {r[fields.index('var_name')]: dict(zip(fields, r)) for r in rows[1:] if r[fields.index('var_name')]}
        tables = []
        for sheet in wb:
            cells = list(sheet.rows)
            header = [c.value for c in cells[0]]
            if 'PRESETS>' not in header or 'var_name' not in header:
                continue
            vi, start = header.index('var_name'), header.index('PRESETS>') + 1
            records, row_numbers = {}, {}
            for row_number, row in enumerate(cells[1:], 2):
                key = row[vi].value
                if key is None:
                    continue
                if key in records:
                    raise ValueError(f'Duplicate variable: {sheet.title}/{key}')
                records[key] = row
                row_numbers[key] = row_number
            presets = []
            for col in range(start, len(header)):
                if header[col] is None:
                    continue
                values, locations = {}, {}
                for key, row in records.items():
                    if key in ('dropdown_name', 'description', 'unit'):
                        continue
                    cell = row[col]
                    if cell.data_type in ('f', 'e'):
                        raise ValueError(f'Unresolved formula/error: {sheet.title}!{cell.coordinate}')
                    values[key] = cell.value
                    locations[key] = f'{openpyxl.utils.get_column_letter(col + 1)}{row_numbers[key]}'
                get = lambda key: records[key][col].value if key in records else None
                presets.append(dict(name=str(header[col]), display_name=get('dropdown_name'),
                                    description=get('description'), unit=get('unit'), values=values, cells=locations))
            labels = {}
            for key, row in records.items():
                if key in ('dropdown_name', 'description', 'unit'):
                    continue
                source = variables.get(key, {})
                fallback = row[header.index('label_de')].value if 'label_de' in header else row[0].value
                labels[key] = dict(label=source.get('label_de') or fallback or key,
                                   unit=source.get('unit'), in_schema=key in variables)
            tables.append(dict(name=sheet.title, variables=labels, presets=presets))
        result = dict(tool_version=meta['tool_version'], source=path.relative_to(ROOT).as_posix(),
                      source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                      exported_at=str(meta.get('created_at', '')), tables=tables)
        result['content_sha256'] = hashlib.sha256(json.dumps(tables, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        output = Path(output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        return output
    finally:
        wb.close()


def preset_anchor(table, name=None):
    """Snapshot-local links; names are not promised stable across Excel versions."""
    suffix = '' if name is None else '-' + hashlib.sha256(name.encode()).hexdigest()[:12]
    return 'preset-' + table + suffix


def build_presets(output=None, snapshot=PRESET_SNAPSHOT):
    """Render only the explicitly selected snapshot and shared editorial notes."""
    import yaml
    data = json.loads(Path(snapshot).read_text(encoding='utf-8'))
    notes = yaml.safe_load((ROOT / 'website/_preset-notes.yml').read_text(encoding='utf-8'))
    tables = {t['name']: t for t in data['tables']}
    if set(notes) != set(tables):
        raise ValueError(f'Review renamed/new tables: {set(notes) ^ set(tables)}')
    out = Path(output) if output else ROOT / 'website/assets'
    out.mkdir(parents=True, exist_ok=True)
    esc = lambda value: escape(str(value))
    count = sum(len(t['presets']) for t in tables.values())
    parts = [f'<section class="schema-catalog" data-source="PRESET" data-item-label="Preset-Spalten">',
             f'<p><strong>Stand: {esc(data["tool_version"])} · {len(tables)} Tabellen · {count} Preset-Spalten</strong><br>Excel-Export: {esc(data["exported_at"])}. Entwicklungsstand, noch nicht als Release freigegeben.</p>',
             '<form class="catalog-controls" hidden><label>Presets und Werte suchen<input id="preset-query" type="search" placeholder="z. B. Wärmepumpe oder Nutzerstrom"></label><label>Eingabegruppe<select id="preset-domain"><option value="*">Alle Gruppen</option>']
    for name, note in notes.items():
        parts.append(f'<option value="{esc(name)}">{esc(note["title"])}</option>')
    parts += ['</select></label><select id="preset-entity" hidden aria-label="Zuordnung"><option value="*">Alle</option></select><div class="catalog-actions"><button type="reset">Zurücksetzen</button><button type="button" id="preset-expand">Alle aufklappen</button><button type="button" id="preset-collapse">Alle zuklappen</button></div></form><p id="preset-count" aria-live="polite"></p><p id="preset-empty" hidden>Keine passenden Presets gefunden.</p>']
    help_by_page = {}
    for name, note in notes.items():
        table = tables[name]
        parts.append(f'<details class="out-domain" data-domain="{esc(name)}" id="{preset_anchor(name)}"><summary>{esc(note["title"])} <span class="out-domain-count"></span></summary><p>{esc(note["text"])}</p><p>Excel-Tabelle: <code>{esc(name)}</code></p><div class="catalog-table"><table><thead><tr><th>Preset / Auswahlname</th><th>Belegung und Herkunft</th></tr></thead><tbody>')
        for preset in table['presets']:
            name_p = preset['name']
            title = preset['display_name'] if preset['display_name'] is not None else name_p
            details = []
            for key, value in preset['values'].items():
                m = table['variables'][key]
                shown = 'Nicht gesetzt – vorhandenen Wert beibehalten' if value is None else ('Ja' if value is True else 'Nein' if value is False else str(value))
                unit = m['unit'] or preset['unit'] or 'Einheit nicht hinterlegt'
                attr = current.ATTR_NAME_MAP.get(key)
                linked = attr and getattr(current.SCHEMA_META, attr).source == 'IN'
                label = f'<span data-in-var="{esc(key)}">{esc(m["label"])}</span>' if linked else esc(m['label'])
                details.append(f'<dt>{label} <code>{esc(key)}</code></dt><dd>{esc(shown)} <span class="text-muted">[{esc(unit)}] · {esc(preset["cells"][key])}</span></dd>')
            parts.append(f'<tr id="{preset_anchor(name, name_p)}" data-entity=""><th scope="row"><a href="#{preset_anchor(name, name_p)}">{esc(title)}</a><br><small>Spaltenname: {esc(name_p)}</small></th><td><p>{esc(preset["description"] or "")}</p>{"<p>Einheit laut Presettabelle: " + esc(preset["unit"]) + "</p>" if preset["unit"] else ""}<details class="out-meta"><summary>{sum(v is not None for v in preset["values"].values())} gesetzte Werte · vollständige Belegung ansehen</summary><dl>{"".join(details)}</dl></details></td></tr>')
        parts.append('</tbody></table></div></details>')
        for page in note.get('pages', []):
            help_by_page.setdefault(page, []).append(f'- **[{note["title"]}](preset-catalog.qmd#{preset_anchor(name)}):** {note["text"]}')
    parts.append(f'<p>Quelle: <code>{esc(data["source"])}</code><br>Inhaltskennung: <code>{data["content_sha256"][:16]}</code></p><noscript>Ohne JavaScript lassen sich alle Gruppen und Werte manuell aufklappen.</noscript></section>')
    (out / 'preset-catalog.qmd').write_text('```{=html}\n' + '\n'.join(parts) + '\n```\n', encoding='utf-8')
    for page, lines in help_by_page.items():
        (out / f'preset-help-{page}.qmd').write_text('::: {.callout-note collapse=true title="Noch keine eigenen Werte? Standardfälle nutzen"}\n\n' + '\n\n'.join(lines) + '\n\nPrüfe die übernommenen Werte für dein Projekt. [So wendest du Presets an](presets.qmd).\n\n:::\n', encoding='utf-8')
    return out / 'preset-catalog.qmd'
# Display translations only: the original domain keys remain visible and searchable.
DOMAIN_LABELS = {
    "heat_balance": "Wärmebilanz", "GWP": "Treibhausgasbilanz",
    "embodied_emissions": "Graue Emissionen", "electricity_dispatch": "Stromflüsse",
    "dhw": "Warmwasser", "primary_energy_balance": "Primärenergiebilanz",
    "heating": "Heizung", "energy_dispatch": "Energieverteilung",
    "final_energy_balance": "Endenergiebilanz", "cooling": "Kühlung",
    "pe_import_export_balance": "Primärenergie: Import und Export",
    "useful_energy": "Nutzenergie", "comfort": "Komfort",
    "electricity_end_use": "Stromanwendungen", "weather": "Wetter",
    "mobility": "Mobilität", "final_energy": "Endenergie",
    "GHG": "Treibhausgase", "PV": "Photovoltaik", "Ventilation": "Lüftung",
    "ventilation": "Lüftung", "assessment": "Bewertung", "battery": "Batterie",
    "construction": "Konstruktion", "declaration": "Deklaration", "district": "Quartier",
    "flexibility": "Flexibilität", "geometry": "Geometrie", "lca": "Lebenszyklus",
    "legacy": "Altbestand", "primary_energy": "Primärenergie", "project": "Projekt",
    "solar_gains": "Solare Gewinne", "thermal_hull": "Thermische Hülle",
    "tool": "Werkzeug", "usage": "Nutzung",
}


def output_variables():
    return catalog_variables("OUT")


def catalog_variables(source="OUT"):
    """Reuse VariableMeta records from the active registry; do not infer missing fields."""
    if source not in {"IN", "OUT"}:
        raise ValueError("Catalog source must be IN or OUT")
    return tuple(meta for attr in current.ATTR_NAME_MAP.values()
                 if (meta := getattr(current.SCHEMA_META, attr)).source == source)


def _text(value):
    return escape(str(value)) if value is not None and str(value).strip() else "Nicht hinterlegt"


def _domain_title(domain):
    return DOMAIN_LABELS.get(domain, domain) if domain else "Ohne Domänenzuordnung"


def render_catalog(source="OUT"):
    variables = catalog_variables(source)
    prefix = source.lower()
    noun = "Parameter" if source == "IN" else "Kennzahl"
    groups = defaultdict(list)
    for meta in variables:
        groups[meta.domain or ""].append(meta)
    domains = sorted(groups, key=lambda key: (not bool(key), _domain_title(key).casefold(), key))
    entities = sorted({m.entity_group for m in variables if m.entity_group})
    missing = {field: sum(not getattr(m, field) for m in variables)
               for field in ("domain", "unit", "label_de", "comment")}
    parts = [f'''<section id="{prefix}-catalog" class="schema-catalog" data-source="{source}" aria-label="{source}-Katalog">
<p><strong>{len(variables)} {source}-Variablen</strong> aus Schema <code>{escape(current.SCHEMA_VERSION)}</code>.
Vollständiger Definitionsbestand, keine Projektwerte. Auch Hilfsgrößen sind enthalten.</p>
<p class="catalog-note">Metadatenlücken: {missing['domain']} ohne Domäne,
{missing['unit']} ohne Einheit, {missing['label_de']} ohne deutsches Label und
{missing['comment']} ohne zusätzliche Beschreibung. „Nicht hinterlegt“ bedeutet nicht „dimensionslos“.</p>
<form class="catalog-controls" hidden>
<div class="catalog-search"><label for="{prefix}-query">{noun} suchen</label>
<input id="{prefix}-query" type="search" placeholder="z. B. PV, Batterie oder Variablenname" aria-describedby="{prefix}-search-help"></div>
<div><label for="{prefix}-domain">Domäne</label><select id="{prefix}-domain"><option value="*">Alle Domänen</option>''']
    for domain in domains:
        parts.append(f'<option value="{escape(domain, quote=True)}">{escape(_domain_title(domain))} ({len(groups[domain])})</option>')
    parts.append(f'</select></div><div><label for="{prefix}-entity">Entity Group</label><select id="{prefix}-entity"><option value="*">Alle Gruppen</option><option value="">Ohne Zuordnung</option>')
    parts.extend(f'<option value="{escape(e, quote=True)}">{escape(e)}</option>' for e in entities)
    parts.append(f'''</select></div>
<div class="catalog-actions">
<button type="button" data-query="{'pv' if source == 'IN' else 'cost_'}">{'Photovoltaik' if source == 'IN' else 'Kosten'}</button>
<button type="button" data-query="flex">Flexibilität</button>
<button type="button" data-query="speicher | batt | soc | zykl">Speicher / Batterie</button>
<button type="reset">Zurücksetzen</button>
</div>
<p id="{prefix}-search-help" class="catalog-search-help">Suche in Labels, Variablennamen, Einheiten und Zuordnungen. Mehrere Wörter grenzen gemeinsam ein;
<code>|</code> verbindet Alternativen. Die Schnelleinstiege sind Suchhilfen, keine zusätzlichen Schema-Domänen.</p>
<div class="catalog-actions"><button type="button" id="{prefix}-expand">Treffer aufklappen</button>
<button type="button" id="{prefix}-collapse">Alle zuklappen</button></div>
</form>
<p id="{prefix}-count" role="status" aria-live="polite">Alle Domänen unten aufklappbar.</p>
<p id="{prefix}-empty" hidden>Keine passenden {source}-Variablen. Suchbegriff oder Filter zurücksetzen.</p>''')
    for index, domain in enumerate(domains):
        parts.append(f'''<details class="out-domain" id="{prefix}-domain-{index}" data-domain="{escape(domain, quote=True)}">
<summary>{escape(_domain_title(domain))} <span class="out-domain-count">({len(groups[domain])})</span></summary>''')
        if domain:
            parts.append(f'<p>Schema-Domäne: <code>{escape(domain)}</code></p>')
        parts.append(f'''<div class="catalog-table" role="region" aria-label="{noun}: {_text(domain)}" tabindex="0">
<table><thead><tr><th scope="col">{noun} / Variablenname</th><th scope="col">Einheit</th>
<th scope="col">Zuordnung und Beschreibung</th></tr></thead><tbody>''')
        for meta in sorted(groups[domain], key=lambda m: ((m.label_de or m.var_name).casefold(), m.var_name)):
            details = ''.join(f'<dt>{label}</dt><dd>{_text(getattr(meta, field))}</dd>' for field, label in (
                ('measure', 'Größentyp (measure)'), ('entity_group', 'Entity Group'),
                ('entity_key', 'Entity Key'), ('spatial_scope', 'Räumlicher Bezug'),
                ('temporal_scope', 'Zeitlicher Bezug'), ('comment', 'Zusätzliche Beschreibung')))
            icon = f'<span class="catalog-icon" aria-hidden="true">{escape(meta.icon)}</span> ' if meta.icon else ''
            parts.append(f'''<tr id="{prefix}-{escape(meta.var_name, quote=True)}" data-entity="{escape(meta.entity_group or '', quote=True)}">
<th scope="row">{icon}<a href="#{prefix}-{escape(meta.var_name, quote=True)}">{_text(meta.label_de)}</a><br><code>{escape(meta.var_name)}</code></th>
<td>{_text(meta.unit)}</td><td><span class="catalog-measure">{_text(meta.measure)}</span>
<details class="out-meta"><summary>Metadaten anzeigen</summary><dl>{details}</dl></details></td></tr>''')
        parts.append('</tbody></table></div></details>')
    parts.append('<noscript><p>Ohne JavaScript sind alle Domänen manuell aufklappbar. Die Suche benötigt JavaScript.</p></noscript></section>')
    return '\n'.join(parts)


def build(output=None, source="OUT"):
    """Write one disposable HTML-in-QMD fragment for the existing website build."""
    html = render_catalog(source)
    path = Path(output) if output is not None else ROOT / f'website/assets/{source.lower()}-catalog.qmd'
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text('```{=html}\n' + html + '\n```\n', encoding='utf-8')
    return path


if __name__ == '__main__':
    for source in ("IN", "OUT"):
        print(build(source=source))
    print(build_presets())
