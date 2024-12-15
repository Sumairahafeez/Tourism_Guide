# **Sway Away: Tourist Guide Management System**

**Sway Away** is a desktop-based Tourist Guide Management System designed to improve travel experiences by offering features like location-based services, route planning, and personalized itinerary management. Built using Python and PyQt, this application integrates real-time navigation through the **Google Maps API**, ensuring seamless exploration for travelers.

---

## **Features**

### **User Modules**

- **Tourist Registration and Profile Management**: Users can create accounts and manage their profiles.
- **Search and Explore Tourist Spots**: Users can search destinations based on categories or specific locations.
- **Personalized Itineraries**: Tourists can create, update, and customize their itineraries dynamically.

### **Administrative Modules**

- **Manage Tourist Spots**: Admins can add, update, or remove details of tourist locations.
- **User Statistics**: Admins can analyze popular destinations and track user activity.

---

## **Key Functionalities**

- **Real-Time Navigation**: Integrated with **Google Maps API** to provide live location-based services and route planning.
- **Search and Recommendations**: Uses **tree-based algorithms** for search auto-completion and accurate recommendations.
- **Route Optimization**: Implements **graph algorithms** to determine the shortest and most efficient travel routes.
- **Backtracking Navigation**: Stack-based implementation allows revisiting previous routes easily.
- **Dynamic Itinerary Updates**: **Linked lists** manage flexible addition or removal of locations in user itineraries.
- **Search History Management**: **Queues** help maintain and retrieve recent search history for convenience.

---

## **Technologies Used**

- **Programming Language**: Python
- **Frontend Development**: PyQt framework using widgets like **QTableWidget**, **QListWidget**, and **QWebEngineView** for an interactive user interface.
- **APIs**: Google Maps API for location-based services and real-time navigation.
- **Visualization Tools**: **Matplotlib** and **PyQtGraph** for displaying statistical or graphical data.
- **Backend Algorithms**: Advanced data structures and algorithms for search, optimization, and dynamic data management.

---

## **Data Structures and Algorithms**

The system leverages key data structures and algorithms to ensure efficiency and accuracy:

- **Trees**: Used for search auto-completion to enhance the search functionality.
- **Graphs**: Applied for route optimization and shortest path calculations between tourist spots.
- **Stacks**: Support backtracking navigation for revisiting previous routes.
- **Linked Lists**: Manage dynamic itineraries by enabling addition or removal of locations.
- **Queues**: Maintain search history for quick access to previous searches.
- **Hash Tables**: Allow fast lookups for storing and retrieving tourist spot details.

---

## **Future Enhancements**

While the current system is limited to a desktop application, future enhancements include:

### **Mobile Application**
- Developing a mobile version for better portability and accessibility, as users cannot always carry laptops while traveling.

### **API Integrations**
- Expanding API integrations to include live weather updates, public transport schedules, and real-time traffic information.

### **User Control Enhancements**
- Allowing travelers to suggest new destinations or edit tourist spot details, making the system more interactive and user-driven.

---

## **Installation Instructions**

### **Prerequisites**

- Python (3.8 or higher)
- PyQt5
- Matplotlib
- Google Maps API Key

### **Steps to Run the Application**

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Sumairahafeez/Tourism_Guide  
    cd tourism-guide
    ```

2. **Install the required dependencies:**
    ```bash
    pip install PyQt5 matplotlib requests
    pip install networkx
    ```

3. **Run the application:**
    ```bash
    python main.py
    ```

---

## **Contributors**

- **Minahil Amjad**
- **Sumaira Hafeez**
- **Fajar Shahzad**
- **Faraih Nazar**

Contributions are welcome! Submit issues or pull requests to improve the system.

---

## **Contact**

For support or inquiries:

**GitHub**: [Sway Away GitHub Repository](https://github.com/Sumairahafeez/Tourism_Guide)

---

## **License**

This project is licensed under the **MIT License**.

