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
tree = build_tree(tourist_spots)

# Display the tree structure
tree.display()
