import sys
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, pyqtSignal

class ZeroSpinBox(QSpinBox):
    zeros = 0
    atzero = pyqtSignal(int)  # 定义信号,定义参数为int类型

    def __init__(self, parent = None):
        super(ZeroSpinBox, self).__init__(parent)
        self.valueChanged.connect(self.checkzero)
        self. atzero.connect(self.announce)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            self.atzero.emit(self.zeros)
        # print("%d" % self.zeros)


    def announce(self,zeros):
        print("ZeroSpinBox has been at zero %d times" % zeros)



app = QApplication(sys.argv)
zerospinbox = ZeroSpinBox()
zerospinbox.show()
app.exec_()
























