# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tutorial2.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 290)
        self.verticalLayoutWidget = QtWidgets.QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 381, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lb.setFont(font)
        self.lb.setAlignment(QtCore.Qt.AlignCenter)
        self.lb.setObjectName("lb")
        self.verticalLayout.addWidget(self.lb)
        self.le = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.le.setObjectName("le")
        self.verticalLayout.addWidget(self.le)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_1.setObjectName("pb_1")
        self.horizontalLayout.addWidget(self.pb_1)
        self.pb_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_2.setObjectName("pb_2")
        self.horizontalLayout.addWidget(self.pb_2)
        self.pb_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pb_3.setObjectName("pb_3")
        self.horizontalLayout.addWidget(self.pb_3)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.pb_1.clicked.connect(Dialog.pb_slot1)
        self.pb_2.clicked.connect(Dialog.pb_slot2)
        self.pb_3.clicked.connect(Dialog.pb_slot3)
        self.le.textChanged['QString'].connect(self.lb.setText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.lb.setText(_translate("Dialog", "여기에 출력됩니다."))
        self.pb_1.setText(_translate("Dialog", "첫번째 버튼"))
        self.pb_2.setText(_translate("Dialog", "두번째 버튼"))
        self.pb_3.setText(_translate("Dialog", "세번째 버튼"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
