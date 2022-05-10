class DimensionMisMatchError(Exception):
    pass

def matrix_multiplication(a, b):
    m, n = len(a), len(a[0])
    x, y = len(b), len(b[0])
    if n != x:
        raise DimensionMisMatchError("Shape Mismatch. Shape of the matrices should be mxn and nxp.")
    res = [[0] * y for _ in range(m)]
    for i in range(m):
        for j in range(y):
            s = 0
            for k in range(x):
                s += a[i][k] * b[k][j]
            res[i][j] = s
    return res

if __name__ == '__main__':
    # take a 3x3 matrix
    A = [[12, 7, 3],
        [4, 5, 6],
        [7, 8, 9]]
     
    # take a 3x4 matrix   
    B = [[5, 8, 1, 2],
        [6, 7, 3, 0],
        [4, 5, 9, 1]]

    print(matrix_multiplication(A, B))
