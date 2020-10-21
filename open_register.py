# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from open_welcome import open_welcome
from register import Ui_Register
import pymysql
import MySQLdb
import hashlib

class open_register(QtWidgets.QWidget, Ui_Register): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_register, self).__init__(parent)
        self.setupUi(self) # import Ui_Register

    # signal channel for connection
    def write_database(self):

        # 获取QLineEdit文本框中的输入内容
        username_input = self.pUserName.text().strip()
        password_1 = self.pPassword.text().strip()
        password_2 = self.queren.text().strip()

        # 先进行两次密码输入是否相同, 并且用户名不为空
        if (len(username_input) == 0 or len(password_1) == 0 or len(password_2) == 0):
            reply = QMessageBox.critical(self, "系统报错提示", "用户名或密码不能为空！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)

        if (password_1 != password_2):
            reply=QMessageBox.warning(self, "系统报错提示", "两次输入密码不一致！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)

        if ((password_1 == password_2) and (len(password_1) != 0) and (len(password_2) != 0)):
            # Mysql的插入处理
            uname = username_input
            pwd = password_1

            # 创建数据库连接对象
            db = MySQLdb.connect("localhost","root","a9b3c927","person" )
            #创建数据库连接
            cursor=db.cursor()
            # 创建加密对象
            md5=hashlib.md5()

            # 先进行查询语句，防止同一个用户名注册多次
            query_repeat= "select * from user where username = '%s'" % (uname)
            try:
                # 执行SQL语句
                cursor.execute(query_repeat)
                # 获取所有记录列表
                results=cursor.fetchall()
                flag_user = 0 # 默认用户已经注册
                if(not results):
                    flag_user = 1 # 表示用户未曾注册
                if flag_user == 0:
                    reply=QMessageBox.warning(self, "系统消息提示", "该用户已注册，请登录！", QMessageBox.Yes | QMessageBox.No,
                                                  QMessageBox.Yes)
                    print(reply)
                else:
                    # SQL 插入语句
                    query_register='insert into user(username, password) values(%s, %s)'
                    username=uname
                    password=pwd

                    # 加密
                    md5.update(password.encode('utf-8'))
                    values=(username, md5.hexdigest())

                    try:
                        # 执行sql语句
                        cursor.execute(query_register, values)
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
                    reply=QMessageBox.information(self, "系统消息提示", "用户注册成功！", QMessageBox.Yes | QMessageBox.No,
                                                  QMessageBox.Yes)
                    print(reply)
            except:
                # 发生错误时回滚
                db.rollback()
                reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                print(reply)








