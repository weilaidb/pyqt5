from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import *
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtSlot, pyqtSignal


class ColorPickerWin(QQuickView, QObject):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(ColorPickerWin, self).__init__()

        self.setSource(QUrl("colorpicker.qml"))

    def cpwinOpen(self):
        # print(self.__class__)
        # qe = QtCore.QEventLoop()
        if not self.isVisible():
            self.show()
