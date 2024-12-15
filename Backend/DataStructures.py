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
class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
    def enqueue(self,data):
        if self.head == None:
            self.head = LinkedList(data)
            self.tail = self.head
        else:
            self.tail.next = LinkedList(data)
            self.tail = self.tail.next
    def dequeue(self):
        if self.head == None:
            return None
        else:
            current = self.head
            self.head = self.head.next
            return current.data
    def isEmpty(self):
        return self.head == None
    def peek(self):
        if self.head == None:
            return None
        else:
            return self.head.data
    def tostring(self):
        return str(self.head.data)     
    def getAll(self):
        actions = []
        current = self.head
        while current != None:
            print(current.data)
            actions.append(current.data)
            current = current.next 
        return actions                                    
import random
# Sorting Algorithms
def bubbleSort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1] , arr[j]
def shuffleArray(arr):
    n = len(arr)
    for i in range(n):
        j = random.randint(0,n-1)
        arr[i], arr[j] = arr[j], arr[i]     
class Graph:
    def __init__(self):
        self.nodes = {}
    
    def addNode(self, value):
        self.nodes[value] = {}
    
    def addEdge(self, from_node, to_node, weight):
        self.nodes[from_node][to_node] = weight
        self.nodes[to_node][from_node] = weight  # Assuming undirected graph
    def dijkstra(self, start):
        # Initialize distances and previous nodes
        try:
            distances = {node: float('inf') for node in self.nodes}
            previous_nodes = {node: None for node in self.nodes}
            distances[start] = 0
            unvisited_nodes = list(self.nodes.keys())
            
            while unvisited_nodes:
                # Get the node with the smallest distance
                current_node = min(unvisited_nodes, key=lambda node: distances[node])
                unvisited_nodes.remove(current_node)
                
                for neighbor, weight in self.nodes[current_node].items():
                    if neighbor in unvisited_nodes:
                        alternative_route = distances[current_node] + weight
                        if alternative_route < distances[neighbor]:
                            distances[neighbor] = alternative_route
                            previous_nodes[neighbor] = current_node
            return distances, previous_nodes
        except Exception as e:
            print(e)

class RBNode:
       def __init__(self, key, date_time):
          self.key = key  # Place name
          self.date_time = date_time  # Date and Time of visit
          self.color = "red"  # New nodes are red by default
          self.left = None
          self.right = None
          self.parent = None
  
class RBTree:
    def __init__(self):
        self.nil = RBNode(None, None)
        self.nil.color = "black"  # Sentinel node
        self.root = self.nil
    def insert(self, key, date_time):
        new_node = RBNode(key, date_time)
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.parent = None

        parent = None
        current = self.root

        while current != self.nil:
            parent = current
            if key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:  # New node is the root
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = "red"
        self.fix_insert(new_node)

    def fix_insert(self, node):
        # Red-Black Tree balancing logic
        pass

    def inorder_traversal(self, node, result):
        if node != self.nil:
            self.inorder_traversal(node.left, result)
            result.append((node.key, node.date_time))
            self.inorder_traversal(node.right, result)

    def get_itinerary(self):
        result = []
        self.inorder_traversal(self.root, result)
        return result
    
    def remove(self, key, date_time):
        node = self.find_node(self.root, key, date_time)
        if node == self.nil:
            return False  # Node not found
        self._delete_node(node)
        return True
    
    def find_node(self, node, key, date_time):
        while node != self.nil:
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            else:
                if node.date_time == date_time:
                    return node
                else:
                    return self.nil
        return self.nil

    def _delete_node(self, node):
        if node.left == self.nil and node.right == self.nil:
            # Node is a leaf
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = self.nil
                else:
                    node.parent.right = self.nil
            else:
                self.root = self.nil

        elif node.left == self.nil or node.right == self.nil:
            # Node has one child
            child = node.left if node.left != self.nil else node.right
            if node.parent:
                if node.parent.left == node:
                    node.parent.left = child
                else:
                    node.parent.right = child
            else:
                self.root = child
            child.parent = node.parent

        else:
            # Node with two children
            successor = self._get_successor(node)
            node.key, node.date_time = successor.key, successor.date_time
            self._delete_node(successor)

    def _get_successor(self, node):
        successor = node.right
        while successor.left != self.nil:
            successor = successor.left
        return successor
RBTreeNode = RBTree()        



                        