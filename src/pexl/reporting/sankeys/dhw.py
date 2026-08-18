from pexl.i18n import LocalizedText
from pexl.reporting.sankey import SankeyFlow, SankeyFlowType, SankeyNode, SankeySpec
from pexl.schema.current import SCHEMA_META as v


# Nodes ------------------------------------------------------------------------

ENERGY_INPUT_THERMAL = SankeyNode(
    id="ENERGY_INPUT_THERMAL",
    label=LocalizedText(
        de="Thermische Energie",
        en="Thermal energy input",
    ),
)

ENERGY_INPUT_ELECTRICAL = SankeyNode(
    id="ENERGY_INPUT_ELECTRICAL",
    label=LocalizedText(
        de="Stromzufuhr",
        en="Electricity input",
    ),
)

ENERGY_INPUT_ENVIRONMENT = SankeyNode(
    id="ENERGY_INPUT_ENVIRONMENT",
    label=LocalizedText(
        de="Umweltwärme",
        en="Environmental energy input",
    ),
)

DHW_SYSTEM_1 = SankeyNode(
    id="dhw_system_1",
    label=LocalizedText(
        de="WW-System 1",
        en="DHW system 1",
    ),
)

DHW_SYSTEM_2 = SankeyNode(
    id="dhw_system_2",
    label=LocalizedText(
        de="WW-System 2",
        en="DHW system 2",
    ),
)

DHW_STORAGE_1 = SankeyNode(
    id="dhw_storage_1",
    label=LocalizedText(
        de="WW-Speicher 1",
        en="DHW storage 1",
    ),
)

DHW_STORAGE_2 = SankeyNode(
    id="dhw_storage_2",
    label=LocalizedText(
        de="WW-Speicher 2",
        en="DHW storage 2",
    ),
)

DHW_DISTRIBUTION = SankeyNode(
    id="dhw_distribution",
    label=LocalizedText(
        de="WW-Verteilung",
        en="DHW distribution",
    ),
)

DHW_USAGE = SankeyNode(
    id="dhw_usage",
    label=LocalizedText(
        de="Warmwasser-Nutzung",
        en="DHW use",
    ),
)

GENERATION_LOSSES = SankeyNode(
    id="generation_losses",
    label=LocalizedText(
        de="Erzeugungsverluste",
        en="Generation losses",
    ),
)

STORAGE_LOSSES = SankeyNode(
    id="storage_losses",
    label=LocalizedText(
        de="Speicherverluste",
        en="Storage losses",
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

DHW_SYSTEM = SankeySpec(
    name="dhw",
    title=LocalizedText(
        de="Warmwasser",
        en="Domestic hot water",
    ),
    flows=(
        # Energy input -> generation
        SankeyFlow(
            source=ENERGY_INPUT_THERMAL,
            target=DHW_SYSTEM_1,
            variable=v.EUIdhw_1th, 
            flow_type=SankeyFlowType.THERMAL
        ),

        SankeyFlow(
            source=ENERGY_INPUT_THERMAL,
            target=DHW_SYSTEM_2,
            variable=v.EUIdhw_2th, 
            flow_type=SankeyFlowType.THERMAL
        ),
        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=DHW_SYSTEM_1,
            variable=v.EUIdhw_1el,  
            flow_type=SankeyFlowType.ELECTRICITY
        ),
        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=DHW_SYSTEM_2,
            variable=v.EUIdhw_2el,  
            flow_type=SankeyFlowType.ELECTRICITY
        ),
        SankeyFlow(
            source=ENERGY_INPUT_ENVIRONMENT,
            target=DHW_SYSTEM_1,
            variable=v.Qenv_dhw_1,  
            flow_type=SankeyFlowType.ENVIRONMENTAL_HEAT
        ),
        SankeyFlow(
            source=ENERGY_INPUT_ENVIRONMENT,
            target=DHW_SYSTEM_2,
            variable=v.Qenv_dhw_2,  
            flow_type=SankeyFlowType.ENVIRONMENTAL_HEAT
        ),

        # Generation -> storage
        SankeyFlow(
            source=DHW_SYSTEM_1,
            target=DHW_STORAGE_1,
            variable=v.Qdhw_1_total, 
            flow_type=SankeyFlowType.THERMAL
        ),
        SankeyFlow(
            source=DHW_SYSTEM_2,
            target=DHW_STORAGE_2,
            variable=v.Qdhw_2_total, 
            flow_type=SankeyFlowType.THERMAL
        ),

        # Generation losses
        SankeyFlow(
            source=DHW_SYSTEM_1,
            target=GENERATION_LOSSES,
            variable=v.Qdhw_1_generation_losses,
            flow_type=SankeyFlowType.LOSS
        ),
        SankeyFlow(
            source=DHW_SYSTEM_2,
            target=GENERATION_LOSSES,
            variable=v.Qdhw_2_generation_losses,
            flow_type=SankeyFlowType.LOSS
        ),

        # Storage -> distribution
        SankeyFlow(
            source=DHW_STORAGE_1,
            target=DHW_DISTRIBUTION,
            variable=v.Qdhw_1_drawoff,      
            flow_type=SankeyFlowType.THERMAL
        ),
        SankeyFlow(
            source=DHW_STORAGE_2,
            target=DHW_DISTRIBUTION,
            variable=v.Qdhw_2_drawoff, 
            flow_type=SankeyFlowType.THERMAL
        ),

        # Storage losses
        SankeyFlow(
            source=DHW_STORAGE_1,
            target=STORAGE_LOSSES,
            variable=v.Qdhw_1_storage_losses,  
            flow_type=SankeyFlowType.LOSS
        ),
        SankeyFlow(
            source=DHW_STORAGE_2,
            target=STORAGE_LOSSES,
            variable=v.Qdhw_2_storage_losses,  
            flow_type=SankeyFlowType.LOSS
        ),

        # Distribution -> use
        SankeyFlow(
            source=DHW_DISTRIBUTION,
            target=DHW_USAGE,
            variable=v.Qdhw_1_tap,  
            flow_type=SankeyFlowType.USEFUL_HEAT
        ),        
        SankeyFlow(
            source=DHW_DISTRIBUTION,
            target=DHW_USAGE,
            variable=v.Qdhw_2_tap, 
            flow_type=SankeyFlowType.USEFUL_HEAT
        ),

        # Distribution losses
        SankeyFlow(
            source=DHW_DISTRIBUTION,
            target=DISTRIBUTION_LOSSES,
            variable=v.Qdhw_1_distr_losses, 
            flow_type=SankeyFlowType.LOSS
        ),       
        SankeyFlow(
            source=DHW_DISTRIBUTION,
            target=DISTRIBUTION_LOSSES,
            variable=v.Qdhw_2_distr_losses, 
            flow_type=SankeyFlowType.LOSS
        ),
        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=DHW_DISTRIBUTION,
            variable=v.Edhw_1_aux_el,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),        
        SankeyFlow(
            source=ENERGY_INPUT_ELECTRICAL,
            target=DHW_DISTRIBUTION,
            variable=v.Edhw_2_aux_el,
            flow_type=SankeyFlowType.ELECTRICITY,
        ),

    ),
)