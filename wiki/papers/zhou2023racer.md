---
type: paper
key: zhou2023racer
title: "RACER: Rapid Collaborative Exploration With a Decentralized Multi-UAV System"
authors: [Zhou, Xu, Shen]
year: 2023
venue: IEEE Transactions on Robotics, vol. 39, no. 3
url: null
relevance: adjacent
llm_role: []
rl_role: null
rl_algo: []
llm_model: []
tasks: [autonomous-exploration]
simulator: [模擬 + 實機]
agents: multi
real_world: true
code: "論文註腳指向 HKUST-Aerial-Robotics 的 GitHub（確切 repo 待確認）"
added: 2026-11-15
---

# RACER：分散式多無人機快速協同探索

> ⚠️ **關聯度：adjacent**：沒有 RL 也沒有 LLM，是古典規劃。收錄原因是它是多無人機協同探索的**重要實機 baseline**，作者宣稱首次在真實世界達成完全分散式的多無人機協同探索。

**一句話總結**：把未知空間切成 hgrid 格子，無人機兩兩互動，用 CVRP 平衡分配格子；每台無人機再用階層式規劃器（探索路徑 → 局部視點 → 最短時間軌跡）快速、安全地探索。

## 問題與動機
- 多無人機能大幅加速自主探索，但相關研究很少；而且真實環境裡的通訊是非同步、有限、不可靠的。

## 方法
- **hgrid 空間分解 + 兩兩互動**：線上切分未知空間，兩台無人機相遇時重新分配各自的格子，只需要非同步、有限的通訊。
- **CVRP 工作量分配**：用容量限制的車輛路徑問題，最小化覆蓋路徑總長並平衡工作量。
- **階層式探索規劃**：全局探索路徑 → 細化局部視點 → 產生最短時間軌跡。
- **實機系統**：自製四旋翼（1.32 kg），配 RealSense D435 深度相機、DJI Manifold 2G（Jetson TX2）；用 Omni-Swarm 做分散式狀態估計。

## 實驗設定
- 大量模擬加上具挑戰性的實機實驗；有消融研究，也比較了不同的協調策略（集中式和分散式）。

## 主要結果
- 探索速度明顯快於現有的集中式和分散式方法；通訊受限時表現更穩定；計算效率高、可擴展。
- 完成完全分散式的實機多無人機協同探索。

## 限制與未解問題
> 💭 觀察：這是「完全不用學習」也能在實機上做得很好的代表作。LLM 或 RL 方法如果要宣稱在多無人機探索上有優勢，應該拿 RACER 這類方法當 baseline。但這批 core 論文（[[ahn2026hallucination]]、[[dong2026hierarchical]]、[[wang2025rally]]）都沒有跟古典規劃方法比較。

## 與其他論文的關係
- 跟 [[yanmaz2024dynamic]] 同樣是多無人機在未知區域的古典方法；RACER 有實機，偏重 3D 探索。

## 相關頁面
[[autonomous-exploration]] · [[multi-uav-routing]]
