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
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed
    def addNode(self, node):
        if node not in self.graph:
            self.graph[node] = []
    def addEdge(self, node1, node2, weight):
        self.addNode(node1)
        self.addNode(node2)
        self.graph[node1].append((node2, weight))
        if not self.directed:
            self.graph[node2].append((node1, weight))
    def display(self):
        for node in self.graph:
            print(node, '->', self.graph[node])
    def getNeighbors(self, node):
        return self.graph[node]
    def removeEdge(self, fromNode, toNode):
        self.graph[fromNode] = [(Node, weight) for Node, weight in self.graph[fromNode] if Node != toNode]
        if not self.directed:
            self.graph[toNode] = [(Node, weight) for Node, weight in self.graph[toNode] if Node != fromNode]
    def removeNode(self, node):
        del self.graph[node]
        for n in self.graph:
            self.graph[n] = [(Node, weight) for Node, weight in self.graph[n] if Node != node]
    def dijkstra(self, start):
        distance = {node: float('infinity') for node in self.graph}
        distance[start] = 0
        visited = set()
        while len(visited) < len(self.graph):
            current_node = None
            current_min_distance = float('infinity')
            for node in self.graph:
                if node not in visited and distance[node] < current_min_distance:
                    current_node = node
                    current_min_distance = distance[node]
            visited.add(current_node)
            for neighbor, weight in self.graph[current_node]:
                distance[neighbor] = min(distance[neighbor], distance[current_node] + weight)
        return distance


                        