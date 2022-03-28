def is_jolly(array):
    n = len(array)
    differences = [abs(j-i) for i, j in zip(array[:-1], array[1:])]
    for difference in differences:
        if difference > n - 1 or difference < 1:
            return False
    return True

print(is_jolly([1, 4, 2, 3]))
print(is_jolly([1, 4, 2, -1, 6]))
print(is_jolly([11, 7, 4, 2, 1, 6]))
