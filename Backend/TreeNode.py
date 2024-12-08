class Tree:
    def __init__(self,name,category=None,ratings=None):
        self.name = name
        self.category = category
        self.ratings = ratings
        self.children = []
    def add_child(self,child):
        self.children.append(child)
    def tostring(self):
       return f"TreeNode(name='{self.name}', category='{self.category}', ratings={self.ratings})"