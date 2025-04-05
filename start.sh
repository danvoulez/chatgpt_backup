#!/bin/bash
while true; do
  echo "🚀 Iniciando ghost_runner.py"
  python3 ghost_runner.py
  echo "⚠️ ghost_runner caiu. Reiniciando em 5 segundos..."
  sleep 5
done
