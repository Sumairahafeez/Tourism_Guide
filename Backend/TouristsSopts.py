from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel
import sys

class TouristApp(QWidget):
    def __init__(self, api_key):
        super().__init__()

        # Initialize the GUI layout
        self.setWindowTitle("Tourist Management System")
        self.layout = QVBoxLayout()

        self.search_bar = QLineEdit(self)
        self.search_button = QPushButton('Search Tourist Spots', self)
        self.result_label = QLabel('Search Results will appear here...', self)

        self.layout.addWidget(self.search_bar)
        self.layout.addWidget(self.search_button)
        self.layout.addWidget(self.result_label)

        self.search_button.clicked.connect(self.search_tourist_spots)

        self.setLayout(self.layout)

        # Google Maps API Integration
        self.google_maps = GoogleMapsAPI(api_key)

        self.show()

    def search_tourist_spots(self):
        city = self.search_bar.text()
        if not city:
            city = "Lahore"  # Default to Lahore if no city is provided
        spots = self.google_maps.get_tourist_spots(city)
        result_text = "\n".join([f"{spot['name']} ({spot['rating']} stars)" for spot in spots])
        self.result_label.setText(result_text)
    
    def get_map_url(location):
        
        return f"https://www.google.com/maps?q={location['lat']},{location['lng']}"

if __name__ == "__main__":
    API_KEY = "YOUR_GOOGLE_MAPS_API_KEY"
    app = QApplication(sys.argv)
    window = TouristApp(api_key=API_KEY)
    sys.exit(app.exec_())
