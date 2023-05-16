import numpy as np
from scipy.stats import binom

# Set the number of trials (i.e., the number of times the die is thrown)
n = 2

# Set the number we're interested in (i.e., the number 5)
k = 5

# Set the probability of getting a 5 on a single throw of the die
p = 1/6

# Set the number of simulations
num_simulations = 100000

# Simulate rolling the die n times
rolls = np.random.randint(1, 7, size=(num_simulations, n))

# Calculate the number of times the number of interest appears in each simulation
counts = np.sum(rolls == k, axis=1)

# Calculate the probability of getting zero or one k in n throws of the die (theoretical solution)
p_not_k_theoretical = binom.pmf(0, n, p)
p_at_least_k_theoretical = 1 - binom.pmf(0, n, p)

# Calculate the probability of getting zero or one k in n throws of the die (simulated solution)
p_not_k_sim = np.mean(counts == 0)
p_at_least_k_sim = np.mean(counts >= 1)

# Print the results
print("Theoretical probability of not getting {} on any of the {} throws: {:.4f}".format(k, n, p_not_k_theoretical))
print("Simulated probability of not getting {} on any of the {} throws: {:.4f}".format(k, n, p_not_k_sim))
print()
print("Theoretical probability of getting {} on at least one of the {} throws: {:.4f}".format(k, n, p_at_least_k_theoretical))
print("Simulated probability of getting {} on at least one of the {} throws: {:.4f}".format(k, n, p_at_least_k_sim))

