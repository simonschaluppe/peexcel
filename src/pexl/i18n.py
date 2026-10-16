from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Language = Literal["de", "en"]


@dataclass(frozen=True)
class LocalizedText:
    """German and English public-facing text."""

    de: str
    en: str

    def get(self, language: Language) -> str:
        """Return the text in the requested language."""
        return getattr(self, language)