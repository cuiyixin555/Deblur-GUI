# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mag_login import Ui_Mag_Login
from open_mag_update import open_mag_update
from open_mag_welcome import open_mag_welcome
from open_super_welcome import open_super_welcome
# MySql模块
import MySQLdb
import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton


class open_mag_login(QtWidgets.QWidget, Ui_Mag_Login): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_mag_login, self).__init__(parent)
        self.setupUi(self) # import Ui_Login

        # 实例化子窗体
        self.open_mag_update = open_mag_update()
        self.open_mag_welcome = open_mag_welcome()
        self.open_super_welcome = open_super_welcome()

    # signal channel for connection
    def open_mag_welcome_page(self):
        # 判别管理员身份
        mname=self.pUserName.text().strip()
        pwd=self.pPassword.text().strip()
        # 对密码进行密文存储
        md5=hashlib.md5()
        md5.update(pwd.encode('utf-8'))

        # 判断是否是‘CuiYixin'
        # 打开数据库连接
        db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
        # 使用cursor()方法获取操作游标
        cursor=db.cursor()
        sql="select * from manager where magname = '%s' and password = '%s'" % (mname, md5.hexdigest())
        # 将根据超级管理员的账户名，对manager表进行查询
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results=cursor.fetchall()
            flag=0  # 默认该用户名在manager表里的不为空
            # 判断对数据库读取的内容是否为空
            if (not results):
                flag=1  # 表示manager表里没有该管理员账户

            if (flag == 0):
                self.open_mag_welcome.show()
            else:
                reply=QMessageBox.critical(self, "系统报错提示", "没有您账户，请联系超管！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                print(reply)
        except:
            # 发生错误时回滚
            db.rollback()
            reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.Yes)
            print(reply)


    def open_super_welcome_page(self):
        # 由于超级管理员只有一个，所以对于超级管理员的登录，必须要对其用户名进行判断
        mname = self.pUserName.text().strip()
        pwd = self.pPassword.text().strip()
        # 对密码进行密文存储
        md5=hashlib.md5()
        md5.update(pwd.encode('utf-8'))

        # 判断是否是‘CuiYixin'
        if(mname == 'CuiYixin'):
            # 打开数据库连接
            db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
            # 使用cursor()方法获取操作游标
            cursor=db.cursor()
            sql="select * from manager where magname = '%s' and password = '%s'" % (mname, md5.hexdigest())
            # 将根据超级管理员的账户名，对manager表进行查询
            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                results=cursor.fetchall()
                flag=0 # 默认manager里是存有超级管理员的记录的
                # 判断对数据库读取的内容是否为空
                if (not results):
                    flag=1  # 表示manager没有CuiYixin的记录，可能是密码输入错误

                if(flag == 0):
                    self.open_super_welcome.show()
                else:
                    reply=QMessageBox.critical(self, "系统报错提示", "没有超管记录或密码输错！", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.Yes)
                    print(reply)
            except:
                # 发生错误时回滚
                db.rollback()
                reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                print(reply)
        else:
            reply=QMessageBox.warning(self, "系统报错提示", "你不是超级管理员！", QMessageBox.Yes | QMessageBox.No,
                                       QMessageBox.Yes)
            print(reply)

    def open_update_password_page(self):
        self.open_mag_update.show()



