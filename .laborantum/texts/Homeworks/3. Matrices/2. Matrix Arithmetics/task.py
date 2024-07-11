import numpy as np

answer = {
   'task': None
}

A = np.array([
   [1, 2, 3], 
   [4, 5, 6],
   [7, 8, 9]
   ])

B = np.array([
   [9, 8, 7],
   [6, 5, 4],
   [3, 2, 1]])

result = 5 * A - 4 * B

print(result)

answer['task'] = result