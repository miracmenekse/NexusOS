<!-- Kaynak: Google Drive | NexusOS Luma Vdeio.mp4 | https://drive.google.com/file/d/1KQHhu5lc4_vmq7Em8AVL1mUQXbYonzow/view | sürükle-bırak 2026-10-11 -->

# NexusOS demo videosu (Luma): sahne dökümü

35,3 sn, 1280x720, 24 fps, **sessiz** (ses kanalı yok). Kamera neredeyse kesintisiz akıyor; tek sert kesme
20,5. saniyede. Kareler 2,5 sn arayla çıkarıldı: "NexusOS Luma - kareler 00-17s.jpg" ve "… 20-32s.jpg".

## Sahneler

| # | Zaman | Görüntü |
|---|---|---|
| 1 | 0–2,5 sn | Karanlık bir sanal mekânda zeminde modül blokları. Üstte üç etiketli küp: CRM'lerden biri **kırmızı** ve üstünde uyarı üçgeni, diğerleri yeşil ve mavi. Aralarından ışık hatları (veri akışı) geçiyor. |
| 2 | 2,5–7,5 sn | Kamera kod uzayına dalıyor: ızgara zemin üzerinde süzülen yarı saydam mavi/yeşil kod küpleri, içlerinde kod satırları. Ortada tek kırmızı küp. Geliştiricinin eli (el takibi) küpe uzanıyor; küpün etrafında hedef halkası beliriyor, yukarıdan ışık huzmesi iniyor (seçim). |
| 3 | 7,5–15 sn | Seçili kırmızı küpün yanında büyük, yarı saydam bir kod paneli açılıyor: kod satırları, ortada dönen analiz göstergesi. Panelde "Analyzing Codebase…" yazıyor. |
| 4 | 15–20,5 sn | Kod duvarlarından oluşan bir koridor; parmak **"Go to Error ▶"** düğmesine basıyor. Kamera ışık noktasına doğru hızlanıyor. |
| 5 | 20,5–27 sn | (Kesme) Işık hatlarıyla dolu bir **kod şehri** üzerinde hızla uçuş; ufukta binalar, birinin üstünde yeşil **"PCM"** yazısı (hatalı modül). |
| 6 | 27–32 sn | Karanlık bir salonda kaide üzerinde kalkan simgeli küp: önce turuncu (uyarı), sonra yeşil parçacık patlamasıyla **mavi küpe** dönüşüyor (güvenlik açığı giderildi). Etrafında bilgi panelleri. |
| 7 | 32–35 sn | Geniş çekim: ufukta sıra sıra modül blokları; üstte yazı: **"NexusOS: Zero Cognitive Load"**. |

## NexusOS ile eşleşme

| Videoda | NexusOS bileşeni / senaryo ("NexusOS: Video-bağlam&senaryo" dokümanı) |
|---|---|
| Modüller süzülen kod küpleri, ışık hatları bağımlılık | AST'den 3B kod küpleri |
| Kırmızı küp + uyarı, kalkan simgeli küp onarılıyor | Senaryo 1: SAST ile hata ayıklama (SecCityVR) |
| "Analyzing Codebase…", "Go to Error" paneli | Senaryo 8: dinamik HUD |
| Kod şehri üzerinde uçuş, hatalı modüle gidiş | Şehir Metaforu, Senaryo 4: yazılım arkeolojisi |
| El ile seçim, hedef halkası | VR-özgü doğrudan manipülasyon (el takibi) |
| Kapanış: "Zero Cognitive Load" | Senaryo 5: bilişsel yük yönetimi |

## Yeni Ar-Ge projesine taşınacaklar (d10: VR yok, dijital ikiz + ses/dokunma)

Luma ana referans video. VR ortamı alınmıyor; görsel dil ve etkileşim akışı alınıyor:
- **Hata akışı tek bakışta:** kırmızı modül → seçim → analiz paneli → "Go to Error" → onarım (kırmızıdan maviye). Tuş yok; dokunma ile ilerliyor. 2B/dijital ikiz arayüzde aynı akış kurulabilir.
- **İki ölçek:** yakında süzülen kod küpleri (modül içi), uzakta kod şehri (sistem geneli). Dijital ikiz görünümünde yakınlaştırma seviyeleri olarak karşılığı var.
- **Bağlamsal panel:** panel yalnız seçimde açılıyor (HUD fikri), sabit pencere yok.
- **Eksik olan:** ses yok, agent yok. Yeni projede agentların birbiriyle konuşması ve sesle komut bu akışa eklenecek parçalar.
