
# array_queue.py

class ArrayQueue:
    def __init__(self, capacity=5):
        if capacity <= 0:
            raise ValueError("Capacity must be greater than zero.")

        self.capacity = capacity
        self.items = [None] * capacity
        self.front = 0
        self.rear = 0
        self.count = 0

    # Add an item at the rear
    def enqueue(self, item):
        if self.is_full():
            raise OverflowError("Queue overflow: queue is full.")

        self.items[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.count += 1

    # Remove and return the front item
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")

        item = self.items[self.front]
        self.items[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.count -= 1
        return item

    # View the front item
    def peek_front(self):
        if self.is_empty():
            raise IndexError("Queue underflow: queue is empty.")
        return self.items[self.front]

    def is_empty(self):
        return self.count == 0

    def is_full(self):
        return self.count == self.capacity

    def __str__(self):
        result = []
        i = self.front

        for _ in range(self.count):
            result.append(str(self.items[i]))
            i = (i + 1) % self.capacity

        return "[" + ", ".join(result) + "]"
