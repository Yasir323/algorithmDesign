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


def subtract(a, b):
    """O(n^2)"""
    n = len(a)
    c = [[None for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = a[i][j] - b[i][j]
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
        
        s1 = subtract(b12, b22)
        s2 = add(a11, a12)
        s3 = add(a21, a22)
        s4 = subtract(b21, b11)
        s5 = add(a11, a22)
        s6 = add(b11, b22)
        s7 = subtract(a12, a22)
        s8 = add(b21, b22)
        s9 = subtract(a11, a21)
        s10 = add(b11, b12)
        
        p1 = subtract(matmul(a11, b12), matmul(a11, b22))
        p2 = add(matmul(a11, b22), matmul(a12, b22))
        p3 = add(matmul(a21, b11), matmul(a22, b11))
        p4 = subtract(matmul(a22, b21), matmul(a22, b11))
        p5 = add(add(add(matmul(a11, b11), matmul(a11, b22)), matmul(a22, b11)), matmul(a22, b22))
        p6 = subtract(subtract(add(matmul(a12, b21), matmul(a12, b22)), matmul(a22, b21)), matmul(a22, b22))
        p7 = subtract(subtract(add(matmul(a11, b11), matmul(a11, b12)), matmul(a21, b11)), matmul(a21, b12))

        c11 = add(subtract(add(p5, p4), p2), p6)
        c12 = add(p1, p2)
        c21 = add(p3, p4)
        c22 = subtract(subtract(add(p5, p1), p3), p7)
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
