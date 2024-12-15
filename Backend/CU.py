from PyQt5 import QtCore, QtGui, QtWidgets
from Backend import HistoryTracker as ht
import navBar
import DataStructures
import webbrowser

class Ui_Formm(object):
    
    def setupUi(self, Form):
        self.Form = Form  # Store the Form reference for later use
        # Initialize the UI window
        Form.setObjectName("Form")
        Form.resize(2012, 1081)
        Form.setStyleSheet("""
                QWidget {
                        background: qlineargradient(
                        spread: pad,
                        x1: 0, y1: 0, x2: 1, y2: 1,
                        stop: 0 #F5F5DC,  /* Beige color */
                        stop: 1 #8B4513   /* Dark brown color */
                        );
                }
        """)
        # Create the main horizontal layout
        self.mainLayout = QtWidgets.QHBoxLayout(Form)

        # 1. Side Navbar (Vertical Layout on the left)
        self.navbar = QtWidgets.QWidget(Form)
        self.navbar.setFixedWidth(200)  # Expanded sidebar width for better UI
        self.navbar.setStyleSheet("""
            QWidget {
                background-color: #D2B48C;  /* Gradient from beige to dark brown */
                border-right: 2px solid #F5F5DC;  /* Beige border */
            }
        """)
        self.navLayout = QtWidgets.QVBoxLayout(self.navbar)
        self.navLayout.setContentsMargins(10, 10, 10, 10)       
        navBar.navBar(self.navLayout, self.Form)  # Add your navBar here

        # Add a spacer to push buttons to the top of the navbar
        self.navLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the navbar to the main layout
        self.mainLayout.addWidget(self.navbar)

        # 2. Central Content (Contact Form)
        self.centralWidget = QtWidgets.QWidget(Form)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        # self.centralLayout.setAlignment(QtCore.Qt.AlignTop)  # Center the form

        # 3. Header Widget (Horizontal Header)
        self.headerWidget = QtWidgets.QWidget(Form)
        self.headerWidget.setStyleSheet("""
            QWidget {
                background-image: url('resources/img.jpg');
                background-position: left;
                background-repeat: no-repeat;
                background-attachment: fixed;
                border-bottom: 4px solid rgba(245, 245, 220, 0.9);  /* Light beige border */
                text-align: center;
                font-size: 40px;
                font-weight: bold;
                color: rgba(245, 245, 220, 0.9);  /* white text color */
                                        
            }
        """)
        headerLayout = QtWidgets.QHBoxLayout(self.headerWidget)
        headerLabel = QtWidgets.QLabel("Contact Us")
        headerLabel.setAlignment(QtCore.Qt.AlignCenter)
        headerLayout.addWidget(headerLabel)
        self.centralLayout.addWidget(self.headerWidget)

        # 4. Contact Form Widget
        self.contactFormWidget = QtWidgets.QWidget(Form)
        self.contactFormWidget.setStyleSheet("""
            QWidget {
                background-color: rgba(255, 255, 255, 0.85);  /* Semi-transparent white */
                border-radius: 15px;
                padding: 30px;
                box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.15);  /* Soft shadow */
            }
        """)
        self.contactFormLayout = QtWidgets.QFormLayout(self.contactFormWidget)
        self.contactFormLayout.setSpacing(20)  # Increased spacing between form fields

        # Name Input
        self.nameEdit = QtWidgets.QLineEdit(self.contactFormWidget)
        self.nameEdit.setPlaceholderText("Enter Your Full Name")
        self.nameEdit.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 20px;
                border: 2px solid #8B4513;
                border-radius: 8px;
                background-color: #FFF9E3;
                color: #333;
                font-family: 'Colonna MT';
            }
            QLineEdit:focus {
                border-color: #A0522D;  /* Darker brown on focus */
                background-color: #F6F4E9;
            }
        """)

        # Email Input
        self.emailEdit = QtWidgets.QLineEdit(self.contactFormWidget)
        self.emailEdit.setPlaceholderText("Your Email Address")
        self.emailEdit.setStyleSheet("""
            QLineEdit {
                padding: 12px;
                font-size: 20px;
                border: 2px solid #8B4513;
                border-radius: 8px;
                background-color: #FFF9E3;
                color: #333;
                font-family: 'Colonna MT';
            }
            QLineEdit:focus {
                border-color: #A0522D;
                background-color: #F6F4E9;
            }
        """)

        # Message Input
        self.messageEdit = QtWidgets.QTextEdit(self.contactFormWidget)
        self.messageEdit.setPlaceholderText("Your Message Here")
        self.messageEdit.setStyleSheet("""
            QTextEdit {
                padding: 12px;
                font-size: 20px;
                border: 2px solid #8B4513;
                border-radius: 8px;
                background-color: #FFF9E3;
                color: #333;
                min-height: 150px;
                font-family: 'Colonna MT';
            }
            QTextEdit:focus {
                border-color: #A0522D;
                background-color: #F6F4E9;
            }
        """)

        # Submit Button
        self.submitButton = QtWidgets.QPushButton("Submit", self.contactFormWidget)
        self.submitButton.setStyleSheet("""
            QPushButton {
                background-color: #8B4513;
                color: white;
                font-size: 18px;
                font-weight: bold;
                padding: 14px 30px;
                border-radius: 10px;
                border: none;
                cursor: pointer;
                transition: background-color 0.3s;
                font-family: 'Colonna MT';
            }
            QPushButton:hover {
                background-color: #A0522D;
            }
        """)
        self.submitButton.clicked.connect(self.submitForm)

        # Add form fields to the layout
        self.contactFormLayout.addRow("Full Name:", self.nameEdit)
        self.contactFormLayout.addRow("Email Address:", self.emailEdit)
        self.contactFormLayout.addRow("Message:", self.messageEdit)
        self.contactFormLayout.addWidget(self.submitButton)

        # Add the contact form widget to the central layout
        self.centralLayout.addWidget(self.contactFormWidget, alignment=QtCore.Qt.AlignCenter)

        # Add the central widget to the main layout
        self.mainLayout.addWidget(self.centralWidget)

    def submitForm(self):
        """Handle form submission and open email prompt."""
        name = self.nameEdit.text()
        email = self.emailEdit.text()
        message = self.messageEdit.toPlainText()

        if name and email and message:
            # Create the email content
            recipient = "swayAwayPakistan@gmail.com"
            subject = f"Message from {name}"
            body = f"Name: {name}\nEmail: {email}\nMessage: {message}"

        # Generate mailto URL
            mailto_url = f"mailto:{recipient}?subject={QtCore.QUrl.toPercentEncoding(subject).data().decode()}&body={QtCore.QUrl.toPercentEncoding(body).data().decode()}"

        # Open the email prompt
            webbrowser.open(mailto_url)

        # Optionally, show a confirmation message
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("Your message has been submitted successfully. An email draft has been opened in your default email client.")
            msg_box.exec_()

        # Clear form fields after submission
            self.nameEdit.clear()
            self.emailEdit.clear()
            self.messageEdit.clear()
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("Please fill out all fields before submitting.")
            msg_box.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
