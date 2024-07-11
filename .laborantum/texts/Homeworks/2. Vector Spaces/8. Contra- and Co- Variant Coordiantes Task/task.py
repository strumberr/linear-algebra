import numpy as np

answer = {
    'x_a_contra': [-1, -1,  3],
    'x_a_co': [1, 3, 6],
    'x_b_contra': [1, 1, 1],
    'x_b_co': [6, 5, 3],
    'y_a_contra': [-1, -1,  5],
    'y_a_co': [3,  7, 12],
    'y_b_contra': [3, 1, 1],
    'y_b_co': [12,  9,  5]
}



# I also coded it here to understand the better logic of the solution
# X = np.array([1, 2, 3])
# Y = np.array([3, 4, 5])

# a1, a2, a3, = np.array([1, 0, 0]), np.array([1, 1, 0]), np.array([1, 1, 1])

# b1, b2, b3, = np.array([1, 1, 1]), np.array([0, 1, 1]), np.array([0, 0, 1])


# # contravariant
# def contravariant(a1, a2, a3, X):
#     A_contra = np.array([a1, a2, a3]).T
#     X_contra = np.linalg.solve(A_contra, X)
#     return X_contra

# #covariant
# def covariant(X, a1, a2, a3):
#     A_cov = np.array([a1, a2, a3])
#     X_cov = np.dot(A_cov, X)
#     return X_cov


# answer['x_a_contra'] = contravariant(a1, a2, a3, X)
# answer['x_a_co'] = covariant(X, a1, a2, a3)

# answer['x_b_contra'] = contravariant(b1, b2, b3, X)
# answer['x_b_co'] = covariant(X, b1, b2, b3)

# answer['y_a_contra'] = contravariant(a1, a2, a3, Y)
# answer['y_a_co'] = covariant(Y, a1, a2, a3)

# answer['y_b_contra'] = contravariant(b1, b2, b3, Y)
# answer['y_b_co'] = covariant(Y, b1, b2, b3)

# print(answer)
