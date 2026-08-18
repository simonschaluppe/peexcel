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

ENERGY_INPUT_ENVIRONMENT = SankeyNode(
    id="energy_input_environment",
    label=LocalizedText(
        de="Umweltwärme",
        en="Environmental heat",
    ),
)

ENERGY_INPUT_WASTEHEAT = SankeyNode(
    id="energy_input_wasteheat",
    label=LocalizedText(
        de="Abwärme",
        en="Waste heat",
    ),
)


HEATING_SYSTEM_1 = SankeyNode(
    id="heating_system_1",
    label=LocalizedText(
        de="Heizsystem 1",
        en="Heating system 1",
    ),
)

HEATING_SYSTEM_2 = SankeyNode(
    id="heating_system_2",
    label=LocalizedText(
        de="Heizsystem 2",
        en="Heating system 2",
    ),
)

HEATING_SYSTEM_3 = SankeyNode(
    id="heating_system_3",
    label=LocalizedText(
        de="Heizsystem 3",
        en="Heating system 3",
    ),
)

HEATING_SYSTEM_4 = SankeyNode(
    id="heating_system_4",
    label=LocalizedText(
        de="Heizsystem 4",
        en="Heating system 4",
    ),
)


HEAT_DISTRIBUTION = SankeyNode(
    id="heat_distribution",
    label=LocalizedText(
        de="Wärmeverteilung",
        en="Heat distribution",
    ),
)

HEAT_USE = SankeyNode(
    id="heat_use",
    label=LocalizedText(
        de="Raumwärme",
        en="Space heating",
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

HEATING_SYSTEM = SankeySpec(
    name="heating_system",
    title=LocalizedText(
        de="Heizsystem",
        en="Space heating system",
    ),
    flows=(

        # ------------------------------------------------------------------
        # Heating system 1: electrical / heat pump
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=HEATING_SYSTEM_1,
            variable=v.Eh_1el,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),

        SankeyFlow(
            source=ENERGY_INPUT_ENVIRONMENT,
            target=HEATING_SYSTEM_1,
            variable=v.Qenv_h_1el,
            flow_type=SankeyFlowType.ENVIRONMENTAL_HEAT,
        ),

        SankeyFlow(
            source=HEATING_SYSTEM_1,
            target=HEAT_DISTRIBUTION,
            variable=v.Qheb_1el,
            flow_type=SankeyFlowType.USEFUL_HEAT,
        ),


        # ------------------------------------------------------------------
        # Heating system 2: thermal
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_THERMAL,
            target=HEATING_SYSTEM_2,
            variable=v.EUIh_2th,
            flow_type=SankeyFlowType.THERMAL,
        ),

        SankeyFlow(
            source=HEATING_SYSTEM_2,
            target=HEAT_DISTRIBUTION,
            variable=v.Qheb_2th,
            flow_type=SankeyFlowType.USEFUL_HEAT,
        ),

        SankeyFlow(
            source=HEATING_SYSTEM_2,
            target=GENERATION_LOSSES,
            variable=v.Qloss_h_th2_generation,
            flow_type=SankeyFlowType.LOSS,
        ),


        # ------------------------------------------------------------------
        # Heating system 3: electrical / heat pump
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=HEATING_SYSTEM_3,
            variable=v.Eh_3el,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),

        SankeyFlow(
            source=ENERGY_INPUT_ENVIRONMENT,
            target=HEATING_SYSTEM_3,
            variable=v.Qenv_h_3el,
            flow_type=SankeyFlowType.ENVIRONMENTAL_HEAT,
        ),

        SankeyFlow(
            source=HEATING_SYSTEM_3,
            target=HEAT_DISTRIBUTION,
            variable=v.Qheb_3el,
            flow_type=SankeyFlowType.USEFUL_HEAT,
        ),


        # ------------------------------------------------------------------
        # Heating system 4: thermal
        # ------------------------------------------------------------------

        SankeyFlow(
            source=ENERGY_INPUT_THERMAL,
            target=HEATING_SYSTEM_4,
            variable=v.EUIh_4th,
            flow_type=SankeyFlowType.THERMAL,
        ),

        SankeyFlow(
            source=HEATING_SYSTEM_4,
            target=HEAT_DISTRIBUTION,
            variable=v.Qheb_4th,    
            flow_type=SankeyFlowType.USEFUL_HEAT,
        ),

        SankeyFlow(
            source=HEATING_SYSTEM_4,
            target=GENERATION_LOSSES,
            variable=v.Qloss_h_th4_generation, 
            flow_type=SankeyFlowType.LOSS,
        ),


        # ------------------------------------------------------------------
        # Distribution
        # ------------------------------------------------------------------


        SankeyFlow(
            source=ENERGY_INPUT_WASTEHEAT,
            target=HEAT_DISTRIBUTION,
            variable=v.Qh_min_wasteheat,   
            flow_type=SankeyFlowType.ENVIRONMENTAL_HEAT,
        ),       
        SankeyFlow(
            source=ENERGY_INPUT_WASTEHEAT,
            target=HEAT_DISTRIBUTION,
            variable=v.Qh_flex_wasteheat,   
            flow_type=SankeyFlowType.ENVIRONMENTAL_HEAT,
        ),

        SankeyFlow(
            source=HEAT_DISTRIBUTION,
            target=HEAT_USE,
            variable=v.QH,   
            flow_type=SankeyFlowType.USEFUL_HEAT,
        ),

        SankeyFlow(
            source=HEAT_DISTRIBUTION,
            target=DISTRIBUTION_LOSSES,
            variable=v.Qh_distr_losses,  # looks clear in sketch
            flow_type=SankeyFlowType.LOSS,
        ),
            SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=HEAT_DISTRIBUTION,
            variable=v.EUIh_el_aux,  # looks clear in sketch
            flow_type=SankeyFlowType.ELECTRICITY,
        ),
    ),
)