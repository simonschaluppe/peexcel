from dataclasses import dataclass




@dataclass(frozen=True)
class SeriesSpec:
    var_name: str
    label_de: str | None = None
    role: str | None = None
    order: int = 0
    color: str | None = None
    pattern: str | None = None


@dataclass(frozen=True)
class ChartSpec:
    chart_name: str
    tab_name: str | None
    title: str
    chart_type: str
    series: tuple[SeriesSpec, ...]