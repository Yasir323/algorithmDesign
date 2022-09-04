def binary_search(arr, left, right, target):
    if target < arr[0] or target > arr[right]:
        return -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def exponential_search(arr, low, high, target):
    i = low
    while i <= high:
        if target == arr[i]:
            return i
        elif target < arr[i]:
            return binary_search(arr, i // 2, i - 1, target)
        i = i * 2 if i > 0 else i + 1
    return -1


# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9]
n = len(arr)
target = 5
print(exponential_search(arr, 0, n - 1, target))
