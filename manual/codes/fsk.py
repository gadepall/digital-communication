from __future__ import division
import numpy as np 
import matplotlib.pyplot as plt 
from scipy import special 
simlen=10000
i=np.random.randint(2,size=simlen)
k=np.pi/2
A=6

n1=np.random.normal(0,1,simlen)
n2=np.random.normal(0,1,simlen)

X=A*np.cos(k*i)+n1
Y=A*np.sin(k*i)+n2

plt.scatter(X,Y) 
plt.grid()
plt.show()			