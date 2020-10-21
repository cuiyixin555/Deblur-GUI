# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui

class Ui_Mag_Welcome(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 553)
        # setup welcome.png
        self.label=QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(23, 10, 585, 368))
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/mag_system.png")))

        # setup pushButton for choose variety of datasets
        self.qLineEdit = QtWidgets.QLineEdit(Form) # 输入要删除的用户名
        self.pushButton = QtWidgets.QPushButton(Form) # 重置用户信息
        self.pushButton_1 = QtWidgets.QPushButton(Form) # 管理员改密
        self.pushButton_2 = QtWidgets.QPushButton(Form) # 数据集存储

        self.qLineEdit.setGeometry(QtCore.QRect(23, 400, 280, 41))
        self.pushButton.setGeometry(QtCore.QRect(323, 400, 283, 41))
        self.pushButton_1.setGeometry(QtCore.QRect(23, 451, 585, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(23, 502, 585, 41))

        self.qLineEdit.setObjectName("qLineEdit") # 输入要删除的用户名
        self.qLineEdit.setPlaceholderText("请输入要删除的用户名")

        self.pushButton.setObjectName("pushButton") # 重置用户信息
        self.pushButton_1.setObjectName("pushButton_1") # 管理员改密
        self.pushButton_2.setObjectName("pushButton_2") # 数据集存储

        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.drop_user_item) # 重置用户信息
        self.pushButton_1.clicked.connect(Form.mag_update_password) # 管理员改密
        self.pushButton_2.clicked.connect(Form.save_picture) # 数据集存储

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员后台系统"))
        self.pushButton.setText(_translate("Form", "重置用户信息"))
        self.pushButton_1.setText(_translate("Form", "管理员改密"))
        self.pushButton_2.setText(_translate("Form", "数据集存储"))

