# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 15:59:30 2021

@author: Thanakorn
"""
#Quiz14
import numpy as np
from scipy.linalg import solve
A = np.array([[1., 2.], [3., 4.]])
b = np.array([1., 4.])
x = solve(A, b)
print(x)