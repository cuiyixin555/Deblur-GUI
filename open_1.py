# -*- coding: utf-8 -*-
# corresponding to first.py for motion deblur
from PyQt5 import QtWidgets, QtGui
import sys
from first import Ui_Form_1   # 导入生成first.py里生成的类
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from manage_1 import manage
import threading
from show_tensordboardX_Resnet import NetWindow
import scipy.misc
import numpy as np

def PSNRLossnp(y_true, y_pred):
    return 10 * np.log(255 * 2 / (np.mean(np.square(y_pred - y_true))))

def SSIMnp(y_true, y_pred):
    u_true=np.mean(y_true)
    u_pred=np.mean(y_pred)
    var_true=np.var(y_true)
    var_pred=np.var(y_pred)
    std_true=np.sqrt(var_true)
    std_pred=np.sqrt(var_pred)
    c1=np.square(0.01 * 7)
    c2=np.square(0.03 * 7)
    ssim=(2 * u_true * u_pred + c1) * (2 * std_pred * std_true + c2)
    denom=(u_true ** 2 + u_pred ** 2 + c1) * (var_pred + var_true + c2)
    return ssim / denom


class open_1(QtWidgets.QWidget, Ui_Form_1): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_1, self).__init__(parent)
        self.setupUi(self) # import Ui_Form
        self.blurryImage = ""
        self.sharpImage = "E:/PyQt5/Openimg/res/" # res path
        self.gtImage = "E:/PyQt5/Openimg/DataSet/motion_blur/groundtruth/" # gt path
        self.imgName = ""
        #self.results = "E:/PyQt5/Openimg/res" # res path
        self.psnr_str = ""
        self.ssim_str = ""
        self.netwindow = NetWindow()

        # 定义槽函数
    def openimage1(self):
    # 打开文件路径
    #设置文件扩展名过滤,注意用双分号间隔
        self.blurryImage,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(self.blurryImage)
        #利用qlabel显示图片
        png = QtGui.QPixmap(self.blurryImage).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png)

    def openimage2(self):
    # 打开文件路径
    #设置文件扩展名过滤,注意用双分号间隔
        # self.sharpImage,imgType= QFileDialog.getOpenFileName(self,
        #                             "打开图片",
        #                             "",
        #                             " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        #
        # print(self.sharpImage)

        # copy the results path to show
        end="k"
        imgName=self.blurryImage [self.blurryImage.rfind(end):]
        self.sharpImage = self.sharpImage + str(imgName)
        # print("aaa "+self.sharpImage)

        # show the result picture to label_2
        png = QtGui.QPixmap(self.sharpImage).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(png)
        # #利用qlabel显示图片
        # png = QtGui.QPixmap(self.sharpImage).scaled(self.label_2.width(), self.label_2.height())
        # self.label_2.setPixmap(png)

    def openimage3(self):
    # 打开文件路径
    #设置文件扩展名过滤,注意用双分号间隔
        # self.gtImage,imgType= QFileDialog.getOpenFileName(self,
        #                             "打开图片",
        #                             "",
        #                             " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")
        #
        # print(self.gtImage)
        #利用qlabel显示图片
        end="k"
        imgName=self.blurryImage [self.blurryImage.rfind(end):]
        self.gtImage=self.gtImage + str(imgName)
        png = QtGui.QPixmap(self.gtImage).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(png)

    def clear(self):
        self.blurryImage = ""
        self.sharpImage = ""
        self.gtImage = ""
        png1=QtGui.QPixmap(self.blurryImage).scaled(self.label.width(), self.label.height())
        self.label.setPixmap(png1)
        png2=QtGui.QPixmap(self.sharpImage).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(png2)
        png3=QtGui.QPixmap(self.gtImage).scaled(self.label_3.width(), self.label_3.height())
        self.label_3.setPixmap(png3)


    def slotStart(self):
        t = threading.Thread(target = manage, args = (self.blurryImage,))
        t.start()

    def calculate(self):
        # print(self.blurryImage)
        print(self.sharpImage)
        print(self.gtImage)
        sharp = scipy.misc.imread(self.sharpImage)
        gt = scipy.misc.imread(self.gtImage)

        self.psnr_str = str(round(PSNRLossnp(gt, sharp), 4))
        self.ssim_str = str(round(SSIMnp(gt, sharp), 4))

        # TODO:
        print(self.psnr_str)
        print(self.ssim_str)
        cal_res = self.psnr_str + '/' + self.ssim_str
        self.QLineEdit_0.setText(cal_res)

    def showNetwork(self):
        self.netwindow.show()


# def open_1():
#     app = QtWidgets.QApplication(sys.argv)
#     window = mywindow()
#     window.show()
#     sys.exit(app.exec_())
