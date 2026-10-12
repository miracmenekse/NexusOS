# NexusOS → Ar-Ge görselleştirme projesi: sunum verisi

Bakım: `nexusos-sunum` skill'i. Panel: https://claude.ai/artifact/DDmawF2kHNmhvE18LPrpbJ

## 1. Hikâye

1. **Kıvılcım:** NexusOS, Metaverse dersinde (Doç. Dr. Murat Yılmaz) doğan, TÜBİTAK 1002-A'ya yazılan "VR'da yazılım geliştirme" fikri.
2. **Problem:** Yazılım, dağıtık servisler ve agent'lar görünmez; geliştirici 2B ekranda bağlam kaybediyor, bilişsel yük artıyor.
3. **Yön:** VR değil; dijital ikiz, görsellik, konuşarak ve dokunarak, az tuşla etkileşim. Ar-Ge projesinin yeni çıktıları.
4. **Dünyada ne var:** üç ayrı görsel dil (kod mekânı, akan trafik, yaşayan agent'lar); üçünü birleştiren yok.
5. **Çıktılarımız:** Ç1 Kod mekânı · Ç2 Servis trafiği · Ç3 Yaşayan agent'lar (ayrı ayrı demolar).
6. **Demo:** 3-4 mikroservisli örnek sistem; Ç1 Neon kod şehri (ExplorViz ile başlandı, kendi hafif görünümümüze geçildi), Ç2 akan trafik, Ç3 agent görünümleri.
7. **Sonraki adımlar:** Ç3 için yeniden kullanılabilir agent görselleştirme altlığı, Neon şehri gerçek koda bağlama, Ar-Ge projesine bağlanma. Ses + dokunma katmanı daha sonra (d20).

## 2. Kayıtlar

### 2026-10-11 · Dağınık bilgi tek yerde
- **Ne:** Drive, NotebookLM, Manus ve video kaynakları toplandı; 28 dosyadan 176 düğümlü bilgi grafiği çıktı.
- **Neden önemli:** Projeye dair her soru kaynak göstererek cevaplanabiliyor.
- **Kanıt:** `~/NexusOS/graphify-out/graph.html`, `kaynaklar/`
- **Sunumda:** 1. Kıvılcım; "nereden başladık" slaytı (grafik görseli).
- **İz:** WBS 2.1, 2.2, 2.3, 2.5

### 2026-10-11 · Esin videosu: "Zero Cognitive Load"
- **Ne:** Luma demo videosu okundu: kırmızı modül → dokun → analiz paneli → "Go to Error" → onarım; tuş yok.
- **Neden önemli:** Hedeflediğimiz etkileşim akışının ilk görsel taslağı.
- **Kanıt:** `kaynaklar/drive/video/demo sahneler.md`, `kaynaklar/drive/video/NexusOS Luma - kareler *.jpg`
- **Sunumda:** 1. Kıvılcım / 3. Yön; kısa video ya da kare dizisi.
- **İz:** d9

### 2026-10-11 · Yön değişikliği: VR yok, dijital ikiz + ses/dokunma
- **Ne:** NexusOS esin kaynağına dönüştü; hedef şirket Ar-Ge projesinin yeni çıktıları.
- **Neden önemli:** Donanım bağımlılığı kalktı; demo tarayıcıda çalışabilir.
- **Kanıt:** panel `charter`, karar d10, d12
- **Sunumda:** 3. Yön.
- **İz:** d10, d12

### 2026-10-11 · Pazar boşluğu bulundu
- **Ne:** ~20 referans tarandı (agent, dijital ikiz, ses-dokunma arayüzleri). Kod + agent + dijital ikizi tek canlı görünümde, ses ve dokunmayla gösteren araç yok.
- **Neden önemli:** Ar-Ge'nin özgün değeri.
- **Kanıt:** `kaynaklar/referans/2026-10-11-referans-taramasi.md`
- **Sunumda:** 4. Dünyada ne var.
- **İz:** WBS 3.2

### 2026-10-11 · Altlık seçildi: ExplorViz
- **Ne:** ExplorViz'in React/three.js arayüzü + backend-mock ile kod şehri, servisler arası çağrı okları ve YZ sohbeti hazır geliyor; Kafka/Java olmadan çalışıyor.
- **Neden önemli:** Sıfırdan yazmak yerine haftalar kazanıyoruz; biz yalnız veri üretip kendi katmanımızı ekliyoruz.
- **Kanıt:** `kaynaklar/referans/2026-10-11-altlik-repolari.md`
- **Sunumda:** 6. Demo; "nasıl hızlandık".
- **İz:** WBS 6.1

### 2026-10-11 · Üç görsel dil, üç ayrı çıktı
- **Ne:** Örnekler üç gruba ayrıldı: kod mekânı (CodeCharta, SEE, ExplorViz), akan trafik (Vizceral), yaşayan agent'lar (AI Town, agent-flow, deskrpg). Karar: üçü ayrı çıktı olarak yapılacak.
- **Neden önemli:** Ar-Ge projesinin farklı çıktıları netleşti; her biri tek başına gösterilebilir.
- **Kanıt:** `kaynaklar/referans/2026-10-11-gorsel-ui-ornekleri.md`
- **Sunumda:** 4 → 5 geçişi; üç sütunlu karşılaştırma slaytı.
- **İz:** d15, WBS 6.3–6.5

### 2026-10-11 · Altlık çalıştı, kendi 4 servisimiz şehirde
- **Ne:** ExplorViz VM'de Docker'sız ayağa kalktı; 4 Python mikroservisi (gateway, orders, inventory, payments) yazıldı, `analyze.py` koddan ve canlı trafikten şehir verisini üretiyor: 11 dosya, 10 kenar, 3 servisler arası çağrı.
- **Neden önemli:** Uçtan uca hat kuruldu: kod → analiz → 3B şehir. Bundan sonrası görsel/etkileşim katmanı.
- **Kanıt:** `demo/run.sh`, `demo/analyze.py`, `gorseller/2026-10-11-c1-ilk-sehir.png`, `gorseller/2026-10-11-explorviz-kieker.png`
- **Sunumda:** 6. Demo; "ilk şehir" slaytı.
- **İz:** WBS 6.2

### 2026-10-11 · Sorunlu servis kendiliğinden kırmızı, veri canlı
- **Ne:** Bina yüksekliği = satır sayısı; başarısız çağrılar (stok yok, ödeme reddi) ısı haritasında varsayılan kırmızı. `run.sh` her çalıştığında şehir yeniden başlatmadan güncelleniyor.
- **Neden önemli:** Kullanıcı hiçbir ayara dokunmadan "sorun nerede" sorusunun cevabını görüyor (Luma'daki kırmızı küp fikrinin ilk gerçek hâli).
- **Kanıt:** `gorseller/2026-10-11-c1-heatmap.png`
- **Sunumda:** 6. Demo.
- **İz:** WBS 6.3

### 2026-10-11 · Dokun → neden bozuk → koda git
- **Ne:** Kırmızı binaya dokununca panel: kaç çağrı başarısız, hangi servisten, son hata, "Go to Error" ile hatanın oluştuğu fonksiyonun kodu (dosya:satır).
- **Neden önemli:** Luma videosundaki "kırmızı modül → panel → Go to Error" akışı gerçek kodla çalışıyor; tek tıkla sorundan koda.
- **Kanıt:** `gorseller/2026-10-11-c1-go-to-error.png`, `gorseller/2026-10-11-c1-sehir-yakin.png`
- **Sunumda:** 6. Demo; esin videosu ile yan yana "konseptten gerçeğe" slaytı.
- **İz:** WBS 6.3

### 2026-10-11 · Ç2 servis trafiği canlı
- **Ne:** Servisler daire, her çağrı akan bir ışık; başarısız çağrı kırmızı nokta, sorun yaşayan servis kırmızı nabız atıyor. Dokununca: kaç çağrı, kimden, ort. süre, son hata. Sürekli trafik üreteci ile kendi kendine yaşıyor.
- **Neden önemli:** "Sistem şu an nasıl?" sorusuna tek bakışta cevap; Netflix Vizceral fikri, kendi servislerimizle ve bağımlılıksız (tek HTML + stdlib Python).
- **Kanıt:** `demo/traffic/` (`bash run.sh` → http://localhost:4400), `gorseller/2026-10-11-c2-trafik.png`
- **Sunumda:** 5. Çıktılarımız (Ç2) + 6. Demo; canlı gösterim.
- **İz:** WBS 6.4

### 2026-10-11 · Ç3 yaşayan agent'lar: bu projenin kendi kaydı
- **Ne:** Claude Code oturum kayıtları (ana agent + 2 alt agent, 478 olay) bir ofis sahnesine dönüşüyor: agent'lar araç kullandıkça istasyonlara (terminal, dosyalar, web, drive, panel) yürüyor, konuşma balonu çıkarıyor; alt agent doğuyor, işi bitince ana agent'a rapor verip ayrılıyor. Oynat / 4× / 16× / zaman çizelgesi.
- **Neden önemli:** Agent'ların görünmez işi insan sezgisiyle okunuyor; ve demo verisi bu Ar-Ge'nin kendisi (projeyi yapan agent'ları izliyoruz).
- **Kanıt:** `demo/agents/` (`bash run.sh` → http://localhost:4500), `gorseller/2026-10-11-c3-agentlar.png`
- **Sunumda:** 5. Çıktılarımız (Ç3) + 6. Demo; açılış ya da kapanış gösterimi.
- **İz:** WBS 6.5

### 2026-10-11 · Ç3 senaryosu: telekom satış agent'ları
- **Ne:** 6 agent bir aboneyi elde tutmaya çalışıyor: orkestratör ekibi kuruyor; analiz CRM'i, teklif tarife kataloğunu, kampanya indirimi (marj sınırıyla), risk kredi skorunu, sözleşme e-imzayı yönetiyor. Müşteri profili rastgele; bazı senaryolar satışla, bazıları "geri arama planlandı" ile bitiyor.
- **Neden önemli:** Agent'ların iş bölümü, birbirine görev ve rapor geçişi bir iş senaryosu üzerinden okunuyor; telekom müşterisine doğrudan anlatılabilir.
- **Kanıt:** `demo/agents/telekom.py`, `run-telekom.sh` → http://localhost:4500/?data=telekom.json, `gorseller/2026-10-11-c3-telekom.png`
- **Sunumda:** 5 → 6; iş senaryosu demosu.
- **İz:** WBS 6.5, d16

### 2026-10-11 · Ç1 görsel dil seçildi: Neon / Luma + gruba yakınlaşma
- **Ne:** Üç kod şehri önerisinden A (karanlık sahne, parlayan cam binalar, akan ışık çizgileri) seçildi. Bir servise dokununca kamera önce gruba yakınlaşıyor, dosyalar etiketleniyor, hatanın hangi dosyada başladığı ve hangi dosyadan geldiği grubun içinde görünüyor.
- **Neden önemli:** "Sistem nerede bozuk?" sorusu iki adımda cevaplanıyor: hangi servis, sonra hangi dosya. Esin videosuna (Luma) en yakın görsel dil.
- **Kanıt:** `demo/tasarim/index.html` (A kartı, `python3 -m http.server 4600 --directory demo/tasarim`), önceki öneri görseli `gorseller/2026-10-11-gorunum-onerileri.png`. İlk sürümde veri sabitti; artık canlı trafiğe bağlı (`bash demo/traffic/run.sh` → http://localhost:4400/sehir). Dosya listesi ve hata satırı hâlâ sabit (WBS 6.6).
- **Sunumda:** 5. Çıktılarımız (Ç1) + 6. Demo; yakınlaşma gösterimi.
- **İz:** WBS 6.3, d17

### 2026-10-11 · Neon şehirde hata görüntüleme
- **Ne:** Bir dosya hata vermeye başlayınca sağ üstte uyarı kartı çıkıyor (dosya, uç nokta, çağıran dosya → servis); hatalı dosya ve onu çağıran dosya grubun içinde işaretleniyor.
- **Neden önemli:** Sorun, kullanıcı aramadan önüne geliyor; Luma'daki "kırmızı modül" akışının canlı hâli.
- **Kanıt:** `demo/tasarim/index.html`, `bash demo/traffic/run.sh` → http://localhost:4400/sehir
- **Sunumda:** 6. Demo.
- **İz:** WBS 6.9, d17

### 2026-10-11 · Ç3 için beş agent görünümü
- **Ne:** Telekom senaryosu beş görünümde oynatılıyor: sprite ofis (pixel-agents görselleri), çizim ofis, kasaba (düz/izometrik/neon), kristal küpler, ağ grafiği (durum halkası, nabız, iş kartları).
- **Neden önemli:** Aynı agent verisinin farklı görsel dillerle okunabildiğini gösteriyor; altlık fikrinin çıkış noktası.
- **Kanıt:** Pano → Demolar (panoda çalışıyor), `demo/agents/*.html`, `kaynaklar/referans/2026-10-11-agent-arayuz-ornekleri.md`
- **Sunumda:** 5. Çıktılarımız (Ç3); yan yana karşılaştırma.
- **İz:** WBS 6.8, d19

### 2026-10-12 · Karar turu: Neon, altlık, ses/dokunma sonra
- **Ne:** Ç1 Neon şehirle devam ediyor (ExplorViz referans). Ç3'te sprite ofis ve ağ görünümü örnek olarak kalıyor; asıl hedef agent görselleştirme altlığı. Ses ve dokunma ertelendi.
- **Neden önemli:** Üç çıktının yönü netleşti; Ç3 tek bir görünüm değil, farklı görünümlerin üzerine kurulacağı bir altlık.
- **Kanıt:** panel `decisions` d18–d21, Pano → Şu an
- **Sunumda:** 7. Sonraki adımlar.
- **İz:** d18, d19, d20

## 3. Referans projeler

| Proje | ★ / lisans / son (2026-10-11) | Ne aldık | Çıktı |
|---|---|---|---|
| [ExplorViz](https://github.com/ExplorViz/frontend) | 6 / MIT? / 2026-10 | Altlık: web kod şehri, servisler arası çağrı okları, CopilotKit sohbet | Ç1, Ç2 |
| [CodeCharta](https://github.com/MaibornWolff/codecharta) | 546 / BSD-3 / 2026-10 | Metrik şehir + Domain (kelime bulutu) görünümü, görünümler arası geçiş | Ç1 |
| [SEE](https://github.com/uni-bremen-agst/SEE) | 29 / MIT / 2026-10 | Çok kullanıcılı, avatarlı kod mekânı (metaverse'e en yakın) | Ç1 |
| [Netflix Vizceral](https://github.com/Netflix/vizceral) | 4.099 / Apache-2.0 / 2023 | Servisler arası akan parçacıklar, hata rengi, içine dalma | Ç2 |
| [AI Town](https://github.com/a16z-infra/ai-town) | 10.616 / MIT / 2026-08 | Karakterler yan yana gelince konuşur, konuşma balonu + geçmiş | Ç3 |
| [agent-flow](https://github.com/patoles/agent-flow) | 1.694 / Apache-2.0 / 2026-10 | Fütüristik canlı agent grafiği: düşünme, dallanma, araç çağrıları, zaman çizelgesi | Ç3 |
| [deskrpg](https://github.com/dandacompany/deskrpg) | 166 / Sustainable Use / 2026-10 | 3B ofis: masada çalışan agent'lar, toplantı modu, kanban, cron | Ç3 |
| [Pixel Agents](https://github.com/pixel-agents-hq/pixel-agents) | 9.643 / MIT / 2026-10 | Claude Code agent'ları piksel ofiste; kayıt dosyasından canlı | Ç3 |

## 4. Rakamlar

| Rakam | Kaynak |
|---|---|
| 96 literatür kaynağı | `kaynaklar/notebooklm/notebooklm1.md` |
| 6 rakip VR/web IDE'nin hiçbirinde AST tabanlı kod görselleştirme yok | `kaynaklar/manus/Rekabet Analizi - Detaylı Araştırma.md` |
| LLM destekli pencere yönetimi (DuoZone, N=16): görev %34,5 daha hızlı, bilişsel yük (NASA-TLX) ~1/3 daha düşük. Taslaktaki "%34 bilişsel yük" ifadesi yanlış birleştirilmiş | `kaynaklar/notebooklm/2026-10-11-ses-dokunma-hci.md` (Qian vd. 2025, §7.1, §8.1) |
| Bilgi grafiği: 176 düğüm, 343 kenar, 12 topluluk | `graphify-out/GRAPH_REPORT.md` |

## 5. Görseller

| Yol | Açıklama |
|---|---|
| `kaynaklar/drive/video/NexusOS Luma - kareler 00-17s.jpg` | Luma esin videosu, hata akışı |
| `kaynaklar/drive/video/NexusOS Luma - kareler 20-32s.jpg` | Kod şehri uçuşu, onarım, "Zero Cognitive Load" |
| `sunum/gorseller/2026-10-11-c1-ilk-sehir.png` | Kendi 4 servisimizin ilk kod şehri |
| `sunum/gorseller/2026-10-11-explorviz-kieker.png` | ExplorViz altlığı, Kieker örneği |
| `graphify-out/graph.html` | Bilgi grafiği (ekran görüntüsü alınacak) |

## 6. Dikkat

- **deskrpg** "Sustainable Use License": yalnız iç iş kullanımı / ticari olmayan kullanım; ticari ürüne altlık olamaz, esin ve iç demo olabilir.
- **ExplorViz frontend** lisansı package.json'da MIT, kökte LICENSE yok; ürünleşmeden önce teyit (risk r8).
- Şirket Ar-Ge projesi (Rovo) bilgisi sunuma `[gizli]` ayıklanmadan girmez.
- Ç3 demosu oturum kaydındaki kullanıcı mesajlarını ve komut özetlerini gösterir; sunumdan önce oynatılacak oturumu gözden geçir (iç bilgi, kişi adı).
- **Sprite görselleri** (`demo/agents/px/`): pixel-agents deposu MIT ama görsellerin kökeni (YZ üretimi?) belirsiz; ticari kullanımdan önce netleştirilmeli (r10).
- Luma/Kling videoları YZ üretimi; "ürün görüntüsü" diye sunulmaz, "esin/konsept" diye sunulur.
