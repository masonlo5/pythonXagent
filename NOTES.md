# Notes for this project

這個專案目前只有一個主要程式檔 `class1.py`，用途為一個使用 Pygame 的簡單繪圖/示範程式。

內容摘要：
- 匯入與初始化：使用 `pygame`、`sys`，並建立畫面（640x320）與時鐘（60 FPS）。
- 畫布：建立一個 `bg` Surface，背景填白（白色也用作橡皮擦顏色 `BG_COLOR`）。
- 繪圖工具：
  - 左鍵（mouse button 1）為畫筆，預設顏色為黑色。
  - 右鍵（mouse button 3）為橡皮擦（會以背景色繪製）。
  - 按住並移動時會以圓形與連線填補間隙，`brush_radius` 控制粗細（目前為 8）。
  - 按鍵 `c` 可以在黑色與背景色之間切換（快速橡皮擦切換）。
- 畫布範例繪製：程式啟動時會在 `bg` 上先繪製一些基本圖形（矩形、圓、橢圓、線條、多邊形、弧線）作為示範。
- 主迴圈：處理事件並把 `bg` blit 到視窗，然後更新顯示。

如何執行：
1. 安裝相依套件（需要 `pygame`）：
   - 建議使用 Python 虛擬環境，然後安裝 pygame：

      python3 -m pip install pygame

2. 執行程式：

      python3 class1.py

注意事項與建議：
- 若你不想把編譯產物（`__pycache__`、`.pyc`）推上 GitHub，已新增 `.gitignore`（參見專案根目錄）。
- 可以將繪圖功能抽成函式以利測試與擴充；若打算分享或發佈，請新增 `requirements.txt`（例如：`pygame==<version>`）。

檔案清單（目前）：
- `class1.py` — Pygame 繪圖示範程式（主要程式）。
- `NOTES.md` — 這份說明檔。
- `.gitignore` — 忽略型態清單。

如果要我繼續，我可以：
- 幫你把變更加入 Git、建立 commit、並嘗試推送到遠端 GitHub（需要遠端已設定且你具備推送權限）。
