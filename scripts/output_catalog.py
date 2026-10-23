"""Render active IN/OUT metadata as searchable Quarto fragments, without project values."""
from collections import defaultdict
from html import escape
from pathlib import Path

from pexl.schema import current

ROOT = Path(__file__).resolve().parents[1]
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
