"""
Circular Queue implementation using an array(list).
"""


class MaxSizeError(Exception):
    """Raised when queue is full."""

    def __init__(self, message="Queue is full") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class EmptyQueueError(Exception):
    """Raised when queue is empty."""

    def __init__(self, message="Queue is empty") -> None:
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return self.message


class CircularQueue:

    def __init__(self, max_size):
        self.max_size = max_size
        self.queue = [None] * max_size
        self.front = self.rear = -1

    def enqueue(self, data):
        """
        1. queue is empty: front == -1
        2. no holes: front <= rear
        3. holes: front > rear
        4. queue is full: (rear+1) % max_size == front
        """
        if (self.rear + 1) % self.max_size == self.front:
            raise MaxSizeError("Queue is full.")
        elif self.front == -1:
            # Queue is empty
            self.front = self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1) % 5
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            raise EmptyQueueError
        elif self.front == self.rear:
            # Only one element in queue
            element = self.queue.pop(self.front)
            self.head = self.rear = -1
            return element
        else:
            element = self.queue.pop(self.front)
            self.front = (self.front + 1) % self.max_size
            return element

    def __repr__(self) -> str:
        return f"{self.queue}"

    def __str__(self) -> str:
        return f"{self.queue}"


if __name__ == '__main__':
    cqueue = CircularQueue(5)
    cqueue.enqueue(1)
    cqueue.enqueue(2)
    cqueue.enqueue(3)
    cqueue.enqueue(4)
    cqueue.enqueue(5)
    print("Initial queue")
    print(cqueue)
    cqueue.dequeue()
    print("After removing an element from the queue")
    print(cqueue)
