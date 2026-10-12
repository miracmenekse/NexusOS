"""Tiny stdlib HTTP helpers shared by the demo services; every call is logged for the dynamic view."""
import json, os, time, urllib.request
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

EVENTS = os.path.join(os.path.dirname(__file__), "..", "events.jsonl")


def log_event(**e):
    with open(EVENTS, "a") as f:
        f.write(json.dumps({"t": time.time_ns(), **e}) + "\n")


def call(method, url, body=None, caller=""):
    start = time.time_ns()
    req = urllib.request.Request(url, data=json.dumps(body or {}).encode(), method=method,
                                 headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            out = json.loads(r.read() or b"{}")
            ok = out.get("ok", True) is not False
    except Exception as ex:
        out, ok = {"error": str(ex)}, False
    log_event(caller=caller, method=method, url=url, ok=ok, ns=time.time_ns() - start,
              detail=None if ok else out)
    return out


def serve(port, routes):
    """routes: {("POST", "/orders"): fn(body) -> dict}"""
    class H(BaseHTTPRequestHandler):
        def _handle(self, method):
            fn = routes.get((method, self.path))
            if not fn:
                self.send_response(404); self.end_headers(); return
            n = int(self.headers.get("Content-Length") or 0)
            body = json.loads(self.rfile.read(n) or b"{}")
            data = json.dumps(fn(body)).encode()
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
            self.wfile.write(data)

        def do_GET(self): self._handle("GET")
        def do_POST(self): self._handle("POST")
        def log_message(self, *a): pass

    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
