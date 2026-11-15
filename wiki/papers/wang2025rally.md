---
type: paper
key: wang2025rally
title: "RALLY: Role-Adaptive LLM-Driven Yoked Navigation for Agentic UAV Swarms"
authors: [Wang (Ziyao), Li (Rongpeng), Li (Sizhao), Xiang, Wang (Haiping), Zhao, Zhang]
year: 2025
venue: IEEE Open Journal of Vehicular Technology, vol. 6（Invited Paper）
url: https://doi.org/10.1109/OJVT.2025.3610852
relevance: core
llm_role: [communicator, planner]
rl_role: role-selector
rl_algo: [RMIX（類 QMIX 的值分解）]
llm_model: [GPT-4o（產生資料）, Qwen2.5-7B（LoRA 微調）]
tasks: [pursuit-evasion-game, cooperative-navigation]
simulator: [MPE, Gazebo-ROS-PX4 SITL]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# RALLY：LLM 語意協商 + MARL 角色分派的無人機集群導航

**一句話總結**：每台無人機用 LLM 以結構化自然語言跟隊友溝通並推理目標；另外用一個值分解網路（RMIX），結合 LLM 的離線先驗和 MARL 的線上經驗，學習動態切換 Commander / Coordinator / Executor 角色。

## 問題與動機
- 任務 DS-CEFC（Dynamic Swarm coordination with Cooperative Evasion and Formation Coverage）：集群要躲避追擊者和障礙，同時用隊形持續覆蓋多個目標區域。
- 純 MARL 的問題：溝通是黑箱（語意落差），角色同質，泛化差。
- 純 LLM 的問題：沒有線上學習，太依賴靜態先驗，探索不足。

## 方法
- **LLMHC**（LLM-based personalized consensus generation）：每台無人機用 LLM 解讀局部觀測，以結構化自然語言跟鄰居溝通，透過協商形成共識目標（[[hierarchical-llm-rl]]）。
- **動態角色異質**：三種角色 Commander / Coordinator / Executor，可以依情勢切換（[[role-assignment]]）。
- **RLHI + RMIX**：用值分解網路做 credit 分配，學習角色選擇策略；結合 LLM 離線先驗和 MARL 線上策略。RMIX 是兩層 MLP，hidden size 16。
- **LLM 部署**：先用 GPT-4o API 收集高品質推理資料，再用 LoRA 微調 Qwen2.5 系列（0.5B～7B）。論文認為 1.5B 在效果和延遲之間最平衡（[[llm-distillation-lora]]）。

## 實驗設定
- 環境：[[mpe]]，另外在 [[gazebo-px4-sitl]] 上做 SITL 驗證（固定高度，PX4 PID 控制）。
- Baseline：CIHRL（SOTA MARL，有通訊、沒有角色）、CoNavGPT（LLM 當全局規劃器，不訓練）、DITTO（LLM 角色協作）。
- LLM 在 8 張 RTX 4090 上分散部署。

## 主要結果
- 任務覆蓋率、收斂速度、泛化都優於 baseline。論文主要以圖呈現，**沒有在正文給出具體百分比（待確認）**。
- **泛化**：集群規模 8→11 時，CIHRL 明顯退化，出現「習慣性分群」，固定組成訓練時學到的群組、無法覆蓋新增目標；RALLY 維持表現。
- **角色消融**：三角色 > 雙角色（Commander-Executor，平均略升但變異大）> 無角色。Coordinator 的角色在調和語意衝突。
- **LLM 消融**：未微調的 Qwen2.5-7B 會產生非法輸出，例如 "go to target point #8, #8"；直接呼叫 GPT-4o 有延遲和網路不穩定的問題；微調後的小模型兩者兼顧。

## 限制與未解問題
- 固定高度；SITL 是軟體模擬，不是實機。
- 用來擴增少樣本語料的 50 筆範例是人工標註的。
> 💭 觀察：這篇明確點出「直接打 API 的 LLM 不適合即時集群控制」，給出的解法是蒸餾到小模型。這跟 [[dong2026hierarchical]] 用 DeepSeek-R1 14B + LoRA 的思路一致，可能是這個領域正在成形的共識。

## 與其他論文的關係
- 跟 [[dong2026hierarchical]] 是最接近的對照組（LLM + MARL，對抗或規避情境）。
- 協同導航的 MARL 基礎可以對照 [[song2024local]]。
- 非法輸出問題對應 [[ahn2026hallucination]] 處理的幻覺問題，但兩篇的解法不同：微調 vs safe-RL 過濾。
- baseline [[xiang2025decentralized]]（CIHRL）是同團隊的純 MARL 前作，任務相同（CEFC），可以看出加入 LLM 的差異。
- baseline [[yu2025conavgpt]]（Co-NavGPT）是純 VLM 規劃、零訓練的代表。
- 另一個 baseline DITTO（ACL 2024）其實是 LLM 角色扮演的自我對齊方法，和無人機無關，未收錄。

## 相關頁面
[[pursuit-evasion-game]] · [[cooperative-navigation]] · [[role-assignment]] · [[llm-distillation-lora]] · [[llm-hallucination]] · [[qwen2-5]] · [[gpt-4o]] · [[mpe]] · [[gazebo-px4-sitl]]
