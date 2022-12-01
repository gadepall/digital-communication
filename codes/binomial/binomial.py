#Code by GVV Sharma
#November 20,2020
#Released under GNU/GPL
#To find the probability of an event using the binomial distribution

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom




#Simlen
simlen=1000

#Number of hurdles
n =  10

#Probability of  clearing a hurdle
p = 1-5/6

#Mean 
mu = p

#Variance
sigma = np.sqrt(p*(1-p))

#Theoretical probability of knocking down fewer than 2 hurdles
k = 1
print(binom.cdf(k, n, p),3*(5/6)**10)

#Using the Gaussian approximation for the binomial pdf
print(1/(sigma*np.sqrt(n))*(norm.pdf((k-n*mu)/(sigma*np.sqrt(n)))+norm.pdf((k-1-n*mu)/(sigma*np.sqrt(n)))))


#Simulating the probability using  the binomial random variable
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of jumping 10 hurdles
err_ind = np.nonzero(data_binom <=k) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n/simlen)
#print(data_binom)


#Simulating the probability using  the bernoulli random variable
data_bern_mat = bernoulli.rvs(p,size=(n,simlen))
data_binom=np.sum(data_bern_mat, axis=0)
#print(data_bern_mat)
#print(data_binom)
err_ind = np.nonzero(data_binom <=k) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n/simlen)

