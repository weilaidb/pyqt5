#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
ZetCode PyQt5 tutorial
 
In this example, we create a bit
more complicated window layout using
the QGridLayout manager.
 
author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
 
import sys
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
    QTextEdit, QGridLayout, QApplication)
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel
# from __future__ import division
import sys
from math import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Example(QWidget):
     
    def __init__(self):
        super().__init__()
        self.initUI()
         
         
    def initUI(self):
         
        title = QLabel('Title')
        author = QLabel('Author')
        review = QLabel('Review')
 
        titleEdit = QLineEdit(self)
        authorEdit = QLineEdit(self)
        reviewEdit = QTextEdit(self)

        # reviewEdit.setText("abc")
        # titleEdit.setText("aaaaaaaaaa")
        # titleEdit.s
        # titleEdit.textChanged[str].connect(self.onChangedText)
        # titleEdit.textChanged(self,str).co
        titleEdit.textChanged[str].connect(self.onChangedText)
        titleEdit.textChanged.connect(reviewEdit.setText)

 
        grid = QGridLayout()
        grid.setSpacing(10)
 
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
 
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
 
        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
         
        self.setLayout(grid)
         
        self.setGeometry(300, 300, 350, 300)
        self.showMaximized()
        self.setWindowTitle('Review222222222222222')   
        self.show()
        self.showMaximized()

    def onChangedText(self, text):
        self.reviewEdit.setText(text)
        self.reviewEdit.adjustSize()
        # self.reviewEdit.setText(self,text);
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
	
	
