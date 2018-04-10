import sys
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import  PyQt5.uic

MainWindowForm, MainWindowBase = PyQt5.uic.loadUiType('ui/mainwindow.ui')

class MainWindow(MainWindowBase, MainWindowForm):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        # setup the ui
        self.setupUi(self)

if ( __name__ == '__main__' ):
    app = None
    if ( not app ):
        app = QApplication([])

    window = MainWindow()
    window.show()

    if ( app ):
        app.exec_()