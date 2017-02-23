#!/bin/env python3
# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__=='__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    
    w = QtWidgets.QWidget()
    w.resize(250, 150)
    w.move(100, 300)
    w.setWindowTitle('Simple')
    w.show()
    
    sys.exit(app.exec_())



def setlabel_8(self):
        self.label_8.setPixmap(QtGui.QPixmap("res/image_green.png"))
