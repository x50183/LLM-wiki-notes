# LLM + RL × 無人機 論文知識庫 — Wiki Schema

本專案參考 Karpathy 的 LLM Wiki 模式，長期追蹤「LLM + 強化學習應用於無人機（UAV）」領域的論文。
**使用者負責**：蒐集論文、提出問題、決定方向。
**Claude 負責**：閱讀、摘要、交叉連結、維護一致性，wiki 的所有內容都由 Claude 撰寫與維護。

---

## 1. 目錄結構

```
raw/                  ← 原始資料（只讀，不修改內容）
  inbox/              ← 使用者丟新論文的地方（PDF 等）
  papers/             ← 處理完的 PDF，重新命名為 <key>.pdf
  assets/             ← 從論文擷取的圖片（必要時）
wiki/                 ← Claude 全權維護
  index.md            ← 內容目錄（每次匯入都要更新）
  log.md              ← 時間序紀錄（只能往後追加）
  overview.md         ← 領域總覽與目前的整體觀點（持續修訂）
  papers/             ← 一篇論文一頁
  concepts/           ← 方法、演算法、範式（PPO、RLHF、LLM-as-planner、sim-to-real…）
  tasks/              ← 無人機任務（路徑規劃、導航、集群協同、目標追蹤、降落、空中 VLN…）
  entities/           ← 具名事物：模擬器、資料集、benchmark、模型、硬體平台、研究團隊
  synthesis/          ← 跨論文分析：分類法、比較表、研究缺口、趨勢、問答存檔
slides/               ← HTML 簡報
assets/chibi/         ← 簡報用的 Q 版素材（使用者自行放入）
```

## 2. 語言與命名

- 正文用**繁體中文**，專有名詞保留英文（必要時第一次出現寫成「近端策略最佳化（PPO）」）。
- 檔名一律用**英文 kebab-case**：`concepts/reward-shaping.md`、`tasks/swarm-coordination.md`。
- **禁用檔名**：`claude.md`、`agents.md`（Windows 不分大小寫，會被當成 Claude Code 的指令檔載入）。例如 Claude 模型的頁面要命名為 `claude-model.md`。
- **論文 key** 格式：`第一作者姓氏 + 年份 + 標題第一個實義詞`，全部小寫，例如 `chen2024uavgpt`。key 同時作為：
  - wiki 頁面：`wiki/papers/chen2024uavgpt.md`
  - PDF 檔名：`raw/papers/chen2024uavgpt.pdf`
- 連結使用 Obsidian wikilink：`[[chen2024uavgpt]]`、`[[reward-shaping|獎勵塑形]]`。檔名不可重複，所以連結不用加資料夾路徑。

## 3. 頁面格式

所有 wiki 頁面都要有 YAML frontmatter，方便日後用 Dataview 查詢。

### 3.1 論文頁 `wiki/papers/<key>.md`

```markdown
---
type: paper
key: chen2024uavgpt
title: "完整英文標題"
authors: [Chen, Wang, ...]
year: 2024
venue: ICRA 2024        # 或 arXiv
url: https://arxiv.org/abs/...
relevance: core        # core = LLM+RL+UAV 三者都有；adjacent = 缺其中一項，但方法或場景可借鏡
llm_role: [planner]     # 見 §4 分類法；沒有 LLM 就填 []
rl_role: low-level-control   # RL 負責什麼，見 §4；沒有 RL 就填 null
rl_algo: [PPO]
llm_model: [GPT-4]
tasks: [path-planning]
simulator: [AirSim]
agents: single          # single | multi
real_world: false       # 是否有實機實驗
code: null              # 程式碼連結，沒有就填 null
added: 2026-11-14
---

# 中文短標題

**一句話總結**：……

## 問題與動機
## 方法
（LLM 扮演什麼角色、RL 怎麼用、兩者怎麼銜接；可附簡單架構描述）
## 實驗設定
（環境、baseline、評估指標）
## 主要結果
（附具體數字）
## 限制與未解問題
（論文自己承認的，加上 Claude 觀察到的，兩者要分開標示）
## 與其他論文的關係
- 延伸自 [[...]]、與 [[...]] 對比、被 [[...]] 引用

## 相關頁面
[[concept]] · [[task]] · [[entity]]
```

### 3.2 概念 / 任務 / 實體頁

