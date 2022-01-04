#!/usr/bin/env python3

import json
import sys
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QApplication
from func.string_handler import get_desktop
import func.globalvar as gl


class MyTree(QTreeWidget):
    def __init__(self, parent=None):
        super(MyTree, self).__init__(parent)
        self.setWindowTitle('Tree')
        # 设置列数
        self.setColumnCount(4)
        # 设置头的标题
        self.setHeaderLabels(['Name', 'OID', 'Value', 'attribute'])
        self.rootList = []

    def generateTreeWidget(self, data, root):
        if isinstance(data, dict):
            for key in data.keys():
                child = QTreeWidgetItem()
                child.setText(0, key)
                if isinstance(root, QTreeWidget) == False:  # 非根节点，添加子节点
                    root.addChild(child)
                self.rootList.append(child)
                value = data[key]
                self.generateTreeWidget(value, child)
        else:
            root.setText(1, str(data))
            root.setText(2, str(self.ret[str(data)]))

    def showdata(self):
        log = gl.get_value('log_func')
        log("start")

        oidpath = get_desktop() + '\\OID.json'
        with open(oidpath) as json_file:
            data = json.load(json_file)
        root = self
        retpath = get_desktop() + '\\res.json'
        with open(retpath) as json_file:
            self.ret = json.load(json_file)

        self.generateTreeWidget(data, root)
        self.insertTopLevelItems(0, self.rootList)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MyTree()
    win.show()
    sys.exit(app.exec_())