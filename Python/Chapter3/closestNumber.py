def get_closest(val1, val2, target):
    if abs(val1 - target) <= abs(val2 - target):
        return val1
    else:
        return val2


def find_closest(arr, n, target):
    """
    Using Binary Search find the number closest 
    to target in the given sorted array
    """
    if target <= arr[0]:
        return arr[0]
    elif target >= arr[n - 1]:
        return arr[n - 1]
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return arr[mid]
        elif target < arr[mid]:
            if (mid > 0 and arr[mid - 1] < target):
                return get_closest(arr[mid - 1], arr[mid], target)
            right = mid
        else:
            if (mid < n - 1 and arr[mid + 1] > target):
                return get_closest(arr[mid], arr[mid + 1], target)
            left = mid + 1
    return arr[mid]
       
    
if __name__ == "__main__":
    arr = [1, 2, 4, 5, 6, 6, 8, 9]
    n = len(arr)
    target = 7
    print(find_closest(arr, n, target))
