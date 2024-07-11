#!/usr/bin/env python
# coding: utf-8

# In[2]:


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


# In[4]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/2. Vector Spaces/6. Linear Independency Task')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[7]:


import numpy as np

def project(u, v):
    return np.dot(u, v) / np.dot(v, v) * v

def gram_schmidt(input_vectors):
    
    orthogonal_basis = []
    
    for vector in input_vectors:
        
        temp_vector = vector
        
        for basis_vector in orthogonal_basis:
            temp_vector = temp_vector - project(vector, basis_vector)
            
        if np.linalg.norm(temp_vector) > 1e-6:
            temp_vector = temp_vector / np.linalg.norm(temp_vector)
            orthogonal_basis.append(temp_vector)
    
    return orthogonal_basis


def is_independent(A):
    
    GS = gram_schmidt(A)
    
    if len(GS) < len(A):
        return False
    
    return True


# In[8]:


import time

start = time.time()

debug_result = [is_independent(**x) for x in debug_cases]
answer = [is_independent(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

