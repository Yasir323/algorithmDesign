"""
Shell sort is mainly a variation of Insertion Sort. In insertion 
sort, we move elements only one position ahead. When an element 
has to be moved far ahead, many movements are involved. The idea 
of ShellSort is to allow the exchange of far items. In Shell 
sort, we make the array k-sorted for a large value of k. We keep 
reducing the value of k until it becomes 1. An array is said to 
be k-sorted if all sublists of every k’th element are sorted.

Algorithm:

Step 1 − Start
Step 2 − Initialize the value of gap size. Example: k
Step 3 − Divide the list into smaller sub-part. Each must have 
    equal intervals to k
Step 4 − Sort these sub-lists using insertion sort
Step 5 – Repeat this step 2 until the list is sorted.
Step 6 – Print a sorted list.
Step 7 – Stop.
"""


def shell_sort(arr, n):
    gap = n // 2
    while gap > 0:
        j = gap  # To move to right side
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] < arr[i]:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i -= gap  # To check on the left side also
            j += 1
        gap = gap // 2


if __name__ == "__main__":
    arr2 = [12, 34, 54, 2, 3]
    print("input array:",arr2)
      
    shell_sort(arr2, len(arr2))
    print("sorted array",arr2)
