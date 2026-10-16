import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import os
import json
import tkinter as tk
from tkinter import filedialog

# ==========================================
# 0. HILFSFUNKTIONEN & KONFIGURATION
# ==========================================

CONFIG_FOLDER = ".streamlit"
CONFIG_FILE = os.path.join(CONFIG_FOLDER, "path_config.json")

def load_saved_path():
    """Lädt den zuletzt verwendeten Dateipfad aus der Konfigurationsdatei."""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                data = json.load(f)
                return data.get("last_path", "")
        except json.JSONDecodeError:
            return ""
    return ""

def save_path(path):
    """Speichert den ausgewählten Dateipfad in der Konfigurationsdatei."""
    os.makedirs(CONFIG_FOLDER, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump({"last_path": path}, f)

def select_file():
    """Öffnet einen nativen Datei-Explorer zur Auswahl einer Excel-Datei."""
    root = tk.Tk()
    root.attributes('-topmost', True)
    root.withdraw()
    
    file_path = filedialog.askopenfilename(
        title="Excel-Datendatei auswählen",
        filetypes=[("Excel-Dateien", "*.xlsx *.xls")]
    )
    
    root.destroy()
    return file_path

def darken_color(hex_color, factor=0.7):
    """Nimmt einen Hex-Farbstring und gibt eine dunklere Version für die Musterstreifen zurück."""
    hex_color = hex_color.strip().strip('#')
    
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
        
    if len(hex_color) != 6:
        return "#000000"
        
    try:
        r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
        r = max(0, int(r * factor))
        g = max(0, int(g * factor))
        b = max(0, int(b * factor))
        return f"#{r:02x}{g:02x}{b:02x}"
    except ValueError:
        return "#000000"

def get_chart_columns(config):
    """Extrahiert alle variablen Spaltennamen dynamisch aus der Konfiguration."""
    cols = []
    kwargs = config.get("chart_kwargs", {})
    
    variable_groups = kwargs.get("variable_groups", {})
    for dest, var_list in variable_groups.items():
        if isinstance(var_list, list):
            cols.extend(var_list)
        elif isinstance(var_list, str):
            cols.append(var_list)
            
    unique_cols = []
    for c in cols:
        if c not in unique_cols:
            unique_cols.append(c)
            
    return ["Variant"] + unique_cols


# ==========================================
# 1. DATENSCHICHT (DATA LAYER)
# ==========================================

@st.cache_data
def load_data(file_path):
    """Lädt und verarbeitet die Excel-Daten für die Varianten-Werte (IN/OUT)."""
    df_in_raw = pd.read_excel(file_path, sheet_name="IN")
    df_out_raw = pd.read_excel(file_path, sheet_name="OUT")
    
    df_out_raw.set_index("var_name", inplace=True)
    df_out_raw = df_out_raw[df_out_raw.index.notna()]

    default_pos = df_out_raw.columns.get_loc("Default") + 1
    variant_columns = df_out_raw.columns[default_pos:] 
    
    df_out_filtered = df_out_raw[variant_columns]
    df_out = df_out_filtered.T.reset_index().rename(columns={"index": "Variant"})
    
    df_in_raw.set_index("var_name", inplace=True)
    df_in_raw = df_in_raw[df_in_raw.index.notna()]
    df_in_filtered = df_in_raw[variant_columns]
    df_in = df_in_filtered.T.reset_index().rename(columns={"index": "Variant"})
    
    df_final = pd.merge(df_in, df_out, on="Variant")
    
    for col in df_final.columns:
        if col == "Variant":
            continue 
            
        try:
            df_final[col] = pd.to_numeric(df_final[col])
        except (ValueError, TypeError):
            pass
            
    return df_final

@st.cache_data
def load_metadata(file_path):
    """Lädt und verarbeitet die Metadaten aus dem chart_info-Dokument."""
    df_meta = pd.read_excel(file_path, sheet_name="metadata")
    
    metadata = {}
    for _, row in df_meta.iterrows():
        var_name = row.get("var_name")
        if pd.isna(var_name):
            continue
            
        pattern_val = row.get("pattern", "")
        clean_pattern = str(pattern_val) if pd.notna(pattern_val) and str(pattern_val).strip().lower() not in ["nan", "none", ""] else ""
        
        domain_val = row.get("domain", "")
        clean_domain = str(domain_val).strip() if pd.notna(domain_val) else ""
        
        dest_val = row.get("destination", "")
        clean_dest = str(dest_val).strip() if pd.notna(dest_val) else ""
        
        metadata[var_name] = {
            "label_de": str(row.get("label_de", var_name)) if pd.notna(row.get("label_de")) else str(var_name),
            "color": str(row.get("color", "#FF00B3")) if pd.notna(row.get("color")) else "#FF00B3",
            "pattern": clean_pattern,
            "diagram": clean_domain,
            "destination": clean_dest
        }   
    return metadata


# ==========================================
# 2. VISUALISIERUNGSSCHICHT
# ==========================================

def get_marker_dict(color, pattern):
    marker = {"color": color}
    if color.strip().lower() == "#ffffff":
        marker["line"] = dict(color="black", width=1)
    if pattern:
        marker["pattern"] = dict(shape=pattern, fgcolor=darken_color(color), bgcolor=color)
    return marker

def build_comparison_chart(df, metadata, title, y_axis_title, variable_groups):
    bedarf_vars = variable_groups.get("Bedarf", [])
    deckung_vars = variable_groups.get("Deckung", [])
    
    fig = go.Figure()
    variants = df["Variant"].tolist()
    x_bedarf = [variants, ["Bedarf"] * len(variants)]
    x_deckung = [variants, ["Deckung"] * len(variants)]

    for var_key in bedarf_vars:
        if var_key in df.columns:
            label_de = metadata.get(var_key, {}).get("label_de", var_key)
            color = metadata.get(var_key, {}).get("color", "#cccccc")
            pattern = metadata.get(var_key, {}).get("pattern", "")
            y_values = df[var_key].abs().tolist()
            
            fig.add_trace(go.Bar(
                name=label_de, x=x_bedarf, y=y_values, 
                marker=get_marker_dict(color, pattern), text=y_values,
                texttemplate="<b>%{y:.1f}</b>", textposition="inside", insidetextanchor="middle",
                textfont=dict(size=12, color="black", family="Arial"),
                legendgroup="Bedarf", legendgrouptitle_text="Bedarf",
                hovertemplate=f"<b>{label_de}</b><br>Wert: %{{y:.1f}}<extra></extra>"
            ))

    for var_key in deckung_vars:
        if var_key in df.columns:
            label_de = metadata.get(var_key, {}).get("label_de", var_key)
            color = metadata.get(var_key, {}).get("color", "#cccccc")
            pattern = metadata.get(var_key, {}).get("pattern", "")
            y_values = df[var_key].abs().tolist()
            
            fig.add_trace(go.Bar(
                name=label_de, x=x_deckung, y=y_values, 
                marker=get_marker_dict(color, pattern), text=y_values,
                texttemplate="<b>%{y:.1f}</b>", textposition="inside", insidetextanchor="middle",
                textfont=dict(size=12, color="black", family="Arial"),
                legendgroup="Deckung", legendgrouptitle_text="Deckung",
                hovertemplate=f"<b>{label_de}</b><br>Wert: %{{y:.1f}}<extra></extra>"
            ))

    fig.update_layout(
        title=title, barmode='stack', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        yaxis_title=y_axis_title, xaxis=dict(tickangle=0, dividerwidth=2, dividercolor="gray", showgrid=False),
        yaxis=dict(gridcolor="gray", griddash="dot"), legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02),
        margin=dict(t=50, l=50, r=150, b=50)
    )
    return fig