```markdown
---
type: concept | task | entity
aliases: [中文名, 縮寫]
papers: [key1, key2]    # 提到這個頁面的論文
updated: 2026-11-14
---

# 名稱

定義與說明 → 在 LLM+RL+UAV 脈絡下怎麼用 → 各論文的做法比較（有就列表）→ 爭議與矛盾 → 相關頁面
```

### 3.3 Synthesis 頁
自由格式，但要包含 frontmatter（`type: synthesis`、`papers`、`updated`），而且**每個論點都要附上來源論文連結**。

## 4. 領域分類法（初版，隨著匯入的論文調整）

`llm_role` 的可用值：

| 值 | 意義 |
|---|---|
| `reward-designer` | LLM 產生或修改 RL 獎勵函數（Eureka 類） |
| `planner` | LLM 做高層任務規劃，RL 做底層控制 |
| `policy` | LLM 本身就是策略，經 RL 微調（RLHF / PPO / GRPO 等） |
| `env-generator` | LLM 產生環境、課程（curriculum）或訓練情境 |
| `communicator` | LLM 負責多機之間的溝通與協調 |
| `interface` | LLM 把自然語言指令轉成任務規格 |
| `evaluator` | LLM 做評估、批評或安全檢查 |
| `teacher` | LLM 產生專家策略或示範，讓 RL 模仿（模仿學習 / 先驗策略） |

`rl_role` 的可用值：

| 值 | 意義 |
|---|---|
| `low-level-control` | RL 輸出連續控制或運動指令 |
| `safety-filter` | RL 檢查、接受或拒絕 LLM 的方案 |
| `role-selector` | RL 學習角色或任務分派 |
| `resource-optimizer` | RL 解系統層級的資源或配置最佳化（位置、卸載、頻寬…） |

遇到不屬於上述任何一類的論文：先用最接近的值，並在 log 標記 `[taxonomy?]`，之後由 lint 統一檢討。
`adjacent` 論文照樣寫完整的論文頁，但在 overview 和 synthesis 裡要明確區分，不要拿來當作 LLM+RL+UAV 的證據。

## 5. 工作流程

### 5.1 Ingest（批次匯入）— 預設流程
使用者把 PDF 丟進 `raw/inbox/`，說「匯入」。

1. 列出 inbox 內所有檔案，逐篇閱讀 PDF（長論文分段讀；必要時再看關鍵圖表）。
2. 確定 key，將 PDF 移到 `raw/papers/<key>.pdf`（只改檔名，不改內容）。
3. 撰寫論文頁。
4. 整批讀完後，更新或新增受影響的 concept / task / entity 頁，補上雙向連結。
5. 新論文與舊內容矛盾時，**不要直接覆蓋**：在相關頁面的「爭議與矛盾」段落寫出雙方論點與出處。
6. 更新 `index.md`、`overview.md`（觀點有變才改），並在 `log.md` 追加紀錄。
7. 回報使用者一份**批次摘要**：新增 / 修改了哪些頁面、值得注意的發現、矛盾、不確定的地方、建議追的引用文獻。

一篇 PDF 讀取失敗（掃描檔、加密等）時，留在 inbox，並在回報中說明，其餘論文照常處理。

### 5.2 Query（提問）
1. 先讀 `index.md` 找相關頁面，再深入閱讀；必要時回頭查 `raw/papers/` 原文。
2. 回答時附上 `[[key]]` 引用。wiki 沒有涵蓋的內容要明講，不要用一般知識冒充 wiki 內容。
3. 有保存價值的回答（比較、分析、新發現的連結）存成 `synthesis/` 頁，並記錄到 log。

### 5.3 Lint（健康檢查）
使用者說「lint」時，檢查以下項目並回報，修正前先跟使用者確認範圍：
- 頁面之間的矛盾、被新論文取代的舊說法
- 孤兒頁（沒有其他頁面連進來）、斷掉的連結
- 經常被提到卻沒有獨立頁面的概念
- frontmatter 缺欄位、`llm_role` 分類需要調整的論文
- 研究缺口與建議的新搜尋方向

## 6. index.md 與 log.md

- **index.md**：依 Papers / Concepts / Tasks / Entities / Synthesis 分區，每頁一行：`- [[page]] — 一句話摘要`。論文區依年份排序。
- **log.md**：只能往後追加，每筆的格式固定如下：
  ```
  ## [2026-11-14] ingest | 5 papers
  - 新增：[[a]], [[b]] …
  - 修改：[[c]] …
  - 備註：……
  ```
  類型有 `ingest` / `query` / `lint` / `schema`（修改本檔時）。

