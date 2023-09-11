from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

#Number of samples is 6000, 1 denotes odd number and 0 denotes even number
simlen=int(500)

#Probability of odd number, i.e., X=1 is 0.5
prob = 0.5

#Generating sample date using Bernoulli r.v.
X = bernoulli.rvs(size=simlen,p=prob)

#Calculating the number of favourable outcomes
num_odd = np.nonzero(X == 1)

#calculating the probability
p_X = np.size(num_odd)/simlen

#Total no. of odd numbers

#Using simulation
num_odd_sim=simlen*(p_X)

#Using exact probability
num_odd_act=simlen*(prob)

#Theory vs simulation
print("Probability-simulation,actual:",p_X,prob)
print("No. of odd numbers-simulation,actual:",num_odd_sim,num_odd_act)
print("Samples generated:",X)
