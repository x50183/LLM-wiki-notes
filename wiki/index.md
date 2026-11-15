# Index

LLM + RL × 無人機 論文知識庫目錄。總覽見 [[overview]]，紀錄見 [[log]]。
目前收錄：13 篇論文（core 3 / adjacent 10）。

## Papers
### 2026
- [[ahn2026hallucination]] — ★core｜SafeGPT：兩層 LLM 規劃上千航點，safe-RL（CMDP）擋住幻覺路線
- [[dong2026hierarchical]] — ★core｜LLM-MATD3：LLM 分派任務，embedding 接進 MATD3，5v5 對抗勝率 82%
- [[lou2026llm]] — adjacent（非 UAV）｜LLM 專家工作流當老師，MARL 模仿，用於 P2P 電力交易
- [[hiep2026dynamic]] — adjacent（無 LLM）｜MAGE：無人機中繼 + 擴散模型部分卸載，自適應熵 PPO
- [[zhang2026uavgent]] — adjacent（無 RL）｜UAVgent：LLM 定期檢查修正 + 有理論保證的分散式隊形控制
### 2025
- [[wang2025rally]] — ★core｜RALLY：LLM 語意協商 + RMIX 角色切換的集群導航，蒸餾到 Qwen2.5
- [[zhu2025lamarl]] — adjacent（非 UAV）｜LAMARL：LLM 寫先驗策略和 reward，MADDPG 訓練，執行時不用 LLM
- [[xiang2025decentralized]] — adjacent（無 LLM）｜CI-HRL：共識推論的階層式 MARL 集群追逃，RALLY 的前作與 baseline
- [[yu2025conavgpt]] — adjacent（無 RL、非 UAV）｜Co-NavGPT：VLM 分配前沿的多機器人目標搜尋，零訓練
- [[cao2025survey]] — 綜述｜LLM 增強 RL 的四角色分類法
### 2024
- [[song2024local]] — adjacent（無 LLM、非 UAV）｜MLGA2C：注意力 critic 的協同導航 MARL
- [[yanmaz2024dynamic]] — adjacent（無 RL、無 LLM）｜搜尋型 + 中繼型無人機的多目標搜尋
### 2023
- [[zhou2023racer]] — adjacent（無 RL、無 LLM）｜RACER：分散式多無人機協同探索，有實機

## Concepts
- [[reinforcement-learning]] — 入門：RL / MARL 的基本定義，以及 RL 在本領域扮演的角色
- [[large-language-model]] — 入門：LLM 的基本定義、弱點，以及 LLM 在本領域扮演的角色
- [[hierarchical-llm-rl]] — LLM 高層 + RL 低層的階層式架構（core 論文的共同骨架）
- [[llm-hallucination]] — LLM 在規劃與控制中的幻覺及處理方式
- [[llm-distillation-lora]] — 大模型產生資料 → LoRA 小模型上線
- [[safe-rl-cmdp]] — 受限 MDP 與 Lagrangian 方法
- [[role-assignment]] — 角色與任務分派：從固定分工到動態切換
- [[imitation-learning]] — 模仿學習與 LLM 當老師
- [[llm-reward-design]] — LLM 設計 reward（Eureka 類）
- [[ctde]] — 集中訓練、分散執行
- [[matd3]] — MATD3 / MADDPG
- [[ppo]] — PPO / MAPPO
- [[attention-critic]] — 注意力 critic，用於隊伍規模擴展
- [[entropy-exploration]] — 熵正則化與自適應探索

## Tasks
- [[pursuit-evasion-game]] — 多無人機對抗與追逃（core 最集中的任務）
- [[cooperative-navigation]] — 協同導航與隊伍規模泛化
- [[multi-uav-routing]] — 多無人機路徑規劃與大規模巡訪
- [[autonomous-exploration]] — 未知環境的協同探索與覆蓋
- [[multi-target-search]] — 多目標搜尋與搜救（SAR）
- [[target-tracking]] — 目標追蹤與目標分裂時的重新分派
- [[shape-assembly]] — 形狀組裝與語言引導隊形
- [[uav-edge-computing]] — 無人機輔助邊緣運算與卸載
- [[p2p-energy-trading]] — P2P 電力交易（領域外）

## Entities
- [[gpt-4o]] — GPT-4o / 4o-mini
- [[qwen2-5]] — Qwen2.5（開源，LoRA 微調）
- [[deepseek-r1]] — DeepSeek-R1 14B
- [[claude-model]] — Claude（Claude-4-Opus）
- [[mpe]] — Multi-Agent Particle Environment
- [[gazebo-px4-sitl]] — Gazebo + ROS + PX4 軟體在環模擬

## Synthesis
- [[overview]] — 領域總覽、開放問題、建議下一批文獻
- [[llm-rl-coupling-patterns]] — LLM 與 RL 的四種耦合模式與研究缺口
- [[paper-comparison]] — 全部論文的總比較表
