# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class Ui_Mag_Login(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(765, 295)

        # 全局布局：水平
        self.wlayout=QHBoxLayout(Form)

        # 局部布局：垂直，表单, 水平
        self.vlayout = QVBoxLayout()
        self.formlayout = QFormLayout()
        self.standardlayout = QHBoxLayout()

        # left: setup login.png
        self.label=QtWidgets.QLabel()
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/mag_login.png")))

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

        self.pUserName=QLineEdit()
        self.pPassword=QLineEdit()

        self.pUserName.setPlaceholderText("管理员账户名")
        self.pPassword.setPlaceholderText("管理员账户密码")

        # 设置演示效果
        self.pUserName.setEchoMode(QLineEdit.Normal)
        self.pPassword.setEchoMode(QLineEdit.Password)
        self.pUserName.setFixedSize(445, 31)
        self.pPassword.setFixedSize(445, 31)

        # setup pushButton for choose variety of datasets
        self.pushButton = QPushButton(Form) # 普管登录
        self.pushButton_1 = QPushButton(Form) # 超管登录
        self.pushButton_2 = QPushButton(Form) # 管路员改密

        self.pushButton.setObjectName("pushButton") # 普管登录
        self.pushButton_1.setObjectName("pushButton_1") # 超管登录
        self.pushButton_2.setObjectName("pushButton_2") # 管理员改密


        self.pushButton_2.setFixedSize(445, 31)

        self.label.setText("")
        self.label.setObjectName("label")
        self.label_1.setText("")
        self.label.setObjectName("label_1")

        # 这里是formlayout的布局
        self.formlayout.addWidget(self.label_1)
        self.formlayout.addWidget(self.pUserName) # QLineEdit
        self.formlayout.addWidget(self.pPassword) # QLineEdit
        self.formlayout.addWidget(self.pushButton_2)

        # 添加子水平布局
        self.pushButton.setFixedSize(200, 31) # 普管登录
        self.pushButton_1.setFixedSize(200, 31) # 超管登录

        self.standardlayout.addWidget(self.pushButton)
        self.standardlayout.addWidget(self.pushButton_1)

        self.alayout = QWidget()
        self.alayout.setLayout(self.standardlayout)
        self.formlayout.addWidget(self.alayout)

        self.fwg = QWidget()
        self.fwg.setLayout(self.formlayout)
        self.wlayout.addWidget(self.fwg)
        self.setLayout(self.wlayout)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.open_mag_welcome_page) # 普管登录
        self.pushButton_1.clicked.connect(Form.open_super_welcome_page) # 超管登录
        self.pushButton_2.clicked.connect(Form.open_update_password_page) # 管理员改密

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员登录窗口"))
        self.pushButton.setText(_translate("Form", "SYSTEM ADMIN登录"))
        self.pushButton_1.setText(_translate("Form", "SUPER ADMIN登录"))
        self.pushButton_2.setText(_translate("Form", "管理员改密"))


