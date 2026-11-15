---
type: synthesis
papers: [ahn2026hallucination, dong2026hierarchical, wang2025rally, lou2026llm, hiep2026dynamic, song2024local, yanmaz2024dynamic, zhou2023racer, zhu2025lamarl, xiang2025decentralized, yu2025conavgpt, zhang2026uavgent, cao2025survey]
updated: 2026-11-15
---

# 論文總比較表

## Core（LLM + RL + UAV）

| 論文 | 年份 | 任務 | llm_role | rl_role | RL 演算法 | LLM | 環境 | 實機 |
|---|---|---|---|---|---|---|---|---|
| [[ahn2026hallucination]] SafeGPT | 2026 | [[multi-uav-routing]] | planner | safety-filter | Lagrangian AC | GPT-4o / 4o-mini | 自建 3D | ✗ |
| [[dong2026hierarchical]] LLM-MATD3 | 2026 | [[pursuit-evasion-game]] | planner | low-level-control | MATD3 | DeepSeek-R1 14B (LoRA) | 自建 2D | ✗ |
| [[wang2025rally]] RALLY | 2025 | [[pursuit-evasion-game]] / [[cooperative-navigation]] | communicator, planner | role-selector | RMIX | Qwen2.5 (LoRA，資料來自 GPT-4o) | MPE + SITL | ✗（SITL） |

## Adjacent（缺其中一項）

| 論文 | 年份 | 任務 | 缺什麼 | 借鏡價值 |
|---|---|---|---|---|
| [[zhu2025lamarl]] LAMARL | 2025 | [[shape-assembly]] | 無 UAV（地面機器人） | LLM 寫先驗策略 + reward，執行時不用 LLM；有實機 |
| [[xiang2025decentralized]] CI-HRL | 2025 | [[pursuit-evasion-game]] | 無 LLM | RALLY 的純 MARL 前作與 baseline；SITL |
| [[yu2025conavgpt]] Co-NavGPT | 2025 | [[autonomous-exploration]] | 無 RL、非 UAV | 純 VLM 規劃、零訓練的上限參考；有實機 |
| [[zhang2026uavgent]] UAVgent | 2026 | [[target-tracking]] / [[multi-target-search]] | 無 RL | LLM 定期檢查修正 + 有理論保證的分散式控制 |
| [[cao2025survey]] 綜述 | 2025 | — | 綜述，無 UAV | LLM 增強 RL 的四角色分類法 |
| [[lou2026llm]] | 2026 | [[p2p-energy-trading]] | 無 UAV | LLM 當老師的 MARL（[[imitation-learning]]） |
| [[hiep2026dynamic]] MAGE | 2026 | [[uav-edge-computing]] | 無 LLM | 自適應熵 PPO；處理沒有封閉形式的目標 |
| [[song2024local]] MLGA2C | 2024 | [[cooperative-navigation]] | 無 LLM、非 UAV | 注意力 critic，隊伍規模泛化 |
| [[yanmaz2024dynamic]] | 2024 | [[multi-target-search]] | 無 RL、無 LLM | SAR 問題設定，古典 baseline |
| [[zhou2023racer]] RACER | 2023 | [[autonomous-exploration]] | 無 RL、無 LLM | 實機分散式探索 baseline |

## 一眼看出的現象
- **3 篇 core 全部是多機、全部在模擬**；只有古典方法 RACER 在無人機上過實機。LAMARL、Co-NavGPT 有實機，但都是地面機器人。
- **2 篇 core 是對抗或追逃任務**，加上 CI-HRL 共 3 篇，可能反映目前這個方向的主要應用場景。浙江大學團隊（RALLY、CI-HRL）在這個任務上有連續的研究脈絡。
- **LLM 部署**：3 篇 core 裡有 2 篇用 LoRA 微調開源小模型；adjacent 的 LAMARL 和 lou 則讓 LLM 只出現在訓練階段。
- **LLM 呼叫頻率**：每 300 步（dong）、每 25 步（Co-NavGPT）、定期（UAVgent）、每次規劃（SafeGPT）、只在訓練時（LAMARL、lou）。

## 相關頁面
[[llm-rl-coupling-patterns]] · [[overview]]
