from pathlib import Path
from pexl.batch import run_batch

workbook = Path(
    r"excel\development\ka_PEQ_Nachweistool_DEV.xlsb"
)
output_dir = Path("data/building_typologies/")

result = run_batch(
    workbook,
    scenario_filter={"Base Scenario": "Default"},
    base_reload="first_only",
    batch_size=25,
    export_annual=True,
    export_timeseries=False,
    output_dir=output_dir,
    resume=True,
    overwrite=False,
)

print(f"Status: {result.status}")
print(f"Completed: {len(result.completed)}")
print(f"Failed: {result.failed}")
print(f"Results: {output_dir}")