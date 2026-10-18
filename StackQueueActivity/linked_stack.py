
# linked_stack.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedStack:
    def __init__(self):
        self.top = None

    # Add an item at the head
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    # Remove the top item
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")

        item = self.top.data
        self.top = self.top.next
        return item

    # View the top item
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack underflow: stack is empty.")
        return self.top.data

    def is_empty(self):
        return self.top is None

    # A linked stack has no fixed capacity
    def is_full(self):
        return False

    def __str__(self):
        items = []
        current = self.top

        while current is not None:
            items.append(str(current.data))
            current = current.next

        return "[" + ", ".join(items) + "]"
