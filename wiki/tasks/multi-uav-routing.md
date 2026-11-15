---
type: task
aliases: [多無人機路徑規劃, multi-UAV path planning, RMPT, 多點巡訪, VRP]
papers: [ahn2026hallucination, yanmaz2024dynamic, zhou2023racer]
updated: 2026-11-15
---

# 多無人機路徑規劃與巡訪

決定多台無人機各自要去哪些點、以什麼順序飛。本質上是 TSP / VRP 的多機版本，通常還要加上能量、通訊等限制。

## 各論文

| 論文 | 規模 | 方法 | 限制條件 |
|---|---|---|---|
| [[ahn2026hallucination]] | 10 台、500～2000 航點 | LLM 分區排序 + safe-RL 把關 | 能量、SNR、重複造訪 |
| [[yanmaz2024dynamic]] | 400 m 見方區域 | 古典規劃（DPPP / EDPPP / DAPP）vs NSGA-II | 連線到 GCS |
| [[zhou2023racer]] | 未知 3D 空間 | CVRP 工作量分配 + 階層式規劃 | 非同步通訊 |

> 💭 觀察：LLM 方法（SafeGPT）只跟 GPT-Only 和純 RL 比，沒有跟 CVRP 求解器或 RACER 這類古典規劃比。這是評估上的缺口。

## 相關頁面
[[safe-rl-cmdp]] · [[autonomous-exploration]] · [[multi-target-search]]
