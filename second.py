# GOPRO_Large Deblur Process

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1030, 414)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_4 = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(15, 200, 110, 41))
        self.pushButton_1.setGeometry(QtCore.QRect(235, 200, 110, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(455, 200, 110, 41))
        self.pushButton_3.setGeometry(QtCore.QRect(675, 200, 110, 41))
        self.pushButton_4.setGeometry(QtCore.QRect(902, 200, 110, 41))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label = QtWidgets.QLabel(Form)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_3 = QtWidgets.QLabel(Form)

        self.label.setGeometry(QtCore.QRect(15, 10, 320, 180))
        self.label_2.setGeometry(QtCore.QRect(355, 10, 320, 180))
        self.label_3.setGeometry(QtCore.QRect(695, 10, 320, 180))

        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(255, 170,0);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label_2.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(255, 170,0);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label_3.setStyleSheet("QLabel{\n"
                                   "    border-color: rgb(255, 170,0);\n"
                                   "     border-width: 10px;\n"
                                   "     border-style: solid;\n"
                                   "}")
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText("")
        self.label.setObjectName("label")
        self.label_2.setObjectName("label_2")
        self.label_3.setObjectName("label_3")

        self.QLineEdit_1 = QtWidgets.QLineEdit(Form)
        self.QLineEdit_1.setPlaceholderText("PSNR/SSIM: ")
        self.QLineEdit_1.setObjectName("QLineEdit_1")

        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.QLineEdit_1.setGeometry(QtCore.QRect(15, 251, 1000, 41))
        self.pushButton_5.setGeometry(QtCore.QRect(15, 302, 1000, 41))
        self.pushButton_6.setGeometry(QtCore.QRect(15, 353, 1000, 41))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6.setObjectName("pushButton_6")
        self.retranslateUi(Form)

        self.pushButton.clicked.connect(Form.openimage1)
        self.pushButton_2.clicked.connect(Form.openimage2)
        self.pushButton_3.clicked.connect(Form.openimage3)
        self.pushButton_5.clicked.connect(Form.calculate)
        self.pushButton_6.clicked.connect(Form.showNetwork)

        # 这里是去模糊的核心调用
        self.pushButton_1.clicked.connect(Form.slotStart)
        # 这里是清空QLabel的图片调用
        self.pushButton_4.clicked.connect(Form.clear)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像去模糊系统"))
        self.pushButton.setText(_translate("Form", "模糊图"))
        self.pushButton_1.setText(_translate("Form", "去模糊"))
        self.pushButton_2.setText(_translate("Form", "清晰图"))
        self.pushButton_3.setText(_translate("Form", "真值图"))
        self.pushButton_4.setText(_translate("Form", "清空"))
        self.pushButton_5.setText(_translate("Form", "PSNR/SSIM计算"))
        self.pushButton_6.setText(_translate("Form", "显示网络结构"))


