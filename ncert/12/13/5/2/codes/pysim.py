import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns

#Number of rolls
n =  4

#Probability of a doublet
p = 1/6

#k is the possible values of the doublets
k_values = list(range(n+1))

#y gives the probability values for each of the values of k
y = binom.pmf(k_values,n,p)

print(y[2])   #printing the probability of the number of doublets being 2


#Simulating the probability using the binomial random variable

simlen = 10000

data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of a die rolled 4 times and noting the number of doublets

fav_count = np.count_nonzero(data_binom == 2)  #Finding the number of times there are two doublets in the simulation data

print(fav_count/simlen)  #printing the probability of there being two doublets in the 4 rolls based on the simulation
