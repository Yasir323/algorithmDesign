def ternary_search(arr, low, high, target):
    lmid = low + (high - low) // 3
    rmid = high - (high - low) // 3
    if target < arr[lmid]:
        return ternary_search(arr, low, lmid - 1, target)
    elif target == arr[lmid]:
        return lmid
    elif target > arr[lmid] and target < arr[rmid]:
        return ternary_search(arr, lmid + 1, rmid - 1, target)
    elif target == arr[rmid]:
        return rmid
    elif target > arr[rmid]:
        return ternary_search(arr, rmid + 1, high, target)
    else:
        return -1


# Driver code
arr = [1, 2, 4, 5, 6, 6, 8, 9]
n = len(arr)
target = 5
print(ternary_search(arr, 0, n - 1, target))
