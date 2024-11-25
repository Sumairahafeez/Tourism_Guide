import Queue
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