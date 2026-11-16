# ① 素材盤點

> 流程節點：① → 檢查站 C1（覆蓋檢查）
> 做法：從 `wiki/index.md` 找出需求單上每個主題對應的 wiki 頁，再把**可以直接用的事實和數字**抄出來。之後的大綱和逐頁內容只能從這張表取材。
> 標示：🟦 = 背景知識（wiki 入門頁有寫明不是論文內容）；💭 = Claude 的推論；**A** = adjacent 論文（不是無人機，或缺 LLM／RL）

## 素材表

| ID | 主題 | wiki 頁 | 可用的事實／數字 |
|---|---|---|---|
| M1 | 無人機群要做的任務 | multi-target-search、multi-uav-routing、pursuit-evasion-game、cooperative-navigation | 搜救：在災區找出多個受困者並回傳資訊；巡訪：決定每台飛去哪些點、什麼順序，還要顧電量和通訊；對抗：兩隊互追，是 LLM+RL 論文最集中的任務 |
| M2 | RL 是什麼 | 🟦 reinforcement-learning | agent 在環境中「觀察 → 動作 → 拿 reward」，靠試誤學出讓長期 reward 最大的策略，不需要標準答案 |
| M3 | 多機一起學（MARL、CTDE） | 🟦 reinforcement-learning、ctde | 訓練時 critic 看得到全局，執行時每台只靠自己的局部觀測；CTDE 的弱點是執行時沒有全局視野（💭 dong 的論點是 LLM 能補這塊） |
| M4 | RL 的弱點 | reinforcement-learning | 只看局部觀測、缺全局態勢（dong）；隊伍規模改變時泛化差（wang 對 xiang 的觀察）；沒有專家知識時收斂慢（lou、zhu） |
| M5 | LLM 是什麼 | 🟦 large-language-model | 用大量文字訓練、讀寫自然語言，能推理、規劃、寫程式；例：GPT-4o、Qwen2.5、DeepSeek-R1 |
| M6 | LLM 的弱點 | large-language-model、llm-hallucination | 慢（GPT-4o 有延遲、網路不穩，wang）；會亂講（違反電量／通訊限制的路線，ahn；非法指令 "go to target point #8, #8"，wang）；不會從互動中學（wang） |
| M7 | 分層：LLM 在上、RL 在下 | hierarchical-llm-rl | 3 篇 core 全部是這個架構；LLM 擅長全局推理但慢、會幻覺，RL 擅長即時控制但缺全局視野 |
| M8 | 四種合作方式總覽 | llm-rl-coupling-patterns | ① 條件注入（LLM→RL，執行時每 300 步）② 安全把關（RL 檢查 LLM，每次規劃）③ 先驗混合（雙向，執行時）④ 老師示範（LLM→RL，**只在訓練時**，兩篇都 **A**）；只有 ② 讓 RL 修正 LLM |
| M9 | ① 軍師＋飛行員 | dong2026hierarchical | LLM 讀全局戰況，分派追擊／區域防守／支援並選隊形；RL（MATD3）照任務行動；每 300 步呼叫一次；5v5 勝率 82% vs MATD3 69%、MADDPG 55%、MAPPO 42%；LLM 分派 vs 固定分派：Active Tracking 80.5% vs 63.2% |
| M10 | ② 規劃者＋檢查員 | ahn2026hallucination、safe-rl-cmdp | 兩層 LLM 把上千航點分區、排路線（GPT-4o 分區、GPT-4o-mini 排序）；safe-RL 檢查電量、通訊、重複造訪，違規就退回重規劃；N=2000 能耗 2.24 vs GPT-Only 3.54（×10⁷ kJ，多耗 58%）；違規率 SNR 0.3%、電量 0.3% |
| M11 | ③ 會開會的小隊 | wang2025rally、role-assignment | 每台用結構化自然語言跟隊友溝通；RL（RMIX）學習切換 Commander／Coordinator／Executor；三角色 > 雙角色 > 無角色；隊伍 8→11 台時舊方法 CI-HRL 退化，RALLY 維持；正文**沒有具體百分比** |
| M12 | ④ 家教（**A**，非無人機） | zhu2025lamarl、lou2026llm、imitation-learning | LLM 寫「先驗策略」和 reward 兩段程式；訓練時 RL 參考先驗，執行時**不用 LLM**；樣本效率平均 +185.9%（字母 R：720 vs 1360 episodes）；地面機器人實機 |
| M13 | LLM 上線的解法 | llm-hallucination、llm-distillation-lora、overview | 降低呼叫頻率（每 300 步）；safe-RL 過濾；GPT-4o 產生資料 → LoRA 微調 Qwen2.5，1.5B 最平衡；未微調的 7B 會產生非法輸出；只在訓練時用 LLM |
| M14 | 現況 | overview、paper-comparison | 收錄 13 篇（core 3、adjacent 10）；3 篇 core 全是多機、全在模擬，最多到 SITL；無人機實機只有古典方法 RACER；都是固定高度 2D |
| M15 | 研究缺口 | overview、llm-rl-coupling-patterns | 💭 無人機上還沒有「LLM 當老師、執行時不用 LLM」；💭 沒有 RL 微調 LLM 本身；💭 RL 決定何時呼叫 LLM |

## C1 覆蓋檢查（需求單的每個主題，都要有 wiki 頁支撐）

| 需求單的主題 | 對應素材 | 結果 |
|---|---|---|
| 重點 1：RL 和 LLM 互補 | M2～M7 | ✅（基本定義是 🟦 背景知識，入門頁已標明） |
| 重點 2：四種合作方式 | M8～M12 | ✅（④ 只有 adjacent 證據，簡報上要標明） |
| 重點 3：LLM 不能直接上機、還在模擬 | M13、M14 | ✅ |
| 開場用的任務情境 | M1 | ✅ |
| 收尾用的研究缺口 | M15 | ✅（全部是 💭 推論，要標示） |

**C1 結果：通過，不需要回 wiki 補頁。**
注意事項（帶到下一階段）：
- RALLY 沒有具體數字，只能用質性結論。
- RALLY 的 LLM 呼叫頻率在 wiki 上是「待確認」，不能寫。
