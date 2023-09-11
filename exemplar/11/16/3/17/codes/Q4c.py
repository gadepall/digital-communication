from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

#Number of samples is 500, 1 denotes king/ 9 of hearts/ 3 of spades and 0 denotes otherwise
simlen=int(500)

#Probability of king/ 9 of hearts/ 3 of spades, i.e., X=1 is 0115
prob = 0.115

#Generating sample date using Bernoulli r.v.
X = bernoulli.rvs(size=simlen,p=prob)

#Calculating the number of favourable outcomes
num_card = np.nonzero(X == 1)

#calculating the probability
p_X = np.size(num_card)/simlen

#Total no. of king/ 9 of hearts/ 3 of spades

#Using simulation
num_card_sim=simlen*(p_X)

#Using exact probability
num_card_act=simlen*(prob)

#Theory vs simulation
print("Probability-simulation,actual:",p_X,prob)
print("No. of king/ 9 of hearts/ 3 of spades-simulation,actual:",num_card_sim,num_card_act)
print("Samples generated:",X)
