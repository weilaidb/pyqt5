import sys
from PyQt5.QtWidgets import QApplication, QWidget
from form1 import Ui_Form1
from form2 import Ui_Form2


class myform1(QWidget, Ui_Form1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def close_w1(self):  # 点击按钮将窗体1关掉
        self.close()


class myform2(QWidget, Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def show_w2(self):  # 显示窗体2
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w1 = myform1()
    w2 = myform2()
    w1.show()
    w1.btn.clicked.connect(w1.close_w1)
    w1.btn.clicked.connect(w2.show_w2)
    app.exec_()

# 没有那么多乱七八糟的东西，还是很简单的。