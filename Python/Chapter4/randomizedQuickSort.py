import random


def randomized_quick_sort(array, low, high):
    if low < high:
        partition_index = randomized_partition(array, low, high)
        randomized_quick_sort(array, low, partition_index - 1)
        randomized_quick_sort(array, partition_index + 1, high)


def randomized_partition(arr, low, high):
    i = random.randint(low, high)
    arr[i], arr[high] = arr[high], arr[i]
    return partition(arr, low, high)


def partition(array, low, high):  # O(n)
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
    randomized_quick_sort(nums, 0, len(nums) - 1)
    print(nums)
