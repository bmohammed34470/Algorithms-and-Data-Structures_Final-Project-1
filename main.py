import numpy as np
import time

# Create a sparse matrix (largely filled with zeros)
# Use a dictionary to represent the sparse matrix (key: (row, col), value: matrix element)
sparse_matrix = {
    (0, 0): 1,
    (1, 1): 2,
    (2, 2): 3,
    (3, 3): 4,
    (4, 4): 5
}

# Create a dense matrix of the same shape for comparison
dense_matrix = np.zeros((5, 5))
dense_matrix[0, 0] = 1
dense_matrix[1, 1] = 2
dense_matrix[2, 2] = 3
dense_matrix[3, 3] = 4
dense_matrix[4, 4] = 5

# Function to sum elements in the sparse matrix
def sum_sparse(matrix, shape):
    total_sum = 0
    for (i, j), value in matrix.items():
        total_sum += value
    return total_sum

# Time the summation operation for the dense matrix
start_time = time.time()
dense_matrix_sum = np.sum(dense_matrix)
end_time = time.time()
dense_matrix_time = end_time - start_time

# Time the summation operation for the sparse matrix
start_time = time.time()
sparse_matrix_sum = sum_sparse(sparse_matrix, (5, 5))
end_time = time.time()
sparse_matrix_time = end_time - start_time

# Output the performance comparison results
print("\nDense Matrix Summation Time: {:.6f} seconds".format(dense_matrix_time))
print("Sparse Matrix Summation Time: {:.6f} seconds".format(sparse_matrix_time))

# Show the difference in memory usage
dense_memory = dense_matrix.nbytes

# Calculate memory for the sparse matrix
# Memory for dictionary keys (tuples), values (integers)
sparse_memory = len(sparse_matrix) * (2 * 8) + sum(value.bit_length() // 8 + 1 for value in sparse_matrix.values())
print("\nMemory Usage Comparison:")
print(f"Dense Matrix Memory Usage: {dense_memory} bytes")
print(f"Sparse Matrix Memory Usage: {sparse_memory} bytes")
