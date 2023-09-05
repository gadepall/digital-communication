import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
n=10
simlen=int(1e2)

#Probability of the event
prob=0.05
#Generating sample date using Bernoulli r.v.
data_bernoulli = bernoulli.rvs(prob,size=(n,simlen))
data_binom=np.sum(data_bernoulli, axis=0)
print(data_binom)
err_ind = np.nonzero(data_binom <=1) #checking probability condition of not more than 1 defective item
err_n = np.size(err_ind) #computing the probability
print("the practical probability of not more than 1 defective item is",err_n/simlen)
print()
 	
# using binomial to calculate theoretical probability 

# Parameters for the binomial distribution
n = 10 # Number of trials
p = 0.05  # Probability of success in each trial

#k is the possible number of defective items
k_values = list(range(n+1))
#y gives the probability values for each of the values of k
y = binom.pmf(k_values,n,p)
z=y[0]+y[1] #the probability of the number of defective item being atmost 1
print("the probability calculated using the binomial distribution is",z)
