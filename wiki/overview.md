---
type: synthesis
papers: [ahn2026hallucination, dong2026hierarchical, wang2025rally, lou2026llm, hiep2026dynamic, song2024local, yanmaz2024dynamic, zhou2023racer, zhu2025lamarl, xiang2025decentralized, yu2025conavgpt, zhang2026uavgent, cao2025survey]
updated: 2026-11-15
---

# 領域總覽：LLM + RL × 無人機

> 目前收錄 13 篇：**core 3 篇**（LLM+RL+UAV 都有）、**adjacent 10 篇**（含 1 篇綜述）。以下觀點會隨著論文增加持續修訂。

## 目前的整體圖像

**1. 主流架構是「LLM 在上、RL 在下」的階層式設計。** 三篇 core 論文都是這樣：LLM 負責全局語意決策（分區、任務分派、目標協商），RL 負責即時執行或把關。見 [[hierarchical-llm-rl]]。同樣的骨架也出現在非 RL 的系統，下層改成古典規劃（[[yu2025conavgpt]]）或分散式控制（[[zhang2026uavgent]]）。

**2. 但 LLM 和 RL 的接法差很多。** 可以分成條件注入、安全把關、先驗混合、老師示範四種模式。見 [[llm-rl-coupling-patterns]]。

**3. 「LLM 不能直接上線」已經是共識。** 每篇都在處理 LLM 的延遲和幻覺：
- 降低呼叫頻率（[[dong2026hierarchical]]：每 300 步一次）
- 用 safe-RL 過濾（[[ahn2026hallucination]]）
- 從大模型蒸餾到小模型（[[wang2025rally]]：GPT-4o → Qwen2.5-1.5B）
- 只在訓練時用 LLM（adjacent：[[lou2026llm]]、[[zhu2025lamarl]]）

見 [[llm-hallucination]]、[[llm-distillation-lora]]。

**4. 「LLM 只在訓練時當老師」的證據增加，但仍不在無人機上。** [[zhu2025lamarl]] 讓 LLM 寫先驗策略和 reward，先驗策略使樣本效率平均提升 185.9%，並且有地面機器人實機驗證；[[lou2026llm]] 在電力領域得到類似結論。見 [[imitation-learning]]、[[llm-reward-design]]。

**5. 應用集中在多機協作。** 包括對抗或追逃（2 篇 core，加上純 MARL 的 [[xiang2025decentralized]]）和大規模路徑規劃（1 篇）。單機的 LLM+RL 控制還沒有收錄到。

**6. 驗證層級偏低。** core 論文全部在模擬，最多到 SITL（[[gazebo-px4-sitl]]）。無人機實機只有古典方法 [[zhou2023racer]]。

**7. 綜述也確認 LLM+MARL 是空白。** [[cao2025survey]] 的四角色分類法以單一 agent 為主，沒有涵蓋高層規劃、多機溝通、把關這幾種角色，而這正是無人機 core 論文集中的地方。本 wiki 的 `llm_role` 分類比綜述更適合這個領域，暫不更改。

## 開放問題與研究缺口
> 💭 以下是 Claude 根據目前文獻的推論，不是論文的結論。
- 無人機上還沒有人用**「LLM 當老師、執行時不用 LLM」**的模式。這個方法已經在電力（[[lou2026llm]]）和地面多機器人（[[zhu2025lamarl]]）上證明可行，是目前最清楚的缺口。
- 沒有論文用 RL **微調 LLM 本身**（RLHF / GRPO）來做無人機決策。
- LLM+RL 方法缺少跟**古典規劃 baseline** 的比較（CVRP、RACER 等）。
- **對手都不會邊訓練邊學**：規則系統（dong）或預先訓練好就固定的 PPO（[[xiang2025decentralized]]），沒有自我對弈。
- 都是固定高度的 2D 設定；3D 動力學和實機上的 LLM 延遲都還沒驗證。

## 建議下一批找的文獻
- **LGPF**（Liu et al., IROS 2024）：語言 → 隊形 → MARL，有實機。和本主題很接近，但沒有 arXiv 版，需要從 IEEE 下載。
- **FlockGPT**（Lykov et al., 2024）：LLM 引導無人機集群隊形（[[zhang2026uavgent]] 引用）。
- **LLM2Swarm**、**ZeroCAP**：語言 → 集群的其他做法。
- 單機的 LLM+RL 無人機控制，例如 LLM 設計 reward（Eureka 類）用在飛行控制。
- 空中視覺語言導航（aerial VLN）。
- RL 微調 LLM（GRPO 等）用在機器人或無人機決策的論文，確認缺口是否真的存在。

## 相關頁面
[[paper-comparison]] · [[llm-rl-coupling-patterns]] · [[index]]
