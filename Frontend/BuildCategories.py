from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel, QPushButton, QDialog
import sys

class TreeNode:
    def __init__(self, name):
        self.name = name
        self.children = []  # List of child nodes
    
    def add_child(self, child_node):
        self.children.append(child_node)

    def display(self, level=0):
        print(" " * level * 4 + self.name)  # Indent based on the level
        for child in self.children:
            child.display(level + 1)

def build_tree(data, node_name="Tourist Spots"):
    root = TreeNode(node_name)

    for category, subcategories in data.items():
        # Create category node
        category_node = TreeNode(category)
        root.add_child(category_node)

        if isinstance(subcategories, dict):
            # If subcategories exist, build the tree for them
            for subcategory, places in subcategories.items():
                subcategory_node = TreeNode(subcategory)
                category_node.add_child(subcategory_node)

                # Add places under the subcategory
                for place in places:
                    subcategory_node.add_child(TreeNode(place))
        elif isinstance(subcategories, list):
            # If there are no subcategories, directly add places under the category
            for place in subcategories:
                category_node.add_child(TreeNode(place))

    return root

# Hierarchical data (tourist spots)
tourist_spots = {
    "Historic Site": {
        "Religious": ["Badshahi Mosque", "Masjid Wazir Khan"],
        "Museum": ["Lahore Museum", "Army Museum"],
        "Monuments & Statues": ["Minar-e-Pakistan", "Jehangir's Tomb & Kamran's Baradari Pavilion"],
        "Architectural Buildings": ["Shahi Qila Lahore"],
        "Historic Wall Areas": ["Lahore Guided Tours"],
    },
    "Points of Interest & Landmarks": {
        "Historic": ["Minar-e-Pakistan", "Walled City of Lahore Authority"],
        "Neighborhoods": ["Anarkali Bazaar"],
        "Other": ["Food Street Fort Road"],
    },
    "Parks": ["Bagh-e-Jinnah", "Jilani Park", "Gulshan-e-Iqbal Park", "Jehangir's Tomb & Kamran's Baradari Pavilion"],
    "Shopping Malls": ["Emporium Mall", "Fortress Stadium", "Amanah Mall"],
    "Amusement & Theme Parks": ["Playdium Avenue Mall", "Joyland"],
}

# Build the tree from the hierarchical data
tourist_tree = build_tree(tourist_spots)


class SubCategoryForm(QDialog):
    """Form to display subcategories or places."""
    def __init__(self, title, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 400, 300)
        
        layout = QVBoxLayout(self)
        if isinstance(data, dict):
            for subcategory, items in data.items():
                button = QPushButton(subcategory, self)
                button.clicked.connect(lambda _, d=items, t=subcategory: self.openSubForm(t, d))
                layout.addWidget(button)
        elif isinstance(data, list):
            for place in data:
                layout.addWidget(QLabel(place, self))

    def openSubForm(self, title, data):
        """Open another form for the selected subcategory."""
        self.sub_form = SubCategoryForm(title, data, self)
        self.sub_form.exec_()

class MainForm(QMainWindow):
    """Main form with ComboBox."""
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tourist Spots Explorer")
        self.setGeometry(100, 100, 400, 300)
        
        layout = QVBoxLayout()
        
        self.comboBox = QComboBox(self)
        self.comboBox.addItem("Select Category")
        self.comboBox.addItems([node.name for node in tourist_tree.children])  # Use the tree structure for categories
        self.comboBox.currentIndexChanged.connect(self.handleSelection)
        
        layout.addWidget(self.comboBox)
        
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handleSelection(self, index):
        """Handle category selection."""
        if index > 0:  # Skip the first item (placeholder)
            category_name = self.comboBox.currentText()
            category_node = self.find_node(tourist_tree, category_name)
            if category_node:
                data = {child.name: self.get_subcategory_places(child) for child in category_node.children}
                self.sub_form = SubCategoryForm(category_name, data, self)
                self.sub_form.exec_()

    def find_node(self, node, name):
        """Find a node by name in the tree."""
        if node.name == name:
            return node
        for child in node.children:
            result = self.find_node(child, name)
            if result:
                return result
        return None

    def get_subcategory_places(self, node):
        """Return places for subcategories or direct places."""
        if isinstance(node.children, list):
            return [child.name for child in node.children]
        else:
            return {child.name: [place.name for place in child.children] for child in node.children}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_form = MainForm()
    main_form.show()
    sys.exit(app.exec_())
