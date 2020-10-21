# Save Picture for manager function
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Save_Picture_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(625, 623)
        # 先设置图片的位置
        self.label = QtWidgets.QLabel(Form) # 呈现save_pic_title.png
        self.label_1 = QtWidgets.QLabel(Form) # 呈现256*256尺寸的去模糊图片
        self.label_2 = QtWidgets.QLabel(Form) # 呈现320*180尺寸的去模糊图片

        self.label.setGeometry(QtCore.QRect(20, 10, 585, 286))
        self.label_1.setGeometry(QtCore.QRect(20, 306, 256, 256))
        self.label_2.setGeometry(QtCore.QRect(286, 306, 320, 180))

        self.label.setStyleSheet("QLabel{\n"
                                 "    border-color: rgb(0, 204,255);\n"
                                 "     border-width: 10px;\n"
                                 "     border-style: solid;\n"
                                 "}")
        self.label.setPixmap((QtGui.QPixmap("./asserts/image/save_pic_title.png")))

        self.label_1.setStyleSheet("QLabel{\n"
                                   "    border-color: rgb(255, 170,0);\n"
                                   "     border-width: 10px;\n"
                                   "     border-style: solid;\n"
                                   "}")
        self.label_2.setStyleSheet("QLabel{\n"
                                   "    border-color: rgb(255, 170,0);\n"
                                   "     border-width: 10px;\n"
                                   "     border-style: solid;\n"
                                   "}")

        self.label.setText("") # banner picture
        self.label_1.setText("") # 256*256 picture
        self.label_2.setText("") # 320*180 picture

        self.label.setObjectName("label") # banner picture
        self.label_1.setObjectName("label_1") # 256*256 picture
        self.label_2.setObjectName("label_2") # 320*180 picture

        self.pushButton = QtWidgets.QPushButton(Form) # 选择256*256尺寸的去模糊图片
        self.pushButton_1 = QtWidgets.QPushButton(Form) # 选择320*180尺寸的去模糊图片
        self.pushButton_2 = QtWidgets.QPushButton(Form) # 清空图片
        self.pushButton_3 = QtWidgets.QPushButton(Form) # 保存图片256*256
        self.pushButton_4 = QtWidgets.QPushButton(Form) # 保存图片320*180

        # 在绝对布局中，将pushButton,pushButton_1,pushButton_2设置在一行之中
        # 将pushButton_3,pushButton_4,设置在下一行之中
        self.pushButton.setGeometry(QtCore.QRect(286, 496, 320, 30)) # 选择256*256图片
        self.pushButton_1.setGeometry(QtCore.QRect(286, 531, 320, 30)) # 选择320*180图片

        self.pushButton_2.setGeometry(QtCore.QRect(20, 577, 182, 35)) # 清空图片
        self.pushButton_3.setGeometry(QtCore.QRect(220, 577, 182, 35)) # 保存图片256*256
        self.pushButton_4.setGeometry(QtCore.QRect(420, 577, 182, 35)) # 保存图片320*180

        self.pushButton.setObjectName("pushButton") # 选择256*256
        self.pushButton_1.setObjectName("pushButton_1") # 选择320*180
        self.pushButton_2.setObjectName("pushButton_2") # 清空图片

        self.pushButton_3.setObjectName("pushButton_3") # 保存256*256
        self.pushButton_4.setObjectName("pushButton_4") # 保存320*180

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.openimage1) # 打开256*256尺寸的图片
        self.pushButton_1.clicked.connect(Form.openimage2) # 打开320*180尺寸的图片
        self.pushButton_2.clicked.connect(Form.clear)

        self.pushButton_3.clicked.connect(Form.save256_256_to_database) # 保存256*256
        self.pushButton_4.clicked.connect(Form.save320_180_to_database) # 保存320*180
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "图片结果保存窗口"))
        self.pushButton.setText(_translate("Form", "MOTION/LEVIN"))
        self.pushButton_1.setText(_translate("Form", "GOPRO_LARGE"))
        self.pushButton_2.setText(_translate("Form", "清空"))
        self.pushButton_3.setText(_translate("Form", "256*256图片保存"))
        self.pushButton_4.setText(_translate("Form", "320*180图片保存"))

