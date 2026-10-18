
# linked_queue.py

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    # Add an item at the rear
    def enqueue(self, item):
        new_node = Node(item)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    # Remove and return the front item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")

        item = self.head.data
        self.head = self.head.next

        # Reset tail if the queue becomes empty
        if self.head is None:
            self.tail = None

        return item

    # View the front item
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")
        return self.head.data

    def is_empty(self):
        return self.head is None

    # A linked queue has no fixed capacity
    def is_full(self):
        return False

    def __str__(self):
        items = []
        current = self.head

        while current is not None:
            items.append(str(current.data))
            current = current.next

        return "[" + ", ".join(items) + "]"
