---
type: concept
aliases: [LLM 設計 reward, LLM reward design, reward-designer, Eureka 類, 自動 reward 設計]
papers: [zhu2025lamarl, cao2025survey, dong2026hierarchical]
updated: 2026-11-15
---

# LLM 設計 reward

讓 LLM 依照任務描述產生 reward，取代人工反覆調整 reward 函數。對應本 wiki 的 `llm_role: reward-designer`。

## 兩種形式（依 [[cao2025survey]] 的分法）
- **隱式 reward 模型**：LLM 直接看狀態打分數，當作 reward 值。
- **顯式 reward 模型**：LLM 寫出 reward 函數的程式碼，人類可以讀、可以改。代表作有 Eureka（迭代自我反思改進 reward 程式碼）、Text2Reward。

## 在這批論文中

| 論文 | 形式 | reward 長什麼樣 | 配合什麼 | 平台 |
|---|---|---|---|---|
| [[zhu2025lamarl]] | 顯式（Python） | 稀疏：所有子目標都成立才給 1 | LLM 先驗策略 + MADDPG | 地面機器人（非 UAV） |
| [[dong2026hierarchical]] | 不是 LLM 寫的 | 依 LLM 分派的任務切換人工設計的任務專屬 reward | MATD3 | UAV |

## 爭議與矛盾
- **LLM 寫的 reward 夠不夠好？** [[zhu2025lamarl]] 的 LLM reward 只是簡單的稀疏條件，單獨使用時遇到複雜形狀會失敗，必須搭配 LLM 先驗策略才能練起來。也就是說，**reward 設計單獨使用效果有限，先驗策略才是主要貢獻**（185.9% 的樣本效率提升來自先驗策略）。
> 💭 觀察：無人機領域目前**還沒有收錄到 LLM 寫 reward 的論文**。Eureka 類方法用在單機飛行控制（例如姿態控制、穿越障礙）仍是待補的方向，見 [[overview]]。

## 相關頁面
[[imitation-learning]] · [[llm-rl-coupling-patterns]] · [[hierarchical-llm-rl]]
