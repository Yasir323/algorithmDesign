import random

"""
Find min and max in an array using at most 3(n/2) comparisons.
"""


def find(arr, n):
    if n % 2 == 0:
        i = 2
        first, second = arr[0], arr[1]
        if first < second:
            min_, max_ = first, second
        else:
            min_, max_ = second, first
    else:
        i = 1
        min_ = max_ = arr[0]
    while i < n:
        # First we compare the 2 numbers from the array,
        # then we'll compare lower with the minimum and
        # higher with the maximum.
        first, second = arr[i], arr[i+1]
        if first < second:
            if first < min_:
                min_ = first
            if second > max_:
                max_ = second
        else:
            if second < min_:
                min_ = second
            if first > max_:
                max_ = first
        i += 2
    return min_, max_


if __name__ == "__main__":
    array = [random.randint(0, 20) for _ in range(10)]
    print(array)
    minimum, maximum = find(array, len(array))
    print(f"Minimum: {minimum}\tMaximum: {maximum}")
