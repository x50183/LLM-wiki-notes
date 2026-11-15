---
type: concept
aliases: [LLM 蒸餾, LoRA 微調, 機上 LLM, on-device LLM, edge LLM]
papers: [dong2026hierarchical, wang2025rally, ahn2026hallucination]
updated: 2026-11-15
---

# 把 LLM 縮小、部署到機上：蒸餾與 LoRA 微調

大模型 API（例如 GPT-4o）品質好，但延遲高、依賴網路，不適合即時集群控制。常見做法是用**模擬資料或大模型輸出**，以 LoRA 微調一個本機可執行的小模型。

## 各論文做法

| 論文 | 大模型 / 資料來源 | 部署模型 | 備註 |
|---|---|---|---|
| [[wang2025rally]] | GPT-4o 產生推理資料 | Qwen2.5 0.5B～7B（LoRA） | 1.5B 最平衡；未微調的 7B 會產生非法輸出 |
| [[dong2026hierarchical]] | 約 3000 筆模擬環境自動產生的樣本 | DeepSeek-R1 14B（LoRA，Ollama 本機） | 每 300 步才呼叫一次 |
| [[ahn2026hallucination]] | 沒有微調 | GPT-4o-mini 當 On-Device LLM | 機上算力足夠是**假設** |

> 💭 觀察：這是這批論文裡最一致的趨勢：**大模型產生資料 → 小模型上線**。但目前還沒有論文在真實無人機的機載電腦上實測 LLM 延遲。

## 相關頁面
[[llm-hallucination]] · [[qwen2-5]] · [[deepseek-r1]] · [[gpt-4o]]
