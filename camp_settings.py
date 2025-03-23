import json
import os
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                            QCheckBox, QGroupBox, QScrollArea, QPushButton)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QFont
from map_data import MAP_DATA

class CampSettingsWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.settings_file = 'camp_settings.json'
        self.camp_limits = {
            '天塹沙原': 5,
            '緋紅森林': 5,
            '湧油山谷': 5,
            '冰霧斷崖': 5,
            '龍都遺跡': 4
        }
        # 定義預設勾選且不可變動的營地
        self.default_camps = {
            '大本營': True,
            '莫利巴之家': True,
            '風音之村': True
        }
        self.checkboxes = {}
        self.warning_labels = {}  # 儲存每個地圖的警告標籤
        self.load_settings()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 標題
        title = QLabel("營地選擇設定")
        title.setFont(QFont('微軟正黑體', 14, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # 說明文字
        description = QLabel("請選擇每個地圖可用的營地（勾選表示可用）")
        description.setFont(QFont('微軟正黑體', 12))
        description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(description)
        
        # 創建滾動區域
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        # 創建容器widget
        container = QWidget()
        container_layout = QVBoxLayout(container)
        
        # 按照指定順序為每個地圖創建選擇區域
        map_order = ['天塹沙原', '緋紅森林', '湧油山谷', '冰霧斷崖', '龍都遺跡']
        for map_name in map_order:
            # 創建地圖標題區域
            title_layout = QHBoxLayout()
            
            # 地圖名稱
            map_title = QLabel(map_name)
            map_title.setFont(QFont('微軟正黑體', 12))
            title_layout.addWidget(map_title)
            
            # 警告訊息標籤
            warning_label = QLabel()
            warning_label.setFont(QFont('微軟正黑體', 11))
            warning_label.setStyleSheet("color: red;")
            warning_label.setAlignment(Qt.AlignmentFlag.AlignLeft)
            title_layout.addWidget(warning_label)
            
            # 添加彈性空間
            title_layout.addStretch()
            
            # 創建群組框
            group_box = QGroupBox()
            group_box.setFont(QFont('微軟正黑體', 12))
            group_layout = QVBoxLayout()
            
            # 添加地圖標題區域
            group_layout.addLayout(title_layout)
            
            # 添加按鈕區域
            button_layout = QHBoxLayout()
            select_all_btn = QPushButton("全選")
            select_all_btn.setFont(QFont('微軟正黑體', 11))
            select_all_btn.clicked.connect(lambda checked, m=map_name: self.select_all_camps(m))
            clear_all_btn = QPushButton("清空")
            clear_all_btn.setFont(QFont('微軟正黑體', 11))
            clear_all_btn.clicked.connect(lambda checked, m=map_name: self.clear_all_camps(m))
            
            button_layout.addWidget(select_all_btn)
            button_layout.addWidget(clear_all_btn)
            button_layout.addStretch()
            
            group_layout.addLayout(button_layout)
            
            # 獲取該地圖的所有營地
            camps = MAP_DATA[map_name]['camps']
            self.checkboxes[map_name] = {}
            
            # 創建每個營地的勾選框
            for camp_name in camps:
                checkbox = QCheckBox(camp_name)
                checkbox.setFont(QFont('微軟正黑體', 11))
                
                # 特殊處理預設勾選的營地
                if camp_name in self.default_camps:
                    checkbox.setChecked(True)  # 預設勾選
                    checkbox.setEnabled(False)  # 禁用勾選框
                else:
                    # 設置其他營地的初始狀態
                    checkbox.setChecked(self.saved_settings.get(map_name, {}).get(camp_name, False))
                    # 連接信號
                    checkbox.stateChanged.connect(self.on_checkbox_changed)
                
                group_layout.addWidget(checkbox)
                self.checkboxes[map_name][camp_name] = checkbox
            
            group_box.setLayout(group_layout)
            container_layout.addWidget(group_box)
            
            # 保存警告標籤的引用
            self.warning_labels[map_name] = warning_label
        
        scroll.setWidget(container)
        layout.addWidget(scroll)

    def get_selected_camps_count(self, map_name):
        """獲取指定地圖中已選擇的營地數量（不包括預設營地）"""
        if map_name not in self.checkboxes:
            return 0
        
        count = 0
        for camp_name, checkbox in self.checkboxes[map_name].items():
            if camp_name not in self.default_camps and checkbox.isChecked():
                count += 1
        return count

    def show_warning(self, map_name, message):
        """顯示警告訊息"""
        if map_name in self.warning_labels:
            self.warning_labels[map_name].setText(message)
            # 3秒後自動清除警告
            QTimer.singleShot(3000, lambda: self.warning_labels[map_name].setText(""))

    def on_checkbox_changed(self, state):
        """處理勾選框狀態改變"""
        # 獲取被點擊的勾選框
        checkbox = self.sender()
        if not checkbox:
            return

        # 找到這個勾選框對應的地圖和營地名稱
        map_name = None
        camp_name = None
        for m_name, camps in self.checkboxes.items():
            for c_name, cb in camps.items():
                if cb == checkbox:
                    map_name = m_name
                    camp_name = c_name
                    break
            if map_name:
                break

        if not map_name or not camp_name:
            return

        # 如果是預設營地，不需要檢查數量
        if camp_name in self.default_camps:
            return

        # 檢查是否超過限制
        if state == Qt.CheckState.Checked.value:
            current_count = self.get_selected_camps_count(map_name)
            if current_count > self.camp_limits[map_name]:
                # 顯示警告訊息
                self.show_warning(map_name, f"提醒：營地數量只能設置{self.camp_limits[map_name]}個")

        self.save_settings()

    def select_all_camps(self, map_name):
        """選中指定地圖的所有營地（除了預設勾選的營地）"""
        if map_name in self.checkboxes:
            for camp_name, checkbox in self.checkboxes[map_name].items():
                if camp_name not in self.default_camps:  # 跳過預設勾選的營地
                    checkbox.setChecked(True)
            
            # 檢查是否超過限制
            current_count = self.get_selected_camps_count(map_name)
            if current_count > self.camp_limits[map_name]:
                self.show_warning(map_name, f"提醒：營地數量只能設置{self.camp_limits[map_name]}個")
            
            self.save_settings()

    def clear_all_camps(self, map_name):
        """清空指定地圖的所有營地（除了預設勾選的營地）"""
        if map_name in self.checkboxes:
            for camp_name, checkbox in self.checkboxes[map_name].items():
                if camp_name not in self.default_camps:  # 跳過預設勾選的營地
                    checkbox.setChecked(False)
            self.save_settings()

    def load_settings(self):
        """載入已保存的設定"""
        self.saved_settings = {}
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r', encoding='utf-8') as f:
                    self.saved_settings = json.load(f)
            except Exception as e:
                print(f"載入設定時發生錯誤：{str(e)}")

    def save_settings(self):
        """保存設定到檔案"""
        settings = {}
        for map_name, camps in self.checkboxes.items():
            settings[map_name] = {
                camp_name: checkbox.isChecked()
                for camp_name, checkbox in camps.items()
            }
        
        try:
            with open(self.settings_file, 'w', encoding='utf-8') as f:
                json.dump(settings, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"保存設定時發生錯誤：{str(e)}")

    def get_enabled_camps(self, map_name):
        """獲取指定地圖中已啟用的營地列表"""
        if map_name in self.checkboxes:
            return [
                camp_name for camp_name, checkbox in self.checkboxes[map_name].items()
                if checkbox.isChecked()
            ]
        return [] 