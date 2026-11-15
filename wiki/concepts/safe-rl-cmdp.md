---
type: concept
aliases: [Safe RL, 安全強化學習, CMDP, constrained MDP, Lagrangian actor-critic]
papers: [ahn2026hallucination]
updated: 2026-11-15
---

# Safe RL 與受限 MDP（CMDP）

在一般 MDP 上加入**成本限制**（例如能耗不得超過上限），目標是在滿足限制的前提下最大化 reward。常見解法是 **Lagrangian 方法**：把限制乘上可學習的拉格朗日乘數併入目標函數，乘數會隨違規程度自動調整。

## 在 LLM+RL+UAV 的用法
- [[ahn2026hallucination]]：safe-RL 不直接控制無人機，而是當 LLM 方案的**接受層**。限制包含能量、通訊（SNR）、重複造訪，再加上重新規劃的成本。結果：違規率約 0.3%。

## 相關頁面
[[llm-hallucination]] · [[hierarchical-llm-rl]] · [[multi-uav-routing]]
