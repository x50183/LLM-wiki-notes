---
type: concept
aliases: [MATD3, MADDPG, Multi-Agent TD3]
papers: [dong2026hierarchical, song2024local, zhu2025lamarl, xiang2025decentralized]
updated: 2026-11-15
---

# MATD3 / MADDPG

把 DDPG（MADDPG）和 TD3（MATD3）延伸到多智能體的 [[ctde]] 演算法，適合**連續動作**。MATD3 繼承 TD3 的雙 Q 網路和延遲策略更新，比 MADDPG 穩定。

## 在這批論文中
- [[dong2026hierarchical]]：以 MATD3 為底，加入任務 embedding；5v5 對抗勝率 MATD3 69%、MADDPG 55%，LLM-MATD3 82%。
- [[song2024local]]：MATD3、MADDPG 都是 baseline；作者的 MLGA2C 也沿用了 TD3 的策略延遲更新。
- [[zhu2025lamarl]]：以 MADDPG 為底，actor 目標加上「模仿 LLM 先驗策略」的正則項。
- [[xiang2025decentralized]]：MADDPG 是低層 baseline，隊形人數超過 6 台就學不到有效策略，訓練成本也很高。

## 相關頁面
[[ctde]] · [[ppo]]
