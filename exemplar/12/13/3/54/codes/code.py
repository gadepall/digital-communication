import math
import random
import numpy as np
from statistics import variance

def bernoulli_probability(p, k, n):
    binomial_coefficient = math.comb(n, k)
    probability = binomial_coefficient *  (p**k) * ((1-p)**(n - k))
    return probability

def simulate_bernoulli_trials(p, n, num_simulations, k):
    trials_matrix = np.random.random((num_simulations, n)) < p
    successes_per_simulation = np.sum(trials_matrix, axis=1)
    success_count = np.count_nonzero(successes_per_simulation == k)
    
    proportion_successful = success_count / num_simulations
    return proportion_successful

p = 0.5
n = 2
k1 = 0
k2 = 1
k3 = 2
num_simulations = 15000000
X = np.array(range(n+1))

p1 = bernoulli_probability(p, k1, n)
p2 = bernoulli_probability(p, k2, n)
p3 = bernoulli_probability(p, k3, n)
P = np.array([p1,p2,p3])

sp1= simulate_bernoulli_trials(p, n, num_simulations, k1)
sp2= simulate_bernoulli_trials(p, n, num_simulations, k2)
sp3= simulate_bernoulli_trials(p, n, num_simulations, k3)
sP = np.array([sp1,sp2,sp3])

var = 3*variance(X*P)
svar =  3*variance(X*sP)

print("Actual variancs: ",var)
print("Simulated variance: ", svar)
