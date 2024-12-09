import Queue
import csv
class HistoryTracker:
    def __init__(self):
        self.history = Queue.Queue()
    def add(self, action):
        self.history.enqueue(action)
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
    def writeTocsv(self):
        with open('history.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Action"])
    def readFromcsv(self):
        with open('history.csv', 'r') as file:
            reader = csv.reader(file)
            actions = []
            for row in reader:
                actions.append(row) 
        return actions           
def createInstance():
    return HistoryTracker()
   