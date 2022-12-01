#Importing numpy, scipy, mpmath and pyplot
#6.1.2
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,20,50)#points on the x axis
simlen = int(1e7) #number of samples
err = [] #declaring probability list
randvar1 = np.random.normal(0,1,simlen)
randvar2= np.random.normal (0,1,simlen)
for i in range(0,50):
	err_ind = np.nonzero((randvar1)**2+(randvar2)**2 < x[i]) #checking probability condition
	err_n = np.size(err_ind) #computing the probability
	err.append(err_n/simlen) #storing the probability values in a list

def chi_cdf_ahalf(x): # if alpha=0.5
  return 1-exp(-(x/2))
def chi_cdf_a1(x):  #if alpha=1
  return 1-exp(-(x))
def chi_cdf_a2(x):   #if alpha=2
  return 1-exp(-2*(x))


vec_chi_ahalf=scipy.vectorize(chi_cdf_ahalf)
vec_chi_a1=scipy.vectorize(chi_cdf_a1)	
vec_chi_a2=scipy.vectorize(chi_cdf_a2)		
plt.plot(x.T, err ,marker='o')#plotting the CDF
plt.plot(x,vec_chi_ahalf(x),'r',marker='x')
plt.plot(x,vec_chi_a1(x),'m')
plt.plot(x,vec_chi_a2(x))
plt.grid() #creating the grid
plt.xlabel('$x$')
plt.ylabel('$F_V(x)$')
plt.legend(['simulated' , 'alpha=half','alpha=1','alpha=2'])
plt.show()