# NexusOS → Ar-Ge görselleştirme projesi: sunum verisi

Bakım: `nexusos-sunum` skill'i. Panel: https://claude.ai/artifact/DDmawF2kHNmhvE18LPrpbJ

## 1. Hikâye

> **Biçim (2026-10-13):** Slayt yok. Tüm sunum Manus vr-showcase mantığında tıklanabilir bir web sayfası; aşağıdaki bölümler sayfanın bölümleri.

1. **Kıvılcım:** NexusOS, Metaverse dersinde (Doç. Dr. Murat Yılmaz) doğan, TÜBİTAK 1002-A'ya yazılan "VR'da yazılım geliştirme" fikri.
2. **Problem:** Yazılım, dağıtık servisler ve agent'lar görünmez; geliştirici 2B ekranda bağlam kaybediyor, bilişsel yük artıyor.
3. **Yön:** VR değil; dijital ikiz, görsellik, konuşarak ve dokunarak, az tuşla etkileşim. Ar-Ge projesinin yeni çıktıları. Sayfada sekiz yetenek kartı, yönetici dilinde: iş değeri, çalışma mantığı, esin kaynağı (2026-10-14).
4. **Dünyada ne var:** üç ayrı görsel dil (kod mekânı, akan trafik, yaşayan agent'lar); üçünü birleştiren yok.
4b. **Showcase (Manus vr-showcase kart mantığı):** önce dünyadaki araştırma ve çözümler, sonra aynı kart biçiminde bizim Ç1/Ç2/Ç3 demolarımız. Kart: ad + tek cümle, ekran görüntüleri, hedef kitle, ne çözüyor, kaynak (yıl/yıldız/lisans ya da makale), konum. Rakip kartları §3 Referans projeler'den (ExplorViz, CodeCharta, SEE, Vizceral, AI Town, agent-flow, Pixel Agents, deskrpg) ve literatürden; görselleri toplanacak. Biçim örneği: `kaynaklar/manus/vr-showcase/`. Manus'un fon/haber satırları doğrulanmadan kullanılmaz.
5. **Çıktılarımız:** Ç1 Kod mekânı · Ç2 Servis trafiği · Ç3 Yaşayan agent'lar (ayrı ayrı demolar).
6. **Demo:** 3-4 mikroservisli örnek sistem; Ç1 Neon kod şehri (ExplorViz ile başlandı, kendi hafif görünümümüze geçildi), Ç2 akan trafik, Ç3 agent görünümleri.
7. **Sonraki adımlar:** konuşarak hata çözme demosu (conversational AI + DBeaver + kod görselleştirme; kullanıcı notu 2026-10-13), 5+5 kullanıcı testi, ses + dokunma katmanı (d20), Ç1 ile Ç3 aynı sahnede, şirket Ar-Ge projesine eşleme (Rovo, sayfada boş bölüm), lisans teyitleri, ölçek. (Altlık ve Neon-gerçek kod bitti.)

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
- **Kanıt:** `demo/tasarim/index.html` (A kartı, `python3 -m http.server 4600 --directory demo/tasarim`), önceki öneri görseli `gorseller/2026-10-11-gorunum-onerileri.png`. İlk sürümde veri sabitti; artık canlı trafiğe ve (2026-10-13) koda bağlı (`bash demo/run.sh` → http://localhost:4400/sehir).
- **Sunumda:** 5. Çıktılarımız (Ç1) + 6. Demo; yakınlaşma gösterimi.
- **İz:** WBS 6.3, d17

### 2026-10-11 · Neon şehirde hata görüntüleme
- **Ne:** Bir dosya hata vermeye başlayınca sağ üstte uyarı kartı çıkıyor (dosya, uç nokta, çağıran dosya → servis); hatalı dosya ve onu çağıran dosya grubun içinde işaretleniyor.
- **Neden önemli:** Sorun, kullanıcı aramadan önüne geliyor; Luma'daki "kırmızı modül" akışının canlı hâli.
- **Kanıt:** `demo/tasarim/index.html`, `bash demo/run.sh` → http://localhost:4400/sehir
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

### 2026-10-12 · Ç3 altlığı: aynı olay modeli, farklı kaynaklar, farklı görünümler
- **Ne:** Agent'ların ne yaptığı tek bir olay biçiminde tutuluyor (mesaj, araç, konuşma, sonuç). Sprite ofis ve ağ görünümü kim nerede, hangi renk, hangi araç bilgisini veriden çıkarıyor; telekom senaryosu (6 agent) ve bu projenin Claude Code oturumu (ana + 2 alt agent, 530 olay) aynı iki görünümde oynuyor.
- **Neden önemli:** Ç3 artık tek bir demo değil, altlık: yeni bir agent sistemi bağlamak için yalnız bir dönüştürücü yazmak yetiyor, görünümler değişmiyor.
- **Kanıt:** `demo/agents/altlik.py`, `gorseller/2026-10-12-c3-altlik-ag-oturum.png`, `gorseller/2026-10-12-c3-altlik-ofis-telekom.png`
- **Sunumda:** 5. Çıktılarımız (Ç3); iki kaynak × iki görünüm, 2×2 slayt.
- **İz:** WBS 6.10, d19, d22

### 2026-10-12 · Proje toplandı: git + tek komut
- **Ne:** Proje git'e alındı; tüm demolar `bash demo/run.sh` ile tek komutla açılıyor (2 port). ExplorViz ve seçilmeyen görünümler arşivde.
- **Neden önemli:** Demo gösterimi tek adım; ekip üyesi kurulumsuz çalıştırabilir.
- **Kanıt:** `demo/run.sh`, `demo/arsiv/`
- **Sunumda:** 6. Demo; "nasıl çalıştırılır" notu.
- **İz:** WBS 1.4

### 2026-10-13 · Neon şehir gerçek koddan: hatanın satırına kadar
- **Ne:** Şehrin binaları, yükseklikleri ve çağrı yayları artık `services/` kodundan okunuyor (Python ast); elle yazılmış liste kalmadı. Bir servis hata döndürünce ya da çökünce cevabın içinde hatayı üreten dosya:satır geliyor; "koda git" tam o satırı işaretliyor (ör. `stock.py:16`, "stok yetersiz").
- **Neden önemli:** Demo artık bir çizim değil, kodun dijital ikizi: kod değişince şehir değişir; "sorun nerede?" sorusu satır düzeyinde cevaplanıyor.
- **Kanıt:** `demo/traffic/yapi.py`, `demo/services/common/web.py` (`fail`), `gorseller/2026-10-13-c1-neon-koddan.png`, `gorseller/2026-10-13-c1-neon-gercek-satir.png`
- **Sunumda:** 6. Demo; esin videosundaki "Go to Error" ile yan yana.
- **İz:** WBS 6.6, d18

### 2026-10-13 · Konsept: yazılımın canlı dijital ikizi
- **Ne:** Konsept taslağı yazıldı: problem, dört kullanıcı tipi, üç çıktının karşılaştırması, 8 etkileşim ilkesi ("sorun kullanıcıya gelir", "iki dokunuşta satıra", "görülen her şeyin kaynağı vardır", "ses fiil, dokunma nesne"), özgünlük ve 5+5 kişilik doğrulama planı (SUS, NASA-TLX).
- **Neden önemli:** Demoların arkasındaki fikir tek sayfada; sunumun 2-5. bölümlerinin metni buradan çıkar.
- **Kanıt:** `konsept/4.2-konsept.md`
- **Sunumda:** 2. Problem, 3. Yön, 5. Çıktılarımız; ilkeler tek slayt.
- **İz:** WBS 4.2

### 2026-10-13 · Ç3 tamam: geri sarma, takılma, canlı izleme
- **Ne:** Agent ekibinin dört sorusunun hepsi görünümde cevaplanıyor. Zaman çizelgesiyle herhangi bir ana dönülüyor; agent'a dokununca rolü, durumu, kullandığı araçlar ve yaptıkları listeleniyor; bir bekleme zincirinin ucundaki agent 10 sn sessiz kalınca turuncu halka ve "kampanya 12 sn'dir sessiz · orkestratör → analiz → teklif → kampanya bekliyor" uyarısı çıkıyor. Çalışan bir Claude Code oturumu 1 sn gecikmeyle canlı izleniyor; agent bir servis dosyasını okuyunca Neon şehirde o bina mor parlıyor. Üçüncü kaynak olarak OpenTelemetry GenAI izleri modele çevriliyor.
- **Neden önemli:** Agent sistemi kuran ekip için "kim kimi bekliyor, nerede takıldı" sorusu kayıt dosyası okumadan cevaplanıyor; OpenTelemetry desteğiyle farklı agent çatıları aynı görünüme bağlanabiliyor. 15 agent / 2.000 olayda 61 fps.
- **Kanıt:** `demo/agents/altlik.js`, `canli.py`, `test-altlik.js`, `konsept/4.3-kapsam-gereksinim.md` (14/14 gereksinim), `gorseller/2026-10-13-c3-takilma-ag.png`, `gorseller/2026-10-13-c3-takilma-ofis.png`, `gorseller/2026-10-13-c3-canli-oturum.png`
- **Sunumda:** 5. Çıktılarımız (Ç3) + 6. Demo; canlı gösterimde projeyi yapan agent'ı izlemek (açılış ya da kapanış).
- **İz:** WBS 6.11, 6.12, 6.13, 6.14, d23

### 2026-10-13 · Ç1 geliştirici için: isteğin yolu, dosya ilişkileri, "düzeldi mi?"
- **Ne:** Her istek bir iz kimliği taşıyor; hatanın panelinde isteğin tüm yolu sırayla görünüyor (kullanıcı → gateway → orders → inventory, süreler; hatalı halka kırmızı). Bir binaya dokununca koddan okunan ilişkiler çiziliyor (kullandığı / onu kullanan dosyalar). Kod kaydedilince servis kendiliğinden yeniden başlıyor, şehir 2 sn içinde yeniden çiziliyor, değişen bina işaretleniyor; hatalı dosya düzeltildiyse bina yeşile dönüp "✓ düzeldi (53 çağrı temiz)" yazıyor. "VS Code'da aç" dosyayı hatalı satırda açıyor.
- **Neden önemli:** Geliştiricinin döngüsü (hatayı gör → yolunu izle → koda git → düzelt → düzeldiğini gör) tek ekranda kapanıyor; log ve editör arasında gidip gelmek yok.
- **Kanıt:** `demo/tasarim/index.html`, `demo/traffic/yapi.py`, `demo/services/common/web.py` (iz), `demo/services/calistir.py`, `gorseller/2026-10-13-c1-iz.png`, `gorseller/2026-10-13-c1-iliski.png`, `gorseller/2026-10-13-c1-duzeldi.png`
- **Sunumda:** 6. Demo; canlı gösterimde stock.py'yi düzeltip binanın yeşile dönmesi.
- **İz:** WBS 6.15, 6.16, d25

### 2026-10-13 · Ç2 operasyon için: sağlık, alarm, kök neden
- **Ne:** Servisler ve bağlantıları artık koddan geliyor. Üst bantta sistemin durumu (sağlıklı / dikkat / sorun) ve giriş servisinin istek/sn, hata %, p95'i; her servisin altında kendi değerleri, halkası seviye renginde. Bir servis 10 sn "sorun"da kalınca alarm açılıyor; kart kök nedeni ve etkilenen servisleri söylüyor ("payments · etkilenen: orders, gateway"), "kodda gör" Neon şehri o servise yakınlaşmış açıyor. Arıza düğmeleriyle servis yavaşlatılıp çökertilebiliyor; temizlenince alarm kapanıp geçmişe düşüyor. Servis panelinde son 5 dk eğrisi.
- **Neden önemli:** Operasyon için "sistem iyi mi, ne zamandır, asıl sorun nerede?" sorularının cevabı tek ekranda; Ç2 → Ç1 geçişiyle alarmdan koda iki dokunuş.
- **Kanıt:** `demo/traffic/index.html`, `demo/services/common/web.py` (arıza), `demo/traffic/server.py` (`/ariza`), `gorseller/2026-10-13-c2-alarm.png`, `gorseller/2026-10-13-c2-kapanan.png`
- **Sunumda:** 6. Demo; canlıda "payments yavaşlasın" → 10 sn sonra alarm, kök neden payments → temizle → alarm kapanır.
- **İz:** WBS 6.17, d26

### 2026-10-13 · Bayi satış asistanı: modern görünüm (2. alternatif)
- **Ne:** Aynı EtiyaCell bayi senaryosu üç panelli modern bir görünümle oynatılıyor: solda temsilcinin iPad'i (müşteri konuşması + asistan önerileri), ortada agent ekibi ağı (temsilci → orkestratör → 5 agent → kullandıkları sistemler, akan mesaj ışıkları), sağda adım adım dolan teklif kartı (510 → rakip 420 → liste 449, %11 indirim → 400 TL). Altta anlatıcı bandı her aşamayı bir cümleyle anlatıyor; sonda özet ekranı açılıyor. Aşamaya tıklayınca o ana atlanıyor.
- **Neden önemli:** Sahne yerine "ne oldu, neden, müşteriye ne kazandırdı" doğrudan okunuyor; telekom müşterisine/yöneticiye anlatmaya uygun. Tek model, çok görünüm ilkesinin bir kanıtı daha: aynı JSON, yeni sayfa.
- **Kanıt:** `demo/agents/bayi2.html`, `demo/agents/bayi-telekom.json` (giris/anlati/kart alanları), `gorseller/2026-10-13-c3-bayi2-modern.png`, `gorseller/2026-10-13-c3-bayi2-ozet.png`; vitrin "Bayi satış asistanı → Modern görünüm".
- **Sunumda:** 5. Bizim çözümlerimiz / Ç3 demo; canlıda oynat, "3. Teklif"e tıklayıp indirim kararını göster, sonda özet: 110 TL/ay tasarruf, rakipten 20 TL ucuz.
- **İz:** Ç3, bayi demosu alternatifi

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
| CodeCity: kontrollü deneyde (41 katılımcı) Eclipse + Excel'e göre %24 daha doğru, %12 daha hızlı | Wettel, Lanza, Robbes, ICSE 2011 |
| ExplorViz: Extravis'e göre %39–61 daha doğru, büyük sistemde %28 daha az süre | Fittkau vd., ICPC 2015 |
| SecCityVR: SUS 70'e 58,75; hayal kırıklığı (TLX) 17,5'e 52,5; görev süresi daha uzun (17 katılımcı) | arXiv:2504.18238 |
| DuoZone: %34,5 daha hızlı; uygulama önerilerinin %90+'ı, düzen önerilerinin %82,8'i kabul (16 uzman) | arXiv:2511.15676 |
| Generative Agents (AI Town'ın esin kaynağı): %1,3 halüsinasyon, ağ yoğunluğu 0,17 → 0,74 | Park vd., UIST 2023 |
| Bilgi grafiği: 176 düğüm, 343 kenar, 12 topluluk | `graphify-out/GRAPH_REPORT.md` |

## 5. Görseller

| Yol | Açıklama |
|---|---|
| `kaynaklar/drive/video/NexusOS Luma - kareler 00-17s.jpg` | Luma esin videosu, hata akışı |
| `kaynaklar/drive/video/NexusOS Luma - kareler 20-32s.jpg` | Kod şehri uçuşu, onarım, "Zero Cognitive Load" |
| `sunum/gorseller/2026-10-11-c1-ilk-sehir.png` | Kendi 4 servisimizin ilk kod şehri |
| `sunum/gorseller/2026-10-11-explorviz-kieker.png` | ExplorViz altlığı, Kieker örneği |
| `sunum/gorseller/2026-10-12-c3-altlik-ag-oturum.png` | Ç3 altlığı: ağ görünümü, Claude Code oturumu (ana + 2 alt agent) |
| `sunum/gorseller/2026-10-12-c3-altlik-ofis-telekom.png` | Ç3 altlığı: sprite ofis, telekom senaryosu |
| `sunum/gorseller/2026-10-13-c1-neon-koddan.png` | Ç1 Neon şehir: koddan okunan yapı, iki dosya canlı hatada |
| `sunum/gorseller/2026-10-13-c1-neon-gercek-satir.png` | Ç1 "koda git": hatayı döndüren satır (stock.py:16) işaretli |
| `sunum/gorseller/2026-10-13-c1-iz.png` | Ç1: hata paneli, isteğin uçtan uca yolu ve VS Code bağlantısı |
| `sunum/gorseller/2026-10-13-c1-iliski.png` | Ç1: order_handler.py'nin koddan okunan ilişkileri |
| `sunum/gorseller/2026-10-13-c1-duzeldi.png` | Ç1: stock.py düzeltildi, bina yeşil, "✓ düzeldi" |
| `sunum/gorseller/2026-10-13-c2-alarm.png` | Ç2: inventory alarmı, sağlık bandı, servis paneli ve 5 dk eğrisi |
| `sunum/gorseller/2026-10-13-c2-kapanan.png` | Ç2: arıza temizlendi, kapanan alarm geçmişi |
| `sunum/gorseller/2026-10-13-c3-takilma-ag.png` | Ç3 ağ: takılma uyarısı ve kampanya ayrıntı paneli |
| `sunum/gorseller/2026-10-13-c3-takilma-ofis.png` | Ç3 ofis: agent şeridi, takılma uyarısı, turuncu halka |
| `sunum/gorseller/2026-10-13-c3-canli-oturum.png` | Ç3 canlı: bu Claude Code oturumu ofiste (iç bilgi içerir, ayıklanmadan kullanma) |
| `sunum/gorseller/2026-10-13-c3-bayi2-modern.png` | Ç3 bayi modern görünüm: iPad, agent ağı, dolan teklif kartı |
| `sunum/gorseller/2026-10-13-c3-bayi2-ozet.png` | Ç3 bayi modern görünüm: satış özeti (tasarruf, süre, agent sayısı) |
| `graphify-out/graph.html` | Bilgi grafiği (ekran görüntüsü alınacak) |

## 6. Dikkat

- **deskrpg** "Sustainable Use License": yalnız iç iş kullanımı / ticari olmayan kullanım; ticari ürüne altlık olamaz, esin ve iç demo olabilir.
- **ExplorViz frontend** lisansı package.json'da MIT, kökte LICENSE yok; ürünleşmeden önce teyit (risk r8).
- Şirket Ar-Ge projesi (Rovo) bilgisi sunuma `[gizli]` ayıklanmadan girmez.
- Ç3 oturum görünümü (`oturum.json`) araç çağrılarında Drive klasör kimliği gibi iç bilgi gösteriyor; sunumdan önce ayıkla.
- `ornek-otel.json` uydurma bir izdir (dönüştürücü sınaması); gerçek sistem verisi diye sunulmaz.
- Ç3 demosu oturum kaydındaki kullanıcı mesajlarını ve komut özetlerini gösterir; sunumdan önce oynatılacak oturumu gözden geçir (iç bilgi, kişi adı).
- **Sprite görselleri** (`demo/agents/px/`): pixel-agents deposu MIT ama görsellerin kökeni (YZ üretimi?) belirsiz; ticari kullanımdan önce netleştirilmeli (r10).
- Luma/Kling videoları YZ üretimi; "ürün görüntüsü" diye sunulmaz, "esin/konsept" diye sunulur.

### 2026-10-13 · Sunum biçimi: tıklanabilir showcase sayfası
- **Ne:** Slayt yok; sunum Manus vr-showcase mantığında bir web sayfası. Önce dünyadaki araştırma ve çözümler kart kart, sonra aynı biçimde Ç1/Ç2/Ç3. 8 referans projenin ekran görüntüleri README'lerinden indirildi (ExplorViz için kendi kurulum görüntümüz).
- **Neden önemli:** Dinleyici her çözümü tıklayıp inceleyebiliyor; bizim demolar rakiplerle aynı çerçevede karşılaştırılıyor.
- **Kanıt:** `gorseller/referans/*.png`, `kaynaklar/manus/vr-showcase/`
- **Sunumda:** 4b. Showcase.
- **İz:** kullanıcı kararı

### 2026-10-13 · Sunum sayfası ön çalışması yayında
- **Ne:** Mentör sunumunun ilk sürümü: https://claude.ai/artifact/PVNuXaTyBDeHLNMKQX4eGD. Kıvılcım → Problem → Yön (8 ilke) → Dünyada ne var (12 kart: 8 araç + 4 araştırma, filtreli) → Bizim çözümlerimiz (Ç1/Ç2/Ç3 kartları, 7 canlı demo düğmesi) → Şirket Ar-Ge (boş, "sonradan yapılacaktır") → Sonraki adımlar.
- **Neden önemli:** Sunumun kendisi; demolar panodaki tarayıcı içi simülasyonla sayfanın içinde çalışıyor.
- **Kanıt:** `sunum/web/index.html` (yayın `files` haritası: img/ yerelden, demo/ panodan)
- **Sunumda:** tümü.
- **İz:** kullanıcı kararı (dinleyici: şirket içi Ar-Ge mentörleri)

### 2026-10-13 · Sunum sayfası 2. sürüm: sayfa sayfa, araştırma kartları, VR sekmesi
- **Ne:** Solda içindekiler paneli, her bölüm tam ekran bir sayfa, kaydırınca sonraki sayfaya geçiyor. Kıvılcım'da Luma videosu doğrudan oynatılıyor. ExplorViz kartında kendi şehrimizin ExplorViz görüntüsü ve mimari görseli var. Araştırma kartları amaç / literatüre katkı / çıktı / performans / teknoloji alanlarıyla (SecCityVR, DuoZone, Saktheeswaran vd. 2020, Hey Dashboard!, CodeCity; arXiv özetlerinden). Yeni sekme "VR çalışma alanları": Manus'un 6 ürünü kendi biçimiyle (fon, pazar ve haberler "doğrulanmamış" etiketli). Demo kartlarında "Nasıl kullanılır" adımları, demo açıkken üst bantta da görünüyor. 3. sürüm: 4. kart EtiyaCell bayi satış asistanı (`demo/agents/bayi.html`); demolar ekrana sığacak şekilde küçültülüyor, demo düğmeleri kartın üstünde sabit.
- **Neden önemli:** Mentörler her bölümü ayrı bir sayfa gibi geziyor; araştırmalar karşılaştırılabilir biçimde.
- **Kanıt:** `sunum/web/index.html`, `sunum/web/manus.json`, `sunum/web/medya/luma.mp4`
- **Sunumda:** tümü.
- **İz:** kullanıcı geri bildirimi

### 2026-10-14 · Yön bölümü yönetici diliyle: 8 yetenek kartı + giriş diyagramı
- **Ne:** "3 · Yön" sekiz yetenek kartına dönüştü (sorun kendini gösterir, alarmdan koda iki dokunuş, gördüğünüz her şey gerçektir, tek veri her role kendi ekranı, konuşarak ve dokunarak sorma, sesin sessiz karşılığı, açıklama bakışı kapatmaz, klavyesiz kullanım). Her kartta bir görsel; karta basınca detay: yönetici için değeri, nasıl çalışıyor, nereden esinlendik (Vizceral, CodeCity, CodeCharta, ExplorViz, agent-flow, Pixel Agents, DuoZone, Saktheeswaran vd. 2020, Hey Dashboard!), nerede görülür. Altı kartta canlı demo düğmesi; ses kartları "sonraki aşama" etiketli, görseli konsept çizimi. Giriş görseli "üç kaynak → tek veri modeli → üç canlı görünüm" diyagramıyla değişti.
- **Neden önemli:** Yöneticiler özelliği iş sorusu olarak okuyor; her yetenek kaynağına ve çalışma mantığına bağlı. Ses yeteneklerinin henüz yapılmadığı açıkça yazılı.
- **Kanıt:** `sunum/web/index.html` (yeni görsel `img/c3-canli-oturum.png` = `gorseller/2026-10-13-c3-canli-oturum.png`)
- **Sunumda:** 1. Giriş, 3. Yön.
- **İz:** kullanıcı isteği
