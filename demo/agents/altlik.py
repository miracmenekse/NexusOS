"""Ç3 altlığı: agent'ların ne yaptığını tek biçimde tutan olay modeli.

Her görünüm (ofis2.html, ag.html, ...) yalnız bu biçimi okur; her kaynak (elle yazılmış senaryo,
Claude Code oturumu, ileride canlı bir agent sistemi) bu biçime çevrilir.

    {
      "title": "...",
      "kanal": "satis-ofisi",                      # isteğe bağlı, sohbet başlığı
      "agents":   {"<ad>": {"rol": "...", "tur": "insan" | "ana" | "agent"}},   # sıra = yerleşim sırası
      "stations": {"<id>": {"label": "...", "icon": "🔧"}},                       # agent'ın kullandığı araçlar
      "events": [                                   # t = saniye, artan
        {"t": 0,   "kind": "msg",   "from": "<ad>", "to": "<ad>", "text": "...",
                   "reply": true, "closes": ["<ad>"]},   # reply: soruya cevap; closes: işi böylece biten agent'lar
        {"t": 3.5, "kind": "tool",  "agent": "<ad>", "station": "<id>", "text": "..."},
        {"t": 11,  "kind": "say",   "agent": "<ad>", "text": "..."},
        {"t": 29,  "kind": "sonuc", "agent": "<ad>", "text": "satış", "ok": true}
      ]
    }

Tam olarak bir "ana" agent olur (koordinatör); "insan" olanlar (müşteri, kullanıcı) agent değildir, dışarıdan gelir.

Kaynaklar (dönüştürücüler): telekom senaryoları (elle, *.json), claude_code() (Claude Code oturum kaydı),
otel() (OpenTelemetry GenAI izleri: invoke_agent / execute_tool span'ları; her agent çatısının ortak dışa aktarımı).

Kullanım: python3 altlik.py [oturum.jsonl]  ->  oturum.json (alt agent başlatmış en yeni Claude Code oturumu, modele çevrilmiş)
          python3 altlik.py izler.json      ->  otel.json   (OTLP JSON ya da düz span listesi)
Görünümde: ofis2.html?data=oturum.json, ag.html?data=otel.json; canlı: canli.py
"""
import glob, json, os, sys

import build

HERE = os.path.dirname(os.path.abspath(__file__))
KINDS = {"msg": ("from", "to"), "tool": ("agent", "station"), "say": ("agent",), "sonuc": ("agent",)}


def dogrula(m):
    """Modeli denetler; sorun varsa AssertionError (mesajı neyin bozuk olduğunu söyler)."""
    ag, st = m["agents"], m["stations"]
    assert sum(a["tur"] == "ana" for a in ag.values()) == 1, "tam olarak bir 'ana' agent olmalı"
    assert all(a["tur"] in ("insan", "ana", "agent") for a in ag.values()), "tur: insan | ana | agent"
    son = 0
    for i, e in enumerate(m["events"]):
        assert e["kind"] in KINDS, f"olay {i}: bilinmeyen kind {e['kind']!r}"
        assert e["t"] >= son, f"olay {i}: t geriye gidiyor"
        son = e["t"]
        for alan in KINDS[e["kind"]]:
            havuz = st if alan == "station" else ag
            assert e.get(alan) in havuz, f"olay {i}: {alan}={e.get(alan)!r} tanımlı değil"
        for x in e.get("closes", []):
            assert x in ag, f"olay {i}: closes içinde tanımsız {x!r}"
    return m


IKON = {"terminal": "⌨", "files": "📄", "web": "🌐", "drive": "🗂", "panel": "📊", "library": "📚"}


def claude_code(session):
    """Claude Code oturumu (ana + alt agent kayıtları) -> model."""
    tl = build.build(session)
    agents = {"sen": {"rol": "Kullanıcı: işi veren", "tur": "insan"},
              "claude": {"rol": "Ana agent: planlar, araç kullanır, alt agent başlatır", "tur": "ana"}}
    for e in tl:
        if e["kind"] == "spawn" and e.get("child"):
            agents[e["child"]] = {"rol": "Alt agent: " + e["text"].removeprefix("Agent: "), "tur": "agent"}
    stations, events, parent, t, prev = {}, [], {}, 0.0, None
    for e in tl:
        # ponytail: gerçek süre saatler sürer; olaylar arası boşluk 0,4-2,5 sn'ye sıkıştırılır
        t = round(t + (0 if prev is None else min(2.5, max(0.4, e["t"] - prev))), 2); prev = e["t"]
        k, a = e["kind"], e["agent"]
        if k == "user":
            events.append(dict(t=t, kind="msg", **{"from": "sen"}, to="claude", text=e["text"]))
        elif k == "spawn" and not e.get("child"):   # still running: its log is linked only when it reports back
            events.append(dict(t=t, kind="say", agent=a, text="alt agent başlattı: " + e["text"].removeprefix("Agent: ")))
        elif k == "spawn":
            parent[e["child"]] = a
            events.append(dict(t=t, kind="msg", **{"from": a}, to=e["child"], text=e["text"].removeprefix("Agent: ")))
        elif k == "report":
            events.append(dict(t=t, kind="msg", **{"from": a}, to=parent.get(a, "claude"), text=e["text"], reply=True))
        elif k == "tool":
            s = e["station"]; stations.setdefault(s, {"label": s, "icon": IKON.get(s, "🔧")})
            events.append(dict(t=t, kind="tool", agent=a, station=s, text=e["text"]))
        else:
            events.append(dict(t=t, kind="say", agent=a, text=e["text"]))
    return dogrula(dict(title="Bu projenin agent'ları · Claude Code oturumu", kanal="nexusos",
                        agents=agents, stations=stations, events=events))


