#Code by Iqra Gilani
#November 18,2020
#Released under GNU/GPL

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#Number of samples is 24, 1 denotes green marble and 0 denotes blue marble
simlen=int(24)

#Probability of the event ball is green, i.e., X=1 is 2/3
prob = 2/3

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability
err_n = np.size(err_ind)/simlen
#Total no. of blue marble
#Using simulation
b_sim=simlen*(1-err_n)
#Using exact probability
b_act=simlen*(1-prob)
#Theory vs simulation
print("Probability-simulation,actual:",err_n,prob)
print("No. of blue marbles-simulation,actual:",b_sim,b_act)
print("Samples generated:",data_bern)
