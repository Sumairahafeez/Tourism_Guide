from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1004, 864)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 1011, 871))
        self.label.setStyleSheet("background-image: url(./resources/db.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        # Example of another button (already existing in your UI)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 50, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton#pushButton{\n"
            " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
            " color:rgba(137,63,3,255);\n"
            " border-radius:5px;\n"
            "}\n"
            "QPushButton#pushButton:hover{\n"
            " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton#pushButton:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(140,120,111,255);\n"
            "}"
        )
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("Another Button")

        # Add the "View List" button
        self.pushButton_view_list = QtWidgets.QPushButton(Form)
        self.pushButton_view_list.setGeometry(QtCore.QRect(400, 50, 200, 40))  # Adjust position and size as needed
        font = QtGui.QFont()
        font.setFamily("Bookman Old Style")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_view_list.setFont(font)
        self.pushButton_view_list.setStyleSheet(
            "QPushButton#pushButton_view_list{\n"
            " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(137, 63, 3, 255), stop:1 rgba(255, 255, 255, 255));\n"
            " color:rgba(137,63,3,255);\n"
            " border-radius:5px;\n"
            "}\n"
            "QPushButton#pushButton_view_list:hover{\n"
            " background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(150, 63, 45, 255), stop:1 rgba(255, 255, 255, 255));\n"
            "}\n"
            "QPushButton#pushButton_view_list:pressed{\n"
            "    padding-left:5px;\n"
            "    padding-top:5px;\n"
            "    background-color:rgba(140,120,111,255);\n"
            "}"
        )
        self.pushButton_view_list.setObjectName("pushButton_view_list")
        self.pushButton_view_list.setText("View List")
        self.pushButton_view_list.clicked.connect(self.viewList)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Tourist Guide Management System"))

    # Define the function for the "View List" button
    def viewList(self):
        # Add logic to open a list view or show relevant information
        print("View List button clicked!")  # Replace with actual functionality

# For testing the UI independently
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
