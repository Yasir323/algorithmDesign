"""
Find i-th highest/lowest number in expected linear time.  
"""

import random


def randomized_partition(arr, low, high):
    i = random.randint(low, high)
    arr[i], arr[high] = arr[high], arr[i]
    return partition(arr, low, high)


def partition(array, low, high):
    p = high
    first_high = low - 1
    for i in range(low, high):
        if array[i] < array[p]:  # Reverse the operation to get nth highest
            first_high += 1
            array[i], array[first_high] = array[first_high], array[i]
    array[p], array[first_high + 1] = array[first_high + 1], array[p]
    return first_high + 1


def randomized_select(arr, low, high, i):
    if low == high:
        return arr[low]

    p = randomized_partition(arr, low, high)
    k = p - low + 1
    if i == k:
        return arr[p]
    elif i < k:
        return randomized_select(arr, low, p - 1, i)
    else:
        return randomized_select(arr, p + 1, high, i - k)  # ******* PAY ATTENTION TO THIS LINE


if __name__ == "__main__":
    array = list(set([random.randint(0, 20) for _ in range(10)]))
    n = len(array)
    print(array)
    print("3rd lowest element: ", randomized_select(array, 0, n - 1, 3))
