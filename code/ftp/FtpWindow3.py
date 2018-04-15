# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from Ui_FtpWindow3 import Ui_MainWindow
import ftplib
import os
import datetime
import timeit



class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    transfnum = 0
    selectfile = ""
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.readSettings()
        self.lineEdit_ip.setPlaceholderText("请输入FTP服务地址")
        self.lineEdit_port.setPlaceholderText("FTP端口")
        self.lineEdit_usr.setPlaceholderText("用户名")
        self.lineEdit_pwd.setPlaceholderText("密码")
        self.lineEdit_upfilepath.setPlaceholderText("上传路径")
        self.lineEdit_uprename.setPlaceholderText("上传更名")
        self.lineEdit_downfilepath.setPlaceholderText("下载路径")
        self.lineEdit_downrename.setPlaceholderText("下载更名")

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
        self.setlabelfilesize(upfilepath)

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
    def on_pushButton_download_clicked(self):
        """
        Slot documentation goes here.
        """
        pass
    
    @pyqtSlot()
    def on_pushButton_upload_clicked(self):
        """
        Slot documentation goes here.
        """
        print ("on_pushButton_upfile_clicked")
  
        file, ok1 = QFileDialog.getOpenFileName(self,  
                                    "多文件选择",  
                                    "",
                                    "All Files (*);;Text Files (*.txt)")



        print(file,ok1)
        print(type(file))
        print(type(ok1))
        print("file:%s " % (file))
        print("ok:%s" %(ok1))
        if(self.selectfile != file):
            self.setlabelfilesize(file)
            self.lineEdit_upfilepath.setText(file)
            self.selectfile = file

    def setlabelfilesize(self,file):
        self.label_fileinfo.setText("文件大小：%u,%fK,%fM" % ((os.path.getsize(file)),
                                    os.path.getsize(file)/1024.0,
                                    (os.path.getsize(file))/1024/1024.0))
  
  
  
    
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
            time_start = timeit.default_timer()
            print("time_start %d" % time_start)

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
            filelen = os.path.getsize(file_local)
            print("filelen:%d" %filelen)
            resp = f.storbinary('STOR ' + file_remote, fp, bufsize)
            fp.close()
            f.quit()
            self.transfnum += 1
            time_end = timeit.default_timer()
            print("time_start %d" % time_end)
            timeelpse = (time_end - time_start) 
            print (datetime.datetime.now())
            print('time_start', time_start)
            print('time_end', time_end)
            print('totally cost', timeelpse)

            if(timeelpse < 1):
                timeshotext = "耗时:%fms" % (timeelpse * 1000)
            else:
                timeshotext = "耗时:%fs" % (timeelpse)

            timeshowtext = ""
            showtext = "文件:%s" % upfilepath \
                        + "\n大小：%d,%s,速度:%fM/s\n" % (filelen, timeshotext, (filelen)/timeelpse/(1024 * 1024)/1.0)\
                       + "\n" \
                       + resp \
                       + "\n成功次数:%d" % self.transfnum \
                       + "\ntransf done!!!"

            self.label_result.setText(showtext)
            print("transf done!!!")
        except:
            self.label_result.setText("连接失败！！！,请检查FTP地址和端口!!!")
            print("transf fail!!!")
    
    @pyqtSlot()
    def on_pushButton_downloadpath_clicked(self):
        """
        Slot documentation goes here.
        """
        directory1 = QFileDialog.getExistingDirectory(self,  
                                    "选取文件夹",  
                                    "")                                 #起始路径  
        print(directory1)  
        self.lineEdit_downfilepath.setText(directory1)