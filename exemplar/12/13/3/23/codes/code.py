import math
import random
import numpy as np

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

p = 0.1
n = 8
k = 0
num_simulations = 15000000

probability = bernoulli_probability(p, k, n)
print("Bernoulli probability: ", 1.0-probability)

simulated_probability = simulate_bernoulli_trials(p, n, num_simulations, k)
print("Simulated probability: ", 1-simulated_probability)
