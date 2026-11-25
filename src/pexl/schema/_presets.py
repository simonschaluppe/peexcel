"""Read versioned preset tables from the repository's Excel schema exports."""
import hashlib
import json
from pathlib import Path
import re

from . import _normalize_version_name, current


def _version_order(version):
    match = re.fullmatch(r"v?(\d+(?:_\d+)*)(.*)", version)
    if match is None:
        return (), False, version
    number, suffix = match.groups()
    return tuple(map(int, number.split("_"))), not suffix, version


def load_preset_catalogs(export_dir):
    """Return the active catalog first, followed by available historical catalogs."""
    export_dir = Path(export_dir)
    version = current.SCHEMA_VERSION
    workbooks = [
        (_normalize_version_name(path.stem.removeprefix("schema_")), path)
        for path in sorted(export_dir.glob("schema_*.xlsx"))
    ]
    active = [path for key, path in workbooks if key == version]
    if len(active) != 1:
        found = ", ".join(path.name for path in active) or "none"
        raise ValueError(f"Expected one Excel schema export for {version} in {export_dir}. Found {found}.")

    catalog = _read_catalog(active[0], version, is_current=True)
    historical = {}
    for key, path in workbooks:
        if key == version:
            continue
        data = _read_catalog(path, key, is_current=False)
        if data is None:
            continue
        if key in historical:
            raise ValueError(f"Multiple preset exports for {key}: {historical[key]['source'].name}, {path.name}")
        historical[key] = data
    return [catalog, *(historical[key] for key in sorted(historical, key=_version_order, reverse=True))]


def _input_metadata(workbook, is_current):
    if is_current:
        variables = (getattr(current.SCHEMA_META, attr) for attr in current.ATTR_NAME_MAP.values())
        return {meta.var_name: dict(label_de=meta.label_de, unit=meta.unit, source=meta.source)
                for meta in variables}
    rows = iter(workbook['IN'].values)
    fields = next(rows)
    var_column = fields.index('var_name')
    return {row[var_column]: dict(zip(fields, row)) for row in rows if row[var_column]}


def _read_catalog(path, version, *, is_current):
    from openpyxl import load_workbook
    from openpyxl.utils import get_column_letter

    wb = load_workbook(path, read_only=True, data_only=False)
    try:
        variables = _input_metadata(wb, is_current) if 'IN' in wb else {}
        tables = []
        for sheet in wb:
            rows = iter(sheet.rows)
            header = [cell.value for cell in next(rows, ())]
            if 'PRESETS>' not in header or 'var_name' not in header:
                continue
            label_column = header.index('label_de') if 'label_de' in header else 0
            unit_column = header.index('unit') if 'unit' in header else None
            vi, start = header.index('var_name'), header.index('PRESETS>') + 1
            records, row_numbers = {}, {}
            for row_number, row in enumerate(rows, 2):
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
                    locations[key] = f'{get_column_letter(col + 1)}{row_numbers[key]}'
                get = lambda key: records[key][col].value if key in records else None
                presets.append(dict(name=str(header[col]), display_name=get('dropdown_name'),
                                    description=get('description'), unit=get('unit'), values=values, cells=locations))
            labels = {}
            for key, row in records.items():
                if key in ('dropdown_name', 'description', 'unit'):
                    continue
                source = variables.get(key, {})
                fallback = row[label_column].value
                unit = row[unit_column].value if unit_column is not None else None
                labels[key] = dict(label=source.get('label_de') or fallback or key,
                                   unit=source.get('unit') or unit,
                                   in_schema=is_current and source.get('source') == 'IN')
            tables.append(dict(name=sheet.title, variables=labels, presets=presets))
        if not tables:
            if is_current:
                raise ValueError(f"{path.name}: no preset tables found for {version}")
            return None

        meta = dict(list(wb['META'].values)[1:]) if 'META' in wb else {}
        tool_version = meta.get('tool_version')
        metadata_version = _normalize_version_name(tool_version) if tool_version else None
        if metadata_version != version:
            # Older exports record the release series in META and the patch in the filename.
            legacy_series, _, patch = version.rpartition("_")
            if not (version.startswith("v") and patch.isdigit() and metadata_version == legacy_series):
                raise ValueError(f"{path.name}: expected META.tool_version matching {version}, got {tool_version!r}")
            tool_version = path.stem.removeprefix("schema_").replace("_", ".")
        content = json.dumps(tables, ensure_ascii=False, sort_keys=True)
        return dict(version_key=version, tool_version=tool_version, source=path,
                    exported_at=str(meta.get('created_at', '')), tables=tables,
                    content_sha256=hashlib.sha256(content.encode()).hexdigest())
    finally:
        wb.close()
