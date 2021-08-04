# -*- coding: utf-8 -*-
"""
Created on Wed Aug  4 21:15:24 2021

@author: Thanakorn
"""
#Quiz16
import numpy as np
m = int(input("m is "))
n = int(input("n is "))
x = np.array([])

for i in range(m):
  for j in range(n):
    if i < j and j != m:
      y = 0
    elif i ==j or j ==m:
      y = 1
    else:
      y = -1
    x = np.append(x,y)
z = np.reshape(x ,(m,n))    
print(z)