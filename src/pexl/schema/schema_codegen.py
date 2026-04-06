from __future__ import annotations
import logging
logger = logging.getLogger(__name__)
logging.basicConfig()
from dataclasses import dataclass
from pathlib import Path
import keyword
import re
from typing import Any

import pandas as pd


CSV_SEP = ";"


@dataclass(frozen=True)
class VariableMetaRow:
    var_name: str
    attr_name: str
    icon: str | None = None
    label_de: str | None = None
    unit: str | None = None
    comment: str | None = None
    source: str | None = None  # "IN" or "OUT"
    ka: int | None = None
    domain: str | None = None
    measure: str | None = None
    spatial_scope: str | None = None
    temporal_scope: str | None = None
    entity_group: str | None = None
    entity_key: str | None = None


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


def optional_int(value: Any) -> int | None:
    value = clean_cell(value)
    if value is None:
        return None
    try:
        return int(float(value))
    except (ValueError, TypeError):
        return None


def collect_rows_by_var_name(df: pd.DataFrame) -> dict[str, dict[str, Any]]:
    if "var_name" not in df.columns:
        raise ValueError("Schema table must contain column 'var_name'.")

    out: dict[str, dict[str, Any]] = {}
    for _, row in df.iterrows():
        var_name = clean_cell(row.get("var_name"))
        if not var_name:
            continue
        out[str(var_name)] = {col: clean_cell(row.get(col)) for col in df.columns}
    return out


def create_row(
    var_name: str,
    attr_name: str,
    row: dict[str, Any],
    source: str,
) -> VariableMetaRow:
    return VariableMetaRow(
        var_name=var_name,
        attr_name=attr_name,
        icon=clean_cell(row.get("icon")),
        label_de=clean_cell(row.get("label_de")),
        unit=clean_cell(row.get("unit")),
        comment=clean_cell(row.get("comment")),
        source=source,
        ka=optional_int(row.get("ka")),
        domain=clean_cell(row.get("domain")),
        measure=clean_cell(row.get("measure")),
        spatial_scope=clean_cell(row.get("spatial_scope")),
        temporal_scope=clean_cell(row.get("temporal_scope")),
        entity_group=clean_cell(row.get("entity_group")),
        entity_key=clean_cell(row.get("entity_key")),
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
    label_de: str | None = None
    unit: str | None = None
    comment: str | None = None
    source: str | None = None
    ka: int | None = None
    domain: str | None = None
    measure: str | None = None
    spatial_scope: str | None = None
    temporal_scope: str | None = None
    entity_group: str | None = None
    entity_key: str | None = None

    def __repr__(self) -> str:
        parts = []

        if self.icon:
            parts.append(self.icon)

        parts.append(self.var_name)

        if self.unit:
            parts.append(f"[{self.unit}]")

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
            f"            label_de={as_python_literal(row.label_de)}, \n"
            f"            unit={as_python_literal(row.unit)}, \n"
            f"            comment={as_python_literal(row.comment)}, \n"
            f"            source={as_python_literal(row.source)}, \n"
            f"            ka={as_python_literal(row.ka)}, \n"
            f"            domain={as_python_literal(row.domain)}, \n"
            f"            measure={as_python_literal(row.measure)}, \n"
            f"            spatial_scope={as_python_literal(row.spatial_scope)}, \n"
            f"            temporal_scope={as_python_literal(row.temporal_scope)}, \n"
            f"            entity_group={as_python_literal(row.entity_group)}, \n"
            f"            entity_key={as_python_literal(row.entity_key)}\n"
            f"        )"
        )
    return "\n".join(lines)


def build_attr_map_code(name_map: dict[str, str]) -> str:
    lines = ["ATTR_NAME_MAP: dict[str, str] = {"]
    for var_name, attr_name in name_map.items():
        lines.append(f"    {var_name!r}: {attr_name!r},")
    lines.append("}")
    return "\n".join(lines)


def build_fill_values_code() -> str:
    return """def fill_values(vars_obj: ExcelNamedVariables, data: dict[str, object], attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> None:
    for var_name, value in data.items():
        attr_name = attr_name_map.get(var_name)
        if attr_name is not None:
            setattr(vars_obj, attr_name, value)
"""


def build_to_dict_code() -> str:
    return """def vars_to_dict(vars_obj: ExcelNamedVariables, attr_name_map: dict[str, str] = ATTR_NAME_MAP) -> dict[str, object]:
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

    overlap = set(in_rows) & set(out_rows)
    if overlap:
        logger.warning(f"var_name overlap between IN and OUT: {sorted(overlap)}")

    rows_by_source = {
        "IN": in_rows,
        "OUT": out_rows,
    }

    all_var_names = list(in_rows.keys())
    all_var_names += [k for k in out_rows.keys() if k not in in_rows]
    name_map = unique_name_map(all_var_names)

    meta_rows = [
        create_row(
            var_name=var_name,
            attr_name=name_map[var_name],
            row=row,
            source=source,
        )
        for source, subrows in rows_by_source.items()
        for var_name, row in subrows.items()
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


def read_schema_csv(csv_path: str | Path) -> pd.DataFrame:
    csv_path = Path(csv_path)
    return pd.read_csv(csv_path, sep=CSV_SEP, encoding="utf-8-sig")


def generate_schema_module_from_csv_dir(
    schema_dir: str | Path,
    output_py_path: str | Path,
    version: str | None = None,
) -> Path:
    schema_dir = Path(schema_dir)
    output_py_path = Path(output_py_path)

    df_in = read_schema_csv(schema_dir / "IN.csv")
    df_out = read_schema_csv(schema_dir / "OUT.csv")

    if version is None:
        version = schema_dir.name

    code = generate_schema_module_text(df_in=df_in, df_out=df_out, version=version)

    output_py_path.parent.mkdir(parents=True, exist_ok=True)
    output_py_path.write_text(code, encoding="utf-8")
    return output_py_path


def generate_schema_module_from_excel(
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
    version = "v1_11_4"
    generate_schema_module_from_csv_dir(
        schema_dir=f"data/schemas/{version}",
        output_py_path=f"src/pexl/schema/generated/excel_{version}.py",
        version=version,
    )