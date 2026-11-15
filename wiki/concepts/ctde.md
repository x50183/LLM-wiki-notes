---
type: concept
aliases: [CTDE, 集中訓練分散執行, centralized training with decentralized execution]
papers: [song2024local, dong2026hierarchical, wang2025rally, lou2026llm, zhu2025lamarl, xiang2025decentralized]
updated: 2026-11-15
---

# CTDE：集中訓練、分散執行

MARL 的主流範式：**訓練時** critic 可以看到全局資訊（所有 agent 的觀測與動作），**執行時**每個 agent 只靠自己的局部觀測做決策。代表演算法有 MADDPG、MATD3、MAPPO，值分解類則有 QMIX。

## 在這批論文中
- [[song2024local]]：在 CTDE critic 加入局部與全局注意力，讓 critic 的輸入維度固定。
- [[dong2026hierarchical]]：任務增強的 [[matd3]]。
- [[wang2025rally]]：RMIX 值分解，用來選擇角色。
- [[lou2026llm]]：CTDE 加上模仿 LLM 專家策略。
- [[zhu2025lamarl]]：MADDPG，但把 critic 改成只吃個體觀測與動作 Q(o_i, a_i)，以支援大規模隊伍（嚴格說已經不是集中式 critic）。
- [[xiang2025decentralized]]：階層式 CTDE（高低層都是 MAPPO）；作者承認超大規模時集中式 critic 複雜度爆炸，是收斂困難的主因。

> 💭 觀察：CTDE 的弱點是執行時缺乏全局視野。[[dong2026hierarchical]] 的論點是：LLM 可以在執行時補上這塊全局視野。

## 相關頁面
[[matd3]] · [[attention-critic]] · [[cooperative-navigation]]
