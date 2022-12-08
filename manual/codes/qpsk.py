from __future__ import division 
import matplotlib.pyplot as plt 
import numpy as np 

simlen=10000

n1=np.random.normal(0,1,simlen)
n2=np.random.normal(0,1,simlen)
pie=np.pi/2
def uniform(x):
	return np.random.randint(4,size=x)

i=uniform(simlen)
x=[]
y=[]
A=5
for l in range(0,simlen):
	x.append(A*np.cos(pie*i[l]))
	y.append(A*np.sin(pie*i[l]))

X=x+n1
Y=y+n2

plt.scatter(X,Y)
plt.grid()
plt.show()