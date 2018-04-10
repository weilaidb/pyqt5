from __future__ import division
import  sys
from math import  *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
# from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget

class Form(QWidget):
    version = "1.2"
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.browser = QTextBrowser()
        self.lineedit = QLineEdit("Type an expression and press Enter")
        self.lineedit.selectAll()
        self.clearlineptn = QPushButton("clear line")
        self.selectptn = QPushButton("select all")
        self.clearbroswerptn = QPushButton("clear broswer")
        self.versionptn = QPushButton("about")
        self.setptnsize(self.selectptn)
        self.setptnsize(self.clearbroswerptn)
        self.setptnsize(self.versionptn)
        self.setptnsize(self.clearlineptn)
        ptnlayout = QHBoxLayout()
        ptnlayout.addWidget(self.clearlineptn)
        ptnlayout.addWidget(self.selectptn)
        ptnlayout.addWidget(self.clearbroswerptn)
        ptnlayout.addWidget(self.versionptn)
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        layout.addLayout(ptnlayout)
        self.setLayout(layout)
        self.lineedit.setFocus()
        self.lineedit.returnPressed.connect(self.updateUi)
        self.selectptn.clicked.connect(self.selectall)
        self.clearlineptn.clicked.connect(self.clearline)
        self.clearbroswerptn.clicked.connect(self.clearbroswer)
        self.versionptn.clicked.connect(self.showversion)
        self.setWindowTitle("Calculate")
        self.setGeometry(300, 300, 800, 600)
        self.center()
        self.show()

    def setptnsize(self, btn):
        btn.setMinimumHeight(50)

    def updateUi(self):
        try:
            text = (self.lineedit.text())
            self.browser.append("%s= <b><font color=red>%s</font></b>" % (text, eval(text)))
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>" % text)

    def selectall(self):
        try:
            self.lineedit.selectAll()
            self.lineedit.setFocus()
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>")

    def clearbroswer(self):
        try:
            self.browser.clear()
            self.selectall()
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>")

    def clearline(self):
        try:
            self.lineedit.clear()
            self.selectall()
        except:
            self.browser.append(
                "<font color=red>%s is invalid!</font>")

    def showversion(self):
        eply = QMessageBox.information(self,  # 使用infomation信息框
                                       "版本",
                                       "%s" % self.version,
                                       QMessageBox.Yes)


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


app = QApplication(sys.argv)
form = Form()
form.show()
app.exec_()












