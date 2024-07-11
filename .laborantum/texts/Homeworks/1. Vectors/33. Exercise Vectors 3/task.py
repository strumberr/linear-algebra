#!/usr/bin/env python
# coding: utf-8

# In[3]:


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

# !{sys.executable} -m pip -q install numpy json-tricks torch jupyter nbconvert


# In[4]:


import json_tricks

path = Path('.laborantum/texts/Homeworks/1. Vectors/33. Exercise Vectors 3')


# In[5]:


debug_cases = json_tricks.load(str(path / 'testcases' / 'debug_cases.json'))
public_cases = json_tricks.load(str(path / 'testcases' / 'public_cases.json'))


# In[6]:


import numpy as np
import math as m
import numpy.typing as npt
from typing import Dict

# functions for use later
def dot_product(x, y):
    dot_prod = 0
    for a_val, b_val in zip(x, y):
        dot_prod += a_val * b_val
    return dot_prod

def cos(a, b):
    dot_prod = dot_product(a, b)
    magnitude_a = m.sqrt(sum([val ** 2 for val in a]))
    magnitude_b = m.sqrt(sum([val ** 2 for val in b]))
    return float(dot_prod / (magnitude_a * magnitude_b))

def magnitude(x):
    return m.sqrt(sum([val ** 2 for val in x]))

def vector_direction(x):
    magnitude_x = magnitude(x)
    direction = []
    for x_val in x:
        direction.append(x_val / magnitude_x)
    return direction

def projection(x, y):
    return dot_product(x, y) / dot_product(y, y) * y

def orthogonal(x, y):
    return x - projection(x, y)


def vector_operations(x, y):

    answer = {
        'expression': 1,
        'dot_prod': 1,
        'length_a': 1,
        'length_b': 1,
        'angle': 1,
        'dir_a': 1,
        'dir_b': 1,
        'a_proj_b': 1,
        'b_proj_a': 1,
        'a_orth_b': 1,
        'b_orth_a': 1
    }
        
        
    a = np.array(x)
    b = np.array(y)


    # 1
    expression = []
    for a_comp, b_comp in zip(a, b):
        res = 2 * a_comp + b_comp
        expression.append(res)
    answer['expression'] = expression

    # 2
    answer['dot_prod'] = dot_product(a, b)

    # 3
    length_a = m.sqrt(sum([val ** 2 for val in a]))
    length_b = m.sqrt(sum([val ** 2 for val in b]))
    answer['length_a'] = length_a
    answer['length_b'] = length_b

    # 4
    answer['angle'] = cos(a, b)

    # 5
    answer['dir_a'] = vector_direction(a)
    answer['dir_b'] = vector_direction(b)

    # 6
    answer['a_proj_b'] = projection(a, b)
    answer['b_proj_a'] = projection(b, a)

    # 7
    answer['a_orth_b'] = orthogonal(a, b)
    answer['b_orth_a'] = orthogonal(b, a)


    print(answer)

    return np.array[answer['expression'], answer['dot_prod'], answer['length_a'], answer['length_b'], answer['angle'], answer['dir_a'], answer['dir_b'], answer['a_proj_b'], answer['b_proj_a'], answer['a_orth_b'], answer['b_orth_a']]


# In[7]:


import time

start = time.time()

debug_result = [vector_operations(**x) for x in debug_cases]
answer = [vector_operations(**x) for x in public_cases]

print(time.time() - start, '<- Elapsed time')

