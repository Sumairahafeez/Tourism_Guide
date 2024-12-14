from PyQt5 import QtCore, QtGui, QtWidgets
from Backend import HistoryTracker as ht
import navBar
import DataStructures

class Ui_Formm(object):
    
    def setupUi(self, Form):
        self.Form = Form  # Store the Form reference for later use
        self.Tracker = ht.createInstance()
        self.iterniaryTree = DataStructures.RBTreeNode  # Make sure to use your RBTreeNode here
        self.cards = []

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
        navBar.navBar(self.navLayout, self.Form)  # Assuming navBar is correctly implemented

        # Add a spacer to push buttons to the top
        self.navLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the navbar to the main layout
        self.mainLayout.addWidget(self.navbar)

        # 2. Top Header Section
        self.headerWidget = QtWidgets.QWidget(Form)
        self.headerWidget.setStyleSheet("""
            QWidget {
                background-color: #8B4513;  /* Dark brown color */
                color: white;
                padding: 15px;
                font-size: 20px;
                font-weight: bold;
                border-bottom: 2px solid #F5F5DC;
            }
        """)
        headerLayout = QtWidgets.QHBoxLayout(self.headerWidget)
        headerLabel = QtWidgets.QLabel("Your Itinerary")
        headerLayout.addWidget(headerLabel)
        self.mainLayout.addWidget(self.headerWidget)

        # 3. Central Content
        self.centralWidget = QtWidgets.QWidget(Form)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)  # Center cards

        # Create a horizontal layout for combo boxes and the button
        controlLayout = QtWidgets.QHBoxLayout()
        controlLayout.setSpacing(20)  # Add spacing between widgets

        # Add the control layout to the main layout
        self.centralLayout.addLayout(controlLayout)

        # Fetch itinerary items from the tree
        itinerary_items = self.iterniaryTree.get_itinerary()  # Make sure this function is properly implemented

        # If no itinerary items are found, show a message box
        if not itinerary_items:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("No items found in your itinerary.")
            msg_box.exec_()
            return

        # Loop through the fetched itinerary items and create cards
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

            # Display the place and date-time information
            place_label = QtWidgets.QLabel(f"<b>Place:</b> {key}")
            date_label = QtWidgets.QLabel(f"<b>Date & Time:</b> {date_time}")

            text_layout.addWidget(place_label)
            text_layout.addWidget(date_label)

            # Add the text layout (place and date) to the card
            card_layout.addLayout(text_layout)

            # Add the card to the central layout
            self.centralLayout.addWidget(card_container)
            self.cards.append(card_container)

        # Add the central widget to the main layout
        self.mainLayout.addWidget(self.centralWidget)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
