"""Tiny stdlib HTTP helpers shared by the demo services; every call is logged for the dynamic view."""
import json, os, sys, threading, time, traceback, urllib.request, uuid
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

EVENTS = os.path.join(os.path.dirname(__file__), "..", "events.jsonl")


def log_event(**e):
    with open(EVENTS, "a") as f:
        f.write(json.dumps({"t": time.time_ns(), **e}) + "\n")


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_iz = threading.local()   # trace id of the request this thread is serving; outgoing calls carry it on


def _where(filename, line):
    return os.path.relpath(filename, ROOT) + ":" + str(line)


def fail(reason, **info):
    """A handler's failure answer; `at` is the file:line that returned it, so the city can point at it."""
    f = sys._getframe(1)
    return {"ok": False, "reason": reason, "at": _where(f.f_code.co_filename, f.f_lineno), **info}


def call(method, url, body=None, caller=""):
    start, iz = time.time_ns(), getattr(_iz, "id", None) or uuid.uuid4().hex[:12]   # no request in hand: a new trace starts
    req = urllib.request.Request(url, data=json.dumps(body or {}).encode(), method=method,
                                 headers={"Content-Type": "application/json", "X-Iz": iz})
    try:
        with urllib.request.urlopen(req, timeout=5) as r:
            out = json.loads(r.read() or b"{}")
            ok = out.get("ok", True) is not False
    except Exception as ex:
        out, ok = {"error": str(ex)}, False
    log_event(caller=caller, method=method, url=url, ok=ok, ns=time.time_ns() - start, iz=iz,
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
            _iz.id = self.headers.get("X-Iz")
            try:
                out = fn(body)
            except Exception as ex:   # crash: point at the deepest line inside the services
                tb = [t for t in traceback.extract_tb(ex.__traceback__) if t.filename.startswith(ROOT)]
                out = {"ok": False, "reason": f"{type(ex).__name__}: {ex}", "at": _where(tb[-1].filename, tb[-1].lineno)}
            data = json.dumps(out).encode()
            self.send_response(200); self.send_header("Content-Type", "application/json"); self.end_headers()
            self.wfile.write(data)

        def do_GET(self): self._handle("GET")
        def do_POST(self): self._handle("POST")
        def log_message(self, *a): pass

    ThreadingHTTPServer(("127.0.0.1", port), H).serve_forever()
