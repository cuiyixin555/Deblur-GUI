# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui

class Ui_Super_Welcome(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 762)
        # setup welcome.png
        self.label=QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(23, 10, 585, 368))
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/super_system.png")))

        # setup pushButton for choose variety of datasets
        self.qLineEdit = QtWidgets.QLineEdit(Form) # 输入要删除的用户名
        self.qLineEdit_1 = QtWidgets.QLineEdit(Form) # 输入要删除的管理员账户
        self.pushButton = QtWidgets.QPushButton(Form) # 重置用户信息
        self.pushButton_1 = QtWidgets.QPushButton(Form) # 管理员注册
        self.pushButton_2 = QtWidgets.QPushButton(Form) # 管理员改密
        self.pushButton_3 = QtWidgets.QPushButton(Form) # 数据集存储
        self.pushButton_4 = QtWidgets.QPushButton(Form) # 重置管理员信息
        self.pushButton_5 = QtWidgets.QPushButton(Form) # 查询用户表
        self.pushButton_6 = QtWidgets.QPushButton(Form) # 查询管理员表

        self.qLineEdit.setGeometry(QtCore.QRect(23, 400, 280, 41))
        self.qLineEdit_1.setGeometry(QtCore.QRect(23, 451, 280, 41))
        self.pushButton.setGeometry(QtCore.QRect(323, 400, 283, 41))
        self.pushButton_4.setGeometry(QtCore.QRect(323, 451, 283, 41)) # 重置管理员信息
        self.pushButton_1.setGeometry(QtCore.QRect(23, 502, 585, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(23, 553, 585, 41))
        self.pushButton_3.setGeometry(QtCore.QRect(23, 604, 585, 41))
        self.pushButton_5.setGeometry(QtCore.QRect(23, 655, 585, 41))
        self.pushButton_6.setGeometry(QtCore.QRect(23, 706, 585, 41))

        self.qLineEdit.setObjectName("qLineEdit") # 输入要删除的用户名
        self.qLineEdit.setPlaceholderText("请输入要删除的用户账户")
        self.qLineEdit_1.setObjectName("qLineEdit")  # 输入要删除的用户名
        self.qLineEdit_1.setPlaceholderText("请输入要删除的管理员账户")

        self.pushButton.setObjectName("pushButton") # 重置用户信息
        self.pushButton_1.setObjectName("pushButton_1") # 管理员注册
        self.pushButton_2.setObjectName("pushButton_2") # 管理员改密
        self.pushButton_3.setObjectName("pushButton_3") # 数据集存储
        self.pushButton_4.setObjectName("pushButton_4") # 重置管理员信息
        self.pushButton_5.setObjectName("pushButton_5") # 查询用户表
        self.pushButton_6.setObjectName("pushButton_6") # 查询管理员表

        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.drop_user_item) # 重置用户信息
        self.pushButton_1.clicked.connect(Form.mag_register) # 管理员注册
        self.pushButton_2.clicked.connect(Form.mag_update_password) # 管理员改密
        self.pushButton_3.clicked.connect(Form.save_picture) # 数据集存储
        self.pushButton_4.clicked.connect(Form.drop_manager_item) # 重置管理员信息
        self.pushButton_5.clicked.connect(Form.query_user_table) # 查询用户表
        self.pushButton_6.clicked.connect(Form.query_manager_table) # 查询管理员表

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员后台系统"))
        self.pushButton.setText(_translate("Form", "重置用户信息"))
        self.pushButton_1.setText(_translate("Form", "管理员注册"))
        self.pushButton_2.setText(_translate("Form", "管理员改密"))
        self.pushButton_3.setText(_translate("Form", "数据集存储"))
        self.pushButton_4.setText(_translate("Form", "重置管理员信息"))
        self.pushButton_5.setText(_translate("Form", "查询用户表"))
        self.pushButton_6.setText(_translate("Form", "查询管理员表"))


