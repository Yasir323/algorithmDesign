# 4 operations: push, pop, peek or top, isEmpty
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


class Queue:

    def __init__(self, elements=None, maxlen=None):
        if elements is None:
            elements = []
        self._maxlen = maxlen
        if self._maxlen and elements:
            if len(elements) > self._maxlen:
                raise MaxSizeError
        self.elements = elements

    def enqueue(self, data):
        if not self._maxlen:
            self.elements.append(data)
        else:
            if len(self.elements) < self._maxlen:
                self.elements.append(data)
            else:
                raise MaxSizeError

    def dequeue(self):
        if self.elements:
            return self.elements.pop(0)
        else:
            raise EmptyQueueError

    def __len__(self):
        return len(self.elements)

    def is_empty(self):
        return True if len(self.elements) == 0 else False

    def __repr__(self) -> str:
        return f"{self.elements}"

    def __str__(self) -> str:
        return f"{self.elements}"


if __name__ == '__main__':
    queue1 = Queue()
    queue2 = Queue(maxlen=5)
    queue3 = Queue([1, 2, 3])
    queue = Queue([1, 2, 3], maxlen=5)
    print(f"Original queue: {queue}")
    queue.enqueue(4)
    print(f"After using enqueue with a value of 4: {queue}")
    queue.dequeue()
    print(f"After using dequeue: {queue}")
    print(f"Length of queue: {len(queue)}")
    print(f"Is the queue empty: {queue.is_empty()}")
    queue.dequeue()
    queue.dequeue()
    queue.dequeue()
    print(f"Is the queue empty: {queue.is_empty()}")
    try:
        queue.dequeue()
    except EmptyQueueError as e:
        print(f"{str(e)}")
