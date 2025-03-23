import numpy as np

# Vector with values from 10 to 49
vector = np.arange(10, 50)
print("Vector:", vector)

# 3x3 matrix with values from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 Matrix:\n", matrix_3x3)

# 3x3 identity matrix
identity_matrix = np.eye(3)
print("Identity Matrix:\n", identity_matrix)

# 3x3x3 array with random values
random_array_3x3x3 = np.random.random((3, 3, 3))
print("3x3x3 Random Array:\n", random_array_3x3x3)

# 10x10 array with random values and min/max
random_array_10x10 = np.random.random((10, 10))
min_val, max_val = random_array_10x10.min(), random_array_10x10.max()
print("Min Value:", min_val, "Max Value:", max_val)

# Random vector of size 30 and mean value
random_vector_30 = np.random.random(30)
mean_value = random_vector_30.mean()
print("Mean Value:", mean_value)

# Normalize a 5x5 random matrix
random_matrix_5x5 = np.random.random((5, 5))
norm_matrix = (random_matrix_5x5 - random_matrix_5x5.min()) / (random_matrix_5x5.max() - random_matrix_5x5.min())
print("Normalized Matrix:\n", norm_matrix)

# Multiply a 5x3 matrix by a 3x2 matrix
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
result_matrix = np.dot(matrix_5x3, matrix_3x2)
print("5x3 * 3x2 Matrix Product:\n", result_matrix)

# Compute dot product of two 3x3 matrices
matrix_a = np.random.random((3, 3))
matrix_b = np.random.random((3, 3))
dot_product = np.dot(matrix_a, matrix_b)
print("Dot Product of 3x3 Matrices:\n", dot_product)

# Transpose of a 4x4 matrix
matrix_4x4 = np.random.random((4, 4))
matrix_transpose = matrix_4x4.T
print("Transpose of 4x4 Matrix:\n", matrix_transpose)

# Determinant of a 3x3 matrix
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)
print("Determinant of 3x3 Matrix:", determinant)

# Compute matrix product of A (3x4) and B (4x3)
A = np.random.random((3, 4))
B = np.random.random((4, 3))
matrix_product = np.dot(A, B)
print("Matrix Product A * B:\n", matrix_product)

# Matrix-vector product
matrix_3x3 = np.random.random((3, 3))
vector_3x1 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)
print("Matrix-Vector Product:\n", matrix_vector_product)

# Solve linear system Ax = b
A = np.random.random((3, 3))
b = np.random.random((3, 1))
x = np.linalg.solve(A, b)
print("Solution to Ax = b:\n", x)

# Row-wise and column-wise sums of a 5x5 matrix
matrix_5x5 = np.random.random((5, 5))
row_sums = matrix_5x5.sum(axis=1)
col_sums = matrix_5x5.sum(axis=0)
print("Row-wise Sums:", row_sums)
print("Column-wise Sums:", col_sums)
