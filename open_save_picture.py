# -*- coding: utf-8 -*-
# corresponding to first.py for motion deblur
from PyQt5 import QtWidgets, QtGui
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from save_picture import Ui_Save_Picture_Form
import threading
from show_tensordboardX_Resnet import NetWindow
import scipy.misc
import numpy as np
import MySQLdb

class open_save_picture(QtWidgets.QWidget, Ui_Save_Picture_Form): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_save_picture, self).__init__(parent)
        self.setupUi(self) # import Ui_Form
        self.pic_256_256 = ""
        self.pic_320_180 = ""

        # 定义槽函数
    def openimage1(self):
    # 打开文件路径
    #设置文件扩展名过滤,注意用双分号间隔
        self.pic_256_256,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.jpg;;*.png;;*.jpeg;;*.bmp;;All Files (*)")

        print(self.pic_256_256)
        #利用qlabel显示图片
        png = QtGui.QPixmap(self.pic_256_256).scaled(self.label_1.width(), self.label_1.height())
        self.label_1.setPixmap(png)

    def openimage2(self):
    # 打开文件路径
    #设置文件扩展名过滤,注意用双分号间隔
        self.pic_320_180,imgType= QFileDialog.getOpenFileName(self,
                                    "打开图片",
                                    "",
                                    " *.png;;*.jpg;;*.jpeg;;*.bmp;;All Files (*)")

        print(self.pic_320_180)
        #利用qlabel显示图片
        png = QtGui.QPixmap(self.pic_320_180).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(png)

    def clear(self):
        self.pic_256_256 = ""
        self.pic_320_180 = ""
        png1=QtGui.QPixmap(self.pic_256_256).scaled(self.label_1.width(), self.label_1.height())
        self.label_1.setPixmap(png1)
        png2=QtGui.QPixmap(self.pic_320_180).scaled(self.label_2.width(), self.label_2.height())
        self.label_2.setPixmap(png2)

    def save256_256_to_database(self):
        pic_256_256_url = self.pic_256_256 # 256*256结果图片的路径
        end = "k"
        pic_256_256_name = pic_256_256_url [pic_256_256_url.rfind(end):] # 这里只能保存motion_blur

        # 创建数据库连接对象
        db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
        # 创建数据库连接
        cursor=db.cursor()

        # SQL语句操作dataset表进行插入
        query_save='insert into dataset(picname, picurl) values(%s, %s)'
        pname = pic_256_256_name
        purl = pic_256_256_url
        values = (pname, purl)
        try:
            # 执行sql语句
            cursor.execute(query_save, values)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.Yes)
            print(reply)
        # 关闭数据库连接
        cursor.close()
        db.close()

        # 显示成功写入数据库的信息框
        reply=QMessageBox.information(self, "系统消息提示", "图片保存成功！", QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        print(reply)


    def save320_180_to_database(self):
        pic_320_180_url = self.pic_320_180  # 320*180结果图片的路径
        end="k"
        pic_320_180_name = pic_320_180_url [pic_320_180_url.rfind(end):]  # 这里只能保存gopro_large
        # 创建数据库连接对象
        db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
        # 创建数据库连接
        cursor=db.cursor()

        # SQL语句操作dataset表进行插入
        query_save='insert into dataset(picname, picurl) values(%s, %s)'
        pname = pic_320_180_name
        purl = pic_320_180_url
        values=(pname, purl)
        try:
            # 执行sql语句
            cursor.execute(query_save, values)
            # 提交到数据库执行
            db.commit()
        except:
            # 发生错误时回滚
            db.rollback()
            reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.Yes)
            print(reply)
        # 关闭数据库连接
        cursor.close()
        db.close()

        # 显示成功写入数据库的信息框
        reply=QMessageBox.information(self, "系统消息提示", "图片保存成功！", QMessageBox.Yes | QMessageBox.No,
                                      QMessageBox.Yes)
        print(reply)




