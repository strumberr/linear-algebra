import numpy as np

answer = {
    'task1': 0
}

A = np.array([
    [1, 2, 2],
    [2, 1, 2],
    [2, 2, 1]
])

x = np.array([1, 1, -1])

Ax = np.dot(A, x)

norm_Ax = np.linalg.norm(Ax)
norm_x = np.linalg.norm(x)

answer['task1'] = norm_Ax / norm_x

print(answer['task1'])

# 3. Matrices
# 	5 - result says 16.0312195418814 but I get 1.9148542155126762
