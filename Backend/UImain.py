# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import navBar
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(2012, 1081)

        # Create the main layout for the form
        self.mainLayout = QtWidgets.QHBoxLayout(Form)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        # 1. Side Navbar
        self.navbar = QtWidgets.QWidget(Form)
        self.navbar.setFixedWidth(200)
        self.navbar.setStyleSheet("""
            QWidget {
                background-color: #D2B48C;  /* Gradient from beige to dark brown */
                border-right: 2px solid #F5F5DC;  /* Beige border */
            }
        """)
        self.navLayout = QtWidgets.QVBoxLayout(self.navbar)
        self.navLayout.setContentsMargins(10, 10, 10, 10)

        # Add navigation buttons
        navBar.navBar(self.navLayout, Form)

        # Add a spacer to push buttons to the top
        self.navLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the navbar to the main layout
        self.mainLayout.addWidget(self.navbar)

        # 2. Main Page Content
        self.centralWidget = QtWidgets.QWidget(Form)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)  # Remove margins to cover the entire page
        self.centralLayout.setSpacing(0)  # Remove spacing between widgets

        # Background image
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setStyleSheet("background-image: url(./resources/main.jpg);"                              
                                 )
        self.label.setScaledContents(True)
        self.centralLayout.addWidget(self.label)
        self.mainLayout.addWidget(self.centralWidget)

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(-40, 480, 371, 331))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(420, 180, 610, 111))
        self.label_6.setStyleSheet("color: rgb(92, 64, 51);")
        font = QtGui.QFont()
        font.setFamily("Verdena")
        font.setPointSize(21)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(420, 210, 531, 141))
        font = QtGui.QFont()
        font.setFamily("Verdena")
        font.setPointSize(21)
        font.setBold(True)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(137, 63, 3);")  # Deep Orange-Brown
        self.label_7.setObjectName("label_7")

        # Subtext Labels
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(420, 290, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Verdena")
        font.setPointSize(12)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(92, 64, 51);")
        self.label_12.setObjectName("label_12")

        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(470, 340, 291, 21))
        font = QtGui.QFont()
        font.setFamily("Verdena")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("color: rgb(92, 64, 51);")
        self.label_13.setObjectName("label_13")


        # Add the central widget to the main layout
        self.mainLayout.addWidget(self.centralWidget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        # self.label_5.setText(_translate("Form", "l"))
        self.label_6.setText(_translate("Form", "IT\'S TIME TO  "))
        self.label_7.setText(_translate("Form", "VISIT LAHORE"))
        self.label_12.setText(_translate("Form", "Explore the new horizons of the lahore.Vist every corner of Lahore with us."))
        self.label_13.setText(_translate("Form", "Join us for the excited journey of Lahore."))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    # Create the initial main page
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())
