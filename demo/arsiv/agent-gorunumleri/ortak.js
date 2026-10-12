// shared by kupler.html: colors, side panel helpers and the timed script engine.
// Agents hand work to each other (msg), use tools (tool), speak (say); a reply (msg with reply:true) closes the asker's wait.
const COL = { "müşteri":"#f2c14e", "orkestratör":"#ff7b9c", analiz:"#4fd1ff", teklif:"#7ee787", kampanya:"#c792ea", risk:"#ffab70", "sözleşme":"#79c0ff" };
const TCOL = { crm:"analiz", katalog:"teklif", kampanya:"kampanya", risk:"risk", sozlesme:"sözleşme" };
const ICON = { crm:"👥", katalog:"📋", kampanya:"🏷", risk:"🛡", sozlesme:"✍" };
const $ = id => document.getElementById(id);

function panelBuild(d) {
  $("baslik").textContent = d.title;
  $("ags").innerHTML = Object.keys(COL).filter(a => a !== "müşteri").map(a => `<div class="row" id="r-${a}" style="--c:${COL[a]}"><i></i><span>${a}</span><span>${a === "orkestratör" ? "hazır" : "bekliyor"}</span></div>`).join("");
  $("log").innerHTML = ""; $("sonuc").textContent = "…"; $("sonuc").className = "";
}
function setRow(a, cls, txt) { const r = $("r-" + a); if (!r) return; r.className = "row " + cls; r.lastElementChild.textContent = txt; }
function logLine(from, to, text) {
  const l = document.createElement("div"); l.style.setProperty("--c", COL[from]);
  l.innerHTML = `<b style="color:${COL[from]}">${from}${to ? " → " + to : ""}</b> ${text}`; $("log").append(l); $("log").scrollTop = 1e5;
}

// h = { msg(from,to,e), tool(agent,station,e), say(agent,e), row(agent,cls,txt), reset() } ; returns { play, pause, restart, running }
function Sahne(d, h) {
  const evs = [...d.events].sort((a, b) => a.t - b.t), sp = () => +$("sp").value;
  let now, nxt, timer, waiting, running = false;
  const row = (a, cls, txt) => { setRow(a, cls, txt); h.row?.(a, cls, txt); };
  function fire(e) {
    if (e.kind === "msg") {
      const f = e.from, t = e.to; h.msg(f, t, e); logLine(f, t, e.text);
      if (e.reply) {
        delete waiting[t + ">" + f]; row(f, "d", "işini verdi");
        for (const x of e.closes || []) { for (const k of Object.keys(waiting)) if (k.startsWith(x + ">") || (k.startsWith(t + ">") && k.endsWith(">" + x))) delete waiting[k]; row(x, "d", "devretti, bitti"); }
        const w = Object.keys(waiting).find(k => k.startsWith(t + ">")); row(t, "w", w ? "yanıt bekliyor: " + w.split(">")[1] : "çalışıyor");
      } else if (f !== "müşteri" && t !== "müşteri") { waiting[f + ">" + t] = 1; row(t, "w", "çalışıyor"); row(f, "w", "yanıt bekliyor: " + t); }
    } else if (e.kind === "tool") { h.tool(e.agent, e.station, e); logLine(e.agent, null, "🔧 " + e.text); }
    else {
      h.say(e.agent, e); logLine(e.agent, null, e.text);
      const m = /^Sonuç:\s*(.+)/.exec(e.text); if (m) { $("sonuc").textContent = m[1]; $("sonuc").className = /satış/i.test(m[1]) ? "ok" : "no"; row("orkestratör", "d", "bitti"); }
    }
  }
  function tick() {
    now += 0.1 * sp();
    while (nxt < evs.length && evs[nxt].t <= now) fire(evs[nxt++]);
    if (nxt >= evs.length) { clearInterval(timer); running = false; $("pl").textContent = "▶"; }
  }
  const S = {
    play() { clearInterval(timer); timer = setInterval(tick, 100); running = true; $("pl").textContent = "⏸"; },
    pause() { clearInterval(timer); running = false; $("pl").textContent = "▶"; },
    restart() { clearInterval(timer); now = 0; nxt = 0; waiting = {}; panelBuild(d); h.reset?.(); S.play(); },
    get running() { return running; }, get finished() { return nxt >= evs.length; },
  };
  $("pl").onclick = () => S.running ? S.pause() : (S.finished ? S.restart() : S.play());
  $("rs").onclick = () => S.restart(); $("sp").onchange = () => S.running && S.play();
  return S;
}
