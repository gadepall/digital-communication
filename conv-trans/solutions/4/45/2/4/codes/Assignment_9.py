#!/usr/bin/env python
# coding: utf-8

# In[2]:


#! /usr/bin/python3
import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

M = np.array([[1,0],[0,1],[-2,3]])
b = np.array([[1],[0],[2]])

#Singular Value Decomposition
U, s, V=LA.svd(M)

S = np.zeros(M.shape)
Sinv = S.T
S[:2,:2] = np.diag(s)
sinv = 1./s

#Moore Penrose Pseudo Inverse
Sinv[:2,:2] = np.diag(sinv)

#Solution
x = V.T.dot(Sinv).dot(U.T).dot(b)
print(x)


# In[ ]:




