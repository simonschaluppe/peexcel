"""Execute an editable audit notebook once and render HTML/DOCX with Quarto.

Notebook Markdown is the report source. Cells tagged audit-help or audit-control
are omitted. Only trusted notebooks should be rendered: their Python executes.
No project texts, source notebooks or Excel files are modified.
"""
from __future__ import annotations

import base64
from copy import deepcopy
from importlib.resources import files
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import uuid


def display_table(frame):
    """Show a native Markdown table (also editable as a Word table on export)."""
    import math
    import numbers
    import pandas as pd
    from IPython.display import Markdown, display

    def value(v):
        if pd.isna(v) or (isinstance(v, numbers.Real) and not math.isfinite(v)):
            return 'nicht verfügbar'
        if isinstance(v, numbers.Real) and not isinstance(v, bool):
            return f'{v:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
        # Prevent source strings from changing Markdown table structure/markup.
        import html
        return html.escape(str(v)).replace('|', '&#124;').replace('\n', ' ').replace('*', '&#42;').replace('_', '&#95;')

    frame = frame.drop(columns=['var_name'], errors='ignore')
    rows = [[value(v) for v in frame.columns]] + [[value(v) for v in row] for row in frame.itertuples(index=False, name=None)]
    lines = ['| ' + ' | '.join(rows[0]) + ' |', '| ' + ' | '.join(['---'] * len(frame.columns)) + ' |']
    lines += ['| ' + ' | '.join(row) + ' |' for row in rows[1:]]
    display(Markdown('\n'.join(lines)))


def display_chart(figure):
    """Keep a standard Plotly MIME output for notebooks and both exporters."""
    from IPython.display import display
    display({'application/vnd.plotly.v1+json': json.loads(figure.to_json()),
             'text/plain': figure.layout.title.text or 'Diagramm'}, raw=True)


def _execute_worker(input_path, output_path):
    """Private subprocess worker for ordinary Python/IPython report cells.

    Rich display outputs are captured without opening Jupyter network sockets.
    Interactive widgets and asynchronous/background execution are not supported.
    """
    import nbformat
    from IPython.core.interactiveshell import InteractiveShell
    from IPython.utils.capture import capture_output
    shell = InteractiveShell.instance()
    notebook = nbformat.read(input_path, as_version=4)
    count = 0
    for cell in notebook.cells:
        if cell.cell_type != 'code':
            continue
        count += 1
        with capture_output() as captured:
            result = shell.run_cell(cell.source, store_history=False)
        if result.error_before_exec or result.error_in_exec:
            raise RuntimeError(f'Notebook cell {count} failed: {result.error_before_exec or result.error_in_exec}\n{captured.stdout}\n{captured.stderr}')
        cell.execution_count = count
        cell.outputs = [nbformat.v4.new_output('display_data', data=o.data, metadata=o.metadata) for o in captured.outputs]
        for name, text in [('stdout', captured.stdout), ('stderr', captured.stderr)]:
            if text:
                cell.outputs.append(nbformat.v4.new_output('stream', name=name, text=text))
    nbformat.write(notebook, output_path)


def _execute(notebook, directory, timeout):
    import nbformat
    # Fresh process, same interpreter and project cwd; no kernel installation.
    with tempfile.TemporaryDirectory(prefix='pexl-execute-') as tmp:
        source, target = Path(tmp) / 'input.ipynb', Path(tmp) / 'output.ipynb'
        nbformat.write(notebook, source)
        completed = subprocess.run([sys.executable, '-c',
            'import sys; from pexl.reporting.document import _execute_worker; _execute_worker(*sys.argv[1:])',
            str(source), str(target)], cwd=directory, capture_output=True, text=True,
            encoding='utf-8', errors='replace', timeout=timeout)
        if completed.returncode:
            raise RuntimeError(f'Notebook execution failed:\n{completed.stdout}\n{completed.stderr}')
        executed = nbformat.read(target, as_version=4)
        notebook.cells = executed.cells
    return notebook


