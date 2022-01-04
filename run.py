import sys
import time
from func.logger import Logger
from func.Update_data import Update_data
import func.globalvar as gl
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPalette
from PyQt5.QtCore import Qt
from ui.station import Ui_MainWindow


pe_red = QPalette()
pe_red.setColor(QPalette.WindowText, Qt.red)

pe_green = QPalette()
pe_green.setColor(QPalette.WindowText, Qt.green)

pe_yel = QPalette()
pe_yel.setColor(QPalette.WindowText, Qt.yellow)


class MyMainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.thread = Update_data()

        gl._init()  # 日志模块
        gl.set_value('log_func', self.write_log)

        # 按键绑定信号
        self.Start_Button.clicked.connect(self.click_start)
        self.Refresh_Button.clicked.connect(self.Tree.showdata)
        # IP输入绑定信号
        self.IPmodel.returnPressed.connect(self.click_start)
        # self.thread.sinOut.connect(self.Tree.add_new_tree)

    def click_start(self):
        # 获取SN
        BMCip = self.IPmodel.text()
        # 初始化Log
        gl.set_value('ip', BMCip)# 实例化对象设为全局变量
        # SN输入框无法编辑
        self.IPmodel.setReadOnly(True)
        # 开始按键变灰
        self.Start_Button.setEnabled(False)
        self.Vchoice.setEnabled(False)
        # 测试线程开始
        self.thread.start()

    def write_log(self, string):
        now = time.localtime()
        nowt = time.strftime("%m-%d %H:%M:%S ", now)
        input = str(nowt) + ' : ' + str(string)
        self.Logmodel.append(input)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MyMainForm()
    mainWindow.show()
    sys.exit(app.exec_())
