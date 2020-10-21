# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui

class Ui_Index_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(630, 503)
        # setup welcome.png
        self.label=QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(23, 10, 585, 368))
        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204, 255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/welcome_login.png")))

        # setup pushButton for choose variety of datasets
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton_1 = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(23, 393, 585, 41))
        self.pushButton_1.setGeometry(QtCore.QRect(23, 444, 585, 41))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_1.setObjectName("pushButton_1")

        self.label.setText("")
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.open_userlogin_page)
        self.pushButton_1.clicked.connect(Form.open_admin_page)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像去模糊系统"))
        self.pushButton.setText(_translate("Form", "USER用户登陆"))
        self.pushButton_1.setText(_translate("Form", "SYSTEM ADMIN系统管理员登陆"))

