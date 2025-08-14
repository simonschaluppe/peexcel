from pathlib import Path
DATA_PATH       = Path("../data/")
EMA_PATH        = Path("../data/Energiemosaik_Datenpaket_AT/")
EMA_EXCEL_PATH  = Path(EMA_PATH, "0_AT_Energiemosaik.xlsx")

def read_project(file):
    """reads a Export.xlsx, returns a _suitable data structure"""
    # maybe json?
    # each sheet is a section,
    # each in row the base column part is a parameter description
    # each project gets its own json branch "scenario" with all rows and their values
    # key is 


class Project():
    """holds a Export.xslx info
    """
    ## read a project
    # hold the json as dataclass?
    
    # game app needs to come here, get a project 
    # and build a district out of it#
    # projectattributes need to findable
    # project is not responsible for ensuring compatability?
    
    # project will also be used for other tasks
        # formula annotation
        # visualization of calculatio graph, network 
            # potentially interactive?
            
    # should it automatically be like the excel?
    # yes, that means dynamic