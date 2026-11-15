---
type: concept
aliases: [大型語言模型, LLM, VLM, 視覺語言模型]
papers: [dong2026hierarchical, ahn2026hallucination, wang2025rally, zhu2025lamarl, lou2026llm, yu2025conavgpt, zhang2026uavgent, cao2025survey]
updated: 2026-11-15
---

# 大型語言模型（LLM）

> 本頁的基本定義屬於背景知識（教科書常識），不是從收錄論文整理出來的；「在本領域的用法」一節才是論文內容。

## 基本定義
- **大型語言模型（Large Language Model, LLM）**：用大量文字訓練、能讀懂並產生自然語言的神經網路，例如 [[gpt-4o]]、[[qwen2-5]]、[[deepseek-r1]]。除了聊天，也能做推理、規劃、寫程式。
- **VLM（視覺語言模型）**：同時能看圖片的 LLM，例如 [[yu2025conavgpt]] 用的 GPT-4o。
- **幻覺（hallucination）**：LLM 產生看起來合理、實際上錯誤或違反限制的輸出，見 [[llm-hallucination]]。
- **微調（fine-tuning）/ LoRA**：用少量資料調整模型，讓小模型學會特定任務，見 [[llm-distillation-lora]]。

## 在本領域的用法
LLM 在收錄論文中扮演的角色（對應 CLAUDE.md 的 `llm_role`）：

| 角色 | 意思 | 例子 |
|---|---|---|
| planner（規劃者） | 讀全局情勢，分派任務或排路線 | [[dong2026hierarchical]]、[[ahn2026hallucination]] |
| communicator（溝通者） | 多機之間用自然語言協商 | [[wang2025rally]] |
| teacher / reward-designer（老師） | 訓練時產生示範、先驗策略或 reward | [[zhu2025lamarl]]、[[lou2026llm]] |
| interface / evaluator | 把指令轉成任務、檢查執行結果 | [[zhang2026uavgent]] |

## LLM 的弱點（論文自己點出的）
- **慢**：直接呼叫 GPT-4o 有延遲和網路不穩的問題（[[wang2025rally]]）。
- **會亂講**：輸出違反電量或通訊限制的路線（[[ahn2026hallucination]]）、非法指令（[[wang2025rally]]）。
- **不會從互動中學習**：只靠靜態先驗，探索不足（[[wang2025rally]]）。

所以 LLM 很少直接控制無人機，而是和 RL 搭配，見 [[hierarchical-llm-rl]]、[[llm-rl-coupling-patterns]]。

## 相關頁面
[[reinforcement-learning]] · [[llm-hallucination]] · [[llm-distillation-lora]] · [[gpt-4o]] · [[qwen2-5]] · [[deepseek-r1]]
