# 教學簡報出處對照表

> 對象：`slides/llm-rl-uav-teaching.html`
> 用途：**先**列出每一頁要用的 wiki 頁面和事實，**才**開始寫簡報；寫完後再逐條核對。
> 這個步驟是在第一份簡報出錯後加的：那份簡報寫完才發現，MAPPO 那頁把 CI-HRL 的說法寫錯，參考文獻的標題也是憑印象改寫的。
> 「順序」是內容順序，不含章節頁；核對紀錄裡的「第 N 頁」指簡報實際頁碼。
> 標示說明：🟦 = 背景知識（wiki 入門頁有寫明不是論文內容）；💭 = Claude 的推論。

| 順序 | 頁面 | wiki 來源 | 要用的事實／數字 | 核對 |
|---|---|---|---|---|
| 1 | 封面 | overview | 13 篇（core 3、adjacent 10） | ✅ |
| 2 | 今天要回答的三個問題 | — | （結構頁，沒有事實） | — |
| 3 | 無人機群要做什麼 | pursuit-evasion-game、multi-uav-routing、cooperative-navigation、multi-target-search | 5v5 對抗；10 台巡訪 500～2000 個航點；躲避追擊者＋隊形覆蓋；搜救 | ✅ |
| 4 | RL 是什麼 | 🟦 reinforcement-learning | agent／環境／狀態／動作／reward／策略；靠試誤學習 | ✅ |
| 5 | 很多台一起學：MARL 與 CTDE | 🟦 reinforcement-learning、ctde | 訓練時 critic 看全局，執行時只靠自己的局部觀測 | ✅ |
| 6 | LLM 是什麼 | 🟦 large-language-model | 讀寫自然語言、推理、規劃、寫程式；GPT-4o、Qwen2.5、DeepSeek-R1 | ✅ |
| 7 | 兩者的弱點互補 | reinforcement-learning、large-language-model、hierarchical-llm-rl | RL：局部觀測、泛化差、收斂慢；LLM：慢、幻覺、不會從互動中學 | ✅ |
| 8 | 結合法①：軍師＋飛行員 | dong2026hierarchical | 每 300 步分派追擊／防守／支援；勝率 82% vs MATD3 69%、MADDPG 55%、MAPPO 42%；對手是規則系統 | ✅ |
| 9 | 結合法②：規劃者＋檢查員 | ahn2026hallucination、llm-hallucination、safe-rl-cmdp | GPT-4o 分區、GPT-4o-mini 排序；safe-RL 檢查電量／通訊／重複造訪；N=2000 能耗 2.24 vs GPT-Only 3.54（×10⁷ kJ）；違規率 0.3% | ✅ |
| 10 | 結合法③：會開會的小隊 | wang2025rally、role-assignment | 用自然語言協商；Commander／Coordinator／Executor；三角色 > 雙角色 > 無角色；8→11 台時 CI-HRL 退化；沒有具體百分比（待確認） | ✅ |
| 11 | 結合法④：家教 | zhu2025lamarl、lou2026llm、imitation-learning | LLM 寫先驗策略＋reward；樣本效率平均 +185.9%；執行時不用 LLM；**兩篇都不是無人機** | ✅ |
| 12 | 四種結合法比較 | llm-rl-coupling-patterns | 方向、LLM 何時運作 | ✅ |
| 13 | LLM 上線的三個難題 | llm-hallucination、llm-distillation-lora | 降頻（每 300 步）、RL 把關、蒸餾（GPT-4o → Qwen2.5，1.5B 最平衡）、只在訓練時用 | ✅ |
| 14 | 現在做到哪裡 | paper-comparison、overview | core 3/3 多機；core 全在模擬，最多到 SITL；無人機實機只有古典方法 RACER；固定高度 2D | ✅ |
| 15 | 還沒解決的問題 | overview、llm-rl-coupling-patterns | 💭 無人機上的「LLM 當老師」；RL 微調 LLM；RL 決定何時呼叫 LLM | ✅ |
| 16 | 小測驗 | 同第 7～11 頁 | 答案要和前面的頁面一致 | ✅ |
| 17 | 名詞小辭典 | reinforcement-learning、large-language-model、ctde、llm-hallucination、llm-distillation-lora、gazebo-px4-sitl | 定義要和 wiki 一致 | ✅ |
| 18 | 參考文獻 | 各論文頁 frontmatter 的 title／venue | **直接複製**，不要改寫 | ✅ |

## 核對紀錄
**2026-11-15 第一次執行**

1. **寫之前發現缺頁**：wiki 沒有「RL 是什麼」「LLM 是什麼」的入門頁，教學簡報卻一定要講。
   → 先在 wiki 補了 [[reinforcement-learning]]、[[large-language-model]] 兩頁（標明基本定義是背景知識），再寫簡報。wiki 從 45 頁變 47 頁。
2. **數字自動核對**：用腳本把簡報裡所有數字抓出來，逐一比對 wiki 全文。
   - 結果：28 個數字裡只有「47」不在 wiki 裡。它是 wiki 頁數，實際數過，確認正確。
   - 專有名詞（"go to target point #8, #8"、GPT-4o-mini、Qwen2.5、DeepSeek-R1、RACER、1.5B）都在 wiki 裡找得到。
3. **人工核對說法**：發現 1 處說得比 wiki 更強。
   - 第 11 頁原本寫「少了檢查員，LLM 的幻覺讓耗能多了 58%」，但 wiki 只寫 GPT-Only 多耗 58%，沒有說差距全部來自幻覺。
   - → 改成「只用 LLM、沒有檢查員時，耗能多了 58%」。
4. **參考文獻**：直接沿用第一份簡報從 frontmatter 複製的標題，沒有重寫。
5. **版面**：逐頁截圖，發現並修正 2 個問題。
   - RL 循環圖的文字壓在虛線上 → 文字改放在線上、加底色。
   - 結合法頁的流程圖擠在半欄裡 → 改成整列寬。
6. **連結檢查**：47 頁，沒有斷掉的連結，也沒有孤兒頁。

與第一份簡報比較：第一份是寫完才發現內容錯（MAPPO 說法、參考文獻標題）；這次先列對照表再寫，內容錯誤減少到 1 處，而且在發布前就抓到了。
