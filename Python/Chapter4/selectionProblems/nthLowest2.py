"""
Find i-th highest/lowest number in worst case linear time.  
"""

import random


def modified_partition(array, low, high, x):
    for i in range(low, high + 1):
        if array[i] == x:
            array[i], array[high] = array[high], array[i]
            break
    p = high
    first_high = low - 1
    for i in range(low, high + 1):
        if array[i] <= x:
            first_high += 1
            array[i], array[first_high] = array[first_high], array[i]
    array[p], array[first_high + 1] = array[first_high + 1], array[p]
    return first_high + 1


def select(arr, low, high, j):
    if low == high:
        return arr[low]
    medians = []
    i = 0
    n = high - low + 1
    while i < n // 5:
        medians.append(find_median(arr, low + i * 5, 5))
        i += 1
    if i * 5 < n:
        medians.append(find_median(arr, low + i * 5, n % 5))
        i += 1
    if i == 1:
        x = medians[i - 1]
    else:
        x = select(medians, 0, i - 1, i // 2)
    p = modified_partition(arr, low, high, x)
    k = p - low + 1
    if j == k:
        return arr[p]
    elif j < k:
        return select(arr, low, p - 1, j)
    else:
        return select(arr, p + 1, high, j - k)


def find_median(arr, low, n):
    ls = []
    for i in range(low, low + n):
        ls.append(arr[i])
    ls.sort()
    return ls[n // 2]


if __name__ == "__main__":
    array = list(set([random.randint(0, 30) for _ in range(20)]))
    n = len(array)
    random.shuffle(array)
    print(sorted(array))
    print("3rd lowest element: ", select(array, 0, n - 1, 3))
