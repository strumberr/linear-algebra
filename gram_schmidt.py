import numpy as np


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

vectors = [
    np.array([1, 0]), 
    np.array([0, 1]), 
]

orthonormal_set = gram_schmidt(vectors)

if(len(orthonormal_set) == len(vectors)):
    print("The set of vectors is linearly independent")
else:
    print("The set of vectors is linearly dependent")

for vector in orthonormal_set:
    print(vector)
    