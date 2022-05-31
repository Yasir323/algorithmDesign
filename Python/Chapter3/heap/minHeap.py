def min_heapify(array, n, i):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    smallest = i
    if lchild < n and array[lchild] < array[i]:
        smallest = lchild
    if rchild < n and array[rchild] < array[smallest]:
        smallest = right
    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        min_heapify(array, n, smallest)


def build_min_heap(array):
    n = len(array)
    for i in range(n//2, -1, -1):
        min_heapify(array, n, i)


def insert(array, data):
    n = len(array)
    if n == 0:
        array.append(data)
    else:
        array.append(data)
        build_min_heap(array)


def delete_node(array, data):
    n = len(array)
    for index, element in enumerate(array):
        if element == data:
            array[index], array[n - 1] = array[n - 1], array[index]
            break
    array.remove(data)
    build_min_heap(array)


def peek(array):
    return array[0]


def extract_min(array):
    min_ = array[0]
    delete_node(array, min_)
    return min_


if __name__ == '__main__':
    array = [1, 4, 3, 7, 8, 9, 10]
    build_min_heap(array)
    print(array)
    insert(array, 5)
    print(array)
    delete_node(array, 7)
    print(array)
