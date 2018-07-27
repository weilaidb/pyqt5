# -*- coding: utf-8 -*-

"""
Module implementing Dialog.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QDialog

from Ui_HelloWindow import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Dialog, self).__init__(parent)
        self.setupUi(self)
        
    @pyqtSlot()
    def on_pushButton_ok_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label.setText('ok Hello world!')
		self.label.setText('nihaoma')
        
    @pyqtSlot()
    def on_pushButton_cancle_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label.setText('cancle, Hello world!')
    
    @pyqtSlot()
    def on_pushButton_exit_clicked(self):
        """
        Slot documentation goes here.
        """
        # TODO: not implemented yet
        self.label.setText('exit Hello world!')
        exit()
        




if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
    
 
