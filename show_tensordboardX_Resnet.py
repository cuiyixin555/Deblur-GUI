from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys

class NetWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setWindowTitle('展示ResNet网络结构')
        self.browser = QWebEngineView()

        # 加载外部的Web页面
        self.browser.load(QUrl('http://localhost:6006/#graphs&run=.'))
        # self.browser.load(QUrl('http://laptop-b6f6vraq:6006/#graphs&run=.'))
        self.setCentralWidget(self.browser)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     app.exec_()