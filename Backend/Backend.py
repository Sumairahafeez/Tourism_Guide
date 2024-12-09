from DataStructures import Tree ,Queue,Graph
import DataStructures as ds
import csv
import random
def divideCategory(category):
    print(category)
    if 'museums' in category.lower() or 'art' in category.lower():
        return 'Museums'
    if 'historic' in category.lower() or 'religious' in category.lower() or 'landmarks' in category.lower():
        return 'Historic'
    if 'parks' in category.lower() or 'gardens' in category.lower() or 'zoo' in category.lower():
        return 'Parks'
    if 'malls' in category.lower() or 'markets' in category.lower():
        return 'Malls'
    else:
        return 'Others'
def build_Tree(places):
    root = Tree('Places')
    category_map = {}
    for place in places:
        
        name = place['Name']
        ratings = place['Ratings']
        category = place['Category']
        category = divideCategory(category)
        print(category,"is the category assigned")
        if category not in category_map:
            category_map[category] = Tree(category)
            root.add_child(category_map[category])
        placeNode = Tree(name,category=category,ratings=ratings)
        category_map[category].add_child(placeNode)
    print('Tree built successfully')    
    return root
def bfsRecommendation(root,target,topN):
    queue = [root]
    recommendations = []
    while queue:
        node = queue.pop(0)
        if node.name == target:
            recommendations.extend([child for child in node.children if child.ratings is not None])
        queue.extend(node.children)
    # sr.bubbleSort(recommendations)
    return recommendations[:topN]
csv_file = 'Places.csv'
def ReadCsv():
    places = []
    try:
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
                places.append({
                    'Name': row[0],
                    'Ratings': row[1],
                    'Category': row[2],
                })
                print("places loaded successfully")        
    except FileNotFoundError:
        print('File not found')  
    return places    
def writeCsv(places):
    try:
        with open(file=csv_file, mode = 'w') as file:
            writer = csv.writer(file)
            writer.writeheader(['Name', 'Ratings', 'Category'])
            writer.writerows(places) 
            print('places written successfully')
    except FileNotFoundError:
        print('File not found')                         
def AddPlace(name,ratings,category):
    places = ReadCsv()
    if any(places['Name'].lower() == name.lower() for place in places):
        print('Place already exists')
    else:
        places.append({
            'Name': name,
            'Ratings': ratings,
            'Category': category
        })
        writeCsv(places)
def GetTop6Places():
    places = ReadCsv()
    Ratings = [place['Ratings'] for place in places]  
    ds.bubbleSort(Ratings)
    top6 = Ratings[:6]
    return [place for place in places if place['Ratings'] in top6]
def GetRandomPlaces():
    places = ReadCsv()
    RandomPlaces = [place['Ratings'] for place in places]
    ds.shuffleArray(RandomPlaces)
    return [place for place in places if place['Ratings'] in RandomPlaces[:6]]
def GetPlacesByCategory(category):
    places = ReadCsv()
    return [place for place in places if place['Category'].lower == category.lower()] 
from DataStructures import Queue
import csv
class HistoryTracker:
    def __init__(self):
        self.history = Queue()
    def add(self, action):
        self.history.enqueue(action)
        self.writeTocsv(action)
    def remove(self):
        return self.history.dequeue()
    def isEmpty(self):
        return self.history.isEmpty()
    def peek(self):
        return self.history.peek()
    def getAll(self):
        return self.history.getAll()
    def getLatest(self):
        return self.readFromcsv()
    def getoldest(self):
        actions = self.readFromcsv()
        actions.reverse()
        return actions
    def writeTocsv(self, action):
        with open('history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            # Write the action (sentence) as a single entry in a row
            writer.writerow([action])
    def readFromcsv(self):
        with open('history.csv', 'r') as file:
            reader = csv.reader(file)
            actions = []
            for row in reader:
                actions.append(row) 
        return actions           
    def createInstance():
        return HistoryTracker()
def load_map(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        names = []
        for row in reader:
            names.append(row[0])
    return connectPlaces(names)        
def connectPlaces(places):
    g = Graph()
    for place in places:
        g.addNode(place)
    for place in places:
        for other_place in places:
            if place != other_place:
                weight = random.randint(1, 10)
                g.addEdge(place, other_place, weight)
    # g.display() 
    for place in places:
        print(f"Shortest path from {place}:")
        distances = g.dijkstra(place)
        for other_place in places:
            print(f"{other_place}: {distances[other_place]}")           
    return g
load_map('Places.csv')               


