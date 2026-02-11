import numpy as np

identitymatrix = np.eye(3)
diagonalarray = np.diag([1,2,3])
zeros_like_array = np.zeros_like(diagonalarray)
ones_like_array = np.ones_like(diagonalarray)

print(identitymatrix)
print(diagonalarray)
print(zeros_like_array)
print(ones_like_array)