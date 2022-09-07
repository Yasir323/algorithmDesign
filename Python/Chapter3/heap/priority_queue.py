import math

NEGATIVE_INFINITY = -math.inf


class PriorityQueue:

    def __init__(self):
        self.arr = []
        self.heap_size = 0

    def parent(self, i):
        if len(self.arr) < 1:
            raise Exception("Heap Underflow.")
        return (i - 1) // 2

    def left_child(self, i):
        left_child_index = 2 * i + 1
        if left_child_index > len(self.arr):
            raise Exception("No child for this node.")
        return left_child_index

    def right_child(self, i):
        right_child_index = 2 * i + 2
        if right_child_index > len(self.arr):
            raise Exception("No right child for this node.")
        return right_child_index
    
    def max_heapify(self, index):
        left = self.left_child(index)
        right = self.right_child(index)
        if left < self.heap_size and self.arr[left] > self.arr[index]:
            largest = left
        else:
            largest = index
        if right < self.heap_size and self.arr[right] > self.arr[largest]:
            largest = right
        if largest != index:
            self.arr[index], self.arr[largest] = self.arr[largest], self.arr[index]
            self.max_heapify(largest)

    def peek(self):
        return self.arr[0]

    def extract_max(self):
        if self.heap_size < 1 or len(self.arr) < 0:
            raise Exception("Heap Underflow.")
        max = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.max_heapify(0)
        return max

    def increase_key(self, index, key):
        if key < self.arr[index]:
            raise ValueError("New key less than old!")
        self.arr[index] = key
        while index > 0 and self.arr[self.parent(index)] < self.arr[index]:
            self.arr[self.parent(index)], self.arr[index] = self.arr[index], self.arr[self.parent(index)]
            index = self.parent(index)

    def insert(self, key):
        self.heap_size += 1
        self.arr.append(NEGATIVE_INFINITY)
        self.increase_key(self.heap_size - 1, key)


if __name__ == '__main__':
    pq = PriorityQueue()
    pq.insert(3)
    pq.insert(1)
    pq.insert(5)
    pq.insert(7)
    pq.insert(4)
    pq.insert(2)
    pq.insert(9)
    pq.insert(19)
    print(pq.peek())
    print(pq.extract_max())
    print(pq.peek())
    pq.increase_key(3, 78)
    print(pq.peek())
