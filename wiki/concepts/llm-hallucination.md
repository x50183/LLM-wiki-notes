---
type: concept
aliases: [LLM 幻覺, hallucination, 非法輸出]
papers: [ahn2026hallucination, wang2025rally, zhu2025lamarl, zhang2026uavgent, yu2025conavgpt]
updated: 2026-11-15
---

# LLM 幻覺（在控制與規劃中的表現）

LLM 產生**看起來合理，但違反限制或格式**的輸出。在無人機場景裡，它的後果不只是答錯，而是可能造成電量耗盡、斷訊、重複飛行等實際失敗。

## 在這個領域的具體形式
- **違反物理限制的路線**：路線在文字上看起來連貫，但超出電量或通訊範圍（[[ahn2026hallucination]]）。
- **非法或格式錯誤的輸出**：例如 "go to target point #8, #8"、"region 8"，無法解析成合法動作（[[wang2025rally]]）。

## 處理方式比較

| 方法 | 論文 | 做法 |
|---|---|---|
| Safe-RL 過濾 | [[ahn2026hallucination]] | 用 CMDP 學習接受或拒絕 LLM 方案（[[safe-rl-cmdp]]） |
| 微調小模型 | [[wang2025rally]] | 用 GPT-4o 產生的資料，LoRA 微調 Qwen2.5（[[llm-distillation-lora]]） |
| 只在訓練時用 LLM | [[lou2026llm]]、[[zhu2025lamarl]]（皆非 UAV） | 執行時不呼叫 LLM，從根本避開問題；另外有程式修正或審查步驟 |
| 結構化提示 + 審查 | [[zhu2025lamarl]] | CoT + 基本 API 讓函數產生成功率從 1% 提升到 68.5%，再由 LLM 審查擋下錯誤輸出 |
| 降低呼叫頻率 | [[dong2026hierarchical]]、[[yu2025conavgpt]] | 每 300 步 / 每 25 步才呼叫一次 LLM |
| LLM 定期自我檢查 | [[zhang2026uavgent]] | LLM 比對實際隊形和使用者意圖，不符就修正（無 RL） |

## 爭議與矛盾
- **誰來檢查 LLM？** [[ahn2026hallucination]] 用 RL 檢查 LLM 的方案；[[zhang2026uavgent]] 反過來用 LLM 檢查控制器的執行結果，LLM 自己的錯誤只靠提示詞規則避免。兩種方向各自只解決一半。

## 相關頁面
[[hierarchical-llm-rl]] · [[safe-rl-cmdp]] · [[llm-distillation-lora]]
