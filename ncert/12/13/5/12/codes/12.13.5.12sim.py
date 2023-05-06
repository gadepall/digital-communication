import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns
#Number of rolls
n = 6  
#Probability of a six
p = 1/6
#k is the possible number of the sixes
k_values = list(range(n+1))
#y gives the probability values for each of the values of k
y = binom.pmf(k_values,n,p)
z=y[0]+y[1]+y[2]
print(z)   #printing the probability of the number of sixes being atmost 2
#Simulating the probability using the binomial random variable
simlen = 10000
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of a die rolled 6 times and noting the number of sixes
total_count = np.count_nonzero(data_binom <= 2)  #Finding the number of times there are atmost two sixes in the simulation data
print(total_count/simlen)  #printing the probability of there being atmost two sixes in the 6 rolls based on the simulation


