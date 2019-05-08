# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
 
class Form(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = uic.loadUi("tutorial1.ui")
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())