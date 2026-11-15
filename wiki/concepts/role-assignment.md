---
type: concept
aliases: [角色分派, 任務分配, task allocation, role heterogeneity]
papers: [wang2025rally, dong2026hierarchical, yanmaz2024dynamic, ahn2026hallucination, xiang2025decentralized, yu2025conavgpt, zhang2026uavgent]
updated: 2026-11-15
---

# 角色與任務分派

多無人機系統中，誰負責什麼。從**固定分工**到**動態切換**，是這批論文看得到的演進方向。

## 各論文做法

| 論文 | 角色或任務 | 誰來分派 | 固定或動態 |
|---|---|---|---|
| [[yanmaz2024dynamic]] | 搜尋 / 中繼 | 預先設計 | 固定（DAPP 會臨時指派監控） |
| [[ahn2026hallucination]] | 各自負責的航點扇區 | Global-LLM | 每次規劃 |
| [[dong2026hierarchical]] | 追擊 / 區域防守 / 支援 + 隊形 | 中央 LLM | 每 300 步 |
| [[wang2025rally]] | Commander / Coordinator / Executor | LLM 先驗 + RMIX（MARL） | 動態切換 |
| [[xiang2025decentralized]] | 選哪個錨點（目標區） | 高層 MARL + ConsMAC 共識 | 每 10 步 |
| [[yu2025conavgpt]] | 每台去哪個前沿 | VLM（GPT-4o） | 每 25 步 |
| [[zhang2026uavgent]] | 哪幾台追哪台車 | 底層控制先粗分，LLM 定期重新平衡 | 定期 |

## 發現
- [[dong2026hierarchical]]：任務比例很重要，55:35:10 最佳，比例偏極端時勝率下降、變異變大。
- [[wang2025rally]]：三角色優於雙角色，雙角色時太依賴 Commander，結果不穩定。

## 相關頁面
[[hierarchical-llm-rl]] · [[pursuit-evasion-game]]
