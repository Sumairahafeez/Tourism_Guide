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
    def getAll(self):
        actions = []
        current = self.head
        while current != None:
            print(current.data)
            actions.append(current.data)
            current = current.next 
        return actions                                