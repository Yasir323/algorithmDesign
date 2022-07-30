import itertools as it


def count_sort(arr, exp1):
    n = len(arr)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radix_sort(arr):
    max_ = max(arr)
    exp = 1
    while max_ / exp > 1:
        count_sort(arr, exp)
        exp *= 10


if __name__ == '__main__':
    array = [3, 4, 6, 8, 9, 2, 1, 4, 5, 2]
    radix_sort(array)
    print(array)
