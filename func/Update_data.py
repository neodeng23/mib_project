# code:utf-8
from PyQt5.QtCore import QThread, pyqtSignal
import os


class Update_data(QThread):
    """更新数据类"""
    sinOut = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Update_data, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.flag = 1

    def run(self):
        res_flag = 0
        mib_loc = os.getcwd() + "\\" + "SNK-BMC-MIB.mib"
        # try:
        #
        # except:
        #     res_flag = 1
        #     row_list = [["invaild csv"]]

        if res_flag == 0:
            res_pass = ['All_Pass!!!!', '', '', '', '', '', '', '', '', total_time]
            self.sinOut.emit(res_pass)
        else:
            res_fail = ['Test_Fail!!!!', '', '', '', '', '', '', '', '', total_time]
            self.sinOut.emit(res_fail)
