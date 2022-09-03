import math


def bsearch(arr, target):
    n = len(arr)
    num_bits = int(math.log2(n - 1)) + 1
    pos = 0
    for i in range(num_bits - 1, -1, -1):
        if arr[pos] == target:
            return pos
        new_pos = pos | (1 << i)
        if (new_pos < n) and (arr[new_pos] <= target):
            pos = new_pos
    return (pos if arr[pos] == target else -1)


if __name__ == "__main__":
    array = [ -2, 10, 100, 250, 32315 ]
    print( bsearch(array, 10))
