#!/bin/bash
# ARŞİV (d18: Ç1 Neon). Start the 4 demo services, send some orders, rebuild ExplorViz data. Usage: bash run.sh [orders]
cd "$(dirname "$0")/../../services"
rm -f events.jsonl
for s in payments inventory orders gateway; do python3 $s/app.py & done
trap 'kill $(jobs -p) 2>/dev/null' EXIT
sleep 1
for i in $(seq 1 "${1:-30}"); do
  item=$(shuf -n1 -e book pen lamp); qty=$(shuf -n1 -i 1-5)
  curl -s -X POST localhost:8101/checkout -d "{\"item\":\"$item\",\"qty\":$qty}" > /dev/null
done
curl -s localhost:8101/status; echo
cd .. && python3 analyze.py
