from PyQt5 import QtCore, QtGui, QtWidgets
import Recommendations as rm
import HistoryTracker as ht
import datetime
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
        # Combo Box for selecting priority
        self.comboBox2 = QtWidgets.QComboBox()
        self.comboBox2.addItems(['Oldest', 'Latest'])
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
        actions = ht.HistoryTracker.getAll(self.Tracker)
        # Create cards dynamically
        self.cards = []  # List to store card references
        actions = self.Tracker.readFromcsv()
        self.createCards(actions)

        # Add a spacer at the bottom for centering effect
        self.centralLayout.addSpacerItem(QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding))

        # Add the central widget to the main layout
        self.mainLayout.addWidget(self.centralWidget)

    def createCards(self, actions):       
        # Remove all widgets from the central layout (clear all previous cards)
        for i in reversed(range(self.centralLayout.count())):
            widget = self.centralLayout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()

        self.cards.clear()

        if not actions:  # Check if actions is empty
            no_data_label = QtWidgets.QLabel("No recommendations available.")
            self.centralLayout.addWidget(no_data_label)
            return

        # Create new notification bar-style cards dynamically
        for node in actions:
            # Container for the notification
            notification_bar = QtWidgets.QWidget()
            notification_bar.setFixedSize(880, 80)  # Notification bar size adjusted to fit the central area
            notification_bar.setStyleSheet("""
                QWidget {
                    background-color: #FFFACD;  /* Light yellow background */
                    border: 2px solid #FFD700;  /* Gold border */
                    border-radius: 8px;         /* Rounded corners */
                    box-shadow: 2px 4px 8px rgba(0, 0, 0, 0.2); /* Subtle shadow */
                    padding: 10px;
                }
            """)

            # Layout for the notification content
            bar_layout = QtWidgets.QHBoxLayout(notification_bar)
            bar_layout.setContentsMargins(10, 5, 13, 0)
            # Text section
            text_layout = QtWidgets.QVBoxLayout()
            title_label = QtWidgets.QLabel(f"Notification: {node}", notification_bar)
            title_label.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))
            text_layout.addWidget(title_label)

            bar_layout.addLayout(text_layout)

            # Action buttons section
            button_layout = QtWidgets.QVBoxLayout()
            dismiss_button = QtWidgets.QPushButton("Dismiss")
            dismiss_button.setFixedSize(80, 30)
            dismiss_button.setStyleSheet("""
                QPushButton {
                    background-color: #FF6347;  /* Tomato red */
                    color: #FFF;                /* White text */
                    border: none;
                    border-radius: 5px;
                }
                QPushButton:hover {
                    background-color: #FF4500;  /* Darker tomato red */
                }
            """)
            dismiss_button.clicked.connect(lambda: self.dismissNotification(notification_bar))
            button_layout.addWidget(dismiss_button)

            bar_layout.addLayout(button_layout)

            # Add the notification bar directly to the central layout
            self.centralLayout.addWidget(notification_bar)
            self.cards.append(notification_bar)
    def dismissNotification(self, notification_bar):
        self.centralLayout.removeWidget(notification_bar)
        notification_bar.deleteLater()
        self.cards.remove(notification_bar)
        
    def refreshRecommendations(self):
        selected_category = self.comboBox2.currentText() 
        if(selected_category == 'Oldest'):
            actions = self.Tracker.getoldest()
            
        elif(selected_category == 'Latest'):
            actions = self.Tracker.getLatest()
        self.createCards(actions)    
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Formm()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
