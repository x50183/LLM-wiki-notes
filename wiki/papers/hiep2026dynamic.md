---
type: paper
key: hiep2026dynamic
title: "Dynamic Multi-Layer Aerial System for Latent Diffusion-Based Generative AI Inference at the Edge"
authors: [Hiep, Luong, Gong, Li, Nguyen, Niyato, Kim]
year: 2026
venue: IEEE Transactions on Communications, vol. 74
url: null
relevance: adjacent
llm_role: []
rl_role: resource-optimizer
rl_algo: [PPO（自適應熵）]
llm_model: []
tasks: [uav-edge-computing]
simulator: [數值模擬 + COCO-Stuff 資料集]
agents: multi
real_world: false
code: null
added: 2026-11-15
---

# MAGE：無人機中繼 + 部分卸載的擴散模型邊緣推論

> ⚠️ **關聯度：adjacent**：有 RL 和無人機，但沒有 LLM。生成式 AI（擴散模型）是被服務的**工作負載**，不是決策者。

**一句話總結**：多台無人機幫地面用戶轉送圖像生成請求到基地台，也可以在機上先跑擴散模型的編碼器、只把去噪卸載出去；用改良的 PPO 一起決定無人機位置、用戶關聯、去噪步數和卸載策略。

## 問題與動機
- 地面用戶不在固定邊緣設施的覆蓋範圍內，又想使用 LDM（Latent Diffusion Model）圖像生成服務。
- 目標：最小化所有用戶的 BRISQUE 分數（無參考圖像品質指標，越低越自然），同時滿足無人機的能耗和延遲限制。
- BRISQUE 沒有封閉形式，所以問題非凸，傳統最佳化解不了，改用 RL。

## 方法
- 系統：地面 UE → UAV（中繼，可以在機上執行圖像自編碼器和 prompt 編碼器）→ BS（執行擴散去噪）。
- 決策變數：UAV 位置、UE-UAV 關聯、BS 去噪步數、UAV 卸載策略。
- **MAGE-AE**：在 PPO 上加**自適應探索**，依近期 reward 的進步幅度調整熵獎勵的權重（[[entropy-exploration]]、[[ppo]]）。
- 對照組：MAGE-FE（標準 PPO，固定探索）、MAGE-TD（twin-delayed 策略）。

## 實驗設定
- 以 COCO-Stuff 資料集模擬圖像生成請求。
- 指標：BRISQUE、推論能耗、傳輸能耗、延遲。

## 主要結果
- 摘要宣稱：BRISQUE 降低 20～28.57%、推論能耗降低 15.98～30.17%、傳輸能耗降低 15.4～18.5%、延遲降低 33.33～43.28%（相較 baseline）。
- 策略行為：UAV 和 BS 之間頻寬增加時，UAV 傾向把整個任務卸載給 BS，以節省自身能量。
- ⚠️ **數字前後不一致**：引言說 BRISQUE 比 MAGE-FE 低「最多 20%」，結論說「最多 15%」。比 MAGE-TD 都是 30%。

## 限制與未解問題
- 論文自述：未考慮無人機的推進能耗、飛行動力學、避障；只有單一 BS。
- > 💭 觀察：「無人機位置」只是最佳化變數，沒有軌跡或飛行控制。對 LLM+RL 無人機研究來說，主要價值在**用 RL 處理無封閉形式的目標函數**，以及**自適應熵探索**這個技巧。

## 與其他論文的關係
- 自適應熵探索可以對照 [[song2024local]]，那篇也用策略熵鼓勵探索。
- 「無人機當通訊中繼」的設定和 [[yanmaz2024dynamic]] 的 relay UAV 相同。

## 相關頁面
[[uav-edge-computing]] · [[ppo]] · [[entropy-exploration]]
