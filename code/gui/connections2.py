import sys
import urllib.request
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ZeroSpinBox(QSpinBox):
    zeros = 0

    def __init__(self, parent = None):
        super(ZeroSpinBox, self).__init__(parent)
        self.valueChanged.connect(self.checkzero)
        self._signal.atzero.connect(self.announce)

    def checkzero(self):
        if self.value() == 0:
            self.zeros += 1
            # self.
            self._signal.atzero.emit("atzero")
        print("%d" % self.zeros)
            # self._signal.connect(self.zeros)
            # self._signal.emit("atzero")
            # self.atzero.connect(self.zeros)
        # self.atzero.connect(self.announce)

    def announce(self):
        print("ZeroSpinBox has been at zero %d times" % self.zeros)



app = QApplication(sys.argv)
zerospinbox = ZeroSpinBox()
zerospinbox.show()
app.exec_()
























