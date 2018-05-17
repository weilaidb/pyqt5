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
import re
# from PyQt5.QtCore import QSize, Qt,pyqtSignal
# from PyQt5.QtGui import QColor, QFont,QFontMetrics, QIcon, QKeySequence, QPixmap,QTextCharFormat
# from PyQt5.QtWidgets import QAction,QApplication,QMenu,QTextEdit
#

from Ui_automyccode import *
from dbApi import *
import pyperclip
import os

# 将一个字符串变量转换成raw字符串：
escape_dict = {'\a': r'\a',
               '\b': r'\b',
               '\c': r'\c',
               '\f': r'\f',
               '\n': r'\n',
               '\r': r'\r',
               '\t': r'\t',
               '\v': r'\v',
               '\'': r'\'',
               '\"': r'\"',
               '\0': r'\0',
               '\1': r'\1',
               '\2': r'\2',
               '\3': r'\3',
               '\4': r'\4',
               '\5': r'\5',
               '\6': r'\6',
               '\7': r'\7',
               '\8': r'\8',
               '\9': r'\9'}


def raw(text):  # 将每个可能的转义字符都进行了替换
    """Returns a raw string representation of text"""
    new_string = ''
    for char in text:
        try:
            new_string += escape_dict[char]
        except KeyError:
            new_string += char
    return new_string



class Highlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(Highlighter, self).__init__(parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b",
                           "\\berror\\b" ,
                           "\\bERROR\\b" ,
                           "\\bfailed\\b" ,
                           ]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);




class MyHighlighter(QSyntaxHighlighter):

    def __init__(self, parent):  # parent即绑定的QTextEdit对象
        QSyntaxHighlighter.__init__(self, parent)

        keywordFormat = QTextCharFormat()
        keywordFormat.setForeground(Qt.darkBlue)
        keywordFormat.setFontWeight(QFont.Bold)

        keywordPatterns = ["\\bchar\\b", "\\bclass\\b", "\\bconst\\b",
                "\\bdouble\\b", "\\benum\\b", "\\bexplicit\\b", "\\bfriend\\b",
                "\\binline\\b", "\\bint\\b", "\\blong\\b", "\\bnamespace\\b",
                "\\boperator\\b", "\\bprivate\\b", "\\bprotected\\b",
                "\\bpublic\\b", "\\bshort\\b", "\\bsignals\\b", "\\bsigned\\b",
                "\\bslots\\b", "\\bstatic\\b", "\\bstruct\\b",
                "\\btemplate\\b", "\\btypedef\\b", "\\btypename\\b",
                "\\bunion\\b", "\\bunsigned\\b", "\\bvirtual\\b", "\\bvoid\\b",
                "\\bvolatile\\b",
                           "\\berror\\b" ,
                           "\\bERROR\\b" ,
                           "\\bfailed\\b" ,
                           ]

        self.highlightingRules = [(QRegExp(pattern), keywordFormat)
                for pattern in keywordPatterns]

        classFormat = QTextCharFormat()
        classFormat.setFontWeight(QFont.Bold)
        classFormat.setForeground(Qt.darkMagenta)
        self.highlightingRules.append((QRegExp("\\bQ[A-Za-z]+\\b"),
                classFormat))

        singleLineCommentFormat = QTextCharFormat()
        singleLineCommentFormat.setForeground(Qt.red)
        self.highlightingRules.append((QRegExp("//[^\n]*"),
                singleLineCommentFormat))

        self.multiLineCommentFormat = QTextCharFormat()
        self.multiLineCommentFormat.setForeground(Qt.red)

        quotationFormat = QTextCharFormat()
        quotationFormat.setForeground(Qt.darkGreen)
        self.highlightingRules.append((QRegExp("\".*\""), quotationFormat))

        functionFormat = QTextCharFormat()
        functionFormat.setFontItalic(True)
        functionFormat.setForeground(Qt.blue)
        self.highlightingRules.append((QRegExp("\\b[A-Za-z0-9_]+(?=\\()"),
                functionFormat))

        self.commentStartExpression = QRegExp("/\\*")
        self.commentEndExpression = QRegExp("\\*/")

        #mine defination hight liters
        self.parent = parent
        self.highlight_data = []  # 存储匹配结果的列表

        self.matched_format = QTextCharFormat()  # 定义高亮格式
        brush = QBrush(Qt.yellow, Qt.SolidPattern)
        self.matched_format.setBackground(brush)




    def highlightBlock(self, text):
        for pattern, format in self.highlightingRules:
            expression = QRegExp(pattern)
            index = expression.indexIn(text)
            while index >= 0:
                length = expression.matchedLength()
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        startIndex = 0
        if self.previousBlockState() != 1:
            startIndex = self.commentStartExpression.indexIn(text)

        while startIndex >= 0:
            endIndex = self.commentEndExpression.indexIn(text, startIndex)

            if endIndex == -1:
                self.setCurrentBlockState(1)
                commentLength = len(text) - startIndex
            else:
                commentLength = endIndex - startIndex + self.commentEndExpression.matchedLength()

            self.setFormat(startIndex, commentLength,
                    self.multiLineCommentFormat)
            startIndex = self.commentStartExpression.indexIn(text,
                    startIndex + commentLength);

        #mine definitioin pattern
        index = 0
        length = 0
        for item in self.highlight_data:
            # print("item:", item)
            # print("text:", text)
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
                try:
                    index = text.index(item, index + length)
                    length = len(item)
                    self.setFormat(index, length, self.matched_format)
                except Exception as e:
                    # print("exception:", e)
                    pass

    def setHighlightData(self, highlight_data):
        self.highlight_data = highlight_data