def render_notebook(notebook, *, output_dir=None, formats=('html', 'docx'), execute=True,
                    timeout=300, reference_docx=None):
    """Render saved notebook to report/<stem>.html/.docx; return format→Path.

    Installs nothing. Requires Quarto and pexl's publication extra (Kaleido with
    Chrome for DOCX). Control cells are never executed recursively. Export runs
    in a temporary directory, and publishes only after all formats succeed.
    ``execute=False`` is for an already executed notebook, not a data refresh.
    """
    import nbformat
    import plotly.graph_objects as go

    source = Path(notebook).resolve(strict=True)
    formats = tuple(formats)
    if not formats or len(set(formats)) != len(formats) or set(formats) - {'html', 'docx'}:
        raise ValueError('formats must contain html and/or docx, without duplicates')
    quarto = shutil.which('quarto')
    if quarto is None:
        raise RuntimeError('Quarto fehlt. Quarto installieren und erneut rendern.')
    destination = Path(output_dir).resolve() if output_dir else source.parent / 'report'
    nb = nbformat.read(source, as_version=4)
    nb.cells = [c for c in nb.cells if not set(c.metadata.get('tags', [])) & {'audit-help', 'audit-control'}]
    if execute:
        for cell in nb.cells:
            if cell.cell_type == 'code':
                cell.outputs = []
                cell.execution_count = None
        _execute(nb, source.parent, timeout)
    if any(o.output_type == 'error' for c in nb.cells if c.cell_type == 'code' for o in c.outputs):
        raise ValueError('Notebook contains failed cells; report was not exported')
    result = {}
    with tempfile.TemporaryDirectory(prefix='.pexl-audit-', dir=source.parent) as tmp:
        tmp = Path(tmp)
        # Isolate from any enclosing website's _quarto.yml/output directory.
        (tmp / '_quarto.yml').write_text('project:\n  type: default\n  output-dir: .\nlang: de\nexecute:\n  enabled: false\n', encoding='utf-8')
        # Keep Markdown image paths relative to the original project directory.
        for fmt in formats:
            prepared = deepcopy(nb)
            html_plots = {}
            first_plot = True
            plot_number = 0
            for cell in prepared.cells:
                if cell.cell_type != 'code':
                    continue
                cell.source = '#| echo: false\n' + cell.source
                cleaned = []
                for output in cell.outputs:
                    if output.output_type == 'stream':
                        continue
                    data = output.get('data', {})
                    if 'application/vnd.plotly.v1+json' in data:
                        fig = go.Figure(data['application/vnd.plotly.v1+json'])
                        plot_number += 1
                        if fmt == 'html':
                            # Inject after Quarto's resource bundling: Plotly's JS
                            # contains URL strings which are not page resources.
                            marker = f'PEXL-PLOT-{uuid.uuid4().hex}'
                            placeholder = f'<p>{marker}</p>'
                            html_plots[placeholder] = fig.to_html(full_html=False, include_plotlyjs=first_plot,
                                        config={'responsive': True}, default_width='100%')
                            data = {'text/markdown': marker}
                            first_plot = False
                        else:
                            image = tmp / f'figure-{plot_number}.png'
                            figure_path = tmp / f'figure-{plot_number}.json'
                            figure_path.write_text(fig.to_json(), encoding='utf-8')
                            # A broken Kaleido/browser startup must not block the
                            # notebook forever. Keep existing export logic in a
                            # disposable process with a bounded lifetime.
                            try:
                                image_run = subprocess.run([sys.executable, '-c',
                                    'import sys; import plotly.io as pio; from pexl.plot.export import export_figure; '
                                    'f=pio.read_json(sys.argv[1]); export_figure(f,sys.argv[2],provenance=f.layout.meta or {})',
                                    str(figure_path), str(image)], capture_output=True, text=True,
                                    encoding='utf-8', errors='replace', timeout=min(timeout, 60))
                            except subprocess.TimeoutExpired as exc:
                                raise RuntimeError(f'Statischer Diagrammexport überschritt {min(timeout, 60)} Sekunden. Kaleido/Chrome prüfen; HTML kann separat mit formats=("html",) erzeugt werden.') from exc
                            if image_run.returncode or not image.is_file():
                                raise RuntimeError(f'Statischer Diagrammexport fehlgeschlagen:\n{image_run.stderr}')
                            data = {'image/png': base64.b64encode(image.read_bytes()).decode('ascii')}
                        output['data'] = data
                    cleaned.append(output)
                cell.outputs = cleaned
            staged = tmp / f'{source.stem}.ipynb'
            nbformat.write(prepared, staged)
            args = [quarto, 'render', staged.name, '--to', fmt, '--no-execute',
                    '--output', f'{source.stem}.{fmt}', '-M', 'lang:de', '-M', 'echo:false',
                    '-M', 'toc:true', '-M', 'number-sections:false',
                    '-M', f'resource-path:["{source.parent.as_posix()}"]']
            if fmt == 'html':
                args += ['--embed-resources', '-M', 'theme:cosmo']
            else:
                reference = Path(reference_docx) if reference_docx else Path(str(files('pexl.reporting').joinpath('assets/audit-reference.docx')))
                if not reference.is_file():
                    raise FileNotFoundError(f'Word reference not found: {reference}')
                args += ['-M', f'reference-doc:{reference.resolve().as_posix()}']
            completed = subprocess.run(args, cwd=tmp, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
            if completed.returncode:
                raise RuntimeError(f'Quarto {fmt} failed:\n{completed.stdout}\n{completed.stderr}')
            rendered = tmp / f'{source.stem}.{fmt}'
            if not rendered.is_file():
                raise RuntimeError(f'Quarto did not create {rendered.name}')
            if fmt == 'html':
                text = rendered.read_text(encoding='utf-8')
                for placeholder, plot_html in html_plots.items():
                    if text.count(placeholder) != 1:
                        raise RuntimeError('Quarto did not preserve the Plotly placeholder')
                    text = text.replace(placeholder, plot_html)
                rendered.write_text(text, encoding='utf-8')
            result[fmt] = destination / rendered.name
        destination.mkdir(parents=True, exist_ok=True)
        for fmt, path in result.items():
            shutil.copy2(tmp / path.name, path)
    return result
