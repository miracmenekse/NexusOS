// node test-altlik.js : durum/zincir/takılma kuralları üç telekom senaryosunda
const A = require("./altlik.js"), fs = require("fs"), m = f => JSON.parse(fs.readFileSync(f, "utf8"));
const at = (M, t) => A.durum(M, M.events.filter(e => e.t <= t).map(e => ({ e, at: e.t })));
const tak = (M, t) => A.takilanlar(at(M, t), t);
const ok = (c, s) => { if (!c) { console.error("HATA:", s); process.exit(1); } };
const N = m("telekom-ag.json"), T = m("telekom-takilma.json"), K = m("telekom-kayip.json");
let D = at(N, 14);   // same moment the browser check used
ok(D.A["orkestratör"].hal === "bekliyor" && D.A.teklif.hal === "calisiyor" && D.A.kampanya.hal === "bitti", "t=14 durumları");
ok(A.zincir(D, "orkestratör").join(">") === "orkestratör>analiz>teklif", "t=14 zincir " + A.zincir(D, "orkestratör"));
for (let t = 0; t <= 31; t += 0.5) ok(!tak(N, t).length, "normal senaryoda takılma çıkmamalı t=" + t);
ok(at(N, 31).sonuc.ok === true, "normal sonuç satış");
ok(!tak(T, 18).length, "takılma 10 sn dolmadan uyarı yok");
const k = tak(T, 21); ok(k.length === 1 && k[0].uc === "kampanya" && k[0].zincir.join(">") === "orkestratör>analiz>teklif>kampanya", "takılma: " + JSON.stringify(k));
ok(!tak(T, 41).length, "kampanya araca dokununca uyarı kalkar");
ok(at(K, 30).sonuc.ok === false && at(K, 30).A["orkestratör"].hal === "bitti", "kayıp sonucu");
ok(at(N, 31).A.analiz.arac.crm === 2 && at(N, 31).A.risk.arac.risk === 1, "araç sayıları");
console.log("altlik.js tamam: durum, zincir, takılma, sonuç, araç sayıları");
