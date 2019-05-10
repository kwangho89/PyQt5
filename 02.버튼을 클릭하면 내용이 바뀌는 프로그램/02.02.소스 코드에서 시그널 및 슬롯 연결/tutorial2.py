# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
from PyQt5 import uic
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
 
 
class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("tutorial2.ui", self)
 
    @pyqtSlot()
    def slot_1st(self):
        self.ui.lb.setText("첫번째 버튼")
 
    @pyqtSlot()
    def slot_2nd(self):
        self.ui.lb.setText("두번째 버튼")
 
    @pyqtSlot()
    def slot_3rd(self):
        self.ui.lb.setText("세번째 버튼")
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    w.ui.show()
    sys.exit(app.exec())