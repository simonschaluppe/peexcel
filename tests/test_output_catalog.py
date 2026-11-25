from dataclasses import replace
from html.parser import HTMLParser
from pathlib import Path
import sys

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import output_catalog
from pexl.i18n import domain_text
from pexl.schema import current
from pexl.schema._presets import load_preset_catalogs


class CatalogParser(HTMLParser):
    def __init__(self, source="OUT"):
        self.prefix = source.lower() + "-"
        super().__init__()
        self.ids = []
        self.domains = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'tr' and attrs.get('id', '').startswith(self.prefix):
            self.ids.append(attrs['id'][len(self.prefix):])
        if tag == 'details' and attrs.get('class') == 'out-domain':
            self.domains.append(attrs['data-domain'])


@pytest.mark.parametrize("source", ["IN", "OUT"])
def test_catalog_covers_exactly_the_active_registry_once(source):
    metadata = [getattr(current.SCHEMA_META, a) for a in current.ATTR_NAME_MAP.values()]
    expected = {m.var_name for m in metadata if m.source == source}
    html = output_catalog.render_catalog(source)
    parser = CatalogParser(source)
    parser.feed(html)
    assert set(parser.ids) == expected
    assert len(parser.ids) == len(expected)
    assert set(parser.domains) == {m.domain or '' for m in metadata if m.source == source}
    assert current.SCHEMA_VERSION in html
    assert 'Ohne Domänenzuordnung' in html
    assert 'Nicht hinterlegt' in html
    assert html.count('class="catalog-icon"') == sum(bool(m.icon) for m in metadata if m.source == source)
    if source == 'OUT':
        for name in ('cost_total', 'cost_E_grid', 'PEI_sub_flex', 'Batt_FEC', 'Batt_RTE'):
            assert name in parser.ids


def test_missing_fields_remain_missing_and_metadata_is_html_escaped(monkeypatch):
    sample = replace(output_catalog.output_variables()[0], label_de='<script>test</script>',
                     unit=None, comment='A & B', domain=None, entity_group=None, icon='<img src=x>')
    monkeypatch.setattr(output_catalog, 'catalog_variables', lambda source: (sample,))
    html = output_catalog.render_catalog()
    assert '<script>test</script>' not in html
    assert '&lt;script&gt;test&lt;/script&gt;' in html
    assert 'A &amp; B' in html
    assert '&lt;img src=x&gt;' in html
    assert '<img src=x>' not in html
    assert '<td>Nicht hinterlegt</td>' in html
    assert '1 ohne Einheit' in html


def test_build_is_deterministic_and_writes_only_one_fragment(tmp_path):
    target = tmp_path / 'assets/out-catalog.qmd'
    assert output_catalog.build(target) == target
    first = target.read_bytes()
    output_catalog.build(target)
    assert target.read_bytes() == first
    assert target.read_text(encoding='utf-8').startswith('```{=html}\n')
    assert list(tmp_path.rglob('*.*')) == [target]


def test_navigation_separates_excel_python_and_project():
    config = yaml.safe_load((ROOT / 'website/_quarto.yml').read_text(encoding='utf-8'))
    navbar = config['website']['navbar']['left']
    assert {'href': 'python.qmd', 'text': 'Python'} in navbar
    assert all(link['href'] != 'research.qmd' for link in navbar)
    sections = config['website']['sidebar']['contents']
    start = next(s for s in sections if s.get('section') == 'Starten')
    assert all(x.get('href') != 'glossary.qmd' for x in start['contents'])
    assert {'href': 'glossary.qmd', 'text': 'Nachschlagen'} in navbar
    glossary = next(i for i, s in enumerate(sections) if s.get('section') == 'Nachschlagen')
    assert {s['href'] for s in sections[glossary]['contents']} == {'glossary.qmd', 'preset-catalog.qmd'}
    assert sections[glossary - 1]['section'] == 'Deklarieren'
    assert sections[glossary + 1]['section'] == 'Python & Automatisierung'
    assert any(s.get('section') == 'Python & Automatisierung' for s in sections)
    about = next(s for s in sections if s.get('section') == 'Über das Projekt')
    assert 'research.qmd' in about['contents']
    assert '!assets/**' in config['project']['render']
    assert 'output-catalog.js' in config['project']['resources']
    assert config['project']['pre-render'] == ['python ../scripts/output_catalog.py']


def test_preset_catalog_defaults_to_current_and_renders_historical_exports(tmp_path):
    catalogs = load_preset_catalogs(output_catalog.SCHEMA_EXPORTS)
    active, *historical = catalogs
    assert active['version_key'] == current.SCHEMA_VERSION
    assert {data['tool_version'] for data in catalogs} >= {'1.13.1_dev', 'v1.12.7', 'v1.11.6'}
    assert all(not field['in_schema'] for data in historical for table in data['tables']
               for field in table['variables'].values())
    catalog = output_catalog.build_presets(tmp_path).read_text(encoding='utf-8')
    assert f'data-current="{current.SCHEMA_VERSION}"' in catalog
    assert f'Stand: {active["tool_version"]}' in catalog
    for data in historical:
        key = data['version_key']
        assert f'value="{key}"' in catalog
        fragment = (tmp_path / 'preset-versions' / f'{key}.html').read_text(encoding='utf-8')
        assert f'Stand: {data["tool_version"]}' in fragment
        assert data['source'].name in fragment


def test_active_preset_export_must_exist_and_match_its_metadata(tmp_path):
    from openpyxl import Workbook

    version = current.SCHEMA_VERSION
    with pytest.raises(ValueError, match=f'Expected one Excel schema export for {version}'):
        load_preset_catalogs(tmp_path)
    workbook = Workbook()
    workbook.active.title = 'META'
    workbook['META'].append(['key', 'value'])
    workbook['META'].append(['tool_version', '0.0.0'])
    presets = workbook.create_sheet('example')
    presets.append(['var_name', 'PRESETS>', 'Default'])
    presets.append(['Example', None, 0])
    workbook.save(tmp_path / f'schema_{version}.xlsx')
    with pytest.raises(ValueError, match=f'expected META.tool_version matching {version}'):
        load_preset_catalogs(tmp_path)


def test_domain_text_is_shared_and_preserves_untranslated_keys():
    assert domain_text('heat_balance') == 'Wärmebilanz'
    assert domain_text('heat_balance', 'en') == 'Heat balance'
    assert domain_text('new_domain') == 'new_domain'


def test_both_catalogs_have_unique_ids_and_keep_existing_out_anchors():
    class IdParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.ids = []
        def handle_starttag(self, tag, attrs):
            value = dict(attrs).get('id')
            if value:
                self.ids.append(value)
    parser = IdParser()
    parser.feed(output_catalog.render_catalog('IN') + output_catalog.render_catalog('OUT'))
    assert len(parser.ids) == len(set(parser.ids))
    assert 'in-query' in parser.ids and 'out-query' in parser.ids
    assert 'out-Batt_FEC' in parser.ids
    with pytest.raises(ValueError):
        output_catalog.render_catalog('SIM')
