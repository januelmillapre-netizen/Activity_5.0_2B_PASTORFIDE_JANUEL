
# array_stack.py

class ArrayStack:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.items = []

    # Add an item to the top
    def push(self, item):
        if self.is_full():
            raise OverflowError("Stack overflow: stack is full.")
        self.items.append(item)

    # Remove and return the top item
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")
        return self.items.pop()

    # View the top item
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def is_full(self):
        return len(self.items) == self.capacity

    def __str__(self):
        return str(self.items)
