---
type: paper
key: yu2025conavgpt
title: "Co-NavGPT: Multi-Robot Cooperative Visual Semantic Navigation Using Vision Language Models"
authors: [Yu (Bangguo), Yuan (Qihao), Li (Kailai), Kasaei (Hamidreza), Cao (Ming)]
year: 2025
venue: arXiv:2310.07937（v3，2025）
url: https://arxiv.org/abs/2310.07937
relevance: adjacent
llm_role: [planner]
rl_role: null
rl_algo: []
llm_model: [GPT-4o, GPT-4o-mini]
tasks: [autonomous-exploration, cooperative-navigation]
simulator: [Habitat, HM3D]
agents: multi
real_world: true
code: https://sites.google.com/view/co-navgpt2
added: 2026-11-15
---

# Co-NavGPT：VLM 當全局規劃器的多機器人目標搜尋

**一句話總結**：多台機器人把各自的點雲地圖合併，畫成帶有前沿（frontier）標記的俯視圖，交給 VLM（GPT-4o）決定每台機器人要去哪個前沿；底層用快速行進法（FMM）規劃路徑。**完全不需要訓練**，也沒有 RL。

> 為什麼是 adjacent：**沒有 RL、也不是無人機**（地面四足機器人）。收錄是因為 [[wang2025rally]] 拿它當「純 LLM 規劃、不訓練」的 baseline，可以拿來看 LLM 單獨做規劃的上限。
> 版本注意：2023 年的 v1 標題寫 "Large Language Models"，本頁讀的是 2025 年 v3，標題改成 "Vision Language Models"，作者也多了兩位。

## 問題與動機
- 多機器人視覺目標導航：幾台機器人一起在未知環境裡找某個物體（例如「找電視」）。
- 單機器人方法效率低、容錯差；學習式方法需要大量資料，多機器人時更嚴重。
- VLM 有常識（例如電視通常在客廳），可以零樣本做高層規劃。

## 方法
1. 每台機器人用 RGB-D、YOLOv8（開放詞彙偵測）、Mobile-SAM（分割）建立局部點雲地圖，再依位姿合併成全局地圖。
2. 投影成 2D 探索地圖，萃取前沿區塊。
3. **視覺提示**：每個候選前沿畫一張俯視圖並標上編號、機器人位置。**文字提示**：任務、情境、推理要求（理解 → 分析 → 決策 → 反思）、JSON 輸出格式。
4. VLM 輸出每台機器人分到的前沿，**每 25 步更新一次**。
5. 底層用 FMM 規劃路徑，不用 VLM 做細部控制。

## 實驗設定
- Habitat 模擬器、HM3D v0.2，36 個驗證場景、1000 個 episode，6 類目標，2 台機器人。
- Baseline：Greedy（選最近前沿）、Cost-Utility、隨機取樣、Multi-SemExp（學習式）。
- 指標：成功率 SR、路徑長度加權成功率 SPL、結束時離目標距離 DTG。

## 主要結果
- Co-NavGPT：SR **0.666**、SPL 0.368、DTG 1.684；最好的 baseline（隨機取樣）為 0.636 / 0.336 / 2.048。
- 消融：單機器人 SR 0.579；換成 GPT-4o-mini 0.641；只給障礙物地圖（沒有語意）0.645。
- 失敗原因：約 14% 來自探索問題（困在重建不好的區域、目標在別的樓層），約 20% 來自物體偵測錯誤。
- 實機：2 台 Unitree Go2 四足機器人，約 5 FPS 即時運作；所有感知和 VLM 規劃都跑在一台 RTX 4090 工作站上。

## 限制與未解問題
**論文承認的：**
- 多樓層導航仍是難題；偵測錯誤會讓機器人提早停下。

**Claude 觀察到的：**
> 💭 觀察：比最好的 baseline 只多 3 個百分點的成功率，而且「隨機取樣」竟然贏過 Cost-Utility 和學習式的 Multi-SemExp。這表示在這個任務上，前沿分配策略本身的影響可能沒有想像中大。

> 💭 觀察：VLM 跑在工作站、不在機器人上，而且每 25 步才呼叫一次。這和 [[dong2026hierarchical]]（每 300 步）一樣，都是用「降低呼叫頻率」處理延遲，見 [[llm-hallucination]]。

## 與其他論文的關係
- 被 [[wang2025rally]] 當作 baseline。RALLY 說 Co-NavGPT 的平均 reward 高於 CIHRL（[[xiang2025decentralized]]），但沒有探索、容易卡在局部最佳。
- 和 [[zhou2023racer]] 都是多機協同探索，一個用 VLM、一個用古典規劃。

## 相關頁面
[[autonomous-exploration]] · [[cooperative-navigation]] · [[gpt-4o]] · [[hierarchical-llm-rl]]
