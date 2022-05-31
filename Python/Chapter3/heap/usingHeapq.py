from heapq import (
    heappush,
    heappop,
    heappushpop,
    heapreplace,
    heapify
)


class MinHeap:

    def __init__(self):
        self.heap = []

    @staticmethod
    def parent(i):
        return (i - 1) // 2

    @staticmethod
    def left_child(i):
        return (2 * i) + 1

    @staticmethod
    def right_child(i):
        return (2 * i) + 2

    def insert_key(self, k):
        heappush(self.heap, k)

    def decrease_key(self, i, new_value):
        if new_value > self.heap[i]:
            raise ValueError("The key passes is greater than the key present at node i.")
        self.heap[i] = new_value
        while (i != 0) and (self.heap[self.parent(i)] > self.heap[i]):
            # Swap
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def extract_min(self):
        return heappop(self.heap)

    def delete(self, i):
        # Reduce the key to -infinity
        self.decrease_key(i, float('-inf'))
        # Extract that key
        self.extract_min()

    def get_min(self):
        return self.heap[0]


# Driver program to test above function
if __name__ == '__main__':
    min_heap = MinHeap()
    min_heap.insert_key(3)
    min_heap.insert_key(2)
    min_heap.delete(1)
    min_heap.insert_key(15)
    min_heap.insert_key(5)
    min_heap.insert_key(4)
    min_heap.insert_key(45)

    print(min_heap.extract_min())
    print(min_heap.get_min())
    min_heap.decrease_key(2, 1)
    print(min_heap.get_min())
