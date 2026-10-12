# Demo teknik araştırması: mikroservis kod şehri (WBS 6.1, 2026-10-11)

Web araştırması (Claude). Hedef: 3-4 mikroservisli kodu kod şehri / kod küpü mantığıyla tarayıcıda görselleştirmek,
servisler arası çağrıları canlı akış olarak göstermek.

## 1. En yakın hazır örnek: ExplorViz
- Açık kaynak, web tabanlı, 3B şehir metaforu; statik + dinamik analiz; WebGL/WebXR. ([explorviz.dev](https://explorviz.dev/1-about/), [GitHub](https://github.com/ExplorViz/ExplorViz))
- Eşleme: iç içe yeşil/mavi kutular = paketler (mahalle), açık mavi = sınıf (bina). Seçili zaman aralığındaki metot çağrıları **sarı kavisli çizgi + yön oku**; 10 sn'lik güncelleme döngüsü.
- Mikroservis: dağıtık PetClinic'te 6 uygulama gri temeller üzerinde; TeaStore referans mikroservis uygulamasıyla da gösterilmiş.
- Veri yolu: OpenTelemetry uyumlu trace → Collector (gRPC) → Kafka → backend → frontend. Trace'te metodun sınıfı varsa paket yapısı yalnız trace'ten çıkarılabiliyor. ([Kieker→OTel](https://arxiv.org/pdf/2411.07982))
- Ölçek için: anlamsal yakınlaştırma ve mini harita ([arXiv 2510.00003](https://arxiv.org/html/2510.00003)), ısı haritası kaplaması ([arXiv 2109.14217](https://arxiv.org/pdf/2109.14217)).

**Çıkarım:** ExplorViz'i kurmak yerine onun görsel dilini (bina + kavisli çağrı okları + zaman penceresi) kendi hafif demomuzda kullanmak daha hızlı ve bize ait.

## 2. Statik analiz: servisler arası çağrıyı koddan bulmak
Ortak desen üç adım ([Codebase-Memory, arXiv 2603.27277](https://arxiv.org/pdf/2603.27277); [MDPI 2024](https://www.mdpi.com/2076-3417/14/22/10725); [Neo4j](https://neo4j.com/blog/nodes/fixing-microservices-architecture-graphconnect/)):
1. Endpoint tanımlarını çıkar (framework'e özgü tree-sitter sorgusu ya da AST: route dekoratörleri, `@GetMapping`…).
2. İstemci çağrılarını çıkar (`requests`/`fetch`/`axios`/Feign…).
3. Normalize edilmiş **yol + HTTP metodu** ile eşle → servis→servis kenarı.
- Bizim demoda servisler Python olursa stdlib `ast` yeterli: bağımlılık yok.

## 3. Dinamik analiz (isteğe bağlı)
- OpenTelemetry trace'lerinden servis bağımlılık grafiği; Jaeger DAG ve kuvvet yönlü görünüm çağrı sayısını gösterir. ([Better Stack rehberi](https://betterstack.com/community/guides/observability/opentelemetry-demo/))
- Demo için daha basit yol: her servis gelen/giden çağrıyı tek bir olay akışına (SSE) yazar, görselleştirici canlı çizer.

## 4. Tarayıcıda çizim
- Three.js / react-three-fiber (MIT). JSCity: AST'den fonksiyon verisi → şehir ızgarası → r3f render ([yazı](https://peaonunes.com/blog/jscity-visualizing-javascript-code-5cej)). git-city (5,7k yıldız) aynı yığınla. ([r3f](https://github.com/pmndrs/react-three-fiber))
- Demo için: tek HTML + CDN'den Three.js, derleme adımı yok.

## 5. Hazır mikroservis örnekleri
- OpenTelemetry Demo (Astronomy Shop): 10+ servis, 12 dil, gRPC+HTTP, Kafka; 6 GB RAM, 14 GB disk ([docs](https://opentelemetry.io/docs/demo/docker-deployment/)). **VM için ağır** (7,8 GB RAM).
- Online Boutique, TeaStore, Sock Shop: hepsi 3-4 servisten büyük.
- **Karar önerisi:** kendi küçük 4 servisimizi yazmak (kontrol bizde, hafif, görselleştirmeye uygun isimli kod).

## 6. Önerilen demo mimarisi
```
demo/services/{gateway,orders,inventory,payments}/app.py   (Python stdlib http.server, docker yok)
        │  statik: analyze.py (stdlib ast) → model.json
        │     servis → mahalle, modül/sınıf → bina, fonksiyon → kat
        │     yükseklik = fonksiyon sayısı, taban = LOC, renk = karmaşıklık/sağlık
        │     kenar = HTTP route ↔ istemci çağrısı eşlemesi
        │  dinamik: her servis çağrıyı /events (SSE) akışına yazar
        ▼
demo/viz/index.html (Three.js): şehir + kavisli çağrı okları (ExplorViz),
   tıkla → bağlamsal panel (Luma), hata → kırmızı bina
```
