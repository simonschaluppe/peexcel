"""Render the active IN, OUT and preset catalogs as searchable Quarto fragments."""
from collections import defaultdict
from html import escape
from pathlib import Path
import hashlib
import re

from pexl.i18n import domain_text
from pexl.schema import current
from pexl.schema._presets import load_preset_catalogs

ROOT = Path(__file__).resolve().parents[1]
SCHEMA_EXPORTS = ROOT / 'data/exports/schemas'


def preset_anchor(table, name=None):
    """Snapshot-local links; names are not promised stable across Excel versions."""
    suffix = '' if name is None else '-' + hashlib.sha256(name.encode()).hexdigest()[:12]
    return 'preset-' + table + suffix


def _render_presets(data, notes):
    source = data['source'].relative_to(ROOT).as_posix()
    tables = {table['name']: table for table in data['tables']}
    table_names = [name for name in notes if name in tables]
    table_names.extend(name for name in tables if name not in notes)
    esc = lambda value: escape(str(value))
    count = sum(len(t['presets']) for t in tables.values())
    parts = [f'<section class="schema-catalog" data-source="PRESET" data-item-label="Preset-Spalten">',
             f'<p><strong>Stand: {esc(data["tool_version"])} · {len(tables)} Tabellen · {count} Preset-Spalten</strong><br>Excel-Export: {esc(data["exported_at"])}.</p>',
             '<form class="catalog-controls" hidden><label>Presets und Werte suchen<input id="preset-query" type="search" placeholder="z. B. Wärmepumpe oder Nutzerstrom"></label><label>Eingabegruppe<select id="preset-domain"><option value="*">Alle Gruppen</option>']
    for name in table_names:
        title = notes.get(name, {}).get('title', name)
        parts.append(f'<option value="{esc(name)}">{esc(title)}</option>')
    parts += ['</select></label><select id="preset-entity" hidden aria-label="Zuordnung"><option value="*">Alle</option></select><div class="catalog-actions"><button type="reset">Zurücksetzen</button><button type="button" id="preset-expand">Alle aufklappen</button><button type="button" id="preset-collapse">Alle zuklappen</button></div></form><p id="preset-count" aria-live="polite"></p><p id="preset-empty" hidden>Keine passenden Presets gefunden.</p>']
    for name in table_names:
        note = notes.get(name, {})
        title = note.get('title', name)
        table = tables[name]
        note_html = re.sub(r'\[([^\]]+)\]\{\.excel-value\}', r'<span class="excel-value">\1</span>', esc(note.get('text', '')))
        introduction = f'<p>{note_html}</p>' if note_html else ''
        parts.append(f'<details class="out-domain" data-domain="{esc(name)}" id="{preset_anchor(name)}"><summary>{esc(title)} <span class="out-domain-count"></span></summary>{introduction}<p>Excel-Tabelle: <code>{esc(name)}</code></p><div class="catalog-table"><table><thead><tr><th>Preset / Auswahlname</th><th>Belegung und Herkunft</th></tr></thead><tbody>')
        for preset in table['presets']:
            name_p = preset['name']
            title = preset['display_name'] if preset['display_name'] is not None else name_p
            details = []
            for key, value in preset['values'].items():
                m = table['variables'][key]
                shown = 'Nicht gesetzt – vorhandenen Wert beibehalten' if value is None else ('Ja' if value is True else 'Nein' if value is False else str(value))
                unit = m['unit'] or preset['unit'] or 'Einheit nicht hinterlegt'
                label = f'<span data-in-var="{esc(key)}">{esc(m["label"])}</span>' if m['in_schema'] else esc(m['label'])
                details.append(f'<dt>{label} <code>{esc(key)}</code></dt><dd>{esc(shown)} <span class="text-muted">[{esc(unit)}] · {esc(preset["cells"][key])}</span></dd>')
            parts.append(f'<tr id="{preset_anchor(name, name_p)}" data-entity=""><th scope="row"><a href="#{preset_anchor(name, name_p)}">{esc(title)}</a><br><small>Spaltenname: {esc(name_p)}</small></th><td><p>{esc(preset["description"] or "")}</p>{"<p>Einheit laut Presettabelle: " + esc(preset["unit"]) + "</p>" if preset["unit"] else ""}<details class="out-meta"><summary>{sum(v is not None for v in preset["values"].values())} gesetzte Werte · vollständige Belegung ansehen</summary><dl>{"".join(details)}</dl></details></td></tr>')
        parts.append('</tbody></table></div></details>')
    parts.append(f'<p>Quelle: <code>{esc(source)}</code><br>Inhaltskennung: <code>{data["content_sha256"][:16]}</code></p><noscript>Ohne JavaScript lassen sich alle Gruppen und Werte manuell aufklappen.</noscript></section>')
    return '\n'.join(parts)


