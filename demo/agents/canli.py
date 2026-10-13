"""Ç3 canlı izleme (G3): demo/ klasörünü sunar ve çalışan Claude Code oturumunu modele çevirip verir.

    python3 agents/canli.py          -> http://127.0.0.1:4500  (run.sh bunu başlatır)
    /canli/oturum.json               -> en yeni oturum, altlik modeli (dosya değişmedikçe önbellekten)
    /canli/oturum.json?s=<oturum-id> -> belirli bir oturum
Görünümde: agents/ofis2.html?canli=/canli/oturum.json, agents/ag.html?canli=/canli/oturum.json
"""
import glob, json, os, sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse, parse_qs

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import altlik, build

_cache = {}


def oturum(sid=None):
    if sid:
        path = os.path.join(build.PROJ, os.path.basename(sid) + ".jsonl")
    else:
        path = max(glob.glob(build.PROJ + "/*.jsonl"), key=os.path.getmtime)
    sub = path[:-6] + "/subagents"
    imza = (path, os.path.getsize(path), os.path.getmtime(path),
            sum(os.path.getsize(f) for f in glob.glob(sub + "/*.jsonl")))
    if imza not in _cache:
        _cache.clear()
        m = altlik.claude_code(path)
        m["title"] = "Canlı · Claude Code oturumu " + os.path.basename(path)[:8]
        _cache[imza] = json.dumps(m, ensure_ascii=False).encode()
    return _cache[imza]


class H(SimpleHTTPRequestHandler):
    def do_GET(self):
        u = urlparse(self.path)
        if u.path != "/canli/oturum.json":
            return super().do_GET()
        try:
            body, code = oturum(parse_qs(u.query).get("s", [None])[0]), 200
        except (FileNotFoundError, ValueError, AssertionError) as ex:
            body, code = json.dumps({"hata": str(ex)}).encode(), 404
        self.send_response(code)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Access-Control-Allow-Origin", "*")   # Neon şehir (:4400) agent dokunuşlarını buradan okur
        self.end_headers(); self.wfile.write(body)

    def log_message(self, *a): pass


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 4500
    ThreadingHTTPServer(("127.0.0.1", port), partial(H, directory=os.path.dirname(HERE))).serve_forever()