def _attrs(span):
    a = span.get("attributes") or {}
    if isinstance(a, list):   # OTLP JSON: [{"key": k, "value": {"stringValue": v}}]
        a = {x["key"]: next(iter(x["value"].values()), None) for x in a}
    return a


def otel(data):
    """OpenTelemetry GenAI span'ları -> model. invoke_agent = agent'a iş verildi (bitişi = cevap),
    execute_tool = araç kullanımı; üst agent, en yakın invoke_agent atası. En üstteki agent "ana"dır."""
    spans = data.get("spans") if isinstance(data, dict) and "spans" in data else data
    if isinstance(data, dict) and "resourceSpans" in data:
        spans = [s for r in data["resourceSpans"] for ss in r.get("scopeSpans", []) for s in ss.get("spans", [])]
    by = {s["spanId"]: s for s in spans}
    ns = lambda s, k: int(s[k]) / 1e9
    t0 = min(ns(s, "startTimeUnixNano") for s in spans)

    def ajan(s):   # agent that owns this span
        while s:
            a = _attrs(s)
            if a.get("gen_ai.operation.name") == "invoke_agent" and s is not cur:
                return a.get("gen_ai.agent.name")
            s = by.get(s.get("parentSpanId"))
        return None

    agents, stations, ev = {"kullanıcı": {"rol": "İsteği veren", "tur": "insan"}}, {}, []
    for cur in sorted(spans, key=lambda s: int(s["startTimeUnixNano"])):
        a, t1, t2 = _attrs(cur), round(ns(cur, "startTimeUnixNano") - t0, 2), round(ns(cur, "endTimeUnixNano") - t0, 2)
        op, ok = a.get("gen_ai.operation.name"), (cur.get("status") or {}).get("code") not in ("STATUS_CODE_ERROR", 2)
        if op == "invoke_agent":
            ad, ust = a.get("gen_ai.agent.name"), ajan(by.get(cur.get("parentSpanId")))
            agents.setdefault(ad, {"rol": a.get("gen_ai.agent.description", ""), "tur": "agent" if ust else "ana"})
            gorev = a.get("nexusos.gorev") or a.get("gen_ai.agent.description") or "görev"
            if ust:
                ev += [dict(t=t1, kind="msg", **{"from": ust}, to=ad, text=gorev),
                       dict(t=t2, kind="msg", **{"from": ad}, to=ust, text=a.get("nexusos.sonuc", "tamam" if ok else "hata"), reply=True)]
            else:
                ev += [dict(t=t1, kind="msg", **{"from": "kullanıcı"}, to=ad, text=gorev),
                       dict(t=t2 + 0.01, kind="sonuc", agent=ad, text=a.get("nexusos.sonuc", "tamam" if ok else "hata"), ok=ok)]
        elif op == "execute_tool":
            ad, arac = ajan(cur), a.get("gen_ai.tool.name", "araç")
            stations.setdefault(arac, {"label": arac, "icon": "🔧"})
            ev.append(dict(t=t1, kind="tool", agent=ad, station=arac, text=a.get("nexusos.ozet", arac) + ("" if ok else " (hata)")))
    ev.sort(key=lambda e: e["t"])
    return dogrula(dict(title=data.get("title", "OpenTelemetry izi") if isinstance(data, dict) else "OpenTelemetry izi",
                        agents=agents, stations=stations, events=ev))


if __name__ == "__main__":
    # self-check: elle yazılmış senaryo modele uyuyor
    dogrula(json.load(open(os.path.join(HERE, "telekom-ag.json"))))
    try:
        dogrula({"agents": {"a": {"tur": "ana"}}, "stations": {}, "events": [{"t": 0, "kind": "msg", "from": "a", "to": "yok"}]})
        raise SystemExit("dogrula tanımsız alıcıyı yakalamadı")
    except AssertionError:
        pass
    o = otel(json.load(open(os.path.join(HERE, "ornek-otel.json"))))   # self-check: GenAI izi dönüştürücüsü
    assert list(o["agents"]) == ["kullanıcı", "planlayıcı", "araştırmacı", "yazar"] and o["events"][-1]["kind"] == "sonuc", o["agents"]
    if len(sys.argv) > 1 and sys.argv[1].endswith(".json"):
        json.dump(otel(json.load(open(sys.argv[1]))), open(os.path.join(HERE, "otel.json"), "w"), ensure_ascii=False)
        raise SystemExit(f"otel.json yazıldı")
    # varsayılan: alt agent başlatmış en yeni oturum (yoksa görünümde tek agent kalır)
    session = sys.argv[1] if len(sys.argv) > 1 else max((p for p in glob.glob(build.PROJ + "/*.jsonl") if os.path.isdir(p[:-6] + "/subagents")), key=os.path.getmtime)
    m = claude_code(session)
    out = os.path.join(HERE, "oturum.json")
    json.dump(m, open(out, "w"), ensure_ascii=False)
    print(f"{len(m['events'])} olay, {len(m['agents'])} katılımcı, {m['events'][-1]['t']:.0f} sn -> {out}")
