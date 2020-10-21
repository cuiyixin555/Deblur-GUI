# Welcome Page to choose variety of DataSets

# Motion_Blur Dataset for Deblur Processing

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui

class Ui_Form(object):
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
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/welcome.png")))

        # setup pushButton for choose variety of datasets
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_2 = QtWidgets.QPushButton(Form)

        self.pushButton.setGeometry(QtCore.QRect(23, 400, 585, 41))
        self.pushButton_1.setGeometry(QtCore.QRect(23, 451, 585, 41))
        self.pushButton_2.setGeometry(QtCore.QRect(23, 502, 585, 41))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label.setText("")
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.open_motion_blur)
        self.pushButton_1.clicked.connect(Form.open_gopro_blur)
        self.pushButton_2.clicked.connect(Form.open_Levin)

        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图像去模糊系统"))
        self.pushButton.setText(_translate("Form", "MOTION_BLUR数据集"))
        self.pushButton_1.setText(_translate("Form", "GOPRO_BLUR数据集"))
        self.pushButton_2.setText(_translate("Form", "LEVIN数据集"))

