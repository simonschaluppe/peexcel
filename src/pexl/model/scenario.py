
from dataclasses import dataclass
from pexl.schema.current import ExcelNamedVariables, SCHEMA_META

@dataclass
class Usage:
    key: str
    NFA: float #m2 NFA
    NFA_to_GFA_ratio: float #m2 NFA
    room_height: float
    # add more usage-scoped variables over time
    density_NFApPers: float | None = None
    cool_share: float | None = None
    vent_scale: float | None = None
    vent_share_mechanical: float | None = None
    usage_concurrency_summer: float | None = None
    usage_concurrency_winter: float | None = None
    DHW_concurrency: float | None = None
    DHW_1_share: float | None = None
    DHW_demand_kWhm2: float | None = None
    DHW_occupancy: float | None = None
    plugloads_scale: float | None = None
    Ev_scale: float | None = None
    StatPAX_scale: float | None = None
    aux_el_demand: float | None = None
    fc: float | None = None
    illuminance_min: float | None = None


class Scenario:
    """
    Represents a single scenario within a district.

    A scenario contains:
    - `name`: Name of the Scenario
    - `v`: all excel "var_name" variable values (inputs + results)
    - `meta`: static metadata for each variable (units, names, etc.)

    Values are accessed via dot-notation:
        scenario.v.QH
        scenario.meta.QH.unit

    Scenarios are created from Excel columns and belong to exactly one District.
    Scenario is indirectly linked to district via scenario.v.project_name -> District name
    """
    def __init__(self, name: str):
        self.name = name
        self.v = ExcelNamedVariables()
        self.meta = SCHEMA_META
        # TODO: attach timestep data container here, e.g. self.sim = None

    def __repr__(self) -> str:
        return f"<Scenario {self.name!r}>"

    def as_dict(self) -> dict:
        """Flat dict of all v.* values"""
        return vars(self.v)

    @staticmethod
    def _get(d, key, default=0):
        val = d.get(key)
        return default if val is None else val

    @property
    def usage_keys(self) -> list[str]:
        return [
            "retailother",
            "retailfood",
            "schoolprim",
            "schoolsec",
            "office",
            "other",
            "residential",
        ]
    
    @property
    def usages(self) -> list[Usage]:
        d = self.as_dict()
        usages = []
        for k in self.usage_keys:
            area = self._get(d, f"NFA_{k}")
            if area <= 0:
                continue

            usages.append(
                Usage(
                    key=k,
                    NFA=area,
                    NFA_to_GFA_ratio= d.get(f"NFA_to_GFA_ratio{k}"), 
                    room_height=self._get(d, f"rh_{k}"),
                    density_NFApPers=self._get(d, f"density_NFApPers_{k}"),
                    cool_share = d.get(f"cool_share_{k}"),
                    vent_scale=d.get(f"vent_scale_{k}"),
                    vent_share_mechanical = d.get(f"vent_share_mechanical_{k}"),
                    usage_concurrency_summer=self._get(d, f"usage_concurrency_summer_{k}"),
                    usage_concurrency_winter=self._get(d, f"usage_concurrency_winter_{k}"),
                    DHW_concurrency=self._get(d, f"DHW_concurrency_{k}"),
                    DHW_1_share=d.get(f"DHW_1_share_{k}"),
                    DHW_demand_kWhm2=d.get(f"DHW_demand_kWhm2_{k}"),
                    DHW_occupancy=d.get(f"DHW_occupancy_{k}"),
                    Ev_scale = d.get(f"Ev_scale_{k}"),                 
                    StatPAX_scale = d.get(f"StatPAX_scale_{k}"),  
                    aux_el_demand = d.get(f"aux_el_demand_{k}"),  
                    fc = d.get(f"fc_{k}"),  
                    illuminance_min =  d.get(f"illuminance_min_{k}"), 
                    plugloads_scale=d.get(f"Plugloads_scale_{k}"),
                )
            )
        return usages
 
