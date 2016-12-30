# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(381, 273)
        MainWindow.setMinimumSize(QtCore.QSize(381, 273))
        MainWindow.setMaximumSize(QtCore.QSize(381, 273))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 100, 81, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(90, 170, 111, 31))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 151, 31))
        self.label.setObjectName("label")
        self.wanEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.wanEdit.setGeometry(QtCore.QRect(0, 50, 299, 20))
        self.wanEdit.setObjectName("wanEdit")
        self.inputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.inputEdit.setGeometry(QtCore.QRect(0, 130, 299, 20))
        self.inputEdit.setObjectName("inputEdit")
        self.outputEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.outputEdit.setGeometry(QtCore.QRect(0, 200, 299, 20))
        self.outputEdit.setObjectName("outputEdit")
        self.btnOpenVideo = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenVideo.setGeometry(QtCore.QRect(300, 130, 75, 23))
        self.btnOpenVideo.setObjectName("btnOpenVideo")
        self.btnOpenWAN1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnOpenWAN1.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.btnOpenWAN1.setObjectName("btnOpenWAN1")
        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(300, 200, 75, 23))
        self.btnSave.setObjectName("btnSave")
        self.lblFinished = QtWidgets.QLabel(self.centralwidget)
        self.lblFinished.setGeometry(QtCore.QRect(60, 230, 291, 20))
        self.lblFinished.setText("")
        self.lblFinished.setObjectName("lblFinished")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 381, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "We Are Number One Meme Generator"))
        self.label_2.setText(_translate("MainWindow", "Input video file:"))
        self.label_3.setText(_translate("MainWindow", "Output video file:"))
        self.label.setText(_translate("MainWindow", "We Are Number One video file:"))
        self.btnOpenVideo.setText(_translate("MainWindow", "Open..."))
        self.btnOpenWAN1.setText(_translate("MainWindow", "Open..."))
        self.btnSave.setText(_translate("MainWindow", "Save As..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

