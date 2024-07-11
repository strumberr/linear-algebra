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

path = Path(".laborantum/texts/Homeworks/3. Matrices/14. Diagonal Matrices Product")

debug_cases = json_tricks.load(
    str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(
    str(path / 'testcases' / 'public_cases.json'))


# In[6]:


import numpy as np

def DA_AD_product(D, A):

    res = {
        'DA': 0,
        'AD': 0
    }
    
    # Calculate DA: each row i of A is scaled by D[i]
    DA = (D[:, np.newaxis] * A)
    # Calculate AD: each column j of A is scaled by D[j]
    AD = (A * D[np.newaxis, :])
    
    res['DA'] = DA
    res['AD'] = AD
    
    print(res)
    
    return res


# In[7]:


import time

start = time.time()

debug_result = [DA_AD_product(**x) for x in debug_cases]
answer = [DA_AD_product(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')


# In[ ]:




