---
type: entity
aliases: [GPT-4o, GPT-4o-mini]
papers: [ahn2026hallucination, wang2025rally, yu2025conavgpt]
updated: 2026-11-15
---

# GPT-4o / GPT-4o-mini

OpenAI 的閉源 LLM，只能透過 API 使用。

## 在這批論文中
- [[ahn2026hallucination]]：GPT-4o 當 Global-LLM 負責分區；GPT-4o-mini 當 On-Device LLM，**假設**可以在機上執行。
- [[wang2025rally]]：GPT-4o 只用來產生訓練資料；直接線上呼叫有延遲和網路不穩定的問題，所以最後部署的是微調過的 Qwen2.5。
- [[yu2025conavgpt]]：GPT-4o 當 VLM 全局規劃器（看俯視圖分配前沿）；換成 GPT-4o-mini 時成功率從 0.666 降到 0.641。

## 其他 OpenAI 模型
- [[zhu2025lamarl]]：用 o1-preview 產生先驗策略和 reward 程式碼。

## 相關頁面
[[llm-distillation-lora]] · [[qwen2-5]]
