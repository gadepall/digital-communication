from scipy.stats import bernoulli
import numpy as np
import matplotlib.pyplot as plt

simlen = int(10000)

#For X=1
#Probability of X=1 is 0.1
prob1 = 0.1
#Generating sample date using Bernoulli r.v.
W = bernoulli.rvs(size=simlen,p=prob1)

#For X=2
#Probability of X=2
prob2 = 0.2
#Generating sample date using Bernoulli r.v.
X = bernoulli.rvs(size=simlen,p=prob2)

#For X=3
#Probability of X=3
prob3 = 0.3
#Generating sample date using Bernoulli r.v.
Y = bernoulli.rvs(size=simlen,p=prob3)

#For X=4
#Probability of X=4
prob4 = 0.4
#Generating sample date using Bernoulli r.v.
Z = bernoulli.rvs(size=simlen,p=prob4)

#simlen = simlen1 + simlen2 + simlen3 + simlen4
#A = np.append(W, X, Y, Z)

#Calculating the number of favourable outcomes
num_fav_W = np.nonzero(W == 1)
num_fav_X = np.nonzero(X == 1)
num_fav_Y = np.nonzero(Y == 1)
num_fav_Z = np.nonzero(Z == 1)

#calculating the probability
p_W = np.size(num_fav_W)/simlen
p_X = np.size(num_fav_X)/simlen
p_Y = np.size(num_fav_Y)/simlen
p_Z = np.size(num_fav_Z)/simlen

#Calculating Theoretical expactance
values = np.array([1, 2, 3, 4])
probabilities = np.array([0.1, 0.2, 0.3, 0.4])

expectance = np.sum(values**2 * probabilities)

#Calculating experimental expactance
probabilities_exp = np.array([p_W, p_X, p_Y, p_Z])

expectance_exp = np.sum(values**2 * probabilities_exp)

#Theory vs simulation
print("Probability for X=1 -simulation,actual:",p_W,prob1)
print("Probability for X=2 -simulation,actual:",p_X,prob2)
print("Probability for X=3 -simulation,actual:",p_Y,prob3)
print("Probability for X=4 -simulation,actual:",p_Z,prob4)
print("E[X^2] -simulation,actual:", expectance_exp,expectance)

print("Samples generated for X=1 :",W)
print("Samples generated for X=2 :",X)
print("Samples generated for X=3 :",Y)
print("Samples generated for X=4 :",Z)
