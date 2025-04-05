import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

SESSION_TOKEN = os.getenv("SESSION_TOKEN")
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Cookie": f"__Secure-next-auth.session-token={SESSION_TOKEN}"
}

def session_is_valid():
    r = requests.get("https://chat.openai.com/api/auth/session", headers=HEADERS)
    return r.status_code == 200

def fetch_conversations():
    url = "https://chat.openai.com/backend-api/conversations?offset=0&limit=100"
    r = requests.get(url, headers=HEADERS)
    if r.status_code == 200:
        data = r.json()
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        fname = f"conversations_backup_{timestamp}.json"
        with open(fname, "w") as f:
            json.dump(data, f, indent=2)
        log(f"✅ Backup salvo: {fname}")
        return fname
    else:
        log(f"❌ Erro ao buscar conversas: {r.status_code}")
        return None

def log(message):
    with open("ghost.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {message}\n")
    print(message)
