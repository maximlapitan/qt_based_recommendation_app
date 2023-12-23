# This Python file uses the following encoding: utf-8

import os
import requests
import zipfile
from tqdm import tqdm


def check_and_download_folder_contents(folder_path, download_url):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    if not os.listdir(folder_path):
        download_folder_contents(folder_path, download_url)
    else:
        print("Folder already has contents.")


def download_folder_contents(folder_path, download_url):
    response = requests.get(download_url, stream=True)

    if response.status_code == 200:
        # Save the archive
        archive_path = os.path.join(folder_path, 'archive.zip')
        total_size = int(response.headers.get('content-length', 0))
        block_size = 1024  # 1 Kibibyte

        print(f"Downloading: {download_url}")
        with open(archive_path, 'wb') as archive_file, tqdm(
            desc="Progress",
            total=total_size,
            unit='B',
            unit_scale=True,
            unit_divisor=1024,
        ) as progress_bar:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                archive_file.write(data)

        print("\nArchive downloaded successfully.")

        extract_folder_contents(folder_path, archive_path)
    else:
        print(
            f"Failed to download archive. Status code: {response.status_code}")


def extract_folder_contents(folder_path, archive_path):
    # Extract the contents of the archive into the target folder
    with zipfile.ZipFile(archive_path, 'r') as zip_ref:
        zip_ref.extractall(folder_path)

    # Move the extracted files to the target folder
    extracted_folder = os.path.join(folder_path, zip_ref.namelist()[0])
    for item in os.listdir(extracted_folder):
        item_path = os.path.join(extracted_folder, item)
        new_item_path = os.path.join(folder_path, item)
        os.rename(item_path, new_item_path)

    # Remove the now-empty extracted folder
    os.rmdir(extracted_folder)

    print("Archive extracted successfully.")


# Example usage:
folder_path = 'weights_variables'
download_url = 'https://nextcloud.th-deg.de/s/AxST3iar5JDjyrf/download'
check_and_download_folder_contents(folder_path, download_url)
