// Ç1/Ç2 without the VM: when the page is not served by traffic/server.py (:4400), e.g. inside the pano, the four demo
// services are imitated in the browser with the same rules (stock refilled every 20 s, lamp stock 3, large payments
// rejected half the time, ariza.json faults) and the server's endpoints are answered here.
// ponytail: the call chain (checkout → orders → reserve → charge) is written out for these 4 services, not read from code.
(() => {
  if (["4400", "4410"].includes(location.port)) return;   // real server: nothing to do
  window.SEHIR = "sehir.html";                             // Ç2 → Ç1 links
  const Y = (() => { const r = new XMLHttpRequest(); r.open("GET", "yapi.json", false); r.send(); return JSON.parse(r.responseText); })();
  const dosya = (svc, cagir) => Y.services.find(s => s.name === svc).files.find(f => (f.calls || []).includes(cagir))?.file;
  const portu = svc => Object.entries(Y.port_svc).find(([, s]) => s === svc)[0];
  const isle = svc => Y.port_file[portu(svc)];
  const failSatir = svc => { const f = isle(svc), x = Y.services.flatMap(s => s.files).find(g => g.file === f); return x?.fail?.[0] ? `${f}:${x.fail[0]}` : null; };

  // --- server endpoints
  let ARIZA = {};
  const json = (v, status = 200) => Promise.resolve(new Response(JSON.stringify(v), { status, headers: { "Content-Type": "application/json" } }));
  const _fetch = window.fetch.bind(window);
  window.fetch = (url, opt = {}) => {
    const u = String(url);
    if (u.startsWith("/yapi")) return json(Y);
    if (u.startsWith("/kod?f=")) return _fetch("kod/" + decodeURIComponent(u.slice(7)));
    if (u.startsWith("/ariza")) {
      if ((opt.method || "GET") === "POST") {
        const b = JSON.parse(opt.body || "{}"), t = {};
        for (const [s, v] of Object.entries(b)) if (Object.values(Y.port_svc).includes(s))
          t[s] = { gecikme_ms: Math.max(0, Math.min(5000, +v.gecikme_ms || 0)), hata: Math.max(0, Math.min(1, +v.hata || 0)) };
        ARIZA = t;
      }
      return json(ARIZA);
    }
    if (u.includes(":4500/canli/")) return Promise.reject(new Error("simülasyonda agent köprüsü yok"));
    return _fetch(url, opt);
  };
  const _open = XMLHttpRequest.prototype.open;
  XMLHttpRequest.prototype.open = function (m, url, ...r) { return _open.call(this, m, String(url).startsWith("/yapi") ? "yapi.json" : url, ...r); };

  // --- the services
  const FULL = { book: 50, pen: 200, lamp: 3 }, PRICE = { book: 12.5, pen: 1.2, lamp: 30 };
  let stok = { ...FULL }, dolum = performance.now();
  const dinleyen = new Set();
  const yolla = ev => dinleyen.forEach(es => es._ver(ev));
  const bekle = ms => new Promise(r => setTimeout(r, ms));
  // one hop: `kim` (file of the caller) calls service `svc`; returns the answer after logging the call like web.call()
  async function cagri(fromSvc, fromFile, svc, path, iz, isFn) {
    const bas = performance.now(), a = ARIZA[svc] || {};
    await bekle(1 + Math.random() * 2 + (a.gecikme_ms || 0));
    let out = Math.random() < (a.hata || 0) ? { ok: false, reason: `enjekte arıza (${svc}, ariza.json)` } : await isFn();
    const ok = out.ok !== false, ms = performance.now() - bas;
    yolla({ from: fromSvc, to: svc, ok, ms, fromFile, toFile: isle(svc), at: ok ? null : out.at || null, path, detail: ok ? null : out, iz, bas });
    return out;
  }
  const reserve = (item, qty) => {
    if (performance.now() - dolum > 20000) { stok = { ...FULL }; dolum = performance.now(); }
    if ((stok[item] || 0) < qty) return { ok: false, reason: "stok yetersiz", at: failSatir("inventory"), item, istenen: qty, kalan: stok[item] || 0 };
    stok[item] -= qty; return { ok: true, left: stok[item] };
  };
  const charge = amount => amount >= 40 && Math.random() < .5 ? { ok: false, reason: "sağlayıcı ödemeyi reddetti", at: failSatir("payments"), amount } : { ok: true, amount };
  async function siparis() {   // traffic/load.py: one random checkout through the gateway
    const iz = Math.random().toString(16).slice(2, 14), item = ["book", "pen", "lamp"][Math.floor(Math.random() * 3)], qty = 1 + Math.floor(Math.random() * 5);
    await cagri("user", "user", "gateway", "/checkout", iz, () =>
      cagri("gateway", dosya("gateway", "orders"), "orders", "/orders", iz, async () => {
        const s = await cagri("orders", dosya("orders", "inventory"), "inventory", "/reserve", iz, async () => reserve(item, qty));
        if (s.ok === false) return { status: "out_of_stock" };
        const p = await cagri("orders", dosya("orders", "payments"), "payments", "/charge", iz, async () => charge(PRICE[item] * qty));
        return { status: p.ok === false ? "payment_failed" : "paid" };
      }));
  }
  (function dongu() { siparis(); setTimeout(dongu, 200 + Math.random() * 600); })();

  window.EventSource = class {
    constructor() { this.listeners = []; dinleyen.add(this); setTimeout(() => this.onopen?.({}), 50); }
    addEventListener(t, f) { if (t === "message") this.listeners.push(f); }
    close() { dinleyen.delete(this); }
    _ver(ev) { const m = { data: JSON.stringify(ev) }; this.onmessage?.(m); this.listeners.forEach(f => f(m)); }
  };
  addEventListener("DOMContentLoaded", () => {
    const b = document.createElement("div");
    b.textContent = "simülasyon · servisler tarayıcıda taklit ediliyor; gerçeği için VM'de demo/run.sh";
    b.style.cssText = "position:fixed;left:50%;bottom:6px;transform:translateX(-50%);z-index:20;font:11px system-ui;color:#9fb0cc;background:#0d1628cc;border:1px solid #22355a;border-radius:999px;padding:2px 10px;pointer-events:none";
    document.body.append(b);
  });
})();
