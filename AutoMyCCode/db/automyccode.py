# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_automyccode import Ui_MainWindow
import pymysqldb


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

    @pyqtSlot()
    def on_pushButton_showresult_clicked(self):
        """
        Slot documentation goes here.
        """
        print("show result")




