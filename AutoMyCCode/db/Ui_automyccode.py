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
        MainWindow.resize(752, 536)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.centralWidget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget = QtWidgets.QWidget(self.splitter_2)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_paste = QtWidgets.QPushButton(self.widget)
        self.pushButton_paste.setMinimumSize(QtCore.QSize(91, 41))
        self.pushButton_paste.setMaximumSize(QtCore.QSize(91, 41))
        self.pushButton_paste.setObjectName("pushButton_paste")
        self.horizontalLayout.addWidget(self.pushButton_paste)
        self.pushButton_insert = QtWidgets.QPushButton(self.widget)
        self.pushButton_insert.setMinimumSize(QtCore.QSize(81, 41))
        self.pushButton_insert.setMaximumSize(QtCore.QSize(81, 41))
        self.pushButton_insert.setObjectName("pushButton_insert")
        self.horizontalLayout.addWidget(self.pushButton_insert)
        self.pushButton_clean = QtWidgets.QPushButton(self.widget)
        self.pushButton_clean.setMinimumSize(QtCore.QSize(91, 41))
        self.pushButton_clean.setMaximumSize(QtCore.QSize(91, 41))
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.horizontalLayout.addWidget(self.pushButton_clean)
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.listWidget_search = QtWidgets.QListWidget(self.splitter)
        self.listWidget_search.setWordWrap(False)
        self.listWidget_search.setObjectName("listWidget_search")
        self.textEdit_inserttext = QtWidgets.QTextEdit(self.splitter)
        self.textEdit_inserttext.setObjectName("textEdit_inserttext")
        self.layoutWidget = QtWidgets.QWidget(self.splitter_3)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_showresult = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_showresult.setMinimumSize(QtCore.QSize(91, 41))
        self.pushButton_showresult.setMaximumSize(QtCore.QSize(91, 41))
        self.pushButton_showresult.setObjectName("pushButton_showresult")
        self.horizontalLayout_2.addWidget(self.pushButton_showresult)
        self.lineEdit_search = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit_search.setMinimumSize(QtCore.QSize(0, 41))
        self.lineEdit_search.setMaximumSize(QtCore.QSize(16777215, 41))
        self.lineEdit_search.setObjectName("lineEdit_search")
        self.horizontalLayout_2.addWidget(self.lineEdit_search)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.textEdit_showresult = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_showresult.setObjectName("textEdit_showresult")
        self.verticalLayout_2.addWidget(self.textEdit_showresult)
        self.gridLayout.addWidget(self.splitter_3, 0, 0, 1, 1)
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

