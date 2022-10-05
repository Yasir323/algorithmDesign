from typing import List


def quick_sort(array: List[int], low: int, high: int):
    if low < high:
        partition_index: int = partition(array, low, high)
        quick_sort(array, low, partition_index)
        quick_sort(array, partition_index + 1, high)


def partition(arr: List[int], low: int, high: int):  # O(n)
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 8, 0, 2, 2]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
