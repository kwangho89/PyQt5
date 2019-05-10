# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QWidget 
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic
 
class Form(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.ui = uic.loadUi("dial_wo.ui")
        # 아래가 시그널/슬롯을 연결하는 구문이다.
        self.ui.dial.valueChanged.connect(self.ui.horizontalSlider.setValue)
        self.ui.horizontalSlider.valueChanged.connect(self.ui.dial.setValue)
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Form()
    form.ui.show()
    sys.exit(app.exec_())