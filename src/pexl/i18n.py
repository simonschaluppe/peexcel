from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Language = Literal["de", "en"]

# TODO(i18n, deferred): The website currently targets German only. English
# rendering, navigation and translation parity are not build/acceptance criteria.
# Keep existing LocalizedText and explicit language="en" callers compatible.
# Inventory and staged decisions: docs/development/website_scripts_audit.md.
# Before restoring English website support, resolve these together:
# - One language/fallback policy for labels, units, missing-value text and errors;
#   preserve canonical schema keys, scenario names and recorded preset names.
# - Localize reporting.materialize, plot/export labels, temporal inventories and
#   spatial teaching labels through the same public Python APIs as notebooks.
# - Replace output_catalog.DOMAIN_LABELS as a separate translation dictionary;
#   preserve actual schema domain/source values (including BOTH semantics).
# - Supply browser labels/locales from the same language source for the catalog,
#   Quick-Check and teaching viewers; no independently maintained JS dictionary.
# - Cover number/date formatting, search normalization and German-only heuristics
#   such as heating-family splitting and default scenario selection.
# - Reconcile website/en sources, language links, URLs, notebook/data downloads and
#   Quarto configuration; do not revive render_english_site.py as a second build.
# - Verify notebook/browser/export parity before making English a supported target.
# Scope update: chart-wide library localization is part of the plotting design;
# English website publication remains deferred. See section 5 of
# docs/development/website_layout_refactor_plan.md. Reuse LocalizedText and schema
# labels; do not introduce a separate translation framework or language-specific
# renderer copies. Keep semantic IDs independent of display translations.


@dataclass(frozen=True)
class LocalizedText:
    """German and English public-facing text."""

    de: str
    en: str

    def get(self, language: Language) -> str:
        """Return the text in the requested language."""
        return getattr(self, language)


# Shared reference-chart vocabulary. Keys are semantic, never translated IDs.
CHART_TEXT = {
    "primary_energy": LocalizedText("Primärenergiebedarf", "Primary energy demand"),
    "demand": LocalizedText("Bedarf", "Demand"),
    "supply": LocalizedText("Deckung", "Supply"),
    "difference": LocalizedText("Deckung − Bedarf", "Supply − demand"),
    "value": LocalizedText("Wert", "Value"),
    "hour": LocalizedText("Tagesstunde", "Hour of day"),
    "time": LocalizedText("Zeit", "Time"),
    "all": LocalizedText("Gesamter Zeitraum", "Full period"),
}


def chart_text(key, language="de"):
    if language not in ("de", "en"):
        raise ValueError("language must be 'de' or 'en'")
    return CHART_TEXT[key].get(language)


PRIMARY_ENERGY_LABELS = {
    'PEI_el_plugloads': LocalizedText('Nutzerstrom', 'Plug loads'),
    'PEI_sub_PV': LocalizedText('Lokale Erneuerbare (Netzstrom Substitutionsäquivalent)', 'Local renewables (grid electricity substitution equivalent)'),
    'PEI_el_hvac': LocalizedText('HKLS Strom', 'HVAC electricity'),
    'PEI_sub_flex': LocalizedText('Energieflexibilität (Netzstrom Substitutionsäquivalent)', 'Energy flexibility (grid electricity substitution equivalent)'),
    'PEI_district_heating': LocalizedText('HKLS Fernwärme', 'HVAC district heating'),
    'PEI_cf_density_pos': LocalizedText('Kontext bauliche Dichte positiv', 'Density context positive'),
    'PEI_natural_gas': LocalizedText('HKLS Erdgas', 'HVAC natural gas'),
    'PEI_cf_mobility': LocalizedText('Kontext Mobilität', 'Mobility context'),
    'PEI_biomass': LocalizedText('HKLS Biomasse', 'HVAC biomass'),
    'PEI_cf_renovation': LocalizedText('Kontext Sanierung', 'Renovation context'),
    'PEI_other': LocalizedText('HKLS Sonstige', 'HVAC other'),
    'PEI_mob_fossile': LocalizedText('MIV Fossil', 'Private motorised transport, fossil'),
    'PEI_mob_el': LocalizedText('MIV Elektrisch', 'Private motorised transport, electric'),
    'PEI_cf_density_neg': LocalizedText('Kontext bauliche Dichte negativ', 'Density context negative'),
}
