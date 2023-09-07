import numpy as np

# Parameters
num_simulations = 100000  # Number of simulations
num_trials = 6
p_success = 2/3

# Simulate Bernoulli trials
simulations = np.random.choice([0, 1], size=(num_simulations, num_trials), p=[1-p_success, p_success])

# Count the number of successes in each simulation
num_successes = np.sum(simulations, axis=1)

# Calculate the probability of at least 4 successes
at_least_4_successes = np.sum(num_successes >= 4) / num_simulations

print("Simulated probability of at least 4 successes:", at_least_4_successes)

