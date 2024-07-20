#!/usr/bin/env python
# coding: utf-8

# In[2]:


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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/12. Neighbors Difference Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[15]:


import numpy as np

def diff(N):
    # Initialize an (N-1) x N matrix of zeros
    A = np.zeros((N-1, N))
    
    # Fill the matrix to compute differences of adjacent elements
    for i in range(N-1):
        A[i, i+1] = 1
        A[i, i] = -1
    
    return A


# In[16]:


import time

start = time.time()

debug_result = [diff(**x) for x in debug_cases]
answer = [diff(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




