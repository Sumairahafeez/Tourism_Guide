from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication
from HistoryUI import Ui_Formm as history
from DestinationUI import Ui_Formm as destination
from AboutusUI import Ui_Formz as aboutus
from TravelPlansUI import Ui_Formm as travelplans
from CU import Ui_Formm as contactus
from UImain import Ui_Form as Ui_Forms
import sys
def showHistoryPage(Form):
    Form.close()
    historyPage = QtWidgets.QWidget()
    historyUI = history()
    historyUI.setupUi(historyPage)
    historyPage.show()
def showDestinationPage(Form):
    Form.close()
    destinationPage = QtWidgets.QWidget()
    destinationUI = destination()
    destinationUI.setupUi(destinationPage)
    destinationPage.show()
def showAboutUs(Form):
    print("About Us")
    Form.close()
    aboutUsPage = QtWidgets.QWidget()
    aboutUsUI = aboutus()
    aboutUsUI.setupUi(aboutUsPage)
    aboutUsPage.show() 
def showContactUs(Form):
    Form.close()
    contactUsPage = QtWidgets.QWidget()
    contactUsUI = contactus()
    contactUsUI.setupUi(contactUsPage)
    contactUsPage.show()     
def showTravelPlan(Form):
    Form.close()
    travelPlanPage = QtWidgets.QWidget()
    travelPlanUI = travelplans()
    travelPlanUI.setupUi(travelPlanPage)
    travelPlanPage.show() 
def showMainPage(Form):
    print("Main Page")
    Form.close()
    main = MainPage()
    main.show()
    # sys.exit(app.exec_())
    # mainPage.open_main_page(mainPage)
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
        navBar.ShowAboutUs(self)
    def open_places(self):
        self.close()
        navBar.showDestinationPage(self)

    def handle_sway_away(self):
        QtWidgets.QMessageBox.information(self,"lets gooo.!!","Navigating to SWAY AWAY page...")                 
def navBar(navLayout,Form):
    for label in ["Sway Away","Home", "About Us", "Contact Us", "My Travel Plans", "My History","Maps","Destinations","Log Out"]:
            button = QtWidgets.QPushButton(label)
            button.setFixedSize(180, 50)
            button.setStyleSheet("""
                QPushButton {
                    background-color: #F5F5DC;  /* Beige button background */
                    color: #8B4513;            /* Dark brown text color */
                    font-size: 14px;
                    border: none;
                    border-radius: 5px;
                    padding: 10px;
                }
                QPushButton:hover {
                    background-color: #D2B48C;  /* Lighter beige on hover */
                }
                QPushButton:pressed {
                    background-color: #C19A6B;  /* Darker beige on press */
                }
            """)
            button.setObjectName(f"navButton_{label.lower()}")
            if label == "My History":
                button.clicked.connect(lambda:showHistoryPage(Form))  # Connect to show history page
            if label == "My Travel Plans":
               button.clicked.connect(lambda:showTravelPlan(Form))
            if label == "Maps":
               button.clicked.connect(lambda:destination.showLahoreMap)
            if label == "Destinations":
               button.clicked.connect(lambda:showDestinationPage(Form))
            if label == "Log Out":
               button.clicked.connect(Form.close)
            if label == "Sway Away":
               pass
            if label == "Home":
               button.clicked.connect(lambda: showMainPage(Form))
            if label == "About Us":
               button.clicked.connect(lambda: showAboutUs(Form)) 
            if label == "Contact Us":
               button.clicked.connect(lambda: showContactUs(Form))         
            navLayout.addWidget(button)
