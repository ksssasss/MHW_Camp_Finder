# 魔物獵人荒野 最近營地查詢系統

這是一個用於查詢魔物獵人荒野中最近營地的工具。使用 PyQt6 開發的圖形界面應用程式。

## 功能特點

- 支援多個地圖區域：
  - 遺跡平原 (Ruins of Wyveria)
  - 冰霜峭壁 (Iceshard Cliffs)
  - 油井盆地 (Oilwell Basin)
  - 緋紅森林 (Scarlet Forest)
  - 迎風平原 (Windward Plains)
- 直觀的圖形界面
- 即時查詢最近營地
- 顯示詳細的距離資訊

## 系統需求

- Python 3.8 或更高版本
- PyQt6
- 其他依賴項請參考 requirements.txt

## 安裝步驟

1. 克隆此倉庫：
```bash
git clone https://github.com/ksssasss/MHW_Camp_Finder.git
cd MHW_Camp_Finder
```

2. 創建並啟動虛擬環境：
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# 或
.venv\Scripts\activate  # Windows
```

3. 安裝依賴項：
```bash
pip install -r requirements.txt
```

## 使用方法

1. 啟動程式：
```bash
python mhw_camp_finder_qt.py
```

2. 在界面中：
   - 選擇要查詢的地圖
   - 選擇目標區域
   - 點擊「查詢最近營地」按鈕
   - 查看結果

## 數據結構說明

### 地圖數據格式

每個地圖的數據結構包含兩個主要部分：

1. `camps` 字典：
   - 包含所有營地的日文名稱
   - 每個營地都有到其他區域的距離數據
   - 距離單位為公尺

2. `camp_names` 字典：
   - 將數字索引映射到營地名稱
   - 用於在程式中識別和顯示營地

### 最近更新

- 2024-03-21: 統一所有地圖的數據結構格式
  - 將所有地圖數據轉換為新的標準格式
  - 包含完整的營地距離資訊
  - 優化程式碼以適應新的數據結構

## 開發者說明

### 數據更新

如需更新地圖數據，請修改 `map_data.py` 文件，確保遵循以下格式：

```python
MAP_DATA = {
    '地圖名稱': {
        'camps': {
            '營地名稱': {
                區域編號: 距離,
                ...
            },
            ...
        },
        'camp_names': {
            索引: '營地名稱',
            ...
        }
    }
}
```

### 注意事項

- 確保所有距離數據的單位統一（公尺）
- 保持營地名稱的一致性
- 更新數據時注意保持格式正確

## 授權

MIT License 