---
type: concept
aliases: [強化學習, RL, 多智能體強化學習, MARL]
papers: [dong2026hierarchical, ahn2026hallucination, wang2025rally, xiang2025decentralized, zhu2025lamarl, lou2026llm, hiep2026dynamic, song2024local]
updated: 2026-11-15
---

# 強化學習（RL）與多智能體強化學習（MARL）

> 本頁的基本定義屬於背景知識（教科書常識），不是從收錄論文整理出來的；「在本領域的用法」一節才是論文內容。

## 基本定義
- **強化學習（Reinforcement Learning, RL）**：一個 **agent（智能體）** 在 **環境** 中反覆「觀察狀態 → 做出動作 → 得到 reward（獎勵）」，目標是學到一個 **策略（policy）**，讓長期累積的 reward 最大。不需要標準答案，靠試誤學習。
- **reward（獎勵）**：環境給的分數，定義「什麼是好行為」。reward 設計得不好，agent 會學到奇怪的行為，所以有 [[llm-reward-design|讓 LLM 幫忙設計 reward]] 的研究。
- **多智能體強化學習（MARL）**：多個 agent 同時學習、互相影響。多無人機系統就是典型的 MARL 問題。最常見的訓練方式是 [[ctde]]（集中訓練、分散執行）。
- 常見演算法：[[ppo]]（及多機版 MAPPO）、[[matd3]]、MADDPG、QMIX 類值分解。

## 在本領域的用法
RL 在收錄論文中扮演的角色（對應 CLAUDE.md 的 `rl_role`）：

| 角色 | 意思 | 例子 |
|---|---|---|
| 底層控制 | 輸出每一步的移動指令 | [[dong2026hierarchical]]（MATD3）、[[zhu2025lamarl]]（MADDPG） |
| 安全把關 | 判斷 LLM 的方案能不能接受 | [[ahn2026hallucination]]（[[safe-rl-cmdp]]） |
| 角色分派 | 學習誰當指揮、誰當執行者 | [[wang2025rally]]（RMIX，見 [[role-assignment]]） |
| 資源最佳化 | 決定位置、頻寬等系統配置 | [[hiep2026dynamic]] |

## RL 的弱點（論文自己點出的）
- 只看局部觀測，缺乏全局態勢感知（[[dong2026hierarchical]]）。
- 隊伍規模改變時泛化差（[[wang2025rally]] 對 [[xiang2025decentralized]] 的觀察）。
- 沒有專家知識時收斂慢（[[lou2026llm]]、[[zhu2025lamarl]]）。

這些弱點正是 LLM 被引進來的理由，見 [[hierarchical-llm-rl]]、[[large-language-model]]。

## 相關頁面
[[ctde]] · [[ppo]] · [[matd3]] · [[large-language-model]] · [[llm-rl-coupling-patterns]]
