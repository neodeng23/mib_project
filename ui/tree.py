#!/usr/bin/env python3

import json
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QApplication
from func.string_handler import get_desktop


class MyTree(QTreeWidget):
    def __init__(self, parent=None):
        super(MyTree, self).__init__(parent)
        self.setWindowTitle('Tree')
        # 设置列数
        self.setColumnCount(4)
        # 设置头的标题
        self.setHeaderLabels(['Name', 'OID', 'Value', 'attribute'])

    def add_new_tree(self, dict):
        jsonpath = get_desktop() + '\\OID.json'
        f = open(jsonpath, encoding='utf-8')
        res = f.read()  # 读文件
        dict = json.loads(res)
        root = QTreeWidgetItem(self)
        root.setText(0, 'bmc')
        test_group = list(dict.keys())
        for group_name in test_group:
            value = group_name
            group_name = QTreeWidgetItem(root)
            group_name.setText(0, value)

        # child1 = QTreeWidgetItem(root)
        # child1.setText(0, 'child1')
        # child1.setText(1, '1')
        #
        # child2 = QTreeWidgetItem(root)
        # child2.setText(0, 'child2')
        # child2.setText(1, '2')
        #
        # child3 = QTreeWidgetItem(root)
        # child3.setText(0, 'child3')
        # child3.setText(1, '3')
        #
        # child4 = QTreeWidgetItem(child3)
        # child4.setText(0, 'child4')
        # child4.setText(1, '4')
        #
        # child5 = QTreeWidgetItem(child3)
        # child5.setText(0, 'child5')
        # child5.setText(1, '5')
