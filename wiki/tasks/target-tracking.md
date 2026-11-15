---
type: task
aliases: [目標追蹤, target tracking, 主動追蹤, active tracking]
papers: [zhang2026uavgent, dong2026hierarchical]
updated: 2026-11-15
---

# 目標追蹤

無人機持續跟住一個或多個移動目標（車輛、人、敵機），通常還要維持隊形或包圍。

## 各論文
- [[zhang2026uavgent]]：24 台無人機追 3 台嫌疑車。車子分開後，底層控制先粗略分組，LLM 定期檢查並重新平衡各組人數、重排隊形（無 RL）。
- [[dong2026hierarchical]]：「Active Tracking」是 LLM 分派的三種任務之一，在對抗情境中追擊敵機。

> 💭 觀察：目標分裂時「誰追誰」的重新分派，正是 [[role-assignment]] 的問題。UAVgent 交給 LLM 定期修正，RALLY（[[wang2025rally]]）交給 MARL 學角色切換，兩種做法還沒有在同一個任務上比較過。

## 相關頁面
[[pursuit-evasion-game]] · [[multi-target-search]] · [[role-assignment]]
