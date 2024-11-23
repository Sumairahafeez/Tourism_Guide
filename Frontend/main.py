from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import os
from SignUp import Ui_Form  # Replace with actual file name
from page import Ui_MainWindow

USER_FILE = "users.csv"

def initialize_csv():
    if not os.path.exists(USER_FILE):
        with open(USER_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Username", "Password", "Role"])

def save_user_to_csv(username, password, role):
    with open(USER_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, password, role])

def validate_login(username, password):
    if not os.path.exists(USER_FILE):
        return False
    with open(USER_FILE, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Username"] == username and row["Password"] == password:
                return True
    return False

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login_action)
        self.ui.label_5.mousePressEvent = self.open_signup
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clear_fields()
    def login_action(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        if validate_login(username, password):
            QtWidgets.QMessageBox.information(self, "Login Success", f"Welcome {username}!")
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid credentials. Please try again.")

    def open_signup(self, event):
        self.signup_window = SignUpWindow()
        self.signup_window.clear_fields() 
        self.signup_window.show()
        self.close()
    def clear_fields(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
class SignUpWindow(QMainWindow):
    def __init__(self):
        super(SignUpWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.signup_action)
        self.ui.pushButton_3.clicked.connect(self.back_to_login)
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clear_fields()
        
    def signup_action(self):
        username = self.ui.lineEdit.text()
        role = self.ui.comboBox.currentText()
        password = self.ui.lineEdit_3.text()

        if not username or not password or not role:
            QtWidgets.QMessageBox.warning(self, "Error", "All fields are required.")
            return

        save_user_to_csv(username, password, role)
        QtWidgets.QMessageBox.information(self, "Signup Success", f"Account created for {username}!")
        self.back_to_login()

    def back_to_login(self):
        self.login_window = LoginWindow()
        self.login_window.clear_fields()
        self.login_window.show()
        self.close()
    def clear_fields(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_3.clear()
    
def main():
    initialize_csv()
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
