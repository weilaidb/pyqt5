# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'codesophia.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CodeSophia(object):
    def setupUi(self, CodeSophia):
        CodeSophia.setObjectName("CodeSophia")
        CodeSophia.resize(800, 600)
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        CodeSophia.setFont(font)
        self.centralwidget = QtWidgets.QWidget(CodeSophia)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textEdit_key = QtWidgets.QTextEdit(self.frame)
        self.textEdit_key.setObjectName("textEdit_key")
        self.gridLayout_2.addWidget(self.textEdit_key, 1, 0, 1, 1)
        self.textEdit_result = QtWidgets.QTextEdit(self.frame)
        self.textEdit_result.setObjectName("textEdit_result")
        self.gridLayout_2.addWidget(self.textEdit_result, 1, 4, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_leftclear = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_leftclear.sizePolicy().hasHeightForWidth())
        self.pushButton_leftclear.setSizePolicy(sizePolicy)
        self.pushButton_leftclear.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_leftclear.setObjectName("pushButton_leftclear")
        self.verticalLayout.addWidget(self.pushButton_leftclear)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_rightclear = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_rightclear.sizePolicy().hasHeightForWidth())
        self.pushButton_rightclear.setSizePolicy(sizePolicy)
        self.pushButton_rightclear.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_rightclear.setObjectName("pushButton_rightclear")
        self.verticalLayout.addWidget(self.pushButton_rightclear)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_gen = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_gen.sizePolicy().hasHeightForWidth())
        self.pushButton_gen.setSizePolicy(sizePolicy)
        self.pushButton_gen.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_gen.setObjectName("pushButton_gen")
        self.verticalLayout.addWidget(self.pushButton_gen)
        self.pushButton_load = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_load.sizePolicy().hasHeightForWidth())
        self.pushButton_load.setSizePolicy(sizePolicy)
        self.pushButton_load.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_load.setObjectName("pushButton_load")
        self.verticalLayout.addWidget(self.pushButton_load)
        self.checkBox_showFunc = QtWidgets.QCheckBox(self.frame)
        self.checkBox_showFunc.setObjectName("checkBox_showFunc")
        self.verticalLayout.addWidget(self.checkBox_showFunc)
        self.checkBox_showAllText = QtWidgets.QCheckBox(self.frame)
        self.checkBox_showAllText.setObjectName("checkBox_showAllText")
        self.verticalLayout.addWidget(self.checkBox_showAllText)
        self.pushButton_paster2left = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_paster2left.sizePolicy().hasHeightForWidth())
        self.pushButton_paster2left.setSizePolicy(sizePolicy)
        self.pushButton_paster2left.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_paster2left.setObjectName("pushButton_paster2left")
        self.verticalLayout.addWidget(self.pushButton_paster2left)
        self.pushButton_fetchright = QtWidgets.QPushButton(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_fetchright.sizePolicy().hasHeightForWidth())
        self.pushButton_fetchright.setSizePolicy(sizePolicy)
        self.pushButton_fetchright.setMinimumSize(QtCore.QSize(50, 0))
        self.pushButton_fetchright.setObjectName("pushButton_fetchright")
        self.verticalLayout.addWidget(self.pushButton_fetchright)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.gridLayout_2.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.comboBox_keytips = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_keytips.setFont(font)
        self.comboBox_keytips.setMaxVisibleItems(50)
        self.comboBox_keytips.setObjectName("comboBox_keytips")
        self.gridLayout_2.addWidget(self.comboBox_keytips, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_print = QtWidgets.QLabel(self.frame)
        self.label_print.setObjectName("label_print")
        self.horizontalLayout.addWidget(self.label_print)
        self.lineEdit_print = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_print.setObjectName("lineEdit_print")
        self.horizontalLayout.addWidget(self.lineEdit_print)
        self.comboBox_print = QtWidgets.QComboBox(self.frame)
        self.comboBox_print.setEditable(True)
        self.comboBox_print.setObjectName("comboBox_print")
        self.horizontalLayout.addWidget(self.comboBox_print)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label_dataprint = QtWidgets.QLabel(self.frame)
        self.label_dataprint.setObjectName("label_dataprint")
        self.horizontalLayout.addWidget(self.label_dataprint)
        self.lineEdit_dataprint = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_dataprint.setObjectName("lineEdit_dataprint")
        self.horizontalLayout.addWidget(self.lineEdit_dataprint)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 4, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        CodeSophia.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CodeSophia)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        CodeSophia.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CodeSophia)
        self.statusbar.setObjectName("statusbar")
        CodeSophia.setStatusBar(self.statusbar)
        self.action_declare = QtWidgets.QAction(CodeSophia)
        self.action_declare.setObjectName("action_declare")
        self.action_fucntion = QtWidgets.QAction(CodeSophia)
        self.action_fucntion.setObjectName("action_fucntion")
        self.action_define = QtWidgets.QAction(CodeSophia)
        self.action_define.setObjectName("action_define")
        self.action_struct = QtWidgets.QAction(CodeSophia)
        self.action_struct.setObjectName("action_struct")
        self.action_structprint = QtWidgets.QAction(CodeSophia)
        self.action_structprint.setObjectName("action_structprint")
        self.actionCPP = QtWidgets.QAction(CodeSophia)
        self.actionCPP.setObjectName("actionCPP")
        self.actionJAVA = QtWidgets.QAction(CodeSophia)
        self.actionJAVA.setObjectName("actionJAVA")
        self.actionSHELL = QtWidgets.QAction(CodeSophia)
        self.actionSHELL.setObjectName("actionSHELL")
        self.action = QtWidgets.QAction(CodeSophia)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(CodeSophia)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(CodeSophia)
        self.action_3.setObjectName("action_3")
        self.action_6 = QtWidgets.QAction(CodeSophia)
        self.action_6.setObjectName("action_6")
        self.action_7 = QtWidgets.QAction(CodeSophia)
        self.action_7.setObjectName("action_7")
        self.action_save = QtWidgets.QAction(CodeSophia)
        self.action_save.setObjectName("action_save")
        self.actionC_2 = QtWidgets.QAction(CodeSophia)
        self.actionC_2.setObjectName("actionC_2")
        self.action_header = QtWidgets.QAction(CodeSophia)
        self.action_header.setObjectName("action_header")
        self.action_ifcondition = QtWidgets.QAction(CodeSophia)
        self.action_ifcondition.setObjectName("action_ifcondition")
        self.action_loop = QtWidgets.QAction(CodeSophia)
        self.action_loop.setObjectName("action_loop")
        self.action_note = QtWidgets.QAction(CodeSophia)
        self.action_note.setObjectName("action_note")
        self.action_common_print = QtWidgets.QAction(CodeSophia)
        self.action_common_print.setObjectName("action_common_print")
        self.menu.addAction(self.action_header)
        self.menu.addAction(self.action_declare)
        self.menu.addAction(self.action_fucntion)
        self.menu.addAction(self.action_define)
        self.menu.addAction(self.action_struct)
        self.menu.addAction(self.action_structprint)
        self.menu.addAction(self.action_ifcondition)
        self.menu.addAction(self.action_loop)
        self.menu.addAction(self.action_note)
        self.menu.addSeparator()
        self.menu.addAction(self.action_common_print)
        self.menu_2.addAction(self.actionC_2)
        self.menu_2.addAction(self.actionCPP)
        self.menu_2.addAction(self.actionJAVA)
        self.menu_2.addAction(self.actionSHELL)
        self.menu_3.addAction(self.action_save)
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(CodeSophia)
        QtCore.QMetaObject.connectSlotsByName(CodeSophia)

    def retranslateUi(self, CodeSophia):
        _translate = QtCore.QCoreApplication.translate
        CodeSophia.setWindowTitle(_translate("CodeSophia", "CodeSophia"))
        self.pushButton_leftclear.setText(_translate("CodeSophia", "左清空"))
        self.pushButton_rightclear.setText(_translate("CodeSophia", "右清空"))
        self.pushButton_gen.setText(_translate("CodeSophia", "生成"))
        self.pushButton_load.setText(_translate("CodeSophia", "加载结果"))
        self.checkBox_showFunc.setText(_translate("CodeSophia", "函数名"))
        self.checkBox_showAllText.setText(_translate("CodeSophia", "全文本"))
        self.pushButton_paster2left.setText(_translate("CodeSophia", "贴左<-"))
        self.pushButton_fetchright.setText(_translate("CodeSophia", "取右->"))
        self.label_print.setText(_translate("CodeSophia", "打印函数"))
        self.label_dataprint.setText(_translate("CodeSophia", "打印数据"))
        self.menu.setTitle(_translate("CodeSophia", "功能"))
        self.menu_2.setTitle(_translate("CodeSophia", "语言"))
        self.menu_3.setTitle(_translate("CodeSophia", "结果"))
        self.action_declare.setText(_translate("CodeSophia", "声明"))
        self.action_fucntion.setText(_translate("CodeSophia", "函数"))
        self.action_define.setText(_translate("CodeSophia", "宏"))
        self.action_struct.setText(_translate("CodeSophia", "结构体"))
        self.action_structprint.setText(_translate("CodeSophia", "结构体打印"))
        self.actionCPP.setText(_translate("CodeSophia", "C++"))
        self.actionJAVA.setText(_translate("CodeSophia", "JAVA"))
        self.actionSHELL.setText(_translate("CodeSophia", "SHELL"))
        self.action.setText(_translate("CodeSophia", "头文件"))
        self.action_2.setText(_translate("CodeSophia", "注释"))
        self.action_3.setText(_translate("CodeSophia", "声明"))
        self.action_6.setText(_translate("CodeSophia", "宏"))
        self.action_7.setText(_translate("CodeSophia", "函数"))
        self.action_save.setText(_translate("CodeSophia", "保存"))
        self.actionC_2.setText(_translate("CodeSophia", "C"))
        self.action_header.setText(_translate("CodeSophia", "头文件"))
        self.action_ifcondition.setText(_translate("CodeSophia", "条件"))
        self.action_loop.setText(_translate("CodeSophia", "循环"))
        self.action_note.setText(_translate("CodeSophia", "注释"))
        self.action_common_print.setText(_translate("CodeSophia", "打印"))

