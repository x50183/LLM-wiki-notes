# ③ 逐頁內容

> 流程節點：③ → 檢查站 C3（腳本＋Claude 核對）→ G3（使用者按章節確認）
> **這份就是簡報的最終文字**。④ 做 HTML 時只能使用這裡出現的文字（C4 會用腳本比對），要改字就先改這份。
> 每頁的格式：**版面**（給 ④ 的排版指示，不會出現在投影片上）／**文字**（投影片上的字，逐行）／**出處**（頁底 `.src`）／**講稿**（口頭補充，不上投影片）。
> 素材 ID 對應 `01-materials.md`。

---

## 序

### 第 1 頁｜封面
- 版面：沿用目前精簡過的封面（標題、副標、一隻 drone-chan、青海波）；副標下方加作者（2026-11-16 G4 使用者要求）。
- 文字：
  - 讓無人機
  - 聽得懂、學得會
  - LLM ＋ 強化學習 × 無人機 入門
  - 作者：SHIH-YU,CHENG

### 第 2 頁｜一群無人機，誰來想、誰來飛？（M1、M7）
- 版面：三張任務卡並排，下方一條結論帶；角色用 drone-chan-thinking。
- 文字：
  - 一群無人機，誰來想、誰來飛？
  - 搜救：在災區找出多個受困者，把資訊傳回地面
  - 巡訪：決定每台飛去哪些點、照什麼順序，還要顧電量和通訊
  - 對抗：兩隊無人機互相追逐、防守
  - 這些任務同時需要兩種能力：
  - 看全局：整隊怎麼分工
  - 即時反應：下一步往哪裡飛
- 出處：multi-target-search、multi-uav-routing、pursuit-evasion-game、hierarchical-llm-rl
- 講稿：今天的問題是，這兩種能力要交給誰。答案會是兩種 AI 分工合作。

---

## 壱 兩位主角

### 第 3 頁｜章節頁
- 文字：
  - 壱
  - 兩位主角
  - RL 與 LLM

### 第 4 頁｜RL：靠試誤學會反應（M2）
- 版面：左邊是循環圖（無人機 → 動作 → 環境 → 狀態與分數 → 無人機），右邊是說明卡。
- 文字：
  - RL：靠試誤學會反應
  - 強化學習（Reinforcement Learning, RL）
  - 無人機
  - 環境
  - 動作
  - 狀態＋分數（reward）
  - 不需要標準答案
  - 做對了加分、做錯了扣分，反覆嘗試
  - 學到一套「看到什麼就怎麼動」的策略（policy）
  - 就像訓練寵物：做對了給零食
- 出處：reinforcement-learning（基本定義屬背景知識）
- 講稿：reward 是人設計的分數。分數設計得不好，無人機會學出奇怪的行為。

### 第 5 頁｜很多台一起學（M3、M4）
- 版面：左右兩格對照：「訓練時」與「飛行時」。
- 文字：
  - 很多台一起學
  - 多智能體強化學習（MARL）：好幾台無人機一起學
  - 訓練時
  - 可以看到全部隊友的狀況
  - 飛行時
  - 每台只看得到自己周圍
  - 這種做法叫 CTDE（集中訓練、分散執行）
  - 弱點：飛行時缺少全局視野
  - 隊伍人數一變，學過的分工可能就不管用
- 出處：reinforcement-learning、ctde、dong2026hierarchical、wang2025rally
- 講稿：第二個弱點的例子會在「會開會的小隊」那頁出現：舊方法遇到隊伍從 8 台變 11 台就亂掉。

### 第 6 頁｜LLM：會讀會想的大腦（M5、M6）
- 版面：左邊是能力卡，右邊是弱點卡；角色用 llm-bot。
- 文字：
  - LLM：會讀會想的大腦
  - 大型語言模型（Large Language Model, LLM）
  - 讀過大量文字，看得懂、寫得出自然語言
  - 會推理、做規劃、寫程式
  - 例如 GPT-4o、Qwen2.5、DeepSeek-R1
  - 弱點
  - 慢：呼叫大模型有延遲，網路也可能不穩
  - 會講錯：說得很有把握，內容卻是錯的，這叫「幻覺」
  - 例：路線超出電量或通訊範圍
  - 例：輸出 "go to target point #8, #8" 這種無法執行的指令
