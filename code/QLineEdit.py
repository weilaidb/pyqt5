#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
PyQt5 教程

这个例子中,在QLineEdit中输入的文字实时的在QLabel中显示出来。

作者：我的世界你曾经来过
博客：http://blog.csdn.net/weiaitaowang
最后编辑：2016年8月4日
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lb1 = QLabel(self)
        qle = QLineEdit(self)
        showtext = QLineEdit(self)

        qle.move(60, 100)
        self.lb1.move(60, 40)

        qle.textChanged[str].connect(self.onChanged)

        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('单行文本')
        self.show()

    def onChanged(self, text):

        self.lb1.setText(text)
        self.lb1.adjustSize()
        # self.showtext.setText(text)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())