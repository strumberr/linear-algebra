import numpy as np

answer = {
    'task': 1
}

n = 100
matrix = np.zeros((n, n), dtype=int)
np.fill_diagonal(matrix, np.arange(1, n + 1))
matrix[np.triu_indices(n, 1)] = 1

A = matrix
B = matrix
