import sys


def maximum_subarray(arr):
    """Using Brute force. O(n^2)"""
    max = -sys.maxsize
    arr = [arr[j] - arr[j - 1] for j in range(1, len(arr))]
    n = len(arr)
    index = ()
    for i in range(n - 1):
        sum = arr[i]
        for j in range(i + 1, n):
            sum += arr[j]
            if sum > max:
                max = sum
                index = (i + 1, j + 1)
    return max, index


if __name__ == '__main__':
    array = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101, 79, 94, 90, 97]
    print(maximum_subarray(array))
