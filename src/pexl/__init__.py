from __future__ import annotations

import importlib

__all__ = ["Project", "plot"]


def __getattr__(name: str):
    if name == "Project":
        from pexl.model.project import Project
        return Project

    if name == "plot":
        return importlib.import_module(".plot", __name__)

    raise AttributeError(
        f"module {__name__!r} has no attribute {name!r}"
    )