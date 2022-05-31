import math


def heapify(array, n):
    """MAx Heap."""
    i = 0
    while i < math.ceil(math.log2(n)):
        lchild = (2 * i) + 1
        rchild = (2 * i) + 2
        if lchild >= n:
            break
        elif rchild >= n:
            largest = lchild
        else:
            if array[rchild] > array[lchild]:
                largest = rchild
            else:
                largest = lchild
        if array[i] < array[largest]:
            array[largest], array[i] = array[i], array[largest]
            heapify(array, largest)
        i += 1
    return array


if __name__ == '__main__':
    ls = [1, 3, 5, 2, 4, 6]
    ls2 = [5, 3, 2]
    ls3 = [100, 99, 98, 5, 3, 60]
    print(heapify(ls, len(ls)))
    print(heapify(ls2, len(ls2)))
    print(heapify(ls3, len(ls3)))