- 出處：large-language-model、llm-hallucination、ahn2026hallucination、wang2025rally
- 講稿：在無人機上講錯的後果不只是答錯，而是可能沒電、斷訊。

### 第 7 頁｜剛好互補 → 分層合作（M4、M6、M7）
- 版面：上方是對照表；下方是兩層架構圖（LLM 在上、RL 在下、箭頭指向無人機）。
- 文字：
  - 剛好互補 → 分層合作
  - 擅長
  - 弱點
  - RL
  - 即時、連續的控制
  - 缺全局視野
  - LLM
  - 看懂全局、做規劃
  - 慢、會講錯
  - LLM 在上面想：看全局、分工
  - RL 在下面飛：每一步的動作
  - 收錄的 3 篇核心論文，全部是這種分層架構
- 出處：hierarchical-llm-rl、reinforcement-learning、large-language-model
- 講稿：分層讓 LLM 不必每一步都回答，它的「慢」就比較不會造成問題。

---

## 弐 四種合作方式

### 第 8 頁｜章節頁
- 文字：
  - 弐
  - 四種合作方式
  - 誰聽誰的？LLM 什麼時候上場？

### 第 9 頁｜四種方式一覽（M8）
- 版面：一張表，四列。
- 文字：
  - 四種方式一覽
  - 合作方式
  - 誰聽誰的
  - LLM 什麼時候上場
  - ① 軍師＋飛行員
  - RL 照 LLM 分派的任務飛
  - 飛行時，每 300 步一次
  - ② 規劃者＋檢查員
  - RL 檢查 LLM 排的路線
  - 飛行時，每次規劃
  - ③ 會開會的小隊
  - 雙向：LLM 商量目標，RL 決定角色
  - 飛行時
  - ④ 家教
  - RL 參考 LLM 寫的範例
  - 只在訓練時
  - 只有 ② 讓 RL 回頭檢查 LLM
- 出處：llm-rl-coupling-patterns
- 講稿：接下來四頁每種方式各講一篇代表論文。

### 第 10 頁｜① 軍師＋飛行員（M9）
- 版面：左邊流程（LLM 讀戰況 → 分派任務 → RL 執行）；右邊勝率長條圖，4 條。
- 文字：
  - ① 軍師＋飛行員
  - LLM 讀全局戰況
  - 分派任務：追擊、區域防守、支援
  - RL 照任務飛
  - 每 300 步才問一次 LLM
  - 5 對 5 空中對抗的勝率
  - LLM＋RL
  - 82%
  - MATD3
  - 69%
  - MADDPG
  - 55%
  - MAPPO
  - 42%
  - MATD3、MADDPG、MAPPO：只用 RL 的多機方法
  - 注意：對手是固定規則，不會學習
- 出處：dong2026hierarchical
- 講稿：每 300 步問一次，是為了避開 LLM 慢的問題。對手不會學，所以 82% 不代表遇到會學習的對手也能贏。

### 第 11 頁｜② 規劃者＋檢查員（M10）
- 版面：左邊流程（GPT-4o 分區 → GPT-4o-mini 排路線 → RL 檢查 → 違規就退回重排）；右邊兩張數字卡。
- 文字：
  - ② 規劃者＋檢查員
  - GPT-4o 把上千個航點分區
  - GPT-4o-mini 排出每台的路線
  - RL 檢查：電量夠嗎？通訊連得到嗎？有沒有重複飛？
  - 違規就退回重排
  - 2000 個航點時的總耗能（×10⁷ kJ）
  - 只用 LLM：3.54
  - LLM＋RL 檢查員：2.24
  - 只用 LLM、沒有檢查員時，耗能多了 58%
  - 違規率最低 0.3%
- 出處：ahn2026hallucination、safe-rl-cmdp
- 講稿：這是四種方式裡唯一由 RL 回頭檢查 LLM 的設計。58% 是整體差距，論文沒有說全部來自幻覺。

