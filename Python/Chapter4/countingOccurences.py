def modified_binary_search(array, low, high, target):
    left_index = left_boundary(array, low, high, target)
    right_index = right_boundary(array, low, high, target)
    return right_index - left_index + 1


def right_boundary(array, low, high, target):
    """
    If we remove the equality condition form the Binary Search
    we will never find the target, and when the base condition
    is satisfied, if we return high instead of -1 and have >
    condition first, we end up on the right side and get the
    last index of the target.
    """
    if low > high:
        return high
    middle = low + (high - low) // 2
    if array[middle] > target:
        return right_boundary(array, low, middle - 1, target)
    else:
        return right_boundary(array, middle + 1, high, target)


def left_boundary(array, low, high, target):
    """
    If we remove the equality condition form the Binary Search
    we will never find the target, and when the base condition
    is satisfied, if we return low instead of -1 and have <
    condition first, we end up onm the left side and get the
    first index of the target.
    """
    if low > high:
        return low
    middle = low + (high - low) // 2
    if array[middle] < target:
        return left_boundary(array, middle + 1, high, target)
    else:
        return left_boundary(array, low, middle - 1, target)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'target',
        help='Number to search in the array.',
        type=int
    )
    args = parser.parse_args()
    arr = [1, 3, 4, 4, 5, 5, 5, 5, 7, 9]
    print(modified_binary_search(arr, 0, len(arr) - 1, args.target))
