from collections import deque
from typing import List, Optional, Any


class Queue:
    def __init__(self, size: Optional[int]=None):
        self.__size = size
        self.__queue = deque([], maxlen=size)

    def enqueue(self, element: Any):
        if self.__size:
            if self.is_full():
                raise Exception("Queue is full.")
        self.__queue.append(element)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self.__queue.popleft()

    def is_empty(self):
        if len(self.__queue) == 0:
            return True
        return False

    def is_full(self):
        if self.__size:
            return self.__size == len(self.__queue)
        else:
            return False

    def front(self):
        if not self.is_empty():
            return self.__queue[0]
        else:
            raise Exception("Queue is empty.")

    def __repr__(self):
        return str(self.__queue)


def merge_sort(array: List[int], low: int, high: int):
    if low < high:
        middle: int = low + (high - low) // 2
        merge_sort(array, low, middle)
        merge_sort(array, middle + 1, high)
        merge(array, low, middle, high)


def merge(array: List[int], low: int, middle: int, high: int):  # O(n)
    lqueue = Queue()
    rqueue = Queue()
    # Fill the queue
    for i in range(low, middle + 1):
        lqueue.enqueue(array[i])
    for i in range(middle + 1, high + 1):
        rqueue.enqueue(array[i])
    i = low
    while not (lqueue.is_empty() or rqueue.is_empty()):
        left = lqueue.front()
        right = rqueue.front() 
        if left <= right:
            array[i] = lqueue.dequeue()
        else:
            array[i] = rqueue.dequeue()
        i += 1
    while not lqueue.is_empty():
        array[i] = lqueue.dequeue()
        i += 1
    while not rqueue.is_empty():
        array[i] = rqueue.dequeue()
        i += 1


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 8, 0, 2, 2]
    merge_sort(nums, 0, len(nums) - 1)
    print(nums)