### 第 12 頁｜③ 會開會的小隊（M11）
- 版面：三個角色卡（指揮、協調、執行）；下方是隊伍變大時的對照。
- 文字：
  - ③ 會開會的小隊
  - 每台無人機都有 LLM，用自然語言跟隊友商量要去哪
  - RL 決定每台現在當什麼角色
  - Commander 指揮
  - Coordinator 協調
  - Executor 執行
  - 三種角色 ＞ 兩種角色 ＞ 不分角色
  - 隊伍從 8 台變 11 台
  - 只用 RL 的舊方法：照舊分群，新目標沒人管
  - LLM＋RL：維持表現
  - 論文以圖呈現結果，正文沒有給具體百分比
- 出處：wang2025rally、role-assignment、xiang2025decentralized
- 講稿：舊方法指同一個團隊的前作 CI-HRL。協調者的作用是化解隊友之間意見不一致。

### 第 13 頁｜④ 家教（非無人機）（M12）
- 版面：上方標示「非無人機研究」；左邊流程（LLM 寫範例與評分規則 → RL 訓練時參考 → 上場只用 RL）；右邊數字卡。
- 文字：
  - ④ 家教
  - 非無人機的研究：地面機器人排字母形狀
  - LLM 寫兩段程式：示範怎麼走的「範例策略」和「評分規則」
  - RL 訓練時參考範例
  - 上場只跑 RL，不用 LLM
  - 樣本效率（學會需要的訓練量）平均提升 185.9%
  - 字母 R：720 回合學會，沒有範例要 1360 回合
  - 有實體機器人實驗
- 出處：zhu2025lamarl、lou2026llm、imitation-learning
- 講稿：「快了 185.9%」是論文說的樣本效率提升。電力交易領域的 lou2026llm 也得到類似結論。兩篇都不是無人機，所以這頁只能說明「可能可行」。

---

## 参 走向真實世界

### 第 14 頁｜章節頁
- 文字：
  - 参
  - 走向真實世界
  - LLM 能直接上機嗎？

### 第 15 頁｜LLM 上機的兩個難題（M6、M13）
- 版面：兩欄，難題在上、解法在下；最下方一條橫跨兩欄的「第三條路」。
- 文字：
  - LLM 上機的兩個難題
  - 難題一：慢
  - 少問幾次：每 300 步才問一次
  - 換小模型：用 GPT-4o 產生資料，訓練小模型 Qwen2.5，1.5B 大小最平衡
  - 難題二：會講錯
  - 讓 RL 把關：違規路線退回重排
  - 微調過的小模型：沒微調時會輸出無法執行的指令，微調後減少，也比較快
  - 第三條路：只在訓練時用 LLM，上場就沒有這兩個問題（目前只在非無人機領域驗證）
- 出處：llm-distillation-lora、llm-hallucination、dong2026hierarchical、wang2025rally、ahn2026hallucination、zhu2025lamarl
- 講稿：沒微調的是 Qwen2.5-7B，它會輸出 "go to target point #8, #8"。論文的結論是，微調後的小模型同時改善了延遲和非法輸出。

### 第 16 頁｜現在做到哪裡、還缺什麼（M14、M15）
- 版面：左邊「現況」卡，右邊「還缺什麼」卡（標 💭）。
- 文字：
  - 現在做到哪裡、還缺什麼
  - 現況
  - 3 篇核心論文都是多台無人機，全部在模擬裡做
  - 最接近真實的是 SITL：真的飛控程式，跑在模擬世界裡
  - 收錄的論文中，真的飛上天的無人機實驗，只有不用 LLM 也不用 RL 的傳統方法
  - 對抗和集群導航兩篇，都是固定高度的平面（2D）設定
  - 還缺什麼
  - 💭 觀察（推論，非論文結論）
  - 無人機上還沒有人試「家教」模式
  - 讓 RL 學會「什麼時候該問 LLM」
- 出處：overview、paper-comparison、gazebo-px4-sitl、llm-rl-coupling-patterns
- 講稿：傳統方法指 RACER。這些缺口是根據目前收錄的 13 篇推論出來的，要找更多文獻才能確認。

---

## 結

### 第 17 頁｜小測驗
- 版面：三題，答案用 fragment，翻頁才出現。
- 文字：
  - 小測驗
  - Q1　每一步的即時控制，比較適合交給 RL 還是 LLM？
  - RL。LLM 反應慢，而且會講錯。
  - Q2　「規劃者＋檢查員」裡，誰檢查誰？
  - RL 檢查 LLM 排的路線：電量、通訊、有沒有重複飛。
  - Q3　「家教」模式為什麼不怕 LLM 慢？
  - LLM 只在訓練時上場，飛行時只跑 RL。但目前只在地面機器人上驗證。
