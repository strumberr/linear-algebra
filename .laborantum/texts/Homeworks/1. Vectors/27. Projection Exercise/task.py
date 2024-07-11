import numpy as np

answer = {
    'proj_a_b': 0,
    'orth_a_b': 0,
    'proj_b_a': 0,
    'orth_b_a': 0
}

a = np.array([6, 3, 2, 1, 0])
b = np.array([1, 1, 3, 3, 4])


proj_a_b = (np.dot(a, b) / np.dot(b, b)) * b
answer['proj_a_b'] = proj_a_b

orth_a_b = a - proj_a_b
answer['orth_a_b'] = orth_a_b

proj_b_a = (np.dot(a, b) / np.dot(a, a)) * a
answer['proj_b_a'] = proj_b_a

orth_b_a = b - proj_b_a
answer['orth_b_a'] = orth_b_a


print(answer)