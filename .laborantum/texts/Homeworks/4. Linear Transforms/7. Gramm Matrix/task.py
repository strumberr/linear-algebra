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

path = Path(".laborantum/texts/Homeworks/4. Linear Transforms/7. Gramm Matrix")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[2]:


import numpy as np

def contra_to_co(B, x):
   
    # B are basis vectors
    # x is a vector in contra-variant basis
    # return x in co-variant basis
    
    res = []
    
    for el in B:
        # dot product of el and x:
        dot = np.dot(el, x)
        res.append(dot)
    
    return np.array(res)




# In[3]:


import time

start = time.time()

debug_result = [contra_to_co(**x) for x in debug_cases]
answer = [contra_to_co(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:





# In[ ]:




