# -*- coding: utf-8 -*-
#pyqtmain pyqt main
from mainui import *
import math 


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ftpw = MainWindow()
    ftpw.show()
    sys.exit(app.exec_())

