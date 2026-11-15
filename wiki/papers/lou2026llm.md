---
type: paper
key: lou2026llm
title: "LLM-Enhanced Multi-Agent Reinforcement Learning With Expert Workflow for Real-Time P2P Energy Trading"
authors: [Lou, Jin, Tang, Geng, Yang, Zhang]
year: 2026
venue: IEEE Transactions on Smart Grid, vol. 17, no. 5
url: null
relevance: adjacent
llm_role: [teacher]
rl_role: low-level-control
rl_algo: [模仿式專家 MARL（Wasserstein 正則化）, 差分注意力 critic]
llm_model: [Claude-4-Opus 等多款主流 LLM]
tasks: [p2p-energy-trading]
simulator: [修改版 IEEE 141-bus 配電網]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# LLM 當專家老師的 MARL：即時 P2P 電力交易

> ⚠️ **關聯度：adjacent**：沒有無人機。收錄原因是它的 **LLM-as-teacher** 模式可以直接搬到多無人機 MARL。

**一句話總結**：每個產消者（prosumer）有一條 LLM 工作流，負責建模、找工具、寫程式、修程式，再呼叫求解器產生「專家策略」；MARL 在訓練時用 Wasserstein 距離模仿這些策略，執行時只用輕量網路。

## 問題與動機
- 即時 P2P 電力市場裡，每個產消者的需求不同，人類專家沒辦法逐一客製化指導；單一專家也處理不了異質性。
- 純 MARL 沒有專家知識，收斂慢，也可能違反配電網電壓限制。

## 方法
1. **LLM 專家工作流**（每個產消者一條）：自然語言需求 → 模型生成 → 工具檢索 → 程式生成 → 程式修正 → 求解器輸出專家策略。
2. **模仿式專家 MARL**：在 [[ctde]] 架構下，用 Wasserstein 距離衡量 agent 策略和專家策略的差異，當作模仿項（[[imitation-learning]]）。
3. **差分注意力 critic**：為了擴展到大規模 P2P 網路，用 differential attention 抽取關鍵互動特徵（[[attention-critic]]）。

## 實驗設定
- 修改版 IEEE 141-bus 配電網。
- 測試多款主流 LLM 能不能勝任專家工作流。

## 主要結果
- **LLM 能取代人類專家**：Claude-4-Opus 在專家工作流任務達到 100% 通過率、99.93% 正確率。
- 平均營運成本 4840.61 CNY，電壓違規率 1.06 × 10⁻³ p.u.，都優於 baseline。
- LLM 工作流的平均成本 < 6.27 CNY；LLM 的開銷集中在訓練階段，即時運作只用輕量網路。

## 限制與未解問題
- 論文自述：未來要擴大產消者規模、擴充外部知識庫、嘗試不同的工作流架構。
- 只有在拓樸或市場規則改變時才需要重新訓練。
> 💭 觀察：「LLM 只在訓練時用、執行時完全不用」這個設計，剛好避開了 [[wang2025rally]] 和 [[ahn2026hallucination]] 遇到的即時延遲和幻覺問題。如果搬到無人機上，LLM 可以在離線階段產生專家航線或分派方案，供 MARL 模仿。

## 與其他論文的關係
- 跟 [[song2024local]] 都把注意力機制放進 critic 處理大規模 agent。
- 跟 [[dong2026hierarchical]] 對照：那篇是 LLM 在執行時持續給指令，這篇只在訓練時當老師。
- 跟 [[zhu2025lamarl]] 同屬「LLM 只在訓練時出現」：這篇的老師是 LLM 工作流加求解器，LAMARL 的老師是 LLM 寫的先驗策略程式碼（再加上 LLM 寫的 reward）。

## 相關頁面
[[p2p-energy-trading]] · [[imitation-learning]] · [[attention-critic]] · [[ctde]] · [[claude-model]] · [[llm-rl-coupling-patterns]]
