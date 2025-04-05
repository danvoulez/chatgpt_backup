#!/bin/bash
echo "Iniciando Watcher..."
python3 watcher.py

# Start the application
uvicorn main:app --host 0.0.0.0 --port 8080