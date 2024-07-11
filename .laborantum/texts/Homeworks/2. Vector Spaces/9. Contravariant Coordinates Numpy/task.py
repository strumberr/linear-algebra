#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

get_ipython().system('{sys.executable} -m pip -q install --user numpy json-tricks torch jupyter nbconvert')


# In[2]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/2. Vector Spaces/9. Contravariant Coordinates Numpy')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[3]:


import numpy as np

def vectors_from_contravariant_coords(B, C):
    """
    # B is a set of N basis vectors, row-matrix form, size NxM
    # C is a set of N contravariant coordinates, 
    # in that basis C for K vectors of size N×K
    
    # thus, N is the number of basis vectors and coordinates in the span.
    # M is the number of dimensions of the space.
    # K is the number of vectors to reconstruct
    
    # normal to contravariant coordinates
    # def contravariant(a1, a2, a3, X):
    #     A_contra = np.array([a1, a2, a3]).T
    #     X_contra = np.linalg.solve(A_contra, X)
    #     return X_contra
    
    # The task is to reconstruct the vectors that are 
    # defined using these coordinates. 
    # The answer should be a matrix of shape K×M:
    """
    
    # Step 1: Reshape B to size (N, 1, M)
    B_reshaped = np.expand_dims(B, axis=1)
    
    # Step 2: Reshape C to size (N, K, 1)
    C_reshaped = np.expand_dims(C, axis=2)
    
    # Step 3: Multiply the reshaped arrays to get an array of size (N, K, M)
    intermediate_result = B_reshaped * C_reshaped
    
    # Step 4: Sum along the first axis to get the final result of size (K, M)
    reconstructed_vectors = np.sum(intermediate_result, axis=0)
    
    return reconstructed_vectors
    
    
    return 0
    
    


# In[4]:


import time

start = time.time()

debug_result = [vectors_from_contravariant_coords(**x) for x in debug_cases]
answer = [vectors_from_contravariant_coords(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

