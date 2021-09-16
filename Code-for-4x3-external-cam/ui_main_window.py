# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\dell\Desktop\its__done\ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1280, 635)
        self.numlabel = QtWidgets.QLabel(Form)
        self.numlabel.setGeometry(QtCore.QRect(740, 520, 121, 71))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.numlabel.setFont(font)
        self.numlabel.setText("")
        self.numlabel.setObjectName("numlabel")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(530, 530, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.image_label = QtWidgets.QLabel(Form)
        self.image_label.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.image_label.setText("")
        self.image_label.setObjectName("image_label")
        self.control_bt = QtWidgets.QPushButton(Form)
        self.control_bt.setGeometry(QtCore.QRect(50, 530, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.control_bt.setFont(font)
        self.control_bt.setObjectName("control_bt")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(280, 530, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.image_label_2 = QtWidgets.QLabel(Form)
        self.image_label_2.setGeometry(QtCore.QRect(640, 0, 640, 480))
        self.image_label_2.setText("")
        self.image_label_2.setObjectName("image_label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Cam_4_3"))
        self.label_3.setText(_translate("Form", "the numbers of people"))
        self.control_bt.setText(_translate("Form", "Start"))
        self.pushButton.setText(_translate("Form", "Process"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

