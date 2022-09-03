import sys


def max_crossing_subarray(arr, low, mid, high):
    left_sum = -sys.maxsize
    sum = 0
    for i in range(mid, low - 1, -1):
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    right_sum = -sys.maxsize
    sum = 0
    for j in range(mid + 1, high + 1):
        sum += arr[j]
        if sum > right_sum:
            right_sum = sum
            max_right = j
    return left_sum + right_sum, max_left, max_right


def max_subarray(arr, low, high):
    """Using Divide and Conquer. O(n*log(n))"""
    if low == high:
        return arr[low], low, high
    mid = (low + high) // 2
    left_sum, left_low, left_high = max_subarray(arr, low, mid)
    right_sum, right_low, right_high = max_subarray(arr, mid + 1, high)
    cross_sum, cross_low, cross_high = max_crossing_subarray(arr, low, mid, high)
    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_sum, left_low, left_high
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_sum, right_low, right_high
    else:
        return cross_sum, cross_low, cross_high


if __name__ == '__main__':
    array = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    array = [array[i] - array[i - 1] for i in range(1, len(array))]
    sum, left, right = max_subarray(array, 0, len(array) - 1)
    print(sum, left + 1, right + 1)
