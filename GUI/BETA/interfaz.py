from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from pathlib import Path

class Ui_Dialog(QMainWindow):

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 386)
        Dialog.setStyleSheet("background-color: #3a3e47")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 30, 171, 51))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    font: 10pt\"Century Gothic\";\n"
"    color: #f2b824;\n"
"    background-color: #1d1c21;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #f2c44e;\n"
"    background-color: #3a3c42;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #eb7b13;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 120, 171, 51))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    font: 10pt\"Century Gothic\";\n"
"    color: #f2b824;\n"
"    background-color: #1d1c21;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #f2c44e;\n"
"    background-color: #3a3c42;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #eb7b13;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 210, 291, 131))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    font: 18pt\"Century Gothic\";\n"
"    color: #f2b824;\n"
"    background-color: #1d1c21;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    color: #f2c44e;\n"
"    background-color: #3a3c42;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    color: #eb7b13;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(190, 40, 191, 31))
        self.label.setStyleSheet("color: #ccc;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(190, 130, 191, 31))
        self.label_2.setStyleSheet("color: #ccc;\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "ВВОДИТЬ КАРТУ"))
        self.pushButton_2.setText(_translate("Dialog", "ВВОДИТЬ ЛЕГЕНДУ"))
        self.pushButton_3.setText(_translate("Dialog", "АНАЛИЗИРОВАТЬ"))

    def browse_image(self):
        fname = QFileDialog.getOpenFileName(self, 'Открывайте карту', 'c:\\',"Image files (*.jpg *.png)")
        # self.fname = fname
        return fname

    def browse_folder(self):
        dname = QFileDialog.getExistingDirectory()
        # self.fname = fname
        return dname