def build_gwp_chart(df, metadata, title, y_axis_title, variable_groups):
    ee_vars = variable_groups.get("Baulich", [])
    oe_vars = variable_groups.get("Betrieblich", [])
    balance_vars = variable_groups.get("Balance Variable", [])
    balance_var = balance_vars[0] if balance_vars else None
    
    limit_bands = [
        {"name": "L3", "y0": 195, "y1": 320, "color": "#CFDCE0"},
        {"name": "L2", "y0": 70,  "y1": 195, "color": "#93B9C6"},
        {"name": "L1", "y0": 0,   "y1": 70,  "color": "#73A8BB"}
    ]
    fig = go.Figure()
    variants = df["Variant"].tolist()
    
    x_top = [var for var in variants for _ in (0, 1)]
    x_bottom = ['Baulich', 'Betrieblich'] * len(variants)
    x_axis = [x_top, x_bottom]

    def interleave(values, is_oe=False):
        interleaved = []
        for v in values:
            if is_oe: interleaved.extend([0, v])  
            else: interleaved.extend([v, 0])  
        return interleaved

    if limit_bands:
        for band in limit_bands:
            fig.add_hrect(
                y0=band["y0"], y1=band["y1"], fillcolor=band["color"], opacity=0.4, 
                layer="below", line_width=0
            )
            fig.add_trace(go.Bar(
                x=[[variants[0]], ['Baulich']], y=[None], name=f'☁ {band["name"]}',
                marker=dict(color=band["color"]), showlegend=True
            ))

    def add_dynamic_trace(var_keys, is_oe):
        for var_key in var_keys:
            if var_key in df.columns:
                label = metadata.get(var_key, {}).get("label_de", var_key)
                color = metadata.get(var_key, {}).get("color", "#cccccc")
                pattern_shape = metadata.get(var_key, {}).get("pattern", "")
                
                y_data = interleave(df[var_key].tolist(), is_oe=is_oe)
                marker = dict(color=color)
                
                if color.strip().lower() == "#ffffff":
                    marker["line"] = dict(color="gray", width=1)
                if pattern_shape:
                    marker['pattern'] = dict(shape=pattern_shape, fillmode="replace", fgcolor=darken_color(color), bgcolor=color)
                
                fig.add_trace(go.Bar(
                    name=label, x=x_axis, y=y_data, marker=marker, width=0.6,
                    hovertemplate=f"<b>{label}</b><br>Wert: %{{y:.1f}}<extra></extra>"
                ))

    add_dynamic_trace(ee_vars, is_oe=False)
    add_dynamic_trace(oe_vars, is_oe=True)

    if balance_var and balance_var in df.columns:
        balance_y = df[balance_var].tolist()
        balance_x = [variants, ee_vars[0] * len(variants)]
        
        fig.add_trace(go.Scatter(
            name='THG Ökobilanz', x=balance_x, y=balance_y, mode='markers+text',
            marker=dict(symbol='diamond', color='#7B8E1D', size=8),
            text=[f"  {val:.1f}" for val in balance_y], textposition='middle right',
            textfont=dict(color='#7B8E1D', size=12, family="Arial")
        ))

    fig.update_layout(
        title=title, barmode='relative', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02),
        yaxis=dict(title=y_axis_title, autorange=True, gridcolor="gray", griddash="dot", zerolinecolor="gray", zerolinewidth=2),
        xaxis=dict(type='multicategory', tickangle=0, dividercolor="gray", dividerwidth=2, showgrid=False),
        margin=dict(l=50, r=150, t=50, b=50) 
    )
    return fig

