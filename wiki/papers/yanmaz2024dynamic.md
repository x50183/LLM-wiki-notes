---
type: paper
key: yanmaz2024dynamic
title: "Dynamic Multi-UAV Path Planning for Multi-Target Search and Connectivity"
authors: [Yanmaz, Balanji, Güven]
year: 2024
venue: IEEE Transactions on Vehicular Technology, vol. 73, no. 7
url: null
relevance: adjacent
llm_role: []
rl_role: null
rl_algo: []
llm_model: []
tasks: [multi-target-search, multi-uav-routing]
simulator: [數值模擬（400 m × 400 m 網格）]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# 搜尋型 + 中繼型無人機的多目標搜尋與連線規劃

> ⚠️ **關聯度：adjacent**：只有無人機，沒有 RL 也沒有 LLM，是古典路徑規劃。收錄原因是它提供了搜救（SAR）任務的問題設定和非學習式 baseline。

**一句話總結**：把無人機分成「搜尋」和「中繼」兩種角色，比較三種偵測到目標後的反應策略（適應性由低到高），結論是：適應性越高，連線品質越好，但找到所有目標的速度越慢。

## 問題與動機
- 搜救任務：在未知區域找出多個隨機分布的目標，把目標連回地面控制站（GCS）持續監控，同時無人機本身也要維持跟 GCS 的連線。

## 方法
- 兩種無人機：**搜尋 UAV**（有感測器）、**中繼 UAV**（只負責連線）。這是一種固定的角色分工（[[role-assignment]]）。
- 三種偵測後的反應：
  1. **DPPP**（Detection Priority Path Planning）：照預定路徑飛，有機會時才通知 GCS。
  2. **EDPPP**：照預定路徑飛，另外派新的無人機去監控目標（全名待確認）。
  3. **DAPP**（Detection Adaptive Path Planning）：指派一台搜尋 UAV 監控目標，其餘重新規劃路徑。
- 對照組：單一類型無人機的多目標最佳化規劃器（Weighted-Sum、NSGA-II），同時最佳化覆蓋時間和連線百分比。

## 實驗設定
- 區域 400 m × 400 m；搜尋 UAV 最高速 2.5 m/s，中繼 UAV 10 m/s。

## 主要結果
- DPPP 和 EDPPP 找到所有目標最快；DAPP 的目標連線率接近 100%，搜尋 UAV 平均只斷線約 5 秒（只發生在最後階段）。
- DPPP 平均斷線 25～40 秒（搜尋 UAV 少的時候），目標連線率可能低於 50%。
- WS 和 NSGA-II 加上中繼後有改善，但任務時間仍可能比作者的方法多 **40%**。

## 限制與未解問題
- 論文自述：未來要處理有時限的目標偵測和目標追蹤，並改成線上決策，用古典和深度學習方法即時做路徑決策。
> 💭 觀察：作者自己提到要往深度學習和線上決策走，這是一個很明確的 RL 切入點。「搜尋 vs 中繼」的角色分工也可以改成由 RL 或 LLM 動態分派，類似 [[wang2025rally]] 的角色切換。

## 與其他論文的關係
- 跟 [[zhou2023racer]] 同樣是多無人機在未知區域探索或搜尋的古典方法。
- 中繼 UAV 的概念也出現在 [[hiep2026dynamic]]。

## 相關頁面
[[multi-target-search]] · [[multi-uav-routing]] · [[role-assignment]] · [[autonomous-exploration]]
