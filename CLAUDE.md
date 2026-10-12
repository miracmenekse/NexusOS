# NexusOS

Yazılım geliştirmeyi 2B ekrandan VR'a özgü 3B uzamsal işletim katmanına taşıma fikri. Metaverse dersinde
(Doç. Dr. Murat Yılmaz) doğdu, TÜBİTAK 1002-A başvurusu olarak yazıldı, şirketin Ar-Ge projesine taşınıyor.
Bileşenler: Şehir Metaforuyla 3B kod şehri (AST), yerel LLM destekli karma inisiyatifli pencere yönetimi
(DuoZone), 3B işbirlikçi güvenlik/mimari analiz (SecCityVR), Web3/NFT eklenti pazar yeri, OASIS etiği, B2B.
Literatür haritası: `kaynaklar/notebooklm/notebooklm1.md` (96 kaynak). Rakipler: `kaynaklar/manus/`.
Felsefe: Newtoncu 2B ekrandan Leibniz'in ilişkisel uzayına, Kant'ın "mavi gözlük"ü, "Üçüncül Mekan",
"Üç Büyük Lens"; %100 yerel (bulutsuz) mimari. Senaryolar: `kaynaklar/drive/NexusOS Video-bağlam ve senaryo.md`.
Başvuru: `kaynaklar/drive/Metaverse-NexusOS 1002-A Başvuru Final.md` (eski form yapısında, risk r7);
esas kural resmi `TÜBİTAK 1002-A Başvuru İçeriği Bilgi Notu.md` (kelime sınırları, 12 ay, İP/B planı).
Kullanıcı dosyaları teker teker anlatıyor; öğrendikçe bu özeti büyüt.

**Yön (2026-10-11, d10):** NexusOS yalnız esin kaynağı. Hedef yeni Ar-Ge projesi: kod, agent ve dijital ikiz
yapılarını görselleştiren, az tuşla, konuşarak ve dokunarak kullanılan fütüristik HCI arayüzü. VR YOK
(dijital ikiz). Örnek: agentların konuştuğu 2B arayüzler (Claude vb.), ama görsel olarak farklı.
TÜBİTAK dosyasını tamamlamak hedef değil; şimdilik projeyi anlama + yeni projeye hazırlık.
Ana video: Luma (`kaynaklar/drive/video/demo sahneler.md`).

**Çıktılar (d15):** Ç1 kod mekânı, Ç2 servis trafiği, Ç3 yaşayan agent'lar — ayrı demolar (WBS 6.3-6.5).
**Yön (2026-10-12, d18-d20):** Ç1 = Neon şehir (`demo/tasarim/index.html`, ExplorViz yalnız referans). Ç3 = agent
görselleştirme altlığı (ortak olay modeli); sprite ofis ve ağ onun örnek görünümleri. Ses/dokunma ertelendi.
**Demolar:** `bash demo/run.sh` hepsini açar (4400: Ç1 `/sehir`, Ç2 `/`; 4500: statik). Ç3 olay modeli ve doğrulayıcı
`demo/agents/altlik.py` (docstring = biçim); görünümler `?data=<model>.json` okur. Eskiler `demo/arsiv/`. Proje git'te.
**Sunum verisi:** önemli iş bitince `nexusos-sunum` skill'iyle `sunum/sunum-verisi.md`'ye kayıt ekle.

**Analiz bölüşümü (d11):** Dokümanları burada özetleme/kopyalama. Önemli dosyaları kullanıcı doğrudan verir,
Claude onları okur; geniş tarama ve özetler için NotebookLM köprü kartı yaz.
**YZ işleri Claude'da (d14):** Manus'a görev verme. Web araştırması, plan ve kod Claude'da; köprü yalnız
verinin zaten durduğu yer için (NotebookLM, Drive).

## Pano (kullanıcının günlük ekranı, iş durumu burada)
https://claude.ai/artifact/5ieGH9T4MNU3CN7d6ZqvRF — kaynak: `pano/index.html` (+ `demo/` sayfaları ve
`img/` görselleri aynı yayına `files` ile gider; yeniden yayında aynı `files` haritasını ver).
Koleksiyonlar: `isler` (doc id = WBS kodu; kod, ad, durum `yapilacak|yapiliyor|bekliyor|bitti`, sira,
kimde, grup = kategori (İşler sekmesi buna göre gruplar), karar = bekleyen karar, neden = neden yapılmadı,
teslim; bitenlerde sonuc), `demolar`
(cikti, ad, yer `panel|yerel`, ozet, karar, sayfalar[{ad,yol}], komut, adres, gorsel, sira),
`adim/simdi` (baslik, aciklama, isler[], claude, aksiyonlar[{soru, neden, adimlar[], secenekler[{ad,
aciklama, demo, oneri}], cevap, not}], sonra[]). Kullanıcı aksiyonları panelden cevaplar.
- Oturum başında `adim/simdi` oku; `cevap`ı dolu aksiyonları işle (karar → eski paneldeki `decisions`).
- Her iş bitince ya da adım değişince `isler` ve `adim/simdi`'yi güncelle: pano her zaman güncel adımı göstermeli.
- Yeni demo çıkınca `demolar`'a ekle; statik sayfaysa yayına dahil et.

