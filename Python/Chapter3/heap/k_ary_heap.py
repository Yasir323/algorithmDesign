import math


class K_Ary_Heap:

    def __init__(self, k):
        self.k = k
        self.arr = []
        self.heap_size = 0

    def parent(self, i):
        return math.floor((i - 2) / self.k + 1)
    
    def child(self, i, j):
        return self.k * (i - 1) + j + 1
    
    def extract_max(self):
        if self.heap_size < 1:
            raise Exception("Heap Underflow")
        max_ = self.arr[0]
        self.arr[0] = self.arr[self.heap_size - 1]
        self.heap_size -= 1
        self.heapify(0)
        return max_

    def heapify(self, i):
        largest = i
        for a in range(1, self.k + 1):
            if self.child(i, a) < self.heap_size and self.arr[self.child(i, a)] > self.arr[i]:
                if self.arr[self.child(i, a)] > self.arr[largest]:
                    largest = self.child(i, a)
        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.heapify(largest)

    def insert(self, element):
        self.heap_size += 1
        self.arr.append(element)
        i = self.heap_size - 1
        while i > 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)

    def increase_key(self, i, key):
        if key < self.arr[i]:
            raise Exception("New key is smaller than current key")
        self.arr[i] = key
        while i > 0 and self.arr[self.parent(i)] < self.arr[i]:
            self.arr[i], self.arr[self.parent(i)] = self.arr[self.parent(i)], self.arr[i]
            i = self.parent(i)


if __name__ == "__main__":
    h = K_Ary_Heap(3)
    h.insert(3)
    h.insert(1)
    h.insert(5)
    h.insert(7)
    h.insert(4)
    h.insert(2)
    h.insert(9)
    h.insert(19)
    print(h.extract_max())
    h.increase_key(3, 78)
    print(h.extract_max())