class MainWindow(QMainWindow, Ui_MainWindow):
    """
    global variable
    """
    namelist, contents = [],[]
    versionnum = 2.2
    staticcharformat = 0


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
        # self.showtipsinfo()
        self.showtipsinfoSelf(self.lineEdit_search, ("请输入搜索关键字"))
        self.showtipsinfoSelf(self.textEdit_regexpress, ("请输入替换正则表达式，格式: 查找项+空格+替换项"))
        self.showtipsinfoSelf(self.textEdit_inserttext, ("请输入待处理的数据"))

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

        #high light something
        # self.setupEditor()

        #using my highlighter
        self.CI = False     # case insensitive (i)
        self.MB = True     # ^$ match at line breaks (m)
        self.DM = False     # dot matched all (s)
        self.regex = ''
        self.data = ''
        self.previous_data = ''
        self.highlighter_my = MyHighlighter(self.textEdit_showresult)

        #regex mode ui
        self.hideRegrexModeUi()



    def hideRegrexModeUi(self):
        self.textEdit_regexpress.hide()
        self.pushButton_regular_mode.hide()

    def showRegrexModeUi(self):
        self.textEdit_inserttext.show()
        self.textEdit_regexpress.show()
        self.pushButton_regular_mode.show()

        #hide list widget
        self.listWidget_search.hide()



    def dragEnterEvent(self, event):
        print("dragEnter event")
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.accept()
        else:
            event.ignore()


    def dragMoveEvent(self, event):
        print("dragMove event")
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event):
        print("drop event")
        if event.mimeData().hasFormat("application/x-icon-and-text"):
            data = event.mimeData().data("application/x-icon-and-text")
            stream = QDataStream(data, QIODevice.ReadOnly)
            text = ""
            #stream >> text
            text=stream.readQString()
            self.setText(text)
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def setupEditor(self):
        font = QFont()
        font.setFamily('Courier')
        font.setFixedPitch(True)
        font.setPointSize(10)

        self.editor = QTextEdit()
        self.editor.setFont(font)

        self.highlighter = Highlighter(self.textEdit_showresult.document())

    def aboutVersion(self):
        self.statusBar.showMessage("数据库版本V%s"% self.versionnum)

    def showtipsinfo(self):
        # self.textEdit_showresult.setText("")
        self.lineEdit_search.setPlaceholderText("请输入搜索关键字")

    def showtipsinfoSelf(self,ui, text):
        # self.textEdit_showresult.setText("")
        ui.setPlaceholderText(text)

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
        #hide regrex mode ui
        self.hideRegrexModeUi()

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
            self.statusBar.showMessage("写入成功" + str(retval) + "条")
        elif (retval == 0xFFFF):
            # print("aaa")
            self.statusBar.showMessage("数据库未开启，请开启数据库")
            return
        else:
            self.statusBar.showMessage("失败")

        self.timer.start(2000)

    def showresultbyText(self,text):
        #hide regrex mode ui
        self.hideRegrexModeUi()

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
        #hide regrex mode ui
        self.hideRegrexModeUi()

        self.showinsertUI()
        self.textEdit_inserttext.setText("")

    @pyqtSlot()
    def on_pushButton_paste_clicked(self):
        """
        Slot documentation goes here.
        """
        #hide regrex mode ui
        self.hideRegrexModeUi()

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

        #hide regrex mode ui
        self.hideRegrexModeUi()
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

    ##save old charFormat of textEdit_showresult
    def getshowresultOldCharFormat(self):
        global plainFormat
        if (self.staticcharformat == 0):
            find_cursor = self.textEdit_showresult.textCursor()
            plainFormat = (find_cursor.charFormat())
            self.staticcharformat = 1
        return  plainFormat


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
        print("after deal rowcontent:", rowcontent)
        # self.textEdit_showresult.mergeCurrentCharFormat(self.getshowresultOldCharFormat())

        if(currentRow >= 0):
            self.textEdit_showresult.setText(self.contents[currentRow])
            # self.highlighter.setHighlightData(keyword)
            # self.highlighter.rehighlight()
            return



            self.textEdit_showresult.textCursor().charFormat().setForeground(Qt.black)

            org_cursor = self.textEdit_showresult.textCursor()
            self.textEdit_showresult.textCursor().clearSelection()
            # self.textEdit_showresult.textCursor().clear()
            # selection.cursor.clearSelection();

            to_find_text = self.getSearchText()
            print("to find text:", to_find_text )

            # functionFormat = QTextCharFormat()
            # functionFormat.setFontItalic(True)
            # functionFormat.setForeground(Qt.blue)
            # self.highlightingRules.append((QRegExp("\\b"+to_find_text),
            #                                functionFormat))

            #move cursor to end
            self.textEdit_showresult.moveCursor(QTextCursor.End)
            while (self.textEdit_showresult.find(to_find_text, QTextDocument.FindBackward)):
                print("while loop")
                # self.__lastSearch = (txt, caseSensitive, wholeWord)
                # flags = QTextDocument.FindFlags(QTextDocument.FindBackward)
                # if caseSensitive:
                #     flags |= QTextDocument.FindCaseSensitively
                # if wholeWord:
                #     flags |= QTextDocument.FindWholeWords
                # ok = self.find(txt, flags)

                find_cursor = self.textEdit_showresult.textCursor()
                if(find_cursor.isNull()):
                    continue
                platformat = find_cursor.charFormat()
                # colorFormat = platformat
                colorFormat = (org_cursor.charFormat())
                # colorFormat.setForeground(Qt.blue)

                print("find_cursor:", find_cursor)
                find_cursor.movePosition(QTextCursor.WordRight,
                                         QTextCursor.KeepAnchor)

                self.textEdit_showresult.mergeCurrentCharFormat(colorFormat)

            # self.textEdit_showresult.mergeCurrentCharFormat(self.getshowresultOldCharFormat())

            # {
            # QTextCursor find_cursor=ui->textEdit->textCursor()
            # QTextCharFormat plainFormat(find_cursor.charFormat())
            # QTextCharFormat colorFormat = plainFormat
            # colorFormat.setForeground(Qt::red);
            # ui->textEdit->mergeCurrentCharFormat(colorFormat)
            # }




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
        keyword = self.getSearchText()
        self.regex = keyword
        if(self.regex.strip() == ''):
            return
        self.data = (self.textEdit_showresult.toPlainText())
        print("self.data:", self.data)
        if(self.data.strip() == ''):
            return
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
            pattern = re.compile(self.regex, re.M | re.S)
        elif (self.CI) and (not self.MB) and (not self.DM):
            pattern = re.compile(self.regex, re.I)
        elif (self.CI) and (not self.MB) and (self.DM):
            pattern = re.compile(self.regex, re.I | re.S)
        elif (self.CI) and (self.MB) and (not self.DM):
            pattern = re.compile(self.regex, re.I | re.M)
        elif (self.CI) and (self.MB) and (self.DM):
            pattern = re.compile(self.regex, re.I | re.M | re.S)

        print("pattern:", pattern)
        print("data   :", self.data)
        dataMatched = re.findall(pattern, self.data)
        self.highlighter_my.setHighlightData(dataMatched)
        self.highlighter_my.rehighlight()

    @pyqtSlot(bool)
    def on_textEdit_showresult_copyAvailable(self, b):
        """
        Slot documentation goes here.

        @param b DESCRIPTION
        @type bool
        """
        pass
    
    @pyqtSlot()
    def on_pushButton_insert_quickly_clicked(self):
        """
        Slot documentation goes here.
        """
        self.on_pushButton_paste_clicked()
        self.on_pushButton_insert_clicked()
    
    @pyqtSlot()
    def on_textEdit_regexpress_textChanged(self):
        """
        Slot documentation goes here.
        """
        pass


    @pyqtSlot()
    def on_pushButton_regular_mode_clicked(self):
        """
        Slot documentation goes here.
        """
        # pass
        todotext = self.textEdit_inserttext.toPlainText()
        patterntext = self.textEdit_regexpress.toPlainText()
        splitlists = patterntext.split('\n')
        apattern = []
        bpattern = []
        for sub in splitlists:
            print("sub:", sub)
            insub = re.split(r'\s+',sub)
            print("insub     :", insub)
            print("len(insub):", len(insub))
            if (len(insub) > 1):
                print("re.compile(raw(insub[0]:", re.compile(raw(insub[0])))
                print("raw(insub[1]:", raw(insub[1]))
                apattern.append(re.compile(raw(insub[0])))
                bpattern.append(raw(insub[1]))
            else:
                print("invalid insub !!!")

        print("apattern", apattern)
        print("bpattern", bpattern)

        # ##tuple 必须是初始化完成的，不能直接赋值，使用list
        # combinepattern = [[re.compile(p)
        #                    for p in apattern], bpattern]
        # print("combinepattern", combinepattern)

        #deal text todotext
        # todotext
        loop = 0
        resulttext = todotext
        for pattern in apattern:
            print('Seeking "%s" ->'% pattern)
            print('Replace "%s" ->'% bpattern[loop])
            if(pattern.search(todotext)):
                print('match')
            else:
                print('no match')

            try:
                print("Replace Text:", pattern.sub(bpattern[loop], resulttext))
                resulttext = pattern.sub(bpattern[loop], resulttext)
            except Exception as e:
                print("replace error!,", e)


            loop+=1


        self.textEdit_showresult.setText(resulttext)
        return
        # replaceregexes = ([re.compile(p)
        #                    for p in [raw(t)   for t in patterntext.split('\n')]])
        # patternscombine  = ([p],[w]
        #                    for p, w  in [raw(t.split(r"\s+")[0])   for t in patterntext.split('\n')]])
        #
        # searchpattern  = ([re.compile(p)
        #                    for p in [raw(t.split(r"\s+")[0])   for t in patterntext.split('\n')]])
        # replacepattern = ([w
        #                    for w in [raw(t.split(r"\s+")[1])   for t in patterntext.split('\n')]])
        # print("searchpattern :", searchpattern)
        # print("replacepattern:", replacepattern)
        # print("replaceregexes:", replaceregexes)

        # for sub in replaceregexes:
        #     print("sub:", sub)
        #     insub = sub.split("\\s+")
        #     print("insub size:", insub.count())
    
    @pyqtSlot()
    def on_actionReGex_triggered(self):
        """
        Slot documentation goes here.
        """
        self.showRegrexModeUi()
