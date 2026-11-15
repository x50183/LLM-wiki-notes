---
type: task
aliases: [形狀組裝, 隊形生成, pattern formation, shape assembly, 語言引導隊形]
papers: [zhu2025lamarl, zhang2026uavgent]
updated: 2026-11-15
---

# 形狀組裝與隊形生成

讓一群機器人排出指定形狀（字母、圓、方、十字等），同時保持間距均勻、不碰撞。難點在於每台只能看到局部鄰居、機器人彼此相同（沒有預先指派位置）、卻要滿足一個全局形狀限制。

## 各論文

| 論文 | 形狀從哪來 | 怎麼排出來 | 平台 |
|---|---|---|---|
| [[zhu2025lamarl]] | 預先畫好的區域（字母） | LLM 寫先驗策略和 reward → MADDPG | 30 台模擬 + 8 台地面實機 |
| [[zhang2026uavgent]] | LLM 依自然語言產生每台的 3D 座標 | 分散式邊誤差回授控制（無 RL） | 24 台無人機模擬 |

## 相關但尚未收錄
- LGPF（Liu et al., IROS 2024）：LLM 把「圓、樹、房子」等文字轉成座標，再用 [[ctde]] MARL 排隊形，有實機轉移。被 [[dong2026hierarchical]] 和 [[zhang2026uavgent]] 引用。
- FlockGPT（無人機集群）、ZeroCAP（零樣本、無 RL）。

> 💭 觀察：「語言 → 隊形」是 LLM 在集群上很自然的切入點：LLM 負責想形狀（語意），控制器或 RL 負責排出來（物理）。目前收錄的兩篇都不是 LLM+RL+UAV 三者齊全，LGPF 若補進來，可以看看它是否用在無人機上。

## 相關頁面
[[cooperative-navigation]] · [[hierarchical-llm-rl]]
