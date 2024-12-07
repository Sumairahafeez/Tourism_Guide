import heapq
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


