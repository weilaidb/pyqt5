# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Qtexample\git\pyqt5\code\ftp\FtpWindow3.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 448)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_ip.setMinimumSize(QtCore.QSize(241, 41))
        self.lineEdit_ip.setMaximumSize(QtCore.QSize(241, 41))
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.horizontalLayout_4.addWidget(self.lineEdit_ip)
        self.lineEdit_port = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_port.setMinimumSize(QtCore.QSize(71, 41))
        self.lineEdit_port.setMaximumSize(QtCore.QSize(71, 41))
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.horizontalLayout_4.addWidget(self.lineEdit_port)
        self.lineEdit_usr = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_usr.setMinimumSize(QtCore.QSize(151, 41))
        self.lineEdit_usr.setMaximumSize(QtCore.QSize(151, 41))
        self.lineEdit_usr.setObjectName("lineEdit_usr")
        self.horizontalLayout_4.addWidget(self.lineEdit_usr)
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.centralWidget)
        self.lineEdit_pwd.setMinimumSize(QtCore.QSize(151, 41))
        self.lineEdit_pwd.setMaximumSize(QtCore.QSize(151, 41))
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.horizontalLayout_4.addWidget(self.lineEdit_pwd)
        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_downloadpath = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_downloadpath.setMinimumSize(QtCore.QSize(101, 91))
        self.pushButton_downloadpath.setMaximumSize(QtCore.QSize(101, 91))
        self.pushButton_downloadpath.setObjectName("pushButton_downloadpath")
        self.horizontalLayout_2.addWidget(self.pushButton_downloadpath)
        self.pushButton_download = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_download.setMinimumSize(QtCore.QSize(101, 91))
        self.pushButton_download.setMaximumSize(QtCore.QSize(101, 91))
        self.pushButton_download.setObjectName("pushButton_download")
        self.horizontalLayout_2.addWidget(self.pushButton_download)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_downfilepath = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_downfilepath.sizePolicy().hasHeightForWidth())
        self.lineEdit_downfilepath.setSizePolicy(sizePolicy)
        self.lineEdit_downfilepath.setObjectName("lineEdit_downfilepath")
        self.verticalLayout_2.addWidget(self.lineEdit_downfilepath)
        self.lineEdit_downrename = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_downrename.sizePolicy().hasHeightForWidth())
        self.lineEdit_downrename.setSizePolicy(sizePolicy)
        self.lineEdit_downrename.setObjectName("lineEdit_downrename")
        self.verticalLayout_2.addWidget(self.lineEdit_downrename)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_upload = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_upload.setMinimumSize(QtCore.QSize(101, 91))
        self.pushButton_upload.setMaximumSize(QtCore.QSize(101, 91))
        self.pushButton_upload.setObjectName("pushButton_upload")
        self.horizontalLayout_3.addWidget(self.pushButton_upload)
        self.pushButton_start = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_start.setMinimumSize(QtCore.QSize(101, 91))
        self.pushButton_start.setMaximumSize(QtCore.QSize(101, 91))
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_3.addWidget(self.pushButton_start)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_upfilepath = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_upfilepath.sizePolicy().hasHeightForWidth())
        self.lineEdit_upfilepath.setSizePolicy(sizePolicy)
        self.lineEdit_upfilepath.setObjectName("lineEdit_upfilepath")
        self.verticalLayout_3.addWidget(self.lineEdit_upfilepath)
        self.lineEdit_uprename = QtWidgets.QLineEdit(self.centralWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_uprename.sizePolicy().hasHeightForWidth())
        self.lineEdit_uprename.setSizePolicy(sizePolicy)
        self.lineEdit_uprename.setObjectName("lineEdit_uprename")
        self.verticalLayout_3.addWidget(self.lineEdit_uprename)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_result = QtWidgets.QPushButton(self.centralWidget)
        self.pushButton_result.setMinimumSize(QtCore.QSize(101, 181))
        self.pushButton_result.setMaximumSize(QtCore.QSize(101, 181))
        self.pushButton_result.setObjectName("pushButton_result")
        self.horizontalLayout.addWidget(self.pushButton_result)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_fileinfo = QtWidgets.QLabel(self.centralWidget)
        self.label_fileinfo.setText("")
        self.label_fileinfo.setObjectName("label_fileinfo")
        self.verticalLayout.addWidget(self.label_fileinfo)
        self.label_result = QtWidgets.QLabel(self.centralWidget)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_downloadpath.setText(_translate("MainWindow", "下载路径"))
        self.pushButton_download.setText(_translate("MainWindow", "下载"))
        self.pushButton_upload.setText(_translate("MainWindow", "上传路径"))
        self.pushButton_start.setText(_translate("MainWindow", "上传文件"))
        self.pushButton_result.setText(_translate("MainWindow", "结果"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

