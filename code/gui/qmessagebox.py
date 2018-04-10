from __future__ import division
import  sys
from math import  *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.myButton = QPushButton(self)
        self.myButton.setObjectName("myButton")
        self.myButton.setText("Test")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        reply = QMessageBox.information(self,  # 使用infomation信息框
                                        "标题",
                                        "消息",
                                        QMessageBox.Yes | QMessageBox.No)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    sys.exit(app.exec_())
