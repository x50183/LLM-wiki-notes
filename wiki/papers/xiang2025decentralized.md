---
type: paper
key: xiang2025decentralized
title: "Decentralized Consensus Inference-based Hierarchical Reinforcement Learning for Multi-Constrained UAV Pursuit-Evasion Game"
authors: [Xiang (Yuming), Li (Sizhao), Li (Rongpeng), Zhao (Zhifeng), Zhang (Honggang)]
year: 2025
venue: IEEE Transactions on Neural Networks and Learning Systems（2025 early access）
url: https://arxiv.org/abs/2506.18126
relevance: adjacent
llm_role: []
rl_role: low-level-control
rl_algo: [MAPPO, AT-M（交替訓練 MAPPO）, 策略蒸餾]
llm_model: []
tasks: [pursuit-evasion-game, cooperative-navigation]
simulator: [MPE, Gazebo-ROS-PX4 SITL]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# CI-HRL：共識推論的階層式 MARL，用於無人機集群追逃

**一句話總結**：高層 MARL 選「錨點」（要去哪個目標區），並用監督學習訓練的通訊模組 ConsMAC 從局部觀測推論全局狀態、形成共識；低層用交替訓練的 MAPPO 加策略蒸餾，負責隊形、導航和避障。沒有用 LLM。

> 為什麼是 adjacent：**沒有 LLM**。但它是 [[wang2025rally]]（RALLY）的主要 baseline，而且兩篇是同一個浙江大學團隊（Rongpeng Li、Sizhao Li、Yuming Xiang 都在兩篇作者群裡）。CI-HRL 就是「RALLY 拿掉 LLM 的版本」，對比兩篇可以看出 LLM 到底加了什麼。

## 問題與動機
- 任務 CEFC（Cooperative Evasion and Formation Coverage，協同逃避與隊形覆蓋）：一群四旋翼要以隊形覆蓋多個目標區，同時躲避追捕者和障礙物，而且通訊範圍有限。
- 屬於多限制追逃賽局（MC-PEG）。既有方法常假設追捕者走固定軌跡、全局資訊可得、只有單一隊形。
- 直接用 MAPPO 在這種多任務問題上收斂不好，所以採用階層式 RL（HRL）。

## 方法
**高層（每 10 步決策一次）**：
- 動作空間：9 個離散錨點（x、y 各取 {−8, 0, 8} m）。
- ConsMAC 通訊模組：觀測編碼器 + 距離編碼器 + 記憶模組 + 4 頭注意力，聚合鄰居訊息（64 維），再用「全局估計器」推論全局狀態。**ConsMAC 用監督學習訓練**（標籤是全局錨點輸出或全局觀測），和 RL 交替訓練。消融顯示把 RL loss 加進 ConsMAC 反而變差。

**低層**：
- AT-M：交替訓練 MAPPO，先在無障礙環境學隊形，再在密集障礙環境學避障，最後合併微調。
- 策略蒸餾：先為 3–8 台的六種隊形各訓練一個模型，再蒸餾成一個能隨隊伍人數自動換隊形的學生模型。

**對手**：用單機 PPO 訓練的追捕者，追最近、至少 3 台的群組。

## 實驗設定
- 環境：[[mpe|MPE]] + [[gazebo-px4-sitl|Gazebo-ROS-PX4 SITL]]；固定高度 2D。
- 主要設定 8 台，泛化測到 15 台。
- 通訊 baseline：TarMAC、MASIA、NVIF；無通訊：MAPPO、HASAC。低層 baseline：MADDPG、ORCA-F。

## 主要結果
- 高層總 reward R_H：CI-HRL **−281.56**，優於 MAPPO+AT-M（−397.29）、HASAC+AT-M（−381.07）、TarMAC（−432.81）、MASIA（−404.45）、NVIF（−403.79）。每回合危險次數 E 也最低（4.46）。
- 通訊量：ConsMAC 64 維，NVIF 102 維、MASIA 38 維。
- 換對手測試：追捕者改成 DDPG 或規則（追最大群、追最近）時，CI-HRL 仍可運作（任務 reward 107–188）。
- 規模泛化：8 → 15 台時低層隊形表現下降，但導航和逃避 reward 大致穩定。
- SITL：分散式非同步部署的 AT-M 達到單機模擬的 97.1%，CI-HRL 的有效隊形率達 92.7%；也測了 3–8 m/s 的風和 0.3–0.8 m 的感測誤差。

## 限制與未解問題
**論文承認的：**
- 超大規模時，CTDE 的集中式 critic 複雜度爆炸，加上隊形的拓樸限制，收斂困難。
- 只做 2D 固定高度，未來要加高度規劃。
- 對手還不夠強，未來想用對抗式 RL 讓對手自適應。

**Claude 觀察到的：**
> 💭 觀察：RALLY 論文說 CI-HRL 在 8 → 11 台時「表現大幅下降」，這篇自己則說 15 台時導航和逃避「大致穩定」，只有隊形下降。兩篇的評估指標不同（RALLY 看總分，這篇看分項 reward 的平均），不算直接矛盾，但讀 RALLY 的比較結果時要注意。見 [[cooperative-navigation]] 的爭議段落。

> 💭 觀察：這篇的對手是**訓練過的 PPO 策略**，不是純規則，比 [[dong2026hierarchical]] 的規則專家對手強一些；但訓練完就固定，仍然不是自我對弈。

## 與其他論文的關係
- 被 [[wang2025rally]] 當作主要 baseline（同團隊的前作）。
- 與 [[dong2026hierarchical]] 同屬多無人機 [[pursuit-evasion-game|對抗與追逃]]，但沒有 LLM。
- ConsMAC 的通訊設計可以和 [[song2024local]] 的注意力 critic 對照（一個在 actor 端聚合訊息、一個在 critic 端）。

## 相關頁面
[[hierarchical-llm-rl]] · [[ppo]] · [[ctde]] · [[role-assignment]] · [[pursuit-evasion-game]]