- 出處：同第 7、11、13 頁

### 第 18 頁｜帶走三件事
- 版面：三張編號卡；角色用 drone-chan-happy。
- 文字：
  - 帶走三件事
  - RL 和 LLM 剛好互補：RL 反應快但只看眼前，LLM 看得懂全局但慢、會講錯
  - 兩者有四種合作方式：軍師＋飛行員、規劃者＋檢查員、會開會的小隊、家教
  - LLM 還不能直接上機：少問、換小模型、讓 RL 把關，或只在訓練時用；研究都還在模擬
- 出處：00-brief.md 的三個重點

### 第 19 頁｜參考文獻
- 版面：沿用 `.refs` 樣式。標題和期刊照 frontmatter **直接複製**。
- 文字：
  - 參考文獻
  - dong2026hierarchical — "Hierarchical decision-making for UAVs' game via LLM enhanced multi-agent reinforcement learning" — Aerospace Science and Technology, vol. 177, 112218
  - ahn2026hallucination — "Hallucination-Aware Hierarchical LLM for Autonomous UAV Mobility Control: A Safe Reinforcement Learning Approach" — IEEE Transactions on Networking, vol. 34
  - wang2025rally — "RALLY: Role-Adaptive LLM-Driven Yoked Navigation for Agentic UAV Swarms" — IEEE Open Journal of Vehicular Technology, vol. 6（Invited Paper）
  - zhu2025lamarl — "LAMARL: LLM-Aided Multi-Agent Reinforcement Learning for Cooperative Policy Generation" — IEEE Robotics and Automation Letters, 10(7), 2025
  - lou2026llm — "LLM-Enhanced Multi-Agent Reinforcement Learning With Expert Workflow for Real-Time P2P Energy Trading" — IEEE Transactions on Smart Grid, vol. 17, no. 5
  - xiang2025decentralized — "Decentralized Consensus Inference-based Hierarchical Reinforcement Learning for Multi-Constrained UAV Pursuit-Evasion Game" — IEEE Transactions on Neural Networks and Learning Systems（2025 early access）
  - zhou2023racer — "RACER: Rapid Collaborative Exploration With a Decentralized Multi-UAV System" — IEEE Transactions on Robotics, vol. 39, no. 3
  - 知識來源：個人 LLM Wiki（wiki/），每頁底部標註出處

---

## C3 事實核對

| 檢查項 | 做法 | 結果 |
|---|---|---|
| 出處頁存在 | 腳本：每頁「出處」列出的 wiki 頁都要存在 | ✅ 0 缺 |
| 數字 | 腳本：投影片文字裡的 23 個數字，逐一到 wiki 全文搜尋 | ✅ 0 缺 |
| 參考文獻 | 腳本：7 筆的標題和期刊要跟論文頁 frontmatter 完全一致 | ✅ 7/7 |
| 說法強度 | Claude 逐頁對照 wiki 原文，檢查有沒有說得比 wiki 更強 | ⚠️ 3 處，已修正（見下方） |
| adjacent／💭 標示 | 第 13、15、17 頁標「非無人機」；第 16 頁標 💭 | ✅ |

### 說法強度的修正
1. **第 13 頁**：「學習速度平均快了 185.9%」→「樣本效率（學會需要的訓練量）平均提升 185.9%」。wiki 寫的是**樣本效率**，不是速度。
2. **第 15 頁**：「沒訓練過的小模型反而容易講錯」→「微調過的小模型：沒微調時會輸出無法執行的指令，微調後減少，也比較快」。wiki 只說未微調的 7B 會產生非法輸出，「反而」暗示了一個 wiki 沒有的對比。
3. **第 16 頁**：「都是固定高度的平面（2D）設定」→ 只寫有證據的「對抗和集群導航兩篇」。這句在 overview 裡屬於 💭 推論段落，論文頁只有 dong 和 wang 寫明固定高度，ahn 沒有提到。同一頁的實機那句也補上「收錄的論文中」。
