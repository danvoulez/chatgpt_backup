import os
import requests
import time
import logging

LINKS = [
    "https://chat.openai.com/backend-api/files/primary_link_id",
    "https://chat.openai.com/backend-api/files/fallback_link_id"
]

SAVE_DIR = "downloads"
RETRY_DELAY = 60
LOG_FILE = os.path.join(SAVE_DIR, "watcher.log")
os.makedirs(SAVE_DIR, exist_ok=True)

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def download_and_save(link):
    try:
        response = requests.get(link, timeout=15)
        if response.status_code == 200:
            filename = link.split("/")[-1]
            filepath = os.path.join(SAVE_DIR, filename)
            with open(filepath, "wb") as f:
                f.write(response.content)
            logging.info(f"Downloaded successfully: {link}")
            return filepath
        else:
            logging.warning(f"Failed to download (status {response.status_code}): {link}")
            return None
    except Exception as e:
        logging.error(f"Error downloading {link}: {e}")
        return None

def run_watcher():
    while True:
        saved_files = []
        for link in LINKS:
            result = download_and_save(link)
            if result:
                saved_files.append(result)

        if not saved_files:
            logging.error("No files downloaded. Sending alert message...")

        time.sleep(RETRY_DELAY)

if __name__ == "__main__":
    run_watcher()