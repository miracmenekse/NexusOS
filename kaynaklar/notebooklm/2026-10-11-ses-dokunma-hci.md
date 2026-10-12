# NotebookLM: ses, dokunma, bakış ve jest etkileşimi (HCI)

WBS 6.7 (ertelendi, d20). Kullanıcı NotebookLM'de çalıştırıp 2026-10-11'de yapıştırdı.

## Soru (Claude'un verdiği promptlar)

Kaldığımız yer: Ç1 kod şehri, Ç2 servis trafiği ve Ç3 agent ofisi (telekom senaryosu dahil) çalışıyor. Henüz dokunulmayan konular şunlar: ses ve dokunma odaklı HCI katmanı, üç çıktının tek arayüzde birleşmesi ve "%34" rakamının doğrulanması. Aşağıdaki promptlar bunlara göre hazırlandı, NotebookLM'e sırayla yapıştırabilirsin.

**1. Ses + dokunma etkileşimi**
```
Kaynaklardaki ses ve dokunma (haptik, jest, dokunmatik) tabanlı arayüz çalışmalarını tara. Bir yazılım sistemini (kod yapısı, servis trafiği, çalışan AI agent'lar) görselleştiren bir ekranı klavye ve fare olmadan kullanmak için hangi etkileşim kalıpları öneriliyor? Her kalıp için şunları ver: ne işe yaradığı, hangi kaynakta geçtiği, ölçülmüş bir faydası varsa rakamı ve VR gerektirip gerektirmediği. Tablo olarak yaz.
```

**2. Üç görünümün birleşmesi**
```
Bir yazılım sistemi üç görünümle gösteriliyor: kod şehri (yapı), servis trafiği (çalışma anı) ve agent ofisi (agent'ların ne yaptığı). Kaynaklarda bu tür çoklu görünümler arasında geçiş, yakınlaşma ve bağlam koruma (semantic zoom, focus+context, linked views) için neler öneriliyor? Kullanıcının kaybolmadan görünümler arasında gezmesi için somut tasarım kurallarını kaynak göstererek listele.
```

**3. Bilişsel yük ve "%34" doğrulaması**
```
"LLM destekli pencere yönetimi bilişsel yükü %34'e varan oranda azaltıyor" iddiası hangi kaynakta geçiyor? Tam cümleyi, deney düzenini, katılımcı sayısını ve ölçüm yöntemini (NASA-TLX vb.) ver. Kaynaklarda bilişsel yükü ölçen başka çalışmalar varsa onları da yöntem ve sonuçlarıyla listele. Kaynakta olmayan hiçbir şeyi ekleme.
```

**4. Fütüristik arayüz için ses asistanı**
```
Bir görselleştirmeye doğal dille soru sorulup cevabın görsel olarak vurgulandığı çalışmaları bul (ör. "hangi servis yavaş?" sorusunda ilgili binanın ya da dairenin parlaması). Hangi mimariler kullanılmış, hangi hatalar ve sınırlar raporlanmış? Kısa bir karşılaştırma yaz.
```

**5. Değerlendirme planı**
```
Bu tür bir görselleştirme ve HCI prototipini kullanıcı çalışmasıyla değerlendirmek için kaynaklarda hangi görevler, metrikler ve katılımcı sayıları kullanılmış? Küçük bir ekiple (5–10 kişi) uygulanabilecek bir değerlendirme planı öner ve her adımı bir kaynağa bağla.
```

**6. Boşluk analizi**
```
Kaynaklara göre ses ve dokunma odaklı, VR'sız bir yazılım ve agent görselleştirme arayüzünde henüz çözülmemiş 5 araştırma boşluğu nedir? Her biri için hangi kaynağın bu boşluğa işaret ettiğini ve neden yenilikçi bir katkı sayılacağını yaz.
```

Bunlardan bence önce 1 ile 3'ü çalıştır. 1 numaranın cevabı sıradaki demonun, yani ses ve dokunma katmanının yönünü belirler. 3 numara ise sunumdaki "doğrulanacak" etiketli rakamı netleştirir.

## Cevap (NotebookLM, olduğu gibi)

