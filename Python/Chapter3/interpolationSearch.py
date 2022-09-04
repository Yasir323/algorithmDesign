def interpolation_search(arr, low, high, target):
    index = low + ((target - arr[low]) // (arr[high] - arr[low]) * (high - low))
    if arr[index] == target:
        return index
    elif arr[index] > target:
        return interpolation_search(arr, low, index - 1, target)
    elif arr[index] < target:
        return interpolation_search(arr, index + 1, high, target)
    return -1


# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9]
n = len(arr)
target = 5
print(interpolation_search(arr, 0, n - 1, target))
