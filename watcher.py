import time

def start_watcher():
    print("🟢 Watcher iniciado e rodando 24h por dia.")
    while True:
        # Simulação de monitoramento contínuo
        print("🔍 Verificando novos links...")
        time.sleep(60)

if __name__ == "__main__":
    start_watcher()