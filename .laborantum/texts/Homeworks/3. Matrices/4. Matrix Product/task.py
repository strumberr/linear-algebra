import numpy as np

answer = {
    'task1': 1,
    'task2': 2,
    'task3': 3
}

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

B = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

answer['task1'] = np.dot(A, B)


C = np.array([
    [1, 2],
    [3, 4]
])

D = np.array([
    [1, 2],
    [3, 4]
])

E = np.array([
    [1, 2],
    [3, 4]
])

# matrix poroduct
answer['task2'] = np.dot(np.dot(C, D), E)

# print(answer['task2'])


F = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 0]
])

G = np.array([
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8],
    [9, 0]
])

H = np.array([
    [1],
    [2]
])

# matrix product
answer['task3'] = np.dot(np.dot(F, G), H)

# print(answer['task3'])