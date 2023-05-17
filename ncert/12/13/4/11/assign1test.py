import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns

#Number of rolls
n =  2

#Probability of a six
p = 1/6

#k is the possible values of number of sixes per roll
k_values = list(range(n+1))

#y gives the probability values for each of the values of k
y = binom.pmf(k_values,n,p)

#Simulating the probability using the binomial random variable

simlen = 100000

data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of a die rolled 2 times and noting the number of sixes
fav_count=0
for i in range(n):#counting sixes
    fav_count = fav_count + np.count_nonzero(data_binom == i)*i 
print(fav_count/simlen)  #printing the average number of sixes