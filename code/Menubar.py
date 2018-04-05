#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
"""
ZetCode PyQt5 tutorial
 
This program creates a menubar. The
menubar has one menu with an exit action.
 
author: Jan Bodnar
website: zetcode.com
last edited: January 2015
"""
 
import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
from PyQt5.QtGui import QIcon
 
 
class Example(QMainWindow):
     
    def __init__(self):
        super().__init__()
         
        self.initUI()
         
         
    def initUI(self):              
         
        exitAction = QAction(QIcon('exit.png'), '&Exit', self)       
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)
		
        E2Action = QAction(QIcon('exit.png'), '&Exit2', self)       
        E2Action.setShortcut('Ctrl+Q')
        E2Action.setStatusTip('Exit application')
        E2Action.triggered.connect(qApp.quit)
		
        self.statusBar()
 
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAction)
        fileMenu.addAction(E2Action)
        exitMenu = menubar.addMenu('&Txt')
        exitMenu.addAction(E2Action)
 
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Menubar')   
        self.show()
         
         
if __name__ == '__main__':
     
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())