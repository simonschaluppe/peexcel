from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import keyword
import re
from typing import Any

import pandas as pd


RESERVED_IN_COLUMN_HEADER_NAMES = [
    "Icon",
    "Name",
    "Einheit",
    "Kommentar",
    "Type",
    "var_name",
    "ka",
    "Formel",
]

RESERVED_OUT_COLUMN_HEADER_NAMES = [
    "ID",
    "Kategorie",
    "Type",
    "Name",
    "Icon",
    "Bereich",
    "var_cat",
    "var_name",
    "Einheit",
    "Formel",
    "Label",
    "Kommentar",
]


@dataclass(frozen=True)
class VariableMetaRow:
    var_name: str
    attr_name: str
    icon: str | None = None
    real_name: str | None = None
    unit: str | None = None
    type_name: str | None = None
    comment: str | None = None
    source: str | None = None  # "IN", "OUT", "BOTH"
    ka: int | None = None
    category: str | None = None
    area: str | None = None
    label: str | None = None
    var_cat: str | None = None


def sanitize_identifier(name: str) -> str:
    s = str(name).strip()
    s = s.replace(" ", "_").replace("-", "_").replace("/", "_")
    s = re.sub(r"[^0-9a-zA-Z_]", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")

    if not s:
        s = "unnamed"

    if s[0].isdigit():
        s = f"v_{s}"

    if keyword.iskeyword(s):
        s = f"{s}_"

    return s


def unique_name_map(names: list[str]) -> dict[str, str]:
    used: set[str] = set()
    out: dict[str, str] = {}

    for raw in names:
        base = sanitize_identifier(raw)
        candidate = base
        i = 2
        while candidate in used:
            candidate = f"{base}_{i}"
            i += 1
        used.add(candidate)
        out[raw] = candidate

    return out


def clean_cell(value: Any) -> Any:
    if pd.isna(value):
        return None
    if isinstance(value, str):
        value = value.strip()
        return value if value else None
    return value


def as_python_literal(value: Any) -> str:
    if value is None:
        return "None"
    return repr(value)


def first_nonempty(*values: Any) -> Any:
    for v in values:
        v = clean_cell(v)
        if v is not None:
            return v
    return None


def optional_int(value: Any) -> int | None:
    value = clean_cell(value)
    if value is None:
        return None
    try:
        return int(value)
    except (ValueError, TypeError):
        return None


def collect_rows_by_var_name(df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if "var_name" not in df.columns:
        raise ValueError("Sheet must contain column 'var_name'.")

    out: dict[str, dict[str, Any]] = {}
    for _, row in df.iterrows():
        var_name = clean_cell(row.get("var_name"))
        if not var_name:
            continue
        out[str(var_name)] = {col: clean_cell(row.get(col)) for col in df.columns}
    return out


def merge_meta(
    var_name: str,
    attr_name: str,
    in_row: dict[str, Any] | None,
    out_row: dict[str, Any] | None,
) -> VariableMetaRow:
    in_exists = in_row is not None
    out_exists = out_row is not None

    if in_exists and out_exists:
        source = "BOTH"
    elif in_exists:
        source = "IN"
    elif out_exists:
        source = "OUT"
    else:
        source = None

    return VariableMetaRow(
        var_name=var_name,
        attr_name=attr_name,
        icon=first_nonempty(
            in_row.get("Icon") if in_row else None,
            out_row.get("Icon") if out_row else None,
        ),
        real_name=first_nonempty(
            in_row.get("Name") if in_row else None,
            out_row.get("Name") if out_row else None,
        ),
        unit=first_nonempty(
            in_row.get("Einheit") if in_row else None,
            out_row.get("Einheit") if out_row else None,
        ),
        type_name=first_nonempty(
            in_row.get("Type") if in_row else None,
            out_row.get("Type") if out_row else None,
        ),
        comment=first_nonempty(
            in_row.get("Kommentar") if in_row else None,
            out_row.get("Kommentar") if out_row else None,
        ),
        source=source,
        ka=optional_int(in_row.get("ka")) if in_row else None,
        category=first_nonempty(out_row.get("Kategorie") if out_row else None),
        area=first_nonempty(out_row.get("Bereich") if out_row else None),
        label=first_nonempty(out_row.get("Label") if out_row else None),
        var_cat=first_nonempty(out_row.get("var_cat") if out_row else None),
    )


def build_vars_class_code(var_names: list[str], name_map: dict[str, str]) -> str:
    lines: list[str] = []
    lines.append("class ExcelNamedVariables:")
    lines.append("    def __init__(self):")
    if not var_names:
        lines.append("        pass")
        return "\n".join(lines)

    for var_name in var_names:
        attr_name = name_map[var_name]
        if attr_name == var_name:
            lines.append(f"        self.{attr_name}: object | None = None")
        else:
            lines.append(f"        self.{attr_name}: object | None = None  # var_name: {var_name}")
    return "\n".join(lines)


def build_variable_meta_dataclass_code() -> str:
    return """@dataclass(frozen=True)
class VariableMeta:
    var_name: str
    attr_name: str
    icon: str | None = None
    real_name: str | None = None
    unit: str | None = None
    type_name: str | None = None
    comment: str | None = None
    source: str | None = None
    ka: int | None = None
    category: str | None = None
    area: str | None = None
    label: str | None = None
    var_cat: str | None = None

    def __repr__(self) -> str:
        parts = []

        # main identifier
        if self.icon:
            parts.append(f"{self.icon}")

        name = self.var_name
        if self.real_name:
            name += f" ({self.real_name})"

        parts.append(name)
        # unit + type
        if self.unit:
            parts.append(f"[{self.unit}]")
        if self.type_name:
            parts.append(f"<{self.type_name}>")

        # ka flag (important for your workflow)
        if self.ka is not None:
            parts.append(f"ka={self.ka}")

        # source info
        if self.source:
            parts.append(f"@{self.source}")

        return "<VarMeta " + " ".join(parts) + ">"
"""


def build_meta_class_code(meta_rows: list[VariableMetaRow]) -> str:
    lines: list[str] = []
    lines.append("class Meta:")
    lines.append("    def __init__(self):")
    if not meta_rows:
        lines.append("        pass")
        return "\n".join(lines)

    for row in meta_rows:
        lines.append(
            f"        self.{row.attr_name} = VariableMeta(\n"
            f"            var_name={row.var_name!r}, \n"
            f"            attr_name={row.attr_name!r}, \n"
            f"            icon={row.icon!r}, \n"
            f"            real_name={as_python_literal(row.real_name)}, \n"
            f"            unit={as_python_literal(row.unit)}, \n"
            f"            type_name={as_python_literal(row.type_name)}, \n"
            f"            comment={as_python_literal(row.comment)}, \n"
            f"            source={as_python_literal(row.source)}, \n"
            f"            ka={as_python_literal(row.ka)}, \n"
            f"            category={as_python_literal(row.category)}, \n"
            f"            area={as_python_literal(row.area)}, \n"
            f"            label={as_python_literal(row.label)}, \n"
            f"            var_cat={as_python_literal(row.var_cat)}\n)"
        )
    return "\n".join(lines)


def build_attr_map_code(name_map: dict[str, str]) -> str:
    lines = ["ATTR_NAME_MAP: dict[str, str] = {"]
    for var_name, attr_name in name_map.items():
        lines.append(f"    {var_name!r}: {attr_name!r},")
    lines.append("}")
    return "\n".join(lines)


def build_fill_values_code() -> str:
    return """def fill_values(vars_obj: Vars, data: dict[str, object], attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> None:
    for var_name, value in data.items():
        attr_name = attr_name_map.get(var_name)
        if attr_name is not None:
            setattr(vars_obj, attr_name, value)
"""


def build_to_dict_code() -> str:
    return """def vars_to_dict(vars_obj: Vars, attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> dict[str, object]:
    out: dict[str, object] = {}
    for var_name, attr_name in attr_name_map.items():
        out[var_name] = getattr(vars_obj, attr_name)
    return out
"""


def generate_schema_module_text(
    df_in: pd.DataFrame,
    df_out: pd.DataFrame,
    version: str = "unknown",
) -> str:
    in_rows = collect_rows_by_var_name(df_in)
    out_rows = collect_rows_by_var_name(df_out)

    all_var_names = sorted(set(in_rows.keys()) | set(out_rows.keys()))
    name_map = unique_name_map(all_var_names)

    meta_rows = [
        merge_meta(
            var_name=var_name,
            attr_name=name_map[var_name],
            in_row=in_rows.get(var_name),
            out_row=out_rows.get(var_name),
        )
        for var_name in all_var_names
    ]

    parts: list[str] = []
    parts.append('"""Auto-generated schema bindings. Do not edit manually!"""')
    parts.append("")
    parts.append("from __future__ import annotations")
    parts.append("from dataclasses import dataclass")
    parts.append("")
    parts.append(f"SCHEMA_VERSION = {version!r}")
    parts.append("")
    parts.append(build_variable_meta_dataclass_code())
    parts.append("")
    parts.append(build_vars_class_code(all_var_names, name_map))
    parts.append("")
    parts.append(build_meta_class_code(meta_rows))
    parts.append("")
    parts.append("SCHEMA_META = Meta()")
    parts.append("")
    parts.append(build_attr_map_code(name_map))
    parts.append("")
    parts.append(build_fill_values_code())
    parts.append("")
    parts.append(build_to_dict_code())
    parts.append("")

    return "\n".join(parts)


def generate_schema_module(
    excel_path: str | Path,
    output_py_path: str | Path,
    version: str | None = None,
) -> Path:
    excel_path = Path(excel_path)
    output_py_path = Path(output_py_path)

    df_in = pd.read_excel(excel_path, sheet_name="IN")
    df_out = pd.read_excel(excel_path, sheet_name="OUT")

    if version is None:
        version = excel_path.stem

    code = generate_schema_module_text(df_in=df_in, df_out=df_out, version=version)

    output_py_path.parent.mkdir(parents=True, exist_ok=True)
    output_py_path.write_text(code, encoding="utf-8")
    return output_py_path


if __name__ == "__main__":
    version = "v1.10_4"
    generate_schema_module(
    excel_path=f"data/exports/schema_{version}.xlsx",
    output_py_path=f"src/pexl/schemas/generated/excel_{version.replace(".", "_")}.py",
    version=version.replace(".", "_"),
)