## Panel (kayıt arşivi: charter, kararlar, riskler, köprüler)
https://claude.ai/artifact/DDmawF2kHNmhvE18LPrpbJ — kaynak: `panel/index.html`. Eski `wbs` koleksiyonunun
yerini panodaki `isler` aldı (2026-10-12).
Veri `ArtifactData` ile okunur/yazılır. Koleksiyonlar: `charter` (doc `main`), `wbs` (doc id = WBS kodu;
alanlar: kod, ad, ust, durum, teslim, kabul, bagimli[], raci{R,A,C[],I[]}, not), `bridge`, `sources`,
`stakeholders`, `risks` (olasilik/etki 1-5), `decisions` (tur: karar | degisiklik | ders).
Durumlar: wbs `yapilacak | yapiliyor | dis_bekliyor | bitti`; bridge `bekliyor | cevaplandi`;
risks `acik | kapali`. Yazarken her zaman okuduğun `version`'ı `if_version` olarak ver.

## Yönetim kuralı: PMBOK, takvimsiz, iş bazlı
- Oturum başında panodaki `adim/simdi` ve `isler`, paneldeki `bridge` oku; kaldığımız yeri ve sıradaki işi tek satırla söyle.
- Bir iş bitince: WBS durumunu `bitti` yap, yeni kararı `decisions`'a yaz, gerekiyorsa riskleri güncelle.
- Düzenli rapor, tarih, sprint yok. İlerleme = biten yaprak iş / toplam.
- Kapsam değişirse `decisions`'a `degisiklik` kaydı aç, sonra WBS'i düzelt.

## Köprü protokolü (NotebookLM, Rovo, Manus)
Bilgi bu araçlardaysa tahmin etme; köprü kartı üret, hem sohbette göster hem `bridge`'e yaz:
hedef + tam yer, neden (WBS kodu), adım adım yönlendirme, tek kopyalanabilir prompt, beklenen çıktı.
- NotebookLM prompt'u: yalnız kaynaklara dayan, her iddiaya kaynak numarası.
- Rovo prompt'u: Jira anahtarı ve Confluence linki iste; kullanıcıya gizli bilgiyi ayıklamasını hatırlat.
Cevap yapıştırılınca: `kaynaklar/<araç>/<YYYY-MM-DD>-<konu>.md` (soru + cevap), kartı `cevaplandi` yap
ve `dosya` alanını doldur, `sources` son eşitleme tarihini güncelle, grafı güncelle.

## Kaynaklar ve graf
- `kaynaklar/{drive,notebooklm,odevler,manus,rovo}/` — Drive dokümanları bağlayıcıdan markdown olarak;
  diğerleri VS Code sürükle-bırak ya da köprü cevabı. Drive kökü: "METAVERSE (ÖTE-EVREN)" klasörü.
- Headroom proxy araç çıktısını `<<ccr:hash>>` ile kırpar: Drive içeriğini diske
  `curl -s 127.0.0.1:8787/v1/retrieve/<hash>` (alan `original_content`) ya da oturum `.jsonl`'ından yaz;
  büyük dosyayı okumak yerine grep/python ile sorgula.
- Proje sorusunda `graphify-out/graph.json` varsa önce `graphify query`. Yeni kaynakta
  `/graphify kaynaklar --update` (ilk sefer `/graphify kaynaklar`). Video dökümü Firefox kapalıyken,
  sudo'suz: `uv run --with imageio-ffmpeg` (kare/ses) + `--with faster-whisper` (sesi numpy dizisi ver; `av` uyumsuz).
- Jira/Confluence'a doğrudan bağlanma (kullanıcı kararı). Rovo analizi WBS 4.1 (köprü b3),
  konseptten önce; yeni çıktılar aynı şirket Ar-Ge projesine bağlanır (d12). Ana makineden VM'e dosya yalnız sürükle-bırak.
