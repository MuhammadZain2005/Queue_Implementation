# Queue Implementation

## Overview

This implementation of a Queue in Python provides a standard Queue data structure with added features like step-by-step visualization and time tracking for each operation.

## Features

- **Enqueue**: Add an element to the end of the queue.
- **Dequeue**: Remove and return the element from the front of the queue.
- **Peek**: Return the element at the front of the queue without removing it.
- **Is Empty**: Check if the queue is empty.
- **Visualization**: See the state of the queue after each operation.
- **Time Tracking**: Measure and display the time taken for each operation.

## Methods

### `__init__()`
Initializes an empty queue.

```python
def __init__(self):
    self.items = []
```

### `enqueue(item)`
Adds an `item` to the end of the queue.

- **Parameters**: `item` (Any) - The item to add to the queue.
- **Returns**: None
- **Visualizes**: The queue after the operation.
- **Time Tracking**: Displays the time taken for the operation.

```python
def enqueue(self, item):
    start_time = time.time()
    self.items.append(item)
    end_time = time.time()
    self.visualize_queue()
    print(f"Time taken to enqueue: {end_time - start_time:.6f} seconds\n")
```
### `dequeue(item)`
Removes and returns the element from the front of the queue.
- **Returns**:  The `item` removed from the front of the queue.
- **Raises**: `IndexError` if the queue is empty.
- **Visualizes**: The queue after the operation.
- **Time Tracking**: Displays the time taken for the operation.

```python
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
```
### `peek(item)`
Returns the element at the front of the queue without removing it.

- **Returns**: The `item` at the front of the queue.
- **Raises**: IndexError if the queue is empty.
- **Time Tracking**: Displays the time taken for the operation.

```python
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

```
### `is_empty()`
Checks if the queue is empty.
- **Returns**: `True` if the queue is empty, `False` otherwise.

### `visualize_queue()`
Visualizes the current state of the queue.

```python
def visualize_queue(self):
    print("Queue state: ", self.items)
```
## Example Usage
```python
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.peek()          # Returns 1
queue.dequeue()       # Removes and returns 1
queue.dequeue()       # Removes and returns 2
queue.is_empty()      # Returns True
```
## Error Handling
The dequeue and peek methods raise an IndexError if called on an empty queue.

## Performance Considerations
This queue implementation is based on a list. While enqueuing (appending) is efficient, dequeuing (popping from the front) has O(n) time complexity due to the need to shift all elements.

```bash
You can include this in your documentation to make it easy for others to understand the functionality and performance of your queue implementation.
```
