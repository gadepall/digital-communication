import numpy as np
from scipy.stats import bernoulli

# Number of simulations
num_simulations = 100000

# Simulate the process num_simulations times
coin_tosses = bernoulli.rvs(0.5, size=(num_simulations, 3))

# Count the number of tails for each simulation
num_tails = np.sum(coin_tosses, axis=1)

# Calculate the variance
variance = np.var(num_tails, ddof=1)

# Calculate the simulated standard deviation
simulated_std_deviation = np.sqrt(variance)

# Calculate the theoretical standard deviation
theoretical_std_deviation = np.sqrt(0.5 * 0.5 * 3)

# Print the results
print(f"Simulated Standard Deviation: {simulated_std_deviation:.6f}")
print(f"Theoretical Standard Deviation: {theoretical_std_deviation:.6f}")


