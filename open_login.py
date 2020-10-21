# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from open_welcome import open_welcome
from open_register import open_register
from open_user_update import open_user_update
from login import Ui_Login

# MySql模块
import MySQLdb
import hashlib

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget,QFormLayout, QLabel
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout, QFormLayout, QPushButton

class open_login(QtWidgets.QWidget, Ui_Login): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_login, self).__init__(parent)
        self.setupUi(self) # import Ui_Login

        # 实例化子窗体
        self.open_welcome = open_welcome() # 用户下的去模糊功能页面
        self.open_register = open_register() # 用户注册页面
        self.open_user_update = open_user_update() # 用户改密页面

    # signal channel for connection
    def open_welcome_page(self):
        uname = self.pUserName.text().strip()
        pwd = self.pPassword.text().strip()
        if (len(uname) == 0 or len(pwd) == 0):
            reply = QMessageBox.critical(self, "系统报错提示", "用户名或密码不能为空！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)

        if(len(uname) != 0 and len(pwd) != 0):
            # 遍历数据库的item
            # 打开数据库连接
            db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
            # 使用cursor()方法获取操作游标
            cursor=db.cursor()

            # SQL 查询语句
            md5=hashlib.md5()
            md5.update(pwd.encode('utf-8'))
            sql="select * from user where username = '%s' and password = '%s'" % (uname, md5.hexdigest())

            try:
                # 执行SQL语句
                cursor.execute(sql)
                # 获取所有记录列表
                results=cursor.fetchall()
                flag = 0
                # 判断对数据库读取的内容是否为空
                if (not results):
                    flag = 1 # 表示user表里没有该用户，该用户需要注册
                else:
                    for row in results:
                        id_db=row [0]
                        uname_db=row [1]
                        pwd_db=row [2]
                        print("id_db=%d, uname_db=%s, pwd_db=%s" % (id_db, uname_db, pwd_db))

                # 判断用户是否已经注册 flag == 0表示已经注册， flag == 1 表示没有注册
                if flag == 0:
                    reply=QMessageBox.information(self, "系统消息提示", "用户登陆成功！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                    print(reply)
                    self.open_welcome.show()
                elif flag == 1:
                    reply=QMessageBox.warning(self, "系统报错提示", "用户名错误或密码错误或未注册！", QMessageBox.Yes | QMessageBox.No,
                                               QMessageBox.Yes)
                    print(reply)
            except:
                # 发生错误时回滚
                db.rollback()
                reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                print(reply)

    def open_register_page(self):
        self.open_register.show()

    def open_update_password_page(self):
        self.open_user_update.show()


# app = QtWidgets.QApplication(sys.argv)
# window = open_login()
# window.show()
# app.exec_()
