# -*- coding: utf-8 -*-
# corresponding to welcome.py
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from mag_welcome import Ui_Mag_Welcome   # 导入生成first.py里生成的类
from open_mag_update import open_mag_update
# TODO:
from open_save_picture import open_save_picture
import MySQLdb

class open_mag_welcome(QtWidgets.QWidget, Ui_Mag_Welcome): # 注意：在对象初始化的时候import的是Ui_Form的类对象
    def __init__(self, parent=None):
        super(open_mag_welcome, self).__init__(parent)
        self.setupUi(self) # import Ui_Form

        # 实例化子窗体
        self.open_mag_update = open_mag_update()
        # TODO:
        self.open_save_picture = open_save_picture()

    # signal channel for connection
    def drop_user_item(self):
        username_input=self.qLineEdit.text().strip()

        # 先判断用户名是否为空
        if len(username_input) == 0:
            reply = QMessageBox.critical(self, "系统报错提示", "用户名不能为空！", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
            print(reply)
        else:
            uname=username_input
            # 创建数据库连接对象
            db=MySQLdb.connect("localhost", "root", "a9b3c927", "person")
            # 创建数据库连接
            cursor=db.cursor()

            # 书写查询语句
            query_repeat="select * from user where username = '%s'" % (uname)
            try:
                # 执行SQL语句
                cursor.execute(query_repeat)
                # 获取所有记录列表
                results=cursor.fetchall()
                flag_user=0  # 默认用户已经注册
                if (not results):
                    flag_user=1  # 表示用户未曾注册
                if flag_user == 1:
                    reply=QMessageBox.warning(self, "系统消息提示", "没有该用户名！", QMessageBox.Yes | QMessageBox.No,
                                              QMessageBox.Yes)
                    print(reply)
                else:
                    # SQL 删除记录语句
                    query_drop_item="delete from user where username = '%s'" % (uname)

                    try:
                        # 执行sql语句
                        cursor.execute(query_drop_item)
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
                    reply=QMessageBox.information(self, "系统消息提示", "用户重置成功！", QMessageBox.Yes | QMessageBox.No,
                                                  QMessageBox.Yes)
                    print(reply)
            except:
                # 发生错误时回滚
                db.rollback()
                reply=QMessageBox.critical(self, "系统故障", "系统故障！", QMessageBox.Yes | QMessageBox.No,
                                           QMessageBox.Yes)
                print(reply)

    def mag_update_password(self):
        self.open_mag_update.show()

    def save_picture(self):
        self.open_save_picture.show()



