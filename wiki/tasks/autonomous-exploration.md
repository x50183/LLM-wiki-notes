---
type: task
aliases: [自主探索, collaborative exploration, 協同探索, coverage]
papers: [zhou2023racer, yanmaz2024dynamic, yu2025conavgpt]
updated: 2026-11-15
---

# 多無人機自主探索與覆蓋

在未知環境中建圖或掃描，目標是盡快探索完整個區域。

## 各論文
- [[zhou2023racer]]：分散式 3D 探索的代表作，有實機。hgrid 加兩兩互動，加上 CVRP。
- [[yanmaz2024dynamic]]：2D 網格掃描，加上目標偵測和連線維持。
- [[yu2025conavgpt]]：VLM 依語意（例如「電視通常在客廳」）分配前沿給各機器人，邊探索邊找物體；地面四足機器人，無 RL。

> 💭 觀察：無人機上目前只有古典方法；LLM 的語意探索只出現在地面機器人（[[yu2025conavgpt]]），而且它的成功率只比隨機取樣多 3 個百分點。後續可以找「LLM 語意探索」或「RL 探索策略」的 UAV 論文來補。

## 相關頁面
[[multi-uav-routing]] · [[multi-target-search]] · [[cooperative-navigation]]
