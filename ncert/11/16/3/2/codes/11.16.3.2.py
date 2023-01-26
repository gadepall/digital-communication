import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#import seaborn as sns



#Simlen
simlen=4

#Number of hurdles
n =  2

#Probability of  clearing a hurdle
p = 1/2

#Theoretical probability of getting atleast one tail when a coin is tossed twice
k_values = list(range(n+1))
x = [binom.cdf(k, n, p) for k in k_values]
print(x)
y= [binom.pmf(k,n,p) for k in k_values]
plt.bar(k_values,y)
plt.show()

#Simulating the probability using  the binomial random variable
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of tossing a coin twice
err_ind = np.nonzero(data_binom >=1) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n)
print(err_n/simlen)
#print(data_binom)

#Simulating the probability using  the bernoulli random variable
data_bern_mat = bernoulli.rvs(p,size=(n,simlen))
data_binom=np.sum(data_bern_mat, axis=0)
#print(data_bern_mat)
#print(data_binom)
err_ind = np.nonzero(data_binom >=1) #checking probability condition
err_n = np.size(err_ind) #computing the probability
print(err_n)
print(err_n/simlen)
