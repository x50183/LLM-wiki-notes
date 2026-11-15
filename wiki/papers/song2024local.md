---
type: paper
key: song2024local
title: "A Local-and-Global Attention Reinforcement Learning Algorithm for Multiagent Cooperative Navigation"
authors: [Song, He, Dong]
year: 2024
venue: IEEE Transactions on Neural Networks and Learning Systems, vol. 35, no. 6（2022 線上發表）
url: https://doi.org/10.1109/TNNLS.2022.3220798
relevance: adjacent
llm_role: []
rl_role: low-level-control
rl_algo: [MLGA2C（基於 CTDE 的 actor-critic + 注意力）]
llm_model: []
tasks: [cooperative-navigation]
simulator: [自建 2D 多機器人環境（類 MPE，待確認）]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# MLGA2C：局部 + 全局注意力的多智能體協同導航

> ⚠️ **關聯度：adjacent**：純 MARL、沒有 LLM，對象是地面移動機器人，不是無人機。收錄原因是它是協同導航 MARL 的方法基礎，常被當作 baseline 框架。

**一句話總結**：在 CTDE 的 actor-critic 中加入兩層注意力，局部注意力找出自己觀測裡最重要的目標，全局注意力決定要關注哪些隊友；critic 的輸入因此固定長度，agent 數量增加時仍能擴展。

## 問題與動機
- 集中式方法計算量大、需要全局資訊、有單點故障；分散式方法缺乏全局視野、容易次優。
- 想要兼顧兩者：只用局部觀測、不需要完美感知，又能擴展到大量 agent。

## 方法
- **局部與全局注意力模組**：局部注意力負責 agent 內部觀測（要往哪個目標）；全局注意力用 Q/K/V 處理 agent 之間的資訊，輸出固定維度的編碼（[[attention-critic]]）。
- **新的 actor-critic**：把策略熵（類 SAC）和策略延遲更新（類 TD3）延伸到 [[ctde]] 架構，雙 Q 網路，輸出連續動作（[[entropy-exploration]]）。

## 實驗設定
- 兩個情境：靜態目標導航（N 台機器人覆蓋 N 個目標）、動態行人目標追蹤。
- N = 5, 10, 15, 20；Baseline：MADDPG、MATD3、MASAC、MAAC。
- 100 次隨機測試；指標：成功率、到達時間、碰撞數、覆蓋數、平均 reward。

## 主要結果
- 所有情境成功率最高，收斂速度幾乎不隨 N 增加而下降。
- **One-shot 推論**：在 20 台訓練，直接用在 15/25/30/35 台，仍維持高成功率；baseline 都失敗。
- **雜訊魯棒性**：加入致動器雜訊 N(0, 0.1)、觀測雜訊 N(0, 0.5)、觀測遺失，仍優於 baseline。
- 注意力視覺化顯示 agent 確實學會關注對應的目標和鄰近隊友。

## 限制與未解問題
- 論文自述：注意力模組需要較多訓練資料，前期隨機探索期很長，reward 曲線早期會驟降。
> 💭 觀察：2D 質點模型，沒有無人機動力學。但「隊伍規模改變不必重新訓練」這點，正是 [[wang2025rally]] 想用 LLM 解決的泛化問題；這篇用注意力而不是 LLM 達成類似效果，可以當作對照組。

## 與其他論文的關係
- 跟 [[lou2026llm]] 同樣用注意力 critic 處理大規模 agent。
- 跟 [[dong2026hierarchical]] 使用相同類型的 baseline（MATD3、MADDPG）。

## 相關頁面
[[cooperative-navigation]] · [[ctde]] · [[attention-critic]] · [[matd3]] · [[entropy-exploration]]
