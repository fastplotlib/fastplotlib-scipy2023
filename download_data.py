import os
import requests
from tqdm import tqdm
from pathlib import Path
from zipfile import ZipFile

# make data dir if not exists
data_dir = Path(os.path.dirname(os.path.abspath(__file__)), "fpl-scipy2023-data")
os.makedirs(data_dir, exist_ok=True)

data_file = Path(
    os.path.dirname(os.path.abspath(__file__)), "fpl-scipy2023-data.zip"
)


def download_data():

    # if data already exists, return
    if os.path.exists(data_dir) & len(list(data_dir.iterdir())) != 0:
        print("data already exists")
        return

    # else download
    print(f"Downloading data")
    url = f"https://zenodo.org/record/8140484/files/fpl-scipy2023-data.zip"

    # basically from https://stackoverflow.com/questions/37573483/progress-bar-while-download-file-over-http-with-requests/37573701
    response = requests.get(url, stream=True)
    total_size_in_bytes = int(response.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    progress_bar = tqdm(total=total_size_in_bytes, unit="iB", unit_scale=True)

    with open(data_file, "wb") as file:
        for data in response.iter_content(block_size):
            progress_bar.update(len(data))
            file.write(data)
    progress_bar.close()

    ZipFile(data_file).extractall(data_dir.parent)
