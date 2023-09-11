from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

#Number of samples is 6000, 1 denotes atleast one head and 0 denotes both tails
simlen=int(500)

#Probability of atleast one head, i.e., X=1 is 0.5
prob = 0.75

#Generating sample date using Bernoulli r.v.
X = bernoulli.rvs(size=simlen,p=prob)

#Calculating the number of favourable outcomes
num_head = np.nonzero(X == 1)

#calculating the probability
p_X = np.size(num_head)/simlen

#Total no. of odd numbers

#Using simulation
num_head_sim=simlen*(p_X)

#Using exact probability
num_head_act=simlen*(prob)

#Theory vs simulation
print("Probability-simulation,actual:",p_X,prob)
print("No. of atleast one head-simulation,actual:",num_head_sim,num_head_act)
print("Samples generated:",X)
