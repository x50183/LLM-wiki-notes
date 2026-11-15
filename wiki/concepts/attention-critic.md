---
type: concept
aliases: [注意力 critic, attention-based critic, differential attention]
papers: [song2024local, lou2026llm]
updated: 2026-11-15
---

# 注意力 critic

在 MARL 的 critic 中用注意力機制，從大量 agent 的資訊裡挑出重要的部分，把可變數量的輸入壓成**固定維度**。這樣 agent 數量增加時不必改網路，也能減少冗餘資訊。

## 在這批論文中
- [[song2024local]]：局部注意力 + 全局注意力（Q/K/V）。在 20 台訓練，可以直接推論到 35 台。
- [[lou2026llm]]：差分注意力（differential attention）critic，用於大規模 P2P 網路。

> 💭 觀察：要擴展隊伍規模，「注意力 critic」和「LLM 語意協商」（[[wang2025rally]]）是兩條不同的路線，目前沒有論文直接比較。

## 相關頁面
[[ctde]] · [[cooperative-navigation]]
