import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

def get_access_token():
    response = requests.post(
        "https://oauth2.googleapis.com/token",
        data={
            "client_id": os.getenv("GOOGLE_DRIVE_CLIENT_ID"),
            "client_secret": os.getenv("GOOGLE_DRIVE_CLIENT_SECRET"),
            "refresh_token": os.getenv("GOOGLE_DRIVE_REFRESH_TOKEN"),
            "grant_type": "refresh_token"
        }
    )
    return response.json().get("access_token")

def upload_to_drive(file_path: str, file_name: str = None):
    access_token = get_access_token()
    folder_id = os.getenv("GOOGLE_DRIVE_FOLDER_ID")
    file_name = file_name or os.path.basename(file_path)

    metadata = {
        "name": file_name,
        "parents": [folder_id]
    }

    files = {
        'data': ('metadata', json.dumps(metadata), 'application/json'),
        'file': open(file_path, "rb")
    }

    response = requests.post(
        "https://www.googleapis.com/upload/drive/v3/files?uploadType=multipart",
        headers={"Authorization": f"Bearer {access_token}"},
        files=files
    )

    if response.status_code == 200:
        print(f"✅ Upload feito: {file_name}")
    else:
        print(f"❌ Falha no upload: {response.text}")
