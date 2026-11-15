---
type: paper
key: dong2026hierarchical
title: "Hierarchical decision-making for UAVs' game via LLM enhanced multi-agent reinforcement learning"
authors: [Dong, Li, Zhang, Xiao, Wang]
year: 2026
venue: Aerospace Science and Technology, vol. 177, 112218
url: https://doi.org/10.1016/j.ast.2026.112218
relevance: core
llm_role: [planner]
rl_role: low-level-control
rl_algo: [MATD3]
llm_model: [DeepSeek-R1 14B（LoRA 微調）]
tasks: [pursuit-evasion-game]
simulator: [自建 2D 對抗環境（1600 m × 1600 m）]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# LLM-MATD3：LLM 分派任務、MATD3 執行的多無人機對抗

**一句話總結**：LLM 讀全局戰況，幫每台無人機分派任務標籤（追擊、區域防守、支援）並選擇隊形；任務標籤轉成 embedding，餵進 MATD3 的 actor 和 critic，讓 RL 策略「照任務行動」。

## 問題與動機
- 多無人機對抗遊戲（5 vs 5，接近近距離空戰的設定）。
- 作者指出三個缺口：
  1. MATD3 這類方法只看局部觀測，缺乏全局態勢感知。
  2. LLM 的高層指令和 RL 的連續策略之間有**語意落差**。
  3. 缺少兩者「持續」整合的機制：過去多半只在冷啟動或預訓練時給一次指導。

## 方法
三層架構（[[hierarchical-llm-rl]]）：環境建模層 → LLM 任務規劃器 → 任務增強的 MATD3。
- **LLM 任務規劃**：分析全局態勢，分派三種任務（Active Tracking / Area Defense / Cooperative Support），並依敵我數量比例選隊形（例如 Scattered、Surrounding）。每 300 個 timestep 更新一次建議。
- **階層式任務分解**：為每種任務設計專屬 reward，把離散的任務標籤轉成依狀態變化的連續子目標分數。
- **任務感知 actor-critic**：任務 embedding 同時接進 policy 和 value 網路（[[matd3]]、[[ctde]]）。
- **LLM 部署**：DeepSeek-R1 14B，用 Ollama 在本機執行，以約 3000 筆從模擬環境自動產生的樣本做 LoRA 微調（[[llm-distillation-lora]]）。

## 實驗設定
- 1600 m × 1600 m 平面，隨機靜態障礙，雙方各 5 台；固定高度的 2D 運動學模型。
- 對手（B 隊）是專家規則系統。
- Baseline：MATD3、MADDPG、MAPPO。訓練 3500 episodes（圖上以 ×10 標示，實際總數待確認）。
- 指標：勝率、交換比（擊落敵機數 / 我方損失數）、累積 reward。

## 主要結果
- **勝率**：LLM-MATD3 82%，MATD3 69%、MADDPG 55%、MAPPO 42%。
- **LLM 分派 vs 固定分派**的任務成功率：Active Tracking 80.5% vs 63.2%；Cooperative Support 46.4% vs 31.6%。
- **任務比例**：最佳的追擊 : 防守 : 支援 = 55:35:10，勝率 82.0%、交換比 2.59，變異也最小；比例偏極端時表現較差。

## 限制與未解問題
- 論文自述的未來方向：更深的 LLM-RL 整合、動靜混合任務分配、多模態態勢感知、輕量化部署。
- 只有 2D、固定高度的模擬；對手是固定規則，不是會學習的對手。
> 💭 觀察：隊形選擇是用敵我數量比例的門檻規則觸發（例如 num > 1.3），這部分可能其實不需要 LLM。值得追問的是：如果把 LLM 換成規則式的任務分派器，82% 的勝率還剩多少？論文沒有做這個消融。

## 與其他論文的關係
- 跟 [[wang2025rally]] 很像（LLM 做高層語意決策 + MARL），但 RALLY 是每台無人機各自用 LLM 協商、再用 RL 選角色；這篇是中央 LLM 分派、RL 執行。
- 跟 [[ahn2026hallucination]] 相反：這篇是 LLM 指導 RL，SafeGPT 是 RL 把關 LLM。
- MATD3 的同一組 baseline 也出現在 [[song2024local]]。
- 相關研究引用了 [[zhu2025lamarl]]（LAMARL，LLM 產生先驗策略和 reward）和綜述 [[cao2025survey]]。

## 相關頁面
[[pursuit-evasion-game]] · [[matd3]] · [[ctde]] · [[role-assignment]] · [[deepseek-r1]] · [[llm-rl-coupling-patterns]]
