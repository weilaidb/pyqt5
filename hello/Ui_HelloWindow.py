# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Qtexample\git\pyqt5\hello\HelloWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(462, 351)
        Dialog.setSizeGripEnabled(True)
        self.pushButton_ok = QtWidgets.QPushButton(Dialog)
        self.pushButton_ok.setGeometry(QtCore.QRect(50, 190, 91, 51))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_cancle = QtWidgets.QPushButton(Dialog)
        self.pushButton_cancle.setGeometry(QtCore.QRect(170, 190, 91, 51))
        self.pushButton_cancle.setObjectName("pushButton_cancle")
        self.pushButton_exit = QtWidgets.QPushButton(Dialog)
        self.pushButton_exit.setGeometry(QtCore.QRect(290, 190, 91, 51))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 221, 51))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_ok.setText(_translate("Dialog", "ok"))
        self.pushButton_cancle.setText(_translate("Dialog", "cancle"))
        self.pushButton_exit.setText(_translate("Dialog", "exit"))
        self.label.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

