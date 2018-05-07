# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Qtexample\git\pyqt5\AutoMyCCode\db\automyccode.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(772, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.textEdit_inserttext = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_inserttext.setGeometry(QtCore.QRect(10, 70, 301, 471))
        self.textEdit_inserttext.setObjectName("textEdit_inserttext")
        self.textEdit_showresult = QtWidgets.QTextEdit(self.centralWidget)
        self.textEdit_showresult.setGeometry(QtCore.QRect(350, 70, 301, 471))
        self.textEdit_showresult.setObjectName("textEdit_showresult")
        self.pushButton_insert = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_insert.setGeometry(QtCore.QRect(20, 40, 75, 23))
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.pushButton_showresult = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_showresult.setGeometry(QtCore.QRect(360, 40, 75, 23))
        self.pushButton_showresult.setObjectName("pushButton_showresult")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_insert.setText(_translate("MainWindow", "Insert"))
        self.pushButton_showresult.setText(_translate("MainWindow", "ShowResult"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

