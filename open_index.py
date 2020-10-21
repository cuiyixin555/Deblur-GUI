# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from welcome import Ui_Form   # 导入生成first.py里生成的类
from index import Ui_Index_Form
from open_login import open_login
from open_mag_login import open_mag_login

class open_index(QtWidgets.QWidget, Ui_Index_Form): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_index, self).__init__(parent)
        self.setupUi(self) # import Ui_Form

        # 实例化子窗体
        self.open_login = open_login()
        self.open_mag_login = open_mag_login()

    # signal channel for connection
    def open_userlogin_page(self):
        self.open_login.show()

    def open_admin_page(self):
        self.open_mag_login.show()

app = QtWidgets.QApplication(sys.argv)
window = open_index()
window.show()
app.exec_()
