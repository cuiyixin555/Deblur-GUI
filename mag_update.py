# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class Ui_Mag_Update(object):
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
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/mag_update.png")))

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
        self.oldPassword = QLineEdit()
        self.newPassword = QLineEdit()

        self.pUserName.setPlaceholderText("输入管理员账户名")
        self.oldPassword.setPlaceholderText("输入旧密码")
        self.newPassword.setPlaceholderText("确认新密码")

        # 设置演示效果
        self.pUserName.setEchoMode(QLineEdit.Normal)
        self.oldPassword.setEchoMode(QLineEdit.Password)
        self.newPassword.setEchoMode(QLineEdit.Password)
        self.pUserName.setFixedSize(445, 35)
        self.oldPassword.setFixedSize(445, 35)
        self.newPassword.setFixedSize(445, 35)

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
        self.formlayout.addWidget(self.oldPassword)
        self.formlayout.addWidget(self.newPassword)
        self.formlayout.addWidget(self.pushButton)

        self.fwg = QWidget()
        self.fwg.setLayout(self.formlayout)
        self.wlayout.addWidget(self.fwg)
        self.setLayout(self.wlayout)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.mag_update_password)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员改密窗口"))
        self.pushButton.setText(_translate("Form", "MANAGER更改密码"))

