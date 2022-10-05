import random


class Interval:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f"({self.a}, {self.b})"


def find_intersection(arr, low, high):
    rand = random.randint(low, high)
    arr[rand], arr[high] = arr[high], arr[rand]
    a = arr[high].a
    b = arr[high].b
    for i in range(low, high):
        if arr[i].a < b and arr[i].b > a:
            if arr[i].a > a:
                a = arr[i].a
            if arr[i].b < b:
                b = arr[i].b
    return a, b


def partition_right(arr, a, low, high):
    i = low - 1
    for j in range(low, high):
        if arr[j].a <= a:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def partition_left(arr, b, low, t):
    i = low - 1
    for j in range(low, t):
        if arr[j].b < b:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[t] = arr[t], arr[i + 1]
    return i + 1


def fuzzy_sort(arr, low, high):
    if low < high:
        a, b = find_intersection(arr, low, high)
        t = partition_right(arr, a, low, high)
        q = partition_left(arr, b, low, t)
        fuzzy_sort(arr, low, q - 1)
        fuzzy_sort(arr, t + 1, high)


if __name__ == "__main__":
    i1 = Interval(2, 4)
    i2 = Interval(0, 2)
    i3 = Interval(5, 10)
    i4 = Interval(9, 16)
    i5 = Interval(20, 30)
    i6 = Interval(24, 27)
    array = [i4, i3, i6, i5, i1, i2]
    print("Unsorted Array: ", array)
    # Critical: Overlapping intervals do not require sorting
    # This causes best case running time O(n), when all intervals
    # overlap
    fuzzy_sort(array, 0, len(array) - 1)
    print("Sorted Array:   ", array)
