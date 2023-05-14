import numpy as np

# Set the seed for reproducibility
np.random.seed(42)

# Define the number of bulbs and the number of defective bulbs
num_bulbs = 100
num_defective = 10

# Define the sample size and the number of simulations
sample_size = 5
num_simulations = 100000
tolerance = 0.01

# Simulate drawing samples and count the number of times all samples are non-defective
count = 0
for i in range(num_simulations):
    sample = np.random.choice(num_bulbs, sample_size, replace=False)
    if all(sample >= num_defective):
        count += 1

# Calculate the empirical probability of all samples being non-defective
empirical_prob = count / num_simulations

print("Empirical probability:", empirical_prob)
if abs(empirical_prob - 0.59) <= tolerance:
  print("solution is correct")
