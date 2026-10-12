# Kendi UI'ı olan görsel örnekler (WBS 6.1, 2026-10-11)

Kullanıcı notu: düz 2B diyagram altlıkları değil, SEE (metaverse'e yakın) ve CodeCharta (kelime bulutu / şehir) gibi
**kendi zengin arayüzü olan** örnekler aranıyor; özellikle agent'lar arası konuşma.
★ / lisans / son güncelleme GitHub API'den 2026-10-11.

## A. Agent'lar arası konuşma ve çalışma (en çok aranan)

| Repo | ★ | Lisans | Son | Görsel dil | Not |
|---|---|---|---|---|---|
| [a16z-infra/ai-town](https://github.com/a16z-infra/ai-town) | 10.616 | MIT | 2026-08 | 2B piksel kasaba; karakterler yürür, yan yana gelince **konuşur**, konuşma balonları + sohbet geçmişi | Agent konuşmasını en iyi gösteren; TS + Convex. Agent mimarisi değil, sosyal simülasyon |
| [joonspk-research/generative_agents](https://github.com/joonspk-research/generative_agents) | 22.215 | Apache-2.0 | 2024 | "Smallville": Stanford makalesinin kasabası, ajanların günlük planı ve diyalogları | Araştırma kökeni; Python; durgun |
| [pixel-agents-hq/pixel-agents](https://github.com/pixel-agents-hq/pixel-agents) | 9.643 | MIT | 2026-10 | Claude Code agent'ları piksel ofiste: masaya yürür, yazarken yazar, ararken okur, beklerken **konuşma balonu**; alt agent'lar ayrı karakter | Claude Code JSONL kayıtlarını izler, hiç değişiklik gerektirmez; VS Code + `npx pixel-agents` tarayıcı |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | 1.694 | Apache-2.0 | 2026-10 | Claude Code agent orkestrasyonu canlı akış: düşünme, dallanma, koordinasyon | VS Code eklentisi |
| [geezerrrr/agent-town](https://github.com/geezerrrr/agent-town) | 247 | belirsiz | 2026-10 | Piksel RPG ofis; sen patron olarak yürüyüp yüz yüze iş verirsin | OpenClaw gerekiyor |
| [dandacompany/deskrpg](https://github.com/dandacompany/deskrpg) | 166 | belirsiz | 2026-10 | **3B** sanal ofis: agent'lar masada oturur, sohbet eder, **toplantı yapar**, kanban kartı işler | Hermes agent |
| [eliautobot/my-virtual-world](https://github.com/eliautobot/my-virtual-world) | 83 | belirsiz | 2026-08 | 3B sanal dünya (2B sürümü my-virtual-office ★337) | |
| [KbWen/agent-virtual-office](https://github.com/KbWen/agent-virtual-office) | 39 | MIT | 2026-10 | Claude/Codex/Gemini piksel iş arkadaşı: kahve molası, "takıldım", "teslim ettim" | Tarayıcıda |
| [haimadrian/claude-village](https://github.com/haimadrian/claude-village) | 1 | – | 2026-04 | Minecraft benzeri **voksel köy**; her agent kullandığı araca göre temalı bölgeler arasında yürür | Three.js; küçük ama fikir güçlü |
| [BitmapAsset/pepeclaw](https://github.com/BitmapAsset/pepeclaw) | 3 | MIT | 2026-04 | 8 etkileşimli WebGL odası | Three.js + React |
| [OpenBMB/ChatDev](https://github.com/OpenBMB/ChatDev) | 34.481 | Apache-2.0 | 2026-07 | 1.x: sanal şirket, rollerin konuşma kaydı ve tekrar oynatma; 2.0: agent = düğüm tuvali | Visualizer Flask; 2.0'da 2B diyagrama döndü |
| [voicetreelab/agent-canvas](https://github.com/voicetreelab/agent-canvas) | 30 | GPL-3.0 | 2025-12 | Agent'lar graf tuvalinde; ses kökenli | GPL |
| AgentGUI ([arXiv 2607.26300](https://arxiv.org/html/2607.26300v2)) | – | açık kaynak | 2026 | Piksel ofiste çalışanlar; alt agent'lar masanın yanında küçük avatar | Araştırma |

## B. Servisler arası canlı trafik (mikroservis iletişimi)

| Repo | ★ | Lisans | Son | Görsel dil | Not |
|---|---|---|---|---|---|
| [Netflix/vizceral](https://github.com/Netflix/vizceral) | 4.099 | Apache-2.0 | 2023 | WebGL; servisler daire, aralarında **akan parçacıklar** (normal / sarı uyarı / kırmızı hata); bölge → servis → tek servis olarak **içine dalma** | JSON besle (`updateData`), çalışır; React sarmalayıcısı var. Durgun ama kararlı |
| [kiali/kiali](https://github.com/kiali/kiali) | 3.643 | Apache-2.0 | 2026-10 | Istio servis ağı grafiği; trafik animasyonu, hata rengi | Istio gerektirir; ağır |

## C. Kod tabanı (kendi UI'ı olan)

| Repo | ★ | Lisans | Son | Görsel dil |
|---|---|---|---|---|
| [MaibornWolff/codecharta](https://github.com/MaibornWolff/codecharta) | 546 | BSD-3 | 2026-10 | 3B şehir + **Domain görünümü** (klasör başına kelime bulutu), Metric/Domain arası geçiş |
| [uni-bremen-agst/SEE](https://github.com/uni-bremen-agst/SEE) | 29 | MIT | 2026-10 | Unity; masaüstü/VR, **çok kullanıcılı**, avatarlar, sesli iletişim; metaverse'e en yakın |
| [ExplorViz/frontend](https://github.com/ExplorViz/frontend) | 6 | MIT? | 2026-10 | Web 3B şehir, servisler arası çağrı okları, CopilotKit sohbet |
| [anvaka/pm](https://github.com/anvaka/pm) (Software Galaxies) | 1.787 | MIT | 2026-06 | Paketler **galaksideki yıldızlar**; tıkla → bağımlı (yeşil) / bağımlılık (kırmızı) |
| [acaudwell/Gource](https://github.com/acaudwell/Gource) | 13.167 | GPL-3.0 | 2026-03 | Git geçmişi **film** gibi: dosyalar dallanan ağaç, geliştiriciler etrafta uçar |
| [glato/emerge](https://github.com/glato/emerge) | 1.163 | MIT | 2026-08 | Çok dilli (Python dahil) bağımlılık grafiği, Louvain kümeleme; D3 2B |
| [Manavarya09/code-city](https://github.com/Manavarya09/code-city) | 9 | MIT | 2026-06 | Three.js şehir; hatalar yangın, deploy roket, yürüyen karakterler |
| [githubocto/repo-visualizer](https://github.com/githubocto/repo-visualizer) | 1.310 | MIT | arşiv | İç içe daireler; arşivlendi |

## Çıkarım: üç görsel dil, birleştiren yok

1. **Yaşayan karakterler** (AI Town, Pixel Agents, deskrpg, claude-village): agent'ın *ne yaptığını* ve *kiminle konuştuğunu* insanın sezgisiyle gösteriyor; ama kod yapısı yok.
2. **Akan trafik** (Vizceral, Kiali, ExplorViz okları): servisler arası iletişimin *hacmini ve sağlığını* gösteriyor; ama "kim neden konuşuyor" yok.
3. **Kod mekânı** (CodeCharta, SEE, ExplorViz, Software Galaxies): yapıyı gösteriyor; ama canlı aktör yok.

Bizim demoya öneri: **3 + 2 + 1 katman**: kod şehri zemini (ExplorViz/CodeCharta mantığı), servisler arası
Vizceral tarzı akan parçacıklar, ve servislerde çalışan agent'lar şehirde yürüyen/konuşan karakterler
(Pixel Agents / claude-village fikri). Hiçbir repo bunu tek başına yapmıyor; bu ayrışma noktamız.
