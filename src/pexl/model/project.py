
from pathlib import Path
from typing import Iterator
from .district import District


class Project:
    """
    Top-level representation of a Project Excel file.

    A project consists of (1 to many) districts, each containing multiple scenarios.

    The project does NOT expose scenarios directly — they are always accessed
    through their district:

        project["District A"]["Base"]

    Attributes:
        file_source: path to the source Excel file
        districts: list of District objects
        warnings: list of import warnings (e.g. mismatches between column names
                  and values inside the Excel data)

    Access patterns:
        project["District A"]   -> district by name
        project[0]              -> district by index
        for d in project: ...   -> iterate districts
    """
    def __init__(self, file_source: str | Path | None = None):
        self.file_source = str(file_source) if file_source is not None else None
        self.districts: list[District] = []
        self._district_dict: dict[str, District] = {}
        self.warnings: list[str] = []

    def add_district(self, district: District) -> None:
        if district.name in self._district_dict:
            raise ValueError(f"Duplicate district name: {district.name!r}")
        self.districts.append(district)
        self._district_dict[district.name] = district

    def get_or_create_district(self, district_name: str) -> District:
        district = self._district_dict.get(district_name)
        if district is None:
            district = District(district_name)
            self.add_district(district)
        return district

    def __getitem__(self, key: str | int) -> District:
        if isinstance(key, str):
            return self._district_dict[key]
        if isinstance(key, int):
            return self.districts[key]
        raise TypeError(f"Unsupported district key type: {type(key)}")

    def __iter__(self) -> Iterator[District]:
        return iter(self.districts)

    def __len__(self) -> int:
        return len(self.districts)

    def get(self, name: str, default=None):
        return self._district_dict.get(name, default)

    def names(self) -> list[str]:
        return [d.name for d in self.districts]

    def __repr__(self) -> str:
        src = f" source={self.file_source!r}" if self.file_source else ""
        return f"<Project districts={len(self.districts)} warnings={len(self.warnings)}{src}>"
