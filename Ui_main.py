# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Z:\work\program\pyQt\project\main.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtCore import QTimer

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("color: rgb(85, 85, 127);")
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pushButton_sweepFreq = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_sweepFreq.setGeometry(QtCore.QRect(190, 140, 71, 51))
        self.pushButton_sweepFreq.setObjectName("pushButton")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 140, 141, 51))
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar.setGeometry(QtCore.QRect(460, 110, 231, 51))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralWidget)
        self.line.setGeometry(QtCore.QRect(20, 10, 411, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralWidget)
        self.line_2.setGeometry(QtCore.QRect(20, 580, 411, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralWidget)
        self.line_3.setGeometry(QtCore.QRect(10, 20, 20, 571))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralWidget)
        self.line_4.setGeometry(QtCore.QRect(420, 20, 20, 571))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(self.centralWidget)
        self.line_5.setGeometry(QtCore.QRect(450, 10, 331, 20))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 111, 41))
        self.label.setObjectName("label")
        self.pushButton_pause = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_pause.setGeometry(QtCore.QRect(270, 140, 71, 51))
        self.pushButton_pause.setObjectName("pushButton_pause")
        self.line_6 = QtWidgets.QFrame(self.centralWidget)
        self.line_6.setGeometry(QtCore.QRect(440, 20, 20, 151))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralWidget)
        self.line_7.setGeometry(QtCore.QRect(450, 160, 331, 20))
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralWidget)
        self.line_8.setGeometry(QtCore.QRect(770, 20, 20, 151))
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(460, 20, 111, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(460, 180, 111, 41))
        self.label_3.setObjectName("label_3")
        self.line_9 = QtWidgets.QFrame(self.centralWidget)
        self.line_9.setGeometry(QtCore.QRect(440, 180, 20, 411))
        self.line_9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralWidget)
        self.line_10.setGeometry(QtCore.QRect(770, 180, 20, 411))
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralWidget)
        self.line_11.setGeometry(QtCore.QRect(450, 580, 331, 20))
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.line_12 = QtWidgets.QFrame(self.centralWidget)
        self.line_12.setGeometry(QtCore.QRect(450, 170, 331, 20))
        self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_12.setObjectName("line_12")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(30, 60, 121, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton_stop = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_stop.setGeometry(QtCore.QRect(350, 140, 71, 51))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.label_netconnect = QtWidgets.QLabel(self.centralWidget)
        self.label_netconnect.setGeometry(QtCore.QRect(310, 60, 32, 32))
        self.label_netconnect.setText("")
        self.label_netconnect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        self.label_netconnect.setObjectName("label_netconnect")
        self.pushButton_netconnect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_netconnect.setGeometry(QtCore.QRect(350, 60, 71, 31))
        self.pushButton_netconnect.setObjectName("pushButton_netconect")
        self.lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_serial0connect = QtWidgets.QLabel(self.centralWidget)
        self.label_serial0connect.setGeometry(QtCore.QRect(310, 100, 32, 32))
        self.label_serial0connect.setText("")
        self.label_serial0connect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        self.label_serial0connect.setObjectName("label_serial0connect")
        self.pushButton_serial0connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_serial0connect.setGeometry(QtCore.QRect(350, 100, 71, 31))
        self.pushButton_serial0connect.setObjectName("pushButton_serial0connect")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(30, 250, 81, 31))
        self.label_5.setObjectName("label_5")
        self.pushButton_serial1connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_serial1connect.setGeometry(QtCore.QRect(460, 60, 71, 41))
        self.pushButton_serial1connect.setObjectName("pushButton_serial1connect")
        self.label_serial1connect = QtWidgets.QLabel(self.centralWidget)
        self.label_serial1connect.setGeometry(QtCore.QRect(540, 61, 31, 41))
        self.label_serial1connect.setText("")
        self.label_serial1connect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        self.label_serial1connect.setObjectName("label_serial1connect")
        self.pushButton_programmer = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_programmer.setGeometry(QtCore.QRect(700, 110, 71, 51))
        self.pushButton_programmer.setObjectName("pushButton_programmer")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_9.setGeometry(QtCore.QRect(700, 60, 71, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.label_serial2connect = QtWidgets.QLabel(self.centralWidget)
        self.label_serial2connect.setGeometry(QtCore.QRect(540, 230, 32, 32))
        self.label_serial2connect.setText("")
        self.label_serial2connect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        self.label_serial2connect.setObjectName("label_serial2connect")
        self.pushButton_serial2connect = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_serial2connect.setGeometry(QtCore.QRect(460, 230, 71, 31))
        self.pushButton_serial2connect.setObjectName("pushButton_serial2connect")
        self.listView = QtWidgets.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(460, 371, 311, 211))
        self.listView.setObjectName("listView")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(460, 340, 91, 31))
        self.label_6.setObjectName("label_6")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralWidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(460, 280, 131, 51))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_11.setGeometry(QtCore.QRect(600, 280, 51, 51))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_12.setGeometry(QtCore.QRect(720, 280, 51, 51))
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(610, 250, 81, 21))
        self.label_7.setObjectName("label_7")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_13.setGeometry(QtCore.QRect(660, 280, 51, 51))
        self.pushButton_13.setObjectName("pushButton_13")
        self.toolButton = QtWidgets.QToolButton(self.centralWidget)
        self.toolButton.setGeometry(QtCore.QRect(350, 200, 71, 51))
        self.toolButton.setObjectName("toolButton")
        self.label_12 = QtWidgets.QLabel(self.centralWidget)
        self.label_12.setGeometry(QtCore.QRect(740, 250, 31, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(690, 250, 41, 21))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_13 = QtWidgets.QLabel(self.centralWidget)
        self.label_13.setGeometry(QtCore.QRect(610, 220, 81, 21))
        self.label_13.setObjectName("label_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(690, 220, 41, 21))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_14 = QtWidgets.QLabel(self.centralWidget)
        self.label_14.setGeometry(QtCore.QRect(740, 220, 31, 21))
        self.label_14.setObjectName("label_14")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralWidget)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 200, 311, 51))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit.setGeometry(QtCore.QRect(30, 280, 391, 301))
        self.textEdit.setObjectName("textEdit")
        self.label_15 = QtWidgets.QLabel(self.centralWidget)
        self.label_15.setGeometry(QtCore.QRect(30, 100, 111, 31))
        self.label_15.setObjectName("label_15")
        self.spinBox = QtWidgets.QSpinBox(self.centralWidget)
        self.spinBox.setGeometry(QtCore.QRect(140, 100, 41, 31))
        self.spinBox.setObjectName("spinBox")
        self.label_16 = QtWidgets.QLabel(self.centralWidget)
        self.label_16.setGeometry(QtCore.QRect(180, 100, 61, 31))
        self.label_16.setObjectName("label_16")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 100, 61, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.label_netconnect_true = 0
        self.label_serial0connect_true = 0
        self.label_serial1connect_true = 0
        self.label_serial2connect_true = 0
        self.sweepFreqstop_true = 0
        self.timer_flag = False
        
        self.retranslateUi(MainWindow)
        self.pushButton_netconnect.clicked.connect(self.netconnect)
        self.pushButton_serial0connect.clicked.connect(self.serial0connect)
        self.pushButton_serial1connect.clicked.connect(self.serial1connect)
        self.pushButton_serial2connect.clicked.connect(self.serial2connect)
        self.pushButton_sweepFreq.clicked.connect(self.sweepFreqShow)
        self.pushButton_pause.clicked.connect(self.sweepFreqPause)
        self.pushButton_stop.clicked.connect(self.sweepFreqStop)
        self.pushButton_programmer.clicked.connect(self.programmer)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    def programmer(self):
        freq = 1000
        self.programStep = 0
        self.programTimer = QTimer()
        self.programTimer.timeout.connect(self.programOperate) #计时结束调用operate()方法
        self.programTimer.start(freq)
        self.programTimer_flag = True
    
    def programOperate(self):
        self.progressBar.setValue(self.programStep)
        self.programStep += 1
    
    def sweepFreqStop(self):
        if self.timer_flag == True:
            self.timer.stop()
            self.lcdNumber.display(0)
            self.progressBar_2.setValue(0)
    
    def sweepFreqPause(self):
        if self.sweepFreqstop_true:
            self.sweepFreqstop_true = 0
            self.timer.start()
        else:
            self.sweepFreqstop_true = 1
            self.timer.stop()
    
    def sweepFreqShow(self):
        freq = 10
        self.step = 0
        self.qfreq = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.operate) #计时结束调用operate()方法
        self.timer.start(freq)
        self.timer_flag = True
    
    def operate(self):
        if self.qfreq < 4096:
            self.qfreq += 1
            if self.qfreq/40 <= 100:
                self.step = self.qfreq / 40
            else:
                self.step = 100
            self.lcdNumber.display(self.qfreq)
            self.progressBar_2.setValue(self.step)
        else:
            self.lcdNumber.display(4096)
            
    def netconnect(self):
        if self.label_netconnect_true:
            self.label_netconnect_true = 0
            self.label_netconnect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        else:
            self.label_netconnect_true = 1
            self.label_netconnect.setPixmap(QtGui.QPixmap("res/image_green.png"))

    def serial0connect(self):
        if self.label_serial0connect_true:
            self.label_serial0connect_true = 0
            self.label_serial0connect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        else:
            self.label_serial0connect_true = 1
            self.label_serial0connect.setPixmap(QtGui.QPixmap("res/image_green.png"))
    
    def serial1connect(self):
        if self.label_serial1connect_true:
            self.label_serial1connect_true = 0
            self.label_serial1connect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        else:
            self.label_serial1connect_true = 1
            self.label_serial1connect.setPixmap(QtGui.QPixmap("res/image_green.png"))

    def serial2connect(self):
        if self.label_serial2connect_true:
            self.label_serial2connect_true = 0
            self.label_serial2connect.setPixmap(QtGui.QPixmap("res/image_gray.png"))
        else:
            self.label_serial2connect_true = 1
            self.label_serial2connect.setPixmap(QtGui.QPixmap("res/image_green.png"))
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "跳频调试基础测试软件"))
        self.pushButton_sweepFreq.setText(_translate("MainWindow", "扫频"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">全频扫描</span></p></body></html>"))
        self.pushButton_pause.setText(_translate("MainWindow", "暂停"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">频点固化</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">跳频调制</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">频谱仪IP地址:</span></p></body></html>"))
        self.pushButton_stop.setText(_translate("MainWindow", "停止"))
        self.pushButton_netconnect.setText(_translate("MainWindow", "网络连接"))
        self.lineEdit.setText(_translate("MainWindow", "192.168.10.100"))
        self.pushButton_serial0connect.setText(_translate("MainWindow", "串口连接"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">扫频信息:</span></p></body></html>"))
        self.pushButton_serial1connect.setText(_translate("MainWindow", "串口连接"))
        self.pushButton_programmer.setText(_translate("MainWindow", "固化"))
        self.pushButton_9.setText(_translate("MainWindow", "导入"))
        self.pushButton_serial2connect.setText(_translate("MainWindow", "串口连接"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">频点信息:</span></p></body></html>"))
        self.pushButton_11.setText(_translate("MainWindow", "<"))
        self.pushButton_12.setText(_translate("MainWindow", ">"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">步进设置:</span></p></body></html>"))
        self.pushButton_13.setText(_translate("MainWindow", "开始"))
        self.toolButton.setText(_translate("MainWindow", "导出"))
        self.label_12.setText(_translate("MainWindow", "Mhz"))
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">中心频点:</span></p></body></html>"))
        self.label_14.setText(_translate("MainWindow", "Mhz"))
        self.label_15.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">串口设置:</span><span style=\" font-size:10pt;\">COM</span></p></body></html>"))
        self.label_16.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">波特率</span></p></body></html>"))

#import res_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

