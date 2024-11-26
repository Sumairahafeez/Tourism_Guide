from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys

# Dummy data for categories and their respective areas
category_data = {
    "Historic Sites": ["Badshahi Mosque", "Lahore Fort", "Minar-e-Pakistan", "Walled City of Lahore"],
    "Point of Interests and Landmarks": ["Wagah Border", "Food Street Fort Road", "Delhi Gate"],
    "Parks n Gardens": ["Shalimar Gardens", "Bagh-e-Jinnah", "Jilani Park", "Gulshan-e-Iqbal Park"],
    "Shopping Malls": ["Emporium Mall", "Packages Mall", "Fortress Stadium"],
    "Amusement n Theme Parks": ["Sozo Water Park", "Joyland", "Playdium Avenue Mall"],
}

class DetailsForm(QWidget):
    """Form to display details of selected category"""
    def __init__(self, category, items, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"{category} Details")
        self.setGeometry(100, 100, 300, 200)
        layout = QVBoxLayout(self)

        # Display items in the category
        for item in items:
            layout.addWidget(QWidget().createLabel(item, self))  # Display each area as a label

class MainForm(QMainWindow):
    """Main form with ComboBox"""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tourist Management System")
        self.setGeometry(100, 100, 400, 300)
        
        # ComboBox for categories
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(["Select Category"] + list(category_data.keys()))
        self.comboBox.currentIndexChanged.connect(self.handleSelection)
        
        # Layout setup
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handleSelection(self, index):
        """Handle selection from ComboBox"""
        if index > 0:  # Skip "Select Category" option
            category = self.comboBox.currentText()
            areas = category_data.get(category, [])
            # Open the new form with the selected category details
            self.details_form = DetailsForm(category, areas)
            self.details_form.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