def build_four_column_gwp_chart(df, metadata, title, y_axis_title, variable_groups):
    
    ee_vars = variable_groups.get("Baulich", [])
    ee_offset_vars = variable_groups.get("Baulich kompensation", [])
    oe_vars = variable_groups.get("Betrieblich", [])
    oe_offset_vars = variable_groups.get("Betrieblich kompensation", [])
    
    limit_bands = [
        {"name": "L3", "y0": 195, "y1": 320, "color": "#CFDCE0"},
        {"name": "L2", "y0": 70,  "y1": 195, "color": "#93B9C6"},
        {"name": "L1", "y0": 0,   "y1": 70,  "color": "#73A8BB"}
    ]

    fig = go.Figure()
    variants = df["Variant"].tolist()
    
    x_variant = [var for var in variants for _ in range(4)]
    x_type = ['Baulich', 'Baulich kompensation', 'Betrieblich', 'Betrieblich kompensation'] * len(variants)
    x_axis = [x_variant, x_type]

    def interleave_four(values, target_col_idx):
        interleaved = []
        for v in values:
            row_vals = [0, 0, 0, 0]
            row_vals[target_col_idx] = v
            interleaved.extend(row_vals)
        return interleaved

    if limit_bands:
        for band in limit_bands:
            fig.add_hrect(
                y0=band["y0"], y1=band["y1"], fillcolor=band["color"], opacity=0.4, 
                layer="below", line_width=0
            )
            fig.add_trace(go.Bar(
                x=[[variants[0]], x_type[0]], y=[None], name=f'{band["name"]}',
                marker=dict(color=band["color"]), showlegend=True
            ))

    def add_traces_for_group(var_keys, col_idx):
        for var_key in var_keys:
            if var_key in df.columns:
                label = metadata.get(var_key, {}).get("label_de", var_key)
                color = metadata.get(var_key, {}).get("color", "#cccccc")
                pattern_shape = metadata.get(var_key, {}).get("pattern", "")
                
                y_data = interleave_four(df[var_key].tolist(), col_idx)
                marker = dict(color=color)
                
                if color.strip().lower() == "#ffffff":
                    marker["line"] = dict(color="gray", width=1)
                if pattern_shape:
                    marker['pattern'] = dict(shape=pattern_shape, fillmode="replace", fgcolor=darken_color(color), bgcolor=color)
                
                fig.add_trace(go.Bar(
                    name=label, x=x_axis, y=y_data, marker=marker, width=0.6,
                    hovertemplate=f"<b>{label}</b><br>Wert: %{{y:.1f}}<extra></extra>"
                ))

    add_traces_for_group(ee_vars, col_idx=0)
    add_traces_for_group(ee_offset_vars, col_idx=1)
    add_traces_for_group(oe_vars, col_idx=2)
    add_traces_for_group(oe_offset_vars, col_idx=3)

    fig.update_layout(
        title=title, barmode='relative', plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        legend=dict(orientation="v", yanchor="top", y=1, xanchor="left", x=1.02),
        yaxis=dict(title=y_axis_title, autorange=True, gridcolor="gray", griddash="dot", zerolinecolor="gray", zerolinewidth=2),
        xaxis=dict(type='multicategory', tickangle=90, dividercolor="gray", dividerwidth=2, showgrid=False),
        margin=dict(l=50, r=180, t=50, b=50) 
    )
    return fig


