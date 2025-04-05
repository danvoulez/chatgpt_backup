import time, traceback
from ghost_fetcher import fetch_conversations, session_is_valid
from drive_uploader import upload_to_drive
from datetime import datetime

def log(msg):
    with open("ghost.log", "a") as f:
        f.write(f"[{datetime.now().isoformat()}] {msg}\n")
    print(msg)

def ghost_loop():
    while True:
        try:
            log("👻 Iniciando ciclo do ghost...")
            if session_is_valid():
                log("🟢 Sessão válida.")
                filename = fetch_conversations()
                if filename:
                    upload_to_drive(filename)
            else:
                log("🔴 Sessão inválida. Verifique SESSION_TOKEN.")
        except Exception as e:
            log(f"💥 Erro crítico: {e}")
            log(traceback.format_exc())
        time.sleep(3600)  # espera 1 hora

if __name__ == "__main__":
    ghost_loop()
