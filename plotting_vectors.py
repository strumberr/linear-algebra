import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# using matplotlib, plot 5 dimensional vectors
vectors = [
    np.array([1, 0, 0]),
    np.array([0, 1, 0]),
    np.array([0, 0, 1]),
]

def project(u, v):
    return np.dot(u, v) / np.dot(v, v) * v

def gram_schmidt(vectors):
    
    u = []
    
    for v in vectors:
        t_v = v
        for vector in u:
            t_v = t_v - project(v, vector)
            
        if np.linalg.norm(t_v) > 1e-6:
            t_v = t_v / np.linalg.norm(t_v)
            u.append(t_v)
    
    return u

# check if the vectors are linearly independent
orthonormal_set = gram_schmidt(vectors)



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for vector in vectors:
    ax.quiver(0, 0, 0, vector[0], vector[1], vector[2])

ax.set_xlim([0, 1])
ax.set_ylim([0, 1])
ax.set_zlim([0, 1])

plt.show()