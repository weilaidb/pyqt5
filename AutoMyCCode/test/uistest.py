import sys
import json
# from utils import reg, cal, colorpicker
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQuick import *
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtSlot
from PyQt5.QtQml import QQmlApplicationEngine


class MyClass(QQuickView, QObject):
    def __init__(self, parent=None):
        super(MyClass, self).__init__(parent)
        self.cpwin = colorpicker.ColorPickerWin()

    @pyqtSlot()
    def openColorPicer(self):
        self.cpwin.cpwinOpen()
        self.win.hide()

    @pyqtSlot()
    def showthiswin(self):
        if not self.win.isVisible():
            self.win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('ui/main.qml')
    win = engine.rootObjects()[0]
    win.show()
    con = MyClass()
    con.win = win
    engine.rootContext().setContextProperty("con", con)

    con.cpwin.visibleChanged.connect(con.showthiswin)
    sys.exit(app.exec_())
