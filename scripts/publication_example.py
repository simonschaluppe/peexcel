"""Synthetic publication workflow shared by Quarto, notebooks and tests.

Run from the repository root: python scripts/publication_example.py
All numeric scenario values are illustrative, not simulation results.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
import plotly.graph_objects as go

from pexl import Project, reporting
from pexl.analysis.targets import Zielwert
from pexl.plot import electricity_balance, plotly
from pexl.plot.export import export_figure
from pexl.schema.current import ATTR_NAME_MAP, CHARTS, SCHEMA_VERSION


CHART_NAMES = ("primary_energy_balance", "gwp_ee_detail")


def example_project():
    """Build a small Project using the active schema, without private inputs."""
    project = Project()
    for name, scale in (("Synthetisch A", 1.0), ("Synthetisch B", 0.7)):
        scenario = project.get_or_create_scenario(name)
        for chart_name in CHART_NAMES:
            for index, series in enumerate(CHARTS[chart_name].series):
                value = (index + 1) * 3.0 * scale
                if "kompensation" in (series.role or "").lower():
                    value = -value
                setattr(scenario.v, ATTR_NAME_MAP[series.var_name], value)
    return project


def density_figure():
    model = Zielwert.ZQSynergy()
    gfz = np.linspace(0, 5, 51)
    fig = go.Figure()
    fig.add_scatter(x=gfz, y=model.target(gfz), name="Dichteabhängiger Zielwert")
    fig.add_scatter(x=gfz, y=model.context_factor(gfz), name="Virtuelle Gut-/Lastschrift")
    fig.update_layout(title="Dichtekontext – ZQ Synergy (historischer Parametersatz)",
                      xaxis_title="GFZ [-]", yaxis_title="kWhPE/(m² NGF a)")
    fig.add_annotation(x=0, y=1.15, xref="paper", yref="paper", showarrow=False,
                       xanchor="left", text="Kontextfaktor ist kein realer Energiefluss")
    return fig, (f"Zielwert.ZQSynergy: A={model.A}, dx={model.dx}, EUI={model.EUI}, "
                 f"fPE={model.fPE}, cutoff={model.cutoff}; Bezug NGF. "
                 "Gut-/Lastschrift = negativer Zielwert; kein realer Energiefluss.")


def mobility_figure(shares, budgets, actual):
    """Prototype: area-weight existing per-NGF budget inputs, never infer them.

    Mirrors SCHEMA_META.context_factor_mobility.formula (area / total area).
    Inputs must share kWhPE/(m² NGF a); actual is positive demand. The budget
    allocation's national derivation is outside this plotting example.
    """
    if (not shares or set(shares) != set(budgets)
            or not np.isfinite(list(shares.values())).all()
            or not np.isfinite(list(budgets.values())).all()
            or any(v < 0 for v in shares.values())
            or any(v < 0 for v in budgets.values())
            or not np.isclose(sum(shares.values()), 1)
            or not np.isfinite(actual) or actual < 0):
        raise ValueError("Require matching non-negative budgets/shares summing to 1 and demand >= 0")
    budget = sum(shares[k] * budgets[k] for k in shares)
    fig = go.Figure(go.Bar(
        x=["Zugeordnetes Budget", "Tatsächlicher Bedarf", "Bilanzbeitrag (Budget − Bedarf)"],
        y=[budget, actual, budget - actual], texttemplate="%{y:.1f}",
    ))
    fig.update_layout(title="Mobilitätsbudget – synthetische Eingaben",
                      yaxis_title="kWhPE/(m² NGF a)")
    return fig


def example_figures():
    """Return existing Figure objects and their explicit conventions."""
    project = example_project()
    figures = {}
    for name in CHART_NAMES:
        report = reporting.materialize(project.view, name)
        fig = plotly.render(report)
        convention = ("Bedarf und Deckung als positive Beträge in getrennten Säulen; "
                      "Kontextfaktoren sind virtuelle Beiträge.") if name == CHART_NAMES[0] else (
            "Vorzeichen wie im Report; negative Werte = Kompensation. "
            "L1/L2/L3: bestehende Renderer-Bänder, keine neu berechneten Budgets. "
            "Bewertung 2025–2075 (50 Jahre); nationales Zieljahr und "
            "Dekarbonisierungspfad sind im synthetischen Datensatz nicht definiert.")
        figures[name] = fig, convention
    flows = pd.DataFrame({"Stunde": [0, 1, 2, 3], "E_grid": [2, 1, 0, 0],
                          "PV_to_Egrid": [0, 0, 2, 3]})
    figures["electricity"] = electricity_balance(
        flows, positive=["E_grid"], negative=["PV_to_Egrid"], x="Stunde",
        title="Synthetische Stromflüsse", x_title="Stunde", y_title="kWh je Stunde",
    ), "Netzbezug positiv; PV-Netzeinspeisung negativ. Keine weitere Aggregation."
    figures["density"] = density_figure()
    shares = {"Wohnen": 0.7, "Büro": 0.3}
    budgets = {"Wohnen": 20.0, "Büro": 10.0}
    figures["mobility"] = mobility_figure(shares, budgets, actual=22), (
        "Synthetische Demonstration, keine nationalen Referenzwerte: "
        "70 % Wohnen × 20 + 30 % Büro × 10 = 17; Bedarf 22; Beitrag −5. "
        "Mobilität eingeschlossen. Budget und Bedarf getrennt; positiv = Gutschrift.")
    return figures


def provenance(convention):
    return {
        "source": "scripts/publication_example.py; synthetisch, keine Projektdaten",
        "scenario": "Synthetisch A/B; Methoden- und Strombeispiele separat",
        "model_version": "Illustration ohne Excel-Berechnung; kein Stable-/Development-Release",
        "schema_version": SCHEMA_VERSION,
        "calculated_at": "Keine Simulation; deterministische synthetische Beispielwerte",
        "convention": convention,
    }


def build(output, formats=("html", "svg", "png")):
    paths = []
    for name, (figure, convention) in example_figures().items():
        for fmt in formats:
            paths.append(export_figure(figure, Path(output) / f"{name}.{fmt}",
                                       provenance=provenance(convention)))
    return paths


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("website/assets"))
    parser.add_argument("--formats", nargs="+", choices=["html", "svg", "png", "pdf"],
                        default=["html", "svg", "png"])
    args = parser.parse_args()
    build(args.output, args.formats)