1.Yazılım sistemlerini (kod yapısı, servis trafiği, çalışan AI agent'lar) görselleştiren 3B uzamsal ekranların klavye ve fare olmadan kullanımı için kaynaklarda önerilen ses, dokunma (haptik, jest, dokunmatik), bakış (gaze) ve gövde hareketi tabanlı etkileşim kalıpları aşağıdaki tabloda özetlenmiştir.

---

### Klavyesiz ve Faresiz Etkileşim Kalıpları Tablosu

| Etkileşim Kalıbı | Ne İşe Yaradığı / Amacı | Geçtiği Kaynak(lar) | Ölçülmüş Faydası / Rakamlar | VR Gerektirir mi? |
| :--- | :--- | :--- | :--- | :--- |
| **Sadece Sesli Komutlar (Speech-Only Commands)** | Menülere ihtiyaç duymadan servis veya sınıf adını söyleyerek bileşeni çağırma, görünürlüğü değiştirme ve anlamsal ışınlanma (örn. *"Take me to transformer T-2"* veya *"Take me to green bin"*). | *Architectural Evolution...*, *Analysis of Speech-Based Teleportation...*, *Identifying Usability Issues... (Getaviz)* | Bakışla hedeflemeye kıyasla beklenenin aksine **daha düşük bilişsel yük** üretmiştir. Ancak domain terimlerini hatırlama zorluğu nedeniyle hata oranı artabilmektedir. Getaviz AR (HoloLens) çalışmasında teknik olarak %100 çalışmasına karşın kullanıcıların genel bir direnç göstererek sesli komutu kullanmak istemediği belirlenmiştir. | **Hayır** (AR, MR, VR ve ekran tabanlı sistemlerde uygulanabilir). |
| **Ses + Bakış Füzyonu (Speech + Head/Eye-Gaze Fusion)** | Baş veya göz yönelimiyle nesneye odaklanıp ses komutuyla (*"Take me there"*, *"Teleport"*) işlemi tetikleme. Nesne adını hatırlama zorunluluğunu kaldırır ve *"Midas Touch"* problemini önler. | *Analysis of Speech-Based Teleportation...*, *Beyond the Screen*, *Architectural Evolution...* | Yalnızca bakış yönelimiyle odaklanmada (SG) küçük ve uzak nesnelerde hedefleme zorluğu yaşanmıştır (SG zorluk skoru: **3.2**; S: **1.4**, SGD: **1.8**; \\(p=0.0001\\) ve \\(p=0.0009\\)). Çakışan nesnelerde hibrit ses+bakış+tanım (SGD) kullanımı çakışmaları belirgin şekilde çözmüştür. | **Hayır** (AR/MR başlıklarında da baş/göz takibi ve mikrofon ile çalışır). |
| **Bakış ve Bekleme Süresi (Gaze Selection with Dwell Time)** | Göz veya baş hareketleriyle hedefe odaklanıp belirli bir sabitleme süresi boyunca hedefe bakarak seçimi onaylama. | *Beyond the Screen*, *Extended Reality in Spatial Sciences* | Sabitleme süresi **300 ms - 1000 ms** arasında tutularak *"Midas Touch"* engellenmektedir. Monteiro et al. çalışmasında kullanıcıların en çok tercih ettiği etkileşim yöntemi olduğu ölçülmüştür. | **Hayır** (AR gözlükleri, masaüstü eye-tracker'lar ve webcam sistemlerinde uygulanır). |
| **Jest ve El Takibi / Doğrudan Manipülasyon (Hand Gestures & Point & Teleport / Code Cubes)** | 3B kod küplerini/bileşenlerini (Code Cubes) uzayda el hareketleriyle taşıma, döndürme, açma (unfolding) ve parmakla işaret ederek konumlandırma (Point & Teleport). | *VRIDE*, *Analysis of Speech-Based Teleportation...*, *CityVR* | VRIDE ile geliştiricilerin **24 m³'lük** 3B hacmi aktif olarak kullandığı ve sanal klavyede stroke yazımının hata sayısını düşürdüğü tespit edilmiştir. Point & Teleport işaretleme tekniğinde 2 saniyelik onay beklemesi gezinme süresini uzatmış, ancak engellerle çarpışma sayısı (collisions) neredeyse sıfıra inmiştir. | **Hayır** (AR ortamlarında Air-tap veya el takibi ile uygulanabilir). |
| **Gövdeye / Bileğe Sabitlenmiş Arayüzler ve Haptik (Body-Anchored / Palm-Wrist UIs & Haptics)** | Sanal kontrol panellerinin/widget'ların avuç içine veya bileğe sabitlenmesi (Handows, Wrispack) ve etkileşimlerde dokunsal (vibrotactile/haptic) geri bildirim sağlanması. | *Beyond the Screen*, *DuoZone / Handows*, *Virtual Reality and Metaverse* | Avuç içine sabitlenmiş arayüzlerin (palm-anchored UIs) serbest uzaydaki nesnelere kıyasla etkileşim maliyetini ve yorgunluğu düşürdüğü gösterilmiştir. Dokunsal geri bildirim etkileşim farkındalığını ve gerçekçilik hissini artırır. (Kaynakta spesifik sayısal değer yok). | **Hayır** (AR, MR ve giyilebilir haptik bantlarla da çalışır). |
| **Vücut / Gövde Hareketi ile Etkileşim (Whole-Body Interaction / Physicalization)** | Kullanıcının tüm vücudunu hareket ettirerek kod bloklarını manipüle etmesi (örn. BlocklyVR) veya uzamda yürüyerek gezinmesi. | *Architectural Evolution...*, *CityVR* | Programlama görevlerinin fizikselleştirilmesinin (physicalization) kullanıcı katılımını (engagement) ve motivasyonunu artırdığı belirlenmiştir. (Kaynakta spesifik sayısal değer yok). | **Hayır** (AR/MR ve CAVE sistemlerinde de mümkündür). |
| **AI Agent / LLM Destekli Mekânsal Bölge Yönetimi (LLM-Guided Spatial Window/Agent Management)** | Çalışan AI agent'ları, pencere görünümlerini ve servis akışlarını yönetmek için doğal dil girdileri ve LLM ile mekânsal bölge (spatial zones) düzenlemeleri yapma. | *DuoZone: A User-Centric, LLM-Guided XR Window Management System* | Apple Vision Pro üzerinde yapılmış kullanıcı çalışmasında (**N=16**) mekânsal bölgelerin ve LLM ipuçlarının geleneksel yöntemlere kıyasla belirgin şekilde daha hızlı ayarlama sağladığı, çabayı ve bilişsel yükü düşürdüğü ölçülmüştür. | **Hayır** (MR/AR sistemlerinde de uygulanmaktadır). |

---

### Detaylı Açıklamalar ve Tasarım Çıkarımları

1. **Ses Komutları ve Bilişsel Yük Yansıması:**
   Sadece sesle kontrol, kullanıcının görsel olarak ekrana bağımlı kalmadan işlem yapmasını sağlar. Bilişsel yük ölçümlerinde, hedefi baş ile hedefleyip dikkat yoğunlaştırmaya kıyasla sesli komutların daha az konsantrasyon gerektirdiği ve bilişsel yükünün daha düşük çıktığı ölçülmüştür. Ancak kullanıcıların sistemdeki spesifik nesne isimlerini hatırlamakta zorlanması hata oranını artırabilmektedir.

2. **Çakışma Önleme (Disambiguation) ve Hibrit Yöntemler (SGD):**
   Bir mikroservis mimarisinde üst üste binen veya iç içe geçen kod yapıları/servis hatları olduğunda, yalnızca bakış kullanmak arka plandaki nesnelerin seçilmesini zorlaştırır. Hibrit yaklaşımda (SGD: Speech + Gaze + Description) kullanıcı hem bakışıyla yönü gösterebilir hem de *"Kırmızı binaya git"* veya *"Sarı servise odaklan"* diyerek sözel tanım ekleyerek çakışmayı anında çözebilir.

3. **Midas Touch ve Dwell Time Dengesi:**
   Göz ve baş takibiyle gezinmede kullanıcının etrafı incelemesi ile bir nesneyi seçmek istemesi arasındaki farkı anlamak zordur (*Midas Touch* problemi). 300 ms ile 1000 ms arasındaki bekleme süreleri (dwell time) veya sesli tetikleyiciler (*"Select"*, *"There"*) bu sorunu çözmek için en etkili mekanizmalardır.

4. **Klavyesiz Kod Düzenleme ve Uzamsal Kullanım:**
   VRIDE ortamında 3B kod küpleri (Code Cubes) kullanılarak geliştiricilerin gelen/giden bağımlılıkları ve metot hiyerarşilerini uzayda serbestçe yerleştirdikleri ve ortalama 24 m³'lük bir uzamsal alanı aktif olarak kullandıkları tespit edilmiştir. Metin veya parametre girişinde fiziksel klavye yerine jest bazlı çizim harfleri (stroke letters) kullanıldığında başarısız metin giriş denemelerinin belirgin şekilde azaldığı rapor edilmiştir.

5. **Gövdeye Sabitlenmiş Arayüzler (Palm / Wrist Anchored UIs):**
   Görselleştirme panelini ve butonları uzayda boşluğa asmak yerine kullanıcının bileğine veya avucuna sabitlemek (Handows / Wrispack), vücuda göre sabit bir referans noktası sunarak etkileşim maliyetini ve kol yorgunluğunu (*gorilla arm effect*) önemli ölçüde azaltmaktadır.

---

🎯 **Projeniz için Öneri:** Klavye ve fare bulunmayan deponuzda, gezinti ve odaklanma için **Bakış + Ses Füzyonunu (SGD)**, agent ve servis panellerinin yönetimi için ise **Avuç İçi Sabitlenmiş (Palm-Anchored) Arayüzler** ile **LLM destekli doğal dil komutlarını** birlikte kullanmak en yüksek kullanılabilirliği sağlayacaktır.

Demo ekranınızın bu etkileşim modelleriyle çalışan etkileşimli bir prototip mimarisini veya akış şemasını hazırlamamı ister misiniz?
2.Geliştiricilerin ve kullanıcıların karmaşık yazılım sistemlerinde (kod yapısı, çalışma anı servis trafiği ve çalışan AI agent'lar gibi çoklu görünümlerde) kaybolmadan gezinebilmesi için kaynaklarda **Anlamsal Yakınlaşma (Semantic Zoom)**, **Odak + Bağlam Koruma (Focus + Context)** ve **Bağlantılı Görünümler (Linked Views)** başlıkları altında somut tasarım kuralları ve mimari yöntemler önerilmektedir.

---

### 1. Anlamsal Yakınlaşma (Semantic Zoom) Kuralları

Anlamsal yakınlaşma, kameranın nesneye yaklaşmasıyla görünümün sadece optik olarak büyümesi değil, sunulan bilginin semantik ve detay düzeyinin dinamik olarak değişmesidir.

*   **Hiyerarşik Soyutlama Katmanları Oluşturma:** Yazılım sistemi tek bir detay seviyesinde sabitlenmemeli; mimariden koda doğru dereceli hiyerarşik katmanlar tanımlanmalıdır. *Immersive Software Archaeology (ISA)* çalışmasında bu yapı; **Güneş Sistemi (Yazılım Sistemi) \\(\rightarrow\\) Gezegenler (Üst Düzey Bileşenler) \\(\rightarrow\\) Kıtalar (Ara Bileşenler) \\(\rightarrow\\) Şehirler (Alt Düzey Bileşenler) \\(\rightarrow\\) Binalar (Sınıflar) \\(\rightarrow\\) Katlar (Metotlar)** şeklinde katmanlandırılmıştır.
*   **Detay Zenginleştirme (Detail Enrichment):** Kullanıcı üst düzey mimari bakıştan (observer role) şehir düzeyindeki birinci şahıs bakışına (first-person perspective) yaklaştığında, binalar semantik verilerle zenginleştirilmelidir. Örneğin metot katlarının yüksekliği ifade sayısı (expressions), çapı ise bilişsel karmaşıklık (cognitive complexity) ile ölçeklenmeli, soyut metotlar ise "inşaat alanı" olarak görselleştirilmelidir.
*   **Diegetik Bilgi Panelleri Kullanımı:** Bileşen veya metot detaylarına inildiğinde sabit 2B ekranı kaplayan pencereler yerine, kullanıcının koluna/bileğine sabitlenebilen veya 3B uzayda istenilen yere bırakılabilen diegetik bilgi panelleri (Diegetic Information Canvases / Info Panels) sunulmalıdır.

---

### 2. Odak + Bağlam Koruma (Focus + Context) Kuralları

Mikro bir detay incelenirken (örneğin belirli bir kod binası veya servis akışı), sistemin makro mimarisinin ve kullanıcının nerede olduğunun unutulmaması için şu yöntemler uygulanmalıdır:

*   **Gökyüzü Projeksiyonu (Sky Projection of Macro Overview):** *ISA (Hoff et al.)* tasarım kuralına göre, kullanıcı bir şehrin içine yakınlaştığında (Focus), makro sistem mimarisi ve gezegen yapısı **gökyüzüne yansıtılır (projected in the sky)**. Kullanıcı şehir içinde kod incelerken başını yukarı kaldırdığında diğer bileşenlerin makro konumunu (Context) ve aralarındaki bağlantı çizgilerini görebilir.
*   **Görsel Konum İşaretçileri (Orange Arrow / Target Indicators):** Kullanıcı mikro görünüme geçtiğinde, ana mimari haritada gezilmekte olan şehir veya bileşen belirgin bir **turuncu ok (orange arrow)** ile vurgulanarak kaybolma riski engellenir.
*   **İsteğe Bağlı Bağlantı Çizimi (On-Demand Rendering):** Servis trafiği veya metot çağrı kavislerinin (call graph arcs) tümü ekranda sürekli açık tutulduğunda görsel karmaşaya (visual clutter) yol açar. *SecCityVR* kuralına göre çağrı grafikleri varsayılan olarak gizli kalmalı; kullanıcı bir bileşeni seçip *"Render Call Graph"* komutunu tetiklediğinde yalnızca ilgili gelen/giden kavisler çizilmelidir.
*   **Saydamlık ve Gölgeleme Şablonları (Occlusion Templates):** Karmaşık 3B yapılarda odaklanılan içeriğin arkasında kalan öğelerin görüşü kapatmaması için yarı-saydam katmanlar (semi-transparent bubbles) veya *DuoZone* sisteminde tanımlanan **Saydamlık Şablonları (Occlusion Templates)** kullanılmalıdır.

---

### 3. Bağlantılı Görünümler (Linked Views) Kuralları

Farklı görünümler (örneğin yapısal kod şehri ile çalışma anı servis akışları veya AI agent panelleri) arasındaki ilişkinin kopmaması için kaynaklarda şu kurallar verilmektedir:

*   **Çapraz Hiyerarşik Kavisler (Cross-Hierarchical Relation Arcs):** Bir şehrin (kod yapısı) içindeki bir bina ile gökyüzünde duran başka bir gezegen (dış servis/bileşen) arasındaki ilişkiler, binadan gökyüzüne uzanan renkli kavislerle (connecting lines) görsel olarak birbirine bağlanmalıdır.
*   **Küp Türetme ve Görsel Çizgi Bağlantısı (Spawning & Connecting Lines):** *VRIDE* kuralına göre, 3B bir kod küpünün (Code Cube) bağımlılık veya alt/üst sınıf yüzeyine tıklandığında yeni bir kod küpü türetilmeli (spawning) ve iki küp arasına kopmayan görsel bir bağlantı çizgisi (connecting line) çekilmelidir.
*   **Çok Kullanıcılı Senkronizasyon ve Rehberli Keşif (Multi-User Network Synchronization & Guided Review):** Birden fazla kullanıcının çoklu görünümlerde kaybolmaması için *SecCityVR* modelindeki **Rehberli İnceleme (Guided Review)** modu kullanılmalıdır; bu modda takipçinin konumu ve bakış odağı otomatik olarak rehbere senkronize edilir. Bir kullanıcının görünüm üzerinde açtığı çağrı grafiği veya bağlantı kavisleri ağ üzerinden tüm kullanıcıların görünümlerinde eşzamanlı güncellenir.
*   **AI Agent ve Mekânsal Bölge Düzenlemeleri (LLM-Guided Spatial Zones):** *DuoZone* çalışmasında, çalışan AI/LLM agent'larının ve uygulama pencerelerinin yönetimi için **Düzenleme Bölgeleri (Arrangement Zones)** ve **Öneri Bölgeleri (Recommendation Zones)** kullanılması önerilir. Kullanıcının zihinsel mekânsal modelini korumak için öneri bölgelerinin konumları sabit tutulurken (retaining spatial mental model), içerikleri bağlama göre dinamik doldurulur. *(Not: "Agent ofisi" şeklinde özel bir 3B şehir metaforu adı kaynaklarda doğrudan yer almamakla birlikte, XR ortamında AI agent ve pencerelerinin mekânsal bölgelerle yönetimi DuoZone üzerinde incelenmiştir).*

---

### 4. Kullanıcının Kaybolmasını Önleyen Mekânsal Tasarım Kuralları

*   **Fiziksel Zemin ve Masa Referansı (Physical Table Reference / Anchors):** Görselleştirmelerin boş uzayda uzamsal oryantasyon kaybı yaşatmaması için gerçek bir masa veya zemin üzerine sabitlenmesi önerilir. Kullanıcılar bu masayı nirengi noktası olarak kullanarak etrafında yürüyebilir.
*   **Mekânsal Konum Sabitliği (Sense of Locality & Spatial Memory):** Binaların ve mahallelerin konumları dinamik olarak rastgele değişmemelidir; yerel konum duygusu (sense of locality) kullanıcının mekânsal hafızasını (spatial memory) kullanmasını sağlar.
*   **İki Farklı Gezinme Modu Sunma (Locomotion Modes):** Kullanıcıya hem sokak seviyesinde ışınlanarak gezinebileceği **Yürüme Modu (Walking/Teleportation)** hem de sistemin genelini üstten görebileceği **Uçma Modu (Flying Mode)** bir arada sunulmalıdır.

---

### Tasarım Kuralları Özet Tablosu

| Tasarım İlkesi | Uygulama Yöntemi / Mekanizması | Geçtiği Kaynak(lar) | Açıklama / Bilişsel Katkısı |
| :--- | :--- | :--- | :--- |
| **Semantic Zoom** | Güneş sistemi \\(\rightarrow\\) Gezegen \\(\rightarrow\\) Kıta \\(\rightarrow\\) Şehir \\(\rightarrow\\) Bina \\(\rightarrow\\) Kat hiyerarşisi | *ISA (Hoff et al. 2022)* | Makrodan mikro koda geçişte semantik detay zenginleştirmesi sağlar. |
| **Sky Projection** | Şehrin içine yakınlaşıldığında genel mimarinin gökyüzüne yansıtılması | *ISA (Hoff et al. 2022)* | Odaklanılan bileşen incelenirken genel bağlamın (context) kaybolmasını önler. |
| **Orange Arrow** | Gezilen şehrin üst haritada turuncu ok ile işaretlenmesi | *ISA (Hoff et al. 2022)* | Kullanıcının sistem mimarisi içindeki konumunu anında gösterir. |
| **Diegetic Canvases** | Detay panellerinin kol/bilek üzerine veya 3B uzaya sabitlenmesi | *ISA*, *SecCityVR* | 2B pencerelerin oluşturduğu ekran tıkanıklığını ve odak kaybını engeller. |
| **On-Demand Arcs** | Servis/çağrı kavislerinin sadece tıklamayla (*"Render Call Graph"*) açılması | *SecCityVR* | Karmaşık ilişki çizgilerinin oluşturduğu görsel kirliliği (visual clutter) önler. |
| **Spawning Lines** | Koda odaklanırken yeni küp türetme ve bağlantı çizgisi çekme | *VRIDE* | Bağımlılıklarda kaybolmadan uzamsal iz sürmeyi kolaylaştırır. |
| **Occlusion Templates** | Yarı-saydam gölgeleme şablonlarıyla görüş alanını açık tutma | *DuoZone*, *Balzer et al.* | Arka plandaki yapıların görüşü kapatmasını engeller, çevre farkındalığını korur. |
| **Guided Review** | Çok kullanıcılı incelemede takipçi konumunu rehbere senkronize etme | *SecCityVR* | Takım çalışmasında kullanıcıların farklı görünümlerde kaybolmasını önler. |
| **Table Anchoring** | 3B şehri/panelleri gerçek masaüstüne sabitleme | *Getaviz AR (HoloLens)* | Kullanıcıya fiziksel bir referans noktası sunarak oryantasyon kaybını engeller. |

---

🧭 **Demo Mimarisi İçin İpucu:** Prototipinizde, kod yapısını masa üzerindeki bir "3B şehir" olarak sunup, servis trafiğini bu binalar arasında isteğe bağlı açılan **ışıklı 3B kavisler** olarak çizdirmek ve gökyüzüne **AI Agent durumu panellerini (DuoZone düzenleme alanları)** yerleştirmek, kullanıcınızın oryantasyonunu kaybetmeden tüm sistem dinamiklerini izlemesini sağlayacaktır.

Bu çoklu görünüm geçişleri için bir kullanıcı akış diyagramı veya yazılım mimarisi dokümanı hazırlamamı ister misiniz?
3.### 1. İddianın Geçtiği Kaynak ve İfadenin Analizi

**İddianın Geçtiği Metin ve Kaynak:**
Bu iddia, projenin Türkçe başvuru ve sunum taslağı olan **`ADIM 1: BİLİMSEL NİTELİK`** (ve bağlantılı `ADIM 2`, `NexusOS-1002 Doldurulmuş Hali`) dokümanında geçmektedir. Bu Türkçe metin, temelde **"DuoZone: A User-Centric, LLM-Guided Mixed-Initiative XR Window Management System"** (Jing Qian et al., 2025) adlı akademik çalışmanın verilerine dayandırılmıştır.

**Tam Cümle:**
*   **Proje Dokümanındaki Türkçe Cümle:** 
    > *"Literatürde, LLM destekli "karma inisiyatifli" (mixed-initiative) uzamsal pencere yönetim sistemlerinin, görev tamamlama hızını artırdığı, bilişsel yükü %34'e varan oranlarda azalttığı ve sanal pencerelerin manuel olarak yeniden boyutlandırılması gibi zahmetli mikro-işlemleri minimize ettiği gösterilmiştir."*

*   **Dayandığı Orijinal DuoZone Makalesindeki Gerçek Değerler:**
    - **Görev Tamamlama Hızı:** Section 7.1'de DuoZone'un görev tamamlama süresini ortalama **%34.5 oranında hızlandırdığı** belirtilmektedir (*"indicating that DuoZone performs 34.5% faster performance on average"*, p < 0.001).
    - **Bilişsel Yük (NASA-TLX):** Section 8.1'de bilişsel yükün ortanca skorlarda yaklaşık **1/3 oranında (~%33.3)** düştüğü ifade edilmektedir (*"with DuoZone reducing median workload scores by roughly 1/3"*).
      - *Task 1 (Layout Matching):* Bilişsel yük ortalaması Baseline'da **47.71** iken DuoZone ile **33.30**'a düşmüştür (\\(H(1) = 7.57, p = 0.006\\)).
      - *Task 2 (Workspace Construction):* Bilişsel yük ortalaması Baseline'da **34.16** iken DuoZone ile **22.38**'e düşmüştür (\\(H(1) = 8.21, p = 0.004\\)).

---

### 2. DuoZone Çalışmasının Deney Düzeni, Katılımcı Sayısı ve Ölçüm Yöntemi

*   **Katılımcı Sayısı:** **16 katılımcı** (8 erkek, 8 kadın; yaş aralığı: 21–39, M = 26.7, SD = 5.5). Katılımcıların tümü günlük işlerinde çoklu pencere düzeni kullanan ve en az 3 yıllık mesleki deneyime sahip kişilerden oluşmaktadır.
*   **Deney Düzeni (Experiment Design):**
    *   Özne-içi (within-subject) tasarım.
    *   **Donanım / Yazılım:** Apple Vision Pro (1. nesil) kaskı, Unity (PolySpatial entegrasyonu), NVIDIA RTX 4050 GPU içeren yerel sunucu (LLM ve ağ iletişimi için).
    *   **Task 1 (Layout Matching):** Katılımcıların 3-4 uygulama panelini belirlenen hedef konuma yerleştirip boyutlandırdığı mikro-işlem testi (30 deneme).
    *   **Task 2 (Workspace Construction):** Katılımcıların tasarımcı veya programcı rolüne göre sıfırdan çalışma alanı oluşturması. Manuel yerleştirme (Baseline) ile DuoZone (sesli komutla LLM önerisi ve hazırlanan "Zone" şablonları) karşılaştırılmıştır.
*   **Ölçüm Yöntemi:**
    *   **Bilişsel Yük:** 0–100 ölçeğindeki dijitalleştirilmiş **NASA-TLX** (Task Load Index) formu (6 alt boyut: Mental Demand, Physical Demand, Temporal Demand, Performance, Effort, Frustration).
    *   **Performans Verileri:** Görev tamamlama süreleri (log-transformed completion time), düzenleme sayısı, AI önerilerini kabul etme oranları ve nitel mülakatlar.

---

### 3. Kaynaklarda Bilişsel Yükü (Cognitive Load / Task Load) Ölçen Diğer Çalışmalar

#### A. SecCityVR (Sanal Gerçeklikte Yazılım Güvenlik Analizi)
*   **Kaynak:** *SecCityVR: Visualization and Collaborative Exploration of Software Vulnerabilities in Virtual Reality* & *Architectural Evolution...*
*   **Katılımcı Sayısı:** Ana çalışmada **17 katılımcı** (öğrenciler, güvenlik araştırmacıları, profesyonel Java yazılımcıları); işbirlikçi çalışmada **8 katılımcı (4 çift)**.
*   **Ölçüm Yöntemi:** **NASA-TLX** anketi ve **SUS (System Usability Scale)** kullanılabilirlik skoru. Tablosal güvenlik paneli (`find-sec-bugs` dashboard) ile VR (SecCityVR) ortamı karşılaştırılmıştır.
*   **Sonuçlar:**
    *   **NASA-TLX Frustration (Bıkkınlık/Hüsran):** Tablosal dashboard'da median **52.5** iken VR ortamında **17.5**'e düşmüştür (\\(p = 0.03\\)).
    *   **NASA-TLX Temporal Demand (Zamansal Baskı):** Tablosal dashboard'da median **42.5** iken VR ortamında **10.0**'a düşmüştür (\\(p = 0.061\\)). İşbirlikçi deneyde dashboard'da **77.5** iken VR'da **25.0**'e düşmüştür (\\(p = 0.029\\)).
    *   **SUS Skoru:** Tablosal dashboard'da **58.75** iken VR ortamında **70.0**'e yükselmiştir.

#### B. XR Deneyim Tasarımı İncelemesi (Beyond the Screen)
*   **Kaynak:** *Beyond the Screen: A Scoping Review of Designing User-Friendly Experiences for Extended Reality*
*   **Ölçüm Yöntemi:** XR ortamlarında kullanılabilirlik ve bilişsel yük yönergelerini inceleyen derleme (scoping review).
*   **Sonuçlar:** 
    *   3B uzayın çevreyi organize etmek için bir araç olarak kullanılması bilişsel yükü düşürmektedir.
    *   Arayüz yerleştirmede **"Semi-auto placement" (Yarı otomatik yerleştirme)** yönteminin en düşük bilişsel yükü ürettiği, "Baseline" ve "Wristpack" yöntemlerinin ise en yüksek bilişsel yükü sunduğu tespit edilmiştir.

#### C. Sürükleyici AR'da Yazılım Analitiği (Getaviz / HoloLens)
*   **Kaynak:** *Identifying Usability Issues of Software Analytics Applications in Immersive Augmented Reality*
*   **Katılımcı Sayısı:** 3 ayrı değerlendirme turunda 5'er kişiden toplam **15 katılımcı** (13 profesyonel yazılım geliştirici, 2 AR deneyimli kullanıcı).
*   **Ölçüm Yöntemi:** Microsoft HoloLens üzerinde MRTK ve Getaviz 3B Şehir altyapısı kullanılarak görev bazlı kullanılabilirlik ve bilişsel yük değerlendirmesi.
*   **Sonuçlar:** AR ortamının 2B ekranlara kıyasla navigasyon ve binaların birbirini kapatması (occlusion) kaynaklı bilişsel zorlukları azalttığı; ancak metin okunabilirliği (text readability) ve sesli komut kullanımına karşı gösterilen kullanıcı direncinin ek bilişsel yük oluşturduğu gözlemlenmiştir.

#### D. VR Ortamında Göz Takibi ve Yol Bulma
*   **Kaynak:** *Augmented Reality, Virtual Reality & Semantic 3D Reconstruction* (Lee et al., 2020)
*   **Katılımcı Sayısı:** **24 katılımcı** (lisans/lisansüstü öğrenciler; geçerli gaze verisi analiz edilen 11 kişi).
*   **Ölçüm Yöntemi:** SMI-HTC Vive HMD ile zaman serisi göz takibi (gaze tracking), görsel odaklanma süresi (0.2s ve 0.3s bilişsel eşikleri) ve mekânsal bilgi tanıma anketi/mülakatı.
*   **Sonuçlar:** Görsel uyaranın alınmasından beyinde aktifleşmesine kadar geçen bilişsel işlemleme süresi (0.2s tepki, 0.3s anlama eşiği) göz hareketi verileriyle doğrulanmış; sanal mekânda yol bulma zorluğunun bilişsel işlemleme süreleri ve göz odaklanma süreleriyle doğrudan ilişkili olduğu belirlenmiştir.

#### E. Akıllı Telefon AR Ortamlarında Görsel Yorgunluk ve Bilişsel Yük
*   **Kaynak:** *[Inner endpaper] - HEC Montréal* (Amritam Mohapatra, 2024)
*   **Katılımcı Sayısı:** **28 katılımcı** (12 kadın, 16 erkek; yaş M = 23.67).
*   **Ölçüm Yöntemi:** Ekran ve ortam parlaklığı kombinasyonlarında (2x2 tasarım) soruluk bilgi testleri, görsel yorgunluk ve Sweller'ın Bilişsel Yük Teorisine (Cognitive Load Theory) dayalı psikometrik ölçümler.
*   **Sonuçlar:** Düşük okunabilirlik ve uyumsuz ışık oranlarının görsel yorgunluğu artırarak kullanıcının zihinsel kaynaklarını tükettiği, bunun da bilişsel yükü (*extraneous cognitive load*) artırarak öğrenme ve görev performansını düşürdüğü tespit edilmiştir.
4.3B uzamsal görselleştirmeler, sanal/artırılmış gerçeklik (XR) ortamları ve yazılım şehirlerinde doğal dille (sesli komut veya metin) soru sorulup cevabın görsel olarak parlatılması, vurgulanması veya filtrelenmesine ilişkin kaynaklarda yer alan çalışmalar, kullanılan mimariler, karşılaşılan hatalar ve sınırlılıklar aşağıda detaylandırılmıştır.

---

### 1. Doğal Dil Sorgusuyla Görsel Vurgulama Yapan Çalışmalar

*   **EvoSpaces (Dinamik İz Analizi ve Gece Modu):** Yazılım şehirleri üzerinde çalışma zamanı iz analizi (dynamic trace analysis) gerçekleştiren bu araçta, sistemdeki dinamik çağrılar ve yürütülen metotlar "gece modu" (*night mode*) metaforu ile gösterilir. Doğal dil veya sistem sorgusu sonucunda aktif çalışan metotların bulunduğu binalar ışıklandırılır ve parlatılır (*illuminated buildings*).
*   **Speech-Based Teleportation & Disambiguation System (PoliTO):** Kullanıcının 3B ortamda doğal dille sorgu yapmasını (`"Take me to the green bin"`, `"Take me to the bin"`, `"Take me there"`) ve doğrudan ilgili nesneye odaklanmasını sağlar. Soru sorulduğunda veya nesneye bakıldığında ilgili hedef nesne parlatılır ve vurgulanır. Belirsizlik (ambiguity) durumunda veya nesnelerin üst üste binmesi durumunda ön plandaki engel yarı saydam (*semi-transparent*) hale getirilerek arkadaki hedef vurgulanır ya da görsel bir seçim paneli açılır.
*   **Getaviz AR (HoloLens / MRTK):** Yazılım mimarisini 3B şehir metaforuyla sunan bu sistemde, sesli komutlarla (`"Filter"`, `"Select"`, `"About"`) nesnelere odaklanılır. Bir sınıfa odaklanıp `"Select"` dendiğinde ilgili bina görsel olarak vurgulanır ve kaynak kod paneli açılır. Küçük ve ince binaları hedefleme zorluğunu aşmak için özel bir gölgelendirici (*custom shader*) ile tolerans aralığı (*tolerance range*) eklenerek kullanıcının baktığı bina parlatılmaya devam eder.
*   **Reasoning3D (LLM Tabanlı 3B Mantıksal Bölümleme):** 3B nesneleri ve sahneleri 2B görünümlere dönüştürerek Büyük Görüş-Dil Modelleri (Vision-Language Models / VLMs) ile işler. Kullanıcı doğal dille nesnenin belirli bir bölümünü sorduğunda (open-vocabulary reasoning), sistem 3B segmentasyon maskeleri (*labeled vertices*) üreterek ilgili nesne parçasını görsel olarak parlatır ve vurgular.
*   **Text-to-Action (LLM-AR Entegrasyonu / Xu et al.):** Doğal dilde verilen karmaşık işletim ve bakım talimatlarını Büyük Dil Modelleri (LLM) ile adım adım eylemlere dönüştürür. Sistem, ortamı analiz ederek etkileşime girilmesi gereken 3B bileşenler üzerinde doğrudan parlayan ve dikkat çeken görsel katmanlar (*actionable visual overlays / cues*) oluşturur.
*   **SecCityVR (Zafiyet ve Çağrı Grafiği Vurgulama):** Kullanıcının güvenlik zafiyeti barındıran metotları görselleştirdiği bu sistemde, zafiyet seviyesine göre metot katları renk kodlarıyla (Kırmızı, Turuncu, Yeşil, Mavi) bina gövdesinden daha geniş çizilerek parlatılır. `"Render Call Graph"` komut veya butonuyla bağımlı servis ve metotlar arasında mavi-beyaz degrade 3B kavisler (*arcs*) çizilerek etkileşimdeki binalar vurgulanır.

---

### 2. Kullanılan Mimariler ve Teknolojiler

*   **Render ve Grafik Motoru Katmanı:** Sürükleyici 3B ortamların oluşturulmasında ağırlıklı olarak **Unity 3D** motoru kullanılmıştır. AR ve VR cihaz uyumluluğu için **MRTK (Mixed Reality Toolkit)**, **SteamVR** ve **OpenXR/WebXR** kütüphanelerinden yararlanılmıştır.
*   **Doğal Dil ve Konuşma Tanıma Katmanı:**
    *   *Kural ve Gramer Tabanlı:* **Microsoft Speech SDK** kullanılarak XML tabanlı dilbilgisi (*GRXML*) kuralları tanımlanmış ve istemci-sunucu (Client-Server) mimarisi üzerinden mesajlaşma sağlanmıştır.
    *   *LLM ve VLM Tabanlı:* **GPT-4**, **GPT-4V**, **BlenderBot** ve **RoBERTa** gibi büyük dil modelleri Chain-of-Thought (Düşünce Zinciri) istemleme ve RAG (Retrieval-Augment Generation) mimarileriyle 3B sahne verilerine bağlanmıştır.
*   **Veri ve Nesne Yönetimi Katmanı:** 3B nokta bulutlarında hızlı sorgulama için **KD-Tree** veri yapıları, mimari bağımlılıklar için **Neo4j** graf veritabanı ve arka plan servis haberleşmesi için **Spring Boot / REST API** mimarileri kullanılmıştır.

---

### 3. Raporlanan Hatalar, Sınırlılıklar ve Problem Alanları

1.  **Muğlaklık ve Yanlış Yorumlama (Vagueness & Disambiguation):**
    *   Yalnızca sesli komut kullanılan sistemlerde, birden fazla nesne aynı ismi taşıyorsa sistem belirsizliğe düşmekte ve kullanıcıyı yanlış hedefe yönlendirebilmektedir. PoliTO çalışmasında sadece sesli arayüzde 20 kez yanlış hedefe teleportasyon gerçekleşmiştir.
    *   Doğal dille sorulan muğlak sorular LLM tabanlı sistemlerde tahmin hatalarına (*mismatches*) yol açmaktadır.
2.  **Hedefleme ve Görsel Kapanma (Occlusion & Targeting Issues):**
    *   3B şehir görselleştirmelerinde ince ve küçük binaların arkada kalması (*occlusion*) veya baş/göz takibiyle ince binalara odaklanırken hedefin kayması ciddi kullanılabilirlik hatalarına neden olmuştur. Getaviz AR çalışmasında ince binaların seçilebilmesi için özel tolerans gölgelendiricileri geliştirmek gerekmiştir.
3.  **Kullanıcı Direnci (User Rejection of Speech):**
    *   Getaviz AR kullanıcı deneyinde, sesli komut mekanizması teknik olarak kusursuz çalışmasına rağmen, katılımcıların büyük çoğunluğu topluluk içinde veya ofis ortamında sesli komut vermeye karşı psikolojik direnç gösterdiklerini ve sesle kontrolü kullanmak istemediklerini belirtmiştir.
4.  **Gecikme, Halüsinasyon ve Donanım Kısıtları (Latency & Hallucinations):**
    *   LLM destekli XR görselleştirmelerinde multi-modal verilerin (göz takibi, ses, 3B sahne) işlenmesi sırasında oluşan gecikmeler (*latency*) kullanıcı deneyimini bozmaktadır.
    *   Görsel ve işitsel uyaranlar arasındaki uyumsuzluklar (*auditory-visual discrepancies*) kullanıcının zihinsel yükünü artırmaktadır. Ayrıca LLM'lerin ürettiği halüsinasyon verileri görselleştirmede yanlış bilgi sunulma riskini taşımaktadır.

---

### 4. Çalışmaların Karşılaştırma Tablosu

| Çalışma / Sistem | Sorgu / Etkileşim Türü | Görsel Vurgulama / Yanıt Biçimi | Kullanılan Mimari | Raporlanan Ana Sınırlılık / Hata |
| :--- | :--- | :--- | :--- | :--- |
| **EvoSpaces** | Çalışma zamanı dinamik kod sorgusu | Aktif çalışan metot binalarının gece modunda parlatılması (*illuminated*) | Code City 3B Mimarisi | Yalnızca çalışma zamanı izini gösterir, statik zafiyetleri kapsamaz. |
| **PoliTO Speech-Teleport** | Sözel veya Hibrit Sorgu (`"Take me to the green bin"`) | Hedef nesnenin parlatılması; çakışmada engelin yarı saydam yapılması | Unity 3D + Microsoft Speech (Client-Server, GRXML) | Sadece seste kelimeleri hatırlama yükü; sadece bakışta uzaktaki küçük nesneleri hedefleyememe. |
| **Getaviz AR** | Sesli Komut (`"Filter"`, `"Select"`) | Seçilen sınıfın parlatılması ve kod diyaloğunun açılması | Unity 3D + HoloLens MRTK + Getaviz Framework | İnce binaları hedefleme zorluğu; kullanıcıların sesli komuta direnç göstermesi. |
| **Reasoning3D** | Doğal Dil Sorgusu (Açık kelime hazineli) | 3B segmentasyon maskeleriyle istenen nesne parçasının vurgulanması | 2D Vision-Language Models + 3B Segmentasyon Maskeleme | Karmaşık 3B veri kümelerine bağımlılık; donanım hesaplama yükü. |
| **Text-to-Action** | Doğal dilde karmaşık görev talimatları | 3B nesneler üzerinde eyleme dönüştürülebilir parlak katmanlar (*overlays*) | LLM (Üç Modüllü İstemleme) + AR Görsel Katmanları | Muğlak talimatlarda LLM'in yanlış katmanlar oluşturma riski. |
| **SecCityVR** | Seçim Komutu (`"Render Call Graph"`) | Zafiyetli katların renklendirilip genişletilmesi; 3B kavislerle bağlantı vurgulanması | Unity 3D + SpotBugs SAST + Network Synchronization | Tüm kavisler aynı anda açıldığında görsel kirlilik (*visual clutter*) oluşması. |

---

🤖 **Öneri:** Geliştireceğiniz demoda, doğal dil sorgusunda yaşanabilecek muğlaklıkları çözmek için **PoliTO** çalışmasındaki gibi *yarı-saydamlaştırma (semi-transparency)* veya **Getaviz** çalışmasındaki gibi *özel tolerans gölgelendiricileri (custom shader tolerance range)* eklemek, kullanıcının sorguladığı servisi veya binayı zahmetsizce algılamasını sağlayacaktır. 

Bu görsel vurgulama tekniklerinin kod tarafındaki Unity shader uygulamaları veya ses tanıma arayüzü entegrasyonu hakkında teknik detay sunmamı ister misiniz?
5.Yazılım sistemlerini 3B sanal/artırılmış gerçeklik (XR) ortamlarında görselleştiren ve doğal dil/jest gibi HCI prototiplerini değerlendiren çalışmalarda kullanılan **görevler**, **metrikler** ve **katılımcı sayıları** aşağıda detaylandırılmış; ardından 5–10 kişilik küçük bir ekiple uygulanabilecek, doğrudan kaynaklara dayalı bir değerlendirme planı sunulmuştur:

---

### 1. Kaynaklardaki Değerlendirme Çalışmalarının Analizi

Literatürdeki HCI veyazılım görselleştirme prototipleri incelendiğinde öne çıkan deney tasarımları şunlardır:

*   **SecCityVR (Zafiyet Görselleştirme ve İşbirliği):**
    *   **Katılımcı Sayısı:** Toplam **17 benzersiz katılımcı** (öğrenciler, güvenlik araştırmacıları ve Java yazılımcıları). Tekil inceleme ana çalışmasında bireysel test yapılmış, işbirlikli çalışma turlarında ise **8 katılımcı (4 çift)** eşleşerek çalışmıştır.
    *   **Görevler:** Binalar ve katlar üzerinden zafiyetleri tespit etme, önceliklendirme, çağrı kavislerini (*call graph arcs*) takip ederek zafiyet yayılımını izleme ve işbirlikli turda ilk çözülecek 2 zafiyeti belirleme.
    *   **Metrikler:** **SUS** (*System Usability Scale* - ortanca skoru VR'da 70.0, tablosal dashboard'da 58.75), **NASA-TLX** (özellikle Frustration: 17.5 vs 52.5; Temporal Demand: 10.0 vs 42.5), **VRSQ** (*Virtual Reality Sickness Questionnaire* ile mide bulantısı/göz yorgunluğu), **Görev Tamamlama Süresi** (*Task Completion Time*) ve **Görev Doğruluğu/Hata Oranı**.
*   **DuoZone (LLM Destekli XR Pencere ve Alan Yönetimi):**
    *   **Katılımcı Sayısı:** **16 uzman katılımcı** (8 erkek, 8 kadın; en az 3 yıllık mesleki deneyime sahip).
    *   **Görevler:** *Task 1 (Layout Matching):* 3-4 paneli hedef hologram düzenine göre yerleştirme (30 deneme). *Task 2 (Workspace Construction):* Programcı veya tasarımcı rolüyle sıfırdan doğal dille pencere/çalışma alanı düzenleme.
    *   **Metrikler:** Görev tamamlama süresi (log-dönüştürülmüş), dijitalleştirilmiş **NASA-TLX** (0–100 ölçekli 6 alt boyut), **AI Öneri Kabul Oranı** (%90.3 uygulama ilgililiği, %82.8 düzen kabulü) ve nitel mülakat kodlaması.
*   **Getaviz AR / HoloLens (Artırılmış Gerçeklikte Yazılım Analitiği):**
    *   **Katılımcı Sayısı:** 3 ayrı iteratif turda 5'er kişiden toplam **15 katılımcı** (13 profesyonel geliştirici, 2 AR deneyimli kullanıcı).
    *   **Görevler:** *Help & Setup* (şehir modelini masaya yerleştirme, boyutlandırma, interaktif tutorial tamamlama), *Visualization* (görsel kalıpları ve aykırı binaları tanıma), *Dialog* (kaynak koda odaklanma, filtreleme).
    *   **Metrikler:** Görev çözme doğruluğu, yarısaydam yarıyapılandırılmış mülakatlar (*semi-structured interviews*) ve kullanılabilirlik sorunlarının kategorizasyonu (Selection, Text Readability, Occlusion, User Guidance).
*   **CityVR (Şehir Metaforu ile Kod Anlama):**
    *   **Katılımcı Sayısı:** **6 deneyimli geliştirici**.
    *   **Görevler:** T1: ArgoUML tasarım kalitesi/kod kokularını tespiti, T2: Paketlerin semantiğini açıklama.
    *   **Metrikler:** Yarı yapılandırılmış mülakatlar ve 5'li Likert ölçeğinde kullanıcı deneyimi geribildirimleri.
*   **ISA / Immersive Software Archaeology (Mimari Geri Kazanım):**
    *   **Katılımcı Sayısı:** Toplam **54 katılımcı** (22 Lisans, 20 Yüksek Lisans, 9 Doktora öğrencisi ve 3 Araştırmacı; 3 araç grubuna 18'er kişi dağıtılmıştır).
    *   **Görevler:** Farklı soyutlama seviyelerinde eleman bulma, tasarım seviyesindeki ilişkileri izleme ve giden/gelen çağrıları bağlama.
    *   **Metrikler:** Görev başarı oranı, doğru yanıt kalıplarının analizi, görev süreleri ve giriş/çıkış anketleri.
*   **PoliTO (Sesli ve Bakış Tabanlı Işınlanma/Navigasyon):**
    *   **Katılımcı Sayısı:** **15 katılımcı**.
    *   **Görevler:** 3 farklı teknik altında (Ses, Ses+Bakış, Ses+Bakış+Tanım) 8 hedef noktaya ışınlanma adımı.
    *   **Metrikler:** **SASSI** anketi (7'li Likert; System Response Accuracy, Cognitive Demand, Speed vb.), **SUS** (5'li Likert), yanlış hedef seçimi sayısı ve işlem süreleri.
*   **ALTER (Model-Driven AR):**
    *   **Katılımcı Sayısı:** **11 katılımcı**.
    *   **Görevler:** AR elemanı oluşturma, taşıma, boyutlandırma, nitelik değiştirme.
    *   **Metrikler:** **SUS** anketi skoru (%79.3) ve açık uçlu artı/eksi geribildirim soruları.

---

### 2. Küçük Bir Ekip İçin (5–10 Kişi) Değerlendirme Planı Önerisi

5–10 kişilik kısıtlı bir katılımcı grubuyla en yüksek bilimsel verimi almak için literatürdeki **İteratif Kullanılabilirlik Değerlendirmesi (Iterative Usability Evaluation)** ve **İç-Özne / Karşılaştırmalı Tasarım (Within-Subject Design)** yaklaşımlarına dayanan 6 adımlı değerlendirme planı aşağıdadır:

```
[Adım 1: Demografik Anket] ➔ [Adım 2: İnteraktif Tutorial] ➔ [Adım 3: Görev Protokolü (T1-T4)]
                                                                    │
[Adım 6: İteratif İyileştirme] ◄─ [Adım 5: Veri Analizi] ◄─ [Adım 4: Post-Study Anketleri]
```

#### Adım 1: Ön Hazırlık ve Demografik Profilleme (Pre-Study)
*   **Katılımcı Profilleme:** Katılımcıların yaş, mesleki tecrübe, Java/kodlama yetkinliği, VR/AR tecrübesi ve sesli/doğal dil arayüzü tecrübesi kaydedilir.
*   **Uygulama Yolu:** Katılımcıların homojenize edilmesi veya deneyim seviyelerine göre dengelenmesi sağlanır.

#### Adım 2: Başlangıç ve İnteraktif Eğitim (Interactive Tutorial)
*   **Ortama Adaptasyon:** Kullanıcının 3B uzamda hareket etme, jest yapma veya sesli komut verme mekanizmalarına alışması için **3–5 dakikalık interaktif bir eğitim** yaptırılır.
*   **Gerekçe:** Kullanıcıların sistemin konumlandırma ve yakınlaşma özelliklerini bilmemesinden kaynaklanan hataları engellemek ve "öğrenme etkisini" kontrol altına almak için tutorial zorunludur.

#### Adım 3: Temel Görev Protokolü (Task Protocol - 4 Kategori)
Katılımcılara uygulamanın tüm fonksiyonlarını kapsayan 4 aşamalı bir görev seti sunulur:
1.  **Görsel Kurulum ve Gezinme (Help & Setup / Navigation):** *"3B kod şehrini/servis panelini masa üzerine yerleştirin, boyutlandırın ve optimal açıya getirin"*.
2.  **Statik Yapı ve Anomali/Zafiyet Tespiti (Comprehension & Pattern Spotting):** *"En karmaşık sınıfı/binayı veya üzerinde kırmızılı zafiyet katı bulunan servisi tespit edin"*.
3.  **Dinamik Akış ve Bağımlılık İzleme (Dependency / Call Graph Tracing):** *"X metoduna tıklayarak çağrı kavislerini açın ve bu metodun çağırdığı bağlı binaları/servisleri listeleyin"*.
4.  **Doğal Dil / Sesli Komut ve İşbirliği (Natural Language & Collaboration):** *"Işınlanma/filtreleme için 'Kırmızı binaya git' veya 'Yavaş servisi göster' sorgusunu çalıştırın"* veya *"Eşinizle birlikte ilk düzeltilecek 2 problemi belirleyin"*.

#### Adım 4: İteratif Test Düzeni (Iterative Evaluation Protocol)
*   **Katılımcı Bölünmesi (5 + 5 İterasyonu):** 10 kişilik grup **5'er kişilik 2 iteraşyona** ayrılır.
*   **Gerekçe:** İlk 5 katılımcının arayüzde yaşadığı seçim (Selection), metin okuma veya pencere bulma sorunları düzeltildikten sonra ikinci 5 kişilik grupla test tekrarlanır. Bu sayede küçük gruplarla bile arayüz sorunları hızla çözülür.

#### Adım 5: Veri Toplama ve Ölçüm Metrikleri (Post-Study Metrics)
Ölçüm kargaşasını önlemek amacıyla post-study (görev sonrası bütünsel) anket yaklaşımı benimsenir:
*   **Öznel Metrikler (Subjektif Anketler):**
    *   **SUS (System Usability Scale):** 10 soruluk 5'li Likert ölçeği ile genel kullanılabilirlik puanı ölçülür (Hedef skoru: >68 benchmark veya >70 Good).
    *   **NASA-TLX:** Bilişsel yükün 6 boyutu (Mental, Physical, Temporal Demand, Performance, Effort, Frustration) ölçülür.
    *   **VRSQ (Virtual Reality Sickness Questionnaire):** VR deneyimlerinde oluşabilecek mide bulantısı ve okülomotor rahatsızlıklar kontrol edilir.
*   **Nesnel / Performans Metrikleri:**
    *   **Görev Tamamlama Süresi (Task Completion Time):** Her bir görevin saniye cinsinden süresi kaydedilir.
    *   **Hata Sayısı ve Doğruluk (Accuracy / Error Rate):** Yanlış hedef tıklamaları veya hatalı bağımlılık tespitleri sayılır.
*   **Nitel Veri:**
    *   **Yarı Yapılandırılmış Mülakat (Semi-structured Interview) ve Sesli Düşünme (Think-Aloud):** Katılımcıların binaları ararken yaşadığı kafa karışıklıkları ve diegetik panellere dair sözlü geribildirimleri kaydedilir.

#### Adım 6: Veri Analizi
*   Küçük örneklemlerde (N=5–10) veriler parametrik olmayan istatistiksel testlerle (**Wilcoxon Signed-Rank Test** veya **Mann-Whitney U Test**) analiz edilir.
*   Mülakat verileri için açık ve eksenel kodlama (**open and axial coding**) uygulanır.

---

💡 **Uygulama Tavsiyesi:** Küçük ekibinizle testi yürütürken kullanıcıların 3B uzamda kaybolmasını engellemek için **Getaviz AR** çalışmasında vurgulandığı gibi *Tutorial (Eğitim)* aşamasını atlamamanız ve **SecCityVR** çalışmasındaki gibi *SUS + NASA-TLX* kombinasyonunu post-study anketi olarak sunmanız en güvenilir sonuçları verecektir.

Bu değerlendirme planı için katılımcılara dağıtılabilecek detaylı bir **Görev Sayfası (Task Sheet)** veya **Anket Formu Taslağı** hazırlamamı ister misiniz?
6.Kaynaklardaki bulgular ve sınırlılıklar incelendiğinde, **VR gözlüğü gerektirmeyen (AR, masaüstü veya uzamsal ekran tabanlı), ses ve dokunma odaklı** bir yazılım mimarisi ve çalışan AI agent görselleştirme sisteminde henüz tam olarak çözülememiş **5 temel araştırma boşluğu** aşağıda detaylandırılmıştır:

---

### 1. Sesli Komutlara Karşı Kullanıcı Direnci, Gürültü ve Çok Modlu (Multimodal) Belirsizlik Çözümü

*   **Çözülmemiş Araştırma Boşluğu:** Sesli komutlar eller serbest gezinme ve koda odaklanma için teknik olarak kusursuz çalışsa da, kullanıcıların ofis ortamında veya başkalarının yanında sesli komut vermeye karşı **psikolojik bir direnç (general rejection of voice control)** gösterdikleri ve sese dayalı arayüzleri kullanmak istemedikleri tespit edilmiştir. Ayrıca gürültülü ortamlarda veya ağ gecikmelerinde ses tanıma doğruluğu düşmekte, isimleri hatırlama zorunluluğu nedeniyle hatalar artmaktadır. VR'sız (AR/masaüstü) ortamlarda, sesli komutların muğlaklığını (*ambiguity*) ortadan kaldırmak için ses, bakış ve dokunmatik jestlerin bir arada kullanıldığı çok modlu (multimodal) sessiz/hibrit doğrulama mekanizmaları henüz olgunlaşmamıştır.
*   **İlgili Kaynaklar:** *Identifying Usability Issues of Software Analytics Applications in Immersive Augmented Reality (Getaviz)*, *Analysis and Comparison of Speech-Based Teleportation Techniques... (PoliTO)*, *Extended Reality in Spatial Sciences*.
*   **Neden Yenilikçi Bir Katkı?:** Sadece sesli komutlara bağımlı kalmak yerine, gizlilik kaygılarını aşan, kullanıcı direncini kıran ve **dokunmatik mikro-jestler ile sesli komutları füzyona uğratan çok modlu (multimodal) sessiz denetim çözümleri** geliştirmek, yazılım görselleştirme arayüzlerinin gerçek dünya profesyonel ofis ortamlarında benimsenmesini sağlayacak kritik bir yeniliktir.

---

### 2. Derinleşen Kod Mimarileri ve Agent Pencerelerinde Görsel Çakışma (Occlusion) ve Dinamik Pencere Yönetimi

*   **Çözülmemiş Araştırma Boşluğu:** 3B kod şehri üzerinde gezinirken ve çalışan çoklu AI agent pencerelerini izlerken, binaların veya sanal panellerin üst üste binerek görüşü kapatması (**occlusion**) ve ekran tıkanıklığı yaratması en büyük ergonomik zorluklardan biridir. *DuoZone* gibi LLM destekli pencere yönetim sistemleri pencereleri gruplayıp otomatize etse de, sistemlerin mevcut yapısı **kullanıcının anlık fiziksel durumunu, değişken iş alışkanlıklarını ve uzun vadeli kişiselleştirmesini çevrim içi (human-in-the-loop) olarak takip edip dinamik uyarlama yapmakta** yetersiz kalmaktadır.
*   **İlgili Kaynaklar:** *DuoZone: A User-Centric, LLM-Guided Mixed-Initiative XR Window Management System*, *Beyond the Screen*.
*   **Neden Yenilikçi Bir Katkı?:** VR başlığı olmadan, AR veya 2B/3B ekranlarda kod şehri ile AI agent pencerelerini **görüşü kapatmayacak (occlusion-free) şablonlarla ve LLM destekli dinamik düzenleme alanlarıyla (Arrangement & Recommendation Zones)** otomatik organize eden karma-inisiyatifli bir arayüz sunmak, kullanıcının zihinsel yükünü düşüren özgün bir katkıdır.

---

### 3. Dokunmatik Sanal Klavyelerin Yetersizliği ve Koda/Agent'lara Doğrudan Fiziksel Temasla Müdahale (Virtually Tangible) Sınırları

*   **Çözülmemiş Araştırma Boşluğu:** 3B kod binalarında arama yapmak, filtreleme uygulamak veya agent parametrelerini değiştirmek gerektiğinde, ekrandaki sanal klavyeler (virtual on-screen keyboard) ve klasik kaydırma çubukları (scrollbars) son derece kullanışsız kalmakta ve ciddi kol yorgunluğuna yol açmaktadır. Kod binalarına veya agent panellerine fiziksel bir nesneye dokunur gibi doğrudan müdahale etme (**direct touch/manipulation**) ve klavye gerektirmeyen metin/parametre girişi sağlama mekanizmaları geleneksel 2B IDE'lerin hızına ve verimliliğine henüz ulaşamamıştır.
*   **İlgili Kaynaklar:** *Identifying Usability Issues of Software Analytics Applications...*, *XRaSE: Towards Virtually Tangible Software using Augmented Reality*, *Beyond the Screen*.
*   **Neden Yenilikçi Bir Katkı?:** Klasik 2B menü ve sanal klavyeleri tamamen ortadan kaldırarak, kod düğümlerini ve agent akışlarını **dokunmatik jestler (stroke letters, haptik menüler) ve dokunsal mikro-etkileşimlerle doğrudan manipüle edilebilir ("virtually tangible")** hale getirmek, VR'sız geliştirme ortamlarında metin girme ve filtreleme darboğazını çözen yenilikçi bir yaklaşımdır.

---

### 4. Çok Kullanıcılı Gerçek Zamanlı Farkındalık İpuçları (Awareness Cues) ve Canlı Agent İletişimi Eksikliği

*   **Çözülmemiş Araştırma Boşluğu:** Yazılım güvenlik denetimleri ve çalışan agent takibi genellikle geliştiriciler tarafından izole ve asenkron yürütülmektedir. *SecCityVR* gibi araçlar VR ortamında çok kullanıcılı eşzamanlı inceleme sunsa da, **VR'sız (AR veya masaüstü) ekranlarda farklı rollerdeki kullanıcıların (yazılımcı, güvenlik uzmanı, yönetici) aynı 3B kod şehri veya canlı agent akışı üzerinde birbirlerinin odağını (göz/dokunma imleçleri, farkındalık ipuçları - awareness cues) gerçek zamanlı görmesi** ve senkronize karar alması için gerekli ortak arayüz standartları eksiktir.
*   **İlgili Kaynaklar:** *SecCityVR: Visualization and Collaborative Exploration of Software Vulnerabilities in Virtual Reality*, *Extended Reality in Spatial Sciences*, *LLM Integration in Extended Reality*.
*   **Neden Yenilikçi Bir Katkı?:** Ağır VR başlıkları kullanmadan, masaüstü veya AR ekranlarında çok kullanıcılı işbirlikçi kod ve agent denetimi yapabilmek; **mimari üzerindeki canlı farkındalık işaretçileri (awareness cues) ve senkronize dokunma/bakış izleri** sayesinde asenkron iletişimin getirdiği kopukluğu ortadan kaldıran güçlü bir mimari yeniliktir.

---

### 5. Gerçek Dünya Masaüstü Nesneleriyle Entegre Karma Gerçeklik (MR) ve Referans Çıpası (Anchoring) Metaforu Eksikliği

*   **Çözülmemiş Araştırma Boşluğu:** Mevcut yazılım görselleştirme araçlarının büyük çoğunluğu sanal şehri veya veri panellerini uzayda süzülen soyut nesneler olarak kurgulamakta, bu da kullanıcının yön duygusunu kaybetmesine yol açmaktadır. AR kullanıcı değerlendirmelerinde, geliştiricilerin sanal kod şehrini **içgüdüsel olarak fiziksel bir çalışma masasına sabitledikleri ve kod panellerini ofisteki gerçek bir beyaz tahtaya (whiteboard) hizaladıkları** tespit edilmiştir. Ancak, fiziksel çalışma masasını, monitör çerçevelerini ve çevre şartlarını 3B kod şehri ve agent akışlarıyla tam entegre eden gelişmiş Karma Gerçeklik (MR) çıpalama metaforları henüz kurulmamıştır.
*   **İlgili Kaynaklar:** *Identifying Usability Issues of Software Analytics Applications...*, *Extended Reality in Spatial Sciences*, *LLM Integration in Extended Reality*.
*   **Neden Yenilikçi Bir Katkı?:** Kullanıcıyı fiziksel ortamdan soyutlayan VR yerine, **fiziksel masaüstünü veya ofis tahtasını birer referans çıpası (physical anchor) olarak kullanıp kod görselleştirmesini ve agent panellerini bu yüzeylere giydiren bir MR etkileşim modeli kurmak**, kullanıcının doğal oryantasyonunu koruyan ve kullanılabilirliği radikal şekilde artıran bir tasarımdır.

---

💡 **Sonuç:** Geliştireceğiniz demoda; **fiziksel masaya çıpalanmış bir 3B şehir**, **dokunmatik mikro-jestlerle kontrol edilen pencereler** ve **LLM destekli dinamik yerleşim alanları (DuoZone)** kullanarak bu 5 araştırma boşluğunu doğrudan hedefleyebilir ve literatüre yüksek etkili yenilikçi bir katkı sunabilirsiniz.

Bu araştırma boşluklarına yönelik bir akademik makale özeti veya proje önerisi gerekçesi hazırlamamı ister misiniz?

## Claude'un notu (bozuk yerler)

NotebookLM çıktılarının bazı yerleri bozuk. 1. cevabın tablosunda sesli komut ve Getaviz satırları birbirine karışmış, 4. cevap da kesik. Aşağıdakiler okunabilen kısımlardan çıkardığım sonuçlar.

**1. %34 iddiası düzeltilmeli.**
- Proje dokümanındaki cümle ("bilişsel yükü %34'e varan oranda azaltıyor") DuoZone makalesiyle (Qian et al., 2025) tam örtüşmüyor.
- Makalede **görev tamamlama hızı %34,5** artıyor (p<0,001).
- **NASA-TLX iş yükü ise yaklaşık 1/3** düşüyor. Task 1'de 47,71→33,30, Task 2'de 34,16→22,38. Katılımcı sayısı N=16.
- Sunuma "bilişsel yük %34" diye girmesin. Doğru ifade: "görevler %34,5 daha hızlı, iş yükü yaklaşık üçte bir azaldı (N=16)".

**2. Ses ve dokunma için dikkat edilecek noktalar.**
- Getaviz AR çalışmasında sesli komut teknik olarak kusursuz çalışmış, ama katılımcılar ofiste sesle komut vermek istememiş. Ses tek başına yeterli olmaz, sessiz bir alternatif gerekir (mikro-jest, dokunma).
- Bakış ve ses birlikte kullanılınca (SGD) üst üste binen nesnelerde seçim daha iyi çalışıyor.
- Bakışta "Midas Touch" sorunu var. 300–1000 ms bekleme süresi ya da sesli tetikleyici öneriliyor.
- Avuç içi ve bilek sabitli paneller etkileşim yorgunluğunu azaltıyor.

**3. Üç görünümün birleşmesi için bulunan kurallar.**
- Semantik yakınlaşma: sistem → bileşen → bina → metot. Yakınlaşınca detay artıyor (ISA).
- Yakınlaşırken genel mimariyi gökyüzüne yansıtmak bağlamı koruyor.
- Çağrı yayları yalnızca istenince açılmalı. Hepsi birden açılınca görsel kirlilik oluyor (SecCityVR).
- Detay panelleri 2B pencere yerine kola ya da uzaya sabitlenmeli.

**4. Değerlendirme planı.**
- 5–10 kişiyle çalışılır: demografik anket, 3–5 dk eğitim, 4 görev, ardından SUS ve NASA-TLX.
- Küçük örneklemde Wilcoxon ya da Mann-Whitney U testi, nitel veri için mülakat.
- Referans değerler: SecCityVR'da SUS 58,75→70, frustration 52,5→17,5.

**5. VR'sız çalışmada en umut verici boşluklar.**
- Kod şehri ile agent pencerelerinin birbirini kapatmasını (occlusion) önleyen, LLM destekli dinamik düzen.
- VR'sız, çok kullanıcılı ortak inceleme: farklı roller aynı şehri ya da agent akışını görüyor, birbirlerinin odağını farkındalık işaretleriyle izliyor.
- Sessiz mikro-jest ve dokunma ile hibrit etkileşim.

Önerim: sunum verisindeki %34 satırını şimdi düzeltmem, ardından 1. ve 5. maddeden bir sonraki demo için kısa bir yön önerisi çıkarmam. Hangisini istersin?
