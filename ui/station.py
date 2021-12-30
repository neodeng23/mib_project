# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'station.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidget
from ui.tree import MyTree


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(986, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.IPmodel = QtWidgets.QLineEdit(self.centralwidget)
        self.IPmodel.setObjectName("IPmodel")
        self.verticalLayout.addWidget(self.IPmodel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Start_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Start_Button.setObjectName("Start_Button")
        self.horizontalLayout.addWidget(self.Start_Button)
        self.Vchoice = QtWidgets.QComboBox(self.centralwidget)
        self.Vchoice.setObjectName("Export_Button")
        self.horizontalLayout.addWidget(self.Vchoice)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.Logmodel = QtWidgets.QTextBrowser(self.centralwidget)
        self.Logmodel.setObjectName("Logmodel")
        self.horizontalLayout_2.addWidget(self.Logmodel)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Refresh_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Refresh_Button.setObjectName("Refresh_Button")
        self.horizontalLayout_3.addWidget(self.Refresh_Button)
        self.Modify_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Modify_Button.setObjectName("Modify_Button")
        self.horizontalLayout_3.addWidget(self.Modify_Button)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.Tree = MyTree(self.centralwidget)
        self.Tree.setObjectName("Tree")
        self.verticalLayout_2.addWidget(self.Tree)
        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 5)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Cancon Mib Browser"))
        self.Start_Button.setText(_translate("MainWindow", "Start"))
        # self.Vchoice.setText(_translate("MainWindow", "Export"))
        self.Refresh_Button.setText(_translate("MainWindow", "Refresh"))
        self.Modify_Button.setText(_translate("MainWindow", "Modify"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
