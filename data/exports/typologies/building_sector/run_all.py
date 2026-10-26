from pathlib import Path

import pandas as pd
from pexl.batch import run_batch

HERE = Path(__file__).resolve().parent
REPO = next(p for p in HERE.parents if (p / "src" / "pexl").is_dir())

workbook = REPO / "excel/development/ka_PEQ_Nachweistool_DEV.xlsb"
output_dir = HERE

scenarios = pd.read_csv(
    HERE / "scenarios_5400_SCEN.csv",
    sep=";",
    encoding="utf-8-sig",
    dtype=str,
    keep_default_na=False,

)

result = run_batch(
    workbook,
    scenarios=scenarios,
    base_reload="first_only",
    batch_size=25,
    export_annual=True,
    export_timeseries=False,
    output_dir=output_dir,
    overwrite=False,
    resume=True

)

print(
    f"Status: {result.status}; "
    f"completed: {len(result.completed)}; "
    f"failed: {len(result.failed)}"
)