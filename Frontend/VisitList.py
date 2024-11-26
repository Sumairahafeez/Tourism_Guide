# stack.py
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def get_stack(self):
        return self.stack



class VisitListManager:
    def __init__(self):
        self.visit_list_stack = Stack()  # Use the Stack class

    def add_to_list(self, place_name):
        """Add place to the visit list (stack)."""
        self.visit_list_stack.push(place_name)

    def get_visit_list(self):
        """Return the current visit list in LIFO order."""
        return self.visit_list_stack.get_stack()

    def is_empty(self):
        """Check if the visit list (stack) is empty."""
        return self.visit_list_stack.is_empty()