# ==========================================
# 3. DYNAMISCHER DIAGRAMM-KONFIGURATOR
# ==========================================

def get_chart_configs(file_path, metadata):
    """Erstellt dynamisch CHART_CONFIGS unter Verwendung der Datei chart_info.xlsx."""
    df_info = pd.read_excel(file_path, sheet_name="diagram_info")
    configs = []
    
    for _, row in df_info.iterrows():
        diagram_id = row.get("diagram")
        tab_name = row.get("tab_name")
        title = row.get("title")
        func_name = row.get("build_function")
        y_axis_title = row.get("y_axis_title", "") 
        
        build_func = globals().get(func_name)
        if not build_func:
            continue
            
        variable_groups = {}
        for var, meta in metadata.items():
            if meta.get("diagram") == diagram_id:
                dest = meta.get("destination")
                if dest:
                    if dest not in variable_groups:
                        variable_groups[dest] = []
                    variable_groups[dest].append(var)
                    
        chart_kwargs = {
            "title": title,
            "y_axis_title": y_axis_title,
            "variable_groups": variable_groups
        }
            
        configs.append({
            "tab_name": tab_name,
            "build_func": build_func,
            "chart_kwargs": chart_kwargs
        })
        
    return configs


# ==========================================
# 4. UI / APP SCHICHT (Streamlit Layout)
# ==========================================

