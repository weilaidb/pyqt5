# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Qtexample\git\pyqt5\code\ftp\FtpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(650, 476)
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(10, 50, 425, 22))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.lineEdit_ip = QtWidgets.QLineEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_ip.sizePolicy().hasHeightForWidth())
        self.lineEdit_ip.setSizePolicy(sizePolicy)
        self.lineEdit_ip.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_ip.setFont(font)
        self.lineEdit_ip.setObjectName("lineEdit_ip")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.lineEdit_port = QtWidgets.QLineEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_port.sizePolicy().hasHeightForWidth())
        self.lineEdit_port.setSizePolicy(sizePolicy)
        self.lineEdit_port.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_port.setFont(font)
        self.lineEdit_port.setObjectName("lineEdit_port")
        self.pushButton_upfile = QtWidgets.QPushButton(Form)
        self.pushButton_upfile.setGeometry(QtCore.QRect(10, 140, 81, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_upfile.sizePolicy().hasHeightForWidth())
        self.pushButton_upfile.setSizePolicy(sizePolicy)
        self.pushButton_upfile.setObjectName("pushButton_upfile")
        self.pushButton_dowfile = QtWidgets.QPushButton(Form)
        self.pushButton_dowfile.setGeometry(QtCore.QRect(10, 230, 81, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_dowfile.sizePolicy().hasHeightForWidth())
        self.pushButton_dowfile.setSizePolicy(sizePolicy)
        self.pushButton_dowfile.setObjectName("pushButton_dowfile")
        self.lineEdit_downfilepath = QtWidgets.QLineEdit(Form)
        self.lineEdit_downfilepath.setGeometry(QtCore.QRect(110, 230, 481, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_downfilepath.sizePolicy().hasHeightForWidth())
        self.lineEdit_downfilepath.setSizePolicy(sizePolicy)
        self.lineEdit_downfilepath.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_downfilepath.setFont(font)
        self.lineEdit_downfilepath.setObjectName("lineEdit_downfilepath")
        self.label_result = QtWidgets.QLabel(Form)
        self.label_result.setGeometry(QtCore.QRect(40, 360, 521, 101))
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.lineEdit_upfilepath = QtWidgets.QLineEdit(Form)
        self.lineEdit_upfilepath.setGeometry(QtCore.QRect(110, 140, 481, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_upfilepath.sizePolicy().hasHeightForWidth())
        self.lineEdit_upfilepath.setSizePolicy(sizePolicy)
        self.lineEdit_upfilepath.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_upfilepath.setFont(font)
        self.lineEdit_upfilepath.setObjectName("lineEdit_upfilepath")
        self.pushButton_start = QtWidgets.QPushButton(Form)
        self.pushButton_start.setGeometry(QtCore.QRect(250, 290, 161, 51))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_start.setFont(font)
        self.pushButton_start.setObjectName("pushButton_start")
        self.splitter_2 = QtWidgets.QSplitter(Form)
        self.splitter_2.setGeometry(QtCore.QRect(10, 90, 425, 22))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_3 = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_usr = QtWidgets.QLineEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_usr.sizePolicy().hasHeightForWidth())
        self.lineEdit_usr.setSizePolicy(sizePolicy)
        self.lineEdit_usr.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_usr.setFont(font)
        self.lineEdit_usr.setObjectName("lineEdit_usr")
        self.label_ = QtWidgets.QLabel(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_.sizePolicy().hasHeightForWidth())
        self.label_.setSizePolicy(sizePolicy)
        self.label_.setMaximumSize(QtCore.QSize(50, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_.setFont(font)
        self.label_.setWordWrap(True)
        self.label_.setObjectName("label_")
        self.lineEdit_pwd = QtWidgets.QLineEdit(self.splitter_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_pwd.sizePolicy().hasHeightForWidth())
        self.lineEdit_pwd.setSizePolicy(sizePolicy)
        self.lineEdit_pwd.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_pwd.setFont(font)
        self.lineEdit_pwd.setObjectName("lineEdit_pwd")
        self.label_fileinfo = QtWidgets.QLabel(Form)
        self.label_fileinfo.setGeometry(QtCore.QRect(120, 205, 471, 21))
        self.label_fileinfo.setText("")
        self.label_fileinfo.setObjectName("label_fileinfo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEdit_ip, self.lineEdit_port)
        Form.setTabOrder(self.lineEdit_port, self.lineEdit_usr)
        Form.setTabOrder(self.lineEdit_usr, self.lineEdit_pwd)
        Form.setTabOrder(self.lineEdit_pwd, self.pushButton_upfile)
        Form.setTabOrder(self.pushButton_upfile, self.lineEdit_upfilepath)
        Form.setTabOrder(self.lineEdit_upfilepath, self.pushButton_dowfile)
        Form.setTabOrder(self.pushButton_dowfile, self.lineEdit_downfilepath)
        Form.setTabOrder(self.lineEdit_downfilepath, self.pushButton_start)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "ftp工具"))
        self.label.setText(_translate("Form", "服务器地址"))
        self.label_2.setText(_translate("Form", "端口"))
        self.pushButton_upfile.setText(_translate("Form", "上传文件路径"))
        self.pushButton_dowfile.setText(_translate("Form", "下载文件路径"))
        self.pushButton_start.setText(_translate("Form", "开 始"))
        self.label_3.setText(_translate("Form", "用户名"))
        self.label_.setText(_translate("Form", "密码"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

