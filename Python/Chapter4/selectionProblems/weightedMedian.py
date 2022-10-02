"""
Find the weighted median.
"""


def weighted_median(arr):
    sorted_arr = list(sorted(arr, key=lambda x: x[1]))
    total_weight = 0
    for i in range(len(sorted_arr)):
        total_weight += sorted_arr[i][1]
        if total_weight >= 0.5:
            return sorted_arr[i - 1][0]


if __name__ == "__main__":
    array = [(2, 0.1), (3, 0.15), (1, 0.35), (5, 0.02), (4, 0.38)]
    print(weighted_median(array))
