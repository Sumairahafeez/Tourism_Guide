from PyQt5.QtWebEngineWidgets import QWebEngineView

class TouristApp(QWidget):
    def __init__(self, api_key):
        super().__init__()

        # Initialize layout
        # self.setWindowTitle("Tourist Management System")
        # self.layout = QVBoxLayout()

        # self.search_bar = QLineEdit(self)
        # self.search_button = QPushButton('Search Tourist Spots', self)
        # self.result_label = QLabel('Search Results will appear here...', self)
        # self.map_view = QWebEngineView()

        # self.layout.addWidget(self.search_bar)
        # self.layout.addWidget(self.search_button)
        # self.layout.addWidget(self.result_label)
        # self.layout.addWidget(self.map_view)

        # self.search_button.clicked.connect(self.search_tourist_spots)

        # self.setLayout(self.layout)

        # MAIN FRONT END (FAJAR AND MINAHIL)

        self.google_maps = GoogleMapsAPI(api_key)

        self.show()

    def search_tourist_spots(self):
        city = self.search_bar.text()
        if not city:
            city = "Lahore"  # Default to Lahore
        spots = self.google_maps.get_tourist_spots(city)
        result_text = "\n".join([f"{spot['name']} ({spot['rating']} stars)" for spot in spots])
        self.result_label.setText(result_text)

        if spots:
            location = spots[0]['location']  # Show the first spot on the map
          #  map_url = f"https://www.google.com/maps?q={location['lat']},{location['lng']}"               not correct yet
            self.map_view.setUrl(QUrl(map_url))
