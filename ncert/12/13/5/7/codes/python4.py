import numpy as np

# n denotes number of questions
n = 20

# p denotes probability of answering correctly
p = 0.5

trials = 1000000

# simulate binomial distribution
simulations = np.random.binomial(n,p,trials)

# calulatiing probability of X>= 12
prob = np.sum(simulations >=12)/trials

print('Probability :',prob)









