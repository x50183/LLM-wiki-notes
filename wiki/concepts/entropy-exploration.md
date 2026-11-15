---
type: concept
aliases: [熵正則化, entropy bonus, 自適應探索, policy entropy]
papers: [hiep2026dynamic, song2024local]
updated: 2026-11-15
---

# 熵與探索

在 RL 目標中加入**策略熵**，鼓勵策略保持隨機性、持續探索，避免太早收斂到次優解。

## 做法比較
- [[hiep2026dynamic]]：**自適應**。近期 reward 有進步就減少探索，停滯就加強探索，靠動態調整熵獎勵的權重達成。
- [[song2024local]]：類 SAC 的最大熵目標，作者認為這讓結果的變異更小、更魯棒。

## 相關頁面
[[ppo]] · [[ctde]]
