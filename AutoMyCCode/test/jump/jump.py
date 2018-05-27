import sys
from PyQt5 import QtWidgets
from j1 import Ui_Form
from j2 import Ui_Form as u2
from j2dialog import Ui_Dialog


class Mywindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def jump2(self):
        m2 = W2()
        m2.exec_()


class Window2(QtWidgets.QWidget, u2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


class W2(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Mywindow()
    main.show()
    sys.exit(app.exec_())