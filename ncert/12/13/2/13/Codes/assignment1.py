import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli
from scipy.stats import norm
from scipy.stats import binom
#Simlen
simlen=10000000
#Number of hurdles
n = 2
#Probability of clearing a hurdle
p='4/9'        #probability of success
p=Fraction(p)  #change the type of x from string to Fraction
p=float(p)     #change the type of x from Fraction to float
# Simulating the probability using the binomial random variable
data_binom = binom.rvs(n,p,size=simlen) #Simulating the event of jumping 10 hurdles
err_ind2, err_ind1 = np.nonzero(data_binom == 2), np.nonzero(data_binom == 1) #checking probability condition
err_n2, err_n1 = np.size(err_ind2), np.size(err_ind1) #computing the probability
print(f"P(X=2) = {err_n2/simlen}, P(X=1) = {err_n1/simlen}")
