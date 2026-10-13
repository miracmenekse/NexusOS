#!/bin/bash
# Tüm demolar tek komutla. Ctrl+C hepsini durdurur.
#   http://localhost:4400/sehir  Ç1 Neon kod şehri (canlı)
#   http://localhost:4400        Ç2 servis trafiği (canlı)
#   http://localhost:4500/agents/ofis2.html, /agents/ag.html   Ç3 agent örnekleri
#   http://localhost:4500/arayuz-secenekleri/                  ses/dokunma taslakları
#   http://localhost:4500/agents/ofis2.html?canli=/canli/oturum.json   şu an çalışan Claude Code oturumu, canlı
#   ?data=telekom-takilma.json | telekom-kayip.json | otel.json        takılma, kayıp ve OpenTelemetry örnekleri
cd "$(dirname "$0")"
: > services/events.jsonl   # ponytail: her başlatmada sıfırlanır; uzun koşuda büyür, gerekirse load.py'ye döndürme ekle
trap 'kill $(jobs -p) 2>/dev/null' EXIT
for s in payments inventory orders gateway; do (cd services && exec python3 $s/app.py) & done
sleep 1
python3 traffic/load.py &
python3 agents/canli.py &   # demo/ statik + /canli/oturum.json (çalışan Claude Code oturumu)
python3 traffic/server.py
