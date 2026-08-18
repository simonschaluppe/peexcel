from __future__ import annotations

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pexl.schema.current import Meta

    glossary: Meta


__all__ = ["Project", "plot", "glossary"]


def __getattr__(name: str):
    if name == "Project":
        from pexl.model.project import Project
        return Project

    if name == "plot":
        return importlib.import_module(".plot", __name__)

    if name == "glossary":
        from pexl.schema.current import SCHEMA_META
        return SCHEMA_META

    raise AttributeError(
        f"module {__name__!r} has no attribute {name!r}"
    )