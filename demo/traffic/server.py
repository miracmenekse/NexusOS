"""Ç2 servis trafiği: serves index.html and streams services/events.jsonl as Server-Sent Events."""
import json, os, time
from urllib.parse import urlparse, parse_qs
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
EVENTS = os.path.join(HERE, "..", "services", "events.jsonl")
from yapi import yapi
YAPI = yapi()   # services, files, port -> service / handler file; /yapi re-reads the code on every request (K4)
PORTS, PORT_FILE = YAPI["port_svc"], YAPI["port_file"]


def to_edge(ev):
    port = int(ev["url"].split(":")[2].split("/")[0])
    src = ev["caller"].split("/")[0]
    return {"from": src, "to": PORTS.get(port, "?"), "ok": ev["ok"], "ms": ev["ns"] / 1e6,
            "fromFile": ev["caller"], "toFile": PORT_FILE.get(port), "at": (ev.get("detail") or {}).get("at"),
            "path": "/" + ev["url"].split("/", 3)[3], "detail": ev.get("detail"),
            "iz": ev.get("iz"), "bas": (ev["t"] - ev["ns"]) / 1e6}   # trace id + start (ms): the page rebuilds each request's path (K2)


ARIZA = os.path.join(HERE, "..", "services", "ariza.json")


class H(BaseHTTPRequestHandler):
    def do_POST(self):   # O6: {"svc": {"gecikme_ms": 0-5000, "hata": 0-1}}; {} clears every fault
        if self.path != "/ariza":
            self.send_response(404); self.end_headers(); return
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
            temiz = {s: {"gecikme_ms": max(0, min(5000, float(v.get("gecikme_ms", 0)))), "hata": max(0.0, min(1.0, float(v.get("hata", 0))))}
                     for s, v in body.items() if s in YAPI["port_svc"].values()}
        except (ValueError, AttributeError, TypeError):
            self.send_response(400); self.end_headers(); return
        json.dump(temiz, open(ARIZA, "w"))
        self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
        self.wfile.write(json.dumps(temiz).encode())

    def do_GET(self):
        if self.path.startswith("/kod?"):   # source of one service file, for the error view
            root = os.path.realpath(os.path.join(HERE, "..", "services"))
            f = os.path.realpath(os.path.join(root, parse_qs(urlparse(self.path).query).get("f", [""])[0]))
            ok = f.startswith(root + os.sep) and f.endswith(".py") and os.path.isfile(f)
            self.send_response(200 if ok else 404); self.send_header("Content-Type", "text/plain; charset=utf-8"); self.end_headers()
            self.wfile.write(open(f, "rb").read() if ok else b""); return
        if self.path == "/ariza":
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
            self.wfile.write(open(ARIZA, "rb").read() if os.path.exists(ARIZA) else b"{}"); return
        if self.path == "/yapi":
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
            self.wfile.write(json.dumps(yapi()).encode()); return
        if self.path != "/events":
            page = os.path.join(HERE, "..", "tasarim", "index.html") if self.path.startswith("/sehir") else os.path.join(HERE, "index.html")
            body = open(page, "rb").read()
            self.send_response(200); self.send_header("Content-Type", "text/html; charset=utf-8"); self.end_headers()
            self.wfile.write(body); return
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream"); self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        pos = os.path.getsize(EVENTS) if os.path.exists(EVENTS) else 0
        try:
            while True:
                if os.path.exists(EVENTS):
                    if os.path.getsize(EVENTS) < pos:
                        pos = 0  # run.sh truncated the log
                    with open(EVENTS) as f:
                        f.seek(pos)
                        for line in f:
                            if line.endswith("\n"):
                                self.wfile.write(f"data: {json.dumps(to_edge(json.loads(line)))}\n\n".encode())
                                pos += len(line.encode())
                    self.wfile.flush()
                time.sleep(0.1)
        except (BrokenPipeError, ConnectionResetError):
            pass

    def log_message(self, *a): pass


if __name__ == "__main__":
    print("Ç2 trafik: http://localhost:4400  ·  canlı şehir: http://localhost:4400/sehir")
    ThreadingHTTPServer(("127.0.0.1", 4400), H).serve_forever()
