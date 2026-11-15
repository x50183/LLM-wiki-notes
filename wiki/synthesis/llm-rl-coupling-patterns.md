---
type: synthesis
papers: [ahn2026hallucination, dong2026hierarchical, wang2025rally, lou2026llm, zhu2025lamarl, zhang2026uavgent, cao2025survey]
updated: 2026-11-15
---

# LLM 與 RL 的耦合模式

這個領域最關鍵的設計問題：**LLM 的輸出怎麼進入 RL？RL 又怎麼回饋給 LLM？** 從目前收錄的論文，可以整理出四種模式。

## 四種模式

| 模式 | 方向 | 論文 | LLM 何時運作 | 介面 |
|---|---|---|---|---|
| ① **條件注入**：LLM 指令變成 RL 的輸入 | LLM → RL | [[dong2026hierarchical]] | 執行時（每 300 步） | 任務標籤 → embedding 接進 actor 和 critic，加上任務專屬 reward |
| ② **安全把關**：RL 驗證 LLM 方案 | RL → LLM | [[ahn2026hallucination]] | 執行時（每次規劃） | 完整路線 → CMDP 接受或重規劃 |
| ③ **先驗混合**：LLM 先驗 + MARL 線上學習 | 雙向 | [[wang2025rally]] | 執行時（每台 UAV） | 自然語言共識 + RMIX 角色價值 |
| ④ **老師示範**：LLM 產生專家策略或 reward 讓 RL 學 | LLM → RL | [[lou2026llm]]、[[zhu2025lamarl]]（皆非 UAV） | **只在訓練時** | 專家動作 → 模仿項；LLM 寫的先驗策略 → actor 正則項；LLM 寫的 reward → 環境 |

**非 RL 的對照**：[[zhang2026uavgent]] 是「LLM 把關執行」——LLM 定期檢查分散式控制器的結果並修正參考值，方向和 ② 相反，但下層不是 RL（adjacent）。

## 和綜述分類法的對應
[[cao2025survey]] 把 LLM 在 RL 中的角色分成資訊處理者、reward 設計者、決策者、產生器。對照上表：
- ④ 屬於綜述的「reward 設計者」和「決策者 → 專家動作」。
- ①②③ 在綜述的分類裡**找不到明確位置**：綜述以單一 agent 為主，沒有討論「LLM 做高層規劃、RL 做底層」或「RL 把關 LLM」。綜述本身也指出 LLM 增強的 MARL 是空白。

## 比較觀察
- **執行時是否需要 LLM**：①②③ 都需要，所以都得面對延遲和幻覺問題，各自的解法分別是降低呼叫頻率、safe-RL 把關、蒸餾成小模型（見 [[llm-distillation-lora]]、[[llm-hallucination]]）。④ 完全避開了這個問題。
- **④ 的證據變多了**：兩篇不同領域的論文（電力交易、地面多機器人）都顯示 LLM 老師能大幅加速 MARL 收斂（[[zhu2025lamarl]]：樣本效率平均 +185.9%），而且 LAMARL 有實機驗證。
- **誰修正誰**：只有 ② 讓 RL 修正 LLM；①③④ 都預設 LLM 的建議是對的（④ 至少有一個 LLM 自我審查步驟）。
- **評估缺口**：三篇 UAV core 論文都沒有比較「同一個問題換成另一種耦合模式」的效果。

## 研究缺口（候選題目）
> 💭 以下是根據目前 13 篇論文的推論，還需要更多文獻確認：
1. **④ 模式還沒在無人機上出現**：LLM 離線產生專家航線、分派方案或先驗策略程式碼，讓 MARL 模仿，執行時零 LLM 延遲。[[zhu2025lamarl]] 的框架看起來可以直接搬到無人機集群的隊形任務（見 [[shape-assembly]]）。
2. **① + ② 合併**：LLM 指導 RL 的同時，再用 safe-RL 檢查 LLM 的指令。
3. **RL 微調 LLM 本身**（RLHF / GRPO 用在無人機決策）：目前收錄的論文裡完全沒有。
4. **RL 決定何時呼叫 LLM**：讓 LLM 的呼叫頻率由學習決定，而不是固定每 300 步或每 25 步。

## 相關頁面
[[hierarchical-llm-rl]] · [[imitation-learning]] · [[llm-reward-design]] · [[paper-comparison]] · [[overview]]
