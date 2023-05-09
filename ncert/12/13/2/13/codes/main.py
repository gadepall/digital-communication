import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

#Simlen
simlen=10000

#Number of trials
n =  2

#Probability of success
p = 4/9

#Mean 
mu = p

#Variance
sigma = np.sqrt(p*(1-p))


#Theoretical probability of getting both red balls
k = 2
print("Theoretical probability of getting both red balls:  ",binom.pmf(k, n, p))
#Theoretical probability of getting one red ball and one black ball
k = 1
print("Theoretical probability of getting one red ball and one black ball:  ",binom.pmf(k, n, p))


#Simulating ball draws using the Binomial Random Variable
print("--Simulating ball draws using Binomial Random Variable--")
data_binom = binom.rvs(n,p,size=simlen) 

#Checking Probability
k = 2
err_ind2 = np.nonzero(data_binom == k) 
k = 1
err_ind1 = np.nonzero(data_binom == k) 


#Finding probability values
err_n2 = np.size(err_ind2) 
print( "Observed probability of getting both red balls:  ", err_n2/simlen)
err_n1 = np.size(err_ind1) 
print( "Observed probability of getting one red ball and one black ball:  ", err_n1/simlen)


redBalls,values = np.unique(data_binom , return_counts=True)
value = values/simlen


#Using matplotlib
plt.xlabel("Number of Red balls")
plt.ylabel("PMF")
ax=plt.gca()
ax.locator_params('y', nbins=15)
ax.locator_params('x', nbins=3)
plt.stem(redBalls, value, linefmt='g-', markerfmt='ro', label = "Observed")
plt.plot(redBalls , np.array(binom.pmf(redBalls , n , p)) , 'bo' , label = "Theoretical")
plt.legend()
plt.show()
