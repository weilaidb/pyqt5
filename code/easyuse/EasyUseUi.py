# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from Ui_EasyUseUi import Ui_MainWindow


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
        self.texteditshow = QTextEdit("");
    
    @pyqtSlot(int)
    def on_tabWidget_currentChanged(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type int
        """
        print("index:%d" % index)
        self
        #self.textEdit_show.show()
    
    @pyqtSlot(str)
    def on_tabWidget_objectNameChanged(self, objectName):
        """
        Slot documentation goes here.
        
        @param objectName DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_tab_3_windowTitleChanged(self, title):
        """
        Slot documentation goes here.
        
        @param title DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_tab_2_objectNameChanged(self, objectName):
        """
        Slot documentation goes here.
        
        @param objectName DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
    
    @pyqtSlot(str)
    def on_tab_2_windowTitleChanged(self, title):
        """
        Slot documentation goes here.
        
        @param title DESCRIPTION
        @type str
        """
        # TODO: not implemented yet
        raise NotImplementedError
