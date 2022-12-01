import numpy as np
from numpy.linalg import inv
from numpy import linalg as LA

M = np.array([[1,0],[0,1],[1/2,1/3]])
b = np.array([[-3],[2],[1]])

#Singular Value Decomposition
U, s, V=LA.svd(M)

# Diagonalizing S
S = np.zeros(M.shape)
Sinv = S.T
S[:2,:2] = np.diag(s)
sinv = 1./s

#Inverse transpose of S (Moore Penrose Pseudo Inverse)
Sinv[:2,:2] = np.diag(sinv)

#Solution
x = V.T.dot(Sinv).dot(U.T).dot(b)
print(x)