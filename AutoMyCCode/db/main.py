# -*- coding: utf-8 -*-

from automyccode import *
from caculater import *
from ssh import *

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ftpw = MainWindow()
    ftpw.show()
    app.installEventFilter(ftpw)

    #显示另外一个窗体
    cal = Calculator()
    ftpw.actionCalculator.triggered.connect(cal.show_w2)
    cal.hide()

    ssh = SshWindow()
    ftpw.actionSSH.triggered.connect(ssh.show_w3)

    sys.exit(app.exec_())
    
 
 
