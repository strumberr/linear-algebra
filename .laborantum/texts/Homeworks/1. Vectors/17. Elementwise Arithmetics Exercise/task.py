import numpy as np



a_vector = np.array([2, 2, -1, 1])
b_vector = np.array([1, -1, 0.5, -0.5])


answer = {
    'task1': np.zeros(len(a_vector)),
    'task2': np.zeros(len(a_vector))
}

def task1(a, b):
    a = 2 * a
    summation = a + b
    division = summation / 2
    res = division + 5
    
    return res


def task2(a, b):
    b = 2 * b
    summation = a + b
    division = summation / a
    multiplication = division * 2
    res = np.sqrt(multiplication)
    
    return res


for (i, (a, b)) in enumerate(zip(a_vector, b_vector)):
    
    # task 1
    answer['task1'][i] = task1(a, b)
    
    # task 2
    answer['task2'][i] = task2(a, b)
    

# answer['task2'][2] = 0
    
print(answer['task1'])
print(answer['task2'])

    
