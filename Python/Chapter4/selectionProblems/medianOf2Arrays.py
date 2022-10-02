"""
Let X[1..n]X[1..n] and Y[1..n]Y[1..n] be two 
arrays, each containing nn numbers already in 
sorted order. Give an O(\lg n)O(lgn)-time 
algorithm to find the median of all 2n2n elements 
in arrays XX and YY.
"""


def median(x, y, n):
    if n == 1: return min(x[0], y[0])
    if x[n//2] < y[n//2]:
        return median(x[n//2+1:], y[:n//2+1], n//2)
    return median(x[:n//2+1], y[n//2+1:], n//2)


if __name__ == "__main__":
    a = [i for i in range(1, 11, 2)]
    b = [i for i in range(2, 11, 2)]
    n = len(a)
    print(median(a, b, n))