def main():
    st.set_page_config(page_title="klimaaktiv Quick-Check", layout="wide")
    
    if "data_path" not in st.session_state:
        st.session_state.data_path = load_saved_path()

    with st.sidebar:
        st.header("Datenquelle")
        
        if st.session_state.data_path:
            st.info(f"Aktuelle Datei: \n{os.path.basename(st.session_state.data_path)}")
        else:
            st.warning("Keine Daten geladen.")
            
        if st.button("Projekt-Export öffnen"):
            new_path = select_file()
            if new_path:
                st.session_state.data_path = new_path
                save_path(new_path)
                st.rerun()
                
        st.divider()

    file_path = st.session_state.data_path
    if not file_path or not os.path.exists(file_path):
        st.title("klimaaktiv Quick-Check")
        st.info("Bitte wähle über die Seitenleiste ('Projekt-Export öffnen') eine Excel-Datei aus, um zu starten.")
        return

    # Die chart_info.xlsx ist strikt verantwortlich für alles, was geplottet wird
    diagram_info_path = "chart_info.xlsx"
    try:
        df = load_data(file_path)
        metadata = load_metadata(diagram_info_path)
    except Exception as e:
        st.error(f"Fehler beim Laden der Datei: {e}")
        return

    chart_configs = get_chart_configs(diagram_info_path, metadata)

    st.sidebar.header("Presetauswahl")
    active_filters = {}
    
    current_filtered_df = df.copy()
    filter_columns = [col for col in current_filtered_df.columns if str(col).startswith("preset_recorded_")]
    
    for excel_col in filter_columns:
        key = excel_col.replace("preset_recorded_", "")
        available_values = current_filtered_df[excel_col].dropna().unique().tolist()
        
        if len(available_values) <= 1:
            active_filters[key] = "Alle"
            continue 
        
        options = ["Alle"] + available_values
                
        display_name = key.replace("_", " ").title()
        selected_val = st.sidebar.selectbox(display_name, options=options)
        active_filters[key] = selected_val
        
        if selected_val != "Alle":
            current_filtered_df = current_filtered_df[current_filtered_df[excel_col] == selected_val]

    filtered_df = current_filtered_df

    st.title("klimaaktiv Quick-Check")
    st.markdown(f"**Aktuell werden {len(filtered_df)} Varianten angezeigt.**")

    if filtered_df.empty:
        st.warning("Keine Varianten passen zur eingegebenen Filterkonfiguration.")
        return

    # Tabs werden NUR auf Basis der in 'chart_info.xlsx' definierten config generiert
    tab_names = ["Übersicht (Alle)"] + [config["tab_name"] for config in chart_configs]
    tabs = st.tabs(tab_names)
    
    # --- 1. ÜBERSICHTS-TAB (Alle Diagramme untereinander, KEINE Datentabelle) ---
    with tabs[0]:
        for config in chart_configs:
            fig = config["build_func"](
                df=filtered_df,
                metadata=metadata,
                **config["chart_kwargs"] 
            )
            st.plotly_chart(fig, width='stretch', theme="streamlit", key=f"overview_{config['tab_name']}")
            st.markdown("---")
            
    # --- 2. INDIVIDUELLE TABS (Ein Diagramm pro Tab inkl. zugehöriger Datentabelle) ---
    for tab, config in zip(tabs[1:], chart_configs):
        with tab:
            fig = config["build_func"](
                df=filtered_df,
                metadata=metadata,
                **config["chart_kwargs"] 
            )
            st.plotly_chart(fig, width='stretch', theme="streamlit", key=f"detail_{config['tab_name']}")
            
            relevant_columns = get_chart_columns(config)
            existing_columns = [col for col in relevant_columns if col in filtered_df.columns]
            
            display_df = filtered_df[existing_columns].copy()
            rename_dict = {}
            for col in existing_columns:
                if col != "Variant":
                    label = metadata.get(col, {}).get("label_de", col)
                    rename_dict[col] = f"{label} ({col})"
                    
            display_df.rename(columns=rename_dict, inplace=True)
            
            st.subheader("Chart Data (Diagrammdaten)")
            st.dataframe(display_df, width='stretch', hide_index=True)

if __name__ == "__main__":
    main()