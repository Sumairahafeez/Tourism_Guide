from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWidgets,QtWebEngineWidgets
from HistoryUI import Ui_Formmm as history
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
    #print("Main Page")
    #Form.close()
    mainPage = QtWidgets.QWidget()
    mainUI = Ui_Forms()
    mainUI.setupUi(mainPage)
    mainPage.show()
    #sys.exit(app.exec_())
    #mainPage.open_main_page(mainPage)
def showLahoreMap():
       print("Map")
       dialog = QtWidgets.QDialog()
       dialog.setWindowTitle("Map")
       dialog.resize(600, 400)

    # Create QWebEngineView to display the map
       web_view = QtWebEngineWidgets.QWebEngineView()

    # Define the Google Maps URL (center the map on Lahore as an example)
       google_maps_url = "https://www.google.com/maps/place/Lahore"

       web_view.setUrl(QtCore.QUrl(google_maps_url))

       layout = QtWidgets.QVBoxLayout()
       layout.addWidget(web_view)

       dialog.setLayout(layout)
       dialog.exec_()      
def handle_sway_away(Form):
        QtWidgets.QMessageBox.information(Form,"lets gooo.!!","Navigating to SWAY AWAY ...")           
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
               button.clicked.connect(showLahoreMap)
            if label == "Destinations":
               button.clicked.connect(lambda:showDestinationPage(Form))
            if label == "Log Out":
               button.clicked.connect(Form.close)
            if label == "Sway Away":
               button.clicked.connect(lambda:handle_sway_away(Form))
            if label == "Home":
               button.clicked.connect(lambda: showMainPage(Form))
            if label == "About Us":
               button.clicked.connect(lambda: showAboutUs(Form)) 
            if label == "Contact Us":
               button.clicked.connect(lambda: showContactUs(Form))         
            navLayout.addWidget(button)
