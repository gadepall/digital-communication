import math
import random
import numpy as np
from scipy.stats import bernoulli

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

p = 0.02
n = 5
num_simulations = 100000
k=0
probability = bernoulli_probability(p, k, n)
print(f"Bernoulli probability: {probability:.8f}")
simulated_probability = simulate_bernoulli_trials(p, n, num_simulations, k)
print(f"Simulated probability: {simulated_probability:.8f}")
k=2
probability = bernoulli_probability(p, k, n)
print(f"Bernoulli probability: {probability:.8f}")
simulated_probability = simulate_bernoulli_trials(p, n, num_simulations, k)
print(f"Simulated probability: {simulated_probability:.8f}")
probability = bernoulli_probability(p, 0, n) + bernoulli_probability(p, 1, n)
print(f"Bernoulli probability: {probability:.8f}")
x = np.random.binomial(1, p, size=(num_simulations, n))
y = bernoulli.rvs(size=n, p=p)
successes_per_simulation = np.sum(x == y, axis=1)
success_count = np.sum(successes_per_simulation >= 2)
probability = success_count / num_simulations
print(f"Simulated probability: {probability:.8f}")
