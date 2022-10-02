"""
Give an algorithm that k-sorts an n-element array in O(n * log(n/k)) time.

Shell-Sort, i.e., We split the n-element array into k part. For 
each part, we use Insertion-Sort (or Quicksort) to sort in 
O(n/k log(n/k)) time. Therefore, the total 
running time is k⋅O(n/k log(n/k)) = O(n log(n/k))
"""


def shell_sort(arr, n, k=1):
    gap = k
    j = gap
    while j < n:
        i = j - gap
        while i >= 0:
            if arr[i + gap] < arr[i]:
                arr[i + gap], arr[i] = arr[i], arr[i + gap]
            i -= gap  # To check on the left side also
        j += 1


if __name__ == "__main__":
    arr2 = [12, 34, 54, 2, 3]
    print("input array:",arr2)
      
    shell_sort(arr2, len(arr2), 3)
    print("sorted array",arr2)
