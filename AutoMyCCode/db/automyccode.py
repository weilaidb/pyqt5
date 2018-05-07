# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QTimer

from Ui_automyccode import Ui_MainWindow
from pymysqldb import default_insert_contetNameWithTime
import win32clipboard as wc
import win32con
import pyperclip


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        # self.timer.start(2000)  # 设置计时间隔并启动

    def insert2db():
        pass


    def showresult(self):
        pass


    @pyqtSlot()
    def on_pushButton_insert_clicked(self):
        """
        Slot documentation goes here.
        """
        print("insert 2 db")
        content = self.textEdit_inserttext.toPlainText()
        print(content)
        name = ""

        if(len(content.strip()) == 0):
            print("content len 0")
            return
        if(len(content) > 100) :
            name = content.lstrip()[0:100]
        else:
            name = content

        retval = default_insert_contetNameWithTime(data=(name, content))
        if(retval):
            self.statusBar.showMessage("成功")
        else:
            self.statusBar.showMessage("失败")

        self.timer.start(2000)

    @pyqtSlot()
    def on_pushButton_showresult_clicked(self):
        """
        Slot documentation goes here.
        """
        print("show result")
    
    @pyqtSlot()
    def on_pushButton_clean_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit_inserttext.setText("")
    
    @pyqtSlot()
    def on_pushButton_paste_clicked(self):
        """
        Slot documentation goes here.
        """
        self.textEdit_inserttext.setText(pyperclip.paste())

    def operate(self):
        #具体操作
        self.statusBar.showMessage("")
        self.timer.stop()