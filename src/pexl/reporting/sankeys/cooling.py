from pexl.i18n import LocalizedText
from pexl.reporting.sankey import (
    SankeyFlow,
    SankeyFlowType,
    SankeyNode,
    SankeySpec,
)
from pexl.schema.current import SCHEMA_META as v


# Nodes ------------------------------------------------------------------------

ENERGY_INPUT_ELECTRICAL = SankeyNode(
    id="energy_input_electrical",
    label=LocalizedText(
        de="Stromzufuhr",
        en="Electricity",
    ),
)

ENERGY_INPUT_THERMAL = SankeyNode(
    id="energy_input_thermal",
    label=LocalizedText(
        de="Thermische Energie",
        en="Thermal energy",
    ),
)

ENVIRONMENT = SankeyNode(
    id="environment",
    label=LocalizedText(
        de="Umwelt",
        en="Environment",
    ),
)

COOLING_SYSTEM_1 = SankeyNode(
    id="cooling_system_1",
    label=LocalizedText(
        de="Kühlsystem 1 (elektrisch)",
        en="Cooling system 1",
    ),
)

COOLING_SYSTEM_2 = SankeyNode(
    id="cooling_system_2",
    label=LocalizedText(
        de="Kühlsystem 2 (thermisch)",
        en="Cooling system 2",
    ),
)

COOLING_SYSTEM_3 = SankeyNode(
    id="cooling_system_3",
    label=LocalizedText(
        de="Kühlsystem 3 (elektrisch)",
        en="Cooling system 3",
    ),
)

FREE_COOLING = SankeyNode(
    id="free_cooling",
    label=LocalizedText(
        de="Free Cooling",
        en="Free cooling",
    ),
)

COOLING_DISTRIBUTION = SankeyNode(
    id="cooling_distribution",
    label=LocalizedText(
        de="Kälteverteilung",
        en="Cooling distribution",
    ),
)

COOLING_USE = SankeyNode(
    id="cooling_use",
    label=LocalizedText(
        de="Raumkühlung",
        en="Space cooling",
    ),
)

GENERATION_LOSSES = SankeyNode(
    id="generation_losses",
    label=LocalizedText(
        de="Erzeugungsverluste",
        en="Generation losses",
    ),
)

DISTRIBUTION_LOSSES = SankeyNode(
    id="distribution_losses",
    label=LocalizedText(
        de="Verteilverluste",
        en="Distribution losses",
    ),
)


# Sankey -----------------------------------------------------------------------

COOLING_SYSTEM = SankeySpec(
    name="cooling_system",
    title=LocalizedText(
        de="Kühlsystem",
        en="Space cooling system",
    ),
    flows=(

        # ------------------------------------------------------------------
        # Cooling system 1: electrical
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=COOLING_SYSTEM_1,
            variable=v.Ec_1el,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),

        SankeyFlow(
            target=COOLING_SYSTEM_1,
            source=COOLING_DISTRIBUTION,
            variable=v.Qced_1el,
            flow_type=SankeyFlowType.USEFUL_COLD,
        ),

        # Heat rejected to environment
        SankeyFlow(
            source=COOLING_SYSTEM_1,
            target=ENVIRONMENT,
            variable=v.Qenv_c_1el,  
            flow_type=SankeyFlowType.ENVIRONMENTAL_COLD,
        ),


        # ------------------------------------------------------------------
        # Cooling system 2: thermal
        # ------------------------------------------------------------------

        SankeyFlow(
            source=COOLING_SYSTEM_2,
            target=ENERGY_INPUT_THERMAL,
            variable=v.EUIc_2th,
            flow_type=SankeyFlowType.THERMAL,
        ),

        SankeyFlow(
            source=COOLING_DISTRIBUTION,
            target=COOLING_SYSTEM_2,
            variable=v.Qced_2th,
            flow_type=SankeyFlowType.USEFUL_COLD,
        ),

        SankeyFlow(
            source=COOLING_SYSTEM_2,
            target=GENERATION_LOSSES,
            variable=v.Qloss_c_th2_generation, 
            flow_type=SankeyFlowType.LOSS,
        ),


        # ------------------------------------------------------------------
        # Cooling system 3: electrical
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=COOLING_SYSTEM_3,
            variable=v.Ec_3el,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),

        SankeyFlow(
            target=COOLING_SYSTEM_3,
            source=COOLING_DISTRIBUTION,
            variable=v.Qced_3el,
            flow_type=SankeyFlowType.USEFUL_COLD,
        ),

        # Heat rejected to environment
        SankeyFlow(
            source=COOLING_SYSTEM_3,
            target=ENVIRONMENT,
            variable=v.Qenv_c_3el,  
            flow_type=SankeyFlowType.ENVIRONMENTAL_COLD,
        ),


        # ------------------------------------------------------------------
        # Free cooling
        # ------------------------------------------------------------------

        SankeyFlow(
            source=COOLING_DISTRIBUTION,
            target=ENVIRONMENT,
            variable=v.Qc_min_0fc,  
            flow_type=SankeyFlowType.ENVIRONMENTAL_COLD,
        ),


        # ------------------------------------------------------------------
        # Auxiliary electrical cooling
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=COOLING_DISTRIBUTION,
            variable=v.EUIc_el_aux,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),


        # ------------------------------------------------------------------
        # Distribution
        # ------------------------------------------------------------------

        SankeyFlow(
            source=COOLING_USE,
            target=COOLING_DISTRIBUTION,
            variable=v.QC, 
            flow_type=SankeyFlowType.USEFUL_COLD,
        ),

        SankeyFlow(
            source=DISTRIBUTION_LOSSES,
            target=COOLING_DISTRIBUTION,
            variable=v.Qc_distr_losses,
            flow_type=SankeyFlowType.LOSS,
        ),
    ),
)