"""Ç3 senaryosu: telekom satış agent'ları bir müşteriye paket satmaya çalışır.

Kurallı simülasyon (LLM yok): müşteri profili ve kararlar rastgele, akış her çalıştırmada farklı biter.
Usage: python3 telekom.py [seed]  ->  telekom.json  (index.html?data=telekom.json)
"""
import json, os, random, sys

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "telekom.json")

STATIONS = {
    "musteri":  {"label": "müşteri hattı",   "x": .10, "y": .50, "color": "#f2c14e"},
    "crm":      {"label": "CRM",             "x": .32, "y": .22, "color": "#4fd1ff"},
    "katalog":  {"label": "tarife kataloğu", "x": .55, "y": .22, "color": "#7ee787"},
    "kampanya": {"label": "kampanya motoru", "x": .72, "y": .45, "color": "#c792ea"},
    "risk":     {"label": "kredi / risk",    "x": .55, "y": .80, "color": "#ffab70"},
    "sozlesme": {"label": "sözleşme",        "x": .32, "y": .80, "color": "#79c0ff"},
    "meeting":  {"label": "koordinasyon",    "x": .38, "y": .50, "color": "#ff7b9c"},
}
AGENTS = {  # name -> görev
    "müşteri": "Mevcut abone, faturası yüksek, rakip teklifi var",
    "orkestratör": "Satış sürecini yönetir, işi agent'lara dağıtır",
    "analiz": "CRM'den kullanım ve fatura geçmişini çıkarır",
    "teklif": "Katalogdan uygun tarifeyi seçer",
    "kampanya": "İndirim ve ek paket önerir, marj sınırını korur",
    "risk": "Kredi skoru ve cihaz taksit uygunluğunu kontrol eder",
    "sözleşme": "Taahhüt ve sözleşmeyi hazırlar",
}
TARIFFS = [("Mega 20 GB", 349), ("Ultra 40 GB", 449), ("Sınırsız Pro", 599)]


def run(seed):
    r = random.Random(seed)
    gb = r.choice([12, 25, 38, 60]); bill = r.choice([420, 510, 640]); rival = bill - r.choice([60, 90, 130])
    score = r.randint(450, 900); wants_phone = r.random() < .5
    ev, t = [], 0.0

    def e(agent, text, station=None, kind="say", **kw):
        nonlocal t
        t += 1
        ev.append(dict(t=t, agent=agent, kind=kind, station=station, text=text, **kw))

    e("müşteri", f"Faturam {bill} TL, rakip {rival} TL teklif etti", "musteri", "user")
    e("orkestratör", "Müşteri kayıp riski: satış ekibini topluyorum", "meeting")
    for a in ("analiz", "teklif", "kampanya", "risk"):
        e("orkestratör", f"{a} agent'ı göreve", "meeting", "spawn", child=a)
    e("analiz", "CRM: abonelik ve son 6 ay kullanım", "crm", "tool")
    e("analiz", f"Ortalama {gb} GB kullanıyor, ödemeleri düzenli", "crm")
    e("analiz", "bulgular orkestratöre", "meeting", "report")
    pick = next((x for x in TARIFFS if int(x[0].split()[1] if x[0][0] != "S" else 999) >= gb), TARIFFS[-1])
    e("teklif", f"Katalog taraması: {gb} GB için uygun tarifeler", "katalog", "tool")
    e("teklif", f"Önerim: {pick[0]} ({pick[1]} TL)", "katalog")
    e("teklif", "tarife önerisi orkestratöre", "meeting", "report")
    price = pick[1]
    if price >= rival:
        disc = min(price - rival + 20, int(price * .2))
        e("kampanya", f"Rakibin altına inmek için %{round(disc / price * 100)} indirim deniyorum", "kampanya", "tool")
        price -= disc
        if price >= rival:
            e("kampanya", "Marj sınırı! Daha fazla inemem; yerine 10 GB hediye", "kampanya")
        else:
            e("kampanya", f"Yeni fiyat {price} TL, marj içinde", "kampanya")
    else:
        e("kampanya", "Fiyat zaten rakipten iyi, ek olarak 3 ay dijital TV", "kampanya")
    e("kampanya", "kampanya kararı orkestratöre", "meeting", "report")
    if wants_phone:
        e("müşteri", "Yanında yeni telefon da alabilir miyim?", "musteri", "user")
        e("risk", f"Kredi skoru sorgusu: {score}", "risk", "tool")
        phone_ok = score >= 600
        e("risk", "24 ay taksit uygun" if phone_ok else "Skor düşük: taksit yok, peşin önerilsin", "risk")
    else:
        phone_ok = True
        e("risk", "Cihaz talebi yok, risk kontrolü gerekmiyor", "risk")
    e("risk", "risk sonucu orkestratöre", "meeting", "report")
    e("orkestratör", f"Teklif: {pick[0]} {price} TL" + (" + telefon" if wants_phone and phone_ok else ""), "musteri")
    accept = price < rival or (price - rival < 40 and r.random() < .6)
    if wants_phone and not phone_ok:
        accept = accept and r.random() < .5
    if not accept:
        e("müşteri", "Hâlâ pahalı, düşüneceğim", "musteri", "user")
        e("orkestratör", "Kayıp riski sürüyor: 48 saat sonra geri arama planlandı", "crm", "tool")
        e("analiz", "CRM'e not: fiyat hassas, rakip teklifli", "crm", "tool")
        result = "kaybedildi"
    else:
        e("müşteri", "Tamam, kabul ediyorum", "musteri", "user")
        e("orkestratör", "sözleşme agent'ı göreve", "meeting", "spawn", child="sözleşme")
        e("sözleşme", "12 ay taahhüt sözleşmesi hazırlanıyor", "sozlesme", "tool")
        e("sözleşme", "e-imza müşteriye gönderildi, imzalandı", "sozlesme")
        e("sözleşme", "sözleşme tamam", "meeting", "report")
        e("analiz", "CRM güncellendi: yeni tarife aktif", "crm", "tool")
        result = "satış"
    e("orkestratör", f"Sonuç: {result}", "meeting")
    return dict(title=f"Telekom satış · senaryo {seed} · {result}", stations=STATIONS, agents=AGENTS,
                events=ev), result


if __name__ == "__main__":
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else random.randrange(1000)
    data, result = run(seed)
    json.dump(data, open(OUT, "w"), ensure_ascii=False)
    # self-check: every spawned agent reports back; outcome is one of the two endings
    spawned = {x["child"] for x in data["events"] if x["kind"] == "spawn"}
    reported = {x["agent"] for x in data["events"] if x["kind"] == "report"}
    assert spawned <= reported and result in ("satış", "kaybedildi"), (spawned, reported)
    print(f"senaryo {seed}: {len(data['events'])} olay, sonuç {result} -> {OUT}")
