---
type: paper
key: cao2025survey
title: "Survey on Large Language Model-Enhanced Reinforcement Learning: Concept, Taxonomy, and Methods"
authors: [Cao (Yuji), Zhao (Huan), Cheng (Yuheng), Shu, Chen (Yue), Liu (Guolong), Liang (Gaoqi), Zhao (Junhua), Yan (Jinyue), Li (Yun)]
year: 2025
venue: IEEE Transactions on Neural Networks and Learning Systems, 36(6), 2025（本頁讀 arXiv v3，2024-10）
url: https://arxiv.org/abs/2404.00282
relevance: adjacent
llm_role: [reward-designer, policy, teacher, interface, env-generator]
rl_role: null
rl_algo: []
llm_model: []
tasks: []
simulator: []
agents: single
real_world: false
code: null
added: 2026-11-15
---

# 綜述：LLM 增強的強化學習（LLM-enhanced RL）

**一句話總結**：把「LLM 怎麼幫 RL」依照 agent–環境互動迴圈分成四種角色：資訊處理者、reward 設計者、決策者、產生器，並整理各自的方法、解決的 RL 問題和未來方向。

> 為什麼是 adjacent：這是**綜述**，沒有無人機內容，也沒有實驗。收錄目的是拿它的分類法來檢查本 wiki 的 `llm_role`。
> `[taxonomy?]`：綜述不適合 core / adjacent 二分，暫時標 adjacent。frontmatter 的 `llm_role` 列的是它涵蓋的角色，不是它本身的方法。

## 核心定義
LLM-enhanced RL：利用預訓練 LLM 的多模態資訊處理、生成、推理等高階能力來**輔助** RL 的方法。LLM 要解決 RL 的四個老問題：樣本效率低、reward 難設計、泛化差、自然語言指令難理解。

## 四種角色

| 角色 | 子類 | 解決什麼 | 代表方法（綜述內舉例） |
|---|---|---|---|
| 資訊處理者 | 特徵擷取、語言翻譯（自然語言 → 形式化任務語言） | 多模態觀測難學 | HELM、RLang |
| reward 設計者 | 隱式 reward 模型（直接打分）、顯式 reward 模型（寫 reward 程式碼） | 稀疏或難定義的 reward | Eureka、Text2Reward |
| 決策者 | 動作產生（LLM 直接當策略，類 Decision Transformer）、動作引導（給候選動作或專家動作） | 樣本效率、探索效率 | SayCan、instructRL |
| 產生器 | 世界模型模擬器、策略解釋器 | model-based RL、可解釋性 | — |

「動作引導 → 專家動作」這一類，綜述的描述是：LLM 產生先驗策略，再把「RL 策略和 LLM 老師的差距」加進 RL 的 loss（例如 instructRL）。

## 綜述指出的機會與挑戰
- **多智能體 RL 是明確的空白**：相較於大量的多 LLM agent 協作研究，「LLM 增強的 MARL」仍很少。
- 安全 RL：LLM 可以幫忙設計成本函數。
- 挑戰：幻覺與偏誤、對新環境的適應、運算延遲（建議提示壓縮、MoE、快取、非同步）、倫理與安全。
- 應用舉例：機器人、自駕車、能源管理、醫療推薦，**沒有提到無人機**。

## 對本 wiki 分類法的啟示
> 💭 觀察：綜述的四種角色和本 wiki 的 `llm_role` 大致可以對應，但切法不同：

| 綜述角色 | 本 wiki 的 `llm_role` | 備註 |
|---|---|---|
| 資訊處理者（語言翻譯） | `interface` | 對應良好 |
| reward 設計者 | `reward-designer` | 對應良好 |
| 決策者（動作產生） | `policy` | 對應良好 |
| 決策者（專家動作） | `teacher` | 本 wiki 的 `teacher` 比較細 |
| 產生器（世界模型） | `env-generator` | 部分對應 |
| —（綜述沒有） | `planner`、`communicator`、`evaluator` | 這三個都是**多智能體或階層式**才會出現的角色 |

> 💭 觀察：綜述以單一 agent 為主，所以沒有「高層規劃」「多機溝通」「把關」這幾類。而本 wiki 的 core 論文幾乎都落在這些類別，正好呼應綜述說的「LLM+MARL 是空白」。保留本 wiki 的分類法，不需要改成綜述的四分法。

## 與其他論文的關係
- 被 [[dong2026hierarchical]] 引用為 LLM+RL 的總覽。
- [[zhu2025lamarl]]、[[lou2026llm]] 屬於綜述的「reward 設計者」和「決策者 → 專家動作」。

## 相關頁面
[[llm-rl-coupling-patterns]] · [[llm-reward-design]] · [[imitation-learning]] · [[hierarchical-llm-rl]]
