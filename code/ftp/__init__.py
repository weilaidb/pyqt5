from FtpWindow import *
import math 


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    ftpw = FtpWindow()
    ftpw.show()
    sys.exit(app.exec_())
    
 
