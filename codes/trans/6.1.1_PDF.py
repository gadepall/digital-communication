#6.1.1 PDF
import numpy as np
import mpmath as mp
import scipy 
import matplotlib.pyplot as plt
from math import exp
#if using termux
import subprocess
import shlex
#end if


maxrange=50
maxlim=10
x = np.linspace(0,maxlim,maxrange)#points on the x axis
simlen = int(1e6) #number of samples
err = [] #declaring probability list
pdf = [] #declaring pdf list
h = 2*maxlim/(maxrange-1);
randvar1 = np.random.normal(0,1,simlen)
randvar2 = np.random.normal(0,1,simlen)

for i in range(0,maxrange):
	err_ind = np.nonzero((randvar1)**2 + (randvar2)**2 < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

	
for i in range(0,maxrange-1):
	test = (err[i+1]-err[i])/(x[i+1]-x[i])
	pdf.append(test) #storing the pdf values in a list

#def chi_pdf(x):
	#return exp(-x/2)/2
	
#vec_chi_pdf = scipy.vectorize(chi_pdf)

plt.plot(x.T[0:(maxrange-1)],pdf)
#plt.plot(x,vec_chi_pdf(x))#plotting the PDF
plt.grid() #creating the grid
plt.xlabel('$x_i$')
plt.ylabel('$p_V(x_i)$')
#plt.legend(["Numerical","Theory"])


plt.show() #opening the plot window
