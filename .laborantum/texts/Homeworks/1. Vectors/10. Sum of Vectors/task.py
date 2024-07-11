#!/usr/bin/env python
# coding: utf-8

# In[4]:


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


# In[5]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/1. Vectors/10. Sum of Vectors')


# In[6]:


debug_cases = json_tricks.load(str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(str(path / 'testcases' / 'public_cases.json'))


# In[9]:


import numpy as np

def vector_sum(x, y):
    

    res = []
    
    for i in range(len(x)):
        res.append(x[i] + y[i])
        
    res = np.array(res)
    
    return res


# In[10]:


import time

start = time.time()

debug_result = [vector_sum(**x) for x in debug_cases]
answer = [vector_sum(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

