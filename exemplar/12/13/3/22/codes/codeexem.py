import math
import random
import numpy as np

def bernoulli_probability(p, k, n):
    binomial_coefficient = math.comb(n, k)
    probability = binomial_coefficient *  (p ** k) * ((1-p) ** (n - k))
    return probability

def simulate_bernoulli_trials(p, n, num_simulations, k):
    trials_matrix = np.random.random((num_simulations, n)) < p
    successes_per_simulation = np.sum(trials_matrix, axis=1)
    success_count = np.count_nonzero(successes_per_simulation == k)
    
    proportion_successful = success_count / num_simulations
    return proportion_successful

p = 0.25
n = 7
k1 = 0
k2 = 1
num_simulations = 15000000

prob1 = bernoulli_probability(p, k1, n)
prob2 = bernoulli_probability(p, k2, n)
print(f"Bernoulli probability: {1 - prob1 - prob2:.8f}")

simulated_probability1 = simulate_bernoulli_trials(p, n, num_simulations, k1)
simulated_probability2 = simulate_bernoulli_trials(p, n, num_simulations, k2)
print(f"Simulated probability: {1 - simulated_probability1 - simulated_probability2:.8f}")
