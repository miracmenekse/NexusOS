"""Turn demo/services into ExplorViz mock data (structure.json, dynamic.json, timestamps.json).

service -> city, folder -> district, .py file -> building.
Edges: in-service imports + cross-service HTTP calls (call("POST", "http://127.0.0.1:PORT/path")
matched to the serve(PORT, {(method, path): handler}) route table). Runtime counts come from
services/events.jsonl when present (written by common/web.py).
"""
import ast, json, os, sys, time
from collections import defaultdict
from urllib.parse import urlparse

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "services")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "explorviz-mock", "demo-data", "NexusOS Demo")
TOKEN = "nexusos-demo-0001"


def py_files(service):
    for d, _, fs in os.walk(os.path.join(ROOT, service)):
        for f in sorted(fs):
            if f.endswith(".py") and f != "__init__.py":
                yield os.path.relpath(os.path.join(d, f), ROOT)


def module_to_file(mod):
    return mod.replace(".", "/") + ".py"


def handler_source(rel, fn):
    """Line and source of the route handler, for the popup's "Go to Error"."""
    tree = ast.parse(open(os.path.join(ROOT, rel)).read())
    for n in ast.walk(tree):
        if isinstance(n, ast.FunctionDef) and n.name == fn:
            lines = open(os.path.join(ROOT, rel)).read().splitlines()[n.lineno - 1:n.end_lineno]
            return dict(function=fn, line=n.lineno, code="\n".join(lines))
    return dict(function=fn, line=0, code="")


