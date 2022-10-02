"""
Program to sort a k-sorted array

The algorithm uses quick sort but changes the partition function 
in 2 ways.

1. Selects pivot element as the middle element instead of the 
first or last element.
2. Scans the array from max(low, mid – k) to min(mid + k, high) 
instead of low to high.
"""


def quick_sort(array, low, high, k):  # O(log(n))
    if low < high:
        partition_index = partition(array, low, high, k)
        quick_sort(array, low, partition_index - 1, k)
        quick_sort(array, partition_index + 1, high, k)


def partition(array, low, high, k):  # O(k)
    mid = low + (high - low) // 2
    first_high = max(low, mid - k)
    p = min(mid + k, high)
    array[mid], array[p] = array[p], array[mid]
    for i in range(first_high, p):
        if array[i] < array[p]:
            array[i], array[first_high] = array[first_high], array[i]
            first_high += 1
    array[p], array[first_high] = array[first_high], array[p]
    return first_high


if __name__ == '__main__':
    nums = [3, 3, 2, 1, 6, 4, 4, 5, 9, 7, 8, 11, 12]
    k = 3
    quick_sort(nums, 0, len(nums) - 1, k)
    print(nums)
