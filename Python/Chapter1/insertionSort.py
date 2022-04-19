def insertionSort(arr):
    for i in range(len(arr)):
        curr = arr[i]
        j = i - 1
        while j >= 0 and curr < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr
    return arr
                

# Driver code to test above
arr = [12, 11, 13, 5, 6]
print(f"Unsorted Array: {arr}")
insertionSort(arr)
print(f"Sorted Array: {arr}")
