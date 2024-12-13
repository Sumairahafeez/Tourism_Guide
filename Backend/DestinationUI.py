import calendar
from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngineWidgets
import Backend as rm
from Backend import HistoryTracker as ht
import datetime
from HistoryUI import Ui_Formm as historyUI

from functools import partial
from DataStructures import RBTree
import os
import requests

class Ui_Formm(object):
    def setupUi(self, Form):
        self.Form = Form  # Store the Form reference for later use
        self.Tracker = ht.createInstance()
        Form.setObjectName("Form")
        Form.resize(1004, 864)
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
        
        # 1. Side Navbar
        self.navbar = QtWidgets.QWidget(Form)
        self.navbar.setFixedWidth(200)
        self.navbar.setStyleSheet("""
            QWidget {
                background-color: #8B4513;  /* Dark brown background */
                border-right: 2px solid #F5F5DC;  /* Beige border on the right */
            }
        """)
        self.navLayout = QtWidgets.QVBoxLayout(self.navbar)
        self.navLayout.setContentsMargins(10, 10, 10, 10)
        
        self.Form = Form
        self.Tracker = ht.createInstance()

        self.itineraryTree = RBTree()  # Initialize Red-Black Tree for itinerary storage


        # Add buttons to the navbar
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
                button.clicked.connect(self.showHistoryPage)  # Connect to show history page
            self.navLayout.addWidget(button)

            button.setObjectName(f"navButton_{label.lower()}")
            if label == "My Travel Plan":
               button.clicked.connect(self.showTravelPlan)
            
            

        # Add a spacer to push buttons to the top
        self.navLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the navbar to the main layout
        self.mainLayout.addWidget(self.navbar)

        # 2. Central Content
        self.centralWidget = QtWidgets.QWidget(Form)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)  # Center cards

        # Create a horizontal layout for combo boxes and the button
        controlLayout = QtWidgets.QHBoxLayout()
        controlLayout.setSpacing(20)  # Add spacing between widgets

        # Combo Box for selecting categories
        self.comboBox = QtWidgets.QComboBox()
        self.comboBox.addItems(['Malls', 'Historic', 'Parks', 'Museums', 'Others'])
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFixedSize(300, 40)
        controlLayout.addWidget(self.comboBox)

        # Combo Box for selecting priority
        self.comboBox2 = QtWidgets.QComboBox()
        self.comboBox2.addItems(['Most Popular', 'Highest Ratings', 'Top Most'])
        self.comboBox2.setObjectName("comboBox2")
        self.comboBox2.setFixedSize(300, 40)
        controlLayout.addWidget(self.comboBox2)

        # Button to refresh the recommendations
        self.refreshButton = QtWidgets.QPushButton("Refresh Recommendations")
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.setFixedSize(200, 40)
        self.refreshButton.clicked.connect(self.refreshRecommendations)
        controlLayout.addWidget(self.refreshButton)

        # Add the control layout to the main layout
        self.centralLayout.addLayout(controlLayout)

        # Fetch places and recommendations
        places = rm.ReadCsv()
        tree = rm.bfsRecommendation(rm.build_Tree(places), 'Malls', 3)

        # Create cards dynamically
        self.cards = []  # List to store card references
        self.createCards(tree)

        # Add a spacer at the bottom for centering effect
        self.centralLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the central widget to the main layout
        self.mainLayout.addWidget(self.centralWidget)
    def showHistoryPage(self):
        self.Form.hide()
        self.historyPage = QtWidgets.QWidget()
        self.ui = historyUI()
        self.ui.setupUi(self.historyPage)
        self.historyPage.show()
    def createCards(self, tree):
        # Clear previous cards if any
        for card in self.cards:
            card.deleteLater()
        self.cards.clear()

        # Create cards dynamically and add to the main layout
        for i, node in enumerate(tree):
            # Create a container widget for each card
            card_container = QtWidgets.QWidget()
            card_container.setFixedSize(900, 180)  # Set a fixed size for each card
            card_container.setStyleSheet("""
                QWidget {
                    background-color: #F5F5DC;    /* Beige background */
                    border: 2px solid #8B4513;    /* Dark brown border */
                    border-radius: 10px;        /* Rounded corners */
                    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); /* Shadow effect */
                    padding: 10px;              /* Padding inside the card */
                }
            """)

            # Horizontal layout for the card content
            card_layout = QtWidgets.QHBoxLayout(card_container)

            # Image Section
            image_label = QtWidgets.QLabel(card_container)
            pixmap = QtGui.QPixmap(f"./resources/{node.name}.jpg").scaled(320, 160, QtCore.Qt.IgnoreAspectRatio)
            image_label.setPixmap(pixmap)
            image_label.setAlignment(QtCore.Qt.AlignCenter)
            card_layout.addWidget(image_label)

            # Text Section
            text_layout = QtWidgets.QVBoxLayout()
            name_label = QtWidgets.QLabel(f"Name: {node.name}", card_container)
            name_label.setFont(QtGui.QFont("Colonna MT", 14))
            text_layout.addWidget(name_label)

            # Buttons Section
            button_layout = QtWidgets.QHBoxLayout()
            add_to_list_button = QtWidgets.QPushButton("Add to My Plan", card_container)
            self.designButton(add_to_list_button)
        
            add_to_list_button.clicked.connect(partial(self.addToList, node.name))

            show_map_button = QtWidgets.QPushButton("Show Map", card_container)
            self.designButton(show_map_button)
          
            show_map_button.clicked.connect(lambda checked, name=node.name: self.showMap(name))

            button_layout.addWidget(add_to_list_button)
            button_layout.addWidget(show_map_button)

            # Add text and buttons to the card layout
            text_layout.addLayout(button_layout)
            card_layout.addLayout(text_layout)

            # Add the card to the main layout
            self.centralLayout.addWidget(card_container)
            self.cards.append(card_container)

    def designButton(self, button):
        # Button design using stylesheet
        button.setStyleSheet("""
            QPushButton {
                background: qlineargradient(
                    spread: pad,
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #F5F5DC,  /* Beige color */
                    stop: 1 #8B4513   /* Dark brown color */
                );
                color: white;                /* White text */
                font-size: 14px;             /* Text size */
                border: none;                /* No border */
                border-radius: 5px;          /* Rounded corners */
                cursor: pointer;            /* Pointer cursor on hover */
                padding: 10px 20px;          /* Padding inside the button */
            }
            QPushButton:hover {
                background-color: #8B4513;  /* Darker green on hover */
            }
            QPushButton:pressed {
                background-color: #F5F5DC;  /* Even darker green on press */
            }
        """)

    def addToList(self, place_name):
       dialog = QtWidgets.QDialog()
       dialog.setWindowTitle(f"Add {place_name} to Itinerary")
       dialog.resize(400, 300)

       layout = QtWidgets.QVBoxLayout()

    # Calendar to select Date
       date_label = QtWidgets.QLabel("Select Date:")
       calendar = QtWidgets.QCalendarWidget()
       layout.addWidget(date_label)
       layout.addWidget(calendar)
    #background clr 
       background_color = "#F5F5DC"
       calendar.setStyleSheet(f"background-color: {background_color};")
    # Time picker to select Time
       time_label = QtWidgets.QLabel("Select Time:")
       time_picker = QtWidgets.QTimeEdit()
       time_picker.setDisplayFormat("HH:mm")
       layout.addWidget(time_label)
       layout.addWidget(time_picker)

    # Confirm Button to finalize adding the place
       confirm_btn = QtWidgets.QPushButton("Confirm")
       self.designButton(confirm_btn)
       layout.addWidget(confirm_btn)

       dialog.setLayout(layout)

       def on_confirm():
          selected_date = calendar.selectedDate().toString("yyyy-MM-dd")
          selected_time = time_picker.time().toString("HH:mm")
          # Save the itinerary item
          self.itineraryTree.insert(place_name, f"{selected_date} at {selected_time}")

          print(f"Added {place_name} to itinerary on {selected_date} at {selected_time}")
          self.Tracker.add(f"Added {place_name} to the list on {selected_date} at {selected_time}")

          dialog.accept()

       confirm_btn.clicked.connect(on_confirm)

       dialog.exec_()  # Show the dialog



    def refreshRecommendations(self):
        selected_category = self.comboBox.currentText() 
        selected_priority = self.comboBox2.currentText()
        places = rm.ReadCsv()
        if selected_priority == 'Most Popular':
            tree = rm.bfsRecommendation(rm.build_Tree(places), selected_category, 6)
            self.createCards(tree)
        elif selected_priority == 'Highest Ratings':
            tree = rm.bfsRecommendation(rm.build_Tree(places), selected_category, 3)
            self.createCards(tree)
        elif selected_priority == 'Top Most':    
            tree = rm.bfsRecommendation(rm.build_Tree(places), selected_category, 1)
            self.createCards(tree)  # Recreate the cards based on the selected category
    

    def showTravelPlan(self):
    # Clear previous cards
       for card in self.cards:
         card.deleteLater()
       self.cards.clear()

    # Retrieve itinerary items from the Red-Black Tree
       itinerary_items = self.itineraryTree.get_itinerary()

       if not itinerary_items:
          msg_box = QtWidgets.QMessageBox()
          msg_box.setText("No items found in your itinerary.")
          msg_box.exec_()
          return

    # Create and display cards for each itinerary item
       for key, date_time in itinerary_items:
          card_container = QtWidgets.QWidget()
          card_container.setFixedSize(900, 180)
          card_container.setStyleSheet("""
            QWidget {
                background-color: #F5F5DC;
                border: 2px solid #8B4513;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
            }
        """)

          card_layout = QtWidgets.QHBoxLayout(card_container)

          text_layout = QtWidgets.QVBoxLayout()
          place_label = QtWidgets.QLabel(f"<b>Place:</b> {key}")
          date_label = QtWidgets.QLabel(f"<b>Date & Time:</b> {date_time}")

          text_layout.addWidget(place_label)
          text_layout.addWidget(date_label)

          card_layout.addLayout(text_layout)

          self.centralLayout.addWidget(card_container)
          self.cards.append(card_container)


    def getPlaceLocation(self, place_name):
    
    
        try:
        # OpenStreetMap Nominatim API endpoint
           url = "https://nominatim.openstreetmap.org/search"
           params = {
            'q': place_name,
            'format': 'json',
            'addressdetails': 1,
            'limit': 1
        }
        
        # Send a GET request to the Nominatim API
           response = requests.get(url, params=params)
        
        # Check if the request was successful
           if response.status_code == 200:
              data = response.json()
              if data:
                # Extract latitude and longitude from the response
                latitude = float(data[0]['lat'])
                longitude = float(data[0]['lon'])
                print(f"Fetched location for {place_name}: {latitude}, {longitude}")
                return latitude, longitude
              else:
                print(f"No results found for {place_name}. Using default location.")
                return  56.67, 20.75   # Default fallback location
           else:
            print(f"Error: Unable to fetch location for {place_name}. Status Code: {response.status_code}")
            return 31.5497, 74.3436  # Fallback to a default location

        except Exception as e:
          print(f"Error while fetching location for {place_name}: {e}")
          return 56.67, 20.75  # Fallback in case of error


    def showMap(self, place_name):
       print(f"Showing map for {place_name}")

    # Fetch dynamic coordinates using OpenStreetMap API
       latitude, longitude = self.getPlaceLocation(place_name)

    # Generate the HTML content for Leaflet.js
       html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Map of {place_name}</title>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
    <style>
        html, body, #map {{
            height: 100%;
            margin: 0;
            padding: 0;
        }}
    </style>
</head>
<body>
    <div id="map" style="width: 100%; height: 100%;"></div>
    <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
    <script>
        var map = L.map('map').setView([{latitude}, {longitude}], 15);
        L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
            attribution: '&copy; OpenStreetMap contributors'
        }}).addTo(map);
        L.marker([{latitude}, {longitude}]).addTo(map)
            .bindPopup("<b>{place_name}</b>").openPopup();
    </script>
</body>
</html> """
    # Save the HTML content to a temporary file
       temp_path = os.path.join(os.getcwd(), "map_temp.html")
       with open(temp_path, "w", encoding="utf-8") as file:
         file.write(html_content)

    # Open the map in QWebEngineView
       self.map_window = QtWidgets.QWidget()
       self.map_window.setWindowTitle(f"{place_name} Map")
       self.map_window.resize(800, 600)

       layout = QtWidgets.QVBoxLayout()
       self.web_view = QtWebEngineWidgets.QWebEngineView()
       self.web_view.load(QtCore.QUrl.fromLocalFile(temp_path))

       layout.addWidget(self.web_view)
       self.map_window.setLayout(layout)
       self.map_window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
