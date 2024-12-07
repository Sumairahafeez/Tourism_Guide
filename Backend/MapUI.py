import sys
import os
import csv
import random
import folium
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QLabel, QFileDialog, QTextEdit
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings
from PyQt5.QtCore import QUrl
from Graphs import Graph  # Assuming you have the Graph class in a Graphs module
import Maps

class MapApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tourist Map")
        self.setGeometry(100, 100, 800, 600)

        # Main Layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # Widgets
        self.load_button = QPushButton("Load CSV File")
        self.load_button.clicked.connect(self.load_csv)

        self.result_label = QLabel("Results:")
        self.result_label.setStyleSheet("font-weight: bold;")

        self.result_area = QTextEdit()
        self.result_area.setReadOnly(True)

        # Google Map View (actually Folium map)
        self.map_view = QWebEngineView()
        self.map_view.page().settings().setAttribute(QWebEngineSettings.JavascriptEnabled, True)

        # Add widgets to layout
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.result_label)
        self.layout.addWidget(self.result_area)
        self.layout.addWidget(self.map_view)
        self.central_widget.setLayout(self.layout)

        self.graph = None  # Graph instance

    def load_csv(self):
        # Open a file dialog to select the CSV file
        file_path, _ = QFileDialog.getOpenFileName(self, "Open CSV File", "", "CSV Files (*.csv)")
        if file_path:
            self.graph = Maps.load_map(file_path)
            self.result_area.append(f"Loaded places from: {file_path}\n")
            self.result_area.append("Graph created and shortest paths computed.\n")
            self.update_map(file_path)  # Update map visualization
        else:
            self.result_area.append("No file selected.\n")

    def update_map(self, file_path):
        # Generate a Folium map
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            places = [row[0] for row in reader]

        # Set the initial location for the map (can be the center of the places)
        folium_map = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

        # Hardcoded coordinates (you can replace these with actual coordinates)
        locations = {
            "Museum": [40.7128, -74.0060],
            "Hotel": [40.730610, -73.935242],
            "Park": [40.748817, -73.985428],
            "Restaurant": [40.761432, -73.977621],
            "Theater": [40.7580, -73.9855]
        }

        # Add markers for each place from CSV
        for place in places:
            if place in locations:
                folium.Marker(locations[place], popup=place).add_to(folium_map)

        # Save the map to an HTML file
        map_file = "tourist_map.html"
        folium_map.save(map_file)

        # Check if the HTML file exists and is accessible
        if not os.path.exists(map_file):
            print(f"Error: {map_file} not found.")
            return

        # Debugging log to ensure the file is created and path is correct
        print(f"Map saved at: {os.path.abspath(map_file)}")

        # Load the map in the PyQt WebView
        local_url = QUrl.fromLocalFile(os.path.abspath(map_file))

        # Check if the file path is valid
        if local_url.isValid():
            print(f"Loading URL: {local_url.toString()}")
            self.map_view.setUrl(local_url)
        else:
            print("Error: Invalid URL.")

# Run the PyQt Application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MapApp()
    window.show()
    sys.exit(app.exec())
