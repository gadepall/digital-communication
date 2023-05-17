import math
import numpy as np

def binomial_probability(n, k, p):
    binomial_coefficient = math.comb(n, k)
    probability = binomial_coefficient * (p ** k) * ((1 - p) ** (n - k))
    return probability

def simulate_binomial_probability(n, k, p, num_trials):
    random_samples = np.random.rand(num_trials, n)
    defective_counts = np.sum(random_samples < p, axis=1)
    successes = np.sum(defective_counts == k)
    probability = successes / num_trials
    return probability

# Parameters
n = 12  # Total sample size
k = 9   # Number of defective articles
p = 0.1 # Probability of an article being defective
num_trials = 100000000  # Number of simulation trials

# Calculate theoretical probability
theoretical_probability = binomial_probability(n, k, p)

# Run simulation
simulated_probability = simulate_binomial_probability(n, k, p, num_trials)

# Print the results
print("Theoretical probability:", "{:.8f}".format(theoretical_probability))
print("Simulated probability:", "{:.8f}".format(simulated_probability))


