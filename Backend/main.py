from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys
import csv
import os
from SignUp import Ui_Form  # Replace with actual file name
from page import Ui_MainWindow
from UImain import Ui_Form as Ui_Forms
import navBar

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

 

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login_action)
        self.ui.label_5.mousePressEvent = self.open_signup
        self.ui.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.clear_fields()
    def validate_login(self, username, password):
        """Check credentials from CSV and return the role if valid."""
        try:
            with open(USER_FILE, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["Username"] == username and row["Password"] == password:
                        return row["Role"]  # Return role (e.g., "user" or "admin")
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(self, "Error", "User data file not found.")
        return None 
    def login_action(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()

        # Validate login credentials and role
        role = self.validate_login(username, password)
        if role == "User":
            QtWidgets.QMessageBox.information(self,"Login successful",f"Welcome {username} (Role: {role})")
            self.open_main_page()
        elif role == "Admin":
            QtWidgets.QMessageBox.information(self,"Login successful",f"Welcome {username} (Role: {role})")
            self.open_admin_page()
        else:
            QtWidgets.QMessageBox.warning(self, "Login Failed", "Invalid username or password!")


    def open_signup(self, event):
        self.signup_window = SignUpWindow()
        self.signup_window.clear_fields() 
        self.signup_window.show()
        self.close()
    def clear_fields(self):
        self.ui.lineEdit.clear()
        self.ui.lineEdit_2.clear()
    def open_main_page(self):
        self.main_page = MainPage()
        self.main_page.show()
        self.close()

    def open_admin_page(self):
        QtWidgets.QMessageBox.information(self, "Admin Access", "Admin functionality coming soon!")

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
class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage, self).__init__()
        self.ui = Ui_Forms()
        self.ui.setupUi(self)
        self.setup_main_page()

    def setup_main_page(self):
        # Customize the Main Page UI here
        self.ui.pushButton.clicked.connect(self.handle_sway_away)
        self.ui.pushButton_4.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_3.clicked.connect(self.open_places)

    def open_about_us_page(self):
        self.close()
        navBar.showAboutUs(self)
    def open_places(self):
        self.close()
        navBar.showDestinationPage(self)

    def handle_sway_away(self):
        QtWidgets.QMessageBox.information(self,"lets gooo.!!","Navigating to SWAY AWAY page...")
# class AboutUsPage(QMainWindow):
#     def __init__(self):
#         super(AboutUsPage, self).__init__()
#         self.ui = Ui_Formz()
#         self.ui.setupUi(self)
#         self.setup_page()
#     def setup_page(self):
#         self.ui.pushButton.clicked.connect(self.open_main_page)
#     def open_main_page(self):
#         self.main_page=MainPage()
#         self.main_page.show()
#         self.close()
# class DestinationPage(QMainWindow):
#     def __init__(self):
#         super(DestinationPage, self).__init__()
#         self.ui = Ui_Formm()
#         self.ui.setupUi(self)
#         self.setup_page()
#     def setup_page(self):
#         self.ui.pushButton.clicked.connect(self.open_main_page)
#         self.ui.pushButton_2.clicked.connect(self.open_main_page)
#         self.ui.pushButton_3.clicked.connect(self.open_about_us)
#     def open_main_page(self):
#         self.main_page=MainPage()
#         self.main_page.show()
#         self.close()
#     def open_about_us(self):
#         self.page=AboutUsPage()
#         self.page.show()
#         self.close()

def main():
    initialize_csv()
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
