---
type: task
aliases: [多無人機對抗, UAV game, 追逃賽局, pursuit-evasion, DS-CEFC]
papers: [dong2026hierarchical, wang2025rally, xiang2025decentralized]
updated: 2026-11-15
---

# 多無人機對抗與追逃

兩隊無人機在同一空域互動：一方追擊或攻擊，另一方規避或防守。這批論文中 **LLM+RL 最集中的任務**。

## 問題設定比較

| | [[dong2026hierarchical]] | [[wang2025rally]] |
|---|---|---|
| 情境 | 5v5 對抗（近距離交戰） | DS-CEFC：躲避追擊者，同時用隊形覆蓋目標 |
| 對手 | 專家規則系統 | 追擊者（細節待確認） |
| 維度 | 2D、固定高度 | 2D、固定高度（MPE / SITL） |
| 指標 | 勝率、交換比、reward | 任務覆蓋率、reward、泛化 |
| 最佳結果 | 勝率 82% | 優於 CIHRL / CoNavGPT / DITTO（以圖呈現） |

**純 MARL 的對照組（adjacent）**：[[xiang2025decentralized]]（CI-HRL）做的是和 RALLY 相同的 CEFC 任務，8 台、2D 固定高度，對手是訓練過的 PPO 追捕者，有 SITL 驗證，但沒有 LLM。它是 RALLY 的主要 baseline，也是同團隊的前作。

> 💭 觀察：所有論文都是固定高度的 2D 設定。對手方面，[[dong2026hierarchical]] 用規則系統；[[xiang2025decentralized]] 用預先訓練好的 PPO 策略（之後固定），比規則強一些，但仍不是邊訓練邊對抗的自我對弈（self-play）。

## 相關頁面
[[role-assignment]] · [[hierarchical-llm-rl]] · [[cooperative-navigation]]
