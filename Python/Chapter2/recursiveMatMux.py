import numpy as np
import warnings
warnings.filterwarnings('ignore')


def add(a, b):
    """O(n^2)"""
    n = len(a)
    c = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] + b[i][j]
    return c


def partition(matrix, n):
    """O(n^2)"""
    p11 = [[matrix[i][j] for j in range(n//2)] for i in range(n//2)]
    p12 = [[matrix[i][j] for j in range(n//2, n)] for i in range(n//2)]
    p21 = [[matrix[i][j] for j in range(n//2)] for i in range(n//2, n)]
    p22 = [[matrix[i][j] for j in range(n//2, n)] for i in range(n//2, n)]
    return p11, p12, p21, p22


def combine(p11, p12, p21, p22):
    """O(n)"""
    p = []
    n = len(p11)
    for i in range(n):
        p += [p11[i] + p12[i]]
    for i in range(n):
        p += [p21[i] + p22[i]]
    return p


def matmul(a, b):
    n = len(a)
    c = [[None for _ in range(n)] for _ in range(n)]
    if n == 1:
        c[0][0] = a[0][0] * b[0][0]
    else:
        a11, a12, a21, a22 = partition(a, n)
        b11, b12, b21, b22 = partition(b, n)
        c11, c12, c21, c22 = partition(c, n)
        c11 = add(matmul(a11, b11), matmul(a12, b21))
        c12 = add(matmul(a11, b12), matmul(a12, b22))
        c21 = add(matmul(a21, b11), matmul(a22, b21))
        c22 = add(matmul(a21, b12), matmul(a22, b22))
        c = combine(c11, c12, c21, c22)
    return c


if __name__ == '__main__':
    # take a 3x3 matrix
    A = [[12, 7, 3, 2],
        [4, 5, 6, 4],
        [2, 3, 4, 5],
        [7, 8, 9, 6]]

    # take a 3x4 matrix   
    B = [[5, 8, 1, 8],
        [6, 7, 3, 10],
        [2, 3, 4, 5],
        [4, 5, 9, 12]]

    print(matmul(A, B))
