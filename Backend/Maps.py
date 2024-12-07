import Graphs
import csv
import random
def load_map(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        names = []
        for row in reader:
            names.append(row[0])
    return connectPlaces(names)        
def connectPlaces(places):
    g = Graphs.Graph()
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