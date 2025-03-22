import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLabel, QComboBox, QPushButton, 
                            QTextEdit, QScrollArea)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from map_data import MAP_DATA

class MHWCampFinderApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("魔物獵人荒野 最近營地查詢系統")
        self.setMinimumSize(800, 600)
        
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
        
        # 地圖選擇區域
        map_layout = QHBoxLayout()
        map_label = QLabel("選擇地圖：")
        map_label.setFont(QFont('微軟正黑體', 12))
        self.map_combo = QComboBox()
        self.map_combo.setFont(QFont('微軟正黑體', 12))
        self.map_combo.addItems(MAP_DATA.keys())
        self.map_combo.currentTextChanged.connect(self.on_map_selected)
        map_layout.addWidget(map_label)
        map_layout.addWidget(self.map_combo)
        map_layout.addStretch()
        main_layout.addLayout(map_layout)
        
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
        main_layout.addLayout(area_layout)
        
        # 查詢按鈕
        self.search_button = QPushButton("查詢最近營地")
        self.search_button.setFont(QFont('微軟正黑體', 12))
        self.search_button.setEnabled(False)
        self.search_button.clicked.connect(self.find_nearest_camp)
        main_layout.addWidget(self.search_button, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # 結果顯示區域
        result_label = QLabel("查詢結果：")
        result_label.setFont(QFont('微軟正黑體', 12))
        main_layout.addWidget(result_label)
        
        self.result_text = QTextEdit()
        self.result_text.setFont(QFont('微軟正黑體', 12))
        self.result_text.setReadOnly(True)
        self.result_text.setMinimumHeight(200)
        main_layout.addWidget(self.result_text)
        
        # 初始化區域列表
        self.on_map_selected(self.map_combo.currentText())
        
    def on_map_selected(self, map_name):
        """處理地圖選擇事件"""
        self.area_combo.clear()
        if map_name in MAP_DATA:
            # 添加區域選項
            areas = list(range(1, 18))  # 1-17 區域
            self.area_combo.addItems([f"區域 {area}" for area in areas])
            self.search_button.setEnabled(False)
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
            camp_names = map_data['camp_names']
            
            # 計算每個營地到選擇區域的距離
            distances = {}
            for camp_name, distances_dict in camps.items():
                distances[camp_name] = distances_dict[area_number]
            
            # 按距離排序營地
            sorted_camps = sorted(distances.items(), key=lambda x: x[1])
            
            # 顯示結果
            result_text = f"地圖：{selected_map}\n"
            result_text += f"區域：{selected_area}\n\n"
            result_text += "最近的營地：\n"
            
            for camp_name, distance in sorted_camps:
                result_text += f"{camp_name}: {distance} 公尺\n"
                
            self.result_text.setText(result_text)
            
        except Exception as e:
            self.result_text.setText(f"查詢時發生錯誤：{str(e)}")

def main():
    app = QApplication(sys.argv)
    window = MHWCampFinderApp()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 