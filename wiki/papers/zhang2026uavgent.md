---
type: paper
key: zhang2026uavgent
title: "UAVGENT: A Language-Guided Distributed Control Framework"
authors: [Zhang (Ziyi), Deng (Xiyu), Qu (Guannan), Nakahira (Yorie)]
year: 2026
venue: arXiv:2602.13212
url: https://arxiv.org/abs/2602.13212
relevance: adjacent
llm_role: [interface, evaluator]
rl_role: null
rl_algo: []
llm_model: [未說明（待確認）]
tasks: [target-tracking, multi-target-search]
simulator: [自建 3D 模擬]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# UAVgent：LLM 監督 + 分散式控制，有理論保證的多無人機框架

**一句話總結**：三層架構。人類用自然語言下指令；中間層的 LLM 定期檢查無人機的實際隊形是否符合人類意圖，不符合就修正參考位置；底層是只用鄰居相對位置的分散式隊形控制器。作者證明了在有界擾動、參考值會因 LLM 更新而跳動的情況下，追蹤誤差有上界。

> 為什麼是 adjacent：**沒有 RL**，底層是古典的分散式回授控制。收錄是因為它是無人機上「LLM 檢查和修正」的做法，可以和 [[ahn2026hallucination]]（用 RL 檢查 LLM）對照：一個是 LLM 檢查執行，一個是 RL 檢查 LLM。

## 問題與動機
- 多數「語言 → 機器人」流程是「編譯一次就執行到底」，環境變了不會更新。
- 多機系統中，小的指令錯誤會被放大成整體失敗。
- 讓人類一直盯著大量無人機不實際，所以加一個 LLM「助理」負責小調整，人類只在大改變時下指令。

## 方法
三層、三種時間尺度：
1. **外層（偶爾）**：使用者下自然語言指令。LLM 解析成 JSON：模式（stationary / track / search）、每個目標一組、隊形（grid、circle、square、cross…）、間距；另一個 LLM 提示產生 N 台無人機的 3D 隊形座標。
2. **中層（每隔 Δt 一次）**：LLM 拿使用者指令和目前的隊形座標比對，輸出 `{"feedback": true/false, "reason": ...}`；需要修正時重新分配無人機給目標、重新產生隊形。追蹤模式會用最新的目標位置重新定錨，搜尋模式會派新的搜尋航點。
3. **內層（連續）**：單積分器動力學 + 邊誤差回授控制，鄰居由觀測半徑決定，LLM 不碰通訊圖。

理論：在每段 LLM 更新之間，假設通訊圖固定、擾動和目標速度有界時，推導出追蹤誤差上界（Theorem 1）。

## 實驗設定
- 警察追車：3 個場景，24 台無人機追 3 台嫌疑車；車子分開後 LLM 重新分組，最後依指令排成圓、方、十字以區分嫌犯。
- 森林搜救：3 個場景，8 台無人機在區域內隨機派航點搜尋，找到人後包圍成圓或 3D 立方體。

## 主要結果
- 論文只用快照圖展示：車子分開時內層控制會讓隊形變形、各組人數不均，下一次 LLM 檢查時會重新平衡和置中。
- 論文列出要回報的指標（偵測時間、重新指派次數、隊形誤差等），但**正文沒有給出具體數字**，也**沒有和任何 baseline 比較**。

## 限制與未解問題
**論文承認的：**
- 沒有用 VLA 或多模態模型；只支援三種意圖模式。

**Claude 觀察到的：**
> 💭 觀察：沒有量化結果、沒有 baseline、沒有寫用哪個 LLM，目前只是概念驗證，不能當作效能證據。

> 💭 觀察：理論保證只涵蓋「兩次 LLM 更新之間」的控制器，LLM 本身輸出錯誤（例如隊形座標重疊）沒有被保證，只靠提示詞規則避免。這和 [[ahn2026hallucination]] 用 safe-RL 擋 LLM 錯誤的做法剛好互補。

## 與其他論文的關係
- 與 [[ahn2026hallucination]] 對照：LLM 把關執行 vs. RL 把關 LLM。
- 引用 LGPF（Liu et al., IROS 2024）、FlockGPT、LLM2Swarm、ZeroCAP 等「語言 → 集群」研究（尚未收錄）。

## 相關頁面
[[llm-hallucination]] · [[target-tracking]] · [[multi-target-search]] · [[hierarchical-llm-rl]]
