import math


def linear_search(arr, start, end, target):
    for i in range(end, start + 1):
        if arr[i] == target:
            return i
    return -1


def jump_search(arr, n, target):
    step = math.floor(math.sqrt(n))
    i = 0
    while i < n:
        if arr[i] == target:
            return i
        elif arr[i] > target:
            return linear_search(arr, i - step + 1, i - 1, target)
        else:
            i += step
    return -1

# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9]
n = len(arr)
target = 5
print(jump_search(arr, n, target))
