# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from welcome import Ui_Form   # 导入生成first.py里生成的类
from first import Ui_Form_1
from second import Ui_Form_2
from open_1 import open_1
from open_2 import open_2
from open_3 import open_3

class open_welcome(QtWidgets.QWidget, Ui_Form, Ui_Form_1, Ui_Form_2): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_welcome, self).__init__(parent)
        self.setupUi(self) # import Ui_Form

        # 实例化子窗体
        self.open1 = open_1()
        self.open2 = open_2()
        self.open3 = open_3()

    # signal channel for connection
    def open_motion_blur(self):
        self.open1.show()


    def open_gopro_blur(self):
        self.open2.show()

    def open_Levin(self):
        self.open3.show()

# app = QtWidgets.QApplication(sys.argv)
# window = open_welcome()
# window.show()
# app.exec_()
