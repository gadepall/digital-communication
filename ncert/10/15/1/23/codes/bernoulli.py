#Code by Iqra Gilani
#November 18,2020
#Released under GNU/GPL

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

def count_consecutive_triplets_in_sets(arr):
    arr = np.array(arr)
    count = np.sum(np.all(arr.reshape(-1, 3) == arr.reshape(-1, 3)[:, 0:1], axis=1))
    return count

#Number of samples is 24, 1 denotes green marble and 0 denotes blue marble
simlen=int(9999)

#Probability of the event ball is green, i.e., X=1 is 2/3
prob = 1/2
actual_prob = 3/4

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#count
count = count_consecutive_triplets_in_sets(data_bern)
#print(count)
#Calculating the number of favourable outcomes
#err_ind = np.nonzero(data_bern == 1)
#calculating the probability
size = simlen/3
err_n = count/size
sim_prob = 1-err_n
#Total no. of blue marble
#Using simulation
#b_sim=simlen*(1-err_n)
#Using exact probability
#b_act=simlen*(1-prob)
#Theory vs simulation
print("Number of simulations carried out: ",size)
print("Probability-simulation,actual:",sim_prob,actual_prob)
#print("No. of blue marbles-simulation,actual:",b_sim,b_act)
print("Samples generated:",data_bern)
