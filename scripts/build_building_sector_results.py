"""Read-only audit and consolidation of the existing annual building-sector run.

Project remains the data model. This script only orchestrates manifest checks,
existing Project IO and diagnostic tables; it never starts Excel or a simulation.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import time

import openpyxl
import pandas as pd

from pexl import Project
from pexl.io._project_tables import RESERVED_IN_COLUMN_HEADER_SET, RESERVED_OUT_COLUMN_HEADER_SET
from pexl.schema.current import ATTR_NAME_MAP, SCHEMA_META, SCHEMA_VERSION

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'data/exports/typologies/building_sector'
OUTPUT = SOURCE / 'building_sector_project.xlsx'


def digest(path):
    with Path(path).open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def inspect_sources(directory=SOURCE, *, expected=5400):
    """Check identities, hashes and raw tables before Project can normalize them.

Missing values and scientific anomalies are diagnostics, not rejection criteria.
Structural ambiguity, changed files and unknown variables stop the export.
"""
    directory = Path(directory)
    manifest = json.loads((directory / 'batch.json').read_text(encoding='utf-8'))
    definitions = pd.read_csv(directory / 'scenarios_5400_SCEN.csv', sep=';', keep_default_na=False)
    names = definitions['Scenario Name'].tolist()
    chunks = manifest['chunks']
    committed = [name for chunk in chunks for name in chunk['scenarios']]
    embedded = json.loads(manifest['identity']['definitions'])
    original = pd.DataFrame(embedded['data'], columns=embedded['columns'])
    if len(names) != expected or len(set(names)) != expected or Counter(names) != Counter(committed):
        raise ValueError('SCEN/checkpoint scenario identities are incomplete or duplicated')
    if Counter(original['Scenario Name']) != Counter(names):
        raise ValueError('Embedded checkpoint definitions differ from SCEN identities')
    # Control columns (e.g. Simulieren?) are intentionally not part of the batch identity.
    common = [c for c in original if c in definitions and c != 'Scenario Name']
    a = original.set_index('Scenario Name')[common].fillna('').astype(str).sort_index()
    b = definitions.set_index('Scenario Name')[common].fillna('').astype(str).sort_index()
    if not a.equals(b):
        raise ValueError('SCEN parameters differ from the checkpoint definition snapshot')
    paths = sorted(directory.glob('annual-*.xlsx'))
    if {p.name for p in paths} != {c['annual'] for c in chunks}:
        raise ValueError('Annual files differ from checkpoint file inventory')
    by_file = {c['annual']: c for c in chunks}
    missing, excel_errors, sentinel_values = Counter(), Counter(), Counter()
    variable_sets = {}
    hashes = {}
    for path in paths:
        chunk = by_file[path.name]
        hashes[path.name] = digest(path)
        if hashes[path.name] != chunk['files'][path.name]:
            raise ValueError(f'Checkpoint hash mismatch: {path.name}')
        with_workbook = openpyxl.load_workbook(path, read_only=True, data_only=True)
        try:
            for sheet, reserved in [('IN', RESERVED_IN_COLUMN_HEADER_SET), ('OUT', RESERVED_OUT_COLUMN_HEADER_SET)]:
                rows = with_workbook[sheet].iter_rows()
                header = [c.value for c in next(rows)]
                indices = [i for i, h in enumerate(header) if h not in reserved]
                actual = [header[i] for i in indices]
                if actual != chunk['scenarios'] or len(set(header)) != len(header):
                    raise ValueError(f'{path.name}/{sheet}: duplicated or mismatched scenario columns')
                key_index = header.index('var_name')
                variables = []
                for row in rows:
                    key = row[key_index].value
                    if not key or key not in ATTR_NAME_MAP:
                        raise ValueError(f'{path.name}/{sheet}: unknown/empty variable {key!r}')
                    variables.append(key)
                    if getattr(SCHEMA_META, ATTR_NAME_MAP[key]).source not in (sheet, 'BOTH'):
                        raise ValueError(f'{path.name}: variable {key} in wrong sheet')
                    for i in indices:
                        cell = row[i]
                        if cell.value is None:
                            missing[key] += 1
                        elif cell.data_type == 'e':
                            excel_errors[key] += 1
                        elif isinstance(cell.value, (int, float)):
                            if not math.isfinite(cell.value):
                                raise ValueError(f'{path.name}/{key}: nonfinite value')
                            if -2146826300 <= cell.value <= -2146826200:
                                sentinel_values[key] += 1
                if len(set(variables)) != len(variables):
                    raise ValueError(f'{path.name}/{sheet}: duplicate variable rows')
                if sheet in variable_sets and variables != variable_sets[sheet]:
                    raise ValueError(f'{path.name}/{sheet}: inconsistent variable rows')
                variable_sets[sheet] = variables
        finally:
            with_workbook.close()
    if excel_errors:
        raise ValueError(f'Excel error cells cannot be losslessly imported: {dict(excel_errors)}')
    audit = dict(scenarios=len(names), files=len(paths), schema=SCHEMA_VERSION,
                 source_schema=manifest['identity']['schema'], base_reload=manifest['identity']['base_reload'],
                 hashes=hashes, checkpoint_sha256=digest(directory / 'batch.json'),
                 scen_sha256=digest(directory / 'scenarios_5400_SCEN.csv'),
                 variables={k: len(v) for k, v in variable_sets.items()},
                 missing_values=dict(missing), excel_error_sentinels=dict(sentinel_values),
                 failed_checkpoint_entries=manifest.get('failed', {}))
    if manifest.get('failed'):
        raise ValueError('Checkpoint contains failed scenarios')
    return paths, audit


def diagnostics(project):
    """One diagnostic pass; anomalies are not simulation-error classifications."""
    keys = [k for k, attr in ATTR_NAME_MAP.items()
            if getattr(SCHEMA_META, attr).measure == 'test' or 'residual' in k.lower()]
    rows = []
    for key in keys:
        values = pd.to_numeric(pd.Series([getattr(s.v, ATTR_NAME_MAP[key]) for s in project]), errors='coerce')
        rows.append(dict(variable=key, missing=int(values.isna().sum()),
                         nonzero=int((values.abs() > 1e-6).sum()), max_abs=values.abs().max()))
    return pd.DataFrame(rows)


def check_roundtrip(project, restored):
    if project.column_names() != restored.column_names():
        raise ValueError('Roundtrip changed scenario identities/order')
    checked = 0
    for left, right in zip(project, restored):
        for attr in ATTR_NAME_MAP.values():
            x, y = getattr(left.v, attr), getattr(right.v, attr)
            if pd.isna(x) and pd.isna(y):
                continue
            if isinstance(x, (int, float)) and isinstance(y, (int, float)):
                equal = math.isclose(x, y, rel_tol=1e-12, abs_tol=1e-10)
            else:
                equal = x == y
            if not equal:
                raise ValueError(f'Roundtrip changed {left.column_name}/{attr}: {x!r} -> {y!r}')
            checked += 1
    return checked


def build(directory=SOURCE, output=OUTPUT, *, expected=5400, audit_output=None):
    started = time.perf_counter()
    paths, audit = inspect_sources(directory, expected=expected)
    print(f'Validated {len(paths)} source files', flush=True)
    project = Project.from_files(paths, unknown='raise')
    audit['import_seconds'] = time.perf_counter() - started
    if len(project) != expected:
        raise ValueError('Imported scenario count differs from expectation')
    output = Path(output)
    if output.resolve() in [p.resolve() for p in paths]:
        raise ValueError('Output must not overwrite an original annual export')
    output.parent.mkdir(parents=True, exist_ok=True)
    temporary = output.with_name(output.stem + '.pending.xlsx')
    project.to_excel(temporary, include_out=True)
    print('Export written; checking roundtrip', flush=True)
    restored = Project.from_excel(temporary, unknown='raise')
    audit['roundtrip_checked_values'] = check_roundtrip(project, restored)
    del restored
    temporary.replace(output)
    audit['output_sha256'] = digest(output)
    audit['seconds'] = time.perf_counter() - started
    audit['diagnostics'] = json.loads(diagnostics(project).to_json(orient='records'))
    if audit_output is not None:
        audit_output = Path(audit_output)
        audit_output.parent.mkdir(parents=True, exist_ok=True)
        audit_output.write_text(json.dumps(audit, ensure_ascii=False, indent=2), encoding='utf-8')
    return project, audit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=OUTPUT)
    parser.add_argument('--audit-output', type=Path, default=ROOT / 'notebooks/local_exports/building_sector/validation.json')
    args = parser.parse_args()
    _, audit = build(output=args.output, audit_output=args.audit_output)
    print(json.dumps({k: audit[k] for k in ('scenarios', 'files', 'roundtrip_checked_values', 'seconds')}))
