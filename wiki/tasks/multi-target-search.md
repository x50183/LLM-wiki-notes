---
type: task
aliases: [多目標搜尋, 搜救, SAR, search and rescue]
papers: [yanmaz2024dynamic, zhang2026uavgent]
updated: 2026-11-15
---

# 多目標搜尋與搜救（SAR）

在災區等未知區域找出多個目標（例如受困者），並持續把目標資訊傳回地面控制站。

## 各論文
- [[yanmaz2024dynamic]]：搜尋 UAV + 中繼 UAV；適應性越高，連線越好，但找齊目標越慢。作者提到未來要改用深度學習做線上決策。
- [[zhang2026uavgent]]：森林搜救，LLM 在指定區域內派搜尋航點，沒找到就重派，找到後全體包圍目標（8 台，無 RL，無量化結果）。

## 相關頁面
[[autonomous-exploration]] · [[multi-uav-routing]] · [[role-assignment]] · [[target-tracking]]
