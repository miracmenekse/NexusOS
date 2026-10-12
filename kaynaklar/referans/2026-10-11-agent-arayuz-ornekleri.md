# Agent arayüzü örnekleri (web araştırması)

WBS 6.5. İstek: kullanıcı 5 ekran görüntüsü gönderip "başka en iyi örnekler olabilir, araştır" dedi.

Araştırdım. Gönderdiğin 5 görsel ve bulduğum örnekler şu desenlerde buluşuyor. Bulduğum örneklerin hiçbirini açıp denemedim, bilgiler arama sonuçlarındaki özetlerden geliyor.

## Görsellerden çıkan desenler
| Görsel | Desen | Bizim demoya karşılığı |
|---|---|---|
| 1 (beyin + kaideler) | Ortada tek "beyin", etrafında kaideler, aralarında akan parlak kablolar | Orkestratör merkezde, agent'lar kaidede |
| 2 (yeşil ışık çizgileri) | Kişi avatarları, çizgiler üzerinde akan ışık, üstte yüzen panel ekranları | Ağ görünümüne üstte canlı panel şeridi |
| 3 (ışıklı ızgara) | Karanlık ızgara zemin, üstünde duran robot kafaları | Neon kasaba: ızgara zemin, parlayan yollar |
| 4 (ofis masaları) | Merkezde beyin küpü, masalarda robotlar, havada yüzen belgeler | Agent'ın elindeki işi (belge, grafik, uyarı) yanında kart olarak göstermek |
| 5 (ağaç/orman ayarları) | Metrik → görsel eşleme (gövde/yaprak yüksekliği, yarıçap, renk) | Ç1 kod şehri alternatifi: sınıf = ağaç |

## Bulduğum örnekler
**Agent görselleştirme**
- [Pixel Agents](https://open-vsx.org/extension/pablodelucca/pixel-agents): Claude Code agent'larını piksel ofiste gösterir. Masaya yürürler, dosya düzenlerken yazar, aramada okur, onay beklerken uyarır. Alt agent'lar ayrı karakter. Oturum kayıtlarını izler, Claude Code'a dokunmaz. Zaten referans tablomuzda var.
- [zkblk/pixel-agents](https://github.com/zkblk/pixel-agents): İzometrik ofis ve Slack tarzı sohbet paneli. İzometrik görünüm Neon şehirle uyumlu.
- [AI Town (a16z)](https://the-decoder.com/ai-town-lets-you-build-your-own-gpt-based-ai-civilization/): Stanford Smallville'in açık kaynak yeniden yapımı, MIT lisanslı. Karakterler yürür, konuşma balonu çıkar. PixiJS render'ı bilgisi düşük güvenilirlikli bir kaynaktan. Kasaba demomuz bunun hafif sürümü.
- [Lantern PR #30](https://github.com/alyakan/lantern/pull/30): Agent'lar daire, çevresinde durum halkası (çalışırken döner, bitince yeşil, hatada kırmızı). Alt agent ya da araç başlayınca kenar boyunca nabız akar, çalışan kenar "yürür". Düz SVG, ek bağımlılık yok. Ağ görünümüne en doğrudan uyan fikir.
- [Microsoft Conductor](https://opensource.microsoft.com/blog/2026/05/14/conductor-deterministic-orchestration-for-multi-agent-ai-workflows/): Canlı DAG, kenarlarda akış animasyonu (MIT).
- [Growth-swarm #4](https://github.com/Fergus-MW/growth-swarm/issues/4): Ortada bilgi grafiği, çevrede agent izleme kutuları ve bekliyor/çalışıyor/bitti/hata durumları. Görsel 4'e yakın bir tasarım tarifi.
- [agenciavepo/ai-agents-orchestration-platform](https://github.com/agenciavepo/ai-agents-orchestration-platform): Avatar tabanlı ekip yönetimi. Görsel 2'ye en yakın olan.
- Stil için: [frankx.ai](https://www.frankx.ai/research/visual-catalog) koyu lacivert (#0a0e1a) zemin, cyan/zümrüt/altın/mor/turuncu agent renkleri öneriyor. Bizim paletimiz zaten buna yakın.

**Kod şehri ve orman (görsel 5)**
- [CodeForest (Ritsumeikan, ICPC 2014)](https://www.fse.cs.ritsumei.ac.jp/codeforest/icpc2014-maruyama.pdf): Java sınıfı = ağaç, ormanda birçok metrik eşlemesi deneniyor. Görsel 5'e en yakın aday ama tam hangi araç olduğunu, hangi metriğin gövdeye hangisinin yaprağa gittiğini doğrulayamadım. Makaleyi okumak gerekir.
- [CodeCharta](https://codecharta.com/docs/overview/visualization): Bina yüksekliği, taban ve renk için ayrı metrik seçilir (varsayılan: rloc, karmaşıklık). RFC ve CBO yerleşik görünmüyor, ama açık JSON biçimiyle kendi değerini aktarabilirsin.
- [Software Forest](https://www.researchgate.net/publication/349382985_Software_Forest_A_Visualization_of_Semantic_Similarities_in_Source_Code_using_a_Tree_Metaphor): Anlamsal benzerliğe göre yerleştirilmiş orman. [Maya makalesinde](https://arxiv.org/pdf/1603.00418) ağaç = sınıf, her kat = metot.
- Orijinal CodeCity (Wettel & Lanza): Kullanıcılar mimari görevleri %20 daha hızlı bitirmiş (kaynak özetinden, doğrulanacak).

**Bulamadığım:** "NVIDIA tarzı avatar ekibi" için hazır bir UI örneği çıkmadı. Sonuçlar Omniverse dijital ikiz bloglarıydı. Bu da görsel 2'nin sadece konsept çizimi olabileceğini düşündürüyor.

## Önerim
1. **Ağ görünümüne** Lantern'in durum halkası ve nabız fikrini, görsel 4'ün yüzen iş kartlarını ekleyelim. En küçük iş, en görünür kazanç.
2. **Kasabayı** görsel 3'e göre koyu ızgara zeminli, parlayan yollu bir Neon sürüme çevirelim.
3. **Kod şehrine** (Ç1) "orman" modu için önce CodeForest makalesini okuyalım.

Hangisinden başlayalım? İstersen bulduklarımı `sunum-verisi.md`'deki referans projeler tablosuna da işleyeyim.
