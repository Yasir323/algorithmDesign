"""
Matrix Multiplication using Numpy.
"""

import numpy as np
# take a 3x3 matrix
A = [[12, 7, 3],
	[4, 5, 6],
	[7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
	[6, 7, 3, 0],
	[4, 5, 9, 1]]

# result will be 3x4

result= [[0,0,0,0],
		[0,0,0,0],
		[0,0,0,0]]

result = np.dot(A,B)

for r in result:
	print(r)
