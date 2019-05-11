# -*- coding: utf-8 -*-
import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QThread
import time

class Tic_generator(QThread):
    tic = pyqtSignal(name="Tic")
    
    def __init__(self):
        QThread.__init__(self)
        
    def __del__(self):
        self.wait()
        
    def run(self):
        while True:
            t = int(time.time())
            if not t % 5 == 0:
                self.usleep(1)
                continue
            self.Tic.emit()
            self.msleep(1000)
    
    

class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("lambda.ui")
        self.ui.horizontalSlider.valueChanged.connect(self.ui.label.setNum)
    
if __name__=='__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())