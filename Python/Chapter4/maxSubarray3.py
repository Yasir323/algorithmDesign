import sys


def max_subarray(arr):
    """O(n) solution."""
    n = len(arr)
    max_sum = -sys.maxsize
    low, high = None, None
    sum_ = 0
    l = 0
    for i in range(n):  # O(n)
        sum_ += arr[i]
        if sum_ > max_sum:
            low = l
            high = i
            max_sum = sum_
        if sum_ < 0:
            sum_ = 0
            l = i + 1
    return max_sum, low + 1, high + 1  # O(n)

if __name__ == '__main__':
    array = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    array = [array[i] - array[i - 1] for i in range(1, len(array))]
    print(max_subarray(array))
