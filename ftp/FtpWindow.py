# -*- coding: utf-8 -*-

"""
Module implementing FtpWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Ui_FtpWindow import Ui_Form
import ftplib
import os
import sys

class FtpWindow(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    transfnum = 0
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(FtpWindow, self).__init__(parent)
        self.setupUi(self)
        self.readSettings()

    def readSettings(self):
        settings = QSettings("FtpUsr", "Info")
        # size = settings.value("size", QVariant(QSize(400, 400))).toSize()
        host = settings.value("host")
        port = settings.value("port")
        usr = settings.value("usr")
        pwd = settings.value("pwd")
        upfilepath = settings.value("upfilepath")
        upfilename = settings.value("upfilename")

        self.lineEdit_ip.setText(host)
        self.lineEdit_port.setText(port)
        self.lineEdit_usr.setText(usr)
        self.lineEdit_pwd.setText(pwd)
        self.lineEdit_upfilepath.setText(upfilepath)

    def writeSettings(self):
        settings = QSettings("FtpUsr", "Info")
        settings.setValue("host", QVariant(self.lineEdit_ip.text()))
        settings.setValue("port", QVariant(self.lineEdit_port.text()))
        settings.setValue("usr", QVariant(self.lineEdit_usr.text()))
        settings.setValue("pwd", QVariant(self.lineEdit_pwd.text()))
        settings.setValue("upfilepath", QVariant(self.lineEdit_upfilepath.text()))
        settings.setValue("upfilename", QVariant(os.path.basename(self.lineEdit_ip.text())))


    def closeEvent(self, event):
        self.writeSettings()


    @pyqtSlot()
    def on_pushButton_upfile_clicked(self):
        """
        Slot documentation goes here.
        """
        print ("on_pushButton_upfile_clicked")
  
        file, ok1 = QFileDialog.getOpenFileName(self,  
                                    "多文件选择",  
                                    "",
                                    "All Files (*);;Text Files (*.txt)")  
        print(file,ok1)
        self.lineEdit_upfilepath.setText(file)
  
    @pyqtSlot()
    def on_pushButton_dowfile_clicked(self):
        """
        Slot documentation goes here.
        """
        pass


    @pyqtSlot()
    def on_pushButton_start_clicked(self):
        """
        Slot documentation goes here.
        """
        host = self.lineEdit_ip.text()
        port = self.lineEdit_port.text()
        usr  = self.lineEdit_usr.text()
        pwd  = self.lineEdit_pwd.text()
        upfilepath = self.lineEdit_upfilepath.text()
        upfilename = os.path.basename(upfilepath)
        self.label_result.setText("")

        print("host is :%s" % host)
        print("port is :%s" % port)
        print("usr  is :%s" % usr)
        print("pwd  is :%s" % pwd)
        print("upfilepath  is :%s" % upfilepath)
        print("upfilename  is :%s" % upfilename)
        if(len(host) == 0 ):
            QMessageBox.information(self,  # 使用infomation信息框
                                    "提示",
                                    "IP地址 为空",
                                    QMessageBox.Yes)
            return
        if(len(port) == 0 ):
            # QMessageBox.information(self,  # 使用infomation信息框
            #                         "提示",
            #                         "端口 为空",
            #                         QMessageBox.Yes)
            port = "21"
        if(len(usr) == 0 ):
            QMessageBox.information(self,  # 使用infomation信息框
                                    "提示",
                                    "用户名 为空",
                                    QMessageBox.Yes)
            return
        if(len(pwd) == 0 ):
            QMessageBox.information(self,  # 使用infomation信息框
                                    "提示",
                                    "密码 为空",
                                    QMessageBox.Yes)
            return


        if((len(upfilepath) == 0) or (len(upfilename) == 0)):
            QMessageBox.information(self,  # 使用infomation信息框
                                    "提示",
                                    "文件路径 为空",
                                    QMessageBox.Yes)
            return

        print("======111===")
        try:
            self.label_result.setText("")
            f = ftplib.FTP(host, timeout=3)  # 实例化FTP对象
            print("f :%s" % f)
            # print("resp :%s" % respc)
            result = f.login(usr, pwd)  # 登录
            print("result:%s" % result)
            self.label_result.setText(result)

            code = 'UTF-8'
            f.encoding = code
            # f.cwd('documents')
            # 获取当前路径
            cur_path = f.pwd()
            print("FTP当前路径:", cur_path)

            '''以二进制形式上传文件'''
            file_remote = upfilename
            file_local = upfilepath
            bufsize = 102400  # 设置缓冲器大小
            self.label_result.setText("transfing......")
            self.label_result.update()
            fp = open(file_local, 'rb')
            filelen = fp.tell()
            print("filelen:%d" %filelen)
            resp = f.storbinary('STOR ' + file_remote, fp, bufsize)
            fp.close()
            f.quit()
            self.transfnum += 1
            self.label_result.setText("文件:%s" % upfilepath + "\n" + resp + "\n成功次数:%d" % self.transfnum + "\ntransf done!!!")
            print("transf done!!!")
        except:
            self.label_result.setText("连接失败！！！,请检查FTP地址和端口!!!")
