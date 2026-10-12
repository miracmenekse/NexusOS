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

Kullanım: python3 altlik.py [oturum.jsonl]  ->  oturum.json (alt agent başlatmış en yeni Claude Code oturumu, modele çevrilmiş)
Görünümde: ofis2.html?data=oturum.json, ag.html?data=oturum.json
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
        if e["kind"] == "spawn":
            agents[e["child"]] = {"rol": "Alt agent: " + e["text"].removeprefix("Agent: "), "tur": "agent"}
    stations, events, parent, t, prev = {}, [], {}, 0.0, None
    for e in tl:
        # ponytail: gerçek süre saatler sürer; olaylar arası boşluk 0,4-2,5 sn'ye sıkıştırılır
        t = round(t + (0 if prev is None else min(2.5, max(0.4, e["t"] - prev))), 2); prev = e["t"]
        k, a = e["kind"], e["agent"]
        if k == "user":
            events.append(dict(t=t, kind="msg", **{"from": "sen"}, to="claude", text=e["text"]))
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


if __name__ == "__main__":
    # self-check: elle yazılmış senaryo modele uyuyor
    dogrula(json.load(open(os.path.join(HERE, "telekom-ag.json"))))
    try:
        dogrula({"agents": {"a": {"tur": "ana"}}, "stations": {}, "events": [{"t": 0, "kind": "msg", "from": "a", "to": "yok"}]})
        raise SystemExit("dogrula tanımsız alıcıyı yakalamadı")
    except AssertionError:
        pass
    # varsayılan: alt agent başlatmış en yeni oturum (yoksa görünümde tek agent kalır)
    session = sys.argv[1] if len(sys.argv) > 1 else max((p for p in glob.glob(build.PROJ + "/*.jsonl") if os.path.isdir(p[:-6] + "/subagents")), key=os.path.getmtime)
    m = claude_code(session)
    out = os.path.join(HERE, "oturum.json")
    json.dump(m, open(out, "w"), ensure_ascii=False)
    print(f"{len(m['events'])} olay, {len(m['agents'])} katılımcı, {m['events'][-1]['t']:.0f} sn -> {out}")
