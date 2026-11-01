# ConceptLens 🔍 | 抽象概念的白話認知透鏡

> **用 AI 做出一件東西：一個能打破術語高牆、分享給所有學習者的認知透鏡。**  
> 基於費曼學習法（Feynman Technique）與認知負荷理論（Cognitive Load Theory）構建的互動式概念解構 Web 應用。

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Status: Production Ready](https://img.shields.io/badge/Status-Ready-emerald.svg)]()
[![Platform: Web](https://img.shields.io/badge/Platform-Web-indigo.svg)]()

---

## 🌟 核心理念與亮點

大家一定有過類似經驗：**「讀得懂教科書上的每一個字，合在一起卻完全看不懂在講什麼。」**  
傳統教材往往陷入「用術語解釋術語」的死循環，造成學習者嚴重的認知超載。

**ConceptLens** 透過 AI 的語義降維能力，將任何晦澀、抽象的學術與科技概念化為具備「直覺感」的認知體驗：

- 🧒 **三層漸進式費曼透鏡**：
  - **Level 1 (5 歲小孩也能懂)**：摒除所有黑話，用生活中的實體日常道具建立第一層心智錨點。
  - **Level 2 (大學通識與功能剖析)**：剖析概念最初為了解決什麼歷史痛點，以及底層機制（如 Q, K, V 搜尋模型）。
  - **Level 3 (硬核本質與數學公式)**：KaTeX 即時渲染規範公式，深入分析防爆縮放因子與邊界限制。
- 🎭 **跨維度生活比喻轉換器 (Analogy Switcher)**：
  - 一鍵切換 **🍳 頂級大廚煮高湯**、**🎮 RPG 副本組隊**、**🕵️ 福爾摩斯辦案** 或 **🏀 NBA 球隊戰術** 等熟悉維度，按需理解。
- 🗺️ **動態因果認知心智圖**：
  - 整合 Mermaid.js 自動繪製「輸入 ➔ 核心計算 ➔ 輸出融合」的因果流，雙重編碼強化記憶。
- ⚡ **主動提取隨堂快問 (Active Recall)**：
  - 配備直覺陷阱診斷題，點擊即時給予觀念回饋，打破「以為自己懂了」的被動假象。
- 🚀 **零安裝、開箱即用**：
  - 純靜態客戶端架構，預載 Transformer、貝氏定理、量子糾纏、囚徒困境、貨幣通膨等跨領域範例，同時支援自訂 Gemini API Key 探索任何自訂詞彙。

---

## 📁 專案結構 (Project Structure)

```text
concept-lens/
├── index.html         # 核心互動式 Web 應用程式 (可直接以瀏覽器開啟)
├── slides.html        # 專題發表專用互動簡報 (支援鍵盤方向鍵、講者備忘稿 N、全螢幕 F)
├── REPORT.md          # 完整專題成果報告 (做什麼、給誰用、怎麼跟 AI 做、查了什麼、下一步)
├── app.py             # 輕量級 Python 本地預覽伺服器 (選用)
├── README.md          # 專案介紹與開源說明
└── LICENSE            # MIT 開源授權協議
```

---

## 🚀 快速上手 (Quick Start)

本專案採用 **Zero-Dependency（零外部環境依賴）** 哲學，無需安裝 Node.js 或複雜套件：

### 方法一：直接點擊開啟（最簡便）
1. 將本專案下載或 Clone 到本機。
2. 直接雙擊開啟 **`index.html`**，即可在 Chrome / Edge / Safari 等現代瀏覽器中體驗完整功能！
3. 雙擊開啟 **`slides.html`**，即可進入簡報展示模式。

### 方法二：透過 Python 本地伺服器開啟
若你安裝了 Python，可以在專案目錄下執行：
```bash
python app.py
```
系統會自動在預設瀏覽器中開啟 `http://localhost:8000`。

---

## 🖥️ 課堂簡報操作說明 (`slides.html`)

針對現場口頭報告量身打造的極簡簡報系統：
- **切換投影片**：鍵盤方向鍵 <kbd>→</kbd> / <kbd>←</kbd> 或 <kbd>Space</kbd> 空白鍵。
- **講者備忘稿 (Presenter Notes)**：按鍵盤 <kbd>N</kbd> 鍵，下方會彈出每頁投影片的精準時間控制講稿。
- **全螢幕播放**：按鍵盤 <kbd>F</kbd> 鍵即可切換全螢幕劇院模式。

---

## 📚 理論與文獻基礎 (Theoretical Foundations)

本專案之設計深度借鑒教育心理學與認知科學經典文獻：
1. **認知負荷理論 (Cognitive Load Theory)** — Sweller, J. (1988)
2. **雙重編碼理論 (Dual-Coding Theory)** — Paivio, A. (1971)
3. **費曼學習法 (The Feynman Technique)** — Richard Feynman
4. **提取練習與測試效應 (Testing / Retrieval Effect)** — Roediger & Karpicke (2006)

---

## 📄 期中專題報告

完整之書面報告（包含五大標準結構：做什麼、給誰用、怎麼跟 AI 一起做、查了什麼、下一步）已完整收錄於本 Repo 的 [`REPORT.md`](REPORT.md) 文件中。

---

## ⚖️ 授權條款 (License)

本專案基於 [MIT License](LICENSE) 條款開源發布。
