import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns

#Number of rolls
n =  7

#Probability of getting 5
p = 1/6

#Simulating the probability using the binomial random variable

simlen = 10000000

data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of a die rolled 7 times and noting the number of times getting 5 twice

fav_count = np.count_nonzero(data_binom == 2)  #Finding the number of times there are two fives  in the simulation data

print(fav_count/simlen)  #printing the probability of there being two fives in the 7 rolls based on the simulation
