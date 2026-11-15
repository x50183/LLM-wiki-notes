---
type: paper
key: ahn2026hallucination
title: "Hallucination-Aware Hierarchical LLM for Autonomous UAV Mobility Control: A Safe Reinforcement Learning Approach"
authors: [Ahn, Oh, Kim (Gyu Seon), Park, Jung, Kim (Joongheon)]
year: 2026
venue: IEEE Transactions on Networking, vol. 34
url: null
relevance: core
llm_role: [planner]
rl_role: safety-filter
rl_algo: [Lagrangian actor-critic (CMDP)]
llm_model: [GPT-4o, GPT-4o-mini]
tasks: [multi-uav-routing]
simulator: [自建 3D 模擬（10 km × 10 km × 500 m）]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# SafeGPT：用 Safe-RL 擋住 LLM 幻覺的階層式無人機路徑規劃

**一句話總結**：兩層 LLM 先把上千個航點分區並排出路線，再由一層 safe-RL 檢查每條路線是否違反能量、通訊、重複造訪等限制，違規就退回重新規劃。

## 問題與動機
- 問題：大規模隨機多點巡訪（random multi-point tour, RMPT），10 台 eVTOL 級大型旋翼無人機要走完 500～2000 個航點，應用在廣域物流和基礎設施巡檢。
- 傳統最佳化在千點規模算不動；純 RL 有維度災難；純 LLM 會**幻覺**，產出看起來合理、實際上違反物理限制的路線（[[llm-hallucination]]）。

## 方法
三層架構（[[hierarchical-llm-rl]]）：
1. **Global-LLM（GPT-4o）**：分析整個航點集合，切成平衡的扇區，每台無人機分配一區。
2. **On-Device LLM（GPT-4o-mini）**：在每台無人機上，排出區內航點的造訪順序。
3. **Safe-RL 接受層**：把限制寫成 CMDP，用 Lagrangian actor-critic 學習判斷要接受還是重新規劃 LLM 給的路線（[[safe-rl-cmdp]]）。限制包含能量、通訊品質（SNR）、重複造訪；重新規劃的成本也寫進 reward。

## 實驗設定
- 3D 區域 10 km × 10 km × 500 m，10 台無人機從中心點起飛（高度 50 m），航點均勻隨機分布，N ∈ {500, 1000, 2000}。
- Baseline：GPT-Only（沒有 safe-RL）、DQN、actor-critic。
- 指標：能耗、限制違規率、SNR、總飛行距離、完成時間。

## 主要結果
- **累積能耗**：
  - 比 GPT-Only 少 27%（N=500）、33%（N=1000）；N=2000 時 GPT-Only 多耗 58%（3.54 vs 2.24 × 10⁷ kJ）。
  - N=2000 時，DQN 和 actor-critic 分別耗 9.39 × 10⁷ 和 1.12 × 10⁸ kJ，SafeGPT 只要 2.24 × 10⁷ kJ（論文說法：比純 RL 少 75% 以上）。
- **正規化飛行距離**：比 GPT-Only 少 27%、32.8%、36.8%（依 N 遞增），差距隨規模變大。
- **違規率**：最佳權重設定下，SNR 違規 0.3%、電量違規 0.3%。

## 限制與未解問題
- 論文自述：假設無人機上有足夠算力跑 GPT-4o-mini（「on-device」是假設，不是實測）。
- 只有模擬，航點是均勻隨機分布，沒有障礙物或真實城市地圖。
> 💭 觀察：safe-RL 在這裡只做「接受或重規劃」的二元判斷，路線本身仍由 LLM 產生，所以路線品質的上限取決於 LLM。另外，「純 RL 在 N=2000 時表現很差」的比較對 RL 不太公平，因為 RL baseline 沒有用分區策略。

## 與其他論文的關係
- 跟 [[dong2026hierarchical]]、[[wang2025rally]] 一樣是「LLM 在上層、RL 在下層」，但 RL 的角色完全不同：這篇的 RL 是**安全過濾器**，另外兩篇是**執行策略**（見 [[llm-rl-coupling-patterns]]）。
- 跟 [[yanmaz2024dynamic]] 同樣處理多無人機路徑規劃，但那篇用古典演算法、規模小很多。
- 跟 [[zhang2026uavgent]] 方向相反：這篇用 RL 檢查 LLM 的方案，UAVgent 用 LLM 檢查控制器的執行結果。

## 相關頁面
[[multi-uav-routing]] · [[safe-rl-cmdp]] · [[llm-hallucination]] · [[hierarchical-llm-rl]] · [[gpt-4o]]
