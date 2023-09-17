import numpy as np

def mean(a,b):
	return a@b
def Ex2(a,b):
	a2=np.square(a)
	return a2@b
x=np.array([0,1,2,3,4,5])
px=np.array([1/6,5/18,2/9,1/6,1/9,1/18])

variance=Ex2(x,px)-(mean(x,px)*mean(x,px))
print("Variance of given distribution is",variance)
