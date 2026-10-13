"""Neon şehrin yapısı, doğrudan services/ kodundan (ast): servisler, dosyalar (satır sayısı), port → dosya, çağrılar.

    python3 traffic/yapi.py   -> yapıyı yazdırır ve kendini sınar
"""
import ast, json, os, sys

ROOT = os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "services"))


def _py(svc):
    for d, _, fs in os.walk(os.path.join(ROOT, svc)):
        for f in sorted(fs):
            p = os.path.join(d, f)
            if f.endswith(".py") and os.path.getsize(p):   # boş __init__.py bina değil
                yield os.path.relpath(p, ROOT)


def yapi():
    services, port_svc, port_file, calls = [], {}, {}, set()
    for svc in sorted(d for d in os.listdir(ROOT) if os.path.isfile(os.path.join(ROOT, d, "app.py"))):
        files = [{"file": f, "lines": sum(1 for l in open(os.path.join(ROOT, f)) if l.strip()),
                  "degisim": os.path.getmtime(os.path.join(ROOT, f))} for f in _py(svc)]   # changes on every save (K4)
        services.append({"name": svc, "files": files})
        app = ast.parse(open(os.path.join(ROOT, svc, "app.py")).read())
        mods = {a.asname or a.name: n.module for n in ast.walk(app) if isinstance(n, ast.ImportFrom) for a in n.names}
        for n in ast.walk(app):   # serve(8101, {(...): handler}) -> port, handler'ın dosyası
            if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "serve":
                port = n.args[0].value; port_svc[port] = svc
                h = n.args[1].values[0].id
                port_file[port] = mods[h].replace(".", "/") + ".py"
    for s in services:   # call("POST", "http://127.0.0.1:8103/...") -> s çağırır port'un servisini
        for f in s["files"]:
            for n in ast.walk(ast.parse(open(os.path.join(ROOT, f["file"])).read())):
                if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "call" and len(n.args) > 1 and isinstance(n.args[1], ast.Constant):
                    port = int(n.args[1].value.split(":")[2].split("/")[0])
                    if port_svc[port] not in f.setdefault("calls", []):
                        f["calls"].append(port_svc[port])
                    calls.add((s["name"], port_svc[port]))
    # file relations inside the city: `from orders.clients.x import y` -> orders/clients/x.py (shared common/ is not a building)
    dosyalar = {f["file"] for s in services for f in s["files"]}
    for s in services:
        for f in s["files"]:
            mods = {n.module for n in ast.walk(ast.parse(open(os.path.join(ROOT, f["file"])).read())) if isinstance(n, ast.ImportFrom) and n.module}
            f["fail"] = [n.lineno for n in ast.walk(ast.parse(open(os.path.join(ROOT, f["file"])).read()))
                         if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "fail"]   # lines that return a failure
            f["imports"] = sorted(m.replace(".", "/") + ".py" for m in mods if m.replace(".", "/") + ".py" in dosyalar)
    return {"services": services, "calls": sorted(calls), "port_svc": port_svc, "port_file": port_file, "kok": ROOT}


if __name__ == "__main__":
    y = yapi()
    if "--json" in sys.argv:   # snapshot for the in-browser simulation (pano), next to the shim
        json.dump(y, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "yapi.json"), "w"), ensure_ascii=False)
    print(json.dumps(y, indent=1, ensure_ascii=False))
    assert ["gateway", "orders"] in map(list, y["calls"]) and ("orders", "payments") in y["calls"], y["calls"]
    assert y["port_file"][8103] == "inventory/store/stock.py", y["port_file"]
    assert all(f["lines"] > 0 for s in y["services"] for f in s["files"])
    oh = next(f for s in y["services"] for f in s["files"] if f["file"].endswith("order_handler.py"))
    assert "orders/clients/inventory_client.py" in oh["imports"] and "orders/model/order.py" in oh["imports"], oh
    print("yapi tamam:", len(y["services"]), "servis,", sum(len(s["files"]) for s in y["services"]), "dosya")
