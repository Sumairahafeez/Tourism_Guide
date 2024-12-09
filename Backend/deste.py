from PyQt5 import QtCore, QtGui, QtWidgets
import Recommendations as rm
import HistoryTracker as ht
import datetime
class Ui_Formm(object):
    def setupUi(self, Form):
        self.Form = Form  # Store the Form reference for later use
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

        # Add buttons to the navbar
        for label in ["Sway Away","Home", "About Us", "Contact Us", "My Lists", "My History","Maps","Log Out"]:
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
            self.navLayout.addWidget(button)

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
        places = rm.pd.ReadCsv()
        tree = rm.bfsRecommendation(rm.build_Tree(places), 'Malls', 3)

        # Create cards dynamically
        self.cards = []  # List to store card references
        self.createCards(tree)

        # Add a spacer at the bottom for centering effect
        self.centralLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the central widget to the main layout
        self.mainLayout.addWidget(self.centralWidget)

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
            add_to_list_button = QtWidgets.QPushButton("Add to List", card_container)
            self.designButton(add_to_list_button)
            add_to_list_button.clicked.connect(lambda: self.addToList(node.name))
            show_map_button = QtWidgets.QPushButton("Show Map", card_container)
            self.designButton(show_map_button)
            show_map_button.clicked.connect(lambda: self.showMap(node.name))
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
        print(f"Adding {place_name} to the list")
        ht.add(f"Added {place_name} to the list at {datetime.datetime.now()}")

    def showMap(self, place_name):
        print(f"Showing map for {place_name}")
        ht.add(f"Viewed map for {place_name} at {datetime.datetime.now()}")

    def refreshRecommendations(self):
        selected_category = self.comboBox.currentText() 
        selected_priority = self.comboBox2.currentText()
        places = rm.pd.ReadCsv()
        if selected_priority == 'Most Popular':
            tree = rm.bfsRecommendation(rm.build_Tree(places), selected_category, 6)
            self.createCards(tree)
        elif selected_priority == 'Highest Ratings':
            tree = rm.bfsRecommendation(rm.build_Tree(places), selected_category, 3)
            self.createCards(tree)
        elif selected_priority == 'Top Most':    
            tree = rm.bfsRecommendation(rm.build_Tree(places), selected_category, 1)
            self.createCards(tree)  # Recreate the cards based on the selected category


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
