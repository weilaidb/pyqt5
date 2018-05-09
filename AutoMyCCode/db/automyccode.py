# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from Ui_automyccode import *
from dbApi import *
import pyperclip


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    global variable
    """
    namelist, contents = [],[]
    versionnum = 1.1

    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.timer = QTimer(self)  # 初始化一个定时器
        self.timer.timeout.connect(self.operate)  # 计时结束调用operate()方法
        # self.timer.start(2000)  # 设置计时间隔并启动
        self.aboutVersion()
        self.showtipsinfo()

    def aboutVersion(self):
        self.statusBar.showMessage("数据库版本V%s"% self.versionnum)

    def showtipsinfo(self):
        # self.textEdit_showresult.setText("")
        self.lineEdit_search.setPlaceholderText("请输入搜索关键字")

    def insert2db(self):
        pass


    def showresult(self):


        pass

    @pyqtSlot()
    def showinsertUI(self):
        self.listWidget_search.hide()
        self.textEdit_inserttext.show()


    @pyqtSlot()
    def on_pushButton_insert_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showinsertUI()
        print("insert 2 db")
        content = self.textEdit_inserttext.toPlainText()
        # print(content)
        name = ""

        if(len(content.strip()) == 0):
            print("content len 0")
            return
        if(len(content) > 100) :
            name = content.lstrip()[0:100]
        else:
            name = content

        retval = default_insert_contetNameWithTime(data=(name, content))
        if(retval != 0xFFFF):
            self.statusBar.showMessage("成功")
        elif (retval == 0xFFFF):
            # print("aaa")
            self.statusBar.showMessage("数据库未开启，请开启数据库")
            return
        else:
            self.statusBar.showMessage("失败")

        self.timer.start(2000)

    def showresultbyText(self,text):
        self.lineEdit_search.setText(text)
        self.on_lineEdit_search_returnPressed()
        searchtext = self.lineEdit_search.text()
        if(len(searchtext.strip()) == 0):
            self.textEdit_showresult.setText("")
            self.listWidget_search.clear()
            self.lineEdit_search.setText("")

    @pyqtSlot()
    def on_pushButton_showresult_clicked(self):
        """
        Slot documentation goes here.
        """
        print("show result")
        self.showresultbyText(pyperclip.paste())
    
    @pyqtSlot()
    def on_pushButton_clean_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showinsertUI()
        self.textEdit_inserttext.setText("")
    
    @pyqtSlot()
    def on_pushButton_paste_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showinsertUI()
        self.textEdit_inserttext.setText(pyperclip.paste())

    def operate(self):
        #具体操作
        self.statusBar.showMessage("")
        self.timer.stop()
    
    @pyqtSlot()
    def on_lineEdit_search_returnPressed(self):
        """
        Slot documentation goes here.
        """
        print("lineedit search return pressed")
        searchtext = self.lineEdit_search.text()
        if(len(searchtext.strip()) == 0):
            self.textEdit_showresult.setText("")
            self.listWidget_search.clear()
            self.lineEdit_search.setText("")
            return
        print(searchtext)
        self.namelist.clear()
        self.contents.clear()
        retval,self.namelist, self.contents = default_search_contetName(data=(searchtext.strip()))
        if(retval and self.namelist[0] != 0xFFFF):
            self.statusBar.showMessage("查找到数据条数:%d" % retval)
        elif (retval == 0xFFFF and self.namelist[0] == 0xFFFF and self.contents[0] == 0xFFFF):
            # print("aaa")
            self.statusBar.showMessage("数据库未开启，请开启数据库")
            return
        else:
            self.statusBar.showMessage("未查到数据")
            self.namelist.clear()
            self.contents.clear()
            self.listWidget_search.clear()
            return

        showtxtresult = ""

        self.listWidget_search.clear()
        self.listWidget_search.show()
        self.textEdit_inserttext.hide()
        for i in range(0,len(self.namelist)):
            # print(i)
            # print(namelist[i][0])
            # showtxtresult += "<h2>" + namelist[i][0] + "</h2>"
            # showtxtresult += '\n\n'
            splitlist = self.namelist[i].split("\n")
            print(splitlist)
            print(len(splitlist))
            showheight = 0
            if (len(splitlist) >= 4):
                showheight = 4
            else:
                showheight = len(splitlist)
            if (showheight == 0):
                showheight = 1

            print(showheight)

            itemnamestring = ""
            for i in range(0,showheight):
                print(splitlist[i])
                itemnamestring += splitlist[i]
                if(i > 0 and i + 1 < showheight):
                    itemnamestring += '\n'
                # itemnamelist.append(splitlist[i] + '\n')
                # print(self.namelist[i])

            print(itemnamestring)
            self.listWidget_search.addItem(itemnamestring)
            # self.listWidget_search.addItem(self.namelist[i])

        # self.textEdit_showresult.setText(showtxtresult)
        self.timer.start(2000)
    
    @pyqtSlot(QModelIndex)
    def on_listWidget_search_clicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        # print(index)
        # print(type(index))
        # self.textEdit_showresult.setText(self.contents[index])
        pass


    
    @pyqtSlot(QModelIndex)
    def on_listWidget_search_doubleClicked(self, index):
        """
        Slot documentation goes here.
        
        @param index DESCRIPTION
        @type QModelIndex
        """
        pass
    
    @pyqtSlot(int)
    def on_listWidget_search_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.
        
        @param currentRow DESCRIPTION
        @type int
        """
        print(currentRow)
        self.textEdit_showresult.setText(self.contents[currentRow])
    
    @pyqtSlot()
    def on_pushButton_searchclean_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showresultbyText("")