## 7. 寫作原則

- **忠於原文**：數字、結論要照論文寫，不確定的地方標 `（待確認）`。
- Claude 自己的推論要標成 `> 💭 觀察：……`，跟論文內容分開。
- 寧可多連結：第一次提到某個概念、任務或實體就加上 wikilink。
- 不修改 `raw/` 內的檔案內容。

## 8. 簡報（slides/）

- 格式：單一 HTML 檔、可翻頁（例如 reveal.js），檔名 `slides/YYYY-MM-DD-主題.html`。
- 風格：**大正和風 × 可愛**（使用者於 2026-11-15 選定）。預設使用 `assets/chibi-taisho/` 的角色，版面搭配和紙底色、藍染與朱紅、傳統紋樣做裝飾，字體用圓潤或明朝體（例如 Zen Maru Gothic、Shippori Mincho）。
  `assets/chibi/`（粉彩卡通）和 `assets/chibi-pixel/`（像素風）保留作為備用，除非使用者指定，否則不使用。
- 內容從 wiki 頁面整理，每頁都要標註論文出處。
- 現有的原創 SVG 角色（`assets/preview.html` 可預覽全部）：
  `drone-chan`（主角）、`drone-chan-happy`（結果、成功）、`drone-chan-thinking`（問題、研究缺口）、
  `llm-bot`（LLM）、`reward-star`（RL 獎勵）、`paper-kun`（論文）、`researcher`（研究者）。
  共用配色：外框 `#5A4A5E`、粉 `#FFD6E0`、紫 `#CDB4F0`、薄荷 `#B8E6D2`、黃 `#FFE08A`、腮紅 `#FF9AA2`。
  需要新角色或表情時，沿用同樣的線條粗細（4px）和配色加畫。
- **像素風版本**（`assets/chibi-pixel/`，同一組角色與檔名）：由 `assets/tools/pixel2svg.py` 把 16×16 點陣格子轉成 SVG。
  要修改或新增時，編輯腳本裡的格子再重新執行，不要手改 SVG。在 HTML 裡要加 `image-rendering: pixelated`。
- **大正和風版本**（`assets/chibi-taisho/`，同一組角色與檔名）：受和風熱血動漫啟發的原創設計，有頭巾、傳統紋樣（青海波、七寶、矢絣）、浮世繪風的波浪與火焰、印章。
  配色：墨色外框 `#2B2024`（4.5px）、藍染 `#2E3A6B`、朱紅 `#B8323C`、金 `#D9A441`、和紙 `#F4EAD5`；腮紅用斜線 `///`。
  **不要**加入任何現有動漫作品的角色辨識元素（特定角色的羽織花色、耳飾、作品標誌文字等），簡報可能公開。
- **視覺規範**（2026-11-15 第一份簡報 `slides/2026-11-15-llm-rl-uav-overview.html` 定下，之後沿用同一份 CSS）：
  - reveal.js 5.1.0（cdnjs），畫布 1280×720，`center:false`、轉場 `fade`、頁碼 `c/t`。
  - 底色和紙 `#F4EAD5` 加細點紋理；一般頁左側 22px 矢絣帶、底部青海波帶（都用 CSS data-URI SVG）。
  - 標題用 Shippori Mincho 800，左邊放一個朱紅外框、旋轉 -6° 的單字印章（例如「補」「層」「型」）；內文用 Zen Maru Gothic。
  - 章節頁用大字數字「壱 弐 参 肆」（不要用「一」，看起來像橫線）。
  - 卡片：淡和紙底、2.5px 墨色外框、上緣 10px 色帶（藍染 / 朱紅 / 金）、硬陰影。
  - 每頁右下或底部 `.src` 標註出處，寫論文 key；Claude 的推論用 `.note.obs`，標成「💭 觀察（推論，非論文結論）」。
  - 角色用 `<img src="../assets/chibi-taisho/*.svg">` 引用（不要內嵌，SVG 內的 id 會衝突）。
  - 預覽：`.claude/launch.json` 的 `slides` 設定會在 127.0.0.1:8765 起本機 server；直接開 file:// 時圖片不會載入。

---
本檔由使用者與 Claude 共同演進；有修改時要在 log.md 記一筆 `schema`。
