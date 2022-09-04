def bubble_sort(array):
    n = len(array)
    while n > 0:
        for j in range(n - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        n -= 1


# Driver code to test above
arr = [12, 11, 13, 5, 6]
print(f"Unsorted Array: {arr}")
bubble_sort(arr)
print(f"Sorted Array: {arr}")
