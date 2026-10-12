# Referans taraması (WBS 3.2, 2026-10-11)

Amaç: kod, agent ve dijital ikiz görselleştiren; ses ve dokunmayla, az tuşla kullanılan arayüz için
mevcut örnekleri ve boşluğu görmek. Kaynak: web taraması (aşağıda linkler).

## 1. Agent görselleştirme

| Referans | Ne yapıyor | Bizden farkı |
|---|---|---|
| [agent-flow](https://github.com/topics/agent-visualization) (VS Code eklentisi, 1,7k yıldız) | Claude Code agent'larının düşünmesini, dallanmasını, koordinasyonunu canlı gösteriyor | Gözlem aracı; düğüm-kenar akışı, etkileşim fare ile |
| [zoetrope](https://github.com/topics/agent-visualization) | Claude Code / Codex oturumunu canlı akış grafiği olarak (terminal/tarayıcı) | Salt izleme |
| [AgentGUI](https://arxiv.org/html/2607.26300v2) (arXiv 2026) | Uzun süren agent filolarını piksel-art ofiste "çalışan" olarak gösteriyor; alt agentlar masanın yanında küçük avatar | Metafor güçlü (ofis), ama oyunlaştırılmış; kod/dijital ikiz yok |
| [agent-canvas](https://github.com/voicetreelab/agent-canvas) (voicetree) | Kodlama agent'larını graf tuvalinde düğüm olarak yönetme | Ses kökenli (voicetree) ama tuval klasik graf |
| [tldraw "fairies"](https://gitnation.com/contents/agents-on-the-canvas-with-tldraw-3450) | Sonsuz tuvalde çok agent + çok kullanıcı gerçek zamanlı işbirliği | Tuval 2B çizim; mimari/kod modeli yok |
| [LangGraph Studio](https://mem0.ai/blog/visual-ai-agent-debugging-langgraph-studio) | Agent grafiği canlı, düğümde durdurma, durum düzenleme, zaman yolculuğu | Geliştirici hata ayıklama IDE'si; çerçeveye bağlı |
| [Multi-agent debugging](https://arxiv.org/pdf/2503.02068) (arXiv) | Mesajları commit grafiği gibi zaman çizelgesinde, dallandır/sıfırla | Zaman ekseni fikri değerli |
| [MIVAIS](https://arxiv.org/pdf/2609.04983) (arXiv 2026) | Agent'lar yayın/abone kanallarıyla konuşuyor; her mesaj kayıtlı | Mimari model, görsel dil değil |

## 2. Kod görselleştirme (kod şehri)

| Referans | Ne yapıyor | Bizden farkı |
|---|---|---|
| [CodeCharta](https://codecharta.com/) (MaibornWolff, açık kaynak) | Dosya = bina, klasör = mahalle; alan/yükseklik/renk = metrik (karmaşıklık, commit…); sıcak noktalar | Statik metrik haritası; agent ve ses yok. NexusOS'un "kod şehri" fikrinin olgun hâli |
| [CodeScene](https://javapro.io/2025/10/21/map-your-code-master-your-architecture/) | İç içe dairelerle kod sağlığı + Git sıcak noktaları | 2B, analiz odaklı |
| CodeCity (2009), Seerene, CrocoCosmos | Kod şehri öncüleri | Eski / kurumsal |

## 3. Dijital ikiz

| Referans | Ne yapıyor | Bizden farkı |
|---|---|---|
| [Siemens Digital Twin Composer](https://news.siemens.com/en-us/digital-twin-composer-ces-2026/) (CES 2026, NVIDIA Omniverse) | 2B+3B ikiz verisini canlı sensörle fotogerçekçi sahnede birleştiriyor; AI agent'lar değişiklikleri simüle ediyor | Fiziksel tesis ikizi; yazılım ikizi değil |
| [Siemens Industrial Copilot](https://press.siemens.com/global/en/pressrelease/ai-industry-schaeffler-and-siemens-bring-industrial-copilot-shopfloor) | Operatör makineye doğal dille hatayı soruyor; agent'lar plan yapıp eylem alıyor. Ses "ileride" denmiş, doğrulanmadı | İkizle bağı belirsiz; yazarak soru |
| [Snap4City](https://www.snap4city.org/drupal/node/749) | Akıllı şehir ikizi: katmanlar, IoT, ne-olursa analizi | Şehir, yazılım değil |
| Yazılım ikizi literatürü | [DTInsight](https://arxiv.org/pdf/2508.18431); mikroservis mimarisi geri kazanım ve görselleştirme derlemeleri (Cerny vd. 2022, 2024) | "Yazılımın dijital ikizi" araç olarak neredeyse yok |

## 4. Ses + dokunma etkileşimi

| Referans | Bulgu |
|---|---|
| ["Put-that-there"](https://arxiv.org/pdf/2007.09809) (Bolt, 1980) | Ses + işaret etmenin klasik çıkış noktası |
| [Orko](https://arxiv.org/pdf/2004.14505) (arXiv) | Ağ görselleştirmede dokunma + konuşma: düğüme dokun, kement çiz ya da söyle |
| ["Hey Dashboard!"](https://arxiv.org/pdf/2510.12386) (arXiv) | Panoda ses + yazı + işaret etme; bas-konuş |
| [Klavyenin çözülmesi](https://arxiv.org/pdf/2604.17023) (arXiv 2026) | Ses uzamsal bütünlüğü bozar; çözüm: **ses = ne yapılacak, dokunma/bakış = nerede, görsel = onay** |
| [Multimodal UX ilkesi](https://designdecade.org/multimodal-ux-design-how-to-design-for-voice-touch-and-gesture-simultaneously/) | "Ses fiili verir, jest nesneyi" |
| [Sesli geliştirici araçları](https://inworld.ai/resources/best-ai-infrastructure-developer-assistants) | Cursor 2.0 ses modu, Copilot ses komutları, Deepgram Saga, Codex dikte. Hepsi sesi metin kutusuna çeviriyor; görsel model yok |

## Boşluk (bizim yerimiz)

Hiçbir araç şu üçünü birlikte yapmıyor:
1. **Tek canlı model:** kod yapısı + çalışan agent'lar + (yazılımın/sistemin) dijital ikizi aynı görünümde.
2. **Görsel dil:** agent araçları düğüm-kenar ya da oyunlaştırılmış; kod araçları statik şehir haritası. Arada, Luma videosundaki gibi "dokun → bağlamsal panel → onar" akışı olan sinematik bir katman yok.
3. **Ses + dokunma birlikte:** sesli araçlar sesi metne çeviriyor; "bu modüle dokun + 'bunu neden çağırıyor?' de" türü birleşik etkileşim yalnız araştırma prototiplerinde (Orko, Hey Dashboard).

## Konsepte (4.2) taşınacak tasarım fikirleri

- Ses = fiil, dokunma = nesne, görsel = onay (birleşik komut).
- Yakınlaştırma seviyeleri: sistem şehri → modül küpü → agent/fonksiyon (CodeCharta metrik eşlemesi + Luma'nın iki ölçeği).
- Agent'lar şehirde hareket eden varlıklar; mesajlar aralarında akan ışık hatları; zaman çizelgesiyle geri sarma (multi-agent debugging).
- Hata/sağlık rengi (kırmızı → mavi) canlı veriden (SAST, test, telemetri) gelir.
