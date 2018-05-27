# -*- coding: utf-8 -*-

"""
Module implementing SshWindow.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QWidget

from Ui_ssh import Ui_Form

from sshcmd import SSHConnection


class SshWindow(QWidget, Ui_Form):
    """
    Class documentation goes here.
    """
    istestcase = 0
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(SshWindow, self).__init__(parent)
        self.setupUi(self)
    def show_w3(self):#显示窗体2
        self.show()

    @pyqtSlot()
    def on_pushButton_sendcmd_clicked(self):
        """
        Slot documentation goes here.
        """
        ipaddr = self.lineEdit_ip.text()
        usr = self.lineEdit_usr.text()
        pwd = self.lineEdit_pwd.text()
        if(0 == len(self.lineEdit_port.text().strip())):
            port = 22
        else:
            port = int(self.lineEdit_port.text().strip())

        # print(ipaddr)
        # print(usr)
        # print(pwd)
        # print(port)
        if(len(ipaddr.strip()) == 0 and self.istestcase == 0):
            return

        cmdlist = self.textEdit_cmdlist.toPlainText()

        try:
            conn = SSHConnection(ipaddr, port, usr, pwd)
            # conn = SSHConnection('192.168.145.100', 22, 'weilaidb', '00000000')
            data = conn.exec_command(cmdlist)
            # print(type(data))
            # print(type(data.decode('utf-8')))
            # print(data)

            self.textEdit_showresult.setText(data.decode('utf-8').strip())
        except Exception as e:
            self.textEdit_showresult.setText(str(e))

        # conn.exec_command('cd /home/test;pwd')  # cd需要特别处理
        # conn.exec_command('pwd')
        # conn.exec_command('tree /home/test')
