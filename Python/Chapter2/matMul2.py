"""
Matrix Multiplication using LIst Comprehension.
"""

# take a 3x3 matrix
A = [[12, 7, 3],
    [4, 5, 6],
    [7, 8, 9]]
 
# take a 3x4 matrix   
B = [[5, 8, 1, 2],
    [6, 7, 3, 0],
    [4, 5, 9, 1]]

m = len(A)  # No of rows of A
n = len(A[0])  # No of cols of A
p = len(B)  # No of rows of B
q = len(B[0])  # No of cols of B

res = [[sum([a * b for a, b in zip(row_a, col_b)])
                    for col_b in zip(*B)]
                    for row_a in A]
print(res)
