# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2012, 1081)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-80, -10, 2081, 1081))
        self.label.setStyleSheet("background-color: rgb(170, 168, 149);\n"
                "background-image: url(resources/download (8).jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(-40, 480, 371, 331))
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 40, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(8)
        font.setBold(True)
        font.setItalic(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton#pushButton{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(137,63,3,255);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px:\n"
"    background-color:rgba(140,120,111,255);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(530, 390, 93, 28))
        self.pushButton_2.setStyleSheet("QPushButton#pushButton_2{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(137,63,3,255);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_2:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton_2:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px:\n"
"    background-color:rgba(140,120,111,255);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(480, 180, 601, 111))
        self.label_6.setStyleSheet("color: rgb(92, 64, 51);")
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(21)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(420, 210, 531, 141))
        font = QtGui.QFont()
        font.setFamily("Colonna MT")
        font.setPointSize(44)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(137, 63, 3);")  # Deep Orange-Brown
        self.label_7.setObjectName("label_7")

        # Subtext Labels
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(420, 290, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(92, 64, 51);")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(470, 340, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(92, 64, 51);")
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(820, 40, 111, 31))
        self.pushButton_3.setStyleSheet("QPushButton#pushButton_3{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(137,63,3,255);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px:\n"
"    background-color:rgba(140,120,111,255);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(980, 40, 111, 31))
        self.pushButton_4.setStyleSheet("QPushButton#pushButton_4{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(137,63,3,255);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_4:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton_4:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px:\n"
"    background-color:rgba(140,120,111,255);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(1910, 780, 111, 31))
        self.pushButton_5.setStyleSheet("QPushButton#pushButton_3{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
" color:rgba(137,63,3,255);\n"
" border-radius:5px;\n"
"}\n"
"QPushButton#pushButton_3:hover{\n"
" background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton#pushButton_3:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px:\n"
"    background-color:rgba(140,120,111,255);\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.label_5.setText(_translate("Form", "l"))
        self.pushButton.setText(_translate("Form", "SWAY AWAY "))
        self.pushButton_2.setText(_translate("Form", "OUR LAHORE"))
        self.label_6.setText(_translate("Form", "IT\'S TIME TO  "))
        self.label_7.setText(_translate("Form", "VISIT LAHORE"))
        self.label_12.setText(_translate("Form", "Explore the new horizons of the lahore.Vist every corner of Lahore with us."))
        self.label_13.setText(_translate("Form", "Join us for the excited journey of Lahore."))
        self.pushButton_3.setText(_translate("Form", "Destinations"))
        self.pushButton_4.setText(_translate("Form", "About Us"))
        self.pushButton_5.setText(_translate("Form", "View Destinations"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())