def max_heapify(arr, n, i):
    lchild: int = 2 * i + 1
    rchild: int = 2 * i + 2
    largest: int = i
    if lchild < n and arr[lchild] > arr[i]:
        largest: int = lchild
    if rchild < n and arr[rchild] > arr[largest]:
        largest = rchild
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        max_heapify(arr, n, largest)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):
        max_heapify(arr, n, i)


def heap_sort(arr):
    heap_size = n = len(arr)
    build_max_heap(arr)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_size -= 1
        max_heapify(arr, heap_size, 0)


if __name__ == '__main__':
    array = [10, 4, 3, 7, 8, 9, 1]
    heap_sort(array)
    print(array)
