// Ç3 altlığı, tarayıcı tarafı: modelden (altlik.py biçimi) "şu an kim ne yapıyor" hesabı ve iki görünümün ortak panelleri.
// Görünüm yalnız olanları bildirir: olan = [{ e, at }] gerçekleşme sırasıyla, at = olayın görünüm saatindeki anı.
const Altlik = (() => {
  const insan = (m, a) => m.agents[a]?.tur === "insan";
  const mmss = t => `${Math.floor(t / 60)}:${String(Math.floor(t % 60)).padStart(2, "0")}`;
  const esc = v => String(v ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
  const HAL = { bosta: "boşta", calisiyor: "çalışıyor", bekliyor: "yanıt bekliyor", bitti: "bitti" };

  // the same rules the views used to apply one by one: a request makes the sender wait for the receiver,
  // a reply ends that wait and finishes the replier, `closes` finishes the agents the reply settles
  function durum(m, olan) {
    const A = {}, sonuc = { e: null };
    for (const a of Object.keys(m.agents)) A[a] = { ad: a, hal: "bosta", bekler: [], beklemeBasi: null, son: null, gecmis: [], arac: {} };
    const calis = a => { if (A[a] && A[a].hal !== "bekliyor" && !insan(m, a)) A[a].hal = "calisiyor"; };
    const birak = (a, b) => { const x = A[a]; if (!x) return; x.bekler = x.bekler.filter(y => y !== b);
      if (!x.bekler.length && x.hal === "bekliyor") { x.hal = "calisiyor"; x.beklemeBasi = null; } };
    for (const { e, at } of olan) {
      const kim = e.kind === "msg" ? e.from : e.agent;
      if (A[kim]) { A[kim].son = at; A[kim].gecmis.push({ e, at }); }
      if (e.kind === "msg") {
        const { from: f, to: t } = e;
        if (A[t] && t !== f) A[t].gecmis.push({ e, at, gelen: true });
        if (e.reply) {
          if (A[t]) A[t].aldi = at;   // an answer is new work for the asker
          birak(t, f); if (A[f]) { A[f].hal = "bitti"; A[f].bekler = []; A[f].beklemeBasi = null; }
          for (const x of e.closes || []) { birak(t, x); if (A[x]) { A[x].hal = "bitti"; A[x].bekler = []; A[x].beklemeBasi = null; } }
          calis(t);
        } else if (!insan(m, f) && !insan(m, t)) {
          const x = A[f]; if (!x.bekler.includes(t)) x.bekler.push(t);
          x.beklemeBasi ??= at; x.hal = "bekliyor"; A[t].hal = "calisiyor"; A[t].aldi = at;   // a new job: its silence counts from now
        } else calis(t);
      } else if (e.kind === "tool") { A[kim].arac[e.station] = (A[kim].arac[e.station] || 0) + 1; calis(kim); }
      else if (e.kind === "sonuc") { sonuc.e = e; A[kim].hal = "bitti"; }
      else calis(kim);
    }
    return { A, sonuc: sonuc.e };
  }

  // a -> the agent it waits for -> ... until someone who is not waiting (or a loop)
  function zincir(D, a) {
    const z = [a]; let x = a;
    while (D.A[x]?.hal === "bekliyor" && D.A[x].bekler.length) { x = D.A[x].bekler[0]; if (z.includes(x)) break; z.push(x); }
    return z;
  }

  // stuck = a waiting chain whose last agent has done nothing for `esik` seconds (normal delegation keeps the end busy)
  function takilanlar(D, simdi, esik = 10) {
    const uc = {};
    for (const a of Object.values(D.A)) if (a.hal === "bekliyor") {
      const z = zincir(D, a.ad), son = z.at(-1), sessiz = simdi - Math.max(D.A[son].son ?? -1e9, D.A[son].aldi ?? -1e9, a.beklemeBasi);
      if (sessiz >= esik && (!uc[son] || uc[son].zincir.length < z.length)) uc[son] = { uc: son, zincir: z, sessiz };
    }
    return Object.values(uc);
  }

  const ikon = (m, s) => m.stations[s]?.icon || "🔧";
  function satir(m, { e, at, gelen }, renk) {
    const k = renk(e.kind === "msg" ? (gelen ? e.from : e.to) : e.agent);
    const ne = e.kind === "msg" ? (gelen ? `← <b style="color:${k}">${esc(e.from)}</b>` : `→ <b style="color:${k}">${esc(e.to)}</b>`)
      : e.kind === "tool" ? ikon(m, e.station) : e.kind === "sonuc" ? "■" : "💬";
    return `<li><time>${mmss(at)}</time><span>${ne} ${esc(e.text)}</span></li>`;
  }
  // agent card: role, state, who it waits for, tools it used, what it did (newest first)
  function ajanPanel(m, D, a, renk, simdi) {
    const x = D.A[a]; if (!x) return "";
    const z = zincir(D, a), arac = Object.entries(x.arac).sort((p, q) => q[1] - p[1]);
    return `<div class="ap"><div class="ap-bas"><b style="color:${renk(a)}">${esc(a)}</b><span class="ap-hal ap-${x.hal}">${HAL[x.hal]}</span></div>
      <div class="ap-rol">${esc(m.agents[a]?.rol)}</div>
      ${z.length > 1 ? `<div class="ap-z">bekleme zinciri: ${z.map(y => `<b style="color:${renk(y)}">${esc(y)}</b>`).join(" → ")} <span>(${mmss(simdi - x.beklemeBasi)})</span></div>` : ""}
      ${arac.length ? `<div class="ap-arac">${arac.map(([s, n]) => `<span>${ikon(m, s)} ${esc(m.stations[s]?.label || s)} <b>${n}</b></span>`).join("")}</div>` : ""}
      <ol class="ap-g">${x.gecmis.slice(-40).reverse().map(g => satir(m, g, renk)).join("") || "<li><span>henüz bir şey yapmadı</span></li>"}</ol></div>`;
  }
  // tool card: who used it how often, latest calls
  function aracPanel(m, D, s, renk) {
    const kim = Object.values(D.A).filter(x => x.arac[s]).map(x => `<b style="color:${renk(x.ad)}">${esc(x.ad)}</b> ${x.arac[s]}`);
    const son = Object.values(D.A).flatMap(x => x.gecmis.filter(g => g.e.kind === "tool" && g.e.station === s)).sort((p, q) => q.at - p.at).slice(0, 12);
    return `<div class="ap"><div class="ap-bas"><b>${ikon(m, s)} ${esc(m.stations[s]?.label || s)}</b><span class="ap-hal">${son.length ? kim.length + " agent" : "kullanılmadı"}</span></div>
      ${kim.length ? `<div class="ap-arac"><span>${kim.join(" · ")}</span></div>` : ""}
      <ol class="ap-g">${son.map(g => satir(m, g, renk)).join("")}</ol></div>`;
  }
  function uyari(T, renk) {
    return T.map(k => `<div class="au" data-ajan="${esc(k.uc)}">⏳ <b>${esc(k.uc)}</b> ${Math.floor(k.sessiz)} sn'dir sessiz
      <small>${k.zincir.map(y => `<span style="color:${renk(y)}">${esc(y)}</span>`).join(" → ")} bekliyor</small></div>`).join("");
  }

  if (typeof document !== "undefined") {
  const css = document.createElement("style");
  css.textContent = `
  .ap { display:grid; gap:6px; font-size:12px; } .ap-bas { display:flex; justify-content:space-between; gap:8px; align-items:baseline; } .ap-bas b { font-size:14px; }
  .ap-hal { font-size:11px; padding:1px 8px; border-radius:9px; border:1px solid var(--line); color:var(--dim); }
  .ap-calisiyor { color:#4fd1ff; border-color:#4fd1ff66; } .ap-bekliyor { color:#ffb84d; border-color:#ffb84d66; } .ap-bitti { color:#6ee7a0; border-color:#6ee7a066; }
  .ap-rol { color:var(--dim); } .ap-z { color:#ffb84d; } .ap-z span { color:var(--dim); }
  .ap-arac { display:flex; flex-wrap:wrap; gap:4px; } .ap-arac span { border:1px solid var(--line); border-radius:6px; padding:1px 6px; }
  .ap-g { list-style:none; margin:0; padding:0; max-height:240px; overflow:auto; display:grid; gap:3px; }
  .ap-g li { display:grid; grid-template-columns:38px 1fr; gap:6px; } .ap-g time { color:var(--dim); font:11px ui-monospace,monospace; } .ap-g span { min-width:0; overflow-wrap:anywhere; }
  .au { background:#2a1a08ee; border:1px solid #ffb84d; color:#ffe2b8; border-radius:10px; padding:6px 10px; font-size:12px; cursor:pointer; box-shadow:0 0 14px #ffb84d55; }
  .au small { display:block; color:#e9c99a; }`;
  document.head.append(css); }
  return { durum, zincir, takilanlar, ajanPanel, aracPanel, uyari, mmss, ESIK: 10 };
})();
if (typeof module !== "undefined") module.exports = Altlik;
