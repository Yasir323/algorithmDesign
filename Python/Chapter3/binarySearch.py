def binary_search(arr, n, target):
    if target < arr[0] or target > arr[n -1]:
        return -1
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9]
n = len(arr)
target = 5
print(binary_search(arr, n, target))
