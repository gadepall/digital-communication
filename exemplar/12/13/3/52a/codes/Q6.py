from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

#Number of samples is 9999, 0 denotes atleast one head and 1 denotes both tails
prob = 0.738

#For fair coin
simlen1 = int(5000)

#Probability of head, i.e., X=0 is 0.5
prob1 = 0.5

#Generating sample date using Bernoulli r.v.
X = bernoulli.rvs(size=simlen1,p=prob1)

#For unfair coin
simlen2=int(4999)

#Probability of head, i.e., X=0 is 1
prob2 = 1

#Generating sample date using Bernoulli r.v.
Y = bernoulli.rvs(size=simlen2,p=prob2)

simlen = simlen1 + simlen2
Z = np.append(X, Y)

#Calculating the number of favourable outcomes
num_head = np.nonzero(Z == 1)

#calculating the probability
p_Z = np.size(num_head)/simlen

#Total no. of heads

#Using simulation
num_head_sim=simlen*(p_Z)

#Using exact probability
num_head_act=simlen*(prob)

#Theory vs simulation
print("Probability-simulation,actual:",p_Z,prob)
print("No. of heads-simulation,actual:",num_head_sim,num_head_act)
print("Samples generated:",Z)
