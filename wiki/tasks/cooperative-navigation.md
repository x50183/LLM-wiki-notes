---
type: task
aliases: [協同導航, cooperative navigation, 集群導航, swarm navigation]
papers: [song2024local, wang2025rally, xiang2025decentralized, yu2025conavgpt]
updated: 2026-11-15
---

# 協同導航

多個 agent 合作抵達或覆蓋多個目標，同時避免碰撞。MARL 的經典測試任務（常用 [[mpe]]）。

## 各論文
- [[song2024local]]：N 台機器人覆蓋 N 個靜態目標或追蹤行人（地面機器人，非 UAV）。用注意力 critic 擴展到 20 台以上。
- [[wang2025rally]]：UAV 集群，在規避追擊者的同時用隊形覆蓋目標。用 LLM 協商加角色分派，泛化到 8～11 台。
- [[xiang2025decentralized]]：同一個 UAV 集群任務的純 MARL 版本（CI-HRL），用策略蒸餾讓低層能隨隊伍人數換隊形，測到 15 台。
- [[yu2025conavgpt]]：多機器人視覺目標導航，VLM 分配前沿，零訓練（地面四足機器人）。

## 核心挑戰：隊伍規模泛化
兩篇都在處理「訓練時的 agent 數量 ≠ 部署時的數量」，但解法不同：注意力 critic vs LLM 語意協商（見 [[attention-critic]]）。

## 爭議與矛盾
- **CI-HRL 在更大隊伍上表現如何？** [[wang2025rally]] 說 CI-HRL 從 8 台增加到 11 台時「表現大幅下降」，落入固定分群的習慣；[[xiang2025decentralized]] 自己的測試則說到 15 台時導航和逃避 reward 大致穩定，只有隊形表現下降。兩篇的指標不同（總分 vs. 分項平均），不算直接矛盾，但引用 RALLY 的泛化優勢時要注意。

## 相關頁面
[[shape-assembly]] · [[ctde]] · [[pursuit-evasion-game]] · [[autonomous-exploration]]
