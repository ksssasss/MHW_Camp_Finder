import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QComboBox, QPushButton, 
                            QTextEdit, QScrollArea, QTabWidget)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from map_data import MAP_DATA
from camp_settings import CampSettingsWidget

class MHWCampFinderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('魔物獵人荒野 最近營地查詢小工具')
        self.setGeometry(100, 100, 800, 600)
        
        # 設置應用程式字體
        self.setFont(QFont('Microsoft JhengHei', 10))
        
        # 創建中央部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 創建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 標題
        title_label = QLabel("魔物獵人荒野 最近營地查詢系統")
        title_label.setFont(QFont('微軟正黑體', 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title_label)
        
        # 創建分頁
        tab_widget = QTabWidget()
        tab_widget.setFont(QFont('微軟正黑體', 12))
        
        # 查詢分頁
        query_tab = QWidget()
        query_layout = QVBoxLayout(query_tab)
        
        # 地圖選擇區域
        map_layout = QHBoxLayout()
        map_label = QLabel("選擇地圖：")
        map_label.setFont(QFont('微軟正黑體', 12))
        self.map_combo = QComboBox()
        self.map_combo.setFont(QFont('微軟正黑體', 12))
        # 按照指定順序添加地圖
        map_order = ['天塹沙原', '緋紅森林', '湧油山谷', '冰霧斷崖', '龍都遺跡']
        self.map_combo.addItems(map_order)
        self.map_combo.currentTextChanged.connect(self.on_map_selected)
        map_layout.addWidget(map_label)
        map_layout.addWidget(self.map_combo)
        map_layout.addStretch()
        query_layout.addLayout(map_layout)
        
        # 區域選擇區域
        area_layout = QHBoxLayout()
        area_label = QLabel("選擇區域：")
        area_label.setFont(QFont('微軟正黑體', 12))
        self.area_combo = QComboBox()
        self.area_combo.setFont(QFont('微軟正黑體', 12))
        self.area_combo.currentTextChanged.connect(self.on_area_selected)
        area_layout.addWidget(area_label)
        area_layout.addWidget(self.area_combo)
        area_layout.addStretch()
        query_layout.addLayout(area_layout)
        
        # 查詢按鈕
        self.search_button = QPushButton("查詢最近營地")
        self.search_button.setFont(QFont('微軟正黑體', 12))
        self.search_button.setEnabled(False)
        self.search_button.clicked.connect(self.find_nearest_camp)
        query_layout.addWidget(self.search_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 結果顯示區域
        result_label = QLabel("查詢結果：")
        result_label.setFont(QFont('微軟正黑體', 12))
        query_layout.addWidget(result_label)
        
        self.result_text = QTextEdit()
        self.result_text.setFont(QFont('微軟正黑體', 12))
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(200)
        query_layout.addWidget(self.result_text)
        
        # 營地設定分頁
        self.camp_settings = CampSettingsWidget()
        
        # 添加分頁
        tab_widget.addTab(query_tab, "營地查詢")
        tab_widget.addTab(self.camp_settings, "營地設定")
        
        main_layout.addWidget(tab_widget)
        
        # 初始化區域列表
        self.on_map_selected(self.map_combo.currentText())
        
    def on_map_selected(self, map_name):
        """處理地圖選擇事件"""
        self.area_combo.clear()
        if map_name in MAP_DATA:
            map_data = MAP_DATA[map_name]
            # 使用第一個營地的距離數據來確定區域數量
            first_camp = next(iter(map_data['camps'].values()))
            max_area = max(first_camp.keys())
            areas = list(range(1, max_area + 1))
            self.area_combo.addItems([f"區域 {area}" for area in areas])
            
            # 清空查詢結果
            self.result_text.clear()
            self.result_text.append("請選擇區域...")
            
    def on_area_selected(self, area_name):
        """處理區域選擇事件"""
        if area_name:
            self.search_button.setEnabled(True)
            
    def find_nearest_camp(self):
        """查詢最近營地"""
        try:
            selected_map = self.map_combo.currentText()
            selected_area = self.area_combo.currentText()
            
            if not selected_map or not selected_area:
                self.result_text.setText("請選擇地圖和區域")
                return
                
            # 從區域名稱中提取區域編號
            area_number = int(selected_area.split()[-1])
            
            # 獲取該地圖的營地資料
            map_data = MAP_DATA[selected_map]
            camps = map_data['camps']
            
            # 獲取已啟用的營地列表
            enabled_camps = self.camp_settings.get_enabled_camps(selected_map)
            
            if not enabled_camps:
                self.result_text.setText("請先在營地設定中選擇可用的營地")
                return
            
            # 計算每個已啟用營地到選擇區域的距離
            distances = {}
            for camp_name in enabled_camps:
                if area_number in camps[camp_name]:
                    distances[camp_name] = camps[camp_name][area_number]
            
            # 按距離排序營地
            sorted_camps = sorted(distances.items(), key=lambda x: x[1])
            
            # 顯示結果
            result_text = f"地圖：{selected_map}<br>"
            result_text += f"區域：{selected_area}<br><br>"
            result_text += "最近的營地：<br>"
            
            # 使用HTML格式顯示結果
            for i, (camp_name, distance) in enumerate(sorted_camps):
                if i == 0:  # 最近的營地
                    result_text += f'<b><span style="color: #4A90E2">{camp_name}: {distance} 公尺</span></b><br>'
                else:  # 其他營地
                    result_text += f"{camp_name}: {distance} 公尺<br>"
                
            self.result_text.setHtml(result_text)
            
        except Exception as e:
            self.result_text.setText(f"查詢時發生錯誤：{str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MHWCampFinderApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 