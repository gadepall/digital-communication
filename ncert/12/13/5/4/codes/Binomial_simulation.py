import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom

#Simlen
simlen=10000

#Number of trials
n = 5

#Probability of  getting a spade
p = 1/4

#Mean 
mu = p

#Variance
sigma = np.sqrt(p*(1-p))

# (i) Theoretical probability of getting all 5 spades
k = 5
print("Theoretical probability of getting all 5 spades", binom.pmf(k, n, p))

# (ii) Theoretical probability of getting 3 spades
k = 3
print("Theoretical probability of getting 3 spades", binom.pmf(k, n, p))

# (iii) Theoretical probability of getting no spades
k = 0
print("Theoretical probability of getting no spades" ,binom.pmf(k, n, p))





#Simulating the probability using  the binomial random variable
print("Simulate using binomial random variable")
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of getting spades

#checking probability condition
k = 5
err_ind5 = np.nonzero(data_binom ==k) 
k  =3
err_ind3 = np.nonzero(data_binom ==k) 
k = 0
err_ind0 = np.nonzero(data_binom ==k) 


#computing the probability
err_n5 = np.size(err_ind5) 
print( "Probability of getting 5 spades is:", err_n5/simlen)
err_n3 = np.size(err_ind3) 
print( "Probability of getting 3 spades is:", err_n3/simlen)
err_n0 = np.size(err_ind0) 
print( "Probability of getting 0 spades is:", err_n0/simlen)


spades,values = np.unique(data_binom , return_counts=True)
values = values/simlen


#plotting pmfs using matplotlib
plt.figure(figsize = (16 ,10))
plt.xlabel("Number of spades")
plt.ylabel("PMF")
plt.ylim(0 , 0.45)
plt.xlim(-0.5 , 6)
ax=plt.gca()
# adjust the y axis scale.
ax.locator_params('y', nbins=20)
plt.stem(spades, values, linefmt='b-', markerfmt='ro', label = "Observation")
plt.plot(spades , np.array(binom.pmf(spades , n , p)) , 'go' , label = "Theoretical")
plt.legend()
plt.show()
