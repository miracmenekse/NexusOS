# Graph Report - kaynaklar  (2026-10-11)

## Corpus Check
- Corpus is ~38,204 words - fits in a single context window. You may not need a graph.

## Summary
- 176 nodes · 343 edges · 12 communities
- Extraction: 80% EXTRACTED · 20% INFERRED · 1% AMBIGUOUS · INFERRED: 67 edges (avg confidence: 0.87)
- Token cost: 160,819 input · 0 output

## Community Hubs (Navigation)
- Literatür ve Atıflar
- NexusOS Çekirdek Konsepti
- Başvuru Bölümleri (Final)
- Video Senaryoları
- TÜBİTAK Form Kuralları
- İş Paketleri ve Web3
- Ders: Blokzincir ve NFT
- Ders: Deneyim ve Güvenlik
- Ders: Yapay Zekâ ve Pazar
- Ders: VR/AR Temelleri
- Ders: Bilim Kurgu ve OASIS
- Ders: Yıkıcı İnovasyon

## God Nodes (most connected - your core abstractions)
1. `NexusOS (VR-özgü uzamsal işletim katmanı / IDE)` - 28 edges
2. `NexusOS NotebookLM Notebook (96 kaynak)` - 18 edges
3. `EK-1 Kaynaklar (1002-A Final)` - 13 edges
4. `Doç. Dr. Murat Yılmaz (Gazi Üniversitesi)` - 12 edges
5. `Metaverse-NexusOS 1002-A Başvuru Final` - 12 edges
6. `Şehir Metaforu (City Metaphor) / Kod Şehri` - 12 edges
7. `NexusOS Literatür Yakınlık (Affinity) Analizi - en iyi 20 kaynak` - 12 edges
8. `MTVRS-NexusOS Projesi Tanım Dokümanı` - 11 edges
9. `Sunum Şablonu - TÜBİTAK Form Eşleştirme` - 11 edges
10. `TÜBİTAK 1002-A Başvuru İçeriği Bilgi Notu` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Çelişki: Tam sürükleyici VR vs AR (XRaSE)` --semantically_similar_to--> `Açık konu: video karma gerçeklik, başvuru VR-özgü diyor`  [INFERRED] [semantically similar]
  notebooklm/notebooklm1.md → drive/video/NexusOS Kling - sahneler.md
- `Çelişki: Sanal Monitör vs VR-Özgü 3B yaklaşım` --semantically_similar_to--> `Pazar Boşluğu: AST + yerel LLM + 3B çok kullanıcılı kod analizi sunan rakip yok`  [INFERRED] [semantically similar]
  notebooklm/notebooklm1.md → manus/Rekabet Analizi - Detaylı Araştırma.md
- `NexusOS NotebookLM Notebook (96 kaynak)` --references--> `MTVRS-NexusOS Projesi Tanım Dokümanı`  [INFERRED]
  notebooklm/notebooklm1.md → drive/MTVRS-NexusOS Projesi Tanım Dok.md
- `NexusOS NotebookLM Notebook (96 kaynak)` --references--> `Sunum Şablonu - TÜBİTAK Form Eşleştirme`  [INFERRED]
  notebooklm/notebooklm1.md → drive/MTVRS-Sunum Şab. Tubitak Form Eşleştirme.md
- `NotebookLM ADIM 1-4 Taslakları` --references--> `Metaverse-NexusOS 1002-A Başvuru Final`  [INFERRED]
  notebooklm/2026-10-11-adim-taslaklari.md → drive/Metaverse-NexusOS 1002-A Başvuru Final.md

## Hyperedges (group relationships)
- **1002-A Başvuru Formu Ana Bölümleri** — drive_tubitak_1002_a_basvuru_icerigi_bilgi_notu_bilimsel_nitelik, drive_tubitak_1002_a_basvuru_icerigi_bilgi_notu_yontem, drive_tubitak_1002_a_basvuru_icerigi_bilgi_notu_proje_yonetimi, drive_tubitak_1002_a_basvuru_icerigi_bilgi_notu_cikti_etki_kazanimlar [EXTRACTED 1.00]
- **Metaverse Blokzincir Ekonomisi** — drive_metaverse_week2_nft, drive_metaverse_week3_nft_mintleme, drive_metaverse_week3_akilli_sozlesmeler, drive_metaverse_week3_decentraland, drive_metaverse_week3_dao, drive_metaverse_week10_blockchain [INFERRED 0.85]
- **1002-A Başvuru Kılavuz Seti** — drive_tubitak_1002_a_basvuru_icerigi_bilgi_notu_document, drive_tubitak_1002_a_form_sorulari_yanit_format_rehberi__chatgpt__document, drive_tubitak_1002_a_program_basvuru_rehberi_document, drive_tubitak_1002_a_sablon___degerlendirmeli_document [INFERRED 0.85]
- **NexusOS üç bilimsel sütunu (Kod Küpleri/Şehir, Yerel LLM, İşbirlikçi Güvenlik)** — drive_metaverse_nexusos_1002_a_basvuru_final_sehir_metaforu, drive_metaverse_nexusos_1002_a_basvuru_final_kod_kupleri, drive_metaverse_nexusos_1002_a_basvuru_final_yerel_llm_asistani, drive_metaverse_nexusos_1002_a_basvuru_final_isbirlikci_guvenlik_analizi [EXTRACTED 1.00]
- **12 aylık İş Paketleri İP1-İP4** — drive_metaverse_nexusos_1002_a_basvuru_final_ip1, drive_metaverse_nexusos_1002_a_basvuru_final_ip2, drive_metaverse_nexusos_1002_a_basvuru_final_ip3, drive_metaverse_nexusos_1002_a_basvuru_final_ip4 [EXTRACTED 1.00]
- **Felsefi altyapı: Newton→Leibniz, Kant mavi gözlük, Üçüncül Mekan** — drive_mtvrs_nexusos_projesi_tanim_dok_newtoncu_2d_uzaydan_kacis, drive_mtvrs_nexusos_projesi_tanim_dok_leibniz_iliskisel_uzay, drive_mtvrs_nexusos_projesi_tanim_dok_kant_mavi_gozluk, drive_metaverse_nexusos_1002_a_basvuru_final_ucuncul_mekan [EXTRACTED 1.00]

## Communities (12 total, 0 thin omitted)

### Community 0 - "Literatür ve Atıflar"
Cohesion: 0.15
Nodes (25): Architectural evolution of immersive developer environments (n.d.), VR-based user interactions to exploit infinite space in programming (Bergel, 2021), CityVR: Gameful software visualization (Merino et al., 2017), EK-1 Kaynaklar (1002-A Final), DuoZone: LLM-guided mixed-initiative XR window management (Qian et al., 2025), Software architecture recovery to explore large-scale systems in VR (Hoff et al., 2022), Beyond the screen: XR UX scoping review (Lundkvist & Falkenby, 2024), SLR on fundamental technologies and security challenges in metaverse (2025) (+17 more)

### Community 1 - "NexusOS Çekirdek Konsepti"
Cohesion: 0.13
Nodes (22): TÜBİTAK 1002-A: Risk Yönetimi (B Planı), Göz/Bakış Takibi (Gaze Tracking), İP2 Yerel LLM ve Karma İnisiyatif (5-8 ay), NexusOS (VR-özgü uzamsal işletim katmanı / IDE), Üçüncül Mekan (Third Place), Yerel LLM Mekansal Asistan (karma inisiyatif), Canlı Mimari Görselleştirme, Değerlendirme Soruları ve Nihai Cevaplar (+14 more)

### Community 2 - "Başvuru Bölümleri (Final)"
Cohesion: 0.12
Nodes (22): TÜBİTAK 1002-A: Amaç ve SMART Hedefler (H1-H4), TÜBİTAK 1002-A: 5. Belirtmek İstediğiniz Diğer Konular, TÜBİTAK 1002-A: EK-1 Kaynaklar, TÜBİTAK 1002-A: EK-2 Bütçe ve Gerekçesi, TÜBİTAK 1002-A: 1. Özgün Değer / Bilimsel Nitelik, TÜBİTAK 1002-A: 4. Yaygın Etki (Çıktı/Etki), TÜBİTAK 1002-A: 2. Yöntem, Dinamik HUD (Şeffaf Bilgi Ekranı) (+14 more)

### Community 3 - "Video Senaryoları"
Cohesion: 0.13
Nodes (20): Kuantize Yerel Model (CodeLlama 7B), NexusOS Video-bağlam ve Senaryo, Senaryo 1: SAST ile Hata Ayıklama, Senaryo 2: Göz Takibi ve Otonom Asistan, Senaryo 3: Web3 Eklenti Pazar Yeri, Senaryo 4: Sürükleyici Yazılım Arkeolojisi, Senaryo 5: Uzamsal Organizasyon ile Bilişsel Yük Yönetimi, Senaryo 6: VR-Özgü Canlı Programlama (+12 more)

### Community 4 - "TÜBİTAK Form Kuralları"
Cohesion: 0.25
Nodes (18): Bilimsel Nitelik (1000-4500 kelime), Çıktı, Etki ve Kazanımlar, TÜBİTAK 1002-A Başvuru İçeriği Bilgi Notu, Harici Link ile İçerik Paylaşım Yasağı (iade), Proje Yönetimi (İş Paketleri, İş-Zaman Çizelgesi), Risk Yönetimi ve B Planı, Yöntem (750-4000 kelime), TÜBİTAK 1002-A Form Soruları Yanıt Format Rehberi (ChatGPT) (+10 more)

### Community 5 - "İş Paketleri ve Web3"
Cohesion: 0.18
Nodes (13): TÜBİTAK 1002-A: 3. Proje Yönetimi, Çevik ve Yinelemeli Yöntem (12 ay), DAO (Merkeziyetsiz Otonom Organizasyon), Hibrit Ağ Topolojisi (delta paketleri), İP3 İşbirlikçi Güvenlik ve Ağ (9-10 ay), İP4 Web3/NFT Ekosistemi (11-12 ay), IPFS (Merkezsiz Dosya Sistemi), İşbirlikçi Güvenlik Analizi (SAST, çok kullanıcılı kod şehri) (+5 more)

### Community 6 - "Ders: Blokzincir ve NFT"
Cohesion: 0.23
Nodes (13): Blockchain Teknolojisi, Dijital Dönüşüm, Metaverse Hafta 10 Ders Notu, Metaverse Dersi İçeriği (Müfredat), Metaverse Hafta 1 Ders Notu, NFT (Nitelikli Fikri Tapu), Akıllı Sözleşmeler, Merkezsiz Otonom Organizasyon (DAO) (+5 more)

### Community 7 - "Ders: Deneyim ve Güvenlik"
Cohesion: 0.24
Nodes (10): Metaverse Hafta 7 Ders Notu, Göbekli Tepe Gerçek Zamanlı VR Hikâye Anlatımı, Metaverse Deneyimleri (E-spor, konser, seyahat, terapi, savaş simülasyonu), Metaverse ve Güvenlik / Gizlilik, Metaverse Hafta 8 Ders Notu, Metaverse ve Kripto Teknolojileri, Sonuçlar: Sanallaşma ana akım, siber suç artışı, Metaverse Hafta 9 Ders Notu (+2 more)

### Community 8 - "Ders: Yapay Zekâ ve Pazar"
Cohesion: 0.25
Nodes (9): Gazi Üniversitesi Bilgisayar Mühendisliği, Doç. Dr. Murat Yılmaz (Gazi Üniversitesi), Bağlamsal Anlama (Contextual Understanding), Metaverse Hafta 5 Ders Notu, Metinden Görüntü Araçları (DALL-E 2, MidJourney, Stable Diffusion), Büyüyen Yapay Zekâ Manzarası (LLM, ChatGPT, GPT-4), Metaverse Hafta 6 Ders Notu, Metaverse Pazar Haritası (katmanlar ve şirketler) (+1 more)

### Community 9 - "Ders: VR/AR Temelleri"
Cohesion: 0.60
Nodes (6): Artırılmış Gerçeklik (AR), Metaverse Hafta 2 Ders Notu, Metaverse (Öteevren), Metaverse Yapı Taşları (altyapı, ekonomik model, YZ), Sanal Gerçeklik (VR), Üç Büyük Lens: Teleskop, Mikroskop, VR Gözlüğü

### Community 10 - "Ders: Bilim Kurgu ve OASIS"
Cohesion: 0.67
Nodes (4): Bilim Kurguda Metaverse (Snow Crash, Ready Player One, Matrix), Metaverse Hafta 4 Ders Notu, Haptik Dokunma Teknolojileri (H2L, Emerge Home), OASIS (Ready Player One)

### Community 11 - "Ders: Yıkıcı İnovasyon"
Cohesion: 0.67
Nodes (3): Metaverse Hafta 11 Ders Notu, Genel Amaçlı Teknolojiler (buhar, elektrik, transistör), Yenilik ve Bozulma Teorisi (Disruptive Innovation)

## Ambiguous Edges - Review These
- `Metaverse Dersi İçeriği (Müfredat)` → `Merkezsiz Otonom Organizasyon (DAO)`  [AMBIGUOUS]
  drive/Metaverse_Week1.md · relation: references
- `NexusOS (VR-özgü uzamsal işletim katmanı / IDE)` → `Açık konu: video karma gerçeklik, başvuru VR-özgü diyor`  [AMBIGUOUS]
  drive/video/NexusOS Kling - sahneler.md · relation: conceptually_related_to

## Knowledge Gaps
- **13 isolated node(s):** `Gazi Üniversitesi Bilgisayar Mühendisliği`, `Second Life`, `Fortnite Marshmello Konseri`, `Metinden Görüntü Araçları (DALL-E 2, MidJourney, Stable Diffusion)`, `Metaverse Pazar Büyümesi 2021-2027 (CAGR %29.9)` (+8 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 13 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `NexusOS (VR-özgü uzamsal işletim katmanı / IDE)` connect `NexusOS Çekirdek Konsepti` to `Literatür ve Atıflar`, `Başvuru Bölümleri (Final)`, `Video Senaryoları`, `İş Paketleri ve Web3`?**
  _High betweenness centrality (0.157) - this node is a cross-community bridge._
- **Are the 9 inferred relationships involving `NexusOS (VR-özgü uzamsal işletim katmanı / IDE)` (e.g. with `Toward a VR-native live programming environment (n.d.)` and `XRaSE: Virtually tangible software using AR (Mehra et al., 2019)`) actually correct?**
  _`NexusOS (VR-özgü uzamsal işletim katmanı / IDE)` has 9 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Gazi Üniversitesi Bilgisayar Mühendisliği`, `Second Life`, `Fortnite Marshmello Konseri` to the rest of the system?**
  _13 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Literatür ve Atıflar` be split into smaller, more focused modules?**
  _Cohesion score 0.14532019704433496 - nodes in this community are weakly interconnected._
- **Why does `NexusOS NotebookLM Notebook (96 kaynak)` connect `Literatür ve Atıflar` to `NexusOS Çekirdek Konsepti`, `Başvuru Bölümleri (Final)`, `İş Paketleri ve Web3`?**
  _High betweenness centrality (0.087) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Metaverse Dersi İçeriği (Müfredat)` and `Merkezsiz Otonom Organizasyon (DAO)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `NexusOS (VR-özgü uzamsal işletim katmanı / IDE)` and `Açık konu: video karma gerçeklik, başvuru VR-özgü diyor`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._