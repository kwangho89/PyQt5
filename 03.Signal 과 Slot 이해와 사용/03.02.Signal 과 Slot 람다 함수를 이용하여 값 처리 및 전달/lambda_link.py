# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("lambda_link.ui")
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())