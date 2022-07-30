import itertools as it


def insertion_sort(arr):
    for i in range(1, len(arr)):
        up = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > up: 
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = up     
    return arr


def bucket_sort(arr):
    # Build the bucket
    num_buckets = 10
    temp = [[] for _ in range(num_buckets)]
    # Fill the buckets
    for a in arr:
        index = int(a * num_buckets)
        temp[index].append(a)
    # Sort the individual buckets
    for t in temp:
        t = insertion_sort(t)
    # Concatenate the result
    return list(it.chain.from_iterable(temp))


def bucket_sort_for_larger_nums(arr, num_buckets):
    min_ = min(arr)
    max_ = max(arr)
    range_ = ((max_ - min_) // num_buckets) + 1
    # Build the bucket
    temp = [[] for _ in range(num_buckets)]
    # Fill the buckets
    for a in arr:
        index = int((a - min_) / range_)
        temp[index].append(a)
    # Sort the individual buckets
    for t in temp:
        t = insertion_sort(t)
    # Concatenate the result
    return list(it.chain.from_iterable(temp))


if __name__ == '__main__':
    array = [0.897, 0.565, 0.656,
     0.1234, 0.665, 0.3434] 
    print("Sorted Array is")
    print(bucket_sort(array))
    
    array2 = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]
    print(bucket_sort_for_larger_nums(array2, 5))
