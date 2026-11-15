---
type: entity
aliases: [Gazebo, PX4, SITL, Software-In-The-Loop, ROS]
papers: [wang2025rally, xiang2025decentralized]
updated: 2026-11-15
---

# Gazebo + ROS + PX4 SITL

高擬真的無人機軟體在環（Software-In-The-Loop）模擬：Gazebo 負責物理，PX4 是真實的飛控韌體，ROS 負責通訊。比 MPE 更接近實機，通常當作上實機前的最後一步。

## 在這批論文中
- [[wang2025rally]]：在 MPE 訓練後，到 SITL 驗證（固定高度，由 PX4 的 PID 追蹤加速度指令）。
- [[xiang2025decentralized]]：自建 ROS-based SITL，分散式非同步部署的表現達單機模擬的 97.1%（AT-M）和 92.7%（CI-HRL 隊形率）；也模擬了 3–8 m/s 的風和 0.3–0.8 m 的感測誤差。

> 💭 觀察：core 論文裡只有 RALLY 走到 SITL，沒有一篇上實機。無人機實機只有古典方法 [[zhou2023racer]]；其他有實機的（[[zhu2025lamarl]]、[[yu2025conavgpt]]）都是地面機器人。

## 相關頁面
[[mpe]]
