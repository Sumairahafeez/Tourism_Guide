from PyQt5 import QtCore, QtGui, QtWidgets
from Backend import HistoryTracker as ht
import navBar
import DataStructures


class Ui_Formm(object):
    def setupUi(self, Form):
        self.Form = Form
        self.Tracker = ht.createInstance()
        self.iterniaryTree = DataStructures.RBTreeNode  # Ensure to use your RBTreeNode class here
        self.cards = []  # List to track dynamically created cards

        Form.setObjectName("Form")
        Form.resize(2012, 1081)
        Form.setStyleSheet("""
            QWidget {
                background: qlineargradient(
                    spread: pad,
                    x1: 0, y1: 0, x2: 1, y2: 1,
                    stop: 0 #F5F5DC,
                    stop: 1 #8B4513
                );
            }
        """)

        self.mainLayout = QtWidgets.QHBoxLayout(Form)

        # Side Navbar
        self.navbar = QtWidgets.QWidget(Form)
        self.navbar.setFixedWidth(200)
        self.navbar.setStyleSheet("""
            QWidget {
                background-color: #D2B48C;
                border-right: 2px solid #F5F5DC;
            }
        """)
        self.navLayout = QtWidgets.QVBoxLayout(self.navbar)
        self.navLayout.setContentsMargins(10, 10, 10, 10)
        navBar.navBar(self.navLayout, self.Form)

        self.mainLayout.addWidget(self.navbar)

        # Top Header Section
        self.headerWidget = QtWidgets.QWidget(Form)
        self.headerWidget.setStyleSheet("""
            QWidget {
                background-color: #8B4513;
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

        # Central Content
        self.centralWidget = QtWidgets.QWidget(Form)
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.centralLayout.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)

        self.mainLayout.addWidget(self.centralWidget)

        # Populate Itinerary Cards
        self.populate_itinerary_cards()

    def clear_central_layout(self):
        """ Helper function to clear the central layout """
        while self.centralLayout.count():
            item = self.centralLayout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.setParent(None)

    def populate_itinerary_cards(self):
        """ Populate the itinerary cards dynamically """
        # Clear previous items
        self.clear_central_layout()
        self.cards.clear()

        # Fetch updated itinerary
        itinerary_items = self.iterniaryTree.get_itinerary()

        # If no items, show a message box
        if not itinerary_items:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setText("No items found in your itinerary.")
            msg_box.exec_()
            return

        # Add cards for each itinerary item
        for key, date_time in itinerary_items:
            self.add_itinerary_card(key, date_time)

    def add_itinerary_card(self, key, date_time):
        """ Helper function to add a single itinerary card """
        card_container = QtWidgets.QWidget()
        card_container.setFixedSize(900, 180)
        card_container.setStyleSheet("""
            QWidget {
                background-color: #F5F5DC;
                border: 2px solid #8B4513;
                border-radius: 10px;
                padding: 10px;
            }
        """)
        card_layout = QtWidgets.QHBoxLayout(card_container)

        # Labels for place and date/time
        text_layout = QtWidgets.QVBoxLayout()
        place_label = QtWidgets.QLabel(f"<b>Place:</b> {key}")
        date_label = QtWidgets.QLabel(f"<b>Date & Time:</b> {date_time}")
        text_layout.addWidget(place_label)
        text_layout.addWidget(date_label)

        # Delete Button
        delete_btn = QtWidgets.QPushButton("Delete")
        delete_btn.setStyleSheet("""
               QPushButton {
    background: #F5F5DC;  /* Beige */
    color: #8B4513;       /* Dark brown */
    font-size: 14px;
    border: 2px solid #8B4513;
    border-radius: 10px;
    padding: 10px;
}
QPushButton:hover {
    background: #D2B48C;  /* Lighter beige */
}
QPushButton:pressed {
    background: #C19A6B;  /* Darker beige */
}

            """)
        delete_btn.clicked.connect(lambda checked, p=key, d=date_time: self.delete_item(p, d))

        # Add widgets to card layout
        card_layout.addLayout(text_layout)
        card_layout.addWidget(delete_btn)

        # Add card to the central layout and track it
        self.centralLayout.addWidget(card_container)
        self.cards.append(card_container)

    def delete_item(self, place_name, date_time):
        """ Delete an item from the itinerary and refresh the UI """
        if self.iterniaryTree.remove(place_name, date_time):
            print(f"{place_name} scheduled on {date_time} has been removed.")
            self.populate_itinerary_cards()  # Refresh the UI
        else:
            msg_box = QtWidgets.QMessageBox()
            msg_box.setWindowTitle("Deletion Error")
            msg_box.setText(f"{place_name} on {date_time} couldn't be found.")
            msg_box.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
