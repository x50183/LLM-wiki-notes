---
type: concept
aliases: [模仿學習, imitation learning, 專家示範, LLM-as-teacher, 先驗策略]
papers: [lou2026llm, zhu2025lamarl, cao2025survey]
updated: 2026-11-15
---

# 模仿學習（LLM 當老師）

讓 RL agent 模仿專家策略，加快收斂、提高可行性。新的做法是**由 LLM 取代人類專家**來產生示範。[[cao2025survey]] 把這類歸在「決策者 → 動作引導 → 專家動作」：LLM 產生先驗策略，把 RL 策略與 LLM 老師的差距加進 loss。

## 在這批論文中

| 論文 | 老師是什麼 | 怎麼接進 RL | 執行時要 LLM 嗎 | 平台 |
|---|---|---|---|---|
| [[lou2026llm]] | LLM 工作流 + 求解器產生的專家動作 | Wasserstein 距離模仿項 | 不用 | 電力交易（非 UAV） |
| [[zhu2025lamarl]] | LLM 寫的先驗策略程式碼（人工勢場式的力） | actor 目標加 −λ(a − a_prior)² | 不用 | 地面機器人（非 UAV） |

- [[zhu2025lamarl]] 的消融顯示：先驗策略讓樣本效率平均提升 185.9%，而且沒有先驗時部分形狀根本練不起來。

> 💭 觀察：已經有兩篇（電力、地面機器人）證明這個模式可行，但**無人機 core 論文裡仍沒有人用**。無人機的機上算力有限、LLM 延遲是硬傷，正是最適合「LLM 只在訓練時出現」的場景。這是目前最清楚的研究缺口之一，見 [[overview]]。

## 相關頁面
[[llm-rl-coupling-patterns]] · [[llm-reward-design]] · [[ctde]]
