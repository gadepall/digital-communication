from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

#Number of samples is 6000, 1 denotes that she bought the ticket and 0 denotes she didn't
simlen=int(6000)

#Probability of winning, i.e., X=1 is 0.08
prob = 0.08

#Generating sample date using Bernoulli r.v.
X = bernoulli.rvs(size=simlen,p=prob)

#Calculating the number of favourable outcomes
num_tickets = np.nonzero(X == 1)

#calculating the probability
p_X = np.size(num_tickets)/simlen

#Total no. of tickets bought

#Using simulation
num_tickets_sim=simlen*(p_X)

#Using exact probability
num_tickets_act=simlen*(prob)

#Theory vs simulation
print("Probability-simulation,actual:",p_X,prob)
print("No. of tickets bought-simulation,actual:",num_tickets_sim,num_tickets_act)
print("Samples generated:",X)
