# login to nextcloud

import urllib.parse
import requests

FHTW_NEXTCLOUD_URL = "https://cloud.technikum-wien.at/remote.php/dav/files"


def get(file_path):
    parsed_file = urllib.parse.quote(f"{file_path}", )
    user = input("user: ")
    pw = input("pw: ")
    response = requests.request(
        method="GET",
        url=f"{FHTW_NEXTCLOUD_URL}/{user}/{parsed_file}",
        auth=(user, pw)
    )
    return response.content


if __name__ == "__main__":
    import pandas as pd

    file_path = "EE/6_Daten/Energie Österreich/Energiebilanzen_AT_1970-2020_Statistik_Austria.xlsx"
    file = get(file_path)
    df = pd.read_excel(file, sheet_name="Sektoraler Endverbrauch TJ")
    print(df.head())
