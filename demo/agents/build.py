"""Ç3: turn a Claude Code session (main + subagent JSONL transcripts) into a replay timeline for index.html.

Usage: python3 build.py [session.jsonl]   (default: newest session of the home project)
Output: timeline.json = [{t, agent, kind: user|say|tool|spawn|report, station, text}]
"""
import glob, json, os, re, sys
from datetime import datetime

PROJ = os.path.expanduser("~/.claude/projects/-home-karakolyemiracmeneksevm")
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "timeline.json")

STATIONS = {  # tool name -> office station
    "Bash": "terminal", "Read": "files", "Write": "files", "Edit": "files",
    "WebSearch": "web", "WebFetch": "web", "ArtifactData": "panel", "Artifact": "panel",
    "Agent": "meeting", "Skill": "library", "ToolSearch": "library",
}


def station(tool):
    if tool.startswith("mcp__claude_ai_Google_Drive"):
        return "drive"
    return STATIONS.get(tool, "library")


def short(s, n=70):
    s = re.sub(r"\s+", " ", str(s)).strip()
    return s if len(s) <= n else s[: n - 1] + "…"


def tool_text(name, inp):
    for k in ("description", "query", "file_path", "command", "action", "fileId"):
        if k in inp:
            v = os.path.basename(inp[k]) if k == "file_path" else inp[k]
            return f"{name}: {short(v, 60)}"
    return name


def ts(d):
    return datetime.fromisoformat(d["timestamp"].replace("Z", "+00:00")).timestamp()


def events(path, agent):
    for line in open(path):
        d = json.loads(line)
        if d.get("type") not in ("user", "assistant") or "timestamp" not in d:
            continue
        content = (d.get("message") or {}).get("content")
        if d["type"] == "user" and agent == "claude" and not d.get("isMeta"):
            texts = [content] if isinstance(content, str) else [
                c.get("text", "") for c in content or [] if isinstance(c, dict) and c.get("type") == "text"]
            texts = [x for x in texts if x.strip() and not x.lstrip().startswith("<")]
            if texts:
                yield dict(t=ts(d), agent="sen", kind="user", station="desk", text=short(texts[0]))
            if isinstance(content, str):
                continue
        for c in content if isinstance(content, list) else []:
            if not isinstance(c, dict):
                continue
            if c.get("type") == "text" and d["type"] == "assistant" and c["text"].strip():
                yield dict(t=ts(d), agent=agent, kind="say", station=None, text=short(c["text"]))
            elif c.get("type") == "tool_use":
                ev = dict(t=ts(d), agent=agent, kind="tool", station=station(c["name"]),
                          text=tool_text(c["name"], c.get("input") or {}))
                if c["name"] == "Agent":
                    ev.update(kind="spawn", tool_id=c["id"])
                yield ev
            elif c.get("type") == "tool_result" and agent == "claude":
                text = json.dumps(c.get("content"))
                m = re.search(r"agentId: (\w+)", text)
                if m:
                    yield dict(t=ts(d), agent="claude", kind="link", tool_id=c["tool_use_id"], sub=m.group(1))


def build(session):
    main = list(events(session, "claude"))
    links = {e["tool_id"]: e["sub"] for e in main if e["kind"] == "link"}
    timeline = [e for e in main if e["kind"] != "link"]
    subdir = session[:-6] + "/subagents"
    for i, (tool_id, sub) in enumerate(links.items(), 1):
        name = f"yardımcı {i}"
        for e in timeline:
            if e.get("tool_id") == tool_id:
                e["child"] = name
        sub_events = list(events(os.path.join(subdir, f"agent-{sub}.jsonl"), name))
        timeline += sub_events
        if sub_events:
            timeline.append(dict(t=sub_events[-1]["t"] + 1, agent=name, kind="report", station="meeting",
                                 text="raporum hazır"))
    timeline.sort(key=lambda e: e["t"])
    t0 = timeline[0]["t"]
    for e in timeline:
        e["t"] = round(e["t"] - t0, 2)
        e.pop("tool_id", None)
    return timeline


if __name__ == "__main__":
    session = sys.argv[1] if len(sys.argv) > 1 else max(glob.glob(PROJ + "/*.jsonl"), key=os.path.getmtime)
    tl = build(session)
    json.dump(tl, open(OUT, "w"), ensure_ascii=False)
    agents = sorted({e["agent"] for e in tl})
    # self-check: subagents were spawned and linked
    assert any(e["kind"] == "spawn" and e.get("child") for e in tl) or len(agents) <= 2, agents
    print(f"{len(tl)} olay, agent'lar: {agents} -> {OUT}")
