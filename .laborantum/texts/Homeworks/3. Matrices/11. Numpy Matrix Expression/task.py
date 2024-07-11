#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('reload_ext', 'autoreload')
get_ipython().run_line_magic('autoreload', '2')

import sys
import os
from pathlib import Path
import json_tricks

path = Path('.').resolve()

index = str(path).find('.laborantum')

if index > 0:
    path = str(path)[:index]

os.chdir(path)

path = Path('.laborantum/texts/Homeworks/3. Matrices/11. Numpy Matrix Expression')

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[2]:


import numpy as np

def formula(A, B, C, x):

    print(f"matrix A: {A.shape}")
    print(f"matrix B: {B.shape}")
    print(f"matrix C: {C.shape}")
    print(f"vector x: {x.shape}")
    

    BC = B + (2 * C)
    
    AT_BC = A.T @ BC
    
    I = np.eye(AT_BC.shape[0])

    print(AT_BC.shape)
    print(I)
    
    d = AT_BC + 3 * I
    
    e = np.exp(d)
    f = np.dot(e, x)
    
    print(f)
    
    return f


# In[3]:


import time

start = time.time()

debug_result = [formula(**x) for x in debug_cases]
answer = [formula(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




