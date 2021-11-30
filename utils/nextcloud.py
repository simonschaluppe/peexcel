# login to nextcloud
import getpass
import logging
import urllib.parse
from pathlib import Path

import requests


FHTW_NEXTCLOUD_URL = "https://cloud.technikum-wien.at/remote.php/dav/files"

LOCAL_NEXTCLOUD = [r"C:\Users\Simon Schneider\Nextcloud"]


def get(file_path, verbose=False, force=False):
    # try finding a local nextcloud
    if not force:
        for path in LOCAL_NEXTCLOUD:
            if Path(path).exists():
                local_path = Path(path, file_path)
                logging.info(f"{local_path=} found!")
                return local_path
    #only if not locally found, connect
    parsed_file = urllib.parse.quote(f"{file_path}", )
    user = input("user (FHTW): ")
    pw = getpass.getpass("pw (not shown, hit enter after typing): ")
    response = requests.request(
        method="GET",
        url=f"{FHTW_NEXTCLOUD_URL}/{user}/{parsed_file}",
        auth=(user, pw)
    )
    if verbose:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug(f"{parsed_file=}")
        logging.debug(f"{response=}")
        logging.debug(f"{response.content=}")
    return response.content


if __name__ == "__main__":
    import pandas as pd
    logging.basicConfig(level=logging.INFO)
    file_path = "EE/6_Daten/Energie Österreich/Energiebilanzen_AT_1970-2020_Statistik_Austria.xlsx"
    file = get(file_path)
    df = pd.read_excel(file, sheet_name="Sektoraler Endverbrauch TJ")
    print(df.head())
