def binary_search(array, low, high, target):
    if low > high:
        return -1
    middle = low + (high - low) // 2
    if array[middle] == target:
        return middle
    if array[middle] < target:
        return binary_search(array, middle + 1, high, target)
    else:
        return binary_search(array, low, middle - 1, target)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'target',
        help='Number to search in the array.',
        type=int
    )
    args = parser.parse_args()
    arr = [1, 3, 4, 5, 7, 9]
    print(binary_search(arr, 0, len(arr) - 1, args.target))
