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


def insert(array, data):
    n = len(array)
    if n == 0:
        array.append(data)
    else:
        array.append(data)
        build_max_heap(array)


def delete_node(array, data):
    n = len(array)
    for index, element in enumerate(array):
        if element == data:
            array[index], array[n - 1] = array[n - 1], array[index]
            break
    array.remove(data)
    build_max_heap(array)


def peak(array):
    return array[0]


def extract_max(array):
    max_ = array[0]
    delete_node(array, max_)
    return max_


if __name__ == '__main__':
    array = [1, 4, 3, 7, 8, 9, 10]
    build_max_heap(array)
    print(array)
    insert(array, 5)
    print(array)
    delete_node(array, 7)
    print(array)
