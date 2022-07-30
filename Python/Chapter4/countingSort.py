import itertools as it


def count_sort(arr, low, high):
    temp = [0] * (high - low + 1)
    sorted_array = [None] * len(arr)
    for a in arr:
        temp[a - low] += 1
    temp = list(it.accumulate(temp))
    print(temp)
    for a in arr:
        index = temp[a - low] - low
        print(a, index)
        temp[a - low] -= 1
        sorted_array[index] = a
    return sorted_array


if __name__ == '__main__':
    array = [3, 4, 6, 8, 9, 2, 1, 4, 5, 2]
    print(count_sort(array, min(array), max(array)))
