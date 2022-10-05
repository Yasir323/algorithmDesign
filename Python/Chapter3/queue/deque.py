"""
4 operations: enqueue, dequeue, peek, isEmpty, isFull

Array implemntation:
All 5 operations are O(1). Nut after a few enqueue and dedqueue 
operations, there will be non-usable empty space.
Linked list based implementtation can solve this, but it results in
enqueue and isFull operations becoming O(n).
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


class Deque:

    def __init__(self, maxlen):
        self._maxlen = maxlen
        self._queue = [None] * self._maxlen
        self._head = 0
        self._tail = 0

    def is_full(self):
        if self._head == self._tail + 1 or (self._head == 0 and self._tail == self._maxlen - 1):
            return True
        return False

    def is_empty(self):
        if self._head == self._tail:
            return True
        return False

    def appendleft(self, data):
        if self.is_full():
            raise MaxSizeError
        if self._head == 1:
            self._head = self._maxsize - 1
        else:
            self._head -= 1
        self._queue[self._head] = data

    def appendright(self, data):
        if self.is_full():
            raise MaxSizeError
        self._queue[self._tail] = data
        if self._tail == self._maxlen - 1:
            self._tail = 0
        else:
            self._tail += 1
        
    def popleft(self):
        if self.is_empty():
            raise EmptyQueueError
        return_value = self._queue[self._head]
        self._queue[self._head] = None
        if self._head == self._maxlen - 1:
            self._head = 0
        else:
            self._head += 1
        return return_value

    def popright(self):
        if self.is_empty():
            raise EmptyQueueError
        if self._tail == 0:
            self._tail = self._maxlen - 1
        else:
            self._tail -= 1
        return_value = self._queue[self._tail]
        self._queue[self._tail] = None
        return return_value


if __name__ == '__main__':
    queue = Deque(maxlen=5)
    queue.appendleft(2)
    queue.appendleft(1)
    queue.appendright(3)
    queue.appendright(4)
    queue.appendright(5)
    assert queue.popleft() == 1
    assert queue.popright() == 5
    assert queue.popleft() == 2
    assert queue.popleft() == 3
    assert queue.popleft() == 4
    print("Done")
    try:
        queue.popright()
    except EmptyQueueError as e:
        print(f"{str(e)}")
