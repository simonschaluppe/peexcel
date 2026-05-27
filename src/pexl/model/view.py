


from pexl.schema.current import VariableMeta
from .scenario import Scenario


class VariableSelection:
    def __init__(
        self,
        variables: list[VariableMeta],
        scenarios: list[Scenario],
    ):
        self._vars = variables
        self.scenarios = scenarios

    @property
    def values(self) -> list[list[object]]:
        return [
            [getattr(s.v, meta.attr_name) for s in self.scenarios]
            for meta in self._vars
        ]
    
    def to_records(self):
        for var in self._vars:
            row = {
                "var_name": var.var_name,
                "label_de": var.label_de,
                "unit": var.unit,
                "domain": var.domain,
                "measure": var.measure,
                "entity_group": var.entity_group,
                "entity_key": var.entity_key,
            }
            for scenario in self.scenarios:
                row[scenario.name] = getattr(scenario.v, var.attr_name)
            yield row 

            