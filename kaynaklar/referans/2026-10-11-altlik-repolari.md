# Altlık repo taraması (WBS 6.1, 2026-10-11)

Soru: mikroservis kod tabanı görselleştirme demosu için hazır alabileceğimiz bir repo var mı?
Yıldız, lisans ve son güncelleme GitHub API'den 2026-10-11'de alındı.

## Sonuç: ExplorViz frontend + backend-mock

| Parça | Ne | Durum |
|---|---|---|
| [ExplorViz/frontend](https://github.com/ExplorViz/frontend) | Kod şehri arayüzü. **React + react-three-fiber + drei**, three-forcegraph, @react-three/uikit (3B içinde UI), @react-three/xr (isteğe bağlı), **CopilotKit sohbet** | TypeScript, 2026-10-08 güncel. package.json lisansı **MIT**; kökte LICENSE dosyası yok, kullanmadan önce ekiple teyit |
| [ExplorViz/backend-mock](https://github.com/ExplorViz/backend-mock) | Tüm backend'in yerine geçen küçük Node/Express uygulaması; `demo-data/<sistem>/structure.json` ve `dynamic.json` dosyalarını sunuyor | Apache-2.0. PetClinic, OpenTelemetry Demo, Kieker örnek verisi içinde |
| [ExplorViz/ai-chat-serivce](https://github.com/ExplorViz/ai-chat-serivce) | Frontend'deki sohbet botunu OpenAI / **Anthropic** / Google'a bağlayan CopilotKit servisi | "Konuşarak etkileşim" hedefi için hazır başlangıç noktası |
| [ExplorViz/trace-generator](https://github.com/ExplorViz/trace-generator) | Sahte uygulama yapısı ve OpenTelemetry trace'i üreten web aracı | Test verisi için |
| [ExplorViz/code-analyzer](https://github.com/ExplorViz/code-analyzer) | Git reposundan statik analiz | **Yalnız Java**; Python servislerimiz için kendi küçük analizcimizi yazacağız |

Neden bu: görsel dil (iç içe mahalleler, bina = sınıf/dosya, servisler arası kavisli yönlü çağrı okları) zaten var;
modern React/r3f yığını üstüne kendi tasarımımızı (ses, dokunma, bağlamsal panel) eklemek kolay; mock ile **Kafka, Java,
Neo4j olmadan** çalışıyor.

### Veri biçimi (backend-mock)
```
structure.json
  landscapeToken
  cities    {id: {id, name, fqn, originOfData, districtIds[], buildingIds[], allContained…}}   ← servis
  districts {id: {id, name, fqn, parentCityId, parentDistrictId, districtIds[], buildingIds[]}} ← paket/klasör
  buildings {id: {id, name, fqn, parentCityId, parentDistrictId, language}}                    ← dosya/sınıf
dynamic.json
  metrics {executionTime, functionCount, requestCount: {min,max}}
  communications [{id, name, sourceBuildingId, targetBuildingId, isBidirectional,
                   metrics {executionTime, functionCount, requestCount}}]                       ← çağrı
```
Uç noktalar: `/v3/<token>/structure/runtime`, `/dynamic`, `/file-communication`, `/timestamps`, `/repositories`, `/commit-tree/…`.

### Ortam
- VM'de Node 24 var; pnpm ve Docker yok. pnpm `npx`/corepack ile gelir; backend-mock Docker'sız `node` ile çalışabilir.
- Frontend rehberi Node 20 istiyor (24 ile denenecek). Bellek ~2,9 GB boş: Vite dev sunucusu için yeterli olmalı.

## Diğer adaylar

| Repo | ★ | Lisans | Son | Not |
|---|---|---|---|---|
| [MaibornWolff/codecharta](https://github.com/MaibornWolff/codecharta) | 546 | BSD-3 | 2026-10-10 | Olgun kod şehri; cc.json (CSV importer ile özel veri). Servisler arası canlı çağrı yok. İkinci görünüm adayı |
| [MaibornWolff/DependaCharta](https://github.com/MaibornWolff/DependaCharta) | 17 | BSD-3 | 2026-10-11 | Çok dilli bağımlılık analizi + web stüdyo; statik bağımlılık için kullanılabilir |
| [Manavarya09/code-city](https://github.com/Manavarya09/code-city) | 9 | MIT | 2026-06-20 | Tamamen tarayıcıda, Three.js; "hatalar yangın, deploy roket". Görsel ilham |
| [rodrigo-brito/gocity](https://github.com/rodrigo-brito/gocity) | 1809 | MIT | 2025-12-05 | Go kodu için; web görselleştirici |
| [aserg-ufmg/JSCity](https://github.com/aserg-ufmg/JSCity) | 1400 | GPL-2.0 | 2019 | Eski, GPL |
| [uni-bremen-agst/SEE](https://github.com/uni-bremen-agst/SEE) | 29 | MIT | 2026-10-11 | Unity, işbirlikçi; masaüstü/VR, web değil |
| [softvis-research/Getaviz](https://github.com/softvis-research/Getaviz) | 53 | Apache-2.0 | 2023 | Model güdümlü üreteç, durgun |
| [AOEpeople/vistecture](https://github.com/AOEpeople/vistecture) | 88 | Apache-2.0 | 2025-11 | YAML'dan servis grafiği (Graphviz); düz |
| [cloudhubs/prophet](https://github.com/cloudhubs/prophet), [clowee/MicroDepGraph](https://github.com/clowee/MicroDepGraph) | 3 / 14 | Apache / – | 2024 / 2021 | Mikroservis mimarisi geri kazanımı, yalnız Java/Spring |
| [FudanSELab/train-ticket](https://github.com/FudanSELab/train-ticket) | 917 | Apache-2.0 | 2025-11 | Büyük Java mikroservis benchmark'ı; bize fazla |

## Önerilen yol (6.2 / 6.3)
1. ExplorViz frontend + backend-mock'u VM'de PetClinic verisiyle ayağa kaldır (Docker'sız). Çalıştığını gör.
2. 4 Python mikroservisi yaz (gateway, orders, inventory, payments; stdlib).
3. `analyze.py`: stdlib `ast` ile servis → city, klasör → district, dosya → building; route ↔ istemci çağrısı eşlemesiyle
   `communications`. Çıktıyı `backend-mock/demo-data/NexusOS Demo/` altına yaz.
4. Servisler çalışırken çağrı sayısı/süresi kaydedilip `dynamic.json` güncellenir (canlıya yakın).
5. Sonra kendi katmanımız: ses komutu (CopilotKit sohbetinin yanına), dokunma, Luma'daki "hata → panel → onar" akışı.
