from __future__ import annotations

import json
from pathlib import Path
import tkinter as tk
from tkinter import filedialog

import streamlit as st

from pexl import Project
from pexl import reporting
from pexl.plot import plotly


APP_TITLE = "klimaaktiv Quick-Check"
CONFIG_FILE = Path(".streamlit/path_config.json")


def load_saved_path() -> str:
    """Return the last selected project path, if available."""
    if not CONFIG_FILE.exists():
        return ""

    try:
        return json.loads(CONFIG_FILE.read_text(encoding="utf-8")).get("last_path", "")
    except (json.JSONDecodeError, OSError):
        return ""


def save_path(path: str) -> None:
    """Persist the selected project path for the next app start."""
    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
    CONFIG_FILE.write_text(json.dumps({"last_path": path}), encoding="utf-8")


def select_file() -> str:
    """Open a native file dialog and return the selected PEExcel workbook."""
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()

    try:
        return filedialog.askopenfilename(
            title="PEExcel-Projektexport auswählen",
            filetypes=[("Excel-Dateien", "*.xlsx *.xlsm *.xlsb")],
        )
    finally:
        root.destroy()


@st.cache_resource(show_spinner=False)
def load_project(path: str) -> Project:
    """Load a PEExcel workbook into the pexl project model."""
    return Project.from_excel(Path(path))


def apply_preset_filters(view):
    """Render preset filters and return the filtered ProjectView."""
    st.sidebar.header("Presetauswahl")

    preset_vars = [
        meta
        for meta in view.variables
        if meta.var_name.startswith("preset_recorded_")
    ]

    for meta in preset_vars:
        values = view.scenarios.unique(meta.var_name)
        if len(values) <= 1:
            continue

        label = meta.label_de or meta.var_name.removeprefix("preset_recorded_").replace("_", " ").title()
        selected = st.sidebar.selectbox(
            label,
            options=["Alle", *values],
            key=f"filter_{meta.var_name}",
        )

        if selected != "Alle":
            view = view.where(**{meta.var_name: selected})

    return view


def render_sidebar() -> str:
    """Render project-file controls and return the active file path."""
    if "data_path" not in st.session_state:
        st.session_state.data_path = load_saved_path()

    with st.sidebar:
        st.header("Datenquelle")

        if st.session_state.data_path:
            st.info(f"Aktuelle Datei:\n{Path(st.session_state.data_path).name}")
        else:
            st.warning("Keine Daten geladen.")

        if st.button("Projekt-Export öffnen"):
            path = select_file()
            if path:
                st.session_state.data_path = path
                save_path(path)
                st.rerun()

        st.divider()

    return st.session_state.data_path


def main() -> None:
    """Run the Streamlit Quick-Check dashboard."""
    st.set_page_config(page_title=APP_TITLE, layout="wide")

    file_path = render_sidebar()
    if not file_path or not Path(file_path).exists():
        st.title(APP_TITLE)
        st.info("Bitte wähle über die Seitenleiste einen PEExcel-Projektexport aus.")
        return

    try:
        project = load_project(file_path)
    except Exception as exc:
        st.error(f"Fehler beim Laden der Datei: {exc}")
        return

    if project.warnings:
        with st.sidebar.expander(f"Importhinweise ({len(project.warnings)})"):
            for warning in project.warnings:
                st.write(warning)

    view = apply_preset_filters(project.view)

    st.title(APP_TITLE)
    st.markdown(f"**Aktuell werden {len(view.scenarios)} Varianten angezeigt.**")

    if len(view.scenarios) == 0:
        st.warning("Keine Varianten passen zur gewählten Filterkonfiguration.")
        return

    reports = [
        reporting.materialize(view, chart_name)
        for chart_name in reporting.chart_names()
    ]

    tabs = st.tabs(
        ["Übersicht (Alle)"]
        + [report.get("tab_name") or report["title"] for report in reports]
    )

    with tabs[0]:
        for report in reports:
            st.plotly_chart(
                plotly.render(report),
                width="stretch",
                theme="streamlit",
                key=f"overview_{report['chart_name']}",
            )
            st.divider()

    for tab, report in zip(tabs[1:], reports):
        with tab:
            st.plotly_chart(
                plotly.render(report),
                width="stretch",
                theme="streamlit",
                key=f"detail_{report['chart_name']}",
            )
            st.subheader("Chart Data (Diagrammdaten)")
            st.dataframe(report["frame"], width="stretch")


if __name__ == "__main__":
    main()