def build_presets(output=None):
    """Write the current catalog, historical fragments and current editorial help."""
    import yaml

    catalogs = load_preset_catalogs(SCHEMA_EXPORTS)
    active, *historical = catalogs
    notes = yaml.safe_load((ROOT / 'website/_preset-notes.yml').read_text(encoding='utf-8'))
    out = Path(output) if output else ROOT / 'website/assets'
    versions = out / 'preset-versions'
    versions.mkdir(parents=True, exist_ok=True)
    history_titles = {name: {'title': note['title']} for name, note in notes.items()}
    generated = set()
    for data in historical:
        fragment = versions / f"{data['version_key']}.html"
        fragment.write_text(_render_presets(data, history_titles), encoding='utf-8')
        generated.add(fragment)
    for stale in set(versions.glob('*.html')) - generated:
        stale.unlink()

    options = ''.join(f'<option value="{escape(data["version_key"])}">{escape(data["tool_version"])}</option>'
                      for data in catalogs)
    chooser = (
        f'<div hidden data-preset-versions data-current="{escape(active["version_key"])}">'
        f'<label for="preset-version">Version</label> '
        f'<select id="preset-version" class="form-select w-auto d-inline-block">{options}</select>'
        '<p data-preset-version-status role="status" hidden></p></div>'
    )
    catalog = _render_presets(active, notes)
    target = out / 'preset-catalog.qmd'
    target.write_text(f'```{{=html}}\n{chooser}\n<div id="preset-catalog-content">{catalog}</div>\n```\n', encoding='utf-8')

    active_names = {table['name'] for table in active['tables']}
    help_by_page = {}
    for name, note in notes.items():
        for page in note.get('pages', []):
            lines = help_by_page.setdefault(page, [])
            if name in active_names:
                lines.append(f'- **[{note["title"]}](preset-catalog.qmd#{preset_anchor(name)}):** {note["text"]}')
    for page, lines in help_by_page.items():
        if not lines:
            lines = ['[Standardfälle im aktuellen Preset-Katalog](preset-catalog.qmd)']
        (out / f'preset-help-{page}.qmd').write_text(
            '::: {.callout-note collapse=true title="Noch keine eigenen Werte? Standardfälle nutzen"}\n\n'
            + '\n'.join(lines)
            + '\n\nPrüfe die übernommenen Werte für dein Projekt. [So wendest du Presets an](presets.qmd).\n\n:::\n',
            encoding='utf-8',
        )
    return target


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


def render_catalog(source="OUT"):
    variables = catalog_variables(source)
    prefix = source.lower()
    noun = "Parameter" if source == "IN" else "Kennzahl"
    groups = defaultdict(list)
    for meta in variables:
        groups[meta.domain or ""].append(meta)
    domains = sorted(groups, key=lambda key: (not bool(key), domain_text(key).casefold(), key))
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
        parts.append(f'<option value="{escape(domain, quote=True)}">{escape(domain_text(domain))} ({len(groups[domain])})</option>')
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
<summary>{escape(domain_text(domain))} <span class="out-domain-count">({len(groups[domain])})</span></summary>''')
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


def build_catalogs(output=None):
    """Generate the catalog fragments for the website."""
    directory = Path(output) if output is not None else ROOT / 'website/assets'
    presets = build_presets(directory)
    return build(directory / 'in-catalog.qmd', 'IN'), build(directory / 'out-catalog.qmd', 'OUT'), presets


if __name__ == '__main__':
    for fragment in build_catalogs():
        print(fragment)
