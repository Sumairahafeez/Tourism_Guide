from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QComboBox, QLabel, QPushButton, QDialog
import sys
from Badshah import Ui_Form
from Myjoy import Ui_Frm
from empo import Ui_Formm
from LFT import Ui_Frmz
from LM import Ui_LMForm
from minr import Ui_MForm
from SHAL import Ui_ShFrm
from WK import Ui_WkFrm
import webbrowser
import main as m
#from main import Ab
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
        "Monuments & Statues": ["Minar-e-Pakistan", "Jehangir's Tomb & Kamran's Baradari Pavilion"],
        "Architectural Buildings": ["Shahi Qila Lahore"],
        "Historic Wall Areas": ["Lahore Guided Tours"],
    },
    "Points of Interest & Landmarks": {
        "Historic": ["Minar-e-Pakistan", "Walled City of Lahore Authority"],
        "Neighborhoods": ["Anarkali Bazaar"],
    },
    "Parks": ["Bagh-e-Jinnah", "Jilani Park", "Gulshan-e-Iqbal Park", "Jehangir's Tomb & Kamran's Baradari Pavilion"],
    "Masjid Wazir Khan":["123"],
    "Museum": ["Lahore Museum", "Army Museum"],
    "Fort": ["Lahore Fort "],
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
class BadshahiCategoryPage(QMainWindow):
    def __init__(self):
        super(BadshahiCategoryPage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_4.clicked.connect(self.open_main_page)
        self.ui.pushButton_3.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_5.clicked.connect(self.show_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def show_map(self):
        webbrowser.open("https://www.google.com/maps/place/Badshahi+Mosque/@31.587939,74.3094357,15z/data=!4m6!3m5!1s0x39191c9dbf0ddeb1:0x13bfcdb10fb490de!8m2!3d31.587939!4d74.3094357!16s%2Fm%2F025td3k?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class MallCategoryPage(QMainWindow):
    def __init__(self):
        super(MallCategoryPage, self).__init__()
        self.ui = Ui_Formm()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_3.clicked.connect(self.open_main_page)
        self.ui.pushButton_4.clicked.connect(self.open_about_us_page)
        self.ui.pushButton.clicked.connect(self.show_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def show_map(self):
        webbrowser.open("https://www.google.com/maps/place/Emporium+Mall/@31.4678214,74.2640726,17z/data=!3m1!4b1!4m6!3m5!1s0x391903d4d940f12b:0xdb8c83f6699d5226!8m2!3d31.4678169!4d74.2666475!16s%2Fg%2F11cmtv8bxn?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class JoylandCategoryPage(QMainWindow):
    def __init__(self):
        super(JoylandCategoryPage, self).__init__()
        self.ui = Ui_Frm()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_7.clicked.connect(self.open_main_page)
        self.ui.pushButton_6.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_8.clicked.connect(self.open_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def open_map(self):
        """Function to open Google in the default web browser."""
        webbrowser.open("https://www.google.com/maps/dir/31.4960158,74.2531461/Joyland,+Fortress+Stadium+Circular+Rd,+Saddar+Town,+Lahore,+Punjab/@31.5210733,74.228669,12z/data=!3m1!4b1!4m9!4m8!1m1!4e1!1m5!1m1!1s0x3919051cb6d08ffd:0x5a61626c98977248!2m2!1d74.3633895!2d31.5330723?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class FortPage(QMainWindow):
    def __init__(self):
        super(FortPage, self).__init__()
        self.ui = Ui_Frmz()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_2.clicked.connect(self.open_main_page)
        self.ui.pushButton_3.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_6.clicked.connect(self.open_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def open_map(self):
        """Function to open Google in the default web browser."""
        webbrowser.open("https://www.google.com/maps/place/Lahore+Fort/@31.588204,74.3128485,17z/data=!3m1!4b1!4m6!3m5!1s0x39191b622e82346f:0x35bdc71e324cb4ec!8m2!3d31.5881995!4d74.3154234!16zL20vMDJtMzBo?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class LMPage(QMainWindow):
    def __init__(self):
        super(LMPage, self).__init__()
        self.ui = Ui_LMForm()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_7.clicked.connect(self.open_main_page)
        self.ui.pushButton_5.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_6.clicked.connect(self.open_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def open_map(self):
        """Function to open Google in the default web browser."""
        webbrowser.open("https://www.google.com/maps/place/Lahore+Museum/@31.5683915,74.3034835,17z/data=!3m1!4b1!4m6!3m5!1s0x39191ca8f5a906f1:0xc5dad8adc056fa92!8m2!3d31.568387!4d74.3080969!16zL20vMDdmaHJo?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class MinarPage(QMainWindow):
    def __init__(self):
        super(MinarPage, self).__init__()
        self.ui = Ui_MForm()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_4.clicked.connect(self.open_main_page)
        self.ui.pushButton_3.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_5.clicked.connect(self.open_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def open_map(self):
        """Function to open Google in the default web browser."""
        webbrowser.open("https://www.google.com/maps/place/Minar-e-Pakistan/@31.5925193,74.3069101,17z/data=!3m1!4b1!4m6!3m5!1s0x39191c82d18c2ced:0x1aa4688a984fdde1!8m2!3d31.5925148!4d74.309485!16s%2Fg%2F11h38md34s?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class WkPage(QMainWindow):
    def __init__(self):
        super(WkPage, self).__init__()
        self.ui = Ui_WkFrm()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_2.clicked.connect(self.open_main_page)
        self.ui.pushButton_3.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_5.clicked.connect(self.open_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def open_map(self):
        """Function to open Google in the default web browser."""
        webbrowser.open("https://www.google.com/maps/place/Wazir+Khan+Mosque/@31.5832847,74.3210396,17z/data=!3m1!4b1!4m6!3m5!1s0x39191b68076b3149:0x5c8d9d4d735a88e9!8m2!3d31.5832802!4d74.3236145!16zL20vMDM3YzEy?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
class ShalamarPage(QMainWindow):
    def __init__(self):
        super(ShalamarPage, self).__init__()
        self.ui = Ui_ShFrm()
        self.ui.setupUi(self)
        self.setup_page()
    def setup_page(self):
        self.ui.pushButton_2.clicked.connect(self.open_main_page)
        self.ui.pushButton_4.clicked.connect(self.open_about_us_page)
        self.ui.pushButton_5.clicked.connect(self.open_map)
    def open_main_page(self):
        self.main_page=m.MainPage()
        self.main_page.show()
        self.close()
    def open_about_us_page(self):
        self.page=m.AboutUsPage()
        self.page.show()
        self.close()
    def open_map(self):
        """Function to open Google in the default web browser."""
        webbrowser.open("https://www.google.com/maps/place/Shalamar+Garden/@31.5843246,74.3802053,17z/data=!3m1!4b1!4m6!3m5!1s0x39191be37671dcbf:0x786a0e2a0b53d6ef!8m2!3d31.5843201!4d74.3827802!16zL20vMDM0Z2o4?entry=ttu&g_ep=EgoyMDI0MTIwNC4wIKXMDSoASAFQAw%3D%3D")
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
    def open_places(self):
        self.page = BadshahiCategoryPage()
        self.page.show()
        self.close()
    def mall(self):
        self.page= MallCategoryPage()
        self.page.show()
        self.close
    def Joyland(self):
        self.page= JoylandCategoryPage()
        self.page.show()
        self.close
    def LahoreFort(self):
        self.page= FortPage()
        self.page.show()
        self.close
    def LahoreMuseum(self):
        self.page= LMPage()
        self.page.show()
        self.close
    def Minar_e_Pakistan(self):
        self.page= MinarPage()
        self.page.show()
        self.close
    def Wazir_Khan(self):
        self.page= WkPage()
        self.page.show()
        self.close
    def Shalamar(self):
        self.page= ShalamarPage()
        self.page.show()
        self.close
    def handleSelection(self, index):
        """Handle category selection."""
        if index > 0:  # Skip the first item (placeholder)
            category_name = self.comboBox.currentText()
        
        # Custom behavior for specific categories
            if category_name == "Historic Site":
                self.open_places()
            elif category_name == "Shopping Malls":
                self.mall()
            elif category_name == "Amusement & Theme Parks":
                self.Joyland()
            elif category_name == "Points of Interest & Landmarks":
                self.Minar_e_Pakistan()
            elif category_name == "Masjid Wazir Khan":
                self.Wazir_Khan()
            elif category_name == "Parks":
                self.Shalamar()
            elif category_name == "Museum":
                self.LahoreMuseum()
            elif category_name == "Fort":
                self.LahoreFort()
            else:
            # Default behavior: show SubCategoryForm
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
