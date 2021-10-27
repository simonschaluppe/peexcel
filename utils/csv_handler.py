import os
from pathlib import Path
from typing import List

from .excel import PEExcel, Cell


def valid(directory):
    return True

def write_csv(path: Path, list_of_cells: List[Cell], meta_data):
    with open(path, mode="w") as f:
        m = [f"# {k}; {v}\n" for k, v in meta_data.items()]
        f.writelines(m)

        f.write(Cell.csv_header())
        f.write("\n")
        for v in list_of_cells:
            f.write(v.csv_line())
            f.write("\n")



def save_excel_data_to_dir(
        directory: Path,
        peexcel: PEExcel,
        overwrite=False
    ):
    if not valid(directory):
        raise RuntimeError("Directory not valid")

    if directory.is_dir() and not overwrite:
        raise RuntimeError(f"{directory=} ALREADY EXISTS!")

    if not directory.is_dir():
        os.makedirs(directory)

    write_csv(directory / "test_di.csv",
              list_of_cells=peexcel.inputs,
              meta_data=peexcel.info()
              )
    write_csv(directory / "test_results.csv",
              list_of_cells=peexcel.results,
              meta_data=peexcel.info()
              )


if __name__ == "__main__":
    # write_csv(Path("names.csv"), names, dict())
    pass