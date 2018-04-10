import sys
import urllib.request
from PyQt5 import QtCore, QtGui, QtWidgets
import  PyQt5.uic
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from cmdserverUi import Ui_MainWindow

# import Mainpage  # 导入ui文件转换出的python源码模块


##-----------创建UI类-----------
class Mainpage(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Mainpage, self).__init__(parent)
        self.setupUi(self)
        # self.
        self.lineEdit_sendnum.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainpage = Mainpage()
    mainpage.show()
    app.exec_()


