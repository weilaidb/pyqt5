# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import platform
import sys
import html
# from PyQt5.QtCore import QSize, Qt,pyqtSignal
# from PyQt5.QtGui import QColor, QFont,QFontMetrics, QIcon, QKeySequence, QPixmap,QTextCharFormat
# from PyQt5.QtWidgets import QAction,QApplication,QMenu,QTextEdit
#

from Ui_automyccode import *
from dbApi import *
import pyperclip
import os


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    global variable
    """
    namelist, contents = [],[]
    versionnum = 1.9

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
        # 设置窗口的图标，引用当前目录下的web.png图片
        if(os.path.exists("web.png")):
            print("web.png exist")
        else:
            print("web.png no exist!")
        # self.setWindowIcon(QIcon('web.png'))
        self.setWindowIcon(QIcon('akregator.png'))

        # computer_item->setIcon(QIcon(":/res/pix/computer.png"));

        # self.actionSearchText.setShortCut()
        self.actionSearchText.setShortcut('Ctrl+F')  # shortcut key
        self.actionSearchText.triggered.connect(self.searchtext)


    def aboutVersion(self):
        self.statusBar.showMessage("数据库版本V%s"% self.versionnum)

    def showtipsinfo(self):
        # self.textEdit_showresult.setText("")
        self.lineEdit_search.setPlaceholderText("请输入搜索关键字")

    def insert2db(self):
        pass

    def showresult(self):


        pass

    # @pyqtSlot()
    def toSimpleHtml(self):
        htmltext = ""
        black = QColor(Qt.black)
        block = self.textEdit_showresult.document().begin()
        while block.isValid():
            iterator = block.begin()
            while iterator != block.end():
                fragment = iterator.fragment()
                if fragment.isValid():
                    format = fragment.charFormat()
                    family = format.fontFamily()
                    color = format.foreground().color()
                    text=html.escape(fragment.text())
                    if (format.verticalAlignment() ==
                        QTextCharFormat.AlignSubScript):
                        text = "<sub>{0}</sub>".format(text)
                    elif (format.verticalAlignment() ==
                          QTextCharFormat.AlignSuperScript):
                        text = "<sup>{0}</sup>".format(text)
                    if format.fontUnderline():
                        text = "<u>{0}</u>".format(text)
                    if format.fontItalic():
                        text = "<i>{0}</i>".format(text)
                    if format.fontWeight() > QFont.Normal:
                        text = "<b>{0}</b>".format(text)
                    if format.fontStrikeOut():
                        text = "<s>{0}</s>".format(text)
                    if color != black or family:
                        attribs = ""
                        if color != black:
                            attribs += ' color="{0}"'.format(color.name())
                        if family:
                            attribs += ' face="{0}"'.format(family)
                        text = "<font{0}>{1}</font>".format(attribs,text)
                    htmltext += text
                iterator += 1
            block = block.next()
        return htmltext


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

        cursor = self.textEdit_inserttext.textCursor()
        selectext = cursor.selectedText()

        if(len(content.strip()) == 0):
            print("content len 0")
            return
        if(len(content) > 100 and (len(selectext.strip()) == 0)) :
            name = content.lstrip()[0:100]
        elif(len(selectext.strip()) != 0):
            name = selectext[0:100]
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

    def getSearchText(self):
        return self.lineEdit_search.text().strip()

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
            maxline = 3
            if (len(splitlist) >= maxline):
                showheight = maxline
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

    @pyqtSlot(QTextEdit)
    def printout(lineedit):
        print(str(lineedit.toHtml()))
        print(str(lineedit.toPlainText()))
        print(str(lineedit.toSimpleHtml()))

    @pyqtSlot(int)
    def on_listWidget_search_currentRowChanged(self, currentRow):
        """
        Slot documentation goes here.
        
        @param currentRow DESCRIPTION
        @type int
        """
        print(currentRow)
        print("search text:", self.getSearchText())
        keyword = self.getSearchText()
        rowcontent = self.contents[currentRow]
        rowcontent2 = self.contents[currentRow]
        # if keyword in rowcontent:
        #     print("in it ")
        #     # rowcontent = rowcontent.replace(keyword, "<h1>" + keyword + "</h1>")
        #     rowcontent = rowcontent.replace("\t", "    ")
        #     rowcontent = rowcontent.replace(keyword, "<font color=\"red\">" + keyword + "</font>")
        #     rowcontent = rowcontent.replace("\n", "<p>" + "\n" + "</p>")
        #     # rowcontent = rowcontent.replace(" ", "&nbsp")

        print("after deal rowcontent:", rowcontent)

        def normalOutputWritten(self, text):
            """Append text to the QTextEdit."""
            # Maybe QTextEdit.append() works as well, but this is how I do it:
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QTextCursor.End)
            cursor.insertText(text)
            self.textEdit.setTextCursor(cursor)
            self.textEdit.ensureCursorVisible()

        to_find_text = rowcontent2

        if(currentRow >= 0):
            # self.textEdit_showresult.setText(self.contents[currentRow])
            self.textEdit_showresult.setText(to_find_text)
            find_cursor = self.textEdit_showresult.textCursor()
            plainFormat = find_cursor.charFormat()
            colorFormat = plainFormat
            colorFormat.setForeground(Qt.blue)
            print("colorFormat:", colorFormat)
            self.textEdit_showresult.mergeCurrentCharFormat(colorFormat)
            self.textEdit_showresult.update()
            return


            document = self.textEdit_showresult.document()
            cursor = QTextCursor(document)
            # cursor.insertImage("./testimage.png")
            f = cursor.charFormat()
            print(f)

            prop_id = 0x100000 + 1
            f.setProperty(prop_id, 100)
            print(f.intProperty(prop_id))
            print('------')

            block = document.firstBlock()
            while block.length() > 0:
                print(block)
                it = block.begin()
                while not it.atEnd():
                    f = it.fragment()
                    fmt = f.charFormat()
                    print(fmt)
                    print(fmt.intProperty(prop_id))
                    it += 1
                block = block.next()

            # colorFormat.setForeground(Qt::red)
            #
            #
            # while (ui->textEdit->find(to_find_text, QTextDocument::FindBackward)){
            #
            # QTextCharFormat
            # QTextCharFormat colorFormat = plainFormat;
            # colorFormat.setForeground(Qt::red);
            # ui->textEdit->mergeCurrentCharFormat(colorFormat);
            # // QPalette
            # palette = ui->textEdit->palette();
            # // palette.setColor(QPalette::Highlight, QColor(107, 194, 53));
            # // ui->textEdit->setPalette(palette);
            # }

        # app = QApplication(sys.argv)
        # lineedit = RichTextLineEdit()
        # lineedit.returnPressed.connect(lambda: printout(lineedit))
        # self.textEdit_showresult.textChanged.connect(lambda: printout(self.textEdit_showresult))
        # self.textEdit_showresult.returnPressed.connect(lambda: printout(self.textEdit_showresult))


        return
        htmlbody = "<html><body>" + rowcontent + "</body></html>"



        if(currentRow >= 0):
            # self.textEdit_showresult.setText(self.contents[currentRow])
            self.textEdit_showresult.setText(htmlbody)
            # self.textEdit_showresult.setText(rowcontent)
            # self.textEdit_showresult.update()
            # htmltext = self.toSimpleHtml()
            # print("after deal htmltext22222 is:", htmltext)
            # self.textEdit_showresult.setText(htmltext)

            # self.textEdit_showresult.toSimpleHtml()
            # self.
            # self.textEdit_showresult.setText(htmlbody)

    @pyqtSlot()
    def on_pushButton_searchclean_clicked(self):
        """
        Slot documentation goes here.
        """
        self.showresultbyText("")
        self.lineEdit_search.setText("")
        self.lineEdit_search.setFocus()

    @pyqtSlot()
    def on_actionSearchText_triggered(self):
        """
        Slot documentation goes here.
        """

        self.lineEdit_search.setFocus()

    def searchtext(self):
        self.lineEdit_search.setFocus()
        self.lineEdit_search.clear()

    @pyqtSlot()
    def on_textEdit_showresult_textChanged(self):
        """
        Slot documentation goes here.
        """
        pass


    @pyqtSlot(bool)
    def on_textEdit_showresult_copyAvailable(self, b):
        """
        Slot documentation goes here.

        @param b DESCRIPTION
        @type bool
        """
        pass