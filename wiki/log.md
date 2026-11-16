# Log

## [2026-11-14] schema | 初始化
- 建立目錄結構與 CLAUDE.md（v1）
- 定位：長期追蹤 LLM + RL 應用於無人機的論文；批次匯入；繁中正文、英文檔名

## [2026-11-15] schema | 新增 relevance / rl_role 欄位、teacher 類別、禁用檔名
- 第一批論文裡有 5 篇不是 LLM+RL+UAV 三者都有，所以新增 `relevance: core|adjacent`
- 新增 `rl_role` 欄位（low-level-control / safety-filter / role-selector / resource-optimizer）
- `llm_role` 新增 `teacher`（因應 [[lou2026llm]]）
- 禁用 `claude.md` / `agents.md` 當檔名：Windows 不分大小寫，會被當成指令檔；Claude 模型頁改名為 [[claude-model]]

## [2026-11-15] ingest | 8 papers（core 3 / adjacent 5）
- 新增論文：[[ahn2026hallucination]], [[dong2026hierarchical]], [[wang2025rally]], [[lou2026llm]], [[hiep2026dynamic]], [[song2024local]], [[yanmaz2024dynamic]], [[zhou2023racer]]
- 新增概念：[[hierarchical-llm-rl]], [[llm-hallucination]], [[llm-distillation-lora]], [[safe-rl-cmdp]], [[role-assignment]], [[imitation-learning]], [[ctde]], [[matd3]], [[ppo]], [[attention-critic]], [[entropy-exploration]]
- 新增任務：[[pursuit-evasion-game]], [[cooperative-navigation]], [[multi-uav-routing]], [[autonomous-exploration]], [[multi-target-search]], [[uav-edge-computing]], [[p2p-energy-trading]]
- 新增實體：[[gpt-4o]], [[qwen2-5]], [[deepseek-r1]], [[claude-model]], [[mpe]], [[gazebo-px4-sitl]]
- 新增 synthesis：[[llm-rl-coupling-patterns]], [[paper-comparison]]；改寫 [[overview]]
- 備註：[[hiep2026dynamic]] 引言和結論的數字不一致（比 MAGE-FE 的 BRISQUE 改善分別寫 20% 和 15%）；[[wang2025rally]] 正文沒有具體百分比；部分論文的 url 沒有填（PDF 內沒有 DOI 的就留 null）

## [2026-11-15] ingest | 5 papers（core 0 / adjacent 5）
- 來源：從第一批 core 論文的參考文獻追出，經使用者同意從 arXiv 下載
- 新增論文：[[zhu2025lamarl]], [[xiang2025decentralized]], [[yu2025conavgpt]], [[zhang2026uavgent]], [[cao2025survey]]
- 新增概念：[[llm-reward-design]]
- 新增任務：[[shape-assembly]], [[target-tracking]]
- 修改：[[imitation-learning]], [[hierarchical-llm-rl]], [[llm-hallucination]], [[role-assignment]], [[ctde]], [[matd3]], [[ppo]], [[pursuit-evasion-game]], [[cooperative-navigation]], [[autonomous-exploration]], [[multi-target-search]], [[gpt-4o]], [[mpe]], [[gazebo-px4-sitl]], [[wang2025rally]], [[dong2026hierarchical]], [[ahn2026hallucination]], [[lou2026llm]], [[llm-rl-coupling-patterns]], [[paper-comparison]], [[overview]]
- 備註：這批 5 篇都不是 core。[[cao2025survey]] 是綜述，暫標 adjacent `[taxonomy?]`（core/adjacent 二分不適合綜述）。新增兩個爭議段落：[[ppo]]（MAPPO 好不好用）、[[cooperative-navigation]]（RALLY 與 CI-HRL 對 CI-HRL 泛化能力的描述不同）。[[zhang2026uavgent]] 沒有量化結果、沒寫用哪個 LLM。[[yu2025conavgpt]] 讀的是 v3（標題已從 LLM 改成 VLM）。DITTO 和 LGPF 未收錄（前者與主題無關；後者沒有 arXiv 版）

## [2026-11-15] schema | 簡報視覺規範
- 新增：slides/2026-11-15-llm-rl-uav-overview.html（20 頁，大正和風，內容取自 [[overview]]、[[llm-rl-coupling-patterns]]、[[paper-comparison]] 與 3 篇 core 論文頁）
- 修改：CLAUDE.md §8 補上視覺規範（版型、字體、章節數字、出處與推論標示、預覽方式）
- 備註：新增 .claude/launch.json（本機 server 預覽簡報用）

## [2026-11-15] query | 教學型簡報
- 新增：[[reinforcement-learning]], [[large-language-model]]（入門概念頁，基本定義標明為背景知識）
- 新增：slides/2026-11-15-llm-rl-uav-teaching.html（22 頁，給第一次接觸的人）、slides/2026-11-15-llm-rl-uav-teaching.sources.md（出處對照表＋核對紀錄）
- 修改：[[index]]
- 備註：流程改成「先列出處對照表 → 寫簡報 → 數字自動比對 wiki → 人工核對說法 → 逐頁截圖」。核對時抓到 1 處說得比 wiki 更強（SafeGPT 的 58% 被說成全部來自幻覺），已修正。原本的文獻導讀版保留為進階版

## [2026-11-15] query | 作業說明頁
- 新增：slides/2026-11-15-assignment-report.html（主題、wiki 成果、簡報連結、loop/graph 流程圖、一次執行紀錄、反思）
- 備註：流程圖分三條線（建立規則／匯入迴圈／簡報產生），標出重複與退回的路徑；反思結論是「產生簡報」最常出錯（內容偏離 wiki），檢查已經往前移到出處對照表

## [2026-11-16] schema | 簡報檔名不加日期
- 修改：CLAUDE.md §8（檔名改為 `slides/主題.html`，封面不寫日期）
- 改名：slides/ 下 4 個檔案拿掉 `2026-11-15-` 前綴（assignment-report、llm-rl-uav-overview、llm-rl-uav-teaching、llm-rl-uav-teaching.sources），index.html 與說明頁的連結一起更新
- 備註：兩份簡報封面的日期已移除；上方舊紀錄保留原檔名，不回頭修改

## [2026-11-16] query | 用 graph 流程重做教學簡報
- 新增：slides/llm-rl-uav-intro/（00-brief、01-materials、02-outline、03-content、deck.html、check-log）
- 新增：assets/tools/check_deck_text.py（C4 檢查：HTML 上的文字必須都在 03-content.md 裡）
- 備註：流程為 ⓪ 需求單 → ① 素材 → ② 大綱 → ③ 逐頁內容 → ④ HTML，每一步都有檢查站（C 是自動或自查，G 是使用者確認）。這次沒有任何退回。C2 抓到 3 處結構問題，C3 抓到 3 處說得比 wiki 更強，C4 只剩版面問題（5 處）。舊的教學簡報保留不動。

## [2026-11-16] query | 作業說明頁改為 graph 版
- 修改：slides/assignment-report.html（主要作品改成 slides/llm-rl-uav-intro/deck.html；流程圖的簡報線換成 ⓪～⑤ 加檢查站；執行紀錄換成這次的 check-log；反思補上第二次「檢查往前移」和修改 graph 的原因；連到需求單（需求摘要））
- 備註：graph 版簡報經 G4 定稿
