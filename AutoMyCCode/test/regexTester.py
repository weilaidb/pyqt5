#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 18:38:03 2013

@author: Leo
"""
import re

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
# import QSyntaxHighlighter
import regexTesterUi


class MyHighlighter(QSyntaxHighlighter):

    def __init__(self, parent):                                                  # parent即绑定的QTextEdit对象
        QSyntaxHighlighter.__init__(self, parent)
        self.parent = parent
        self.highlight_data = []                                                # 存储匹配结果的列表
        
        self.matched_format = QTextCharFormat()                           # 定义高亮格式
        brush = QBrush(Qt.yellow, Qt.SolidPattern)
        self.matched_format.setBackground(brush)

    def highlightBlock(self, text):
        index = 0
        length = 0
        for item in self.highlight_data:
            if item.count('\n') != 0:
                itemList = item.split('\n')
                for part in itemList:
                    index = text.index(part, index + length)
                    if index == -1:
                        index = 0
                    else:
                        length = len(part)
                        self.setFormat(index, length, self.matched_format)
            else:
                # if (length == (0)):
                #     print("error length is 0")
                #     return
                try:
                    index = text.index(item, index + length)
                    length = len(item)
                    self.setFormat(index, length, self.matched_format)
                except Exception as e:
                    print("exception:", e)


        
    def setHighlightData(self, highlight_data):
        self.highlight_data = highlight_data
       
       
class RegexTesterDialog(QDialog, regexTesterUi.Ui_Dialog):
    
    def __init__(self, parent = None):
        super(RegexTesterDialog, self).__init__(parent)
        self.CI = False     # case insensitive (i)
        self.MB = False     # ^$ match at line breaks (m)
        self.DM = False     # dot matched all (s)
        self.regex = ''
        self.data = ''
        self.previous_data = ''
        self.ui = regexTesterUi.Ui_Dialog()
        self.ui.setupUi(self)
        self.highlighter = MyHighlighter(self.ui.textEdit_Data)

    @pyqtSlot(int)
    def on_checkBox_CI_stateChanged(self, value):
        if self.ui.checkBox_CI.isChecked():
            self.CI = True
        else:
            self.CI = False
        self.matchData()

    @pyqtSlot(int)
    def on_checkBox_MB_stateChanged(self, value):
        if self.ui.checkBox_MB.isChecked():
            self.MB = True
        else:
            self.MB = False
        self.matchData()
            
    @pyqtSlot(int)
    def on_checkBox_DM_stateChanged(self, value):
        if self.ui.checkBox_DM.isChecked():
            self.DM = True
        else:
            self.DM = False
        self.matchData()
    
    @pyqtSlot()                                                  # 该装饰器标志此函数为接收信号的槽函数
    def on_textEdit_Regex_textChanged(self):                            # 槽函数名标准格式 【on_控件名字_信号函数名字】，表示这个函数接收该控件的信号
        self.regex = (self.ui.textEdit_Regex.toPlainText())
        self.matchData()
    
    @pyqtSlot()
    def on_textEdit_Data_textChanged(self):
        self.data = (self.ui.textEdit_Data.toPlainText())
        if self.data != self.previous_data:
            self.previous_data = self.data
            self.matchData()

    def matchData(self):
        if (not self.CI) and (not self.MB) and (not self.DM):
            pattern = re.compile(self.regex)
        elif (not self.CI) and (not self.MB) and (self.DM):
            pattern = re.compile(self.regex, re.S)
        elif (not self.CI) and (self.MB) and (not self.DM):
            pattern = re.compile(self.regex, re.M)
        elif (not self.CI) and (self.MB) and (self.DM):
            pattern = re.compile(self.regex, re.M|re.S)
        elif (self.CI) and (not self.MB) and (not self.DM):
            pattern = re.compile(self.regex, re.I)
        elif (self.CI) and (not self.MB) and (self.DM):
            pattern = re.compile(self.regex, re.I|re.S)
        elif (self.CI) and (self.MB) and (not self.DM):
            pattern = re.compile(self.regex, re.I|re.M)
        elif (self.CI) and (self.MB) and (self.DM):
            pattern = re.compile(self.regex, re.I|re.M|re.S)
        
        dataMatched = re.findall(pattern, self.data)
        self.highlighter.setHighlightData(dataMatched)
        self.highlighter.rehighlight()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = RegexTesterDialog()
    dialog.show()
    sys.exit(app.exec_())
    