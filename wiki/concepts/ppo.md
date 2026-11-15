---
type: concept
aliases: [PPO, MAPPO, Proximal Policy Optimization]
papers: [hiep2026dynamic, dong2026hierarchical, xiang2025decentralized]
updated: 2026-11-15
---

# PPO / MAPPO

on-policy 的策略梯度方法，用 clipped objective 限制每次更新的幅度，穩定、好實作。MAPPO 是它的多智能體版本。

## 在這批論文中
- [[hiep2026dynamic]]：標準 PPO 被批評「探索策略固定」，所以改成依 reward 進步幅度動態調整熵權重（[[entropy-exploration]]）。
- [[dong2026hierarchical]]：MAPPO 是 baseline，在 5v5 對抗中勝率只有 42%，是四種方法中最低。
- [[xiang2025decentralized]]：高低層都用 MAPPO；低層改成「交替訓練」（先學隊形、再學避障、再合併微調）解決直接訓練收斂不好的問題。對手追捕者也是 PPO 策略。

## 爭議與矛盾
- **MAPPO 好不好用？** [[dong2026hierarchical]] 的 5v5 對抗中 MAPPO 勝率最低（42%）；[[xiang2025decentralized]] 則說 MAPPO 因為穩定、計算效率高，仍是實際系統的主流選擇。兩者任務不同，結論不一定衝突：MAPPO 單獨用在複雜多任務上收斂差，但加上階層或交替訓練後可用。

## 相關頁面
[[entropy-exploration]] · [[matd3]]
