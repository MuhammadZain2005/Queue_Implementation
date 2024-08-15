"""
QUEUE IMPLEMENTATION
"""

import time

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        start_time = time.time()
        self.items.append(item)
        end_time = time.time()
        self.visualize_queue()
        print(f"Time taken to enqueue: {end_time - start_time:.6f} seconds\n")

    def dequeue(self):
        if not self.is_empty():
            start_time = time.time()
            item = self.items.pop(0)
            end_time = time.time()
            self.visualize_queue()
            print(f"Time taken to dequeue: {end_time - start_time:.6f} seconds\n")
            return item
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            start_time = time.time()
            item = self.items[0]
            end_time = time.time()
            print(f"Queue peek: {item}")
            print(f"Time taken to peek: {end_time - start_time:.6f} seconds\n")
            return item
        else:
            raise IndexError("peek from empty queue")

    def is_empty(self):
        return len(self.items) == 0

    def visualize_queue(self):
        print(f"Current queue: {self.items}")

# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.peek()
queue.dequeue()
queue.dequeue()
print(queue.is_empty())
