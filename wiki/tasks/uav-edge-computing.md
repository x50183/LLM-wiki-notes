---
type: task
aliases: [無人機邊緣運算, UAV-assisted MEC, 空中中繼, offloading]
papers: [hiep2026dynamic]
updated: 2026-11-15
---

# 無人機輔助邊緣運算

無人機當作空中中繼或行動邊緣伺服器，替地面用戶轉送或分擔運算任務。RL 通常用來做資源最佳化，包括位置、關聯、卸載、頻寬。

## 各論文
- [[hiep2026dynamic]]：服務的工作負載是擴散模型的圖像生成；用自適應熵的 PPO 一起最佳化位置、關聯、去噪步數和卸載策略。

> 💭 觀察：反過來想，**LLM 推論本身**也可以是無人機要卸載的工作負載，這跟 [[llm-distillation-lora]] 的機上部署問題剛好互補。

## 相關頁面
[[ppo]] · [[entropy-exploration]]
