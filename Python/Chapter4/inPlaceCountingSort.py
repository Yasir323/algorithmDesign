import itertools as it


def count_sort(arr, low, high):
    c = [0] * (high - low + 1)
    for a in arr:
        c[a - low] += 1
    c = list(it.accumulate(c))
    arr.insert(0, None)
    b = c[:len(c)-1]
    b.insert(0, 1)  # c now contains the "endpoints" for c
    print(b)
    print(c)
    for i in range(1, len(arr)):
        print(arr[i])
        while c[arr[i] - low] != b[arr[i] - low]:
            key = arr[i]
            arr[c[arr[i] - low]], arr[i] = arr[i], arr[c[arr[i] - low]]
            while arr[c[key - low]] == key:  # make sure that elements with the same keys will not be swapped
                c[key - low] -= 1
    arr.pop(0)
    return arr


if __name__ == '__main__':
    array = [3, 4, 6, 8, 9, 2, 1, 4, 5, 2]
    print(count_sort(array, min(array), max(array)))
