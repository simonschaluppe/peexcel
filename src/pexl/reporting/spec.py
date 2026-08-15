from dataclasses import dataclass


@dataclass(frozen=True)
class ChartSpec:
    chart_id: str
    title: str
    tab_name: str | None
    kind: str
    series: tuple["SeriesSpec", ...]

@dataclass(frozen=True)
class SeriesSpec:
    var_name: str
    label_de: str | None
    role: str | None
    color: str | None
    pattern: str | None