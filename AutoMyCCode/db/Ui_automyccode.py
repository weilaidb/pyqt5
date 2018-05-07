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
        MainWindow.resize(659, 534)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_paste = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_paste.setMinimumSize(QtCore.QSize(91, 41))
        self.pushButton_paste.setMaximumSize(QtCore.QSize(91, 41))
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.horizontalLayout.addWidget(self.pushButton_paste)
        self.pushButton_insert = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_insert.setMinimumSize(QtCore.QSize(81, 41))
        self.pushButton_insert.setMaximumSize(QtCore.QSize(81, 41))
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.horizontalLayout.addWidget(self.pushButton_insert)
        self.pushButton_clean = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clean.setMinimumSize(QtCore.QSize(91, 41))
        self.pushButton_clean.setMaximumSize(QtCore.QSize(91, 41))
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.horizontalLayout.addWidget(self.pushButton_clean)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.textEdit_inserttext = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_inserttext.setObjectName("textEdit_inserttext")
        self.verticalLayout.addWidget(self.textEdit_inserttext)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton_showresult = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_showresult.setMinimumSize(QtCore.QSize(91, 41))
        self.pushButton_showresult.setMaximumSize(QtCore.QSize(91, 41))
        self.pushButton_showresult.setObjectName("pushButton_showresult")
        self.verticalLayout_2.addWidget(self.pushButton_showresult)
        self.textEdit_showresult = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_showresult.setObjectName("textEdit_showresult")
        self.verticalLayout_2.addWidget(self.textEdit_showresult)
        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_paste.setText(_translate("MainWindow", "Paste"))
        self.pushButton_insert.setText(_translate("MainWindow", "Insert"))
        self.pushButton_clean.setText(_translate("MainWindow", "Clean"))
        self.pushButton_showresult.setText(_translate("MainWindow", "ShowResult"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

