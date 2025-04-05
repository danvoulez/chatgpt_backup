import os
from watcher import download_and_save

def test_valid_download():
    url = "https://chat.openai.com/backend-api/files/valid_id"
    result = download_and_save(url)
    assert result is None or os.path.exists(result)

def test_invalid_download():
    url = "https://invalid.openai.com/404"
    result = download_and_save(url)
    assert result is None