# -*- coding: utf-8 -*-

from automyccode import *

if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ftpw = MainWindow()
    ftpw.show()
    sys.exit(app.exec_())
    
 
 
