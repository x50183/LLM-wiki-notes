---
type: paper
key: zhu2025lamarl
title: "LAMARL: LLM-Aided Multi-Agent Reinforcement Learning for Cooperative Policy Generation"
authors: [Zhu (Guobin), Zhou (Rui), Ji (Wenkang), Zhao (Shiyu)]
year: 2025
venue: IEEE Robotics and Automation Letters, 10(7), 2025
url: https://arxiv.org/abs/2506.01538
relevance: adjacent
llm_role: [reward-designer, teacher]
rl_role: low-level-control
rl_algo: [MADDPG]
llm_model: [OpenAI o1-preview]
tasks: [shape-assembly]
simulator: [自建 2D 粒子環境]
agents: multi
real_world: true
code: https://windylab.github.io/LAMARL/
added: 2026-11-15
---

# LAMARL：LLM 自動產生先驗策略和 reward 的 MARL

**一句話總結**：LLM 依照思維鏈（Chain-of-Thought，CoT）的提問和預先寫好的基本 API，自動寫出「先驗策略」和「reward 函數」兩段 Python 程式碼；MARL（MADDPG）訓練時用先驗策略當正則項，reward 放進環境。執行時只跑 RL 策略，**不需要 LLM**。

> 為什麼是 adjacent：實驗平台是地面全向輪機器人，**沒有無人機**。但它是目前 wiki 裡最完整的「LLM 只在訓練時出現」範例，對無人機很有借鏡價值。

## 問題與動機
- MARL 用在多機器人時有兩個痛點：樣本效率低、reward 要人工反覆調。
- 既有的 LLM+RL（如 Eureka、Text2Reward、RLingua）大多是單機器人、簡單任務。
- 直接把 LLM 放在機器人上做線上決策需要大量運算，而且輸出不穩定；用 LLM 寫程式碼策略（Code as Policies）則只適合簡單任務。

## 方法
兩個模組：

**(a) LLM 輔助函數產生**（四步，全部由 LLM 完成，最後一步也可以由人類做）：
1. 使用者輸入：任務描述 + 輔助提示（CoT 問題串 + 基本 API，例如 `get_neighbor_id_list`、`is_within_target_region`）。
2. 限制分析：LLM 列出要滿足的限制，分成基本限制（進入區域、避碰、與鄰居同步）和複雜限制（探索未佔據格子），再推出「基本技能」和「關鍵子目標」。
3. 函數產生：每個基本技能變成一個力（吸引力、排斥力、同步力），加總成先驗策略；每個子目標變成一個條件，全部成立才給 reward = 1（稀疏 reward）。
4. 函數審查：LLM 檢查策略有沒有實作所有技能、reward 有沒有檢查所有子目標。

**(b) MARL 模組**（以 MADDPG 為例）：
- Actor 目標從「最大化 Q」改成「最大化 Q − λ(a − a_prior)²」，讓 RL 動作向 LLM 先驗靠近。
- LLM 產生的 reward 直接放進環境，不改演算法。
- Critic 改成只吃個體的 Q(o_i, a_i)，以支援大規模隊伍。

## 實驗設定
- 任務：[[shape-assembly|形狀組裝]]，30 台機器人依序排出字母形狀，要保持均勻、不碰撞。
- Baseline：Mean-shift（Nature Communications 2023 的手工控制法，目前最佳）、MDR（人工設計 reward 的 RL）、AIRL（逆強化學習，用 1.5×10⁶ 筆 Mean-shift 專家資料）。
- 指標：覆蓋率 M1（越高越好）、均勻度 M2（Voronoi 格數的變異，越低越好）。
- LLM：OpenAI o1-preview。
- 實機：8 台全向輪機器人。

## 主要結果
- 26 個字母平均：LAMARL 的 M1 = 0.5837、M2 = 0.1189；Mean-shift 為 0.5815 / 0.1211；MDR 為 0.5634 / 0.1533；AIRL 為 0.5411 / 0.1821。**和手工最佳方法相當**，優於另外兩種 RL 方法。
- 先驗策略的消融：樣本效率平均提升 **185.9%**（例如字母 R：有先驗 720 episodes 收斂，沒有先驗要 1360）。L、T 等字母沒有先驗時，練到 4000 episodes 仍有碰撞。
- 結構化提示的消融（200 次）：完整提示的成功率 68.5%；拿掉 API 剩 2.5%；拿掉 CoT 剩 40%；兩者都拿掉剩 1%。
- 實機：LAMARL 在所有形狀都沒有碰撞、分布均勻；MDR、AIRL 在 R、T 形狀表現差。

## 限制與未解問題
**論文承認的：**
- LLM 寫的 reward 太簡單，遇到窄通道、多轉角的形狀（L、T）時比手工的 Mean-shift 差。
- 環境參數（機器人數量、感測半徑等）仍要人工設定，LLM 只負責產生兩個函數。
- 只驗證了形狀組裝一個任務；推廣到其他任務是未來工作。

**Claude 觀察到的：**
> 💭 觀察：完整提示的成功率也只有 68.5%，代表約三成的 LLM 輸出不能直接用，需要審查步驟擋下來。論文沒有說明審查失敗時怎麼處理（重新產生幾次？）。

> 💭 觀察：先驗策略本質上是「LLM 寫的人工勢場法」。這和 [[lou2026llm]] 的「LLM 工作流產生專家動作」是同一個思路，只是 LAMARL 的老師是程式碼、lou 的老師是求解器結果。兩篇都證明「LLM 只在訓練時出現」可行。

## 與其他論文的關係
- 被 [[dong2026hierarchical]] 引用為 LLM+MARL 的代表作。
- 與 [[lou2026llm]] 同屬 [[llm-rl-coupling-patterns|老師示範模式（④）]]，但多了 reward 設計。
- 對比 [[dong2026hierarchical]]、[[ahn2026hallucination]]：那兩篇執行時都要呼叫 LLM，LAMARL 完全不用。
- 與 LGPF（Liu et al., IROS 2024，尚未收錄）都在做「語言 → 隊形 → MARL」。

## 相關頁面
[[imitation-learning]] · [[llm-reward-design]] · [[shape-assembly]] · [[matd3]] · [[ctde]]
