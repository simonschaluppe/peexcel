from pathlib import Path
from pexl.batch import run_batch, inspect_batch

workbook = Path(r"excel\development\ka_PEQ_Nachweistool_DEV.xlsb")

scenarios = inspect_batch(
    workbook,
    scenario_filter={"Base Scenario": "Default"},
).head(10)

result = run_batch(
    workbook,
    scenarios=scenarios,
    base_reload="always",
    batch_size=25,
    export_annual=True,
    export_timeseries=False,
    output_dir="first_10",  # separate folder from the full batch
    overwrite=True,
    resume=False,
)