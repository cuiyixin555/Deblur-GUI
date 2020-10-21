# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form_1(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(860, 495)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_4 = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(15, 285, 100, 41))
        self.pushButton_1.setGeometry(QtCore.QRect(195, 285, 100, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(375, 285, 100, 41))
        self.pushButton_3.setGeometry(QtCore.QRect(555, 285, 100, 41))
        self.pushButton_4.setGeometry(QtCore.QRect(735, 285, 100, 41))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4.setObjectName("pushButton_4")

        self.label = QtWidgets.QLabel(Form)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(15, 10, 256, 256))
        self.label_2.setGeometry(QtCore.QRect(296, 10, 256, 256))
        self.label_3.setGeometry(QtCore.QRect(577, 10, 256, 256))
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

        # 设置PSNR和SSIM的指标显示
        self.QLineEdit_0 = QtWidgets.QLineEdit(Form)
        self.QLineEdit_0.setPlaceholderText("PSNR/SSIM: ")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_6 = QtWidgets.QPushButton(Form)

        self.QLineEdit_0.setObjectName("QLineEdit_0")
        self.pushButton_5.setObjectName("pushButton_4")
        self.pushButton_6.setObjectName("pushButton_5")

        self.QLineEdit_0.setGeometry(QtCore.QRect(15, 336, 822, 41))
        self.pushButton_5.setGeometry(QtCore.QRect(15, 387, 822, 41))
        self.pushButton_6.setGeometry(QtCore.QRect(15, 438, 822, 41))

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.openimage1)
        self.pushButton_2.clicked.connect(Form.openimage2)
        # 这里是去模糊的核心调用
        self.pushButton_1.clicked.connect(Form.slotStart)
        # 这里是清空QLabel的图片调用
        self.pushButton_3.clicked.connect(Form.openimage3)
        self.pushButton_4.clicked.connect(Form.clear)
        self.pushButton_5.clicked.connect(Form.calculate)
        self.pushButton_6.clicked.connect(Form.showNetwork)

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

