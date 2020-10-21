# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from mag_update import Ui_Mag_Update
import pymysql
import MySQLdb
import hashlib

class open_mag_update(QtWidgets.QWidget, Ui_Mag_Update): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_mag_update, self).__init__(parent)
        self.setupUi(self) # import Ui_Register

    # signal channel for connection
    def mag_update_password(self):
        # 获取QLineEdit文本框中的输入内容
        magname_input=self.pUserName.text().strip()
        password_old=self.oldPassword.text().strip()
        password_new=self.newPassword.text().strip()

        # 先进行两次密码输入是否相同, 并且用户名不为空
        if (len(magname_input) == 0 or len(password_old) == 0 or len(password_new) == 0):
            reply=QMessageBox.critical(self, "系统报错提示", "用户名或密码不能为空！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)

        if (password_old == password_new):
            reply=QMessageBox.warning(self, "系统报错提示", "新旧密码不能相同！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)

        if ((password_old != password_new) and (len(password_old) != 0) and (len(password_new) != 0)):
            # Mysql的插入处理
            mname=magname_input
            new_pwd=password_new

            # 创建数据库连接对象
            db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
            # 创建数据库连接
            cursor=db.cursor()
            # 创建加密对象
            md5=hashlib.md5()

            # 先进行查询语句，找到该用户
            query_manager="select * from manager where magname = '%s'" % (mname)
            try:
                # 执行SQL语句
                cursor.execute(query_manager)
                # 获取所有记录列表
                results=cursor.fetchall()
                flag_user=0  # 用户记录已存在
                if (not results):
                    flag_user=1  # 表示用户未曾注册

                # 通过flag_user进行判断
                if flag_user == 1:
                    reply=QMessageBox.warning(self, "系统消息提示", "没有这个账户，请注册！", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.Yes)
                    print(reply)
                else:
                    magname=mname
                    password=new_pwd

                    # 加密
                    md5.update(password.encode('utf-8'))

                    # SQL更新
                    update_password="update manager set password = '%s' where magname = '%s'" % (md5.hexdigest(), magname)

                    # values=(username, md5.hexdigest())

                    try:
                        # 执行sql语句
                        cursor.execute(update_password)
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
                    reply=QMessageBox.information(self, "系统消息提示", "管理员改密成功！", QMessageBox.Yes | QMessageBox.No,
                                                  QMessageBox.Yes)
                    print(reply)
            except:
                # 发生错误时回滚
                db.rollback()
                reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                print(reply)













