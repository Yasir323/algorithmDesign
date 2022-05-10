def selection_sort(array):
    n = len(array)
    for i in range(n):
        smallest = i
        for j in range(i, n):
            if array[j] <= array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]


# Driver code to test above
arr = [12, 11, 13, 5, 6]
print(f"Unsorted Array: {arr}")
selection_sort(arr)
print(f"Sorted Array: {arr}")
