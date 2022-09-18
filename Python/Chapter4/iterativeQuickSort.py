from collections import deque


def partition(arr, low, high):
    first_higher = low - 1
    p = arr[high]  # Pivot Element
    for i in range(low, high):
        if arr[i] <= p:
            first_higher += 1
            arr[first_higher], arr[i] = arr[i], arr[first_higher]
    arr[first_higher + 1], arr[high] = arr[high], arr[first_higher + 1]
    return first_higher + 1


def quick_sort(arr, l, h):
    size = h - l + 1
    stack = deque([0] * size, maxlen=size)
    top = -1

    top += 1
    stack.append(l)
    top += 1
    stack.append(h)
    while top >= 0:
        h = stack.pop()
        top -= 1
        l = stack.pop()
        top -= 1
        p = partition(arr, l, h)
        if p - 1 > l:
            top += 1
            stack.append(l)
            top += 1
            stack.append(p - 1)
        if p + 1 < h:
            top += 1
            stack.append(p + 1)
            top += 1
            stack.append(h)


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 8, 0, 2, 2]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)
