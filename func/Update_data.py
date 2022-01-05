# code:utf-8
from PyQt5.QtCore import QThread, pyqtSignal
import os
import json
import time
from func.makejson import Makejson
import func.globalvar as gl
from func.string_handler import get_desktop
from func.common import TraverseSend


class Update_data(QThread):
    """更新数据类"""
    sinOut = pyqtSignal(list)

    def __init__(self, parent=None):
        super(Update_data, self).__init__(parent)
        # 设置工作状态与初始num数值
        self.working = True
        self.flag = 1

    def run(self):
        log = gl.get_value('log_func')
        BMCip = gl.get_value('ip')
        log("线程开始，先读取Mib文件转换为json")
        mib_loc = os.getcwd() + "\\" + "SNK-BMC-MIB.mib"
        mib_dict = Makejson()
        log("mib.json已在桌面生成，接下类将向" + str(BMCip) + "遍历指令")
        res_dict = TraverseSend(BMCip, 1)
        jsonpath = get_desktop() + '\\res.json'
        if os.path.exists(jsonpath):
            print("res.json exist , now delate")
            os.remove(jsonpath)
        with open(jsonpath, 'w') as f:
            json.dump(res_dict, f, indent=2)

        if res_flag == 0:
            res_pass = ['All_Pass!!!!', '', '', '', '', '', '', '', '', total_time]
            self.sinOut.emit(res_pass)
        else:
            res_fail = ['Test_Fail!!!!', '', '', '', '', '', '', '', '', total_time]
            self.sinOut.emit(res_fail)
