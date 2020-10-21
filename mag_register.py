# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class Ui_Mag_Register(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 295)

        # 全局布局：水平
        self.wlayout=QHBoxLayout(Form)

        # 局部布局：垂直，表单
        self.vlayout=QVBoxLayout()
        self.formlayout=QFormLayout()

        # left: setup login.png
        self.label=QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/mag_register.png")))

        # 为左边布局添加控件
        self.vlayout.addWidget(self.label)
        self.vwg = QWidget()
        self.vwg.setLayout(self.vlayout)
        self.wlayout.addWidget(self.vwg)

        # right: setup input text
        self.label_1=QtWidgets.QLabel()
        self.label_1.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label_1.setPixmap((QtGui.QPixmap("./asserts/image/title.png")))

        self.pUserName = QLineEdit()
        self.pPassword = QLineEdit()
        self.queren = QLineEdit()

        self.pUserName.setPlaceholderText("输入管理员账户")
        self.pPassword.setPlaceholderText("输入密码")
        self.queren.setPlaceholderText("确认密码")

        # 设置演示效果
        self.pUserName.setEchoMode(QLineEdit.Normal)
        self.pPassword.setEchoMode(QLineEdit.Password)
        self.queren.setEchoMode(QLineEdit.Password)
        self.pUserName.setFixedSize(445, 35)
        self.pPassword.setFixedSize(445, 35)
        self.queren.setFixedSize(445, 35)

        # setup pushButton for choose variety of datasets
        self.pushButton = QPushButton(Form)

        self.pushButton.setObjectName("pushButton")
        self.pushButton.setFixedSize(445, 35)

        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1.setText("")
        self.label.setObjectName("label_1")

        self.formlayout.addWidget(self.label_1)
        self.formlayout.addWidget(self.pUserName)
        self.formlayout.addWidget(self.pPassword)
        self.formlayout.addWidget(self.queren)
        self.formlayout.addWidget(self.pushButton)
        self.fwg = QWidget()
        self.fwg.setLayout(self.formlayout)
        self.wlayout.addWidget(self.fwg)
        self.setLayout(self.wlayout)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.write_database)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员注册窗口"))
        self.pushButton.setText(_translate("Form", "REGISTER注册"))