def build():
    services = sorted(d for d in os.listdir(ROOT)
                      if os.path.isdir(os.path.join(ROOT, d)) and d not in ("common", "__pycache__"))
    ids = iter(range(1, 100000))
    cities, districts, buildings, file_id, trees = {}, {}, {}, {}, {}

    for s in services:
        cid = str(next(ids))
        cities[cid] = dict(id=cid, name=s, fqn=s, telemetryKey=cid, districtIds=[], buildingIds=[],
                           allContainedDistrictIds=[], allContainedBuildingIds=[])
        dir_id = {}

        def district(path):  # path like "orders/handlers"
            if path in dir_id:
                return dir_id[path]
            parent = os.path.dirname(path)
            did = str(next(ids))
            districts[did] = dict(id=did, name=os.path.basename(path), fqn=path, telemetryKey=did,
                                  parentCityId=cid, districtIds=[], buildingIds=[])
            if parent:
                pid = district(parent)
                districts[did]["parentDistrictId"] = pid
                districts[pid]["districtIds"].append(did)
            else:
                districts[did]["parentDistrictId"] = cid
                cities[cid]["districtIds"].append(did)
            cities[cid]["allContainedDistrictIds"].append(did)
            dir_id[path] = did
            return did

        for rel in py_files(s):
            src = open(os.path.join(ROOT, rel)).read()
            tree = ast.parse(src)
            trees[rel] = tree
            did = district(os.path.dirname(rel))
            bid = str(next(ids))
            funcs = sum(isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)) for n in ast.walk(tree))
            buildings[bid] = dict(id=bid, name=os.path.basename(rel), fqn=rel, telemetryKey=bid,
                                  parentCityId=cid, parentDistrictId=did, language="PYTHON",
                                  metrics={"lineCount": {"current": len(src.splitlines())},
                                           "functionCount": {"current": funcs},
                                           # failed calls received; shown via the issueActivity heatmap
                                           "issueActivity": {"current": 0}})
            districts[did]["buildingIds"].append(bid)
            cities[cid]["allContainedBuildingIds"].append(bid)
            file_id[rel] = bid

    # route table: (port, method, path) -> handler file
    routes, handler_fn = {}, {}
    for rel, tree in trees.items():
        imported = {a.asname or a.name: module_to_file(n.module)
                    for n in ast.walk(tree) if isinstance(n, ast.ImportFrom) and n.module for a in n.names}
        for n in ast.walk(tree):
            if isinstance(n, ast.Call) and getattr(n.func, "id", "") == "serve" and len(n.args) == 2:
                port = n.args[0].value
                for k, v in zip(n.args[1].keys, n.args[1].values):
                    method, path = (e.value for e in k.elts)
                    routes[(port, method, path)] = imported.get(v.id, rel)
                    handler_fn[(port, method, path)] = v.id

    edges = defaultdict(lambda: dict(requestCount=0, executionTime=0, errors=0, functionCount=0))

    def resolve(url, method):
        u = urlparse(url)
        return routes.get((u.port, method, u.path))

    for rel, tree in trees.items():
        for n in ast.walk(tree):
            if isinstance(n, ast.ImportFrom) and n.module and module_to_file(n.module) in file_id:
                e = edges[(rel, module_to_file(n.module))]
                e["functionCount"] += len(n.names)
            if (isinstance(n, ast.Call) and getattr(n.func, "id", "") == "call" and len(n.args) >= 2
                    and all(isinstance(a, ast.Constant) for a in n.args[:2])):
                target = resolve(n.args[1].value, n.args[0].value)
                if target in file_id:
                    edges[(rel, target)]["functionCount"] += 1

    events = os.path.join(ROOT, "events.jsonl")
    spans = 0
    if os.path.exists(events):
        for line in open(events):
            ev = json.loads(line)
            target = resolve(ev["url"], ev["method"])
            if ev.get("caller") in file_id and target in file_id:
                e = edges[(ev["caller"], target)]
                e["requestCount"] += 1
                e["executionTime"] += ev["ns"]
                e["errors"] += not ev["ok"]
                buildings[file_id[target]]["metrics"]["issueActivity"]["current"] += not ev["ok"]
                if not ev["ok"]:
                    u = urlparse(ev["url"])
                    issue = buildings[file_id[target]].setdefault("nexusIssue", dict(
                        count=0, route=f'{ev["method"]} {u.path}', caller=ev["caller"],
                        **handler_source(target, handler_fn.get((u.port, ev["method"], u.path)))))
                    issue["count"] += 1
                    issue["last"] = json.dumps(ev.get("detail"))
                spans += 1

    comms = []
    for (a, b), m in edges.items():
        m = dict(m, requestCount=max(m["requestCount"], 1))
        comms.append(dict(id=f"{file_id[a]}-{file_id[b]}", name=f"{a} -> {b}",
                          sourceBuildingId=file_id[a], targetBuildingId=file_id[b],
                          isBidirectional=False, metrics=m))
    ranges = {k: dict(min=min(c["metrics"][k] for c in comms), max=max(c["metrics"][k] for c in comms))
              for k in ("requestCount", "executionTime", "functionCount")}

    os.makedirs(OUT, exist_ok=True)
    dump = lambda name, obj: json.dump(obj, open(os.path.join(OUT, name), "w"), indent=1)
    dump("structure.json", dict(landscapeToken=TOKEN, cities=cities, districts=districts, buildings=buildings))
    dump("dynamic.json", dict(metrics=ranges, communications=comms))
    dump("timestamps.json", [dict(epochNano=time.time_ns(), spanCount=max(spans, 1))])
    return cities, buildings, comms, routes


if __name__ == "__main__":
    cities, buildings, comms, routes = build()
    cross = [c for c in comms if buildings[c["sourceBuildingId"]]["parentCityId"]
             != buildings[c["targetBuildingId"]]["parentCityId"]]
    # self-check: 4 services, every client call resolved to its route handler
    assert len(cities) == 4, cities
    assert {c["name"] for c in cross} >= {
        "gateway/routing.py -> orders/handlers/order_handler.py",
        "orders/clients/inventory_client.py -> inventory/store/stock.py",
        "orders/clients/payment_client.py -> payments/provider/card.py"}, [c["name"] for c in cross]
    print(f"{len(cities)} services, {len(buildings)} files, {len(comms)} edges ({len(cross)} cross-service) -> {OUT}")
