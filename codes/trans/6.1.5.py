#6.1.5 PDF
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
from math import exp
from math import sqrt
#if using termux
import subprocess
import shlex
#end if


maxrange=100
maxlim=10
x = np.linspace(0,maxlim,maxrange)#points on the x axis
simlen = int(1e7) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
randvar1 = np.random.normal(0,1,simlen)
randvar2 = np.random.normal(0,1,simlen)
sr=[]
for g in range(simlen):
  sr.append(sqrt(randvar1[g]**2 +randvar2[g]**2))

for i in range(0,maxrange):
	err_ind = np.nonzero(sr < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

def chi_pdf(x):
	return x*exp(-x**2/2)
	
vec_chi_pdf = scipy.vectorize(chi_pdf)

plt.plot(x.T[0:(maxrange-1)],pdf)
plt.plot(x,vec_chi_pdf(x),marker='o')#plotting the PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_A(x_i)$')
plt.legend(["Simulation","Theory"])


plt.show() #opening the plot window