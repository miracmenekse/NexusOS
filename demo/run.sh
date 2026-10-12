#!/bin/bash
# Tüm demolar tek komutla. Ctrl+C hepsini durdurur.
#   http://localhost:4400/sehir  Ç1 Neon kod şehri (canlı)
#   http://localhost:4400        Ç2 servis trafiği (canlı)
#   http://localhost:4500/agents/ofis2.html, /agents/ag.html   Ç3 agent örnekleri
#   http://localhost:4500/arayuz-secenekleri/                  ses/dokunma taslakları
#   http://localhost:4500/agents/ofis2.html?data=oturum.json   aynı görünümler, Claude Code oturumu (üret: python3 agents/altlik.py)
cd "$(dirname "$0")"
: > services/events.jsonl   # ponytail: her başlatmada sıfırlanır; uzun koşuda büyür, gerekirse load.py'ye döndürme ekle
trap 'kill $(jobs -p) 2>/dev/null' EXIT
for s in payments inventory orders gateway; do (cd services && exec python3 $s/app.py) & done
sleep 1
python3 traffic/load.py &
python3 -m http.server 4500 --bind 127.0.0.1 >/dev/null 2>&1 &
python3 traffic/server.py
