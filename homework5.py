# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:17:09 2021

@author: Thanakorn
"""

import numpy as np
from scipy.linalg import solve
A = np.array([[0.5,0.2],
              [1,1]])
B = np.array([[10],[30]])
C = np.array([2,3])
X = solve(A,B)
print(X)
x = np.array([[13],[16]])
MAX = np.dot(C,x)
print(MAX)