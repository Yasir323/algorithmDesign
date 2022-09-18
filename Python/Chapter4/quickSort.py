from typing import List


def quick_sort(array: List[int], low: int, high: int):
    if low < high:
        partition_index: int = partition(array, low, high)
        quick_sort(array, low, partition_index - 1)
        quick_sort(array, partition_index + 1, high)


def partition(array: List[int], low: int, high: int):  # O(n)
    p = high
    first_high = low - 1
    for i in range(low, high):
        if array[i] < array[p]:
            first_high += 1
            array[i], array[first_high] = array[first_high], array[i]
    array[p], array[first_high + 1] = array[first_high + 1], array[p]
    return first_high + 1


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 8, 0, 2, 2]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
