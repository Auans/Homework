# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 12:17:09 2021

@author: Thanakorn
"""

import numpy as np
from scipy.optimize import linprog
A = np.array([[0.5,0.2],
              [1,1]])
B = np.array([[10],[30]])
C = np.array([2,3])
#linprog() solves only minimization (not maximization). So convert C into -C
C2 = -C
bnd = [(0, float("inf")),  
      (0, float("inf"))]

opt = linprog(c=C2, A_ub=A, b_ub=B,bounds=bnd, method="revised simplex")
print(opt)
print("X1, X2 =", opt.x)
MAX = np.dot(opt.x, C)
print("the maximum profit is $",MAX)
