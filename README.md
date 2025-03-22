# 魔物獵人荒野 最近營地查詢系統

這是一個用於查詢魔物獵人荒野中最近營地的工具。

## 功能特點

- 支援多個地圖和區域的營地查詢
- 顯示所有營地距離，並按距離排序
- 跨平台支援（Windows 和 macOS）
- 現代化的圖形界面

## 系統需求

- Python 3.9 或更高版本
- PyQt6

## 安裝步驟

1. 克隆專案：
```bash
git clone [repository_url]
cd Auto_Camp
```

2. 創建並啟動虛擬環境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# 或
.venv\Scripts\activate  # Windows
```

3. 安裝依賴：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 啟動應用程式：
```bash
python mhw_camp_finder_qt.py
```

2. 在界面中：
   - 選擇地圖
   - 選擇區域
   - 點擊「查詢最近營地」按鈕
   - 查看結果

## 開發進度

### 2024-03-22
- 移除舊版 tkinter 實現
- 優化 PyQt6 界面
- 簡化專案結構
- 移除不必要的依賴

### 2024-03-22
- 初始版本發布
- 實現基本的營地查詢功能
- 使用 PyQt6 建立現代化界面
- 支援跨平台運行

## 注意事項

- 如果遇到 PyQt6 安裝問題，請確保使用正確的版本
- 在 macOS 上可能需要額外的權限設置

## 授權

MIT License 