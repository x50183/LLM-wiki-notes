---
type: concept
aliases: [階層式 LLM-RL, LLM 高層 + RL 低層, hierarchical LLM-MARL]
papers: [ahn2026hallucination, dong2026hierarchical, wang2025rally, xiang2025decentralized, yu2025conavgpt, zhang2026uavgent]
updated: 2026-11-15
---

# 階層式 LLM + RL 架構

把決策拆成兩層：**LLM 負責高層語意或策略決策**（分區、任務分派、目標協商），**RL 負責低層執行或把關**。這是目前 LLM+RL+UAV 論文最常見的架構，三篇 core 論文全部屬於這一類。

## 為什麼要分層
- LLM 擅長全局推理和語意理解，但推論慢、會幻覺，不適合高頻控制。
- RL 擅長即時、連續的控制，但只看局部觀測時缺乏全局視野，狀態空間太大時難以收斂。

## 各論文的分層方式

| 論文 | 上層（LLM） | 下層（RL） | 介面 | LLM 呼叫頻率 |
|---|---|---|---|---|
| [[ahn2026hallucination]] | Global-LLM 分區 + On-Device LLM 排路線 | Safe-RL 接受或重規劃 | 完整路線方案 | 每次規劃 |
| [[dong2026hierarchical]] | 全局態勢分析、任務分派 | MATD3 執行 | 任務標籤 → embedding | 每 300 timesteps |
| [[wang2025rally]] | 每台 UAV 的 LLM 語意協商 | RMIX 角色選擇 | 結構化自然語言 + 角色 | 待確認 |

## 相近但不是 LLM+RL 的分層（adjacent）
- [[xiang2025decentralized]]（CI-HRL）：高層和低層**都是 RL**，沒有 LLM。它是 RALLY 同團隊的前作，對照可以看出 RALLY 把高層換成 LLM 協商帶來的差異。
- [[yu2025conavgpt]]：上層 VLM 分配前沿，下層是古典路徑規劃（FMM），沒有 RL。
- [[zhang2026uavgent]]：上層 LLM 解析指令並定期檢查修正，下層是有理論保證的分散式控制器，沒有 RL。

> 💭 觀察：「LLM 在上」的骨架不一定要配 RL；下層換成古典控制（UAVgent）可以拿到穩定性證明，換成 RL 則換來學習能力。目前沒有論文在同一任務上比較這兩種下層。

## 爭議與矛盾
- **RL 該執行還是該把關？** SafeGPT 認為 LLM 產出的方案需要 RL 驗證；LLM-MATD3 和 RALLY 則讓 LLM 指導 RL，沒有反向的檢查機制。目前沒有論文直接比較這兩種方向。
> 💭 觀察：「LLM 在上、RL 在下」幾乎成了預設。反過來的設計，例如 RL 決定何時呼叫 LLM，或者 RL 微調 LLM 本身，在這批論文裡還沒出現。

## 相關頁面
[[llm-rl-coupling-patterns]] · [[safe-rl-cmdp]] · [[role-assignment]] · [[llm-hallucination]]
