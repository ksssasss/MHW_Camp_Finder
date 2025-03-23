# Windows 打包說明

## 環境設置
1. 安裝 Python 3.9 或更高版本
2. 安裝所需套件：
```bash
pip install -r requirements.txt
pip install pyinstaller
```

## 打包步驟
1. 開啟命令提示字元（CMD）或 PowerShell
2. 切換到專案目錄：
```bash
cd 專案目錄路徑
```
3. 執行打包命令：
```bash
pyinstaller mhw_camp_finder_win.spec
```
4. 打包完成後，執行檔將位於 `dist` 資料夾中

## 注意事項
- 確保系統安裝了 Microsoft Visual C++ Redistributable
- 如果遇到字體問題，請確保系統安裝了 Microsoft JhengHei 字體
- 打包過程中如果出現錯誤，請檢查 Python 和所有依賴套件的版本是否正確

## 測試步驟
1. 進入 `dist` 資料夾
2. 執行 `魔物獵人荒野 最近營地查詢小工具.exe`
3. 測試以下功能：
   - 地圖選擇
   - 區域選擇
   - 營地查詢
   - 營地設定
   - 中文顯示
   - 視窗縮放 